"""
RAG Pipeline - Basic (Anthropic Claude + Qdrant + OpenAI Embeddings)

Embed a user question with OpenAI text-embedding-3-large, retrieve the top-k
most relevant CWICR work items from Qdrant, then ask Claude to generate an
answer grounded in the retrieved construction-cost data.
"""

import argparse
import os
import textwrap

from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic
from qdrant_client import QdrantClient

load_dotenv()

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
EMBEDDING_MODEL = "text-embedding-3-large"
EMBEDDING_DIMS = 3072
DEFAULT_COLLECTION = "ddc_en_toronto"
DEFAULT_TOP_K = 10
CLAUDE_MODEL = "claude-sonnet-4-20250514"

EXAMPLE_QUERIES = [
    "What is the cost of reinforced concrete foundation work?",
    "How much does excavation of trenches cost per cubic metre?",
    "Compare labour hours for bricklaying vs plastering.",
    "What materials are used for waterproofing basements?",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_openai_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is not set in .env or environment.")
    return OpenAI(api_key=api_key)


def get_anthropic_client() -> Anthropic:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError("ANTHROPIC_API_KEY is not set in .env or environment.")
    return Anthropic(api_key=api_key)


def get_qdrant_client() -> QdrantClient:
    url = os.getenv("QDRANT_URL", "http://localhost:6333")
    api_key = os.getenv("QDRANT_API_KEY")
    return QdrantClient(url=url, api_key=api_key)


def embed_query(client: OpenAI, text: str) -> list[float]:
    """Embed a single query string using OpenAI text-embedding-3-large."""
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
    )
    return response.data[0].embedding


def search_qdrant(
    client: QdrantClient,
    collection: str,
    vector: list[float],
    top_k: int = DEFAULT_TOP_K,
) -> list[dict]:
    """Search Qdrant and return payload dicts with scores."""
    results = client.query_points(
        collection_name=collection,
        query=vector,
        limit=top_k,
        with_payload=True,
    )
    items = []
    for point in results.points:
        entry = dict(point.payload) if point.payload else {}
        entry["_score"] = point.score
        items.append(entry)
    return items


def format_context(items: list[dict]) -> str:
    """Format retrieved items into a text block for the LLM context window."""
    lines = []
    for i, item in enumerate(items, 1):
        parts = [f"[{i}]"]
        for key in (
            "rate_code",
            "rate_final_name",
            "rate_unit",
            "total_cost_per_position",
            "department_name",
            "section_name",
            "resource_name",
            "resource_unit",
            "resource_quantity",
            "resource_price_per_unit_eur_current",
            "labor_hours_construction_workers",
        ):
            val = item.get(key)
            if val is not None:
                parts.append(f"{key}: {val}")
        parts.append(f"relevance_score: {item.get('_score', 'N/A')}")
        lines.append(" | ".join(parts))
    return "\n".join(lines)


def ask_claude(client: Anthropic, question: str, context: str) -> str:
    """Send the question + retrieved context to Claude and return the answer."""
    system_prompt = textwrap.dedent("""\
        You are a construction cost estimation assistant. You answer questions
        using ONLY the CWICR (Construction Work Items, Costs & Resources)
        data provided in the context below. If the context does not contain
        enough information, say so explicitly. Always cite rate codes when
        referencing specific items. Present costs in EUR unless asked otherwise.
    """)

    user_message = (
        f"### Retrieved CWICR data\n{context}\n\n"
        f"### Question\n{question}"
    )

    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=2048,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )
    return response.content[0].text


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="RAG pipeline: Qdrant retrieval + Claude generation over CWICR data.",
    )
    parser.add_argument(
        "--query", "-q",
        type=str,
        default=EXAMPLE_QUERIES[0],
        help="Natural-language question about construction costs.",
    )
    parser.add_argument(
        "--collection", "-c",
        type=str,
        default=DEFAULT_COLLECTION,
        help=f"Qdrant collection name (default: {DEFAULT_COLLECTION}).",
    )
    parser.add_argument(
        "--top-k", "-k",
        type=int,
        default=DEFAULT_TOP_K,
        help=f"Number of results to retrieve (default: {DEFAULT_TOP_K}).",
    )
    parser.add_argument(
        "--show-context",
        action="store_true",
        help="Print the raw retrieved context before the answer.",
    )
    args = parser.parse_args()

    # --- Clients ---
    openai_client = get_openai_client()
    anthropic_client = get_anthropic_client()
    qdrant_client = get_qdrant_client()

    # --- Step 1: Embed the question ---
    print(f"\n{'='*70}")
    print(f"Query: {args.query}")
    print(f"Collection: {args.collection}  |  top_k: {args.top_k}")
    print(f"{'='*70}\n")

    print("[1/3] Embedding query ...")
    query_vector = embed_query(openai_client, args.query)

    # --- Step 2: Retrieve from Qdrant ---
    print("[2/3] Searching Qdrant ...")
    results = search_qdrant(qdrant_client, args.collection, query_vector, args.top_k)
    print(f"      Retrieved {len(results)} items.")

    if not results:
        print("No results found. Try a different query or collection.")
        return

    context = format_context(results)

    if args.show_context:
        print(f"\n--- Retrieved Context ---\n{context}\n--- End Context ---\n")

    # --- Step 3: Generate answer with Claude ---
    print("[3/3] Generating answer with Claude ...")
    answer = ask_claude(anthropic_client, args.query, context)

    print(f"\n{'='*70}")
    print("ANSWER")
    print(f"{'='*70}\n")
    print(answer)
    print()


if __name__ == "__main__":
    main()
