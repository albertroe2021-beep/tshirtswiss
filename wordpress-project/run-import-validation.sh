#!/bin/bash
# Elementor Kit Import and Validation Script

COMPOSE_VALIDATION="/workspaces/tshirtswiss/wordpress-project/docker-compose.validation.yml"
KIT_FILE="/workspaces/tshirtswiss/wordpress-project/exports/tshirtswiss-kit.zip"

echo ""
echo "============================================"
echo "ELEMENTOR KIT IMPORT AND VALIDATION"
echo "============================================"
echo ""

# Function to run commands in validation WordPress
run_validation() {
    docker compose -f "$COMPOSE_VALIDATION" run --rm wpcli "$@"
}

# Step 1: Verify validation site is ready
echo "[1/6] Verifying validation site..."
site_url=$(run_validation wp option get siteurl --allow-root 2>/dev/null | tail -1)
echo "Validation site: $site_url"
echo ""

# Step 2: Check if kit file exists
echo "[2/6] Checking kit file..."
if [ ! -f "$KIT_FILE" ]; then
    echo "ERROR: Kit file not found at $KIT_FILE"
    exit 1
fi
kit_size=$(ls -lh "$KIT_FILE" | awk '{print $5}')
echo "Kit file: $KIT_FILE (Size: $kit_size)"
echo ""

# Step 3: Verify Elementor is installed
echo "[3/6] Verifying Elementor on validation site..."
run_validation wp plugin is-active elementor --allow-root 2>/dev/null
if [ $? -eq 0 ]; then
    echo "✓ Elementor is active"
else
    echo "⚠ Activating Elementor..."
    run_validation wp plugin activate elementor --allow-root 2>/dev/null
    run_validation wp plugin activate hello-elementor --allow-root 2>/dev/null
fi
echo ""

# Step 4: Import the kit
echo "[4/6] Importing kit..."
echo "Command: wp elementor kit import /exports/tshirtswiss-kit.zip --allow-root"
echo ""

import_output=$(run_validation wp elementor kit import /exports/tshirtswiss-kit.zip --allow-root 2>&1)
echo "$import_output"
echo ""

# Step 5: Verify pages were imported
echo "[5/6] Listing imported pages..."
echo ""
run_validation wp post list --post_type=page --post_status=any --fields=ID,post_title,post_name --format=table --allow-root
echo ""

# Step 6: Check for element errors in post meta
echo "[6/6] Checking for element type errors..."
echo ""

# Create a temporary PHP script to analyze elementor data
cat > /tmp/check-elements.php << 'PHPEOF'
<?php
if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

echo "Scanning for unregistered Elementor element types...\n";
echo str_repeat("-", 60) . "\n";

$pages = get_posts([
    'post_type'      => 'page',
    'numberposts'    => -1,
    'fields'         => 'ids',
]);

$unregistered_types = [];
$total_checked = 0;

foreach ($pages as $page_id) {
    $elementor_data = get_post_meta($page_id, '_elementor_data', true);
    
    if (!$elementor_data) {
        continue;
    }
    
    if (is_string($elementor_data)) {
        $elementor_data = json_decode($elementor_data, true);
    }
    
    if (!is_array($elementor_data)) {
        continue;
    }
    
    $total_checked++;
    
    // Recursively scan for element types
    $function = function($elements) use (&$unregistered_types, &$function) {
        if (!is_array($elements)) {
            return;
        }
        
        foreach ($elements as $element) {
            if (!is_array($element)) {
                continue;
            }
            
            $el_type = $element['elType'] ?? null;
            $widget_type = $element['widgetType'] ?? null;
            
            if ($el_type === 'widget' && $widget_type) {
                // Check if widget is registered
                $widget = \Elementor\Plugin::instance()->widgets_manager->get_widget_types($widget_type);
                if (!$widget) {
                    $unregistered_types[$widget_type] = ($unregistered_types[$widget_type] ?? 0) + 1;
                }
            }
            
            // Recurse into children
            if (isset($element['elements']) && is_array($element['elements'])) {
                $function($element['elements']);
            }
        }
    };
    
    $function($elementor_data);
}

if (empty($unregistered_types)) {
    echo "✓ No unregistered widget types found\n";
    echo "✓ Checked $total_checked pages with Elementor data\n";
} else {
    echo "✗ Found unregistered widget types:\n";
    foreach ($unregistered_types as $type => $count) {
        echo "  - $type (appears $count time(s))\n";
    }
}

echo "\nTotal pages in database: " . count($pages) . "\n";
echo "Pages with Elementor data: $total_checked\n";
PHPEOF

# Run the PHP script
run_validation wp eval-file /scripts/check-elements.php --allow-root 2>&1

echo ""
echo "============================================"
echo "IMPORT VALIDATION COMPLETE"
echo "============================================"
echo ""
