<?php
/**
 * Elementor Official Import Kit Method
 * 
 * Uses the official Elementor module method: import_kit()
 * This is the same method called by the WP-CLI command
 * 
 * Usage: wp eval-file /scripts/official-import.php
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

// Ensure we're working with WordPress admin user context
if (!is_user_logged_in()) {
    // Get the admin user (ID 1 is typically admin)
    $admin_user = get_userdata(1);
    if ($admin_user) {
        wp_set_current_user($admin_user->ID);
    }
}

// Verify we have admin capability
if (!current_user_can('manage_options')) {
    echo "ERROR: Current user does not have manage_options capability\n";
    echo "Current user: " . (get_current_user_id() ? get_current_user_id() : 'NONE') . "\n";
    exit(1);
}

echo "\n";
echo str_repeat("=", 80) . "\n";
echo "ELEMENTOR OFFICIAL KIT IMPORT\n";
echo str_repeat("=", 80) . "\n";
echo "\n";

$kit_path = '/exports/tshirtswiss-kit.zip';

// Verify file exists
if (!file_exists($kit_path)) {
    echo "ERROR: Kit file not found: $kit_path\n";
    exit(1);
}

echo "[1/5] Verifying preconditions...\n";
echo "File: $kit_path\n";
echo "Size: " . (filesize($kit_path) / 1024) . " KB\n";
echo "Current User: " . wp_get_current_user()->user_login . "\n";
echo "Has Admin Cap: " . (current_user_can('manage_options') ? 'YES' : 'NO') . "\n";
echo "\n";

// Get the import-export module
echo "[2/5] Loading Elementor import-export module...\n";

try {
    // Get Elementor plugin instance
    $elementor = \Elementor\Plugin::instance();
    
    // Try multiple ways to access the module
    $import_export_module = null;
    
    // Method 1: Via app component (used by WP-CLI)
    if (isset($elementor->app) && method_exists($elementor->app, 'get_component')) {
        $import_export_module = $elementor->app->get_component('import-export');
    }
    
    // Method 2: Via modules manager
    if (!$import_export_module && isset($elementor->modules_manager)) {
        $import_export_module = $elementor->modules_manager->get_modules('import-export');
    }
    
    // Method 3: Direct instantiation as last resort
    if (!$import_export_module) {
        echo "Note: Trying direct module instantiation...\n";
        $import_export_module = new \Elementor\App\Modules\ImportExport\Module();
    }
    
    if (!$import_export_module) {
        echo "ERROR: Import-export module not available through any method\n";
        exit(1);
    }
    
    echo "✓ Module loaded: " . get_class($import_export_module) . "\n";
    echo "\n";
    
} catch (\Throwable $e) {
    echo "ERROR: Could not load import-export module\n";
    echo "Exception: " . $e->getMessage() . "\n";
    exit(1);
}

// Prepare import settings (same as CLI)
echo "[3/5] Preparing import settings...\n";

$import_settings = [
    'include'    => ['content', 'site-settings'],  // Import content and site settings
    'sourceType' => 'local',                        // Source is local file
    'referrer'   => 'local',                        // Referrer is local
];

echo "Settings: " . json_encode($import_settings) . "\n";
echo "\n";

// Execute the import using official method
echo "[4/5] Executing official import_kit() method...\n";

try {
    // This is the exact method called by the WP-CLI command
    $result = $import_export_module->import_kit(
        $kit_path,
        $import_settings,
        false  // split_to_chunks
    );
    
    echo "✓ Import completed\n";
    echo "Result: " . json_encode($result, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES) . "\n";
    echo "\n";
    
    // Get manifest data
    if (isset($import_export_module->import)) {
        echo "[5/5] Import summary:\n";
        
        $manifest = $import_export_module->import->get_manifest();
        if ($manifest) {
            echo "Manifest Version: " . ($manifest['version'] ?? 'UNKNOWN') . "\n";
            echo "Elementor Version: " . ($manifest['elementor_version'] ?? 'UNKNOWN') . "\n";
            
            if (isset($manifest['content']['page'])) {
                echo "Pages imported: " . count($manifest['content']['page']) . "\n";
            }
        }
    }
    
    echo "\n" . str_repeat("=", 80) . "\n";
    echo "SUCCESS: Kit imported using official Elementor method\n";
    echo str_repeat("=", 80) . "\n";
    echo "\n";
    
} catch (\Throwable $e) {
    echo "ERROR: Import failed\n";
    echo "Exception: " . $e->getMessage() . "\n";
    echo "File: " . $e->getFile() . "\n";
    echo "Line: " . $e->getLine() . "\n";
    echo "\nStack trace:\n";
    echo $e->getTraceAsString() . "\n";
    exit(1);
}
