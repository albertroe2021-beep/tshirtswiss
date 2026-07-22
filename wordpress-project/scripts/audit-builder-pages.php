<?php
/**
 * AUDIT BUILDER PAGES - Which pages have Elementor data?
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

echo "BUILDER SITE AUDIT - PAGE ELEMENTOR DATA\n";
echo str_repeat("=", 80) . "\n\n";

$pages = get_posts([
    'post_type'      => 'page',
    'numberposts'    => -1,
    'post_status'    => 'publish',
    'orderby'        => 'ID',
]);

echo "Total published pages: " . count($pages) . "\n\n";
echo "Pages with Elementor data:\n\n";

$pages_with_data = 0;
$pages_without_data = 0;
$samples = [];

foreach ($pages as $page) {
    $page_id = $page->ID;
    $page_title = $page->post_title;
    $elementor_data = get_post_meta($page_id, '_elementor_data', true);
    
    if ($elementor_data === false || $elementor_data === '') {
        $pages_without_data++;
        if ($pages_without_data <= 5) {
            echo "  ✗ ID: $page_id | Title: '$page_title' | Status: NO DATA\n";
        }
    } else {
        $pages_with_data++;
        
        if (is_string($elementor_data)) {
            $size = strlen($elementor_data);
            $decoded = json_decode($elementor_data, true);
            $elem_count = 0;
            
            if (is_array($decoded)) {
                foreach ($decoded as $item) {
                    if (is_array($item) && isset($item['elType'])) {
                        $elem_count++;
                    }
                }
            }
            
            echo "  ✓ ID: $page_id | Title: '$page_title' | Size: $size bytes | Elements: $elem_count\n";
            
            if (count($samples) < 3) {
                $samples[] = [
                    'id' => $page_id,
                    'title' => $page_title,
                    'size' => $size,
                    'elements' => $elem_count,
                ];
            }
        }
    }
}

echo "\n" . str_repeat("=", 80) . "\n";
echo "SUMMARY\n";
echo str_repeat("=", 80) . "\n\n";
echo "Pages with Elementor data: $pages_with_data\n";
echo "Pages WITHOUT Elementor data: $pages_without_data\n\n";

if (!empty($samples)) {
    echo "Sample pages with data:\n";
    foreach ($samples as $sample) {
        echo "  - {$sample['title']} (ID: {$sample['id']})\n";
        echo "    Size: {$sample['size']} bytes\n";
        echo "    Elements: {$sample['elements']}\n";
    }
    echo "\n";
}

if ($pages_with_data > 0) {
    echo "✓ Builder has pages with Elementor content\n";
    echo "These pages should be in the export and should import correctly.\n";
} else {
    echo "⚠ CRITICAL: Builder has NO pages with Elementor data!\n";
    echo "All pages are empty stubs. Nothing to export.\n";
}

echo "\n";
echo "Audit complete.\n";
