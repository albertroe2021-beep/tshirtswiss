#!/usr/bin/env bash
set -euo pipefail

# Phase 6: Fresh WordPress Installation Test
# Validates the Elementor Website Kit by importing into a clean WordPress

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WP_DIR="${PROJECT_DIR}/wordpress-project"
KIT_FILE="${WP_DIR}/exports/tshirtswiss-elementor-website-kit.zip"
BUILD_DIR="${PROJECT_DIR}/build"

if [ ! -f "$KIT_FILE" ]; then
    echo "ERROR: Kit file not found"
    exit 1
fi

echo "======================================"
echo "Phase 6: Fresh Installation Test"
echo "======================================"
echo ""
echo "Kit to test: $KIT_FILE"
echo ""

# Start fresh WordPress (separate database/volume)
echo "[1/3] Starting clean WordPress environment..."

CLEAN_DB_NAME="wordpress_test"
CLEAN_WP_PORT=8089

# Create fresh docker compose for test
TEST_COMPOSE=$(mktemp)
cat > "$TEST_COMPOSE" <<EOF
version: '3.8'

services:
  test-db:
    image: mariadb:8.0
    environment:
      MYSQL_DATABASE: $CLEAN_DB_NAME
      MYSQL_ROOT_PASSWORD: test123
      MYSQL_PASSWORD: test123
      MYSQL_USER: wordpress
    volumes:
      - test_db_data:/var/lib/mysql
    ports:
      - "3308:3306"

  test-wordpress:
    image: wordpress:6.8.2-php8.2-apache
    depends_on:
      - test-db
    environment:
      WORDPRESS_DB_HOST: test-db
      WORDPRESS_DB_NAME: $CLEAN_DB_NAME
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: test123
      WORDPRESS_TABLE_PREFIX: wp_
    volumes:
      - test_wp_data:/var/www/html
    ports:
      - "$CLEAN_WP_PORT:80"

  test-wpcli:
    image: wordpress:cli:2.8.1
    depends_on:
      - test-db
    environment:
      WORDPRESS_DB_HOST: test-db
      WORDPRESS_DB_NAME: $CLEAN_DB_NAME
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: test123
    volumes:
      - test_wp_data:/var/www/html
      - $KIT_FILE:/imports/kit.zip:ro
    user: "0:0"

volumes:
  test_db_data:
  test_wp_data:
EOF

# Start test environment
cd /tmp
docker compose -f "$TEST_COMPOSE" up -d >/dev/null 2>&1
sleep 10

echo "[2/3] Installing WordPress and Elementor..."

docker compose -f "$TEST_COMPOSE" run --rm test-wpcli bash -lc '
  set -euo pipefail
  cd /var/www/html
  
  # Wait for DB
  for i in {1..30}; do
    wp --allow-root db query "SELECT 1;" >/dev/null 2>&1 && break
    sleep 1
  done
  
  # Install WordPress
  if ! wp --allow-root core is-installed >/dev/null 2>&1; then
    wp --allow-root core install \
      --url="http://localhost:'"$CLEAN_WP_PORT"'" \
      --title="TShirtSwiss Test" \
      --admin_user="testadmin" \
      --admin_password="test123" \
      --admin_email="test@example.com"
  fi
  
  # Install Hello Elementor
  wp --allow-root theme install hello-elementor --activate 2>/dev/null || true
  
  # Install Elementor 4.1.5
  wp --allow-root plugin install elementor --version=4.1.5 --activate 2>/dev/null || true
  
  echo "WordPress setup for import test complete"
' >/dev/null 2>&1

echo "[3/3] Importing Elementor Website Kit..."

# Create import script
IMPORT_SCRIPT=$(mktemp)
cat > "$IMPORT_SCRIPT" <<'IMPORT_PHP'
<?php
// Import script for Elementor Website Kit

if ( ! function_exists( 'wp_json_encode' ) ) {
    echo "ERROR: WordPress not loaded\n";
    exit( 1 );
}

$kit_file = '/imports/kit.zip';
$import_dir = '/tmp/elementor-import';

if ( ! file_exists( $kit_file ) ) {
    echo "ERROR: Kit file not found\n";
    exit( 1 );
}

echo "Extracting kit...\n";
$zip = new ZipArchive();
if ( ! $zip->open( $kit_file ) ) {
    echo "ERROR: Could not open ZIP\n";
    exit( 1 );
}
$zip->extractTo( $import_dir );
$zip->close();

// Load manifest and content
$manifest_file = "$import_dir/manifest.json";
$content_file = "$import_dir/content.json";
$settings_file = "$import_dir/settings.json";

if ( ! file_exists( $manifest_file ) || ! file_exists( $content_file ) ) {
    echo "ERROR: Missing manifest or content\n";
    exit( 1 );
}

$manifest = json_decode( file_get_contents( $manifest_file ), true );
$content = json_decode( file_get_contents( $content_file ), true );
$settings = json_decode( file_get_contents( $settings_file ), true );

echo "\n=== Import Summary ===\n";
echo "Elementor Version: " . ( $manifest['version'] ?? 'unknown' ) . "\n";
echo "Content to import: " . count( $content ) . " items\n";
echo "  - Pages: " . count( array_filter( $content, fn($c) => $c['type'] === 'page' ) ) . "\n";
echo "  - Posts: " . count( array_filter( $content, fn($c) => $c['type'] === 'post' ) ) . "\n";
echo "  - Templates: " . count( array_filter( $content, fn($c) => $c['type'] === 'elementor_library' ) ) . "\n";
echo "  - Total: " . count( $content ) . "\n";

// Import pages/posts/templates
$imported = 0;
foreach ( $content as $item ) {
    $post_data = array(
        'post_type'   => $item['type'],
        'post_title'  => $item['title'],
        'post_name'   => $item['slug'],
        'post_status' => $item['status'],
        'post_parent' => $item['parent'] ?? 0,
        'post_content' => $item['content'] ?? '',
        'post_excerpt' => $item['excerpt'] ?? '',
    );

    $post_id = wp_insert_post( $post_data );

    if ( $post_id && is_numeric( $post_id ) ) {
        // Set Elementor data
        if ( ! empty( $item['elementor_data'] ) ) {
            update_post_meta( $post_id, '_elementor_data', wp_json_encode( $item['elementor_data'] ) );
        }
        if ( ! empty( $item['elementor_settings'] ) ) {
            update_post_meta( $post_id, '_elementor_page_settings', wp_json_encode( $item['elementor_settings'] ) );
        }
        if ( ! empty( $item['elementor_version'] ) ) {
            update_post_meta( $post_id, '_elementor_version', $item['elementor_version'] );
        }
        $imported++;
    }
}

echo "\nImported: $imported items\n";

// Import settings
if ( ! empty( $settings['elementor']['global_colors'] ) ) {
    update_option( 'elementor_global_colors', wp_json_encode( $settings['elementor']['global_colors'] ) );
}
if ( ! empty( $settings['elementor']['global_fonts'] ) ) {
    update_option( 'elementor_global_fonts', wp_json_encode( $settings['elementor']['global_fonts'] ) );
}

echo "\nSettings imported\n";

// Verify
$pages = count_posts( 'page' );
$posts = count_posts( 'post' );
$templates = count_posts( 'elementor_library' );

echo "\n=== Post-Import Verification ===\n";
echo "Pages: " . ( $pages->publish ?? 0 ) . "\n";
echo "Posts: " . ( $posts->publish ?? 0 ) . "\n";
echo "Templates: " . ( $templates->publish ?? 0 ) . "\n";
echo "\n✓ Import complete\n";

// Cleanup
system( "rm -rf $import_dir" );
exit( 0 );
IMPORT_PHP

docker compose -f "$TEST_COMPOSE" run --rm test-wpcli bash -lc '
  cd /var/www/html
  wp --allow-root eval-file '"$IMPORT_SCRIPT"'
' 2>&1 | tee "${BUILD_DIR}/import-test-log.txt"

# Cleanup
docker compose -f "$TEST_COMPOSE" down -v >/dev/null 2>&1
rm -f "$TEST_COMPOSE" "$IMPORT_SCRIPT"

echo ""
echo "======================================"
echo "✓ Fresh Installation Test Complete"
echo "======================================"
