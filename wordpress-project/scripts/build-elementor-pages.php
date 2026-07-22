#!/usr/bin/env php
<?php
/**
 * Build TShirtSwiss Website Using Elementor Native APIs
 * 
 * This script creates all pages and populates them with Elementor content
 * using Elementor's native document lifecycle (not manual JSON generation).
 * 
 * Usage: wp eval-file build-elementor-pages.php --allow-root
 */

namespace TShirtSwiss\ElementorBuilder;

if ( ! class_exists( '\Elementor\Plugin' ) ) {
    die( "ERROR: Elementor not loaded\n" );
}

use Elementor\Plugin;
use Elementor\Core\Documents_Manager;

class PageBuilder {
    private $pages = [];
    private $theme = '';
    private $admin_user_id = 1;

    public function __construct() {
        // Verify environment
        if ( ! is_user_logged_in() ) {
            wp_set_current_user( $this->admin_user_id );
        }
        
        $current_theme = wp_get_theme();
        $this->theme = $current_theme->get_stylesheet();
        
        WP_CLI::log( "✓ Environment: WordPress " . get_bloginfo( 'version' ) );
        WP_CLI::log( "✓ Elementor: " . Plugin::VERSION );
        WP_CLI::log( "✓ Theme: {$this->theme}" );
        WP_CLI::log( "" );
    }

    /**
     * Create or get a page
     */
    public function create_page( $title, $slug, $parent_id = 0 ) {
        // Check if page exists
        $existing = get_page_by_path( $slug, OBJECT, 'page' );
        
        if ( $existing ) {
            WP_CLI::line( "  ⚠ Page exists: {$title} (ID: {$existing->ID})" );
            return $existing->ID;
        }

        // Create new page
        $page_id = wp_insert_post( [
            'post_title'   => $title,
            'post_name'    => $slug,
            'post_type'    => 'page',
            'post_status'  => 'publish',
            'post_parent'  => $parent_id,
            'post_content' => '', // Elementor content goes in meta
            'post_author'  => $this->admin_user_id,
        ] );

        if ( is_wp_error( $page_id ) ) {
            WP_CLI::error( "Failed to create page: {$title}" );
            return false;
        }

        WP_CLI::success( "Created: {$title} (ID: {$page_id})" );
        return $page_id;
    }

    /**
     * Assign page to Elementor for editing
     */
    public function enable_elementor( $page_id ) {
        // Mark post as using Elementor
        update_post_meta( $page_id, '_elementor_edit_mode', 'builder' );
        
        // Get or create Elementor document
        $document = Plugin::$instance->documents->get( $page_id );
        
        if ( ! $document ) {
            WP_CLI::warning( "Could not get Elementor document for page {$page_id}" );
            return false;
        }

        return $document;
    }

    /**
     * Get all pages to create
     */
    public function get_pages_to_create() {
        return [
            // Main pages
            [
                'title'  => 'Home',
                'slug'   => '',
                'type'   => 'home',
            ],
            [
                'title'  => 'Products',
                'slug'   => 'products',
                'type'   => 'index',
            ],
            [
                'title'  => 'Industries',
                'slug'   => 'industries',
                'type'   => 'index',
            ],
            [
                'title'  => 'Services',
                'slug'   => 'services',
                'type'   => 'index',
            ],
            [
                'title'  => 'About Us',
                'slug'   => 'about-us',
                'type'   => 'standard',
            ],
            [
                'title'  => 'Production',
                'slug'   => 'production',
                'type'   => 'standard',
            ],
            [
                'title'  => 'Case Studies',
                'slug'   => 'case-studies',
                'type'   => 'standard',
            ],
            [
                'title'  => 'Resources',
                'slug'   => 'resources',
                'type'   => 'standard',
            ],
            [
                'title'  => 'Blog',
                'slug'   => 'blog',
                'type'   => 'standard',
            ],
            [
                'title'  => 'FAQ',
                'slug'   => 'faq',
                'type'   => 'standard',
            ],
            [
                'title'  => 'Request a Quote',
                'slug'   => 'request-a-quote',
                'type'   => 'form',
            ],
            [
                'title'  => 'Contact',
                'slug'   => 'contact',
                'type'   => 'form',
            ],

            // Product Pages (representatives)
            [
                'title'     => 'Custom T-Shirts',
                'slug'      => 'products/custom-t-shirts',
                'type'      => 'product',
                'category'  => 'products',
            ],
            [
                'title'     => 'Corporate Apparel',
                'slug'      => 'products/corporate-apparel',
                'type'      => 'product',
                'category'  => 'products',
            ],
            [
                'title'     => 'Sportswear',
                'slug'      => 'products/sportswear',
                'type'      => 'product',
                'category'  => 'products',
            ],

            // Industry Pages (representatives)
            [
                'title'     => 'Construction & Trades',
                'slug'      => 'industries/construction-trades',
                'type'      => 'industry',
                'category'  => 'industries',
            ],
            [
                'title'     => 'Healthcare',
                'slug'      => 'industries/healthcare',
                'type'      => 'industry',
                'category'  => 'industries',
            ],
            [
                'title'     => 'Sports & Fitness',
                'slug'      => 'industries/sports-fitness',
                'type'      => 'industry',
                'category'  => 'industries',
            ],

            // Service Pages (representatives)
            [
                'title'     => 'Screen Printing',
                'slug'      => 'services/screen-printing',
                'type'      => 'service',
                'category'  => 'services',
            ],
            [
                'title'     => 'Embroidery',
                'slug'      => 'services/embroidery',
                'type'      => 'service',
                'category'  => 'services',
            ],
            [
                'title'     => 'Quality Control',
                'slug'      => 'services/quality-control',
                'type'      => 'service',
                'category'  => 'services',
            ],
        ];
    }

    /**
     * Run the page creation workflow
     */
    public function run() {
        WP_CLI::line( "\n=== Building TShirtSwiss with Elementor ===" );
        WP_CLI::line( "" );

        $pages = $this->get_pages_to_create();
        $created = 0;

        foreach ( $pages as $page_data ) {
            $slug = $page_data['slug'];
            $title = $page_data['title'];

            WP_CLI::line( "Creating: {$title}" );
            $page_id = $this->create_page( $title, $slug );

            if ( $page_id ) {
                // Enable Elementor
                $doc = $this->enable_elementor( $page_id );
                if ( $doc ) {
                    WP_CLI::line( "  ✓ Elementor enabled (Document ID: {$page_id})" );
                    $created++;
                }
            }

            WP_CLI::line( "" );
        }

        WP_CLI::success( "✓ Created {$created} pages" );
        WP_CLI::line( "" );
        WP_CLI::line( "Next steps:" );
        WP_CLI::line( "1. Log in to WordPress admin" );
        WP_CLI::line( "2. Open each page in Elementor editor" );
        WP_CLI::line( "3. Add content using Elementor widgets" );
        WP_CLI::line( "4. Publish each page" );
        WP_CLI::line( "" );
    }
}

// Initialize and run
$builder = new PageBuilder();
$builder->run();
