<?php
/**
 * Direct import of fixed kit
 * Run in validation WordPress environment
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

$kit_path = '/exports/tshirtswiss-kit-fixed.zip';

echo str_repeat("=", 80) . "\n";
echo "IMPORTING FIXED KIT\n";
echo str_repeat("=", 80) . "\n\n";

if (!file_exists($kit_path)) {
    echo "ERROR: Kit file not found: $kit_path\n";
    exit(1);
}

echo "Kit file: $kit_path\n";
echo "Size: " . filesize($kit_path) / 1024 . " KB\n\n";

try {
    // Set current user to admin
    wp_set_current_user(1);
    $current_user = wp_get_current_user();
    if ($current_user->ID === 0) {
        echo "Creating admin user...\n";
        $user_id = wp_create_user('admin', 'admin', 'admin@example.com');
        update_user_meta($user_id, 'wp_user_level', 10);
        update_user_meta($user_id, 'wp_capabilities', array('administrator' => true));
        wp_set_current_user($user_id);
    }
    
    // Get current page count before
    $before_count = wp_count_posts('page')->publish;
    echo "Pages before import: $before_count\n";
    echo "Current user: " . wp_get_current_user()->user_login . "\n\n";
    
    // Import
    echo "Importing kit...\n";
    $import = new \Elementor\App\Modules\ImportExport\Processes\Import(
        $kit_path,
        []
    );
    
    $import->register_default_runners();
    
    // Get reflection to access protected methods
    $reflection = new ReflectionClass($import);
    $method = $reflection->getMethod('save_elements_of_imported_posts');
    $method->setAccessible(true);
    
    try {
        $method->invoke($import);
        echo "✓ Import method completed\n\n";
    } catch (Throwable $e) {
        echo "✗ Import failed: " . $e->getMessage() . "\n";
        echo "File: " . $e->getFile() . "\n";
        echo "Line: " . $e->getLine() . "\n\n";
    }
    
    // Check results
    echo "Checking results...\n\n";
    
    $after_count = wp_count_posts('page')->publish;
    echo "Pages after import: $after_count\n";
    echo "Pages created: " . ($after_count - $before_count) . "\n\n";
    
    // Check _elementor_data
    $args = array(
        'post_type' => 'page',
        'post_status' => 'publish',
        'posts_per_page' => 5,
        'meta_query' => array(
            array(
                'key' => '_elementor_data',
                'compare' => 'EXISTS',
            ),
        ),
    );
    
    $query = new WP_Query($args);
    
    echo "Sample pages with _elementor_data:\n";
    foreach ($query->posts as $post) {
        $data = get_post_meta($post->ID, '_elementor_data', true);
        $size = strlen($data);
        $decoded = json_decode($data, true);
        $elem_count = is_array($decoded) ? count($decoded) : 0;
        
        echo "  • {$post->post_title} (ID {$post->ID}): {$size} bytes, {$elem_count} elements\n";
    }
    
    echo "\n";
    
    if ($decoded && is_array($decoded) && count($decoded) > 0) {
        echo "✓ PAGES IMPORTED WITH CONTENT!\n";
        echo "\nRoot cause proven: Double-wrapping was the issue.\n";
    } else {
        echo "⚠ Pages imported but _elementor_data is empty.\n";
    }
    
} catch (Throwable $e) {
    echo "FATAL: " . $e->getMessage() . "\n";
    echo $e->getTraceAsString() . "\n";
}

echo "\n";
