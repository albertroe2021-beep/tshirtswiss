<?php
/**
 * Check for unregistered Elementor element types
 * 
 * This script scans all pages and identifies any widgets that are
 * not registered in the current Elementor installation.
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

echo "\nScanning Elementor data for unregistered element types...\n";
echo str_repeat("=", 70) . "\n";

$pages = get_posts([
    'post_type'      => 'page',
    'numberposts'    => -1,
    'fields'         => 'ids',
]);

$unregistered_types = [];
$total_pages = count($pages);
$pages_with_data = 0;
$errors_found = [];

// Get registered widgets
$widgets_manager = \Elementor\Plugin::instance()->widgets_manager;

foreach ($pages as $page_id) {
    $page_title = get_the_title($page_id);
    $elementor_data = get_post_meta($page_id, '_elementor_data', true);
    
    if (!$elementor_data) {
        continue;
    }
    
    if (is_string($elementor_data)) {
        $elementor_data = json_decode($elementor_data, true);
    }
    
    if (!is_array($elementor_data)) {
        continue;
    }
    
    $pages_with_data++;
    
    // Recursive function to scan elements
    $scan_elements = null;
    $scan_elements = function($elements, $page_id, $page_title, $depth = 0) use (&$scan_elements, &$unregistered_types, &$errors_found, $widgets_manager) {
        if (!is_array($elements)) {
            return;
        }
        
        foreach ($elements as $element) {
            if (!is_array($element)) {
                continue;
            }
            
            $el_type = $element['elType'] ?? null;
            $widget_type = $element['widgetType'] ?? null;
            $el_id = $element['id'] ?? 'unknown';
            
            // Check if widget type is registered
            if ($el_type === 'widget' && $widget_type) {
                $widget = $widgets_manager->get_widget_types($widget_type);
                if (!$widget) {
                    $unregistered_types[$widget_type] = ($unregistered_types[$widget_type] ?? 0) + 1;
                    $errors_found[] = [
                        'page_id' => $page_id,
                        'page_title' => $page_title,
                        'element_id' => $el_id,
                        'widget_type' => $widget_type,
                    ];
                }
            }
            
            // Recurse into children
            if (isset($element['elements']) && is_array($element['elements'])) {
                $scan_elements($element['elements'], $page_id, $page_title, $depth + 1);
            }
        }
    };
    
    $scan_elements($elementor_data, $page_id, $page_title);
}

echo "\nRESULTS:\n";
echo str_repeat("-", 70) . "\n";
echo "Total pages: $total_pages\n";
echo "Pages with Elementor data: $pages_with_data\n";

if (empty($unregistered_types)) {
    echo "\n✓ SUCCESS: No unregistered widget types found!\n";
} else {
    echo "\n✗ ERRORS FOUND:\n\n";
    echo "Unregistered widget types:\n";
    foreach ($unregistered_types as $type => $count) {
        echo "  - $type (appears in $count element(s))\n";
    }
    
    echo "\nDetailed errors:\n";
    foreach ($errors_found as $error) {
        echo sprintf(
            "  Page: %s (ID: %d)\n    Element ID: %s\n    Widget Type: %s\n",
            $error['page_title'],
            $error['page_id'],
            $error['element_id'],
            $error['widget_type']
        );
    }
}

echo "\n" . str_repeat("=", 70) . "\n";
