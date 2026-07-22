#!/bin/bash
# Step 4: Verification
# Verifies all pages are created and populated with Elementor

echo "=== Step 4: Verification ==="
echo ""

cd /workspaces/tshirtswiss/wordpress-project

echo "Listing all created pages:"
docker compose run --rm wpcli wp post list --post_type=page --format=table --fields=ID,post_title --allow-root

echo ""
echo "Checking Elementor data:"
echo "Pages with Elementor content:"
docker compose run --rm wpcli wp db query \
    "SELECT COUNT(*) as pages_with_elementor FROM wp_postmeta WHERE meta_key='_elementor_data'" \
    --allow-root

echo ""
echo "✓ Verification complete"
echo ""
echo "Next: Access WordPress and review pages"
echo "  URL: http://localhost:8088"
