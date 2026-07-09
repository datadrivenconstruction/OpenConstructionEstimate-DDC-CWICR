#!/usr/bin/env bash
#
# setup-qdrant.sh - Download snapshot, start Qdrant in Docker, import, verify.
#
# This script:
#   1. Downloads the CWICR Qdrant snapshot from the GitHub release
#   2. Starts a Qdrant container via Docker
#   3. Imports the snapshot into Qdrant
#   4. Verifies the collection is healthy
#
# Usage:
#   chmod +x setup-qdrant.sh
#   ./setup-qdrant.sh
#
# Environment variables:
#   QDRANT_PORT        - Qdrant HTTP port (default: 6333)
#   QDRANT_GRPC_PORT   - Qdrant gRPC port (default: 6334)
#   QDRANT_STORAGE     - Local directory for Qdrant storage (default: ./qdrant_storage)
#   SNAPSHOT_URL       - URL to download the snapshot (will be prompted if not set)
#   COLLECTION_NAME    - Collection name to create (default: ddc_en_toronto)

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

QDRANT_PORT="${QDRANT_PORT:-6333}"
QDRANT_GRPC_PORT="${QDRANT_GRPC_PORT:-6334}"
QDRANT_STORAGE="${QDRANT_STORAGE:-./qdrant_storage}"
QDRANT_URL="http://localhost:${QDRANT_PORT}"
COLLECTION_NAME="${COLLECTION_NAME:-ddc_en_toronto}"
CONTAINER_NAME="qdrant-cwicr"
SNAPSHOT_DIR="./snapshots"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

info()  { echo -e "\033[1;34m[INFO]\033[0m  $*"; }
ok()    { echo -e "\033[1;32m[OK]\033[0m    $*"; }
error() { echo -e "\033[1;31m[ERROR]\033[0m $*"; exit 1; }

wait_for_qdrant() {
    info "Waiting for Qdrant to be ready..."
    local retries=30
    while [ $retries -gt 0 ]; do
        if curl -s "${QDRANT_URL}/healthz" > /dev/null 2>&1; then
            ok "Qdrant is ready."
            return 0
        fi
        retries=$((retries - 1))
        sleep 1
    done
    error "Qdrant did not start within 30 seconds."
}

# ---------------------------------------------------------------------------
# Step 1: Download snapshot
# ---------------------------------------------------------------------------

info "Step 1: Downloading Qdrant snapshot..."

mkdir -p "${SNAPSHOT_DIR}"

if [ -z "${SNAPSHOT_URL:-}" ]; then
    echo ""
    echo "  Please provide the snapshot download URL."
    echo "  You can find it on the GitHub Releases page of the repository."
    echo ""
    read -rp "  Snapshot URL: " SNAPSHOT_URL
fi

SNAPSHOT_FILE="${SNAPSHOT_DIR}/$(basename "${SNAPSHOT_URL}")"

if [ -f "${SNAPSHOT_FILE}" ]; then
    info "Snapshot already downloaded: ${SNAPSHOT_FILE}"
else
    info "Downloading from: ${SNAPSHOT_URL}"
    curl -L -o "${SNAPSHOT_FILE}" "${SNAPSHOT_URL}"
    ok "Downloaded: ${SNAPSHOT_FILE}"
fi

# ---------------------------------------------------------------------------
# Step 2: Start Qdrant Docker container
# ---------------------------------------------------------------------------

info "Step 2: Starting Qdrant Docker container..."

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    error "Docker is not installed or not in PATH."
fi

# Stop existing container if running
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    info "Stopping existing container '${CONTAINER_NAME}'..."
    docker stop "${CONTAINER_NAME}" > /dev/null 2>&1 || true
    docker rm "${CONTAINER_NAME}" > /dev/null 2>&1 || true
fi

mkdir -p "${QDRANT_STORAGE}"

docker run -d \
    --name "${CONTAINER_NAME}" \
    -p "${QDRANT_PORT}:6333" \
    -p "${QDRANT_GRPC_PORT}:6334" \
    -v "$(pwd)/${QDRANT_STORAGE}:/qdrant/storage" \
    -v "$(pwd)/${SNAPSHOT_DIR}:/snapshots:ro" \
    qdrant/qdrant:latest

ok "Qdrant container started: ${CONTAINER_NAME}"

wait_for_qdrant

# ---------------------------------------------------------------------------
# Step 3: Import snapshot
# ---------------------------------------------------------------------------

info "Step 3: Importing snapshot into collection '${COLLECTION_NAME}'..."

# Check if the collection already exists
COLLECTION_EXISTS=$(curl -s "${QDRANT_URL}/collections/${COLLECTION_NAME}" | grep -c '"status":"ok"' || true)

if [ "${COLLECTION_EXISTS}" -gt 0 ]; then
    info "Collection '${COLLECTION_NAME}' already exists. Skipping import."
else
    # Upload the snapshot
    SNAPSHOT_BASENAME=$(basename "${SNAPSHOT_FILE}")

    curl -s -X POST \
        "${QDRANT_URL}/collections/${COLLECTION_NAME}/snapshots/upload" \
        -H "Content-Type: multipart/form-data" \
        -F "snapshot=@${SNAPSHOT_FILE}" \
        | python3 -m json.tool 2>/dev/null || true

    ok "Snapshot imported."
fi

# ---------------------------------------------------------------------------
# Step 4: Verify
# ---------------------------------------------------------------------------

info "Step 4: Verifying collection..."

COLLECTION_INFO=$(curl -s "${QDRANT_URL}/collections/${COLLECTION_NAME}")

echo ""
echo "  Collection info:"
echo "${COLLECTION_INFO}" | python3 -m json.tool 2>/dev/null || echo "${COLLECTION_INFO}"
echo ""

POINTS_COUNT=$(echo "${COLLECTION_INFO}" | python3 -c "
import sys, json
data = json.load(sys.stdin)
print(data.get('result', {}).get('points_count', 'unknown'))
" 2>/dev/null || echo "unknown")

ok "Collection '${COLLECTION_NAME}' has ${POINTS_COUNT} points."
echo ""
info "Qdrant is running at: ${QDRANT_URL}"
info "Dashboard: ${QDRANT_URL}/dashboard"
info "gRPC endpoint: localhost:${QDRANT_GRPC_PORT}"
echo ""
ok "Setup complete!"
