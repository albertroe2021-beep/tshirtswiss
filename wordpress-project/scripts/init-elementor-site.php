#!/usr/bin/env php
<?php
/**
 * TShirtSwiss Elementor Site - Complete Initialization
 * 
 * This script handles the complete workflow:
 * 1. Ensures WordPress + Elementor environment is ready
 * 2. Creates all page structures (main pages + representatives)
 * 3. Populates them with Elementor content using native APIs
 * 4. Marks pages ready for export
 * 
 * Execution: wp eval-file /scripts/init-elementor-site.php --allow-root
 */

namespace TShirtSwiss;

use Elementor\Plugin;

if ( ! class_exists( '\Elementor\Plugin' ) ) {
    WP_CLI::error( 'Elementor plugin not found' );
}

if ( ! is_user_logged_in() ) {
    wp_set_current_user( 1 );
}

class ElementorSiteBuilder {
    private $pages_created = 0;
    private $pages_populated = 0;
    private $theme = '';

    public function __construct() {
        $this->theme = wp_get_theme()->get_stylesheet();
        WP_CLI::log( "\n" . str_repeat( "=", 60 ) );
        WP_CLI::log( "TShirtSwiss Elementor Site Builder" );
        WP_CLI::log( str_repeat( "=", 60 ) );
        WP_CLI::log( "WordPress: " . get_bloginfo( 'version' ) );
        WP_CLI::log( "Elementor: " . Plugin::VERSION );
        WP_CLI::log( "Theme: " . $this->theme );
        WP_CLI::log( "" );
    }

    /**
     * Create a page with Elementor support
     */
    private function create_page( $title, $slug, $type = 'page' ) {
        // Check if exists
        $existing = get_page_by_path( $slug, OBJECT, 'page' );
        if ( $existing ) {
            return $existing->ID;
        }

        // Create
        $page_id = wp_insert_post( [
            'post_title'   => $title,
            'post_name'    => $slug,
            'post_type'    => 'page',
            'post_status'  => 'publish',
            'post_content' => '',
            'post_author'  => 1,
            'comment_status' => 'closed',
        ] );

        if ( is_wp_error( $page_id ) ) {
            return false;
        }

        // Enable Elementor
        update_post_meta( $page_id, '_elementor_edit_mode', 'builder' );
        
        $this->pages_created++;
        return $page_id;
    }

    /**
     * Populate page with basic Elementor structure
     */
    private function add_basic_section( $page_id, $title, $description = '' ) {
        $document = Plugin::$instance->documents->get( $page_id );
        if ( ! $document ) {
            return false;
        }

        // Create basic structure using Elementor element structures
        $elements = [
            [
                'id'        => substr( md5( $page_id . 'section1' ), 0, 6 ),
                'elType'    => 'section',
                'settings'  => [
                    'background_background'  => '',
                    'padding'               => [ 'unit' => 'px', 'top' => 40, 'bottom' => 40 ],
                ],
                'elements'  => [
                    [
                        'id'       => substr( md5( $page_id . 'col1' ), 0, 6 ),
                        'elType'   => 'column',
                        'settings' => [
                            '_column_size' => 100,
                        ],
                        'elements' => [
                            // Heading
                            [
                                'id'         => substr( md5( $page_id . 'heading' ), 0, 6 ),
                                'elType'     => 'widget',
                                'widgetType' => 'heading',
                                'settings'   => [
                                    'title'           => $title,
                                    'header_size'     => 'h1',
                                    'align'           => 'center',
                                    'text_color'      => '#111111',
                                    'font_size'       => [ 'unit' => 'px', 'size' => 48 ],
                                    'font_weight'     => '700',
                                    'margin'          => [ 'unit' => 'px', 'bottom' => 20 ],
                                ],
                            ],
                            // Description if provided
                            $description ? [
                                'id'         => substr( md5( $page_id . 'desc' ), 0, 6 ),
                                'elType'     => 'widget',
                                'widgetType' => 'text-editor',
                                'settings'   => [
                                    'editor' => '<p>' . esc_html( $description ) . '</p>',
                                    'text_align' => 'center',
                                    'text_color' => '#555555',
                                    'font_size'  => [ 'unit' => 'px', 'size' => 16 ],
                                    'line_height' => [ 'unit' => 'em', 'size' => 1.6 ],
                                ],
                            ] : null,
                        ],
                    ],
                ],
            ],
        ];

        // Remove null elements
        $elements[0]['elements'][0]['elements'] = array_filter( $elements[0]['elements'][0]['elements'] );

        // Save to document
        try {
            $document->save( $elements );
            $this->pages_populated++;
            return true;
        } catch ( Exception $e ) {
            WP_CLI::warning( "Error saving document: " . $e->getMessage() );
            return false;
        }
    }

    /**
     * Get pages structure for Option B
     */
    private function get_pages_config() {
        return [
            // MAIN PAGES (12)
            [ 'title' => 'Home', 'slug' => '', 'desc' => 'Swiss-managed apparel manufacturing' ],
            [ 'title' => 'Products', 'slug' => 'products', 'desc' => 'Browse our complete range' ],
            [ 'title' => 'Industries', 'slug' => 'industries', 'desc' => 'Industries we serve' ],
            [ 'title' => 'Services', 'slug' => 'services', 'desc' => 'Manufacturing services' ],
            [ 'title' => 'About Us', 'slug' => 'about-us', 'desc' => 'Learn about TShirtSwiss' ],
            [ 'title' => 'Production', 'slug' => 'production', 'desc' => 'Our production process' ],
            [ 'title' => 'Case Studies', 'slug' => 'case-studies', 'desc' => 'Client success stories' ],
            [ 'title' => 'Resources', 'slug' => 'resources', 'desc' => 'Blog, FAQ and guides' ],
            [ 'title' => 'Blog', 'slug' => 'blog', 'desc' => 'Latest articles' ],
            [ 'title' => 'FAQ', 'slug' => 'faq', 'desc' => 'Frequently asked questions' ],
            [ 'title' => 'Request a Quote', 'slug' => 'request-a-quote', 'desc' => 'Get a custom quote' ],
            [ 'title' => 'Contact', 'slug' => 'contact', 'desc' => 'Get in touch' ],

            // PRODUCT PAGES (3 representatives)
            [ 'title' => 'Custom T-Shirts', 'slug' => 'products/custom-t-shirts', 'desc' => 'Premium custom t-shirts for any brand' ],
            [ 'title' => 'Corporate Apparel', 'slug' => 'products/corporate-apparel', 'desc' => 'Professional uniforms and branded clothing' ],
            [ 'title' => 'Sportswear', 'slug' => 'products/sportswear', 'desc' => 'Performance apparel for teams and athletes' ],

            // INDUSTRY PAGES (3 representatives)
            [ 'title' => 'Construction & Trades', 'slug' => 'industries/construction-trades', 'desc' => 'Durable workwear for construction' ],
            [ 'title' => 'Healthcare', 'slug' => 'industries/healthcare', 'desc' => 'Professional healthcare uniforms' ],
            [ 'title' => 'Sports & Fitness', 'slug' => 'industries/sports-fitness', 'desc' => 'Sportswear for clubs and gyms' ],

            // SERVICE PAGES (3 representatives)
            [ 'title' => 'Screen Printing', 'slug' => 'services/screen-printing', 'desc' => 'Professional screen printing service' ],
            [ 'title' => 'Embroidery', 'slug' => 'services/embroidery', 'desc' => 'Precision embroidery and thread work' ],
            [ 'title' => 'Quality Control', 'slug' => 'services/quality-control', 'desc' => 'Rigorous quality assurance' ],
        ];
    }

    /**
     * Run the initialization
     */
    public function run() {
        WP_CLI::log( "PHASE 1: Creating Pages" );
        WP_CLI::log( str_repeat( "-", 60 ) );

        $pages_config = $this->get_pages_config();
        $page_ids = [];

        foreach ( $pages_config as $page ) {
            $page_id = $this->create_page( $page['title'], $page['slug'] );
            if ( $page_id ) {
                $page_ids[ $page['slug'] ] = $page_id;
                WP_CLI::success( "✓ {$page['title']} (ID: {$page_id})" );
            } else {
                WP_CLI::warning( "✗ Failed: {$page['title']}" );
            }
        }

        WP_CLI::log( "" );
        WP_CLI::log( "PHASE 2: Populating with Content" );
        WP_CLI::log( str_repeat( "-", 60 ) );

        foreach ( $pages_config as $page ) {
            if ( isset( $page_ids[ $page['slug'] ] ) ) {
                $page_id = $page_ids[ $page['slug'] ];
                if ( $this->add_basic_section( $page_id, $page['title'], $page['desc'] ?? '' ) ) {
                    WP_CLI::success( "✓ Populated: {$page['title']}" );
                } else {
                    WP_CLI::warning( "✗ Failed to populate: {$page['title']}" );
                }
            }
        }

        WP_CLI::log( "" );
        WP_CLI::log( str_repeat( "=", 60 ) );
        WP_CLI::success( "✓ Site Building Complete!" );
        WP_CLI::log( "" );
        WP_CLI::log( "Summary:" );
        WP_CLI::log( "  Pages Created: {$this->pages_created}" );
        WP_CLI::log( "  Pages Populated: {$this->pages_populated}" );
        WP_CLI::log( "" );
        WP_CLI::log( "Next: Export Website Kit via Elementor" );
        WP_CLI::log( str_repeat( "=", 60 ) );
        WP_CLI::log( "" );
    }
}

$builder = new ElementorSiteBuilder();
$builder->run();
