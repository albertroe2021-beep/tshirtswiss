#!/usr/bin/env php
<?php
/**
 * CORRECT: Use Elementor's actual native Export class
 *
 * This script uses Elementor's internal Export mechanism (not custom JSON writing).
 * The ZIP file produced is created by Elementor itself via its native export API.
 *
 * Run: wp eval-file scripts/elementor_native_export_correct.php
 */

// Ensure WordPress and Elementor are loaded
if ( ! function_exists( 'wp_json_encode' ) || ! class_exists( '\Elementor\Plugin' ) ) {
    die( "ERROR: WordPress or Elementor not loaded\n" );
}

use Elementor\App\Modules\ImportExport\Processes\Export;
use Elementor\Plugin as ElementorPlugin;

echo "=== Elementor Native Export (Using Native API) ===\n\n";

try {
    // Define export directory
    $export_base = '/exports/native-elementor-website-kit';
    if ( ! is_dir( $export_base ) ) {
        wp_mkdir_p( $export_base );
    }

    // Create export settings specifying WHAT to export
    $export_settings = [
        'include' => [
            'content',      // Include all WordPress content (pages, posts, CPTs)
            'settings',     // Include site settings
            'templates',    // Include Elementor templates
            'taxonomies',   // Include categories/tags
        ],
        'kitInfo' => [
            'name'        => 'TShirtSwiss Reference Kit',
            'description' => 'Production-ready Elementor website template',
        ],
        'plugins'                    => [],  // Don't include plugin data
        'selectedCustomPostTypes'    => [ 'page', 'post', 'elementor_library' ], // Only these CPTs
    ];

    echo "Export Settings:\n";
    echo "  - Include: " . implode( ', ', $export_settings['include'] ) . "\n";
    echo "  - Kit Name: " . $export_settings['kitInfo']['name'] . "\n";
    echo "  - Custom Post Types: " . implode( ', ', $export_settings['selectedCustomPostTypes'] ) . "\n";
    echo "\n";

    // Instantiate Elementor's native Export class
    $export = new Export( $export_settings );

    // Register default runners (these are Elementor's standard exporters)
    $export->register_default_runners();

    // THIS IS THE KEY LINE: Call Elementor's native export process
    // This creates the ZIP file using Elementor's internal mechanisms
    $export_result = $export->run();

    echo "Export Result:\n";
    echo "  File: " . basename( $export_result['file_name'] ) . "\n";
    echo "  Size: " . filesize( $export_result['file_name'] ) . " bytes\n";
    echo "  Manifest Keys: " . implode( ', ', array_keys( $export_result['manifest'] ) ) . "\n";

    // The ZIP file is now at $export_result['file_name']
    // Copy it to our dist location
    $source_zip = $export_result['file_name'];
    $dest_zip = '/exports/tshirtswiss-elementor-website-kit.zip';

    if ( copy( $source_zip, $dest_zip ) ) {
        echo "\n✓ ZIP copied to: $dest_zip\n";
        echo "✓ File size: " . filesize( $dest_zip ) . " bytes\n";
    } else {
        echo "\n✗ ERROR: Could not copy ZIP file\n";
        exit( 1 );
    }

    // Verify ZIP contents
    echo "\n✓ ZIP Contents:\n";
    $zip = new ZipArchive();
    if ( $zip->open( $dest_zip ) ) {
        for ( $i = 0; $i < $zip->numFiles; $i++ ) {
            $stat = $zip->statIndex( $i );
            echo "  - " . $stat['name'] . " (" . $stat['size'] . " bytes)\n";
        }
        $zip->close();
    }

    echo "\n✓ SUCCESS: Native Elementor export complete\n";
    echo "   ZIP file is now ready for import into any WordPress/Elementor installation\n";
    echo "   File: $dest_zip\n";

} catch ( Exception $e ) {
    echo "\n✗ ERROR: Export failed\n";
    echo "Message: " . $e->getMessage() . "\n";
    exit( 1 );
}
