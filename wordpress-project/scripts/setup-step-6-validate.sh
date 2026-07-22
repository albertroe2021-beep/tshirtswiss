#!/bin/bash
# Step 6: Validation on Fresh WordPress
# Tests importing the exported Website Kit on a clean WordPress install

echo "=== Step 6: Validation - Fresh Import Test ==="
echo ""

cd /workspaces/tshirtswiss/wordpress-project

echo "Checking for exported ZIP..."
if [ ! -f "exports/tshirtswiss-elementor-kit.zip" ]; then
    echo "✗ Export file not found: exports/tshirtswiss-elementor-kit.zip"
    echo "  Please run Step 5 and export the kit first"
    exit 1
fi

echo "✓ Export file found"
echo ""

echo "Setting up fresh WordPress for validation..."
docker compose -f docker-compose.validation.yml down --remove-orphans 2>/dev/null || true
docker compose -f docker-compose.validation.yml up -d
sleep 10

echo "Installing WordPress..."
docker compose -f docker-compose.validation.yml run --rm wpcli wp core install \
    --url="http://localhost:8089" \
    --title="TShirtSwiss Validation" \
    --admin_user="admin" \
    --admin_password="password" \
    --admin_email="admin@validation.test" \
    --allow-root

echo ""
echo "Activating Elementor..."
docker compose -f docker-compose.validation.yml run --rm wpcli wp plugin activate elementor --allow-root
docker compose -f docker-compose.validation.yml run --rm wpcli wp theme activate hello-elementor --allow-root

echo ""
echo "Importing Website Kit..."
echo "(This may take 30-60 seconds)"
docker compose -f docker-compose.validation.yml run --rm wpcli wp elementor kit import \
    --file=/exports/tshirtswiss-elementor-kit.zip \
    --allow-root

echo ""
echo "Verifying import..."
echo "Pages imported:"
docker compose -f docker-compose.validation.yml run --rm wpcli wp post list \
    --post_type=page --format=count --allow-root

echo ""
echo "✓ Validation setup complete"
echo ""
echo "Test the imported site:"
echo "  URL: http://localhost:8089"
echo "  Admin: http://localhost:8089/wp-admin/"
echo "  User: admin / password"
echo ""
echo "Verify:"
echo "  1. All 24 pages are present"
echo "  2. Pages render without errors"
echo "  3. Elementor editor works on imported pages"
echo "  4. No PHP errors in logs"
