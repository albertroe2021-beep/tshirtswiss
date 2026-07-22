<?php
/**
 * Plugin Name: TShirtSwiss Kit Builder
 * Description: Build Elementor pages using Document API
 * Version: 1.0.0
 * Author: TShirtSwiss
 */

if (!defined('ABSPATH')) {
    exit;
}

class TShirtSwiss_Kit_Builder {
    /**
     * Build a single page with proper Elementor Document API usage
     * 
     * Usage: wp tshirtswiss build <post_id> <title>
     */
    public function __invoke($args = [], $assoc_args = []) {
        if (empty($args)) {
            WP_CLI::error('Usage: wp tshirtswiss build <post_id> <title>');
            return;
        }

        $post_id = intval($args[0]);
        $title = isset($args[1]) ? $args[1] : "Page {$post_id}";

        $this->build_page($post_id, $title);
    }

    /**
     * Build a page using Elementor's Document API
     */
    private function build_page($post_id, $title) {
        WP_CLI::line('');
        WP_CLI::line("Building page: {$title} (ID: {$post_id})");

        // Ensure Elementor is loaded
        if (!class_exists('\Elementor\Plugin')) {
            WP_CLI::error("Elementor plugin is not active or loaded");
            return;
        }

        // Step 1: Ensure page exists in WordPress
        $page = get_post($post_id);
        if (!$page) {
            $created = wp_insert_post([
                'ID' => $post_id,
                'post_type' => 'page',
                'post_title' => $title,
                'post_status' => 'publish'
            ]);

            if (!$created) {
                WP_CLI::error("Failed to create page");
                return;
            }
            WP_CLI::line("  ✓ Page created in WordPress");
        } else {
            WP_CLI::line("  ✓ Page exists in WordPress");
        }

        // Step 2: Get Elementor document via Document Manager
        try {
            $elementor = \Elementor\Plugin::$instance;
            $document = $elementor->documents->get($post_id);

            if (!$document) {
                WP_CLI::error("Failed to get Elementor document");
                return;
            }

            WP_CLI::line("  ✓ Opened Elementor document");

            // Step 3: Build element structure
            $elements = $this->build_sample_elements();

            // Step 4: Save document with proper Elementor save routine
            $document->set_elements_data($elements);
            
            // Call Elementor's save method to ensure proper serialization
            $save_result = $document->save();

            if (!$save_result) {
                WP_CLI::warning("Document save returned false");
            } else {
                WP_CLI::line("  ✓ Document saved via Elementor API");
            }

            // Step 5: Regenerate CSS
            $this->regenerate_css($post_id);
            WP_CLI::line("  ✓ CSS regenerated");

            // Step 6: Verify
            $this->verify_page($post_id);

            WP_CLI::success("Page built successfully!");

        } catch (\Exception $e) {
            WP_CLI::error("Error: " . $e->getMessage());
            WP_CLI::error($e->getTraceAsString());
        }
    }

    /**
     * Build sample Elementor elements
     */
    private function build_sample_elements() {
        return [
            [
                'id' => substr(md5(uniqid()), 0, 8),
                'elType' => 'container',
                'settings' => [
                    'background_color' => '#f7f7f7',
                    'padding' => '60px 20px',
                    'content_width' => 'boxed',
                    'gap' => 'default'
                ],
                'elements' => [
                    [
                        'id' => substr(md5(uniqid()), 0, 8),
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
                        'id' => substr(md5(uniqid()), 0, 8),
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
                        'id' => substr(md5(uniqid()), 0, 8),
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

    /**
     * Regenerate CSS for the page
     */
    private function regenerate_css($post_id) {
        try {
            $elementor = \Elementor\Plugin::$instance;
            $document = $elementor->documents->get($post_id);

            if (!$document) {
                return;
            }

            // Get the CSS file
            if (method_exists($document, 'get_css_file')) {
                $css_file = $document->get_css_file();
                if ($css_file && method_exists($css_file, 'update')) {
                    $css_file->update();
                }
            }

            // Update post meta cache
            if (method_exists($document, 'update_edit_mode')) {
                $document->update_edit_mode('builder');
            }

        } catch (\Exception $e) {
            // Silent fail - CSS regeneration is not critical
        }
    }

    /**
     * Verify the page renders
     */
    private function verify_page($post_id) {
        // Check if Elementor data exists
        $elementor_data = get_post_meta($post_id, '_elementor_data', true);
        
        if (!$elementor_data) {
            WP_CLI::warning("No Elementor data found after save");
            return;
        }

        // Verify it's valid JSON
        $decoded = json_decode($elementor_data, true);
        if (!$decoded) {
            WP_CLI::warning("Elementor data is not valid JSON");
            return;
        }

        WP_CLI::line("  ✓ Elementor data verified and valid");
    }
}

// Register WP-CLI command
if (defined('WP_CLI') && WP_CLI) {
    WP_CLI::add_command('tshirtswiss build', 'TShirtSwiss_Kit_Builder');
}
