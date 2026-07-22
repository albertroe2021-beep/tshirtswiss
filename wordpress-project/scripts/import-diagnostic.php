<?php
/**
 * Diagnostic Report: Why Import Created Empty Pages
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

echo "\n" . str_repeat("=", 80) . "\n";
echo "IMPORT DIAGNOSTIC REPORT\n";
echo str_repeat("=", 80) . "\n\n";

// Set admin context
if (!is_user_logged_in()) {
    wp_set_current_user(1);
}

echo "[1] Check WordPress Environment\n";
echo "WordPress: " . get_bloginfo('version') . "\n";
echo "PHP: " . PHP_VERSION . "\n";

echo "\n[2] Check Elementor Status\n";
$elementor_version = get_option('elementor_version');
echo "Elementor version: " . $elementor_version . "\n";
echo "Elementor Pro: " . (defined('ELEMENTOR_PRO_VERSION') ? ELEMENTOR_PRO_VERSION : 'Not installed') . "\n";

echo "\n[3] Check Theme\n";
$theme = wp_get_theme();
echo "Theme: " . $theme->get('Name') . "\n";
echo "Theme support: " . (current_theme_supports('elementor') ? 'YES' : 'NO') . "\n";

echo "\n[4] Check Import Sessions/Logs\n";
$sessions = get_option('elementor_import_sessions');
if ($sessions && is_array($sessions)) {
    echo "Import sessions: " . count($sessions) . "\n";
    foreach ($sessions as $session_id => $session_data) {
        echo "  Session: $session_id\n";
        if (is_array($session_data)) {
            echo "    Status: " . ($session_data['status'] ?? 'unknown') . "\n";
            echo "    Data: " . (isset($session_data['data']) ? 'present' : 'missing') . "\n";
        }
    }
}

echo "\n[5] Check Sample Pages\n";
$pages = get_posts([
    'post_type' => 'page',
    'posts_per_page' => 3,
    'post_status' => 'publish',
    'orderby' => 'ID',
]);

foreach ($pages as $page) {
    echo "\nPage: " . $page->post_title . " (ID: " . $page->ID . ")\n";
    
    $elementor_data = get_post_meta($page->ID, '_elementor_data', true);
    echo "  _elementor_data type: " . gettype($elementor_data) . "\n";
    
    if (is_string($elementor_data)) {
        $data = json_decode($elementor_data, true);
        echo "  JSON length: " . strlen($elementor_data) . " bytes\n";
        echo "  Parsed as: " . gettype($data) . "\n";
        if (is_array($data)) {
            echo "  Element count: " . count($data) . "\n";
        }
    } elseif (is_array($elementor_data)) {
        echo "  Array length: " . count($elementor_data) . "\n";
    } else {
        echo "  Value: " . var_export($elementor_data, true) . "\n";
    }
    
    // Check other relevant metadata
    $edit_mode = get_post_meta($page->ID, '_elementor_edit_mode', true);
    echo "  _elementor_edit_mode: " . ($edit_mode ?: 'not set') . "\n";
    
    $version = get_post_meta($page->ID, '_elementor_version', true);
    echo "  _elementor_version: " . ($version ?: 'not set') . "\n";
}

echo "\n[6] Check Import Class Availability\n";
if (class_exists('\Elementor\App\Modules\ImportExport\Processes\Import')) {
    echo "✓ Import class available\n";
    
    // Try to check the last import
    $kit_path = '/exports/tshirtswiss-kit.zip';
    if (file_exists($kit_path)) {
        echo "\n[7] Try Manual Import Again\n";
        echo "Running import of $kit_path...\n";
        
        try {
            $import = new \Elementor\App\Modules\ImportExport\Processes\Import(
                $kit_path,
                ['include' => ['content']]
            );
            
            $import->register_default_runners();
            
            // Before running, check if we can inspect the manifest
            $manifest = $import->get_manifest();
            echo "Manifest pages: " . count($manifest['pages'] ?? []) . "\n";
            
            echo "Running...\n";
            $result = $import->run();
            
            echo "Result: " . json_encode($result, JSON_UNESCAPED_SLASHES) . "\n";
            
        } catch (\Throwable $e) {
            echo "Error: " . $e->getMessage() . "\n";
        }
    }
} else {
    echo "✗ Import class NOT available\n";
}

echo "\n" . str_repeat("=", 80) . "\n";
