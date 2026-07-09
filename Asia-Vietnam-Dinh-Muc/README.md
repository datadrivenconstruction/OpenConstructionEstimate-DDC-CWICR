# Vietnam construction cost base

**Định mức xây dựng**

National construction norms (Dinh muc du toan). Part of the DDC CWICR collection of official national construction
cost bases, harmonised into one canonical format so every base loads into
OpenConstructionERP the same way and stays mergeable.

## What this base is

- Source system: National construction norms (Dinh muc du toan) (Định mức xây dựng).
- Issuer and edition: Ministry of Construction, Appendix II of Circular 12/2021/TT-BXD.
- Content: 4,299 work items described through 23,450 resource lines
  (labour, material and machinery with norm quantities), resource coefficients (provincial don gia price them, so the money columns are empty).
- Native language: Vietnamese. Every work item keeps its original-language description;
  an English description is added through a glossary, Latin script only.

## Files

- `VN_workitems_costs_resources_DDC_CWICR.parquet` - the full base in the
  canonical 95-column CWICR master schema (source currency, native plus English).
- `DDC_CWICR_VN_Catalog.csv` and `.xlsx` - the compact resource catalog: one
  row per unique resource with price statistics, usage counts and classification.
- `markets/` - the base repriced and translated for 48 target markets, each as a compact
  catalog in the market currency and language (World Bank PPP is used for the repricing).
  An Excel workbook view of the base, the full resource-level parquet and the
  vector snapshots for the market editions follow in the next release.

## Data quality (measured, honest)

100 percent of positions named, 98 percent of resources named (508 rows lost a name token in the compact source tables).

Coefficient base: materials, a labour line in cong (man-days) with a trade grade, and machine lines in ca (machine-shifts). 4,299 leaf norms across 13 chapters.

## How to use it

Load the parquet into OpenConstructionERP as region `VN_NATIONAL` to browse the work
items with their resource breakdown, or import the compact catalog to browse the
resource master. Both metric and US customary output are supported by the platform.

## License

Data: Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) for the DDC
compilation, plus a separate DDC commercial license for commercial use. Free for
research, teaching, evaluation and non-profit use. See the repository `LICENSE` and
`PROVENANCE.md` in this folder for the source terms and the attribution to preserve.

## Attribution

Dinh muc xay dung, Vien Kinh te xay dung, Ministry of Construction, Vietnam.

## Contact

Commercial license and questions: info@datadrivenconstruction.io
Website: https://datadrivenconstruction.io
