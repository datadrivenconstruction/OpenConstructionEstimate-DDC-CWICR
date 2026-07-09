# 03 - Semantic Search with Qdrant Client

## Description

Perform semantic search against the DDC-CWICR Qdrant collection using the
official `@qdrant/js-client-rest` SDK and OpenAI embeddings. This is the
recommended approach for production use - the client handles retries,
connection pooling, and typed responses.

## Prerequisites

- Node.js >= 18
- Install dependencies from the parent directory:
  ```bash
  cd examples/javascript
  npm install
  ```
- A running Qdrant instance with the `ddc_en_toronto` collection
- An OpenAI API key exported as `OPENAI_API_KEY`

## Usage

```bash
export OPENAI_API_KEY="sk-..."
node basic_search.mjs
```

You can optionally set `QDRANT_URL` (default `http://localhost:6333`) and
`QDRANT_API_KEY` if your instance requires authentication.
