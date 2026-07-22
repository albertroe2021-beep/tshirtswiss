<?php
/**
 * TRACE PAGE DATA PIPELINE - Output to file
 * 
 * Compare _elementor_data across three stages:
 * 1. Builder site before export
 * 2. Inside exported ZIP file
 * 3. Validation site after import
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

$output_file = '/exports/trace-report.txt';

function log_msg($msg) {
    global $output_file;
    if (empty($output_file)) {
        $output_file = '/exports/trace-report.txt';
    }
    file_put_contents($output_file, $msg . "\n", FILE_APPEND);
}

// Clear previous output
file_put_contents($output_file, "");

log_msg("TRACE PAGE DATA PIPELINE");
log_msg("==========================================================================");
log_msg("");

// Get first page from builder
$pages = get_posts([
    'post_type'   => 'page',
    'numberposts' => 1,
    'post_status' => 'publish',
]);

if (empty($pages)) {
    log_msg("ERROR: No published pages found in builder");
    exit(1);
}

$page = $pages[0];
$page_id = $page->ID;
$page_title = $page->post_title;

log_msg("STAGE 1: BUILDER SITE (Before Export)");
log_msg("==========================================================================");
log_msg("Page: $page_title (ID: $page_id)");
log_msg("");

// Get _elementor_data from builder
$elementor_data = get_post_meta($page_id, '_elementor_data', true);

log_msg("Checking _elementor_data post meta:");
log_msg("");

if ($elementor_data === false) {
    log_msg("  Status: POST META DOES NOT EXIST");
    log_msg("  Value: (null)");
} elseif ($elementor_data === '') {
    log_msg("  Status: POST META EXISTS BUT IS EMPTY");
    log_msg("  Value: (empty string)");
} elseif (is_string($elementor_data)) {
    $size = strlen($elementor_data);
    log_msg("  Status: POST META EXISTS (string)");
    log_msg("  Size: $size bytes");
    
    // Try to parse as JSON
    $decoded = json_decode($elementor_data, true);
    if ($decoded === null) {
        log_msg("  JSON: INVALID - json_last_error: " . json_last_error_msg());
    } else {
        log_msg("  JSON: VALID");
        log_msg("  Top-level type: " . gettype($decoded));
        
        if (is_array($decoded)) {
            log_msg("  Array size: " . count($decoded));
            
            // Count elements
            $elem_count = 0;
            foreach ($decoded as $item) {
                if (is_array($item) && isset($item['elType'])) {
                    $elem_count++;
                }
            }
            log_msg("  Elements found: $elem_count");
        }
    }
    
    log_msg("");
    log_msg("First 500 characters:");
    log_msg(substr($elementor_data, 0, 500));
    log_msg("");
} else {
    log_msg("  Status: POST META EXISTS (non-string type)");
    log_msg("  Type: " . gettype($elementor_data));
}

log_msg("");
log_msg("==========================================================================");
log_msg("STAGE 2: EXPORTED ZIP FILE");
log_msg("==========================================================================");
log_msg("");

$zip_path = '/exports/tshirtswiss-kit.zip';

if (!file_exists($zip_path)) {
    log_msg("ERROR: Export ZIP not found at $zip_path");
    exit(1);
}

log_msg("ZIP File: $zip_path");
log_msg("File size: " . filesize($zip_path) . " bytes");
log_msg("");

$zip = new ZipArchive();
if (!$zip->open($zip_path)) {
    log_msg("ERROR: Could not open ZIP file");
    exit(1);
}

log_msg("ZIP opened successfully");
log_msg("Total files in ZIP: " . $zip->numFiles);
log_msg("");

// First check manifest to see page mapping
$manifest_json = $zip->getFromName('manifest.json');
if ($manifest_json === false) {
    log_msg("ERROR: No manifest.json in ZIP");
    exit(1);
}

$manifest = json_decode($manifest_json, true);
log_msg("Manifest loaded successfully");
log_msg("");

$pages_in_manifest = [];
if (isset($manifest['content']['pages']) && is_array($manifest['content']['pages'])) {
    $pages_in_manifest = $manifest['content']['pages'];
    log_msg("Pages listed in manifest: " . count($pages_in_manifest));
}

log_msg("");
log_msg("Searching ZIP for page: '$page_title'");
log_msg("");

// Get all files
$all_files = [];
for ($i = 0; $i < $zip->numFiles; $i++) {
    $stat = $zip->statIndex($i);
    $all_files[] = $stat['name'];
}

$page_files = array_filter($all_files, function($f) {
    return strpos($f, 'content/page/') === 0 && substr($f, -5) === '.json';
});

log_msg("Found " . count($page_files) . " page JSON files in ZIP");
log_msg("");

// Check each page file for our test page
$found_in_zip = false;
foreach ($page_files as $page_file) {
    $content_json = $zip->getFromName($page_file);
    if ($content_json === false) continue;
    
    $content = json_decode($content_json, true);
    if (!is_array($content)) continue;
    
    // Check if this is our page
    if (isset($content['title']) && $content['title'] === $page_title) {
        log_msg("✓ Found matching page in: $page_file");
        log_msg("  Title: " . $content['title']);
        log_msg("  Keys in page: " . implode(', ', array_keys($content)));
        log_msg("");
        
        log_msg("Analyzing 'content' field in ZIP:");
        log_msg("");
        
        if (isset($content['content'])) {
            $content_field = $content['content'];
            log_msg("  Field exists: YES");
            log_msg("  Type: " . gettype($content_field));
            
            if (is_string($content_field)) {
                $size = strlen($content_field);
                log_msg("  Size: $size bytes");
                
                // Check if it's JSON string
                $decoded = json_decode($content_field, true);
                if ($decoded !== null) {
                    log_msg("  Content is JSON string: YES");
                    log_msg("  Decoded type: " . gettype($decoded));
                    if (is_array($decoded)) {
                        log_msg("  Array length: " . count($decoded));
                        
                        // Count elements
                        $elem_count = 0;
                        foreach ($decoded as $item) {
                            if (is_array($item) && isset($item['elType'])) {
                                $elem_count++;
                            }
                        }
                        log_msg("  Elements with elType: $elem_count");
                    }
                } else {
                    log_msg("  Content is JSON string: NO");
                    log_msg("  First 200 chars: " . substr($content_field, 0, 200));
                }
            } elseif (is_array($content_field)) {
                log_msg("  Content is array: YES");
                log_msg("  Array length: " . count($content_field));
                
                // Count elements
                $elem_count = 0;
                foreach ($content_field as $item) {
                    if (is_array($item) && isset($item['elType'])) {
                        $elem_count++;
                    }
                }
                log_msg("  Elements with elType: $elem_count");
            }
        } else {
            log_msg("  Field exists: NO");
        }
        
        log_msg("");
        log_msg("First 300 chars of page JSON from ZIP:");
        log_msg(substr($content_json, 0, 300));
        log_msg("");
        
        $found_in_zip = true;
        break;
    }
}

if (!$found_in_zip) {
    log_msg("⚠ Could not find page by title in ZIP");
    log_msg("");
    
    // Try first page
    if (!empty($page_files)) {
        $sample_file = array_values($page_files)[0];
        log_msg("Using first page file for reference: $sample_file");
        log_msg("");
        
        $content_json = $zip->getFromName($sample_file);
        $content = json_decode($content_json, true);
        
        if (isset($content['title'])) {
            log_msg("Sample page title: " . $content['title']);
        }
        if (isset($content['content'])) {
            log_msg("Sample has 'content' field: YES");
            log_msg("Content type: " . gettype($content['content']));
            if (is_string($content['content'])) {
                log_msg("Content size: " . strlen($content['content']) . " bytes");
            } elseif (is_array($content['content'])) {
                log_msg("Content array length: " . count($content['content']));
            }
        } else {
            log_msg("Sample has 'content' field: NO");
        }
        log_msg("");
    }
}

$zip->close();

log_msg("");
log_msg("==========================================================================");
log_msg("STAGE 3: VALIDATION SITE (After Import) - SEE SEPARATE REPORT");
log_msg("==========================================================================");
log_msg("");
log_msg("To check validation site, look for page titled: '$page_title'");
log_msg("And verify its _elementor_data post meta.");
log_msg("");
log_msg("Report written to: $output_file");

echo "Trace complete. Results written to /exports/trace-report.txt\n";
