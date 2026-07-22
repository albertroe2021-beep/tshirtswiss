<?php
/**
 * Elementor Official Kit Import - Using Import Class Directly
 * 
 * This script imports a kit by directly instantiating the Import class,
 * which is the same process the Module uses internally.
 * 
 * Usage: wp eval-file /scripts/direct-import.php
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

// Ensure admin user context
if (!is_user_logged_in()) {
    $admin_user = get_userdata(1);
    if ($admin_user) {
        wp_set_current_user($admin_user->ID);
    }
}

if (!current_user_can('manage_options')) {
    echo "ERROR: Current user does not have manage_options capability\n";
    exit(1);
}

echo "\n";
echo str_repeat("=", 80) . "\n";
echo "ELEMENTOR KIT IMPORT - DIRECT METHOD\n";
echo str_repeat("=", 80) . "\n";
echo "\n";

$kit_path = '/exports/tshirtswiss-kit.zip';

if (!file_exists($kit_path)) {
    echo "ERROR: Kit file not found: $kit_path\n";
    exit(1);
}

echo "[1/4] Verifying preconditions...\n";
echo "File: $kit_path\n";
echo "Size: " . (filesize($kit_path) / 1024) . " KB\n";
echo "User: " . wp_get_current_user()->user_login . "\n";
echo "Admin: " . (current_user_can('manage_options') ? 'YES' : 'NO') . "\n";
echo "\n";

echo "[2/4] Loading Elementor Import class...\n";

try {
    // Verify Elementor is loaded
    if (!class_exists('\Elementor\Plugin')) {
        echo "ERROR: Elementor plugin not loaded\n";
        exit(1);
    }
    
    // Verify Import class exists
    if (!class_exists('\Elementor\App\Modules\ImportExport\Processes\Import')) {
        echo "ERROR: Elementor Import class not found\n";
        exit(1);
    }
    
    echo "✓ Elementor loaded\n";
    echo "✓ Import class available\n";
    echo "\n";
    
} catch (\Throwable $e) {
    echo "ERROR: " . $e->getMessage() . "\n";
    exit(1);
}

echo "[3/4] Preparing import...\n";

$import_settings = [
    'include'   => ['content', 'site-settings'],
    'referrer'  => 'local',
];

echo "Settings: " . json_encode($import_settings) . "\n";
echo "\n";

echo "[4/4] Executing import...\n";

try {
    // Directly instantiate the Import class
    $import = new \Elementor\App\Modules\ImportExport\Processes\Import(
        $kit_path,
        $import_settings
    );
    
    // Register default runners (same as module does)
    $import->register_default_runners();
    
    echo "✓ Import object created and runners registered\n";
    echo "Running import process...\n\n";
    
    // Run the import (this is where the magic happens)
    $result = $import->run();
    
    echo "\n✓ Import completed\n";
    
    // Show results
    if (is_array($result)) {
        echo "Result status: " . ($result['status'] ?? 'UNKNOWN') . "\n";
        
        if (isset($result['data'])) {
            $data = $result['data'];
            echo "\nImported data:\n";
            if (isset($data['pages_ids'])) {
                echo "  Pages: " . count($data['pages_ids']) . "\n";
            }
            if (isset($data['templates_ids'])) {
                echo "  Templates: " . count($data['templates_ids']) . "\n";
            }
        }
    }
    
    // Get manifest info
    $manifest = $import->get_manifest();
    if ($manifest) {
        echo "\nManifest info:\n";
        echo "  Version: " . ($manifest['version'] ?? 'UNKNOWN') . "\n";
        echo "  Elementor: " . ($manifest['elementor_version'] ?? 'UNKNOWN') . "\n";
    }
    
    echo "\n" . str_repeat("=", 80) . "\n";
    echo "SUCCESS: Kit imported successfully!\n";
    echo str_repeat("=", 80) . "\n";
    echo "\n";
    
} catch (\Throwable $e) {
    echo "ERROR: Import failed\n";
    echo "Message: " . $e->getMessage() . "\n";
    echo "File: " . $e->getFile() . "\n";
    echo "Line: " . $e->getLine() . "\n";
    
    if ($e instanceof \Error) {
        echo "\nStack trace:\n";
        echo substr($e->getTraceAsString(), 0, 500) . "\n";
    }
    
    exit(1);
}
