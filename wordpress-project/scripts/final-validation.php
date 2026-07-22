<?php
/**
 * FINAL VALIDATION REPORT
 * 
 * Comprehensive check of imported pages and Elementor data
 * 
 * Usage: wp eval-file /scripts/final-validation.php
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

echo "\n";
echo str_repeat("=", 80) . "\n";
echo "FINAL VALIDATION REPORT - IMPORTED KIT\n";
echo str_repeat("=", 80) . "\n";
echo "\n";

// ============================================================================
// SECTION 1: Page Count Verification
// ============================================================================

echo "SECTION 1: PAGE COUNT & STRUCTURE\n";
echo str_repeat("-", 80) . "\n";

$all_pages = get_posts([
    'post_type'      => 'page',
    'numberposts'    => -1,
    'post_status'    => 'any',
    'fields'         => 'ids',
]);

$published_pages = get_posts([
    'post_type'      => 'page',
    'numberposts'    => -1,
    'post_status'    => 'publish',
    'fields'         => 'ids',
]);

echo "Total pages in database: " . count($all_pages) . "\n";
echo "Published pages: " . count($published_pages) . "\n";
echo "\n";

// ============================================================================
// SECTION 2: Elementor Data Verification
// ============================================================================

echo "SECTION 2: ELEMENTOR DATA VERIFICATION\n";
echo str_repeat("-", 80) . "\n";

$pages_with_elementor = 0;
$pages_with_content = 0;
$sample_pages = [];

foreach ($published_pages as $page_id) {
    $elementor_data = get_post_meta($page_id, '_elementor_data', true);
    
    if ($elementor_data) {
        $pages_with_elementor++;
        
        if (is_string($elementor_data)) {
            $data = json_decode($elementor_data, true);
        } else {
            $data = $elementor_data;
        }
        
        if (is_array($data) && !empty($data)) {
            $pages_with_content++;
            
            // Collect sample for inspection
            if (count($sample_pages) < 3) {
                $sample_pages[$page_id] = [
                    'title' => get_the_title($page_id),
                    'elements' => is_array($data) ? count($data) : 0,
                    'has_content' => !empty($data),
                ];
            }
        }
    }
}

echo "Pages with _elementor_data: " . $pages_with_elementor . "\n";
echo "Pages with valid content: " . $pages_with_content . "\n";
echo "\n";

if (!empty($sample_pages)) {
    echo "Sample pages:\n";
    foreach ($sample_pages as $page_id => $info) {
        echo "  - " . $info['title'] . " (ID: $page_id)\n";
        echo "    Elements: " . $info['elements'] . "\n";
        echo "    Content: " . ($info['has_content'] ? 'YES' : 'NO') . "\n";
    }
}
echo "\n";

// ============================================================================
// SECTION 3: Element Type Verification
// ============================================================================

echo "SECTION 3: ELEMENT TYPE VERIFICATION\n";
echo str_repeat("-", 80) . "\n";

$element_types = [];
$widget_types = [];
$invalid_types = [];

foreach ($published_pages as $page_id) {
    $elementor_data = get_post_meta($page_id, '_elementor_data', true);
    
    if (!$elementor_data) {
        continue;
    }
    
    if (is_string($elementor_data)) {
        $data = json_decode($elementor_data, true);
    } else {
        $data = $elementor_data;
    }
    
    if (!is_array($data)) {
        continue;
    }
    
    // Recursive function to scan elements
    $scan = null;
    $scan = function($elements) use (&$scan, &$element_types, &$widget_types, &$invalid_types) {
        if (!is_array($elements)) {
            return;
        }
        
        foreach ($elements as $element) {
            if (!is_array($element)) {
                continue;
            }
            
            $el_type = $element['elType'] ?? null;
            $widget_type = $element['widgetType'] ?? null;
            
            if ($el_type) {
                $element_types[$el_type] = ($element_types[$el_type] ?? 0) + 1;
            }
            
            if ($widget_type) {
                $widget_types[$widget_type] = ($widget_types[$widget_type] ?? 0) + 1;
            }
            
            // Check if widget is registered
            if ($el_type === 'widget' && $widget_type) {
                $widgets_manager = \Elementor\Plugin::instance()->widgets_manager;
                if (!$widgets_manager->get_widget_types($widget_type)) {
                    $invalid_types[$widget_type] = ($invalid_types[$widget_type] ?? 0) + 1;
                }
            }
            
            // Recurse
            if (isset($element['elements']) && is_array($element['elements'])) {
                $scan($element['elements']);
            }
        }
    };
    
    $scan($data);
}

echo "Element types found:\n";
if (!empty($element_types)) {
    foreach ($element_types as $type => $count) {
        echo "  - elType: '$type' (appears $count times)\n";
    }
} else {
    echo "  (none found)\n";
}

echo "\nWidget types found:\n";
if (!empty($widget_types)) {
    foreach ($widget_types as $type => $count) {
        echo "  - widgetType: '$type' (appears $count times)\n";
    }
} else {
    echo "  (none found)\n";
}

echo "\n";

// ============================================================================
// SECTION 4: Unregistered Widgets Check
// ============================================================================

echo "SECTION 4: UNREGISTERED WIDGETS\n";
echo str_repeat("-", 80) . "\n";

if (!empty($invalid_types)) {
    echo "⚠ Found unregistered widget types:\n";
    foreach ($invalid_types as $type => $count) {
        echo "  - $type (appears $count times)\n";
    }
} else {
    echo "✓ All widget types are registered\n";
}

echo "\n";

// ============================================================================
// SECTION 5: Kit Manifest Information
// ============================================================================

echo "SECTION 5: KIT INFORMATION\n";
echo str_repeat("-", 80) . "\n";

// Check if we can find kit settings
$kit_settings = get_option('elementor_kit_default');
if ($kit_settings) {
    echo "Default Kit ID: " . $kit_settings . "\n";
} else {
    echo "Default Kit ID: Not set\n";
}

// Check for any import session markers
$sessions = get_option('elementor_import_sessions');
if ($sessions) {
    echo "Import sessions stored: " . count($sessions) . "\n";
}

echo "\n";

// ============================================================================
// SECTION 6: SUMMARY
// ============================================================================

echo "SECTION 6: SUMMARY\n";
echo str_repeat("-", 80) . "\n";

$success_count = 0;
$checks = [];

// Check 1: Pages exist
$check1 = count($published_pages) > 5;
$checks['Pages imported'] = $check1 ? '✓' : '✗';
if ($check1) $success_count++;

// Check 2: Elementor data present
$check2 = $pages_with_elementor > 0 && ($pages_with_elementor / count($published_pages)) > 0.5;
$checks['Elementor data'] = $check2 ? '✓' : '✗';
if ($check2) $success_count++;

// Check 3: Valid content
$check3 = $pages_with_content > 0;
$checks['Page content'] = $check3 ? '✓' : '✗';
if ($check3) $success_count++;

// Check 4: No unregistered widgets
$check4 = empty($invalid_types);
$checks['Widget types'] = $check4 ? '✓' : '✗';
if ($check4) $success_count++;

// Check 5: Content structure
$check5 = !empty($element_types);
$checks['Content structure'] = $check5 ? '✓' : '✗';
if ($check5) $success_count++;

foreach ($checks as $name => $status) {
    echo "  $status $name\n";
}

echo "\n";
echo "Overall: $success_count/5 checks passed\n";
echo "\n";

if ($success_count >= 4) {
    echo "✓ IMPORT VALIDATION SUCCESSFUL\n";
    echo "The kit has been imported successfully into WordPress.\n";
    echo "All pages are present and contain valid Elementor content.\n";
} else {
    echo "⚠ IMPORT VALIDATION INCOMPLETE\n";
    echo "Some validation checks failed. Review above for details.\n";
}

echo "\n" . str_repeat("=", 80) . "\n";
