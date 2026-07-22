#!/usr/bin/env php
<?php
/**
 * Populate TShirtSwiss Pages with Elementor Content
 * 
 * This script creates page structures and populates them with Elementor sections,
 * columns, and widgets using Elementor's native document and element APIs.
 * No manual JSON writing - all through Elementor's proper object lifecycle.
 * 
 * Usage: wp eval-file populate-pages-with-content.php --allow-root
 */

namespace TShirtSwiss\PageContent;

if ( ! class_exists( '\Elementor\Plugin' ) ) {
    die( "ERROR: Elementor not loaded\n" );
}

use Elementor\Plugin;
use Elementor\TemplateLibrary\Documents\Page as PageDocument;

class ContentPopulator {
    private $admin_user = 1;

    public function __construct() {
        if ( ! is_user_logged_in() ) {
            wp_set_current_user( $this->admin_user );
        }
    }

    /**
     * Create a section element
     */
    private function create_section( $settings = [] ) {
        return array_merge( [
            'id'           => wp_generate_password( 6, false ),
            'elType'       => 'section',
            'elements'     => [],
            'settings'     => $settings,
            'widgetType'   => '',
            'isInner'      => false,
        ], $settings );
    }

    /**
     * Create a column element
     */
    private function create_column( $width = 100, $elements = [] ) {
        return [
            'id'           => wp_generate_password( 6, false ),
            'elType'       => 'column',
            'elements'     => $elements,
            'settings'     => [
                '_column_size'         => $width,
                'background_background' => '',
            ],
        ];
    }

    /**
     * Create a heading widget
     */
    private function create_heading( $text, $level = 'h1', $color = '#111' ) {
        return [
            'id'        => wp_generate_password( 6, false ),
            'elType'    => 'widget',
            'widgetType' => 'heading',
            'settings'  => [
                'title'     => $text,
                'header_size' => $level,
                'text_color' => $color,
                'typography_typography' => 'custom',
            ],
        ];
    }

    /**
     * Create a paragraph widget
     */
    private function create_paragraph( $text ) {
        return [
            'id'        => wp_generate_password( 6, false ),
            'elType'    => 'widget',
            'widgetType' => 'text-editor',
            'settings'  => [
                'editor' => $text,
            ],
        ];
    }

    /**
     * Create a button widget
     */
    private function create_button( $text, $url = '#', $style = 'primary' ) {
        return [
            'id'        => wp_generate_password( 6, false ),
            'elType'    => 'widget',
            'widgetType' => 'button',
            'settings'  => [
                'text'           => $text,
                'link'           => [ 'url' => $url ],
                'button_type'    => 'primary',
            ],
        ];
    }

    /**
     * Create a spacer widget
     */
    private function create_spacer( $height = 30 ) {
        return [
            'id'        => wp_generate_password( 6, false ),
            'elType'    => 'widget',
            'widgetType' => 'spacer',
            'settings'  => [
                'space' => [ 'size' => $height ],
            ],
        ];
    }

    /**
     * Get Home page structure
     */
    private function get_home_page_elements() {
        $section_1_col = $this->create_column( 100, [
            $this->create_heading( 'Swiss-Managed Apparel Manufacturing', 'h1' ),
            $this->create_paragraph( '<p><span style="font-size: 24px; font-weight: bold;">For Businesses That Expect Quality</span></p>' ),
            $this->create_paragraph( 'We help Swiss businesses, brands, clubs and organisations manufacture premium custom apparel through a fully managed production process in Thailand.' ),
            $this->create_spacer( 20 ),
            $this->create_button( 'Request a Quote', '/request-a-quote/', 'primary' ),
            $this->create_button( 'Our Production Process', '/production/', 'secondary' ),
        ] );

        return [
            array_merge( $this->create_section(), [
                'elements' => [
                    array_merge( $this->create_column( 100 ), [
                        'elements' => [
                            $this->create_heading( 'Swiss-Managed Apparel Manufacturing', 'h1' ),
                            $this->create_paragraph( '<strong>For Businesses That Expect Quality</strong>' ),
                            $this->create_paragraph( 'We help Swiss businesses manufacture premium custom apparel through a fully managed production process in Thailand.' ),
                            $this->create_spacer( 20 ),
                        ],
                    ] ),
                ],
            ] ),
        ];
    }

    /**
     * Get Products index page elements
     */
    private function get_products_index_elements() {
        return [
            array_merge( $this->create_section(), [
                'elements' => [
                    array_merge( $this->create_column( 100 ), [
                        'elements' => [
                            $this->create_heading( 'Products', 'h1' ),
                            $this->create_paragraph( 'Browse our complete range of custom apparel and manufacturing solutions.' ),
                            $this->create_spacer( 30 ),
                        ],
                    ] ),
                ],
            ] ),
        ];
    }

    /**
     * Get Industries index page elements
     */
    private function get_industries_index_elements() {
        return [
            array_merge( $this->create_section(), [
                'elements' => [
                    array_merge( $this->create_column( 100 ), [
                        'elements' => [
                            $this->create_heading( 'Industries We Serve', 'h1' ),
                            $this->create_paragraph( 'Every industry has different requirements for branded apparel.' ),
                            $this->create_spacer( 30 ),
                        ],
                    ] ),
                ],
            ] ),
        ];
    }

    /**
     * Get Services index page elements
     */
    private function get_services_index_elements() {
        return [
            array_merge( $this->create_section(), [
                'elements' => [
                    array_merge( $this->create_column( 100 ), [
                        'elements' => [
                            $this->create_heading( 'Services', 'h1' ),
                            $this->create_paragraph( 'Comprehensive apparel manufacturing and decoration services.' ),
                            $this->create_spacer( 30 ),
                        ],
                    ] ),
                ],
            ] ),
        ];
    }

    /**
     * Populate a page with Elementor content
     */
    public function populate_page( $page_id, $page_type ) {
        $document = Plugin::$instance->documents->get( $page_id );

        if ( ! $document ) {
            WP_CLI::warning( "Could not get document for page {$page_id}" );
            return false;
        }

        // Get elements based on page type
        $elements = [];
        switch ( $page_type ) {
            case 'home':
                $elements = $this->get_home_page_elements();
                break;
            case 'products_index':
                $elements = $this->get_products_index_elements();
                break;
            case 'industries_index':
                $elements = $this->get_industries_index_elements();
                break;
            case 'services_index':
                $elements = $this->get_services_index_elements();
                break;
            default:
                // Default: simple heading + paragraph
                $elements = [
                    array_merge( $this->create_section(), [
                        'elements' => [
                            array_merge( $this->create_column( 100 ), [
                                'elements' => [
                                    $this->create_heading( get_the_title( $page_id ), 'h1' ),
                                    $this->create_paragraph( 'Page content goes here.' ),
                                ],
                            ] ),
                        ],
                    ] ),
                ];
        }

        // Save elements to document
        try {
            $document->save( $elements );
            WP_CLI::success( "Populated page {$page_id} with Elementor content" );
            return true;
        } catch ( \Exception $e ) {
            WP_CLI::warning( "Error populating page {$page_id}: " . $e->getMessage() );
            return false;
        }
    }

    /**
     * Run population workflow
     */
    public function run() {
        WP_CLI::line( "\n=== Populating Pages with Elementor Content ===" );
        WP_CLI::line( "" );

        $pages = [
            [ 'slug' => '', 'type' => 'home', 'post_type' => 'page' ],
            [ 'slug' => 'products', 'type' => 'products_index', 'post_type' => 'page' ],
            [ 'slug' => 'industries', 'type' => 'industries_index', 'post_type' => 'page' ],
            [ 'slug' => 'services', 'type' => 'services_index', 'post_type' => 'page' ],
        ];

        $populated = 0;

        foreach ( $pages as $page_info ) {
            $post = get_page_by_path( $page_info['slug'], OBJECT, 'page' );

            if ( ! $post ) {
                WP_CLI::warning( "Page not found: {$page_info['slug']}" );
                continue;
            }

            if ( $this->populate_page( $post->ID, $page_info['type'] ) ) {
                $populated++;
            }
        }

        WP_CLI::success( "✓ Populated {$populated} pages" );
    }
}

$populator = new ContentPopulator();
$populator->run();
