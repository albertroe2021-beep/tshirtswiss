#!/bin/bash
# Import kit using Elementor's REST API endpoint

VALIDATION_URL="http://tshirtswiss-validation-wordpress:80"
KIT_FILE="/workspaces/tshirtswiss/wordpress-project/exports/tshirtswiss-kit.zip"

echo ""
echo "================================"
echo "ELEMENTOR KIT IMPORT VIA REST API"
echo "================================"
echo ""

echo "[1/3] Preparing kit file..."
if [ ! -f "$KIT_FILE" ]; then
    echo "ERROR: Kit file not found"
    exit 1
fi

echo "File: $KIT_FILE"
echo "Size: $(ls -lh "$KIT_FILE" | awk '{print $5}')"
echo ""

echo "[2/3] Getting WordPress admin user credentials..."
COMPOSE_VALIDATION="/workspaces/tshirtswiss/wordpress-project/docker-compose.validation.yml"

# Get admin username and password from setup (defaults)
ADMIN_USER="admin"
ADMIN_PASS="password123"

echo "Using: $ADMIN_USER"
echo ""

echo "[3/3] Uploading and importing kit via REST..."
echo ""

# The Elementor kit import REST endpoint is typically:
# POST /wp-json/elementor/v1/import-kit

# First, authenticate and get auth token
echo "Authenticating..."
curl -s -X POST \
  "$VALIDATION_URL/wp-json/jwt-auth/v1/token" \
  -H "Content-Type: application/json" \
  -d "{\"username\":\"$ADMIN_USER\",\"password\":\"$ADMIN_PASS\"}" \
  -o /tmp/auth_response.json 2>&1

if grep -q "token" /tmp/auth_response.json; then
    TOKEN=$(grep -o '"token":"[^"]*' /tmp/auth_response.json | cut -d'"' -f4)
    echo "✓ Authentication successful"
    echo ""
    
    # Upload kit via REST API
    echo "Uploading kit..."
    curl -s -X POST \
      "$VALIDATION_URL/wp-json/elementor/v1/import-kit" \
      -H "Authorization: Bearer $TOKEN" \
      -F "file=@$KIT_FILE" \
      | jq . || echo "Upload response: (check above)"
else
    echo "⚠ JWT authentication failed, trying alternative..."
    
    # Try without JWT auth (some installations don't require it)
    curl -s -X POST \
      "$VALIDATION_URL/wp-json/elementor/v1/import-kit" \
      -F "file=@$KIT_FILE" \
      -u "$ADMIN_USER:$ADMIN_PASS" \
      | jq . || echo "Upload response: (check above)"
fi

echo ""
echo "================================"
echo "IMPORT VIA REST COMPLETE"
echo "================================"
