//! 02 - Qdrant Vector Search (Rust)
//!
//! Connects to a Qdrant instance and searches the DDC-CWICR construction cost
//! collection using a sample embedding vector.
//!
//! Usage:
//!   cargo run -p qdrant-search
//!
//! Environment variables:
//!   QDRANT_URL  - Qdrant gRPC endpoint (default: http://localhost:6334)
//!   QDRANT_KEY  - Optional API key for authentication

use qdrant_client::prelude::*;
use qdrant_client::qdrant::vectors_config::Config;
use qdrant_client::qdrant::{SearchPoints, VectorsConfig};
use serde_json::Value;
use std::env;

/// Collection name in Qdrant
const COLLECTION: &str = "ddc_en_toronto";

/// Number of results to return
const TOP_K: u64 = 5;

/// Embedding dimensions (text-embedding-3-large)
const EMBEDDING_DIMS: usize = 3072;

/// Payload fields we want to display
const DISPLAY_FIELDS: &[&str] = &[
    "rate_code",
    "rate_original_name",
    "rate_final_name",
    "rate_unit",
    "department_name",
    "section_name",
    "total_cost_per_position",
    "total_material_cost_per_position",
    "resource_name",
    "labor_hours_construction_workers",
];

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let qdrant_url = env::var("QDRANT_URL").unwrap_or_else(|_| "http://localhost:6334".into());
    let qdrant_key = env::var("QDRANT_KEY").ok();

    println!("\nConnecting to Qdrant at {}...\n", qdrant_url);

    // -----------------------------------------------------------------------
    // Initialize the Qdrant client
    // -----------------------------------------------------------------------
    let mut config = QdrantClientConfig::from_url(&qdrant_url);
    if let Some(key) = qdrant_key {
        config.set_api_key(&key);
    }
    let client = QdrantClient::new(Some(config))?;

    // -----------------------------------------------------------------------
    // List collections and verify ours exists
    // -----------------------------------------------------------------------
    let collections = client.list_collections().await?;
    let names: Vec<String> = collections
        .collections
        .iter()
        .map(|c| c.name.clone())
        .collect();
    println!("Available collections: {}", names.join(", "));

    if !names.contains(&COLLECTION.to_string()) {
        eprintln!(
            "\nCollection '{}' not found. Available: {}",
            COLLECTION,
            names.join(", ")
        );
        std::process::exit(1);
    }

    // Get collection info
    let info = client.collection_info(COLLECTION).await?;
    if let Some(cfg) = &info.result {
        if let Some(VectorsConfig {
            config: Some(Config::Params(params)),
        }) = &cfg.config.as_ref().and_then(|c| c.params.as_ref()).map(|_| {
            // Just print basic info
            println!("Collection '{}' found.", COLLECTION);
            VectorsConfig { config: None }
        })
        {
            let _ = params;
        }
        if let Some(status) = &cfg.status {
            println!("  Status       : {:?}", status);
        }
        println!(
            "  Points count : {}",
            cfg.points_count.unwrap_or(0)
        );
    }
    println!();

    // -----------------------------------------------------------------------
    // Create a sample query vector
    // -----------------------------------------------------------------------
    // In a real application you would call the OpenAI Embeddings API to get
    // a vector from a text query. Here we use a deterministic sample vector
    // for demonstration purposes.
    println!("Generating sample query vector ({} dims)...", EMBEDDING_DIMS);
    println!("(In production, use the OpenAI Embeddings API to embed your query text.)\n");

    let query_vector: Vec<f32> = (0..EMBEDDING_DIMS)
        .map(|i| {
            // Deterministic pseudo-random values for reproducibility
            let x = (i as f64 * 0.01).sin() as f32 * 0.1;
            x
        })
        .collect();

    // -----------------------------------------------------------------------
    // Search Qdrant
    // -----------------------------------------------------------------------
    println!(
        "Searching collection '{}' for top {} results...\n",
        COLLECTION, TOP_K
    );

    let search_result = client
        .search_points(&SearchPoints {
            collection_name: COLLECTION.into(),
            vector: query_vector,
            limit: TOP_K,
            with_payload: Some(true.into()),
            ..Default::default()
        })
        .await?;

    // -----------------------------------------------------------------------
    // Display results
    // -----------------------------------------------------------------------
    println!("=== Search Results ===\n");

    if search_result.result.is_empty() {
        println!("  No results found.");
    }

    for (i, point) in search_result.result.iter().enumerate() {
        println!("--- Result {} (score: {:.4}) ---", i + 1, point.score);

        for field in DISPLAY_FIELDS {
            let value = point
                .payload
                .get(*field)
                .map(|v| format_qdrant_value(v))
                .unwrap_or_else(|| "N/A".to_string());
            println!("  {:<30} {}", field, value);
        }
        println!();
    }

    println!("Done.");
    Ok(())
}

/// Format a Qdrant payload value for display.
fn format_qdrant_value(value: &qdrant_client::qdrant::Value) -> String {
    use qdrant_client::qdrant::value::Kind;
    match &value.kind {
        Some(Kind::StringValue(s)) => s.clone(),
        Some(Kind::DoubleValue(d)) => format!("{:.2}", d),
        Some(Kind::IntegerValue(i)) => i.to_string(),
        Some(Kind::BoolValue(b)) => b.to_string(),
        Some(Kind::NullValue(_)) => "null".to_string(),
        _ => format!("{:?}", value),
    }
}
