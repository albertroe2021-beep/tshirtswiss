#!/bin/bash
# Setup validation WordPress for import testing

set -e

echo "=== VALIDATION WORDPRESS SETUP ==="
echo "Installing WordPress core..."
wp core install \
    --url=http://localhost:8089 \
    --title="TShirtSwiss Validation" \
    --admin_user=admin \
    --admin_password=admin123 \
    --admin_email=admin@example.com \
    --allow-root

echo "✓ WordPress installed"

echo ""
echo "Installing Hello Elementor theme..."
wp theme install hello-elementor --activate --allow-root

echo ""
echo "Installing Elementor 4.2.0..."
wp plugin install elementor --activate --version=4.2.0 --allow-root

echo ""
echo "Activating required Elementor experiments..."
wp option update elementor_active_experiments '{
  "e_font_icon_svg": "active",
  "additional_custom_breakpoints": "active",
  "container": "active",
  "e_optimized_markup": "active",
  "hello-theme-header-footer": "active",
  "nested-elements": "active"
}' --allow-root

echo ""
echo "Flushing permalinks..."
wp rewrite flush --allow-root

echo ""
echo "✅ Validation WordPress ready at: http://localhost:8089"
echo "Admin: admin / admin123"
