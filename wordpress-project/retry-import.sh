#!/bin/bash
# Retry kit import with proper admin user context

COMPOSE_VALIDATION="/workspaces/tshirtswiss/wordpress-project/docker-compose.validation.yml"
KIT_FILE="/workspaces/tshirtswiss/wordpress-project/exports/tshirtswiss-kit.zip"

echo ""
echo "============================================"
echo "KIT IMPORT WITH ADMIN USER CONTEXT"
echo "============================================"
echo ""

run_validation() {
    docker compose -f "$COMPOSE_VALIDATION" run --rm wpcli "$@"
}

echo "[1/3] Verifying admin user..."
run_validation wp user list --fields=ID,user_login --format=json --allow-root 2>&1 | grep admin

echo ""
echo "[2/3] Importing kit as admin user..."
echo "Command: wp elementor kit import /exports/tshirtswiss-kit.zip --user=admin --allow-root"
echo ""

import_result=$(run_validation wp elementor kit import /exports/tshirtswiss-kit.zip --user=admin --allow-root 2>&1)
echo "$import_result"
echo ""

echo "[3/3] Listing imported pages..."
run_validation wp post list --post_type=page --post_status=publish --fields=ID,post_title,post_name --format=table --allow-root | head -20

echo ""
echo "============================================"
