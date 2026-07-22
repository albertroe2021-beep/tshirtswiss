#!/bin/bash
# Step 2: WordPress Installation
# Installs WordPress, activates Elementor and Hello Elementor theme

echo "=== Step 2: WordPress Installation ==="
echo ""

cd /workspaces/tshirtswiss/wordpress-project

echo "Installing WordPress..."
docker compose run --rm wpcli wp core install \
    --url="http://localhost:8088" \
    --title="TShirtSwiss" \
    --admin_user="admin" \
    --admin_password="password" \
    --admin_email="admin@local.test" \
    --allow-root

echo ""
echo "Verifying installation..."
docker compose run --rm wpcli wp core is-installed --allow-root

echo ""
echo "Activating Elementor plugin..."
docker compose run --rm wpcli wp plugin activate elementor --allow-root

echo ""
echo "Activating Hello Elementor theme..."
docker compose run --rm wpcli wp theme activate hello-elementor --allow-root

echo ""
echo "✓ WordPress ready with Elementor"
echo "  Admin: http://localhost:8088/wp-admin/"
echo "  User: admin / password"
