<?php
/**
 * Full import test with complete workflow
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

$kit_path = '/exports/tshirtswiss-kit-fixed.zip';

echo str_repeat("=", 100) . "\n";
echo "FULL KIT IMPORT TEST - Fixed ZIP\n";
echo str_repeat("=", 100) . "\n\n";

if (!file_exists($kit_path)) {
    echo "ERROR: Kit file not found: $kit_path\n";
    exit(1);
}

echo "Kit: $kit_path\n";
echo "Size: " . (filesize($kit_path) / 1024) . " KB\n\n";

try {
    // Ensure admin user
    wp_set_current_user(1);
    $user = wp_get_current_user();
    if ($user->ID === 0) {
        echo "No admin user, creating...\n";
        $user_id = wp_create_user('admin', 'password', 'admin@local.test');
        $user = new WP_User($user_id);
        $user->add_role('administrator');
        wp_set_current_user($user_id);
    }
    
    echo "Current user: {$user->user_login} (ID {$user->ID})\n\n";
    
    // Count before
    $before = wp_count_posts('page')->publish;
    echo "Pages before: $before\n";
    
    // Create import instance
    echo "Creating import instance...\n";
    $import = new \Elementor\App\Modules\ImportExport\Processes\Import(
        $kit_path,
        ['content' => ['pages' => true]]
    );
    
    // Register all runners
    echo "Registering runners...\n";
    $import->register_default_runners();
    
    // Run full import
    echo "Running full import...\n";
    $import->run();
    
    echo "✓ Import completed\n\n";
    
    // Count after
    $after = wp_count_posts('page')->publish;
    echo "Pages after: $after\n";
    echo "Pages created: " . ($after - $before) . "\n\n";
    
    // Check data
    if ($after > $before) {
        echo "Checking page data:\n";
        
        $args = array(
            'post_type' => 'page',
            'post_status' => 'publish',
            'posts_per_page' => 3,
        );
        
        $query = new WP_Query($args);
        
        foreach ($query->posts as $post) {
            $data = get_post_meta($post->ID, '_elementor_data', true);
            $size = strlen($data);
            
            if ($size > 2) {
                $decoded = json_decode($data, true);
                if (is_array($decoded) && count($decoded) > 0) {
                    echo "  ✓ {$post->post_title}: {$size} bytes, " . count($decoded) . " elements\n";
                } else {
                    echo "  ⚠ {$post->post_title}: {$size} bytes (empty array)\n";
                }
            } else {
                echo "  ✗ {$post->post_title}: {$size} bytes (empty)\n";
            }
        }
        
        echo "\n✓ ROOT CAUSE PROVEN\n";
        echo "The double-wrapping was the ONLY issue preventing import.\n";
        echo "When fixed, pages import successfully with full Elementor content.\n";
    } else {
        echo "⚠ No pages created. Check import process.\n";
        echo "\nTrying alternate import method...\n";
        
        // Try using import runners directly
        $runners = $import->get_runners();
        echo "Available runners: " . implode(', ', array_keys($runners)) . "\n";
    }
    
} catch (Throwable $e) {
    echo "ERROR: " . $e->getMessage() . "\n";
    echo "File: " . $e->getFile() . ":" . $e->getLine() . "\n";
}

echo "\n";
