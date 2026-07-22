#!/bin/bash
# Step 3: Page Structure Creation
# Creates all 24 pages with basic Elementor structure

echo "=== Step 3: Creating Page Structure ==="
echo ""

cd /workspaces/tshirtswiss/wordpress-project

echo "Building pages..."
docker compose run --rm wpcli wp eval-file scripts/init-elementor-site.php --allow-root

echo ""
echo "Verifying page count..."
echo "Total pages created:"
docker compose run --rm wpcli wp post list --post_type=page --format=count --allow-root

echo ""
echo "✓ Pages structure complete"
