#!/bin/bash
# Test page rendering on validation WordPress

VALIDATION_URL="http://tshirtswiss-validation-wordpress"

echo ""
echo "========================================================================"
echo "PAGE RENDERING VALIDATION TEST"
echo "========================================================================"
echo ""

echo "[1/5] Testing home page..."
home_response=$(curl -s -w "\n%{http_code}" "$VALIDATION_URL/")
home_status=$(echo "$home_response" | tail -1)
home_content=$(echo "$home_response" | head -n -1)

echo "Status: $home_status"
if echo "$home_content" | grep -q "elementor"; then
    echo "✓ Contains Elementor content"
else
    echo "⚠ No Elementor markup found"
fi
echo "Content length: $(echo "$home_content" | wc -c) bytes"
echo ""

echo "[2/5] Testing products page..."
products_response=$(curl -s -w "\n%{http_code}" "$VALIDATION_URL/products/")
products_status=$(echo "$products_response" | tail -1)
products_content=$(echo "$products_response" | head -n -1)

echo "Status: $products_status"
if echo "$products_content" | grep -q -i "product\|heading\|text"; then
    echo "✓ Contains content"
else
    echo "⚠ Minimal content"
fi
echo "Content length: $(echo "$products_content" | wc -c) bytes"
echo ""

echo "[3/5] Testing services page..."
services_response=$(curl -s -w "\n%{http_code}" "$VALIDATION_URL/services/")
services_status=$(echo "$services_response" | tail -1)
services_content=$(echo "$services_response" | head -n -1)

echo "Status: $services_status"
echo "Content length: $(echo "$services_content" | wc -c) bytes"
echo ""

echo "[4/5] Checking for errors..."
error_count=0

for page in "" "products/" "services/" "about/"; do
    response=$(curl -s "$VALIDATION_URL/$page" 2>&1)
    
    if echo "$response" | grep -q -i "fatal error\|exception\|undefined\|notice"; then
        echo "⚠ Error in /$page"
        error_count=$((error_count + 1))
    fi
    
    if echo "$response" | grep -q "Elements_Manager::get_element"; then
        echo "✗ Elements_Manager error in /$page"
        error_count=$((error_count + 1))
    fi
done

if [ $error_count -eq 0 ]; then
    echo "✓ No fatal errors detected"
else
    echo "Found $error_count errors"
fi
echo ""

echo "[5/5] Summary..."
echo "Home page: $home_status"
echo "Products page: $products_status"
echo "Services page: $services_status"
echo ""

if [ "$home_status" = "200" ] && [ "$products_status" = "200" ] && [ "$services_status" = "200" ]; then
    echo "✓ SUCCESS: All pages rendering"
else
    echo "⚠ Some pages returned non-200 status"
fi

echo ""
echo "========================================================================"
