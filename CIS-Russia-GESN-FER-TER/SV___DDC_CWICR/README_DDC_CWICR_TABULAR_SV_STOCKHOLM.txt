# OpenConstructionEstimate - Sweden / Stockholm

**Construction Work Items, Components & Resources**

---

| Property | Value |
|---|---|
| Reference region | Sweden / Stockholm |
| ISO country | SE |
| Language | `sv` |
| Currency | `SEK` (ISO 4217) |
| Source track | `DE_BERLIN` (Germany / Berlin) |
| Generated | 2026-04-30 |
| Work items | 900,225 rows |
| Unique resources | 6,671 |

## Available Formats

| Format | File |
|---|---|
| Parquet | `SV_STOCKHOLM_workitems_costs_resources_DDC_CWICR.parquet` |
| Excel (formatted) | `SV_STOCKHOLM_workitems_costs_resources_DDC_CWICR_FORMATTED.xlsx` |
| Excel (simple) | `SV_STOCKHOLM_workitems_costs_resources_DDC_CWICR_SIMPLE.xlsx` |
| Catalog CSV | `DDC_CWICR_SV_STOCKHOLM_Catalog.csv` |
| Catalog XLSX | `DDC_CWICR_SV_STOCKHOLM_Catalog.xlsx` |
| Qdrant snapshot | `SV_STOCKHOLM_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |

## How this track was built

This track was generated from `DE_BERLIN` by
the DDC country-track build pipeline.

- **Norms** (labour hours, machine hours, resource quantities) are
  identical to the source track - Resource-Based Costing methodology
  treats norms as country-agnostic physical first principles.
- **Prices** are derived via the cascade
  `type_factors → location_factor → optional national overrides`.
  Type factors come from OECD wage indexes (labour), construction
  PPP (material), and ECB FX (equipment). FX snapshot date is
  recorded in the per-resource columns.
- **Language** columns are translated where target language differs
  from source. Existing tracks are used as parallel-text seeds.

## Data Structure

85+ columns organised into:

- Classification hierarchy (10 cols)
- Rate / work-item identifiers (11 cols)
- Resource decomposition (7 cols)
- Labour metrics (11 cols)
- Machinery & equipment (12 cols)
- Price aggregates (16 cols)
- Mass / service / regional markers (~18 cols)

See the repository-level [DATA_DICTIONARY.md](../DATA_DICTIONARY.md)
for the complete column-by-column reference.

## Qdrant collection

Vector index built from concatenated localised text fields,
encoded with OpenAI `text-embedding-3-large` (3072-dim, cosine).

```bash
qdrant-client snapshot upload \
  --collection ddc_sv_stockholm \
  --snapshot SV_STOCKHOLM_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot
```

## Licence

Same as the parent dataset: CC BY-NC 4.0 for data, see
[LICENSE-DATA.txt](../LICENSE-DATA.txt). Code: see
[LICENSE-CODE.txt](../LICENSE-CODE.txt).
