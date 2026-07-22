#!/bin/bash

echo "=== Testing Elementor CLI Commands ==="
echo ""

cd /workspaces/tshirtswiss/wordpress-project

echo "1. Checking if elementor CLI is available..."
docker compose run --rm wpcli wp elementor 2>&1 | grep -i "usage\|error\|command" | head -5

echo ""
echo "2. Checking for kit subcommand..."
docker compose run --rm wpcli wp elementor kit 2>&1 | grep -i "usage\|error\|command" | head -5

echo ""
echo "3. Attempting to export kit..."
mkdir -p /tmp/elementor-test
docker compose run --rm wpcli wp elementor kit export /tmp/elementor-test/test.zip --allow-root 2>&1 | head -10

echo ""
echo "4. Check if export succeeded..."
ls -lh /tmp/elementor-test/ 2>&1 || echo "Directory not found or empty"

echo ""
echo "Done."
