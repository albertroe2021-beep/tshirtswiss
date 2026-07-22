#!/bin/bash
# TShirtSwiss Elementor Site - Complete Setup & Export Workflow
#
# This script:
# 1. Brings up fresh WordPress + Elementor environment
# 2. Creates all pages (main + representative categories)
# 3. Populates with Elementor content
# 4. Exports Website Kit
# 5. Prepares for validation

set -e

WORDPRESS_DIR="/workspaces/tshirtswiss/wordpress-project"
SCRIPT_DIR="$WORDPRESS_DIR/scripts"
EXPORTS_DIR="$WORDPRESS_DIR/exports"

echo ""
echo "=============================================================="
echo "TShirtSwiss - Elementor Website Kit Builder"
echo "=============================================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Step 1: Start containers
echo -e "${YELLOW}1️⃣  Starting Docker containers...${NC}"
cd "$WORDPRESS_DIR"
docker compose down 2>/dev/null || true
docker compose up -d
sleep 12
echo -e "${GREEN}✓ Containers running${NC}"
echo ""

# Step 2: Fresh WordPress install
echo -e "${YELLOW}2️⃣  Setting up fresh WordPress installation...${NC}"
docker compose run --rm wpcli wp db reset --yes --allow-root >/dev/null 2>&1 || true
docker compose run --rm wpcli wp core install \
    --url="http://localhost:8088" \
    --title="TShirtSwiss" \
    --admin_user="admin" \
    --admin_password="password" \
    --admin_email="admin@local.test" \
    --allow-root >/dev/null 2>&1
echo -e "${GREEN}✓ WordPress fresh install${NC}"
echo ""

# Step 3: Activate Elementor and theme
echo -e "${YELLOW}3️⃣  Activating Elementor and Hello Elementor theme...${NC}"
docker compose run --rm wpcli wp plugin activate elementor --allow-root >/dev/null 2>&1
docker compose run --rm wpcli wp theme activate hello-elementor --allow-root >/dev/null 2>&1
sleep 2
echo -e "${GREEN}✓ Elementor active${NC}"
echo ""

# Step 4: Initialize site structure and content
echo -e "${YELLOW}4️⃣  Building Elementor pages and content...${NC}"
docker compose run --rm wpcli wp eval-file "$SCRIPT_DIR/init-elementor-site.php" --allow-root
echo ""

# Step 5: Summary and next steps
echo -e "${GREEN}=============================================================="
echo "✓ Site Building Complete!"
echo "==============================================================${NC}"
echo ""
echo "Pages created:"
docker compose run --rm wpcli wp post list --post_type=page --format=count --allow-root
echo ""
echo -e "${YELLOW}Access WordPress:${NC}"
echo "  URL: http://localhost:8088"
echo "  User: admin"
echo "  Password: password"
echo ""
echo -e "${YELLOW}Edit pages in Elementor:${NC}"
echo "  1. Log in to WordPress admin"
echo "  2. Go to Pages"
echo "  3. Edit each page with Elementor"
echo "  4. Make adjustments as needed"
echo ""
echo -e "${YELLOW}Export Website Kit:${NC}"
echo "  1. Go to Elementor > Tools > Export Kit"
echo "  2. Export all pages"
echo "  3. Save to: $EXPORTS_DIR/tshirtswiss-elementor-kit.zip"
echo ""
echo "=============================================================="
echo ""
