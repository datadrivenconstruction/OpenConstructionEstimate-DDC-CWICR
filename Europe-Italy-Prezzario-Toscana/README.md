# Italy construction cost base

**Prezzario Regionale della Toscana**

Regional price list of Tuscany. Part of the DDC CWICR collection of official national construction
cost bases, harmonised into one canonical format so every base loads into
OpenConstructionERP the same way and stays mergeable.

## What this base is

- Source system: Regional price list of Tuscany (Prezzario Regionale della Toscana).
- Issuer and edition: Regione Toscana, Prezzario 2026.
- Content: 5,836 work items described through 41,635 resource lines
  (labour, material and machinery with norm quantities), unit prices in EUR.
- Native language: Italian. Every work item keeps its original-language description;
  an English description is added through a glossary, Latin script only.

## Files

- `IT_TOSCANA_workitems_costs_resources_DDC_CWICR.parquet` - the full base in the
  canonical 95-column CWICR master schema (source currency, native plus English).
- `DDC_CWICR_IT_TOSCANA_Catalog.csv` and `.xlsx` - the compact resource catalog: one
  row per unique resource with price statistics, usage counts and classification.
- `markets/` - the base repriced and translated for 48 target markets, each as a compact
  catalog in the market currency and language (World Bank PPP is used for the repricing).
  An Excel workbook view of the base, the full resource-level parquet and the
  vector snapshots for the market editions follow in the next release.

## Data quality (measured, honest)

100 percent of positions named, 100 percent carry a unit. The resource buildup reconciles to the base price for every item that publishes an analysis.

total_cost_per_position is the final tendered unit price (it includes about 27 percent overhead and profit); the pure resource sum is the base price. They differ by the legal markup by design. 5,369 of 5,836 items carry a full resource breakdown; 467 are price-only catalogue items with no published analysis.

## How to use it

Load the parquet into OpenConstructionERP as region `IT_TOSCANA` to browse the work
items with their resource breakdown, or import the compact catalog to browse the
resource master. Both metric and US customary output are supported by the platform.

## License

Data: Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) for the DDC
compilation, plus a separate DDC commercial license for commercial use. Free for
research, teaching, evaluation and non-profit use. See the repository `LICENSE` and
`PROVENANCE.md` in this folder for the source terms and the attribution to preserve.

## Attribution

Regione Toscana, Prezzario 2026 (CC BY 4.0).

## Contact

Commercial license and questions: info@datadrivenconstruction.io
Website: https://datadrivenconstruction.io
