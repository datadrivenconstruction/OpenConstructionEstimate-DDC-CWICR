# China construction cost base

**定额 (预算定额)**

Construction consumption quotas (Dinge), valued under GB 50500. Part of the DDC CWICR collection of official national construction
cost bases, harmonised into one canonical format so every base loads into
OpenConstructionERP the same way and stays mergeable.

## What this base is

- Source system: Construction consumption quotas (Dinge), valued under GB 50500 (定额 (预算定额)).
- Issuer and edition: Beijing municipal construction quota (2012).
- Content: 11,312 work items described through 61,007 resource lines
  (labour, material and machinery with norm quantities), unit prices in CNY.
- Native language: Chinese. Every work item keeps its original-language description;
  an English description is added through a glossary, Latin script only.

## Files

- `ZH_CHINA_workitems_costs_resources_DDC_CWICR.parquet` - the full base in the
  canonical 95-column CWICR master schema (source currency, native plus English).
- `DDC_CWICR_ZH_CHINA_Catalog.csv` and `.xlsx` - the compact resource catalog: one
  row per unique resource with price statistics, usage counts and classification.
- `markets/` - the base repriced and translated for 48 target markets, each as a compact
  catalog in the market currency and language (World Bank PPP is used for the repricing).
  An Excel workbook view of the base, the full resource-level parquet and the
  vector snapshots for the market editions follow in the next release.

## Data quality (measured, honest)

92 percent of positions named and 99 percent carry a unit. Every work item is fully decomposed into labour, material and machinery norms, and 95 percent of the resource lines resolve to a name.

Distinct works are counted, not region-code pairs. This edition is the Beijing municipal consumption quota, where every work item carries its full resource composition, so quantities and unit prices can be traced line by line.

## How to use it

Load the parquet into OpenConstructionERP as region `ZH_CHINA` to browse the work
items with their resource breakdown, or import the compact catalog to browse the
resource master. Both metric and US customary output are supported by the platform.

## License

Data: Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) for the DDC
compilation, plus a separate DDC commercial license for commercial use. Free for
research, teaching, evaluation and non-profit use. See the repository `LICENSE` and
`PROVENANCE.md` in this folder for the source terms and the attribution to preserve.

## Attribution

Beijing municipal construction quota (2012), People's Republic of China.

## Contact

Commercial license and questions: info@datadrivenconstruction.io
Website: https://datadrivenconstruction.io
