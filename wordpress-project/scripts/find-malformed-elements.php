<?php
/**
 * FIND MALFORMED ELEMENTS - Scan exported ZIP for elements missing elType
 */

$zip_path = '/exports/tshirtswiss-kit.zip';
$output_dir = '/exports/element-analysis';

if (!is_dir($output_dir)) {
    mkdir($output_dir, 0777, true);
}

echo "Analyzing exported JSON for malformed elements...\n";
echo str_repeat("=", 80) . "\n\n";

$zip = new ZipArchive();
$zip->open($zip_path);

$malformed_elements = [];
$pages_analyzed = 0;

// Scan all pages
for ($i = 0; $i < $zip->numFiles; $i++) {
    $stat = $zip->statIndex($i);
    if (strpos($stat['name'], 'content/page/') === 0 && substr($stat['name'], -5) === '.json') {
        $pages_analyzed++;
        
        $page_data = json_decode($zip->getFromIndex($i), true);
        $page_title = $page_data['title'] ?? 'UNKNOWN';
        
        // Recursively scan for malformed elements
        $scan = null;
        $scan = function($elements, $path = []) use (&$scan, &$malformed_elements, $page_title, $stat) {
            if (!is_array($elements)) {
                return;
            }
            
            foreach ($elements as $index => $element) {
                if (!is_array($element)) {
                    continue;
                }
                
                $elem_id = $element['id'] ?? 'NO_ID';
                $elem_type = $element['elType'] ?? null;
                
                // CHECK: Is elType missing?
                if ($elem_type === null) {
                    $current_path = array_merge($path, [$index]);
                    $malformed_elements[] = [
                        'file' => $stat['name'],
                        'page_title' => $page_title,
                        'element_id' => $elem_id,
                        'path' => $current_path,
                        'element_data' => $element,
                    ];
                    
                    error_log("[MALFORMED] Page: $page_title, Element ID: $elem_id, Path: " . implode('.', $current_path));
                }
                
                // Recurse
                if (isset($element['elements']) && is_array($element['elements'])) {
                    $current_path = array_merge($path, [$index, 'elements']);
                    $scan($element['elements'], $current_path);
                }
            }
        };
        
        $content = $page_data['content'] ?? [];
        $scan($content, ['content']);
    }
}

$zip->close();

echo "Analyzed: $pages_analyzed pages\n";
echo "Malformed elements found: " . count($malformed_elements) . "\n\n";

if (!empty($malformed_elements)) {
    echo "MALFORMED ELEMENTS FOUND:\n";
    echo str_repeat("-", 80) . "\n\n";
    
    foreach ($malformed_elements as $i => $malformed) {
        echo "[" . ($i + 1) . "] Page: {$malformed['page_title']}\n";
        echo "    File: {$malformed['file']}\n";
        echo "    Element ID: {$malformed['element_id']}\n";
        echo "    Path: " . implode(' > ', $malformed['path']) . "\n";
        echo "    Keys in element: " . implode(', ', array_keys($malformed['element_data'])) . "\n";
        echo "\n";
        
        // Save this element
        $filename = "$output_dir/" . str_pad($i + 1, 3, '0', STR_PAD_LEFT) . "_" . 
                    str_replace(['/', ' '], ['_', '_'], $malformed['page_title']) . "_" . 
                    $malformed['element_id'] . ".json";
        file_put_contents($filename, json_encode($malformed['element_data'], JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));
        echo "    Saved: $filename\n\n";
    }
} else {
    echo "✓ No malformed elements found in exported ZIP!\n";
    echo "  All elements have the required 'elType' key.\n";
    echo "  The malformed element must be created DURING import.\n";
}

echo "\n";
echo "Analysis complete.\n";
