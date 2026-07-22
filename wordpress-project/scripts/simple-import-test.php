<?php
if (!defined('ABSPATH')) {
    require_once '/var/www/html/wp-load.php';
}

WP_CLI::line('');
WP_CLI::line('=== Import Test ===');
WP_CLI::line('');

$zip_file = '/exports/tshirtswiss-elementor-website-kit.zip';

if (!file_exists($zip_file)) {
    WP_CLI::error('ZIP not found: ' . $zip_file);
    exit(1);
}

WP_CLI::line('ZIP: ' . basename($zip_file) . ' (' . (filesize($zip_file)/1024) . ' KB)');
WP_CLI::line('');

// Try to use REST import endpoint if available
$result = wp_remote_post(get_rest_url(null, 'elementor/v1/import'), [
    'body' => [
        'import_file' => $zip_file
    ],
    'blocking' => true,
    'timeout' => 60
]);

if (is_wp_error($result)) {
    WP_CLI::warning('REST endpoint error: ' . $result->get_error_message());
    WP_CLI::line('');
    WP_CLI::line('Trying direct Import class...');
    
    try {
        use Elementor\App\Modules\ImportExport\Processes\Import;
        
        // Try creating Import with the correct format
        $import = new Import(['file_path' => $zip_file, 'file_name' => basename($zip_file)]);
        $import->register_default_runners();
        $result = $import->run();
        
        WP_CLI::success('Import completed');
    } catch (Throwable $e) {
        WP_CLI::error('Error: ' . substr($e->getMessage(), 0, 100));
    }
} else {
    $body = wp_remote_retrieve_body($result);
    $code = wp_remote_retrieve_response_code($result);
    WP_CLI::line("Response code: $code");
    WP_CLI::line('Response: ' . substr($body, 0, 200));
}

WP_CLI::line('');
