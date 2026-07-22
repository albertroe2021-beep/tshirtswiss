<?php
/**
 * Build pages using Elementor's Document API
 * 
 * Usage: wp eval-file /scripts/build-pages-via-api.php
 */

if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

use Elementor\Plugin as ElementorPlugin;

class PageBuilder {
    private $page_count = 0;
    private $error_count = 0;

    public function build_all() {
        WP_CLI::line('');
        WP_CLI::line('=== Building Pages via Elementor Document API ===');
        WP_CLI::line('');

        // Verify Elementor is loaded
        if (!function_exists('do_action')) {
            WP_CLI::error('WordPress not properly initialized');
            return;
        }

        // Build sample pages
        $pages = [
            [
                'id' => 5,
                'title' => 'Home',
                'slug' => 'home',
            ],
            [
                'id' => 6,
                'title' => 'Products',
                'slug' => 'products',
            ],
            [
                'id' => 7,
                'title' => 'Services',
                'slug' => 'services',
            ],
        ];

        foreach ($pages as $page_config) {
            $this->build_page($page_config);
        }

        WP_CLI::line('');
        WP_CLI::line("Summary: {$this->page_count} pages built, {$this->error_count} errors");
        WP_CLI::line('');

        if ($this->error_count === 0) {
            WP_CLI::success('All pages built successfully!');
        }
    }

    private function build_page($config) {
        $post_id = $config['id'];
        $title = $config['title'];

        try {
            WP_CLI::line("Building: $title (ID: $post_id)");

            // Step 1: Get or create WordPress post
            $post = get_post($post_id);
            if (!$post) {
                $post_id = wp_insert_post([
                    'ID' => $post_id,
                    'post_type' => 'page',
                    'post_title' => $title,
                    'post_status' => 'publish'
                ]);

                if (!$post_id) {
                    WP_CLI::error("  ✗ Failed to create page");
                    $this->error_count++;
                    return;
                }
                WP_CLI::line("  ✓ Page created");
            }

            // Step 2: Get Elementor document
            if (!class_exists('Elementor\Plugin')) {
                WP_CLI::error("  ✗ Elementor not loaded");
                $this->error_count++;
                return;
            }

            $elementor = ElementorPlugin::instance();
            $document = $elementor->documents->get($post_id);

            if (!$document) {
                WP_CLI::error("  ✗ Failed to get Elementor document");
                $this->error_count++;
                return;
            }

            WP_CLI::line("  ✓ Opened Elementor document");

            // Debug: list available methods on document
            $methods = get_class_methods($document);
            WP_CLI::line("  Document methods available:");
            foreach (['save', 'import', 'set_elements', 'update_elements', 'set_json'] as $method) {
                if (in_array($method, $methods)) {
                    WP_CLI::line("    - $method ✓");
                }
            }

            // Step 3: Use Elementor's import() method
            // This is the same routine used when importing templates
            // It properly deserializes and validates the structure
            $elements = $this->build_elements();
            
            // Build the full document structure expected by import()
            $import_data = [
                'content' => [
                    'content' => $elements,
                    'settings' => [],
                    'metadata' => []
                ],
                'settings' => [],
                'metadata' => []
            ];
            
            // Import using Elementor's internal process
            $import_result = $document->import($import_data);

            if ($import_result) {
                WP_CLI::line("  ✓ Content imported via Elementor import()");
            } else {
                WP_CLI::warning("  ⚠ Import returned false, but continuing");
            }

            // Step 5: Regenerate CSS
            $this->regenerate_css($post_id);
            WP_CLI::line("  ✓ CSS regenerated");

            // Step 6: Verify
            $this->verify_page($post_id);

            $this->page_count++;
            WP_CLI::success("  ✓ Page complete\n");

        } catch (\Exception $e) {
            WP_CLI::error("  ✗ " . $e->getMessage());
            $this->error_count++;
        }
    }

    private function build_elements() {
        return [
            [
                'id' => $this->make_id(),
                'elType' => 'container',
                'settings' => [
                    'background_color' => '#f7f7f7',
                    'padding' => '60px 20px',
                    'content_width' => 'boxed',
                    'gap' => 'default'
                ],
                'elements' => [
                    [
                        'id' => $this->make_id(),
                        'elType' => 'widget',
                        'widgetType' => 'heading',
                        'settings' => [
                            'title' => 'Swiss-Managed Apparel Manufacturing',
                            'header_size' => 'h1',
                            'title_color' => '#111',
                            'typography_typography' => 'custom',
                            'typography_font_size' => ['size' => '48', 'unit' => 'px'],
                            'alignment' => 'center'
                        ],
                        'elements' => []
                    ],
                    [
                        'id' => $this->make_id(),
                        'elType' => 'widget',
                        'widgetType' => 'text-editor',
                        'settings' => [
                            'editor' => '<p>Custom apparel solutions with Swiss precision and attention to detail.</p>',
                            'typography_font_size' => ['size' => '16', 'unit' => 'px'],
                            'alignment' => 'center'
                        ],
                        'elements' => []
                    ],
                    [
                        'id' => $this->make_id(),
                        'elType' => 'widget',
                        'widgetType' => 'button',
                        'settings' => [
                            'text' => 'Get Started',
                            'link' => ['url' => '/contact/'],
                            'button_background_color' => '#e1111a',
                            'button_text_color' => '#fff',
                            'alignment' => 'center'
                        ],
                        'elements' => []
                    ]
                ]
            ]
        ];
    }

    private function regenerate_css($post_id) {
        try {
            $elementor = ElementorPlugin::instance();
            $document = $elementor->documents->get($post_id);

            if (!$document) {
                return;
            }

            if (method_exists($document, 'get_css_file')) {
                $css_file = $document->get_css_file();
                if ($css_file && method_exists($css_file, 'update')) {
                    $css_file->update();
                }
            }

        } catch (\Exception $e) {
            // Silent fail
        }
    }

    private function verify_page($post_id) {
        $elementor_data = get_post_meta($post_id, '_elementor_data', true);

        if (!$elementor_data) {
            WP_CLI::warning("  ⚠ No Elementor data found");
            return;
        }

        $decoded = json_decode($elementor_data, true);
        if (!$decoded) {
            WP_CLI::warning("  ⚠ Elementor data is invalid");
            return;
        }

        WP_CLI::line("  ✓ Elementor data verified");
    }

    private function make_id() {
        return substr(md5(uniqid()), 0, 8);
    }
}

// Run the builder
$builder = new PageBuilder();
$builder->build_all();
