#!/bin/bash
# Fresh validation setup and import

COMPOSE_VALIDATION="/workspaces/tshirtswiss/wordpress-project/docker-compose.validation.yml"
KIT_FILE="/workspaces/tshirtswiss/wordpress-project/exports/tshirtswiss-kit.zip"

echo ""
echo "================================"
echo "FRESH VALIDATION SETUP"
echo "================================"
echo ""

echo "[1/7] Stopping validation environment..."
docker compose -f "$COMPOSE_VALIDATION" down --remove-orphans 2>&1 | grep -i "removed\|stopped" || echo "  (no containers running)"

echo ""
echo "[2/7] Starting fresh validation environment..."
docker compose -f "$COMPOSE_VALIDATION" up -d
sleep 15
docker compose -f "$COMPOSE_VALIDATION" ps

echo ""
echo "[3/7] Running setup script..."
docker compose -f "$COMPOSE_VALIDATION" run --rm wpcli bash /scripts/setup_wordpress.sh 2>&1 | tail -20

echo ""
echo "[4/7] Verifying Elementor is activated..."
docker compose -f "$COMPOSE_VALIDATION" run --rm wpcli wp plugin list --allow-root 2>&1 | grep -i "elementor\|hello"

echo ""
echo "[5/7] Checking WordPress admin..."
docker compose -f "$COMPOSE_VALIDATION" run --rm wpcli wp user get 1 --field=user_login --allow-root

echo ""
echo "[6/7] Checking available commands..."
docker compose -f "$COMPOSE_VALIDATION" run --rm wpcli wp elementor kit --allow-root 2>&1 | head -30

echo ""
echo "[7/7] Attempting import..."
docker compose -f "$COMPOSE_VALIDATION" run --rm wpcli wp elementor kit import "$KIT_FILE" --allow-root 2>&1 | tail -10

echo ""
echo "================================"
echo "SETUP COMPLETE"
echo "================================"
