#!/bin/bash
# Elementor CLI Export/Import Workflow Script
# This script uses docker exec to avoid terminal paging issues

set -e

COMPOSE_FILE="/workspaces/tshirtswiss/wordpress-project/docker-compose.yml"
COMPOSE_VALIDATION="/workspaces/tshirtswiss/wordpress-project/docker-compose.validation.yml"

echo "================================"
echo "ELEMENTOR KIT EXPORT/IMPORT TEST"
echo "================================"
echo ""

# Function to run command in builder WordPress
run_builder() {
    docker compose -f "$COMPOSE_FILE" run --rm wpcli "$@"
}

# Function to run command in validation WordPress  
run_validation() {
    docker compose -f "$COMPOSE_VALIDATION" run --rm wpcli "$@"
}

echo "[1/6] Checking if builder WordPress is ready..."
run_builder wp option get siteurl --allow-root > /tmp/site_url.txt 2>&1
SITE_URL=$(cat /tmp/site_url.txt)
echo "Builder site: $SITE_URL"
echo ""

echo "[2/6] Checking Elementor installation..."
run_builder wp plugin list --allow-root --format=json | grep -q elementor
echo "✓ Elementor plugin found"
echo ""

echo "[3/6] Attempting Elementor kit export..."
export_output=$(run_builder wp elementor kit export /exports/tshirtswiss-kit.zip --allow-root 2>&1)
echo "$export_output"
echo ""

if [ -f "/workspaces/tshirtswiss/wordpress-project/exports/tshirtswiss-kit.zip" ]; then
    ZIP_SIZE=$(ls -lh /workspaces/tshirtswiss/wordpress-project/exports/tshirtswiss-kit.zip | awk '{print $5}')
    echo "✓ Export succeeded! Size: $ZIP_SIZE"
else
    echo "⚠ Export file not found in expected location"

fi
echo ""

echo "[4/6] Checking validation WordPress..."
run_validation wp option get siteurl --allow-root > /tmp/validation_url.txt 2>&1
VALIDATION_URL=$(cat /tmp/validation_url.txt)
echo "Validation site: $VALIDATION_URL"
echo ""

echo "[5/6] Importing kit on validation site..."
if [ -f "/workspaces/tshirtswiss/wordpress-project/exports/tshirtswiss-kit.zip" ]; then
    import_output=$(run_validation wp elementor kit import /exports/tshirtswiss-kit.zip --allow-root 2>&1)
    echo "$import_output"
else
    echo "ERROR: No kit file to import"

fi
echo ""

echo "[6/6] Verifying imported pages..."
run_validation wp post list --post_type=page --post_status=publish --fields=ID,post_title --allow-root
echo ""

echo "================================"
echo "WORKFLOW COMPLETE"
echo "================================"
