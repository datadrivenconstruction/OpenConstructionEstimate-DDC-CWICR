# 11 - Offline Cost Estimator

Search DDC CWICR work items and price a bill of quantities directly against
a local Parquet file. No Qdrant, no OpenAI/Anthropic API key, no network
access - everything runs against data already on disk.

This is a lighter alternative to `03-cost-estimation-text` /
`05-boq-generation` / `06-rag-pipeline` for cases where you don't have (or
don't want to set up) Qdrant + an LLM API key, or you already know roughly
which work items you need and just want the numbers.

## Scripts

- **offline_estimate.py** - `search` a track by keyword, or `estimate` a
  bill of quantities from `--item` flags or a CSV.

## Prerequisites

- Python 3.9+
- `pip install pandas pyarrow`

No API keys or external services required.

## Usage

```bash
# Search for matching work items in the default track (EN / Toronto)
python offline_estimate.py search "concrete foundation"

# Search a different track
python offline_estimate.py --path "../../../../CIS-Russia-GESN-FER-TER/DE___DDC_CWICR/DE_BERLIN_workitems_costs_resources_DDC_CWICR.parquet" search "Betonfundament"

# Estimate cost for a small BOQ (quantities inline)
python offline_estimate.py estimate \
  --item "concrete foundation:150:m3" \
  --item "brick wall:500:m2"

# Estimate from a CSV (columns: item, quantity, unit)
python offline_estimate.py estimate --csv my_boq.csv --out estimate_result.csv
```

`--item` tokens can be an exact `rate_code` or a free-text search string -
free text resolves to the first (highest-ranked) text match, so check the
`search` output first if you want a specific item rather than whatever
matches first.

## Notes

- The default `--path` points at the English/Toronto track
  (`CIS-Russia-GESN-FER-TER/EN___DDC_CWICR/...`). Point `--path` at any
  other track's `*_workitems_costs_resources_DDC_CWICR.parquet` file to
  price against a different region/language.
- The raw dataset has one row per (work item x resource/scope line); this
  script dedups to one row per `rate_code` before searching/pricing.
- Many `rate_unit` values bake in a block multiplier (e.g. `"100 m2"`,
  `"1000 m3"`, `"10 pcs"` - priced per that block, not per single unit).
  The script parses this automatically and normalizes to a per-single-unit
  rate, so a `--item "...:500:m2"` quantity prices correctly regardless of
  whether the source item is quoted per m2, per 100 m2, or per 1000 m2.
  `search` shows the original packaging in the `priced_per` column.
- Material / Labor-Resource / Equipment are informational subtotals from
  the source data and may not sum exactly to the total unit cost.
