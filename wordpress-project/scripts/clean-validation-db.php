<?php
if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

global $wpdb;

echo "Deleting existing pages and Elementor data...\n";

// Delete all pages (except home/sample)
$pages = get_posts(['post_type' => 'page', 'numberposts' => -1, 'post_status' => 'any']);
foreach ($pages as $page) {
    if ($page->post_title !== 'Sample Page') {
        wp_delete_post($page->ID, true);
    }
}

echo "Database cleaned.\n";
