# Indonesia construction cost base

**AHSP (Analisa Harga Satuan Pekerjaan)**

Unit price analysis of work (AHSP). Part of the DDC CWICR collection of official national construction
cost bases, harmonised into one canonical format so every base loads into
OpenConstructionERP the same way and stays mergeable.

## What this base is

- Source system: Unit price analysis of work (AHSP) (AHSP (Analisa Harga Satuan Pekerjaan)).
- Issuer and edition: Ministry of Public Works and Housing (Kementerian PUPR), editions 2016 and 2022.
- Content: 2,784 work items described through 15,692 resource lines
  (labour, material and machinery with norm quantities), resource coefficients (prices are set regionally, so the money columns are empty).
- Native language: Indonesian. Every work item keeps its original-language description;
  an English description is added through a glossary, Latin script only.

## Files

- `ID_workitems_costs_resources_DDC_CWICR.parquet` - the full base in the
  canonical 95-column CWICR master schema (source currency, native plus English).
- `DDC_CWICR_ID_Catalog.csv` and `.xlsx` - the compact resource catalog: one
  row per unique resource with price statistics, usage counts and classification.
- `markets/` - the base repriced and translated for 48 target markets, each as a compact
  catalog in the market currency and language (World Bank PPP is used for the repricing).
  An Excel workbook view of the base, the full resource-level parquet and the
  vector snapshots for the market editions follow in the next release.

## Data quality (measured, honest)

100 percent of positions named, 100 percent of resources named. Prices are regional and are not part of the national norm.

Coefficient base: labour man-days, material and equipment coefficients per unit of work. Editions 2016 and 2022 are tagged per item.

## How to use it

Load the parquet into OpenConstructionERP as region `ID_NATIONAL` to browse the work
items with their resource breakdown, or import the compact catalog to browse the
resource master. Both metric and US customary output are supported by the platform.

## License

Data: Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) for the DDC
compilation, plus a separate DDC commercial license for commercial use. Free for
research, teaching, evaluation and non-profit use. See the repository `LICENSE` and
`PROVENANCE.md` in this folder for the source terms and the attribution to preserve.

## Attribution

Analisa Harga Satuan Pekerjaan (AHSP), Kementerian PUPR, Indonesia.

## Contact

Commercial license and questions: info@datadrivenconstruction.io
Website: https://datadrivenconstruction.io
