# Turkey construction cost base

**İnşaat ve Tesisat Birim Fiyatları**

Construction and installation unit prices. Part of the DDC CWICR collection of official national construction
cost bases, harmonised into one canonical format so every base loads into
OpenConstructionERP the same way and stays mergeable.

## What this base is

- Source system: Construction and installation unit prices (İnşaat ve Tesisat Birim Fiyatları).
- Issuer and edition: Ministry of Environment, Urbanisation and Climate Change (Cevre, Sehircilik ve Iklim Degisikligi Bakanligi).
- Content: 12,361 work items described through 97,700 resource lines
  (labour, material and machinery with norm quantities), unit prices in TRY.
- Native language: Turkish. Every work item keeps its original-language description;
  an English description is added through a glossary, Latin script only.

## Files

- `TR_workitems_costs_resources_DDC_CWICR.parquet` - the full base in the
  canonical 95-column CWICR master schema (source currency, native plus English).
- `DDC_CWICR_TR_Catalog.csv` and `.xlsx` - the compact resource catalog: one
  row per unique resource with price statistics, usage counts and classification.
- `markets/` - the base repriced and translated for 48 target markets, each as a compact
  catalog in the market currency and language (World Bank PPP is used for the repricing).
  An Excel workbook view of the base, the full resource-level parquet and the
  vector snapshots for the market editions follow in the next release.

## Data quality (measured, honest)

98 percent of positions named, 100 percent carry a unit, prices carried. Resource categories are 98.7 percent tagged from the Turkish resource names.

The national ministry unit-price analyses decomposed into labour, material and machinery. The source base leaves some codes without a scope row and a few duplicate codes; this is a structural quirk of the source and is reported, not restructured.

## How to use it

Load the parquet into OpenConstructionERP as region `TR_NATIONAL` to browse the work
items with their resource breakdown, or import the compact catalog to browse the
resource master. Both metric and US customary output are supported by the platform.

## License

Data: Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) for the DDC
compilation, plus a separate DDC commercial license for commercial use. Free for
research, teaching, evaluation and non-profit use. See the repository `LICENSE` and
`PROVENANCE.md` in this folder for the source terms and the attribution to preserve.

## Attribution

Insaat ve Tesisat Birim Fiyatlari, Cevre, Sehircilik ve Iklim Degisikligi Bakanligi (Ministry of Environment, Urbanisation and Climate Change), Turkey.

## Contact

Commercial license and questions: info@datadrivenconstruction.io
Website: https://datadrivenconstruction.io
