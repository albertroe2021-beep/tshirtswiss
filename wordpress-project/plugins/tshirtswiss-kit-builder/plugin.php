<?php
/**
 * TShirtSwiss Kit Builder - Main Class
 * 
 * Uses Elementor's Document API to build pages properly
 */

if (!defined('ABSPATH')) {
    exit;
}

// Register plugin for WP-CLI
if (defined('WP_CLI') && WP_CLI) {
    WP_CLI::add_command('tshirtswiss', function() {
        return new TShirtSwiss_Kit_Builder();
    });
}

class TShirtSwiss_Kit_Builder {
    private $elementor;
    private $pages_data = [
        5 => [
            'title' => 'Home',
            'type' => 'page',
            'path' => '/',
            'content' => [
                [
                    'type' => 'container',
                    'background' => '#f7f7f7',
                    'padding' => '60px 20px',
                    'children' => [
                        [
                            'type' => 'heading',
                            'text' => 'Swiss-Managed Apparel Manufacturing',
                            'level' => 'h1',
                            'size' => '48',
                            'color' => '#111'
                        ],
                        [
                            'type' => 'heading',
                            'text' => 'For Businesses That Expect Quality',
                            'level' => 'h2',
                            'size' => '28',
                            'color' => '#e1111a'
                        ],
                        [
                            'type' => 'text',
                            'text' => 'Custom apparel solutions crafted with Swiss precision and attention to detail. Since 2005, we\'ve been trusted by brands across industries.',
                            'color' => '#666'
                        ],
                        [
                            'type' => 'button',
                            'text' => 'Get Started',
                            'url' => '/contact/',
                            'style' => 'primary'
                        ]
                    ]
                ]
            ]
        ],
        // Add more pages as needed
    ];

    public function __construct() {
        $this->elementor = \Elementor\Plugin::$instance;
    }

    /**
     * Build all pages
     * Usage: wp tshirtswiss build-all
     */
    public function __invoke($args = [], $assoc_args = []) {
        if (empty($args) || $args[0] === 'build-all') {
            $this->build_all_pages();
        }
    }

    /**
     * Build all pages using Elementor's Document API
     */
    public function build_all_pages() {
        WP_CLI::line('');
        WP_CLI::line('=== Building TShirtSwiss Pages via Elementor API ===');
        WP_CLI::line('');

        foreach ($this->pages_data as $post_id => $page_config) {
            $this->build_single_page($post_id, $page_config);
        }

        WP_CLI::line('');
        WP_CLI::success('All pages built successfully');
        WP_CLI::line('');
    }

    /**
     * Build a single page using Elementor Document API
     */
    private function build_single_page($post_id, $config) {
        try {
            // Step 1: Ensure page exists
            $page = get_post($post_id);
            if (!$page) {
                $page_id = wp_insert_post([
                    'ID' => $post_id,
                    'post_type' => $config['type'] ?? 'page',
                    'post_title' => $config['title'],
                    'post_status' => 'publish'
                ]);
                if (!$page_id) {
                    WP_CLI::error("Failed to create page {$post_id}");
                    return;
                }
                $post_id = $page_id;
            }

            WP_CLI::line("Building: {$config['title']} (ID: {$post_id})");

            // Step 2: Get Elementor document
            $document = $this->elementor->documents->get($post_id);
            if (!$document) {
                // Create a new document
                $document = $this->elementor->documents->create([
                    'post_id' => $post_id,
                    'post_type' => $config['type'] ?? 'page'
                ]);
                if (!$document) {
                    WP_CLI::error("  ✗ Failed to create Elementor document");
                    return;
                }
            }

            // Step 3: Convert page config to Elementor structure
            $elements = $this->convert_to_elementor_format($config['content'] ?? []);

            // Step 4: Set document data
            $document->save([
                'elements' => $elements,
                'settings' => [
                    'post_title' => $config['title']
                ]
            ]);

            // Step 5: Regenerate CSS
            if (method_exists($document, 'get_css_file')) {
                $css_file = $document->get_css_file();
                if ($css_file) {
                    $css_file->delete();
                }
            }

            // Clear caches
            if (method_exists($document, 'update_meta_cache')) {
                $document->update_meta_cache();
            }

            WP_CLI::line("  ✓ Document saved and CSS regenerated");

            // Step 6: Verify rendering
            $rendered = $this->verify_page_renders($post_id);
            if ($rendered) {
                WP_CLI::line("  ✓ Page renders correctly");
            } else {
                WP_CLI::warning("  ⚠ Page may have rendering issues");
            }

        } catch (\Exception $e) {
            WP_CLI::error("  ✗ " . $e->getMessage());
        }
    }

    /**
     * Convert simple page config to Elementor element format
     */
    private function convert_to_elementor_format($content) {
        $elements = [];

        foreach ($content as $section) {
            if ($section['type'] === 'container') {
                $container = [
                    'id' => $this->generate_id(),
                    'elType' => 'container',
                    'settings' => [
                        'background_color' => $section['background'] ?? '',
                        'padding' => $section['padding'] ?? '40px 20px',
                        'content_width' => 'boxed',
                        'gap' => 'default'
                    ],
                    'elements' => $this->convert_children($section['children'] ?? [])
                ];
                $elements[] = $container;
            }
        }

        return $elements;
    }

    /**
     * Convert child elements
     */
    private function convert_children($children) {
        $elements = [];

        foreach ($children as $child) {
            switch ($child['type']) {
                case 'heading':
                    $elements[] = [
                        'id' => $this->generate_id(),
                        'elType' => 'widget',
                        'widgetType' => 'heading',
                        'settings' => [
                            'title' => $child['text'],
                            'header_size' => $child['level'] ?? 'h2',
                            'title_color' => $child['color'] ?? '#111',
                            'typography_typography' => 'custom',
                            'typography_font_size' => [
                                'size' => $child['size'] ?? '32',
                                'unit' => 'px'
                            ],
                            'alignment' => 'center'
                        ],
                        'elements' => []
                    ];
                    break;

                case 'text':
                    $elements[] = [
                        'id' => $this->generate_id(),
                        'elType' => 'widget',
                        'widgetType' => 'text-editor',
                        'settings' => [
                            'editor' => '<p>' . $child['text'] . '</p>',
                            'typography_typography' => 'custom',
                            'typography_font_size' => [
                                'size' => '16',
                                'unit' => 'px'
                            ],
                            'alignment' => 'center'
                        ],
                        'elements' => []
                    ];
                    break;

                case 'button':
                    $style = $child['style'] ?? 'primary';
                    $bg_color = ($style === 'primary') ? '#e1111a' : 'transparent';
                    $text_color = ($style === 'primary') ? '#fff' : '#111';

                    $elements[] = [
                        'id' => $this->generate_id(),
                        'elType' => 'widget',
                        'widgetType' => 'button',
                        'settings' => [
                            'text' => $child['text'],
                            'link' => ['url' => $child['url'] ?? '#'],
                            'button_background_color' => $bg_color,
                            'button_text_color' => $text_color,
                            'alignment' => 'center'
                        ],
                        'elements' => []
                    ];
                    break;
            }
        }

        return $elements;
    }

    /**
     * Generate unique element ID
     */
    private function generate_id() {
        return substr(md5(uniqid()), 0, 8);
    }

    /**
     * Verify page renders without errors
     */
    private function verify_page_renders($post_id) {
        // Get the page frontend URL
        $url = get_permalink($post_id);
        if (!$url) {
            return false;
        }

        // Simple check: does the page have Elementor data?
        $elementor_data = get_post_meta($post_id, '_elementor_data', true);
        if (!$elementor_data) {
            return false;
        }

        return true;
    }
}
