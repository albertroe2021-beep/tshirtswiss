<?php
/**
 * TRACE PAGE DATA PIPELINE
 * 
 * Compare _elementor_data across three stages:
 * 1. Builder site before export
 * 2. Inside exported ZIP file
 * 3. Validation site after import
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

// Get first page from builder
$pages = get_posts([
    'post_type'   => 'page',
    'numberposts' => 1,
    'post_status' => 'publish',
]);

if (empty($pages)) {
    echo "ERROR: No published pages found in builder\n";
    exit(1);
}

$page = $pages[0];
$page_id = $page->ID;
$page_title = $page->post_title;

echo "STAGE 1: BUILDER SITE (Before Export)\n";
echo str_repeat("=", 80) . "\n";
echo "Page: $page_title (ID: $page_id)\n";
echo "\n";

// Get _elementor_data from builder
$elementor_data = get_post_meta($page_id, '_elementor_data', true);

echo "Checking _elementor_data post meta:\n";

if ($elementor_data === false) {
    echo "  Status: POST META DOES NOT EXIST\n";
    echo "  Value: (null)\n";
} elseif ($elementor_data === '') {
    echo "  Status: POST META EXISTS BUT IS EMPTY\n";
    echo "  Value: (empty string)\n";
} elseif (is_string($elementor_data)) {
    $size = strlen($elementor_data);
    echo "  Status: POST META EXISTS (string)\n";
    echo "  Size: $size bytes\n";
    
    // Try to parse as JSON
    $decoded = json_decode($elementor_data, true);
    if ($decoded === null) {
        echo "  JSON: INVALID - json_last_error: " . json_last_error_msg() . "\n";
    } else {
        echo "  JSON: VALID\n";
        echo "  Top-level type: " . gettype($decoded) . "\n";
        
        if (is_array($decoded)) {
            echo "  Array size: " . count($decoded) . "\n";
            
            // Show first few keys
            $keys = array_slice(array_keys($decoded), 0, 5);
            echo "  First keys: " . implode(', ', $keys) . "\n";
        }
    }
    
    echo "\n";
    echo "First 500 characters:\n";
    echo substr($elementor_data, 0, 500) . "\n";
    echo "\n";
} else {
    echo "  Status: POST META EXISTS (non-string type)\n";
    echo "  Type: " . gettype($elementor_data) . "\n";
}

echo "\n";
echo str_repeat("=", 80) . "\n";
echo "STAGE 2: EXPORTED ZIP\n";
echo str_repeat("=", 80) . "\n";

// The ZIP file contains page data under content/page/{ID}.json
// But the mapping might be different - let's check manifest first

$zip_path = '/exports/tshirtswiss-kit.zip';

if (!file_exists($zip_path)) {
    echo "ERROR: Export ZIP not found at $zip_path\n";
    exit(1);
}

echo "ZIP File: $zip_path\n";
echo "Checking for page content in ZIP...\n\n";

$zip = new ZipArchive();
if (!$zip->open($zip_path)) {
    echo "ERROR: Could not open ZIP file\n";
    exit(1);
}

// First check manifest to see page mapping
$manifest_json = $zip->getFromName('manifest.json');
if ($manifest_json === false) {
    echo "ERROR: No manifest.json in ZIP\n";
    exit(1);
}

$manifest = json_decode($manifest_json, true);
echo "Manifest loaded. Pages listed in manifest:\n";

$pages_in_manifest = [];
if (isset($manifest['content']['pages']) && is_array($manifest['content']['pages'])) {
    $pages_in_manifest = array_keys($manifest['content']['pages']);
    echo "  Found " . count($pages_in_manifest) . " pages\n";
    
    // Show first few
    echo "  Sample pages: " . implode(', ', array_slice($pages_in_manifest, 0, 3)) . "\n";
}

echo "\n";

// Look for page files that contain our page title
echo "Searching ZIP for our page content...\n";

$found_in_zip = false;
$searched_files = [];

// Try to find the page by checking all content/page/*.json files
$all_files = [];
for ($i = 0; $i < $zip->numFiles; $i++) {
    $stat = $zip->statIndex($i);
    $all_files[] = $stat['name'];
}

$page_files = array_filter($all_files, function($f) {
    return strpos($f, 'content/page/') === 0 && substr($f, -5) === '.json';
});

echo "Found " . count($page_files) . " page JSON files in ZIP\n\n";

// Check each page file for our test page
foreach ($page_files as $page_file) {
    $content_json = $zip->getFromName($page_file);
    if ($content_json === false) continue;
    
    $content = json_decode($content_json, true);
    if (!is_array($content)) continue;
    
    // Check if this is our page
    if (isset($content['title']) && $content['title'] === $page_title) {
        echo "✓ Found matching page in: $page_file\n";
        echo "  Title in ZIP: " . $content['title'] . "\n";
        echo "  Content keys: " . implode(', ', array_keys($content)) . "\n";
        
        echo "\n";
        echo "Checking 'content' field:\n";
        
        if (isset($content['content'])) {
            $content_field = $content['content'];
            echo "  Type: " . gettype($content_field) . "\n";
            
            if (is_string($content_field)) {
                $size = strlen($content_field);
                echo "  Size: $size bytes\n";
                
                // Check if it's JSON string or raw array
                $decoded = json_decode($content_field, true);
                if ($decoded !== null) {
                    echo "  Content is JSON string\n";
                    echo "  Decoded type: " . gettype($decoded) . "\n";
                    if (is_array($decoded)) {
                        echo "  Array length: " . count($decoded) . "\n";
                    }
                } else {
                    echo "  Content is NOT valid JSON string\n";
                    echo "  First 200 chars: " . substr($content_field, 0, 200) . "\n";
                }
            } elseif (is_array($content_field)) {
                echo "  Content is array with " . count($content_field) . " elements\n";
            } else {
                echo "  Content type unexpected: " . gettype($content_field) . "\n";
            }
        } else {
            echo "  No 'content' field found!\n";
        }
        
        echo "\n";
        echo "First 500 chars of page file content:\n";
        echo substr($content_json, 0, 500) . "\n";
        
        $found_in_zip = true;
        break;
    }
}

if (!$found_in_zip) {
    echo "⚠ Could not find page by title in ZIP files\n";
    echo "Trying first available page file for comparison...\n\n";
    
    if (!empty($page_files)) {
        $sample_file = array_values($page_files)[0];
        echo "Using sample: $sample_file\n";
        
        $content_json = $zip->getFromName($sample_file);
        $content = json_decode($content_json, true);
        
        if (isset($content['title'])) {
            echo "Sample page title: " . $content['title'] . "\n";
        }
        if (isset($content['content'])) {
            echo "Sample has 'content' field: YES\n";
            echo "Content type: " . gettype($content['content']) . "\n";
            if (is_string($content['content'])) {
                echo "Content size: " . strlen($content['content']) . " bytes\n";
            }
        }
    }
}

$zip->close();

echo "\n";
echo str_repeat("=", 80) . "\n";
echo "STAGE 3: VALIDATION SITE (After Import)\n";
echo str_repeat("=", 80) . "\n";

// For this stage, we need to check the validation WordPress
// But we're currently running in the builder context
// So we'll output instructions for checking validation

echo "To check the validation site, run:\n";
echo "\n";
echo "  docker compose -f docker-compose.validation.yml run --rm wpcli wp post meta get <PAGE_ID> _elementor_data --allow-root\n";
echo "\n";
echo "Where <PAGE_ID> is the ID of the imported page with title: $page_title\n";
echo "\n";
echo "In the validation database, the same page should exist with imported data.\n";
