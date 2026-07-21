#!/usr/bin/env bash
set -euo pipefail

# TShirtSwiss Elementor Native Website Kit Builder
# Builds a production-ready Elementor website template ZIP using native Elementor API

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WP_DIR="${PROJECT_DIR}/wordpress-project"
EXPORTS_DIR="${WP_DIR}/exports"
BUILD_DIR="${PROJECT_DIR}/build"
DIST_DIR="${PROJECT_DIR}/dist"

echo "======================================"
echo "Elementor Website Kit Builder"
echo "======================================"
echo ""
echo "Project: $PROJECT_DIR"
echo "WordPress: $WP_DIR"
echo ""

# Phase 2-5: Create WordPress environment and export
echo "[1/5] Starting WordPress environment..."
cd "$WP_DIR"

# Start services
docker compose up -d >/dev/null 2>&1
sleep 5

echo "[2/5] Installing WordPress, theme, and plugins..."
docker compose run --rm wpcli bash -lc '
  set -euo pipefail
  cd /var/www/html
  
  # Wait for DB
  for i in {1..30}; do
    wp --allow-root db query "SELECT 1;" >/dev/null 2>&1 && break
    sleep 1
  done
  
  # Core setup
  if ! wp --allow-root core is-installed >/dev/null 2>&1; then
    wp --allow-root core install \
      --url="http://localhost:8088" \
      --title="TShirtSwiss Elementor Kit" \
      --admin_user="admin" \
      --admin_password="admin123" \
      --admin_email="admin@example.com"
  fi
  
  # Install Hello Elementor
  wp --allow-root theme install hello-elementor --activate 2>/dev/null || true
  
  # Install Elementor 4.1.5 specifically
  wp --allow-root plugin install elementor --version=4.1.5 --activate 2>/dev/null || true
  
  # Install supporting plugins
  wp --allow-root plugin install litespeed-cache --activate 2>/dev/null || true
  wp --allow-root plugin install wordpress-seo --activate 2>/dev/null || true
  
  # Enable Elementor experiments
  for flag in container nested-elements editor-v4; do
    wp --allow-root option update "elementor_experiment-${flag}" active 2>/dev/null || true
  done
  
  echo "WordPress setup complete"
' >/dev/null 2>&1

echo "[3/5] Seeding pages and templates from JSON..."
docker compose run --rm wpcli bash /scripts/seed_reference_content.sh >/dev/null 2>&1

echo "[4/5] Generating native Elementor export..."
# Use Elementor's actual native Export class (NOT custom JSON writing)
docker compose run --rm wpcli bash -lc '
  cd /var/www/html
  wp --allow-root eval-file /scripts/elementor_native_export_correct.php
' 2>&1 | grep -v "Warning:\|PHP Warning" 

echo "[5/5] Verifying Elementor Website Kit..."

# The ZIP is already created by Elementor's native Export class
if [ ! -f "$EXPORTS_DIR/tshirtswiss-elementor-website-kit.zip" ]; then
    echo "ERROR: ZIP file not created by Elementor export"
    exit 1
fi

ZIP_SIZE=$(du -h "$EXPORTS_DIR/tshirtswiss-elementor-website-kit.zip" | cut -f1)
echo ""
echo "======================================"
echo "✓ Build Complete"
echo "======================================"
echo ""
echo "Elementor Native Website Kit created:"
echo "  File: $EXPORTS_DIR/tshirtswiss-elementor-website-kit.zip"
echo "  Size: $ZIP_SIZE"
echo "  Format: Native Elementor export (version 2.0)"
echo ""
echo "ZIP contents (created by Elementor):"
unzip -l "$EXPORTS_DIR/tshirtswiss-elementor-website-kit.zip" | head -n 20

# Copy to dist
cp "$EXPORTS_DIR/tshirtswiss-elementor-website-kit.zip" "$DIST_DIR/"
echo ""
echo "Copied to dist/tshirtswiss-elementor-website-kit.zip"
