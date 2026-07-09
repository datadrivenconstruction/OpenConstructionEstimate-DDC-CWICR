#!/usr/bin/env bash
#
# api-examples.sh - cURL examples for the Qdrant REST API.
#
# Demonstrates common API operations against the DDC-CWICR Qdrant database:
#   1. List collections
#   2. Get collection info
#   3. Scroll (paginate) points
#   4. Search by vector
#   5. Search with filters
#
# Usage:
#   chmod +x api-examples.sh
#   ./api-examples.sh
#
# Environment variables:
#   QDRANT_URL  - Qdrant HTTP endpoint (default: http://localhost:6333)
#   QDRANT_KEY  - Optional API key

set -euo pipefail

QDRANT_URL="${QDRANT_URL:-http://localhost:6333}"
QDRANT_KEY="${QDRANT_KEY:-}"
COLLECTION="ddc_en_toronto"

# Build auth header if API key is set
AUTH_HEADER=""
if [ -n "${QDRANT_KEY}" ]; then
    AUTH_HEADER="-H \"api-key: ${QDRANT_KEY}\""
fi

info() { echo -e "\n\033[1;34m=== $* ===\033[0m\n"; }

# ---------------------------------------------------------------------------
# 1. List all collections
# ---------------------------------------------------------------------------

info "1. List Collections"

echo "curl -s ${QDRANT_URL}/collections"
echo ""
curl -s ${AUTH_HEADER} "${QDRANT_URL}/collections" | python3 -m json.tool 2>/dev/null || \
curl -s ${AUTH_HEADER} "${QDRANT_URL}/collections"

# ---------------------------------------------------------------------------
# 2. Get collection info
# ---------------------------------------------------------------------------

info "2. Collection Info: ${COLLECTION}"

echo "curl -s ${QDRANT_URL}/collections/${COLLECTION}"
echo ""
curl -s ${AUTH_HEADER} "${QDRANT_URL}/collections/${COLLECTION}" | python3 -m json.tool 2>/dev/null || \
curl -s ${AUTH_HEADER} "${QDRANT_URL}/collections/${COLLECTION}"

# ---------------------------------------------------------------------------
# 3. Scroll (paginate) points - first 3 points with payload
# ---------------------------------------------------------------------------

info "3. Scroll Points (first 3)"

echo 'curl -s -X POST ${QDRANT_URL}/collections/${COLLECTION}/points/scroll \'
echo '  -H "Content-Type: application/json" \'
echo '  -d {"limit": 3, "with_payload": true, "with_vector": false}'
echo ""

curl -s -X POST ${AUTH_HEADER} \
    "${QDRANT_URL}/collections/${COLLECTION}/points/scroll" \
    -H "Content-Type: application/json" \
    -d '{
        "limit": 3,
        "with_payload": true,
        "with_vector": false
    }' | python3 -m json.tool 2>/dev/null || \
curl -s -X POST ${AUTH_HEADER} \
    "${QDRANT_URL}/collections/${COLLECTION}/points/scroll" \
    -H "Content-Type: application/json" \
    -d '{"limit": 3, "with_payload": true, "with_vector": false}'

# ---------------------------------------------------------------------------
# 4. Search by vector (sample vector - first 10 dims shown, rest zeros)
# ---------------------------------------------------------------------------

info "4. Search by Vector"

# Generate a sample vector with 3072 dimensions.
# In practice, you would use the OpenAI Embeddings API to get a real vector.
# Here we use a Python one-liner to create a valid JSON array.
SAMPLE_VECTOR=$(python3 -c "
import math, json
vec = [math.sin(i * 0.01) * 0.1 for i in range(3072)]
print(json.dumps(vec))
" 2>/dev/null || echo "[]")

if [ "${SAMPLE_VECTOR}" = "[]" ]; then
    echo "  Skipping: Python3 is required to generate the sample vector."
else
    echo "curl -s -X POST ${QDRANT_URL}/collections/${COLLECTION}/points/search (3072-dim vector)"
    echo ""

    curl -s -X POST ${AUTH_HEADER} \
        "${QDRANT_URL}/collections/${COLLECTION}/points/search" \
        -H "Content-Type: application/json" \
        -d "{
            \"vector\": ${SAMPLE_VECTOR},
            \"limit\": 3,
            \"with_payload\": true
        }" | python3 -m json.tool 2>/dev/null || echo "(raw response omitted for brevity)"
fi

# ---------------------------------------------------------------------------
# 5. Search with filters
# ---------------------------------------------------------------------------

info "5. Search with Filters (unit = m2, max cost = 500)"

if [ "${SAMPLE_VECTOR}" != "[]" ]; then
    echo 'Filtering: rate_unit == "m2" AND total_cost_per_position <= 500'
    echo ""

    curl -s -X POST ${AUTH_HEADER} \
        "${QDRANT_URL}/collections/${COLLECTION}/points/search" \
        -H "Content-Type: application/json" \
        -d "{
            \"vector\": ${SAMPLE_VECTOR},
            \"limit\": 3,
            \"with_payload\": true,
            \"filter\": {
                \"must\": [
                    {
                        \"key\": \"rate_unit\",
                        \"match\": {\"value\": \"m2\"}
                    },
                    {
                        \"key\": \"total_cost_per_position\",
                        \"range\": {\"lte\": 500}
                    }
                ]
            }
        }" | python3 -m json.tool 2>/dev/null || echo "(raw response omitted for brevity)"
else
    echo "  Skipping: Python3 is required to generate the sample vector."
fi

# ---------------------------------------------------------------------------

info "Done"

echo "All examples completed. For production use, replace the sample vector"
echo "with a real embedding from the OpenAI text-embedding-3-large model."
echo ""
