# DDC CWICR Examples

Hands-on examples for working with the **Open Construction Estimate (DDC CWICR)** dataset -- 55,000+ construction work items with costs, resources, and embeddings across 11 languages.

---

## Examples Overview

### Python

| Example | Difficulty | Prerequisites | Description |
|---------|-----------|--------------|-------------|
| [01-load-and-explore](python/01-load-and-explore/) | Beginner | pandas | Load Parquet files and explore the DDC CWICR dataset structure |
| [02-semantic-search-qdrant](python/02-semantic-search-qdrant/) | Intermediate | qdrant-client, openai | Perform vector similarity search against Qdrant collections |
| [03-cost-estimation-text](python/03-cost-estimation-text/) | Intermediate | qdrant-client, openai | Text-based construction cost estimation using RAG |
| [04-cost-estimation-photo](python/04-cost-estimation-photo/) | Advanced | qdrant-client, openai | Estimate costs from construction site photos via vision AI |
| [05-boq-generation](python/05-boq-generation/) | Intermediate | qdrant-client, openai | Generate a Bill of Quantities from a project description |
| [06-rag-pipeline](python/06-rag-pipeline/) | Advanced | qdrant-client, openai | Full Retrieval-Augmented Generation pipeline for cost Q&A |
| [07-multi-language-comparison](python/07-multi-language-comparison/) | Intermediate | qdrant-client | Compare pricing across regions and languages |
| [08-data-analysis](python/08-data-analysis/) | Beginner | pandas, matplotlib | Statistical analysis and visualization of cost data |
| [09-filtered-search](python/09-filtered-search/) | Intermediate | qdrant-client | Search with metadata filters (category, unit, price range) |
| [10-embedding-pipeline](python/10-embedding-pipeline/) | Advanced | openai, qdrant-client | Generate embeddings and load them into Qdrant |

### JavaScript

| Example | Difficulty | Prerequisites | Description |
|---------|-----------|--------------|-------------|
| [01-load-and-explore](javascript/01-load-and-explore/) | Beginner | parquet-wasm | Load and explore Parquet data in Node.js |
| [02-api-quickstart](javascript/02-api-quickstart/) | Beginner | node-fetch | Quick start with the DDC CWICR REST API |
| [03-semantic-search-qdrant](javascript/03-semantic-search-qdrant/) | Intermediate | @qdrant/js-client-rest | Vector search from JavaScript |
| [04-cost-estimation-text](javascript/04-cost-estimation-text/) | Intermediate | openai, @qdrant/js-client-rest | Text-based cost estimation in Node.js |
| [05-natural-language-query](javascript/05-natural-language-query/) | Advanced | openai, @qdrant/js-client-rest | Natural language queries against cost data |

### Rust

| Example | Difficulty | Prerequisites | Description |
|---------|-----------|--------------|-------------|
| [01-load-parquet](rust/01-load-parquet/) | Intermediate | arrow, parquet crates | Read DDC CWICR Parquet files in Rust |
| [02-qdrant-search](rust/02-qdrant-search/) | Advanced | qdrant-client crate | High-performance vector search from Rust |

### R

| Example | Difficulty | Prerequisites | Description |
|---------|-----------|--------------|-------------|
| [01-load-and-explore](r/01-load-and-explore/) | Beginner | arrow | Load and explore DDC CWICR data in R |
| [02-cost-analysis](r/02-cost-analysis/) | Intermediate | dplyr, ggplot2 | Statistical cost analysis and visualizations |

### Shell

| Example | Difficulty | Prerequisites | Description |
|---------|-----------|--------------|-------------|
| [setup-qdrant](shell/) | Beginner | Docker | Set up Qdrant and load DDC CWICR collections |
| [api-examples](shell/) | Beginner | curl, jq | REST API usage examples with curl |

### n8n Workflows

| Guide | Difficulty | Prerequisites | Description |
|-------|-----------|--------------|-------------|
| [Workflow 1 -- Text Bot](n8n-guides/workflow-1-text-bot.md) | Intermediate | n8n, Telegram, OpenAI, Qdrant | Telegram bot for text-based cost estimation |
| [Workflow 2 -- Photo Estimate](n8n-guides/workflow-2-photo-estimate.md) | Advanced | n8n, OpenAI, Qdrant | Photo-based cost estimation via web form |
| [Workflow 3 -- Universal Bot](n8n-guides/workflow-3-universal-bot.md) | Advanced | n8n, Telegram, OpenAI, Qdrant | Multi-modal bot (text + photo + PDF) |
| [Workflow 4 -- CAD/BIM Pipeline](n8n-guides/workflow-4-cad-bim-pipeline.md) | Advanced | n8n, Revit, OpenAI, Qdrant | 10-stage BIM-to-cost-estimate pipeline |

---

## Getting Started

Choose a path based on your setup:

### Path 1: Zero Setup (REST API / cURL)

No local installation required. Use the hosted API or cURL examples directly.

```bash
# Example: search for "concrete foundation" in the English/Toronto collection
curl -X POST "http://localhost:6333/collections/ddc_en_toronto/points/search" \
  -H "Content-Type: application/json" \
  -d '{"vector": [...], "limit": 5}'
```

Start with: `shell/api-examples` or `javascript/02-api-quickstart`

### Path 2: Local (Python + Parquet)

Work with the included Parquet sample data offline. No Docker or Qdrant needed.

```bash
cd examples
pip install -r python/requirements.txt
```

Start with: `python/01-load-and-explore` or `python/08-data-analysis`

### Path 3: Full Stack (Docker + Qdrant)

Run Qdrant locally with Docker, load all DDC CWICR collections, and use semantic search.

```bash
cd examples
cp .env.example .env
# Edit .env with your API keys

docker compose up -d
# Load collections (see shell/setup-qdrant)
```

Start with: `python/02-semantic-search-qdrant` or `python/06-rag-pipeline`

---

## Infrastructure

| File | Purpose |
|------|---------|
| [docker-compose.yml](docker-compose.yml) | Qdrant vector database |
| [.env.example](.env.example) | Environment variable template |
| [sample-data/](sample-data/) | Sample Parquet files for offline use |

### Qdrant Collections

The DDC CWICR dataset is available as pre-built Qdrant collections:

| Collection | Language | City | Currency |
|------------|----------|------|----------|
| `ddc_en_toronto` | English | Toronto | CAD $ |
| `ddc_de_berlin` | German | Berlin | EUR |
| `ddc_ru_stpetersburg` | Russian | St. Petersburg | RUB |
| `ddc_fr_paris` | French | Paris | EUR |
| `ddc_sp_barcelona` | Spanish | Barcelona | EUR |
| `ddc_ar_dubai` | Arabic | Dubai | AED |
| `ddc_zh_shanghai` | Chinese | Shanghai | CNY |
| `ddc_hi_mumbai` | Hindi | Mumbai | INR |
| `ddc_pt_saopaulo` | Portuguese | Sao Paulo | BRL |
| `ddc_usa_usd` | English | USA | USD |
| `ddc_uk_gbp` | English | UK | GBP |

---

## License

All examples and the DDC CWICR dataset are licensed under **CC BY-NC 4.0** (Creative Commons Attribution-NonCommercial 4.0 International).

You are free to share and adapt the material for any purpose, including commercial use, as long as you provide appropriate attribution.

Attribution: **DataDrivenConstruction.io** -- [OpenConstructionEstimate-DDC-CWICR](https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR)
