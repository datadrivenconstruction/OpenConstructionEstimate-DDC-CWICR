//! 01 - Load and Explore CWICR Parquet Data (Rust)
//!
//! Reads a CWICR Parquet file, prints the schema, previews the first 10 rows,
//! and computes basic statistics on cost columns.
//!
//! Usage:
//!   cargo run -p load-parquet [path_to_parquet]

use std::env;
use std::fs::File;
use std::sync::Arc;

use arrow::array::{ArrayRef, Float64Array, StringArray};
use arrow::datatypes::DataType;
use arrow::record_batch::RecordBatch;
use arrow::util::pretty::print_batches;
use parquet::arrow::arrow_reader::ParquetRecordBatchReaderBuilder;

/// Default path to the sample Parquet file (relative to the workspace root).
const DEFAULT_PATH: &str = "../sample-data/sample_cwicr_en_100rows.parquet";

/// Columns to preview in the first-10-rows table.
const PREVIEW_COLUMNS: &[&str] = &[
    "rate_code",
    "rate_original_name",
    "rate_unit",
    "department_name",
    "total_cost_per_position",
];

/// Numeric columns for which we compute basic statistics.
const STATS_COLUMNS: &[&str] = &[
    "total_cost_per_position",
    "total_material_cost_per_position",
    "resource_price_per_unit_eur_current",
    "labor_hours_construction_workers",
];

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let path = env::args().nth(1).unwrap_or_else(|| DEFAULT_PATH.to_string());
    println!("\nLoading Parquet file: {}\n", path);

    let file = File::open(&path)?;
    let builder = ParquetRecordBatchReaderBuilder::try_new(file)?;

    // -----------------------------------------------------------------------
    // 1. Print the schema
    // -----------------------------------------------------------------------
    let schema = builder.schema().clone();
    println!("=== Schema ({} columns) ===\n", schema.fields().len());
    for field in schema.fields() {
        println!("  {:<50} {:?}", field.name(), field.data_type());
    }
    println!();

    // -----------------------------------------------------------------------
    // Read all record batches
    // -----------------------------------------------------------------------
    let reader = ParquetRecordBatchReaderBuilder::try_new(File::open(&path)?)?
        .with_batch_size(1024)
        .build()?;

    let batches: Vec<RecordBatch> = reader.collect::<Result<Vec<_>, _>>()?;
    let total_rows: usize = batches.iter().map(|b| b.num_rows()).sum();
    println!("Total rows: {}\n", total_rows);

    // -----------------------------------------------------------------------
    // 2. Preview first 10 rows (selected columns)
    // -----------------------------------------------------------------------
    println!("=== First 10 Rows (selected columns) ===\n");

    // Build a projection of selected columns from the first batch(es)
    let mut preview_rows = 0;
    let mut preview_batches: Vec<RecordBatch> = Vec::new();

    for batch in &batches {
        if preview_rows >= 10 {
            break;
        }
        let take = std::cmp::min(10 - preview_rows, batch.num_rows());

        let columns: Vec<ArrayRef> = PREVIEW_COLUMNS
            .iter()
            .map(|name| {
                let idx = batch.schema().index_of(name).unwrap();
                batch.column(idx).slice(0, take)
            })
            .collect();

        let fields: Vec<_> = PREVIEW_COLUMNS
            .iter()
            .map(|name| {
                let idx = schema.index_of(name).unwrap();
                schema.field(idx).clone()
            })
            .collect();

        let preview_schema = Arc::new(arrow::datatypes::Schema::new(fields));
        let preview_batch = RecordBatch::try_new(preview_schema, columns)?;
        preview_batches.push(preview_batch);
        preview_rows += take;
    }

    print_batches(&preview_batches)?;
    println!();

    // -----------------------------------------------------------------------
    // 3. Basic statistics for cost columns
    // -----------------------------------------------------------------------
    println!("=== Basic Statistics ===\n");

    for col_name in STATS_COLUMNS {
        let col_idx = match schema.index_of(col_name) {
            Ok(idx) => idx,
            Err(_) => {
                println!("  Column '{}' not found - skipping.\n", col_name);
                continue;
            }
        };

        // Collect all non-null float values
        let mut values: Vec<f64> = Vec::new();
        for batch in &batches {
            let col = batch.column(col_idx);
            match col.data_type() {
                DataType::Float64 => {
                    let arr = col.as_any().downcast_ref::<Float64Array>().unwrap();
                    for i in 0..arr.len() {
                        if !arr.is_null(i) {
                            values.push(arr.value(i));
                        }
                    }
                }
                DataType::Utf8 => {
                    // Some columns might be stored as strings; try to parse
                    let arr = col.as_any().downcast_ref::<StringArray>().unwrap();
                    for i in 0..arr.len() {
                        if !arr.is_null(i) {
                            if let Ok(v) = arr.value(i).parse::<f64>() {
                                values.push(v);
                            }
                        }
                    }
                }
                _ => {
                    println!(
                        "  Column '{}' has unsupported type {:?} - skipping.\n",
                        col_name,
                        col.data_type()
                    );
                    continue;
                }
            }
        }

        if values.is_empty() {
            println!("  {}: no numeric values\n", col_name);
            continue;
        }

        values.sort_by(|a, b| a.partial_cmp(b).unwrap());

        let count = values.len();
        let sum: f64 = values.iter().sum();
        let mean = sum / count as f64;
        let min = values[0];
        let max = values[count - 1];
        let median = if count % 2 == 0 {
            (values[count / 2 - 1] + values[count / 2]) / 2.0
        } else {
            values[count / 2]
        };

        println!("  {}", col_name);
        println!("    count  : {}", count);
        println!("    min    : {:.2}", min);
        println!("    max    : {:.2}", max);
        println!("    mean   : {:.2}", mean);
        println!("    median : {:.2}", median);
        println!();
    }

    println!("Done.");
    Ok(())
}
