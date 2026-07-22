<?php
/**
 * DEEP INSTRUMENTATION - Trace element data through import
 * 
 * Compares exported ZIP JSON vs. what Elementor tries to process
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

$log_dir = '/exports/deep-trace';
if (!is_dir($log_dir)) {
    mkdir($log_dir, 0777, true);
}

echo "Deep Instrumentation Trace\n";
echo str_repeat("=", 80) . "\n\n";

// ========================================================================
// STEP 1: Extract original page JSON from ZIP
// ========================================================================

echo "STEP 1: Extract page JSON from ZIP\n";
echo str_repeat("-", 80) . "\n";

$zip = new ZipArchive();
$zip->open('/exports/tshirtswiss-kit.zip');

$original_json = null;
$original_file = null;

// Find first page
for ($i = 0; $i < $zip->numFiles; $i++) {
    $stat = $zip->statIndex($i);
    if (strpos($stat['name'], 'content/page/36.json') === 0) {
        $original_json = json_decode($zip->getFromIndex($i), true);
        $original_file = $stat['name'];
        break;
    }
}

if (!$original_json) {
    echo "ERROR: No page found\n";
    exit(1);
}

// Save original JSON
file_put_contents("$log_dir/01-original-zip.json", json_encode($original_json, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));

echo "✓ Extracted: $original_file\n";
echo "✓ Content elements: " . count($original_json['content'] ?? []) . "\n";
echo "✓ Saved to: $log_dir/01-original-zip.json\n\n";

// ========================================================================
// STEP 2: Hook into Elementor to capture element data during import
// ========================================================================

echo "STEP 2: Install Elementor hooks\n";
echo str_repeat("-", 80) . "\n";

$elements_captured = [];
$element_error = null;

// Hook into create_element_instance to log what's being passed
add_action('elementor/core/before_create_element_instance', function($element_data) use ($log_dir) {
    $element_id = $element_data['id'] ?? 'NO_ID';
    $el_type = $element_data['elType'] ?? 'MISSING_ELTYPE';
    
    error_log("[HOOK] before_create_element: id=$element_id, elType=$el_type");
    
    // Save this element
    $filename = "$log_dir/02-element-" . str_pad(count(glob("$log_dir/02-element-*")), 3, '0', STR_PAD_LEFT) . ".json";
    file_put_contents($filename, json_encode($element_data, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));
}, 10, 1);

// Hook into on_import_update_dynamic_content before it processes
// We'll use a filter on the document to intercept
add_filter('elementor/document/before_save', function($document) use ($log_dir) {
    $post_id = $document->get_post_id();
    $post = get_post($post_id);
    
    if ($post && $post->post_type === 'page') {
        // Get the elements structure
        $elements = $document->get_elements_data();
        
        file_put_contents("$log_dir/03-document-elements-before-save.json", json_encode($elements, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));
        
        error_log("[HOOK] document/before_save: post_id=$post_id, title={$post->post_title}, elements=" . count($elements));
    }
    
    return $document;
}, 10, 1);

echo "✓ Hooks installed\n";
echo "✓ Will capture elements to: $log_dir/02-element-*.json\n";
echo "✓ Will capture document data to: $log_dir/03-*.json\n\n";

// ========================================================================
// STEP 3: Run import with wrapped error handler
// ========================================================================

echo "STEP 3: Running import...\n";
echo str_repeat("-", 80) . "\n";

// Wrap the problematic call to catch the error
set_error_handler(function($errno, $errstr, $errfile, $errline) use ($log_dir) {
    if (strpos($errfile, 'elements.php') !== false && strpos($errstr, 'Argument #1') !== false) {
        error_log("[ERROR_HANDLER] Caught error: $errstr at $errfile:$errline");
        file_put_contents("$log_dir/04-error-details.txt", "Error: $errstr\nFile: $errfile\nLine: $errline\n");
    }
    return false; // Continue with default error handling
});

try {
    wp_set_current_user(1);
    
    $import = new \Elementor\App\Modules\ImportExport\Processes\Import(
        '/exports/tshirtswiss-kit.zip',
        []
    );
    
    $import->register_default_runners();
    
    // Temporarily intercept the save_elements_of_imported_posts method
    $reflection = new ReflectionClass($import);
    $method = $reflection->getMethod('save_elements_of_imported_posts');
    $method->setAccessible(true);
    
    // Call it and catch any errors
    try {
        $method->invoke($import);
    } catch (Throwable $e) {
        error_log("[CAUGHT_EXCEPTION] " . $e->getMessage() . " at " . $e->getFile() . ":" . $e->getLine());
        file_put_contents("$log_dir/05-exception.txt", $e->getMessage() . "\n" . $e->getTraceAsString());
    }
    
} catch (Throwable $e) {
    error_log("[FATAL] " . $e->getMessage());
    file_put_contents("$log_dir/06-fatal.txt", $e->getMessage() . "\n" . $e->getTraceAsString());
}

restore_error_handler();

echo "✓ Import completed (or failed)\n\n";

// ========================================================================
// STEP 4: Analyze captured elements
// ========================================================================

echo "STEP 4: Analyze captured elements\n";
echo str_repeat("-", 80) . "\n";

$element_files = glob("$log_dir/02-element-*.json");
echo "Captured " . count($element_files) . " elements\n\n";

if (!empty($element_files)) {
    echo "First 5 elements:\n";
    foreach (array_slice($element_files, 0, 5) as $file) {
        $data = json_decode(file_get_contents($file), true);
        $id = $data['id'] ?? 'NO_ID';
        $type = $data['elType'] ?? 'NO_TYPE';
        $widget = $data['widgetType'] ?? '';
        echo "  - $id: elType=$type widgetType=$widget\n";
    }
    echo "\n";
}

// ========================================================================
// STEP 5: Compare original vs. what was processed
// ========================================================================

echo "STEP 5: Comparison\n";
echo str_repeat("-", 80) . "\n";

echo "Original page content:\n";
$original_content = $original_json['content'] ?? [];
foreach ($original_content as $i => $elem) {
    $id = $elem['id'] ?? 'NO_ID';
    $type = $elem['elType'] ?? 'NO_TYPE';
    $widget = $elem['widgetType'] ?? '';
    echo "  Element[$i]: id=$id, elType=$type, widgetType=$widget\n";
    
    // Check for nested elements with missing elType
    if (isset($elem['elements']) && is_array($elem['elements'])) {
        foreach ($elem['elements'] as $j => $nested) {
            $n_id = $nested['id'] ?? 'NO_ID';
            $n_type = $nested['elType'] ?? 'MISSING';
            if ($n_type === 'MISSING') {
                echo "    ⚠ NESTED[$j] has MISSING elType: id=$n_id\n";
                file_put_contents("$log_dir/07-malformed-element.json", json_encode($nested, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));
            }
        }
    }
}

echo "\nTrace complete.\n";
echo "Results saved to: $log_dir/\n";
