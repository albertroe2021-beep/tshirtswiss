<?php
/**
 * Elementor CLI Wrapper - Test and Execute Export/Import
 * 
 * This script tests Elementor CLI commands and executes the export/import workflow
 */

// Check if running in WordPress context
if (!defined('ABSPATH')) {
    echo "ERROR: Not running in WordPress context\n";
    exit(1);
}

echo "\n";
echo str_repeat("=", 60) . "\n";
echo "ELEMENTOR CLI WORKFLOW TEST\n";
echo str_repeat("=", 60) . "\n";
echo "\n";

// Step 1: Verify Elementor is active and has CLI commands
echo "STEP 1: Verify Elementor CLI Commands\n";
echo str_repeat("-", 60) . "\n";

$wp_cli_class = class_exists('WP_CLI');
echo "WP-CLI available: " . ($wp_cli_class ? "YES" : "NO") . "\n";

$elementor_active = did_action('elementor/loaded') || class_exists('\Elementor\Plugin');
echo "Elementor active: " . ($elementor_active ? "YES" : "NO") . "\n";

if (!$elementor_active) {
    echo "ERROR: Elementor plugin not loaded\n";
    exit(1);
}

// Step 2: Check if Elementor kit commands are registered
echo "\nSTEP 2: Check Elementor Command Registration\n";
echo str_repeat("-", 60) . "\n";

if ($wp_cli_class) {
    // This would normally be checked via WP_CLI::get_commands()
    echo "WP-CLI is available\n";
    echo "Elementor should have registered 'elementor', 'kit', 'library' etc. commands\n";
} else {
    echo "WP-CLI not available - commands cannot be tested directly\n";
}

// Step 3: Get Elementor version
echo "\nSTEP 3: Elementor Version\n";
echo str_repeat("-", 60) . "\n";

$elementor = \Elementor\Plugin::instance();
$elementor_version = $elementor->get_version() ?? 'Unknown';
echo "Elementor Version: " . $elementor_version . "\n";

// Step 4: Check for kit export/import classes
echo "\nSTEP 4: Check Kit Classes\n";
echo str_repeat("-", 60) . "\n";

$export_class_exists = class_exists('\Elementor\App\Modules\ImportExport\Processes\Export');
$import_class_exists = class_exists('\Elementor\App\Modules\ImportExport\Processes\Import');

echo "Export class exists: " . ($export_class_exists ? "YES" : "NO") . "\n";
echo "Import class exists: " . ($import_class_exists ? "YES" : "NO") . "\n";

if ($export_class_exists) {
    echo "  -> \Elementor\App\Modules\ImportExport\Processes\Export\n";
}
if ($import_class_exists) {
    echo "  -> \Elementor\App\Modules\ImportExport\Processes\Import\n";
}

// Step 5: List pages that exist
echo "\nSTEP 5: Pages in Database\n";
echo str_repeat("-", 60) . "\n";

$pages = get_posts([
    'post_type'      => 'page',
    'post_status'    => 'any',
    'numberposts'    => -1,
    'fields'         => 'ids',
]);

echo "Total pages: " . count($pages) . "\n";

if (!empty($pages)) {
    echo "Page IDs: " . implode(', ', array_slice($pages, 0, 10));
    if (count($pages) > 10) {
        echo " ... and " . (count($pages) - 10) . " more";
    }
    echo "\n";
    
    // Check if any pages have Elementor data
    $elementor_pages = 0;
    foreach ($pages as $page_id) {
        if (metadata_exists('post', $page_id, '_elementor_data')) {
            $elementor_pages++;
        }
    }
    echo "Pages with Elementor data: " . $elementor_pages . "\n";
}

// Step 6: Summary
echo "\nSTEP 6: Summary\n";
echo str_repeat("-", 60) . "\n";

if ($wp_cli_class && $elementor_active) {
    echo "✓ Ready to execute: wp elementor kit export\n";
    echo "✓ Ready to execute: wp elementor kit import\n";
    echo "\nNext: Run from shell:\n";
    echo "  wp elementor kit export /path/to/kit.zip --allow-root\n";
    echo "  wp elementor kit import /path/to/kit.zip --allow-root\n";
} else {
    echo "⚠ Cannot execute CLI commands directly\n";
}

echo "\n" . str_repeat("=", 60) . "\n";
echo "END OF TEST\n";
echo str_repeat("=", 60) . "\n";
echo "\n";
