# DDC CWICR - AI Assistant Instructions

> **DDC CWICR** (Construction Work Items, Components & Resources) is an open-source multilingual construction cost database with 55,719 work items and 27,672 resources across **30 country tracks in 23 languages**, powered by pre-computed OpenAI embeddings for semantic search.

## Quick Start

```python
import pandas as pd
from qdrant_client import QdrantClient

# Load data
df = pd.read_parquet("DDC_CWICR_EN.parquet")

# Semantic search
client = QdrantClient("localhost", port=6333)
results = client.search(
    collection_name="ddc_en_toronto",
    query_vector=embedding,
    limit=10
)
```

## What This Repository Is

**DDC CWICR** is a comprehensive construction cost database designed for:
- **Automated cost estimation** from BIM models, photos, or text descriptions
- **Semantic search** via Qdrant vector database with pre-computed embeddings
- **AI/LLM integration** for intelligent material matching and price lookup
- **Multi-language support** with region-specific pricing

## Database Statistics

| Metric | Value |
|--------|-------|
| Work Items | 55,719 |
| Resources | 27,672 |
| Country Tracks | 30 (11 shipped + 19 derived) |
| Languages | 23 unique |
| Data Fields | 93 |
| Embedding Dimensions | 3,072 (OpenAI text-embedding-3-large) |

## Available Formats

| Format | Size | Best For |
|--------|------|----------|
| **Excel** (.xlsx) | 150-400 MB | Manual analysis, pivot tables |
| **Parquet** (.parquet) | 55 MB | ETL pipelines, ML training, Python |
| **CSV** (.csv) | 1.3 GB | Database imports, legacy systems |
| **Qdrant** (.snapshot) | 1 GB | Semantic search, RAG systems |

## Languages & Regional Pricing

### Shipped tracks (11)

| Code | Language | Region | Currency | Collection |
|------|----------|--------|----------|------------|
| `AR` | Arabic | Dubai | AED | `ddc_ar_dubai` |
| `DE` | German | Berlin | EUR | `ddc_de_berlin` |
| `EN` | English | Toronto | CAD | `ddc_en_toronto` |
| `ES` | Spanish | Barcelona | EUR | `ddc_sp_barcelona` |
| `FR` | French | Paris | EUR | `ddc_fr_paris` |
| `HI` | Hindi | Mumbai | INR | `ddc_hi_mumbai` |
| `PT` | Portuguese | São Paulo | BRL | `ddc_pt_saopaulo` |
| `RU` | Russian | St. Petersburg | RUB | `ddc_ru_stpetersburg` |
| `UK` | English | London | GBP | `ddc_uk_gbp` |
| `US` | English | USA | USD | `ddc_usa_usd` |
| `ZH` | Chinese | Shanghai | CNY | `ddc_zh_shanghai` |

### Derived tracks (19) - built by the DDC country-track build pipeline

| Code | Language | Region | Currency | Collection | Source track |
|------|----------|--------|----------|------------|--------------|
| `AU` | English | Sydney | AUD | `ddc_au_sydney` | UK_GBP |
| `BG` | Bulgarian | Sofia | BGN | `ddc_bg_sofia` | DE_BERLIN |
| `CS` | Czech | Prague | CZK | `ddc_cs_prague` | DE_BERLIN |
| `HR` | Croatian | Zagreb | EUR | `ddc_hr_zagreb` | DE_BERLIN |
| `ID` | Indonesian | Jakarta | IDR | `ddc_id_jakarta` | UK_GBP |
| `IT` | Italian | Rome | EUR | `ddc_it_rome` | DE_BERLIN |
| `JA` | Japanese | Tokyo | JPY | `ddc_ja_tokyo` | UK_GBP |
| `KO` | Korean | Seoul | KRW | `ddc_ko_seoul` | UK_GBP |
| `MX` | Spanish | Mexico City | MXN | `ddc_mx_mexicocity` | SP_BARCELONA |
| `NG` | English | Lagos | NGN | `ddc_ng_lagos` | UK_GBP |
| `NL` | Dutch | Amsterdam | EUR | `ddc_nl_amsterdam` | DE_BERLIN |
| `NZ` | English | Auckland | NZD | `ddc_nz_auckland` | UK_GBP |
| `PL` | Polish | Warsaw | PLN | `ddc_pl_warsaw` | DE_BERLIN |
| `RO` | Romanian | Bucharest | RON | `ddc_ro_bucharest` | DE_BERLIN |
| `SV` | Swedish | Stockholm | SEK | `ddc_sv_stockholm` | DE_BERLIN |
| `TH` | Thai | Bangkok | THB | `ddc_th_bangkok` | UK_GBP |
| `TR` | Turkish | Istanbul | TRY | `ddc_tr_istanbul` | DE_BERLIN |
| `VI` | Vietnamese | Hanoi | VND | `ddc_vi_hanoi` | UK_GBP |
| `ZA` | English | Johannesburg | ZAR | `ddc_za_johannesburg` | UK_GBP |

Snapshot path pattern for any track: `<CODE>___DDC_CWICR/<REGION>_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot`.

Derived tracks share the same `rate_code` and `resource_code` as their source - these are the alignment keys for cross-track comparison. Norms (labour hours, machine hours, resource quantities) are identical across all tracks; only prices and translatable text vary by region.

## Core Methodology

**Resource-Based Costing**: Separates unchanging production norms from volatile pricing.

```
Cost = Technology Norm × Regional Price
```

Each work item breaks down into:
- **Materials** - quantities and specifications
- **Labor** - worker hours by qualification
- **Equipment** - machine hours and fuel consumption

## Key Data Fields

### Work Item Identification
- `rate_code` - Unique identifier
- `rate_original_name` - Full description
- `rate_unit_of_measure` - Unit (m², m³, kg, etc.)

### Cost Breakdown
- `total_cost_per_position` - Total cost
- `total_material_cost` - Material costs
- `total_labor_cost` - Labor costs
- `total_machinery_cost` - Equipment costs

### Resources
- `material_*` - Material specifications
- `labor_*` - Labor hours and rates
- `machinery_*` - Equipment requirements

## n8n Workflows

The repository includes production-ready automation workflows:

1. **Text Estimator Bot** - Telegram interface for natural language descriptions
2. **Photo Analyzer** - GPT-4 Vision extracts elements from construction photos
3. **Universal Bot** - Combined text/photo/PDF input
4. **CAD/BIM Pipeline** - 10-stage pipeline for Revit/IFC/DWG → 4D/5D estimates

> **Important for AI Assistants**: These n8n workflows are **examples and templates** that demonstrate cost estimation logic. They can be:
> - Used as-is for quick deployment
> - Partially adapted for specific business requirements
> - Studied to understand the cost calculation methodology
> - Referenced when building custom integrations in any platform
>
> The workflows show how to: query the database, match work items, apply regional pricing, calculate totals, and generate reports. AI can analyze these workflows to understand the complete estimation logic and apply it to any business case.

## Integration Examples

### Python + Pandas
```python
import pandas as pd

df = pd.read_parquet("DDC_CWICR_EN.parquet")

# Find concrete work items
concrete = df[df['rate_original_name'].str.contains('concrete', case=False)]
print(concrete[['rate_code', 'rate_original_name', 'total_cost_per_position']])
```

### Qdrant Semantic Search
```python
from qdrant_client import QdrantClient
import openai

# Get embedding
response = openai.embeddings.create(
    model="text-embedding-3-large",
    input="reinforced concrete foundation"
)
embedding = response.data[0].embedding

# Search
client = QdrantClient("localhost", port=6333)
results = client.search(
    collection_name="ddc_en_toronto",
    query_vector=embedding,
    limit=5
)
```

## License

- **Database**: CC BY-NC 4.0 (free commercial use with attribution)
- **Code**: MIT (unrestricted use)

## Related Repository

For CAD/BIM conversion tools (Revit, IFC, DWG, DGN → Excel), see:
[cad2data-Revit-IFC-DWG-DGN-pipeline](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto)

---

*"The resource-based approach separates the unchanging laws of physics (labor hours, material consumption) from volatile economics (regional prices, inflation)."*
