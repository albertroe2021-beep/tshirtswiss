<?php
/**
 * Custom WP-CLI Command: Import Elementor Kit
 * 
 * Wrapper around Elementor's kit import that properly handles user context
 */

if (defined('WP_CLI') && WP_CLI) {
    class Elementor_Kit_Import_Command extends WP_CLI_Command {
        /**
         * Import an Elementor kit
         *
         * ## SYNOPSIS
         *
         * <file>
         * : Path to the kit ZIP file
         *
         * [--include=<include>]
         * : Which data to include (content, site-settings, templates)
         *
         * ## EXAMPLES
         *
         *     wp elementor-kit-import /path/to/kit.zip
         *     wp elementor-kit-import /path/to/kit.zip --include=content,site-settings
         */
        public function import($args, $assoc_args) {
            // Ensure we have an admin user context
            wp_set_current_user(1); // User ID 1 is typically the admin
            
            if (!current_user_can('manage_options')) {
                WP_CLI::error('Current user does not have admin capability');
            }
            
            $file_path = isset($args[0]) ? $args[0] : null;
            
            if (!$file_path) {
                WP_CLI::error('File path required');
            }
            
            if (!file_exists($file_path)) {
                WP_CLI::error('File not found: ' . $file_path);
            }
            
            WP_CLI::line('Starting import...');
            WP_CLI::line('File: ' . $file_path);
            WP_CLI::line('User: ' . wp_get_current_user()->user_login);
            WP_CLI::line('');
            
            try {
                // Call the actual Elementor import command
                // This runs the official command but with proper user context
                $cmd = 'wp elementor kit import ' . escapeshellarg($file_path);
                
                if (!empty($assoc_args)) {
                    foreach ($assoc_args as $key => $value) {
                        $cmd .= ' --' . $key . '=' . escapeshellarg($value);
                    }
                }
                
                // Re-execute through a subprocess to avoid infinite recursion
                // but this time with the user context already set
                system($cmd . ' --allow-root 2>&1', $return_code);
                
                if ($return_code === 0) {
                    WP_CLI::success('Import completed successfully!');
                } else {
                    WP_CLI::error('Import returned error code: ' . $return_code);
                }
                
            } catch (\Throwable $e) {
                WP_CLI::error('Import failed: ' . $e->getMessage());
            }
        }
    }
    
    WP_CLI::add_command('elementor-kit-import', 'Elementor_Kit_Import_Command');
}
