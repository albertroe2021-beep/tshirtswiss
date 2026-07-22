<?php
/**
 * INSTRUMENTED IMPORT TRACE - Trace Home page through entire import lifecycle
 * 
 * Maps exactly where valid Elementor data becomes []
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

$trace_log = [];

function trace($stage, $msg, $data = null) {
    global $trace_log;
    $entry = [
        'stage' => $stage,
        'time' => microtime(true),
        'msg' => $msg,
        'data' => $data,
    ];
    $trace_log[] = $entry;
    error_log("[TRACE] [$stage] $msg " . ($data ? json_encode($data) : ''));
}

echo "==========================================================================\n";
echo "INSTRUMENTED IMPORT TRACE - Home Page Lifecycle\n";
echo "==========================================================================\n\n";

// ========================================================================
// STAGE 1: Extract Home page JSON from ZIP
// ========================================================================

echo "STAGE 1: Extract Home page JSON from ZIP\n";
echo str_repeat("-", 80) . "\n";

$zip_path = '/exports/tshirtswiss-kit.zip';
$zip = new ZipArchive();
if (!$zip->open($zip_path)) {
    echo "ERROR: Could not open ZIP\n";
    exit(1);
}

$home_page_json = null;
$home_page_file = null;

// Find first available page (page ID 36 is typically first)
for ($i = 0; $i < $zip->numFiles; $i++) {
    $stat = $zip->statIndex($i);
    if (strpos($stat['name'], 'content/page/36.json') === 0) {
        $content = $zip->getFromIndex($i);
        $home_page_json = json_decode($content, true);
        $home_page_file = $stat['name'];
        break;
    }
}

// If not found, find any page
if (!$home_page_json) {
    for ($i = 0; $i < $zip->numFiles; $i++) {
        $stat = $zip->statIndex($i);
        if (strpos($stat['name'], 'content/page/') === 0 && substr($stat['name'], -5) === '.json') {
            $content = $zip->getFromIndex($i);
            $home_page_json = json_decode($content, true);
            $home_page_file = $stat['name'];
            break;
        }
    }
}

if (!$home_page_json) {
    echo "ERROR: No pages found in ZIP\n";
    exit(1);
}

$content_in_zip = $home_page_json['content'] ?? [];
$zip_content_size = strlen(json_encode($content_in_zip));
$zip_first_element = null;
if (is_array($content_in_zip) && count($content_in_zip) > 0) {
    $zip_first_element = $content_in_zip[0];
}

echo "✓ Found Home page in: $home_page_file\n";
echo "  Content size: $zip_content_size bytes\n";
echo "  Root elements count: " . count($content_in_zip) . "\n";
if ($zip_first_element) {
    echo "  First element type: " . ($zip_first_element['elType'] ?? 'N/A') . "\n";
    if (isset($zip_first_element['widgetType'])) {
        echo "  First widget type: " . $zip_first_element['widgetType'] . "\n";
    }
}
echo "\n";

trace('STAGE_1', 'ZIP Home page extracted', [
    'file' => $home_page_file,
    'content_size' => $zip_content_size,
    'element_count' => count($content_in_zip),
]);

$zip->close();

// ========================================================================
// STAGE 2: Monitor the Import class behavior
// ========================================================================

echo "STAGE 2: Trace data through Import class instantiation\n";
echo str_repeat("-", 80) . "\n";

// Before import, check if Home page already exists
$existing_homes = get_posts([
    'post_type' => 'page',
    'title' => 'Home',
    'post_status' => 'publish',
    'numberposts' => -1,
]);

echo "Pre-import pages in database: " . count($existing_homes) . "\n\n";

// ========================================================================
// STAGE 3: Import with hooks to monitor data
// ========================================================================

echo "STAGE 3: Import with data monitoring hooks\n";
echo str_repeat("-", 80) . "\n";

// We need to hook into the Import process
// Add a filter to catch when elements are set

$home_page_id_pre_import = null;
$home_page_id_post_import = null;

// Hook to monitor post saves
add_action('save_post', function($post_id) {
    global $home_page_id_post_import;
    $post = get_post($post_id);
    if ($post->post_type === 'page' && $post->post_title === 'Home') {
        $home_page_id_post_import = $post_id;
        error_log("[HOOK] save_post for Home (ID: $post_id)");
    }
}, 10, 1);

// Hook to monitor post meta updates
add_action('update_post_meta', function($meta_id, $post_id, $meta_key, $meta_value) {
    if ($meta_key === '_elementor_data') {
        $post = get_post($post_id);
        if ($post && $post->post_type === 'page') {
            $size = is_string($meta_value) ? strlen($meta_value) : strlen(json_encode($meta_value));
            error_log("[HOOK] update_post_meta _elementor_data (ID: $post_id, title: {$post->post_title}, size: $size bytes)");
            trace('STAGE_3', 'Elementor data being saved', [
                'post_id' => $post_id,
                'post_title' => $post->post_title,
                'size' => $size,
                'first_chars' => substr(is_string($meta_value) ? $meta_value : json_encode($meta_value), 0, 100),
            ]);
        }
    }
}, 10, 4);

// Now perform the import
echo "Invoking Elementor Import...\n";

$kit_path = '/exports/tshirtswiss-kit.zip';
$import_settings = [];

try {
    $import = new \Elementor\App\Modules\ImportExport\Processes\Import(
        $kit_path,
        $import_settings
    );
    
    trace('STAGE_3', 'Import object instantiated', []);
    echo "✓ Import object created\n";
    
    $import->register_default_runners();
    trace('STAGE_3', 'Default runners registered', []);
    echo "✓ Runners registered\n";
    
    // Check current admin user
    $current_user = wp_get_current_user();
    echo "✓ Current user: {$current_user->user_login} (ID: {$current_user->ID})\n";
    
    $result = $import->run();
    trace('STAGE_3', 'Import completed', ['result' => $result]);
    echo "✓ Import completed\n";
    
} catch (Exception $e) {
    echo "ERROR during import: " . $e->getMessage() . "\n";
    trace('STAGE_3', 'Import exception', ['error' => $e->getMessage()]);
}

echo "\n";

// ========================================================================
// STAGE 4: Check Home page immediately after import
// ========================================================================

echo "STAGE 4: Check Home page after import\n";
echo str_repeat("-", 80) . "\n";

$home_pages = get_posts([
    'post_type' => 'page',
    'post_status' => 'publish',
    'numberposts' => -1,
    'orderby' => 'modified',
    'order' => 'DESC',
]);

if (empty($home_pages)) {
    echo "ERROR: No pages found after import\n";
    exit(1);
}

// Use first page that was just imported (most recent)
$home_page = $home_pages[0];
$home_page_id = $home_page->ID;

echo "✓ Found Home page (ID: $home_page_id)\n";

// Get the _elementor_data
$elementor_data_post_meta = get_post_meta($home_page_id, '_elementor_data', true);

if ($elementor_data_post_meta === false) {
    echo "⚠ _elementor_data post meta: NOT FOUND\n";
    trace('STAGE_4', '_elementor_data not found', []);
} else {
    echo "✓ _elementor_data post meta: EXISTS\n";
    
    if (is_string($elementor_data_post_meta)) {
        $size = strlen($elementor_data_post_meta);
        echo "  Size: $size bytes\n";
        
        $decoded = json_decode($elementor_data_post_meta, true);
        if (is_array($decoded)) {
            echo "  JSON valid: YES\n";
            echo "  Array length: " . count($decoded) . "\n";
            echo "  First 100 chars: " . substr($elementor_data_post_meta, 0, 100) . "\n";
            
            trace('STAGE_4', '_elementor_data after import', [
                'size' => $size,
                'array_length' => count($decoded),
                'first_element_type' => ($decoded[0]['elType'] ?? null) ?? 'EMPTY ARRAY',
            ]);
        } else {
            echo "  JSON valid: NO\n";
        }
    }
}

echo "\n";

// ========================================================================
// STAGE 5: Direct database query
// ========================================================================

echo "STAGE 5: Direct database query\n";
echo str_repeat("-", 80) . "\n";

global $wpdb;
$result = $wpdb->get_row($wpdb->prepare(
    "SELECT meta_value FROM {$wpdb->postmeta} WHERE post_id = %d AND meta_key = %s",
    $home_page_id,
    '_elementor_data'
));

if (!$result) {
    echo "⚠ Database: _elementor_data NOT FOUND\n";
} else {
    $db_value = $result->meta_value;
    $db_size = strlen($db_value);
    
    echo "✓ Database: _elementor_data EXISTS\n";
    echo "  Size: $db_size bytes\n";
    echo "  Value (first 100 chars): " . substr($db_value, 0, 100) . "\n";
    
    trace('STAGE_5', '_elementor_data from database', [
        'size' => $db_size,
        'value' => $db_value,
    ]);
}

echo "\n";

// ========================================================================
// COMPARISON
// ========================================================================

echo str_repeat("=", 80) . "\n";
echo "DATA COMPARISON\n";
echo str_repeat("=", 80) . "\n\n";

echo "Stage 1 (ZIP):\n";
echo "  Content size: $zip_content_size bytes\n";
echo "  Elements: " . count($content_in_zip) . "\n\n";

echo "Stage 4 (After import, from post meta):\n";
if (is_string($elementor_data_post_meta)) {
    $decoded = json_decode($elementor_data_post_meta, true);
    echo "  Content size: " . strlen($elementor_data_post_meta) . " bytes\n";
    echo "  Elements: " . (is_array($decoded) ? count($decoded) : 'N/A') . "\n\n";
}

echo "Stage 5 (After import, from database):\n";
if ($result) {
    $decoded = json_decode($result->meta_value, true);
    echo "  Content size: " . strlen($result->meta_value) . " bytes\n";
    echo "  Elements: " . (is_array($decoded) ? count($decoded) : 'N/A') . "\n\n";
}

echo "\n";
echo "CONCLUSION:\n";
echo str_repeat("-", 80) . "\n";

$zip_content_count = count($content_in_zip);
$post_meta_content = @json_decode($elementor_data_post_meta, true) ?: [];
$post_meta_count = count($post_meta_content);

if ($zip_content_count > 0 && $post_meta_count === 0) {
    echo "⚠ DATA LOSS DETECTED\n";
    echo "  Before import (ZIP): $zip_content_count elements\n";
    echo "  After import (DB): 0 elements\n";
    echo "\n  The Elementor data was replaced with an empty array during import.\n";
} else if ($zip_content_count === $post_meta_count) {
    echo "✓ DATA PRESERVED\n";
    echo "  Both have $zip_content_count elements\n";
} else {
    echo "? DATA MISMATCH\n";
    echo "  ZIP: $zip_content_count elements\n";
    echo "  DB: $post_meta_count elements\n";
}

echo "\n";

// ========================================================================
// OUTPUT TRACE LOG
// ========================================================================

echo "\nFull Trace Log:\n";
echo str_repeat("-", 80) . "\n";

foreach ($trace_log as $entry) {
    echo "[{$entry['stage']}] {$entry['msg']}\n";
    if ($entry['data']) {
        echo "  Data: " . json_encode($entry['data']) . "\n";
    }
}

echo "\n";
echo "Trace complete. Check error log for detailed output.\n";
