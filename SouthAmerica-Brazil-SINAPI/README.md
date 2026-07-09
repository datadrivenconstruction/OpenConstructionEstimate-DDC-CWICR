# Brazil construction cost base

**SINAPI**

National system of construction cost and index research (SINAPI). Part of the DDC CWICR collection of official national construction
cost bases, harmonised into one canonical format so every base loads into
OpenConstructionERP the same way and stays mergeable.

## What this base is

- Source system: National system of construction cost and index research (SINAPI) (SINAPI).
- Issuer and edition: CAIXA and IBGE, analytical compositions; price layer Paraiba, 2022-12, Nao Desonerado.
- Content: 9,723 work items described through 52,188 resource lines
  (labour, material and machinery with norm quantities), unit prices in BRL (SINAPI Paraiba, 2022-12, Nao Desonerado).
- Native language: Portuguese. Every work item keeps its original-language description;
  an English description is added through a glossary, Latin script only.

## Files

- `BR_workitems_costs_resources_DDC_CWICR.parquet` - the full base in the
  canonical 95-column CWICR master schema (source currency, native plus English).
- `DDC_CWICR_BR_Catalog.csv` and `.xlsx` - the compact resource catalog: one
  row per unique resource with price statistics, usage counts and classification.
- `markets/` - the base repriced and translated for 48 target markets, each as a compact
  catalog in the market currency and language (World Bank PPP is used for the repricing).
  An Excel workbook view of the base, the full resource-level parquet and the
  vector snapshots for the market editions follow in the next release.

## Data quality (measured, honest)

100 percent of positions named. 92.6 percent of resources carry a price and 72.2 percent of positions carry the official ready unit cost; the rest are summed from priced resources.

National SINAPI analytical compositions, priced with the official SINAPI price layer (Paraiba, 2022-12, Nao Desonerado). The national coefficients are unchanged and the price layer is swappable for another state or month.

## How to use it

Load the parquet into OpenConstructionERP as region `BR_NATIONAL` to browse the work
items with their resource breakdown, or import the compact catalog to browse the
resource master. Both metric and US customary output are supported by the platform.

## License

Data: Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) for the DDC
compilation, plus a separate DDC commercial license for commercial use. Free for
research, teaching, evaluation and non-profit use. See the repository `LICENSE` and
`PROVENANCE.md` in this folder for the source terms and the attribution to preserve.

## Attribution

Fonte: SINAPI - CAIXA / IBGE.

## Contact

Commercial license and questions: info@datadrivenconstruction.io
Website: https://datadrivenconstruction.io
