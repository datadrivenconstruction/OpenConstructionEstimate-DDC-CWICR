# 08 - Data Analysis

Exploratory data analysis (EDA) of the CWICR dataset. Generates charts showing cost distributions, labour vs material ratios, top expensive items, and resource utilisation patterns.

## Scripts

| Script | Description |
|---|---|
| `cwicr_analysis.py` | Full EDA pipeline that produces multiple PNG charts |

## Charts Generated

- `cost_distribution_by_department.png` - Box plot of total costs per department
- `labor_vs_material_ratio.png` - Scatter plot comparing labour and material cost components
- `top_expensive_items.png` - Horizontal bar chart of the most expensive work items
- `resource_utilization.png` - Bar chart of resource usage frequency and average quantity
- `labor_hours_distribution.png` - Histogram of construction worker labour hours

## Prerequisites

```bash
pip install pandas pyarrow matplotlib plotly python-dotenv kaleido
```

`kaleido` is needed only if you want Plotly charts saved as static images.

## Usage

```bash
# Analyse the default EN Toronto dataset
python cwicr_analysis.py

# Specify a different parquet file
python cwicr_analysis.py --file ../../data/DE___DDC_CWICR/DE_BERLIN_workitems_costs_resources_DDC_CWICR.parquet

# Change output directory
python cwicr_analysis.py --outdir ./charts
```
