# 10 - Embedding Pipeline

Generate embeddings from CSV or Parquet data using OpenAI `text-embedding-3-large` and upsert them into a Qdrant collection. Useful for extending CWICR with your own custom construction cost data.

## Scripts

| Script | Description |
|---|---|
| `generate_embeddings.py` | Read data, batch-embed with rate limiting, upsert into Qdrant |

## How It Works

1. Reads a CSV or Parquet file containing work items / resources.
2. Builds a text representation for each row from configurable columns.
3. Generates embeddings in batches using the OpenAI API with rate-limit handling.
4. Creates a Qdrant collection (if it does not exist) with the correct vector configuration.
5. Upserts points with embeddings and full row payload into Qdrant.

## Prerequisites

```bash
pip install openai qdrant-client pandas pyarrow python-dotenv tqdm
```

Create a `.env` file:

```
OPENAI_API_KEY=sk-...
QDRANT_URL=https://your-qdrant-instance.cloud
QDRANT_API_KEY=your-qdrant-api-key
```

## Usage

```bash
# Embed a Parquet file and upsert to Qdrant
python generate_embeddings.py \
    --input ../../data/EN___DDC_CWICR/ENG_TORONTO_workitems_costs_resources_DDC_CWICR.parquet \
    --collection my_custom_collection

# Embed a CSV file with custom batch size
python generate_embeddings.py \
    --input my_data.csv \
    --collection my_collection \
    --batch-size 100

# Dry run - generate embeddings but do not upsert
python generate_embeddings.py --input data.parquet --dry-run

# Limit rows for testing
python generate_embeddings.py --input data.parquet --collection test_col --max-rows 500
```
