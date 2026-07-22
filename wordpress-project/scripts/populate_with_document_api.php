#!/usr/bin/env php
<?php
/**
 * POPULATE PAGES USING ELEMENTOR DOCUMENT API
 * 
 * This uses Elementor's proper Document API to create page content,
 * ensuring it's formatted correctly for export/import cycles.
 */

if ( ! class_exists( '\Elementor\Plugin' ) ) {
    die( "ERROR: Elementor not loaded\n" );
}

use Elementor\Plugin as ElementorPlugin;
use Elementor\Core\Documents_Manager;

echo "=== POPULATING PAGES WITH ELEMENTOR DOCUMENT API ===\n\n";

$main_pages = [
    5 => ['title' => 'Home', 'type' => 'home'],
    7 => ['title' => 'Products', 'type' => 'products'],
    8 => ['title' => 'Services', 'type' => 'services'],
    9 => ['title' => 'Industries', 'type' => 'industries'],
    6 => ['title' => 'Resources', 'type' => 'resources'],
    10 => ['title' => 'About Us', 'type' => 'about'],
    11 => ['title' => 'Contact', 'type' => 'contact'],
    12 => ['title' => 'Case Studies', 'type' => 'cases'],
];

foreach ( $main_pages as $page_id => $page_info ) {
    try {
        // Get the page document object
        $document = ElementorPlugin::instance()->documents->get( $page_id );
        
        if ( ! $document ) {
            echo "✗ Cannot load document for page $page_id\n";
            continue;
        }

        // Build elements using Elementor's structure
        $elements = build_page_elements( $page_info['type'] );

        // Set the document elements
        $document->set_elements_data( $elements );

        // Save the document (this triggers all proper hooks)
        $document->save();

        echo "✓ Updated page {$page_id} ({$page_info['title']})\n";

    } catch ( Exception $e ) {
        echo "✗ Error updating page $page_id: " . $e->getMessage() . "\n";
    }
}

// Also update child pages
$child_pages = get_posts( [
    'post_type' => 'page',
    'post_parent__not_in' => [ 0 ],
    'numberposts' => -1,
] );

echo "\n✓ Pages populated using Elementor Document API\n";

function build_page_elements( $page_type ) {
    // Build simple but valid Elementor structure
    $hero = [
        'id' => uniqid( 'container_' ),
        'elType' => 'container',
        'settings' => [
            'background_color' => '#f7f7f7',
            'padding' => '60px 20px',
            'content_width' => 'boxed',
            'gap' => 'default',
        ],
        'elements' => [
            [
                'id' => uniqid( 'heading_' ),
                'elType' => 'widget',
                'widgetType' => 'heading',
                'settings' => [
                    'title' => 'TShirtSwiss',
                    'header_size' => 'h1',
                    'title_color' => '#111',
                    'typography_typography' => 'custom',
                    'typography_font_size' => [ 'size' => '48', 'unit' => 'px' ],
                    'alignment' => 'center',
                ],
                'elements' => [],
            ],
            [
                'id' => uniqid( 'text_' ),
                'elType' => 'widget',
                'widgetType' => 'text-editor',
                'settings' => [
                    'editor' => '<p>Premium apparel manufacturing and customization</p>',
                    'editor_color' => '#666',
                    'typography_typography' => 'custom',
                    'typography_font_size' => [ 'size' => '16', 'unit' => 'px' ],
                    'alignment' => 'center',
                ],
                'elements' => [],
            ],
        ],
    ];

    return [ $hero ];
}
