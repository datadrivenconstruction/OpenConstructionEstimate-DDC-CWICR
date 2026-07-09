# n8n Workflow Guides -- DDC CWICR

This directory contains walkthrough guides for the four n8n automation workflows included in the DDC CWICR project. Each workflow uses the DDC CWICR vector database (via Qdrant) to perform construction cost estimation.

The workflow JSON files are located in [`2_n8n_Pipelines_Cost_Calculation/`](../../2_n8n_Pipelines_Cost_Calculation/).

---

## Workflows

| # | Workflow | File | Description |
|---|---------|------|-------------|
| 1 | [Text Bot](workflow-1-text-bot.md) | `n8n_1_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_DDC_CWICR.json` | Telegram bot that accepts text descriptions and returns cost estimates |
| 2 | [Photo Estimate](workflow-2-photo-estimate.md) | `n8n_2_Photo_Cost_Estimate_DDC_CWICR.json` | Web form that accepts construction photos and generates cost breakdowns |
| 3 | [Universal Bot](workflow-3-universal-bot.md) | `n8n_3_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_PHOTO_PDF_DDC_CWICR.json` | Full-featured Telegram bot supporting text, photo, and PDF inputs |
| 4 | [CAD/BIM Pipeline](workflow-4-cad-bim-pipeline.md) | `n8n_4_CAD_(BIM)_Cost_Estimation_Pipeline_4D_5D_with_DDC_CWICR.json` | Automated 10-stage pipeline from Revit/BIM models to cost reports |

---

## Prerequisites

All workflows require:

- **n8n** -- Self-hosted instance (v1.0+). Install via Docker or npm.
- **Qdrant** -- Vector database with DDC CWICR collections loaded. See [docker-compose.yml](../docker-compose.yml).
- **OpenAI API key** -- Used for embeddings (text-embedding-3-large, 3072 dimensions) and LLM processing.

Additional requirements per workflow:

| Workflow | Telegram Bot Token | OpenAI API | Gemini/Anthropic API (optional) | Revit Exporter |
|----------|:-----------------:|:----------:|:-------------------------------:|:--------------:|
| 1 -- Text Bot | Required | Required | Optional | -- |
| 2 -- Photo Estimate | -- | Required | Optional | -- |
| 3 -- Universal Bot | Required | Required | Optional (recommended for vision) | -- |
| 4 -- CAD/BIM Pipeline | -- | Required | Optional | Required |

---

## Quick Start

1. **Import the workflow** -- In n8n, go to Workflows > Import from File and select the JSON file.

2. **Configure credentials** -- Each workflow has a `TOKEN` node at the start. Fill in:
   - `bot_token` -- Telegram Bot API token (from @BotFather)
   - `QDRANT_URL` -- Qdrant server URL (default: `http://localhost:6333`)
   - `QDRANT_API_KEY` -- Qdrant API key (leave empty for local instances)
   - `OPENAI_API_KEY` -- OpenAI API key

3. **Set up n8n credentials** -- Go to Settings > Credentials and add:
   - OpenAI API credential (linked to model nodes)
   - Telegram API credential (for workflows 1 and 3)

4. **Activate the workflow** -- Toggle the workflow to active and test.

---

## Qdrant Collections

All workflows query these Qdrant collections for region-specific pricing:

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
| `ddc_usa_usd` | English (US) | USA | USD |
| `ddc_uk_gbp` | English (UK) | UK | GBP |

Each collection contains ~5,000 work items with pre-computed embeddings (OpenAI `text-embedding-3-large`, 3072 dimensions).

---

## Architecture

All workflows follow a common pattern:

```
User Input --> AI Parsing --> Embedding Generation --> Qdrant Vector Search --> AI Reranking --> Cost Calculation --> Report Output
```

The AI layer handles:
- Parsing free-form input into structured construction work items
- Generating embeddings for semantic search
- Reranking search results for relevance
- Formatting final cost reports (HTML, Excel, PDF)

---

## License

CC BY-NC 4.0 -- DataDrivenConstruction.io
