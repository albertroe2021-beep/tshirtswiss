#!/bin/bash
# Fresh import attempt with proper parameters

COMPOSE_VALIDATION="/workspaces/tshirtswiss/wordpress-project/docker-compose.validation.yml"
KIT_FILE="/exports/tshirtswiss-kit.zip"

echo ""
echo "============================================"
echo "KIT IMPORT - FRESH ATTEMPT"
echo "============================================"
echo ""

run_validation() {
    docker compose -f "$COMPOSE_VALIDATION" run --rm wpcli "$@"
}

echo "Clearing previous pages (keeping defaults)..."
# First, let's see what we have
echo ""
echo "[1/5] Checking pages before import..."
page_count=$(run_validation wp post list --post_type=page --post_status=any --format=count --allow-root 2>&1 | tail -1)
echo "Pages in database: $page_count"
echo ""

echo "[2/5] Importing kit..."
echo "Command: wp elementor kit import $KIT_FILE --include=content,site-settings --sourceType=local --allow-root"
echo ""

# Run import with all relevant flags
import_output=$(run_validation wp elementor kit import "$KIT_FILE" \
  --include=content,site-settings \
  --sourceType=local \
  --allow-root 2>&1)

echo "$import_output"
echo ""

echo "[3/5] Pages after import..."
run_validation wp post list --post_type=page --post_status=publish \
  --fields=ID,post_title,post_name \
  --format=csv \
  --allow-root 2>&1 | head -30

echo ""
echo "[4/5] Sample page content check..."
# Get ID of first published page
page_id=$(run_validation wp post list --post_type=page --post_status=publish --format=json --allow-root 2>&1 | grep -o '"ID":[0-9]*' | head -1 | grep -o '[0-9]*')

if [ ! -z "$page_id" ]; then
    echo "Checking page ID $page_id for Elementor data..."
    run_validation wp db query "SELECT meta_key FROM wp_postmeta WHERE post_id = $page_id AND meta_key LIKE '%elementor%'" --allow-root 2>&1
else
    echo "No published pages found"
fi

echo ""
echo "[5/5] Checking CSS and metadata..."
run_validation wp elementor flush-css --allow-root 2>&1 | grep -i "success\|error" | head -5

echo ""
echo "============================================"
echo "IMPORT COMPLETE"
echo "============================================"
echo ""
