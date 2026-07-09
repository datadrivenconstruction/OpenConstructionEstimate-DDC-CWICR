"""
Advanced Qdrant Filtered Search

Combine vector similarity search with payload filters for precise,
faceted queries over CWICR construction cost data. Demonstrates:
  - Department filter
  - Price range filter
  - Unit type filter
  - Boolean flags (is_material, is_machine, is_abstract)
  - Combined / compound filters
"""

import argparse
import os

from dotenv import load_dotenv
from openai import OpenAI
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue, Range

load_dotenv()

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
EMBEDDING_MODEL = "text-embedding-3-large"
DEFAULT_COLLECTION = "ddc_en_toronto"
DEFAULT_TOP_K = 10

DISPLAY_FIELDS = [
    "rate_code",
    "rate_final_name",
    "rate_unit",
    "total_cost_per_position",
    "department_name",
    "section_name",
    "is_material",
    "is_machine",
    "resource_name",
]


# ---------------------------------------------------------------------------
# Clients
# ---------------------------------------------------------------------------

def get_openai_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is not set.")
    return OpenAI(api_key=api_key)


def get_qdrant_client() -> QdrantClient:
    url = os.getenv("QDRANT_URL", "http://localhost:6333")
    api_key = os.getenv("QDRANT_API_KEY")
    return QdrantClient(url=url, api_key=api_key)


def embed_query(client: OpenAI, text: str) -> list[float]:
    response = client.embeddings.create(model=EMBEDDING_MODEL, input=text)
    return response.data[0].embedding


# ---------------------------------------------------------------------------
# Search helpers
# ---------------------------------------------------------------------------

def search_with_filter(
    qdrant: QdrantClient,
    collection: str,
    vector: list[float],
    qdrant_filter: Filter | None = None,
    top_k: int = DEFAULT_TOP_K,
) -> list[dict]:
    """Run a filtered vector search and return results as dicts."""
    results = qdrant.query_points(
        collection_name=collection,
        query=vector,
        query_filter=qdrant_filter,
        limit=top_k,
        with_payload=True,
    )
    items = []
    for point in results.points:
        entry = dict(point.payload) if point.payload else {}
        entry["_score"] = point.score
        items.append(entry)
    return items


def print_results(items: list[dict], title: str = "Results"):
    """Pretty-print search results."""
    print(f"\n{'='*70}")
    print(f"  {title}  ({len(items)} results)")
    print(f"{'='*70}")
    if not items:
        print("  No results found.\n")
        return
    for i, item in enumerate(items, 1):
        print(f"\n  [{i}] score={item.get('_score', 0):.4f}")
        for field in DISPLAY_FIELDS:
            val = item.get(field)
            if val is not None:
                print(f"      {field}: {val}")
    print()


# ---------------------------------------------------------------------------
# Filter builders
# ---------------------------------------------------------------------------

def filter_by_department(department: str) -> Filter:
    """Match items from a specific department (exact match)."""
    return Filter(
        must=[
            FieldCondition(
                key="department_name",
                match=MatchValue(value=department),
            )
        ]
    )


def filter_by_cost_range(min_cost: float | None = None, max_cost: float | None = None) -> Filter:
    """Filter items within a cost range."""
    range_kwargs = {}
    if min_cost is not None:
        range_kwargs["gte"] = min_cost
    if max_cost is not None:
        range_kwargs["lte"] = max_cost
    return Filter(
        must=[
            FieldCondition(
                key="total_cost_per_position",
                range=Range(**range_kwargs),
            )
        ]
    )


def filter_by_unit(unit: str) -> Filter:
    """Match items with a specific measurement unit."""
    return Filter(
        must=[
            FieldCondition(
                key="rate_unit",
                match=MatchValue(value=unit),
            )
        ]
    )


def filter_materials_only() -> Filter:
    """Return only items flagged as materials."""
    return Filter(
        must=[
            FieldCondition(
                key="is_material",
                match=MatchValue(value=True),
            )
        ]
    )


def filter_machines_only() -> Filter:
    """Return only items flagged as machinery."""
    return Filter(
        must=[
            FieldCondition(
                key="is_machine",
                match=MatchValue(value=True),
            )
        ]
    )


def combined_filter(
    department: str | None = None,
    min_cost: float | None = None,
    max_cost: float | None = None,
    unit: str | None = None,
    is_material: bool | None = None,
    is_machine: bool | None = None,
) -> Filter | None:
    """Build a compound filter from multiple optional criteria."""
    conditions = []

    if department:
        conditions.append(
            FieldCondition(key="department_name", match=MatchValue(value=department))
        )
    if min_cost is not None or max_cost is not None:
        range_kwargs = {}
        if min_cost is not None:
            range_kwargs["gte"] = min_cost
        if max_cost is not None:
            range_kwargs["lte"] = max_cost
        conditions.append(
            FieldCondition(key="total_cost_per_position", range=Range(**range_kwargs))
        )
    if unit:
        conditions.append(
            FieldCondition(key="rate_unit", match=MatchValue(value=unit))
        )
    if is_material is not None:
        conditions.append(
            FieldCondition(key="is_material", match=MatchValue(value=is_material))
        )
    if is_machine is not None:
        conditions.append(
            FieldCondition(key="is_machine", match=MatchValue(value=is_machine))
        )

    if not conditions:
        return None
    return Filter(must=conditions)


# ---------------------------------------------------------------------------
# Demo scenarios
# ---------------------------------------------------------------------------

def run_demo_scenarios(
    openai_client: OpenAI,
    qdrant: QdrantClient,
    collection: str,
    top_k: int,
):
    """Run a series of filter examples to demonstrate capabilities."""

    scenarios = [
        {
            "title": "Unfiltered search - concrete work",
            "query": "reinforced concrete foundation",
            "filter": None,
        },
        {
            "title": "Department filter - only 'Concrete' department",
            "query": "reinforced concrete foundation",
            "filter": filter_by_department("Concrete"),
        },
        {
            "title": "Cost range - items between 100 and 1000 EUR",
            "query": "insulation thermal wall",
            "filter": filter_by_cost_range(min_cost=100, max_cost=1000),
        },
        {
            "title": "Unit filter - items measured in m3",
            "query": "excavation earthwork",
            "filter": filter_by_unit("m3"),
        },
        {
            "title": "Materials only - steel reinforcement materials",
            "query": "steel reinforcement rebar",
            "filter": filter_materials_only(),
        },
        {
            "title": "Machinery only - crane and heavy equipment",
            "query": "crane lifting heavy equipment",
            "filter": filter_machines_only(),
        },
        {
            "title": "Combined - Concrete dept, 50-500 EUR, measured in m2",
            "query": "formwork shuttering",
            "filter": combined_filter(
                department="Concrete",
                min_cost=50,
                max_cost=500,
                unit="m2",
            ),
        },
    ]

    for scenario in scenarios:
        print(f"\nEmbedding query: \"{scenario['query']}\"")
        vector = embed_query(openai_client, scenario["query"])
        results = search_with_filter(
            qdrant, collection, vector, scenario["filter"], top_k
        )
        print_results(results, scenario["title"])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Advanced filtered vector search over CWICR data in Qdrant.",
    )
    parser.add_argument(
        "--query", "-q",
        type=str,
        default=None,
        help="Custom search query. If omitted, runs built-in demo scenarios.",
    )
    parser.add_argument(
        "--collection", "-c",
        type=str,
        default=DEFAULT_COLLECTION,
        help=f"Qdrant collection (default: {DEFAULT_COLLECTION}).",
    )
    parser.add_argument(
        "--top-k", "-k",
        type=int,
        default=DEFAULT_TOP_K,
        help=f"Number of results (default: {DEFAULT_TOP_K}).",
    )
    parser.add_argument("--department", type=str, default=None, help="Filter by department_name.")
    parser.add_argument("--min-cost", type=float, default=None, help="Minimum total_cost_per_position.")
    parser.add_argument("--max-cost", type=float, default=None, help="Maximum total_cost_per_position.")
    parser.add_argument("--unit", type=str, default=None, help="Filter by rate_unit (e.g., m3, m2, kg).")
    parser.add_argument("--materials", action="store_true", help="Show only material items.")
    parser.add_argument("--machines", action="store_true", help="Show only machinery items.")
    args = parser.parse_args()

    openai_client = get_openai_client()
    qdrant = get_qdrant_client()

    if args.query:
        # --- Custom single query with optional filters ---
        filt = combined_filter(
            department=args.department,
            min_cost=args.min_cost,
            max_cost=args.max_cost,
            unit=args.unit,
            is_material=True if args.materials else None,
            is_machine=True if args.machines else None,
        )
        vector = embed_query(openai_client, args.query)
        results = search_with_filter(qdrant, args.collection, vector, filt, args.top_k)

        filter_desc = []
        if args.department:
            filter_desc.append(f"dept={args.department}")
        if args.min_cost is not None:
            filter_desc.append(f"min={args.min_cost}")
        if args.max_cost is not None:
            filter_desc.append(f"max={args.max_cost}")
        if args.unit:
            filter_desc.append(f"unit={args.unit}")
        if args.materials:
            filter_desc.append("materials_only")
        if args.machines:
            filter_desc.append("machines_only")
        title = f"Query: \"{args.query}\"" + (f"  filters: [{', '.join(filter_desc)}]" if filter_desc else "")
        print_results(results, title)
    else:
        # --- Demo scenarios ---
        print(f"\nRunning demo filter scenarios on collection: {args.collection}\n")
        run_demo_scenarios(openai_client, qdrant, args.collection, args.top_k)


if __name__ == "__main__":
    main()
