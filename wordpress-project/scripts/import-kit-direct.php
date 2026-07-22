<?php
/**
 * Direct Elementor Kit Import
 * 
 * This script imports a kit using Elementor's Import class directly
 * with proper WordPress authentication context.
 *
 * Usage: wp eval-file /scripts/import-kit-direct.php
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

// Ensure user is admin
if (!current_user_can('manage_options')) {
    // Try to set user context as admin (id=1)
    wp_set_current_user(1);
}

echo "\n";
echo str_repeat("=", 70) . "\n";
echo "DIRECT ELEMENTOR KIT IMPORT\n";
echo str_repeat("=", 70) . "\n";
echo "\n";

$kit_path = '/exports/tshirtswiss-kit.zip';

if (!file_exists($kit_path)) {
    echo "ERROR: Kit file not found: $kit_path\n";
    exit(1);
}

echo "[1/4] Verifying kit file...\n";
echo "File: $kit_path\n";
echo "Size: " . (filesize($kit_path) / 1024) . " KB\n";
echo "Valid ZIP: " . (is_file($kit_path) && function_exists('zip_open') ? "YES" : "MAYBE") . "\n";
echo "\n";

// Check if Elementor is loaded
echo "[2/4] Checking Elementor...\n";
if (!did_action('elementor/loaded')) {
    echo "Loading Elementor plugin...\n";
    do_action('elementor/loaded');
}

$elementor = \Elementor\Plugin::instance();
echo "✓ Elementor " . $elementor->get_version() . " loaded\n";
echo "\n";

// Check for Import class
echo "[3/4] Preparing import...\n";

$import_class = 'Elementor\App\Modules\ImportExport\Processes\Import';

if (!class_exists($import_class)) {
    echo "ERROR: Import class not found: $import_class\n";
    exit(1);
}

echo "✓ Import class found\n";

// Determine correct constructor signature by trying to instantiate
try {
    // Try the most likely signature based on Elementor source
    $reflection = new ReflectionClass($import_class);
    $constructor = $reflection->getConstructor();
    
    if ($constructor) {
        $params = $constructor->getParameters();
        echo "Constructor parameters: " . count($params) . "\n";
        foreach ($params as $param) {
            $type = $param->getType() ? (string)$param->getType() : 'mixed';
            echo "  - " . $param->getName() . " ($type)\n";
        }
    }
} catch (Exception $e) {
    echo "Could not reflect constructor: " . $e->getMessage() . "\n";
}

echo "\n[4/4] Executing import...\n";

try {
    // Try to instantiate with just file path (most common pattern)
    $import = new $import_class($kit_path);
    
    // Register runners
    if (method_exists($import, 'register_default_runners')) {
        $import->register_default_runners();
        echo "✓ Runners registered\n";
    }
    
    // Run the import
    echo "Running import process...\n";
    $result = $import->run();
    
    if ($result === true || (is_array($result) && !empty($result['status']))) {
        echo "✓ Import completed\n";
        if (is_array($result)) {
            echo "Status: " . $result['status'] . "\n";
            if (isset($result['data'])) {
                echo "Data: " . json_encode($result['data'], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES) . "\n";
            }
        }
    } else {
        echo "⚠ Import returned unexpected result: " . var_export($result, true) . "\n";
    }
    
} catch (\TypeError $e) {
    echo "Type error (trying alternative constructor): " . $e->getMessage() . "\n";
    
    // Try with array-based constructor
    try {
        $import = new $import_class([
            'file_path' => $kit_path,
            'source' => $kit_path,
        ]);
        echo "✓ Alternative constructor worked\n";
        
        if (method_exists($import, 'register_default_runners')) {
            $import->register_default_runners();
        }
        
        $result = $import->run();
        echo "✓ Import completed\n";
        
    } catch (\Throwable $e2) {
        echo "ERROR: Both constructor attempts failed\n";
        echo "Error 1: " . $e->getMessage() . "\n";
        echo "Error 2: " . $e2->getMessage() . "\n";
        exit(1);
    }
    
} catch (\Throwable $e) {
    echo "ERROR: " . $e->getMessage() . "\n";
    echo "File: " . $e->getFile() . "\n";
    echo "Line: " . $e->getLine() . "\n";
    exit(1);
}

echo "\n";
echo str_repeat("=", 70) . "\n";
echo "IMPORT COMPLETE\n";
echo str_repeat("=", 70) . "\n";
echo "\n";
