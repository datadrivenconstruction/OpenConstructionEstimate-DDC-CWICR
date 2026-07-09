# Claude Code Instructions for DDC CWICR

> This file provides Claude Code with specific instructions for working with the DDC CWICR construction cost database.

## Repository Overview

**DDC CWICR** is an open-source construction cost database with:
- 55,719 work items (строительные работы)
- 27,672 resources (materials, labor, equipment)
- **30 country tracks across 23 languages** (11 shipped + 19 derived)
- Pre-computed OpenAI embeddings (3072d) for semantic search
- Qdrant vector database integration

## Data Access Patterns

### 1. Load Parquet Data (Recommended)
```python
import pandas as pd

# Load the database
df = pd.read_parquet("DDC_CWICR_EN.parquet")

# Explore structure
print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
print(df.columns.tolist())
```

### 2. Semantic Search with Qdrant
```python
from qdrant_client import QdrantClient
import openai

# Create embedding for search query
def get_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-3-large",
        input=text
    )
    return response.data[0].embedding

# Search for similar work items
client = QdrantClient("localhost", port=6333)
results = client.search(
    collection_name="ddc_en_toronto",  # or ddc_de_berlin, ddc_ru_stpetersburg, etc.
    query_vector=get_embedding("brick masonry wall"),
    limit=10
)

for result in results:
    print(f"{result.payload['rate_code']}: {result.payload['rate_original_name']}")
    print(f"  Cost: {result.payload['total_cost_per_position']}")
```

### 3. Filter by Category
```python
# Find all concrete work
concrete = df[df['rate_original_name'].str.contains('concrete|бетон', case=False, na=False)]

# Find by category code
category_01 = df[df['rate_code'].str.startswith('01-')]
```

## Key Columns Reference

### Identification
| Column | Description |
|--------|-------------|
| `rate_code` | Unique work item code |
| `rate_original_name` | Full description |
| `rate_unit_of_measure` | Unit (m², m³, kg, pcs) |

### Cost Breakdown
| Column | Description |
|--------|-------------|
| `total_cost_per_position` | Total cost per unit |
| `total_material_cost` | Materials subtotal |
| `total_labor_cost` | Labor subtotal |
| `total_machinery_cost` | Equipment subtotal |

### Classification
| Column | Description |
|--------|-------------|
| `category_name` | Main category |
| `department_name` | Department |
| `section_name` | Section |

## Common Tasks

### Task: Find Work Item by Description
```python
query = "reinforced concrete foundation"
matches = df[df['rate_original_name'].str.contains(query, case=False, na=False)]
print(matches[['rate_code', 'rate_original_name', 'total_cost_per_position', 'rate_unit_of_measure']])
```

### Task: Calculate Project Cost
```python
# Given quantities from BIM
quantities = {
    "01-01-001": 150,  # m³ of concrete
    "01-02-003": 2000, # kg of rebar
    "05-01-010": 500,  # m² of brick wall
}

total = 0
for code, qty in quantities.items():
    row = df[df['rate_code'] == code].iloc[0]
    cost = row['total_cost_per_position'] * qty
    total += cost
    print(f"{code}: {qty} × {row['total_cost_per_position']} = {cost}")

print(f"Total: {total}")
```

### Task: Export Cost Breakdown
```python
# Get detailed breakdown for a work item
code = "01-01-001"
item = df[df['rate_code'] == code].iloc[0]

print(f"Work Item: {item['rate_original_name']}")
print(f"Unit: {item['rate_unit_of_measure']}")
print(f"\nCost Breakdown:")
print(f"  Materials: {item['total_material_cost']}")
print(f"  Labor: {item['total_labor_cost']}")
print(f"  Equipment: {item['total_machinery_cost']}")
print(f"  TOTAL: {item['total_cost_per_position']}")
```

## Qdrant Collections

Snapshot path pattern: `<CODE>___DDC_CWICR/<REGION>_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot`.

### Shipped (11)

| Collection | Language | Region | Currency |
|------------|----------|--------|----------|
| `ddc_ar_dubai` | Arabic | Dubai | AED |
| `ddc_de_berlin` | German | Berlin | EUR |
| `ddc_en_toronto` | English | Toronto | CAD |
| `ddc_sp_barcelona` | Spanish | Barcelona | EUR |
| `ddc_fr_paris` | French | Paris | EUR |
| `ddc_hi_mumbai` | Hindi | Mumbai | INR |
| `ddc_pt_saopaulo` | Portuguese | São Paulo | BRL |
| `ddc_ru_stpetersburg` | Russian | St. Petersburg | RUB |
| `ddc_uk_gbp` | English | London | GBP |
| `ddc_usa_usd` | English | USA | USD |
| `ddc_zh_shanghai` | Chinese | Shanghai | CNY |

### Derived (19) - built by the DDC country-track build pipeline

| Collection | Language | Region | Currency | Source |
|------------|----------|--------|----------|--------|
| `ddc_au_sydney` | English | Sydney | AUD | UK_GBP |
| `ddc_bg_sofia` | Bulgarian | Sofia | BGN | DE_BERLIN |
| `ddc_cs_prague` | Czech | Prague | CZK | DE_BERLIN |
| `ddc_hr_zagreb` | Croatian | Zagreb | EUR | DE_BERLIN |
| `ddc_id_jakarta` | Indonesian | Jakarta | IDR | UK_GBP |
| `ddc_it_rome` | Italian | Rome | EUR | DE_BERLIN |
| `ddc_ja_tokyo` | Japanese | Tokyo | JPY | UK_GBP |
| `ddc_ko_seoul` | Korean | Seoul | KRW | UK_GBP |
| `ddc_mx_mexicocity` | Spanish | Mexico City | MXN | SP_BARCELONA |
| `ddc_ng_lagos` | English | Lagos | NGN | UK_GBP |
| `ddc_nl_amsterdam` | Dutch | Amsterdam | EUR | DE_BERLIN |
| `ddc_nz_auckland` | English | Auckland | NZD | UK_GBP |
| `ddc_pl_warsaw` | Polish | Warsaw | PLN | DE_BERLIN |
| `ddc_ro_bucharest` | Romanian | Bucharest | RON | DE_BERLIN |
| `ddc_sv_stockholm` | Swedish | Stockholm | SEK | DE_BERLIN |
| `ddc_th_bangkok` | Thai | Bangkok | THB | UK_GBP |
| `ddc_tr_istanbul` | Turkish | Istanbul | TRY | DE_BERLIN |
| `ddc_vi_hanoi` | Vietnamese | Hanoi | VND | UK_GBP |
| `ddc_za_johannesburg` | English | Johannesburg | ZAR | UK_GBP |

Derived tracks share `rate_code` and `resource_code` with their source. Norms (labour hours, machine hours, resource quantities) are bytewise-identical across all tracks; only prices and translatable text differ. They are produced by the DDC country-track build pipeline.

## n8n Workflows

The repository includes ready-to-use n8n workflows:

| # | Workflow | Purpose |
|---|----------|---------|
| 1 | Text Estimator Bot | Telegram bot for text descriptions |
| 2 | Photo Analyzer | GPT-4 Vision for construction photos |
| 3 | Universal Bot | Combined text/photo/PDF input |
| 4 | CAD/BIM Pipeline | Revit/IFC/DWG → 4D/5D estimates |

> **Note**: These n8n workflows are **examples and templates** demonstrating the cost estimation logic. They can be used fully or partially for any business case. Analyze these workflows to understand how cost calculations work: database queries, work item matching, pricing logic, and report generation. This understanding can be applied to build custom solutions on any platform.

## Example Prompts for Claude Code

| Task | Prompt |
|------|--------|
| Find items | "Search for all work items related to waterproofing" |
| Calculate cost | "Calculate total cost for 100m³ of concrete foundation" |
| Compare prices | "Compare labor costs for brick vs concrete walls" |
| Export data | "Export all electrical work items to Excel" |
| Build pipeline | "Create a Python script that takes quantities CSV and outputs cost estimate" |
| Semantic search | "Set up Qdrant and search for 'exterior wall insulation'" |

## Best Practices

1. **Use Parquet** - Much faster than CSV or Excel for large datasets
2. **Cache embeddings** - Don't recompute for repeated queries
3. **Match units** - Always verify `rate_unit_of_measure` matches your quantities
4. **Check language** - Use appropriate collection for target region
5. **Validate codes** - Work item codes may differ between languages

## Related Resources

- **Live Demo**: [openconstructionestimate.com](https://openconstructionestimate.com)
- **CAD/BIM Tools**: [cad2data Repository](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto)
- **Data & Snapshots**: Stored directly in the repository language folders via Git LFS (e.g., `EN___DDC_CWICR/`)
