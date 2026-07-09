# 02 - Qdrant REST API Quickstart

## Description

Demonstrates how to search the DDC-CWICR vector database by making raw HTTP
requests to the Qdrant REST API using the built-in `fetch()` API. No Qdrant
client library is needed - just plain HTTP.

The script embeds a query string with the OpenAI Embeddings API and then posts
the resulting vector to the Qdrant `/points/search` endpoint.

## Prerequisites

- Node.js >= 18 (for native `fetch`)
- A running Qdrant instance (default: `http://localhost:6333`)
- The `ddc_en_toronto` collection loaded with CWICR embeddings
- An OpenAI API key exported as `OPENAI_API_KEY`

## Usage

```bash
export OPENAI_API_KEY="sk-..."
node search_api.mjs
```

You can customise the query, collection, and Qdrant URL by editing the
constants at the top of the script.
