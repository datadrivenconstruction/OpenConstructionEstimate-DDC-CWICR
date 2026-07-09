# Spain construction cost base

**BCCA (Banco de Costes de la Construcción de Andalucía)**

Construction cost base of Andalusia (BCCA). Part of the DDC CWICR collection of official national construction
cost bases, harmonised into one canonical format so every base loads into
OpenConstructionERP the same way and stays mergeable.

## What this base is

- Source system: Construction cost base of Andalusia (BCCA) (BCCA (Banco de Costes de la Construcción de Andalucía)).
- Issuer and edition: Junta de Andalucia, BCCA 2023.
- Content: 6,453 work items described through 31,129 resource lines
  (labour, material and machinery with norm quantities), unit prices in EUR.
- Native language: Spanish. Every work item keeps its original-language description;
  an English description is added through a glossary, Latin script only.

## Files

- `ES_ANDALUCIA_workitems_costs_resources_DDC_CWICR.parquet` - the full base in the
  canonical 95-column CWICR master schema (source currency, native plus English).
- `DDC_CWICR_ES_ANDALUCIA_Catalog.csv` and `.xlsx` - the compact resource catalog: one
  row per unique resource with price statistics, usage counts and classification.
- `markets/` - the base repriced and translated for 48 target markets, each as a compact
  catalog in the market currency and language (World Bank PPP is used for the repricing).
  An Excel workbook view of the base, the full resource-level parquet and the
  vector snapshots for the market editions follow in the next release.

## Data quality (measured, honest)

100 percent of positions named, 100 percent carry a unit. The resource buildup reconciles to the published partida price for 6,445 of 6,453 items.

Full analytical decomposition with unit prices across 19 capitulos.

## How to use it

Load the parquet into OpenConstructionERP as region `ES_ANDALUCIA` to browse the work
items with their resource breakdown, or import the compact catalog to browse the
resource master. Both metric and US customary output are supported by the platform.

## License

Data: Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) for the DDC
compilation, plus a separate DDC commercial license for commercial use. Free for
research, teaching, evaluation and non-profit use. See the repository `LICENSE` and
`PROVENANCE.md` in this folder for the source terms and the attribution to preserve.

## Attribution

Banco de Costes de la Construccion de Andalucia (BCCA), Junta de Andalucia.

## Contact

Commercial license and questions: info@datadrivenconstruction.io
Website: https://datadrivenconstruction.io
