"""
Offline construction cost estimator for the DDC CWICR dataset.

Works entirely against a local Parquet file - no Qdrant, no OpenAI or
Anthropic API key, no network access. Matches work items by exact
rate_code or by case-insensitive substring search on the item name, and
prices a bill of quantities (BOQ) from the local data.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("pandas and pyarrow are required. Install with: pip install pandas pyarrow")

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_PATH = (
    REPO_ROOT / "CIS-Russia-GESN-FER-TER" / "EN___DDC_CWICR"
    / "ENG_TORONTO_workitems_costs_resources_DDC_CWICR.parquet"
)

# Column names differ slightly between tracks/schema versions - try each
# candidate in order and use the first one present in the file.
NAME_COL_CANDIDATES = ["rate_final_name", "rate_original_name"]
UNIT_COL_CANDIDATES = ["rate_unit_of_measure", "rate_unit"]
COST_COL_CANDIDATES = {
    "total": ["total_cost_per_position"],
    "material": ["total_material_cost_per_position", "total_material_cost"],
    "labor_resource": ["total_resource_cost_per_position", "total_labor_cost"],
    "equipment": ["total_value_machinery_equipment", "total_machinery_cost"],
}


def _first_present(df: pd.DataFrame, candidates: list[str]) -> str | None:
    return next((c for c in candidates if c in df.columns), None)


_UNIT_MULTIPLIER_RE = re.compile(r"^\s*(\d+(?:\.\d+)?)\s+(.+?)\s*$")


def parse_rate_unit(unit: str) -> tuple[float, str]:
    """Split a rate_unit like "100 m2" into (multiplier=100, base_unit="m2").

    Many DDC CWICR items are priced per a block of units (e.g. per 100 m2,
    per 1000 m3, per 10 pcs) rather than per single unit - the multiplier is
    baked into the unit string. Units with no leading number (e.g. "t",
    "pcs", "km of track") have multiplier 1.
    """
    if not isinstance(unit, str):
        return 1.0, str(unit)
    m = _UNIT_MULTIPLIER_RE.match(unit)
    if not m:
        return 1.0, unit
    return float(m.group(1)), m.group(2)


def load_workitems(path: Path) -> pd.DataFrame:
    """Load a DDC CWICR Parquet file and collapse it to one row per work item.

    The raw dataset stores one row per (work item x resource/scope line), so
    cost columns repeat across every row of the same rate_code. Dedup on
    rate_code to get a clean work-item catalog.
    """
    df = pd.read_parquet(path)

    name_col = _first_present(df, NAME_COL_CANDIDATES)
    if name_col is None:
        sys.exit(f"None of {NAME_COL_CANDIDATES} found in {path}")
    unit_col = _first_present(df, UNIT_COL_CANDIDATES)
    total_col = _first_present(df, COST_COL_CANDIDATES["total"])
    if total_col is None:
        sys.exit(f"None of {COST_COL_CANDIDATES['total']} found in {path}")

    items = df.drop_duplicates(subset="rate_code", keep="first").copy()
    items["_name"] = items[name_col]
    items["_packaged_unit"] = items[unit_col] if unit_col else ""

    # rate_unit often bakes in a block multiplier (e.g. "100 m2" = priced
    # per 100 m2). Normalize everything to a per-single-unit rate so BOQ
    # quantities (in plain m2/m3/pcs/...) price correctly.
    parsed = items["_packaged_unit"].apply(parse_rate_unit)
    items["_unit_multiplier"] = parsed.apply(lambda t: t[0])
    items["_unit"] = parsed.apply(lambda t: t[1])

    items["_total"] = items[total_col] / items["_unit_multiplier"]
    for key in ("material", "labor_resource", "equipment"):
        col = _first_present(df, COST_COL_CANDIDATES[key])
        raw = items[col] if col else 0.0
        items[f"_{key}"] = raw / items["_unit_multiplier"] if col else 0.0

    return items.set_index("rate_code", drop=False)


def search(items: pd.DataFrame, query: str, limit: int = 10) -> pd.DataFrame:
    mask = items["_name"].str.contains(query, case=False, na=False)
    return items[mask].head(limit)


def resolve_item(items: pd.DataFrame, token: str) -> pd.Series | None:
    """Resolve a BOQ line's item token: exact rate_code match first, else best text-search hit."""
    if token in items.index:
        row = items.loc[token]
        return row.iloc[0] if isinstance(row, pd.DataFrame) else row
    matches = search(items, token, limit=1)
    return None if matches.empty else matches.iloc[0]


def estimate(items: pd.DataFrame, lines: list[tuple[str, float, str | None]]) -> list[dict]:
    rows = []
    for token, qty, unit_override in lines:
        row = resolve_item(items, token)
        if row is None:
            rows.append({
                "query": token, "matched_code": None, "matched_name": "NO MATCH",
                "quantity": qty, "unit": unit_override or "",
                "unit_rate": 0.0, "amount": 0.0,
                "material": 0.0, "labor_resource": 0.0, "equipment": 0.0,
            })
            continue

        unit_rate = float(row["_total"] or 0)
        rows.append({
            "query": token,
            "matched_code": row["rate_code"],
            "matched_name": row["_name"],
            "quantity": qty,
            "unit": unit_override or row["_unit"],
            "unit_rate": unit_rate,
            "amount": unit_rate * qty,
            "material": float(row["_material"] or 0) * qty,
            "labor_resource": float(row["_labor_resource"] or 0) * qty,
            "equipment": float(row["_equipment"] or 0) * qty,
        })
    return rows


def print_estimate(rows: list[dict]) -> None:
    print(f"{'#':<3} {'Matched item':<45} {'Qty':>10} {'Unit':<8} {'Unit rate':>14} {'Amount':>16}")
    print("-" * 100)
    total = total_material = total_labor = total_equipment = 0.0
    for i, r in enumerate(rows, 1):
        print(f"{i:<3} {str(r['matched_name'])[:45]:<45} {r['quantity']:>10,.2f} {str(r['unit']):<8} "
              f"{r['unit_rate']:>14,.2f} {r['amount']:>16,.2f}")
        if r["matched_code"] is None:
            print(f"     (no match for query: {r['query']!r})")
        total += r["amount"]
        total_material += r["material"]
        total_labor += r["labor_resource"]
        total_equipment += r["equipment"]
    print("-" * 100)
    print(f"{'TOTAL':>85} {total:>16,.2f}")
    print()
    print("Cost breakdown (informational subtotals - may not sum exactly to total):")
    print(f"  Material:       {total_material:>16,.2f}")
    print(f"  Labor/Resource: {total_labor:>16,.2f}")
    print(f"  Equipment:      {total_equipment:>16,.2f}")


def read_boq_csv(path: Path) -> list[tuple[str, float, str | None]]:
    lines = []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            token = (row.get("item") or row.get("rate_code") or row.get("query") or "").strip()
            if not token:
                continue
            qty = float(row.get("quantity") or row.get("qty") or 1)
            unit = (row.get("unit") or "").strip() or None
            lines.append((token, qty, unit))
    return lines


def main():
    parser = argparse.ArgumentParser(
        description="Offline cost estimator for DDC CWICR data (no API keys, no Qdrant)."
    )
    parser.add_argument("--path", type=str, default=str(DEFAULT_PATH),
                         help="Path to a DDC CWICR *_workitems_costs_resources_DDC_CWICR.parquet file.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_search = sub.add_parser("search", help="Search work items by name.")
    p_search.add_argument("query", type=str)
    p_search.add_argument("--limit", type=int, default=10)

    p_estimate = sub.add_parser("estimate", help="Price a bill of quantities.")
    p_estimate.add_argument(
        "--item", action="append", default=[], metavar="CODE_OR_QUERY:QTY[:UNIT]",
        help="Repeatable. e.g. --item \"concrete foundation:150:m3\"",
    )
    p_estimate.add_argument("--csv", type=str, default=None,
                             help="CSV with columns: item, quantity[, unit].")
    p_estimate.add_argument("--out", type=str, default=None,
                             help="Write the estimate to a CSV file.")

    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        sys.exit(
            f"File not found: {path}\n"
            "Use --path to point at a DDC CWICR *_workitems_costs_resources_DDC_CWICR.parquet file."
        )

    print(f"Loading: {path}")
    items = load_workitems(path)
    print(f"{len(items):,} unique work items loaded.\n")

    if args.command == "search":
        matches = search(items, args.query, limit=args.limit)
        if matches.empty:
            print("No matches.")
            return
        view = matches[["rate_code", "_name", "_unit", "_total", "_packaged_unit"]].rename(
            columns={"_name": "name", "_unit": "unit", "_total": "unit_cost", "_packaged_unit": "priced_per"}
        )
        print(view.to_string(index=False))
        return

    if args.command == "estimate":
        lines: list[tuple[str, float, str | None]] = []
        if args.csv:
            lines.extend(read_boq_csv(Path(args.csv)))
        for item_spec in args.item:
            parts = item_spec.split(":")
            if len(parts) < 2:
                sys.exit(f"Invalid --item {item_spec!r}. Expected CODE_OR_QUERY:QTY[:UNIT]")
            token, qty = parts[0], float(parts[1])
            unit = parts[2] if len(parts) > 2 else None
            lines.append((token, qty, unit))

        if not lines:
            sys.exit("No items to estimate. Use --item or --csv.")

        rows = estimate(items, lines)
        print_estimate(rows)

        if args.out:
            pd.DataFrame(rows).to_csv(args.out, index=False)
            print(f"\nWritten to {args.out}")


if __name__ == "__main__":
    main()
