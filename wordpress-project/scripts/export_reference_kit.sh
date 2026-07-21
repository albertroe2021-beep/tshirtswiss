#!/usr/bin/env bash
set -euo pipefail

wp() {
  command wp --allow-root "$@"
}

cd /var/www/html
mkdir -p /exports

TS=$(date -u +"%Y%m%d-%H%M%S")
KIT_BASE="tshirtswiss-reference-kit-${TS}"
TMP_DIR="/tmp/${KIT_BASE}"
mkdir -p "$TMP_DIR"
OUT_DIR="/exports/tshirtswiss-reference-kit"
rm -rf "$OUT_DIR"
mkdir -p "$OUT_DIR"

# Export WordPress content XML as a fallback artifact.
wp export --dir="$TMP_DIR" --filename_format="wordpress-export.xml" >/dev/null

# Export Elementor templates in native JSON format via WP-CLI if available.
if wp help elementor >/dev/null 2>&1; then
  wp post list --post_type=elementor_library --field=ID | while read -r template_id; do
    if [[ -n "$template_id" ]]; then
      wp post meta get "$template_id" _elementor_data > "$TMP_DIR/template-${template_id}.json" || true
    fi
  done
fi

cat > "$TMP_DIR/EXPORT_NOTES.txt" <<'EOF'
This package was produced automatically in a headless environment.
It contains generated WordPress export artifacts and Elementor template payloads.
For a native Elementor Export Kit zip, open WP Admin and export through Elementor -> Tools -> Import Export Kit.
EOF

cp -a "$TMP_DIR"/. "$OUT_DIR"/

echo "Created staging export at /exports/tshirtswiss-reference-kit"
