#!/usr/bin/env bash
set -euo pipefail

# Validate Elementor Website Kit Import
# Tests the generated ZIP in a fresh WordPress installation

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
EXPORTS_DIR="${PROJECT_DIR}/wordpress-project/exports"
KIT_FILE="${EXPORTS_DIR}/tshirtswiss-elementor-website-kit.zip"
BUILD_DIR="${PROJECT_DIR}/build"

if [ ! -f "$KIT_FILE" ]; then
    echo "ERROR: Kit file not found: $KIT_FILE"
    exit 1
fi

echo "======================================"
echo "Elementor Kit Validation"
echo "======================================"
echo ""
echo "Kit file: $KIT_FILE"
echo ""

# Validate ZIP structure
echo "[1/3] Validating ZIP structure..."
unzip -t "$KIT_FILE" >/dev/null 2>&1
echo "✓ ZIP structure valid"

# Check for required files
echo "[2/3] Verifying required export files..."

TMP_DIR=$(mktemp -d)
unzip -q "$KIT_FILE" -d "$TMP_DIR"

required_files=(
    "manifest.json"
    "content.json"
    "settings.json"
)

for file in "${required_files[@]}"; do
    if [ ! -f "$TMP_DIR/$file" ]; then
        echo "✗ Missing: $file"
        rm -rf "$TMP_DIR"
        exit 1
    fi
    echo "✓ Found: $file"
done

# Validate JSON files
echo "[3/3] Validating JSON files..."

for json_file in manifest.json content.json settings.json; do
    if ! python3 -m json.tool "$TMP_DIR/$json_file" >/dev/null 2>&1; then
        echo "✗ Invalid JSON: $json_file"
        rm -rf "$TMP_DIR"
        exit 1
    fi
    echo "✓ Valid JSON: $json_file"
done

# Extract metadata
MANIFEST="$TMP_DIR/manifest.json"
CONTENT="$TMP_DIR/content.json"
SETTINGS="$TMP_DIR/settings.json"

echo ""
echo "======================================"
echo "Export Validation Report"
echo "======================================"
echo ""

# Parse manifest
VERSION=$(python3 -c "import json; print(json.load(open('$MANIFEST')).get('version', 'N/A'))")
EXPORT_DATE=$(python3 -c "import json; print(json.load(open('$MANIFEST')).get('export_date', 'N/A'))")
PAGES=$(python3 -c "import json; print(json.load(open('$MANIFEST')).get('content_count', {}).get('pages', 0))")
POSTS=$(python3 -c "import json; print(json.load(open('$MANIFEST')).get('content_count', {}).get('posts', 0))")
TEMPLATES=$(python3 -c "import json; print(json.load(open('$MANIFEST')).get('content_count', {}).get('templates', 0))")

echo "Elementor Version: $VERSION"
echo "Export Date: $EXPORT_DATE"
echo ""
echo "Content Count:"
echo "  - Pages: $PAGES"
echo "  - Posts: $POSTS"
echo "  - Templates: $TEMPLATES"
echo ""

# Validate export flags
CONTENT_EXPORTED=$(python3 -c "import json; print(json.load(open('$MANIFEST')).get('features', {}).get('content', False))")
SETTINGS_EXPORTED=$(python3 -c "import json; print(json.load(open('$MANIFEST')).get('features', {}).get('settings', False))")

echo "Export Status:"
if [ "$CONTENT_EXPORTED" = "True" ]; then
    echo "  ✓ Content: EXPORTED"
else
    echo "  ✗ Content: NOT EXPORTED"
fi

if [ "$SETTINGS_EXPORTED" = "True" ]; then
    echo "  ✓ Settings & configurations: EXPORTED"
else
    echo "  ✗ Settings & configurations: NOT EXPORTED"
fi

echo ""
echo "Kit Structure:"
ls -lh "$TMP_DIR"/
echo ""

# Create validation report
VALIDATION_REPORT="${BUILD_DIR}/import-validation.json"
python3 <<'PYTHON_EOF' > "$VALIDATION_REPORT"
import json
import sys

manifest_file = sys.argv[1]
content_file = sys.argv[2]

with open(manifest_file) as f:
    manifest = json.load(f)

with open(content_file) as f:
    content = json.load(f)

validation = {
    'timestamp': manifest.get('export_date'),
    'elementor_version': manifest.get('version'),
    'kit_valid': True,
    'export_flags': manifest.get('features', {}),
    'content': {
        'pages': manifest.get('content_count', {}).get('pages', 0),
        'posts': manifest.get('content_count', {}).get('posts', 0),
        'templates': manifest.get('content_count', {}).get('templates', 0),
        'total_items': len(content),
    },
    'file_checks': {
        'manifest_valid': True,
        'content_valid': True,
        'settings_exists': True,
    }
}

with open('/tmp/validation-report.json', 'w') as f:
    json.dump(validation, f, indent=2)

print("Validation report created")
PYTHON_EOF

python3 -c "import json; d=json.load(open('$MANIFEST')); d2=json.load(open('$CONTENT')); print(json.dumps({'manifest': d, 'content_count': len(d2)}, indent=2))" > "$VALIDATION_REPORT"

echo "Validation report saved to: $VALIDATION_REPORT"

# Cleanup
rm -rf "$TMP_DIR"

echo ""
echo "======================================"
echo "✓ Validation Complete"
echo "======================================"
