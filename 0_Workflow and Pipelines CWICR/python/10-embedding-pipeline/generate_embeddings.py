"""
Embedding Pipeline - Generate & Upsert to Qdrant

Read a CSV or Parquet file, generate embeddings via OpenAI
text-embedding-3-large with batching and rate-limit handling,
then upsert into a Qdrant collection.
"""

import argparse
import os
import sys
import time
import uuid
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

try:
    from tqdm import tqdm
except ImportError:
    # Minimal fallback if tqdm is not installed
    def tqdm(iterable, **kwargs):
        total = kwargs.get("total", None)
        for i, item in enumerate(iterable):
            if total:
                print(f"  {i+1}/{total}", end="\r")
            yield item
        print()

load_dotenv()

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
EMBEDDING_MODEL = "text-embedding-3-large"
EMBEDDING_DIMS = 3072
DEFAULT_BATCH_SIZE = 64
MAX_RETRIES = 5
BASE_RETRY_DELAY = 2.0  # seconds

# Columns used to build the text for embedding
TEXT_COLUMNS = [
    "rate_code",
    "rate_final_name",
    "rate_original_name",
    "rate_unit",
    "department_name",
    "section_name",
    "subsection_name",
    "resource_name",
    "resource_unit",
    "work_composition_text",
]

# All columns to store as payload (None = store everything)
PAYLOAD_COLUMNS = None


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


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_data(path: str, max_rows: int | None = None) -> pd.DataFrame:
    """Load a CSV or Parquet file into a DataFrame."""
    p = Path(path)
    if not p.exists():
        print(f"ERROR: File not found: {p}")
        sys.exit(1)

    ext = p.suffix.lower()
    if ext == ".parquet":
        df = pd.read_parquet(p)
    elif ext == ".csv":
        df = pd.read_csv(p)
    else:
        print(f"ERROR: Unsupported file type '{ext}'. Use .csv or .parquet.")
        sys.exit(1)

    if max_rows and max_rows < len(df):
        df = df.head(max_rows)
        print(f"  Limited to first {max_rows} rows.")

    print(f"  Loaded {len(df):,} rows from {p.name}")
    return df


def row_to_text(row: pd.Series, columns: list[str]) -> str:
    """Convert a DataFrame row into a text string for embedding."""
    parts = []
    for col in columns:
        val = row.get(col)
        if pd.notna(val) and str(val).strip():
            parts.append(f"{col}: {val}")
    return " | ".join(parts) if parts else ""


# ---------------------------------------------------------------------------
# Embedding with rate limiting
# ---------------------------------------------------------------------------

def embed_batch(client: OpenAI, texts: list[str]) -> list[list[float]]:
    """Embed a batch of texts with retry logic for rate limits."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.embeddings.create(
                model=EMBEDDING_MODEL,
                input=texts,
            )
            return [item.embedding for item in response.data]
        except RateLimitError as e:
            delay = BASE_RETRY_DELAY * (2 ** (attempt - 1))
            print(f"\n  Rate limited (attempt {attempt}/{MAX_RETRIES}). "
                  f"Waiting {delay:.0f}s ...")
            time.sleep(delay)
    raise RuntimeError(f"Failed to embed batch after {MAX_RETRIES} retries.")


def generate_all_embeddings(
    client: OpenAI,
    texts: list[str],
    batch_size: int,
) -> list[list[float]]:
    """Generate embeddings for all texts in batches."""
    all_embeddings: list[list[float]] = []
    n_batches = (len(texts) + batch_size - 1) // batch_size

    for i in tqdm(range(0, len(texts), batch_size), total=n_batches, desc="Embedding"):
        batch = texts[i : i + batch_size]
        embeddings = embed_batch(client, batch)
        all_embeddings.extend(embeddings)

    return all_embeddings


# ---------------------------------------------------------------------------
# Qdrant upsert
# ---------------------------------------------------------------------------

def ensure_collection(qdrant: QdrantClient, collection: str):
    """Create the Qdrant collection if it does not already exist."""
    collections = [c.name for c in qdrant.get_collections().collections]
    if collection in collections:
        print(f"  Collection '{collection}' already exists.")
        return

    qdrant.create_collection(
        collection_name=collection,
        vectors_config=VectorParams(
            size=EMBEDDING_DIMS,
            distance=Distance.COSINE,
        ),
    )
    print(f"  Created collection '{collection}' (dim={EMBEDDING_DIMS}, cosine).")


def build_payload(row: pd.Series, columns: list[str] | None) -> dict:
    """Build a JSON-safe payload dict from a DataFrame row."""
    if columns:
        data = {col: row.get(col) for col in columns if col in row.index}
    else:
        data = row.to_dict()
    # Convert NaN / NaT to None for JSON compatibility
    return {k: (None if pd.isna(v) else v) for k, v in data.items()}


def upsert_to_qdrant(
    qdrant: QdrantClient,
    collection: str,
    df: pd.DataFrame,
    embeddings: list[list[float]],
    batch_size: int,
    payload_columns: list[str] | None = None,
):
    """Upsert embeddings and payloads into Qdrant in batches."""
    ensure_collection(qdrant, collection)

    n_batches = (len(df) + batch_size - 1) // batch_size
    total_upserted = 0

    for i in tqdm(range(0, len(df), batch_size), total=n_batches, desc="Upserting"):
        batch_df = df.iloc[i : i + batch_size]
        batch_embeddings = embeddings[i : i + batch_size]

        points = []
        for j, (_, row) in enumerate(batch_df.iterrows()):
            point_id = str(uuid.uuid4())
            payload = build_payload(row, payload_columns)
            points.append(
                PointStruct(
                    id=point_id,
                    vector=batch_embeddings[j],
                    payload=payload,
                )
            )

        qdrant.upsert(collection_name=collection, points=points)
        total_upserted += len(points)

    print(f"  Upserted {total_upserted:,} points into '{collection}'.")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Generate embeddings from CSV/Parquet and upsert into Qdrant.",
    )
    parser.add_argument(
        "--input", "-i",
        type=str,
        required=True,
        help="Path to the input CSV or Parquet file.",
    )
    parser.add_argument(
        "--collection", "-c",
        type=str,
        default="ddc_custom",
        help="Qdrant collection name to upsert into (default: ddc_custom).",
    )
    parser.add_argument(
        "--batch-size", "-b",
        type=int,
        default=DEFAULT_BATCH_SIZE,
        help=f"Batch size for embedding and upsert (default: {DEFAULT_BATCH_SIZE}).",
    )
    parser.add_argument(
        "--max-rows",
        type=int,
        default=None,
        help="Limit the number of rows to process (useful for testing).",
    )
    parser.add_argument(
        "--text-columns",
        nargs="+",
        default=None,
        help="Columns to use for building the embedding text. "
             "Defaults to a predefined set of CWICR columns.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Generate embeddings but do not upsert to Qdrant.",
    )
    args = parser.parse_args()

    text_cols = args.text_columns or TEXT_COLUMNS

    # --- Load data ---
    print(f"\n{'='*60}")
    print("Embedding Pipeline")
    print(f"{'='*60}\n")
    print(f"[1/4] Loading data from: {args.input}")
    df = load_data(args.input, max_rows=args.max_rows)

    # --- Build texts ---
    print(f"\n[2/4] Building text representations (columns: {text_cols})")
    available_cols = [c for c in text_cols if c in df.columns]
    if not available_cols:
        print(f"ERROR: None of the text columns {text_cols} found in the data.")
        print(f"Available columns: {list(df.columns)}")
        sys.exit(1)

    missing = set(text_cols) - set(available_cols)
    if missing:
        print(f"  Note: columns not found (skipped): {missing}")

    texts = [row_to_text(row, available_cols) for _, row in df.iterrows()]
    empty_count = sum(1 for t in texts if not t)
    print(f"  Generated {len(texts):,} texts ({empty_count} empty)")

    # Filter out empty texts
    if empty_count:
        mask = [bool(t) for t in texts]
        df = df[[m for m in mask]].reset_index(drop=True) if not all(mask) else df
        texts = [t for t in texts if t]
        print(f"  After filtering: {len(texts):,} rows")

    # --- Generate embeddings ---
    print(f"\n[3/4] Generating embeddings (model={EMBEDDING_MODEL}, batch_size={args.batch_size})")
    openai_client = get_openai_client()
    embeddings = generate_all_embeddings(openai_client, texts, args.batch_size)
    print(f"  Generated {len(embeddings):,} embeddings (dim={len(embeddings[0]) if embeddings else 0})")

    # --- Upsert ---
    if args.dry_run:
        print(f"\n[4/4] Dry run - skipping upsert to Qdrant.")
        print(f"  Would have upserted {len(embeddings):,} points to '{args.collection}'.")
    else:
        print(f"\n[4/4] Upserting to Qdrant collection: {args.collection}")
        qdrant = get_qdrant_client()
        upsert_to_qdrant(qdrant, args.collection, df, embeddings, args.batch_size, PAYLOAD_COLUMNS)

    print(f"\nDone.\n")


if __name__ == "__main__":
    main()
