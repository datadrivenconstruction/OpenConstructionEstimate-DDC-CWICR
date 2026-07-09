"""
Multi-Region Cost Comparison

Load two or more CWICR Parquet files from different regions, match
equivalent work items by rate_code, and compare total_cost_per_position
across regions. Outputs a comparison table and a matplotlib bar chart.
"""

import argparse
import os
import sys
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------------------------
# Default paths (relative to this script's location)
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent.parent.parent

DEFAULT_PARQUET_FILES = {
    "EN_Toronto": REPO_ROOT / "EN___DDC_CWICR" / "ENG_TORONTO_workitems_costs_resources_DDC_CWICR.parquet",
    "DE_Berlin": REPO_ROOT / "DE___DDC_CWICR" / "DE_BERLIN_workitems_costs_resources_DDC_CWICR.parquet",
    "RU_StPetersburg": REPO_ROOT / "RU___DDC_CWICR" / "RU_STPETERSBURG_workitems_costs_resources_DDC_CWICR.parquet",
}

COST_COLUMN = "total_cost_per_position"
MATERIAL_COST_COLUMN = "total_material_cost_per_position"
RESOURCE_COST_COLUMN = "total_resource_cost_per_position"
OUTPUT_CHART = "region_comparison.png"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_parquet(path: str | Path, label: str) -> pd.DataFrame:
    """Load a Parquet file and add a region label column."""
    path = Path(path)
    if not path.exists():
        print(f"WARNING: File not found: {path}")
        return pd.DataFrame()
    df = pd.read_parquet(path)
    df["_region"] = label
    print(f"  Loaded {label}: {len(df):,} rows, {len(df.columns)} columns")
    return df


def find_common_rate_codes(dataframes: dict[str, pd.DataFrame]) -> set[str]:
    """Find rate_codes that appear in ALL provided dataframes."""
    code_sets = []
    for label, df in dataframes.items():
        if "rate_code" in df.columns:
            codes = set(df["rate_code"].dropna().unique())
            code_sets.append(codes)
            print(f"  {label}: {len(codes):,} unique rate_codes")
    if not code_sets:
        return set()
    common = code_sets[0]
    for s in code_sets[1:]:
        common = common.intersection(s)
    print(f"  Common rate_codes across all regions: {len(common):,}")
    return common


def build_comparison_table(
    dataframes: dict[str, pd.DataFrame],
    common_codes: set[str],
    cost_col: str = COST_COLUMN,
) -> pd.DataFrame:
    """
    For each common rate_code, pick the first matching row from each region
    and build a wide comparison table.
    """
    rows = []
    for code in sorted(common_codes):
        entry = {"rate_code": code}
        for label, df in dataframes.items():
            subset = df[df["rate_code"] == code]
            if subset.empty:
                continue
            first = subset.iloc[0]
            entry[f"{label}_name"] = first.get("rate_final_name", first.get("rate_original_name", ""))
            entry[f"{label}_{cost_col}"] = first.get(cost_col, None)
            entry[f"{label}_unit"] = first.get("rate_unit", "")
        rows.append(entry)
    return pd.DataFrame(rows)


def plot_comparison(
    comparison_df: pd.DataFrame,
    regions: list[str],
    cost_col: str,
    top_n: int,
    output_path: str,
):
    """Create a grouped bar chart comparing costs across regions."""
    cost_cols = [f"{r}_{cost_col}" for r in regions]
    existing = [c for c in cost_cols if c in comparison_df.columns]
    if not existing:
        print("No cost columns found for plotting.")
        return

    # Use the first region's name column as the label
    name_col = next(
        (f"{r}_name" for r in regions if f"{r}_name" in comparison_df.columns),
        None,
    )

    plot_df = comparison_df.dropna(subset=existing, how="all").copy()

    # Sort by average cost and take top N
    plot_df["_avg_cost"] = plot_df[existing].mean(axis=1)
    plot_df = plot_df.nlargest(top_n, "_avg_cost")

    labels = (
        plot_df[name_col].str[:40] if name_col else plot_df["rate_code"]
    )

    x = range(len(plot_df))
    width = 0.8 / len(existing)

    fig, ax = plt.subplots(figsize=(14, max(6, top_n * 0.4)))
    for i, col in enumerate(existing):
        region_label = col.replace(f"_{cost_col}", "")
        offset = (i - len(existing) / 2 + 0.5) * width
        bars_x = [xi + offset for xi in x]
        ax.barh(bars_x, plot_df[col].fillna(0), height=width, label=region_label)

    ax.set_yticks(list(x))
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel(f"{cost_col} (EUR)")
    ax.set_title(f"Top {top_n} Work Items - Cost Comparison by Region")
    ax.legend()
    ax.invert_yaxis()
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    print(f"\nChart saved to: {output_path}")
    plt.close()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Compare CWICR construction costs across regions.",
    )
    parser.add_argument(
        "--files", "-f",
        nargs="+",
        default=None,
        help="Paths to Parquet files. If omitted, uses default EN/DE/RU files.",
    )
    parser.add_argument(
        "--labels", "-l",
        nargs="+",
        default=None,
        help="Region labels corresponding to --files (same order).",
    )
    parser.add_argument(
        "--department", "-d",
        type=str,
        default=None,
        help="Filter to a specific department_name (case-insensitive substring).",
    )
    parser.add_argument(
        "--top", "-t",
        type=int,
        default=15,
        help="Number of top items to show in the chart (default: 15).",
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default=OUTPUT_CHART,
        help=f"Output chart filename (default: {OUTPUT_CHART}).",
    )
    args = parser.parse_args()

    # --- Load data ---
    print("\n=== Loading Parquet files ===\n")
    dataframes: dict[str, pd.DataFrame] = {}

    if args.files:
        labels = args.labels or [Path(f).stem for f in args.files]
        if len(labels) != len(args.files):
            print("ERROR: --labels count must match --files count.")
            sys.exit(1)
        for path, label in zip(args.files, labels):
            df = load_parquet(path, label)
            if not df.empty:
                dataframes[label] = df
    else:
        for label, path in DEFAULT_PARQUET_FILES.items():
            df = load_parquet(path, label)
            if not df.empty:
                dataframes[label] = df

    if len(dataframes) < 2:
        print("\nERROR: Need at least 2 datasets to compare. Check file paths.")
        sys.exit(1)

    # --- Optional department filter ---
    if args.department:
        print(f"\nFiltering to department containing: '{args.department}'")
        for label in list(dataframes):
            df = dataframes[label]
            if "department_name" in df.columns:
                mask = df["department_name"].str.contains(
                    args.department, case=False, na=False,
                )
                dataframes[label] = df[mask]
                print(f"  {label}: {mask.sum():,} rows after filter")

    # --- Find common rate codes ---
    print("\n=== Finding common rate_codes ===\n")
    common_codes = find_common_rate_codes(dataframes)

    if not common_codes:
        print("No common rate_codes found across all regions.")
        sys.exit(1)

    # --- Build comparison table ---
    print("\n=== Building comparison table ===\n")
    comparison = build_comparison_table(dataframes, common_codes)
    print(comparison.head(20).to_string(index=False))

    # --- Save CSV ---
    csv_path = args.output.replace(".png", ".csv")
    comparison.to_csv(csv_path, index=False)
    print(f"\nFull table saved to: {csv_path}")

    # --- Plot ---
    print("\n=== Generating chart ===\n")
    regions = list(dataframes.keys())
    plot_comparison(comparison, regions, COST_COLUMN, args.top, args.output)

    print("\nDone.\n")


if __name__ == "__main__":
    main()
