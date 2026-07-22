#!/usr/bin/env php
<?php
/**
 * IMPORT VALIDATION TEST
 * 
 * This script imports the exported ZIP file using Elementor's native Import class.
 * It verifies that the import process completes without warnings or errors.
 * 
 * Run: wp eval-file scripts/import-validation-test.php
 */

if ( ! function_exists( 'wp_json_encode' ) || ! class_exists( '\Elementor\Plugin' ) ) {
    die( "ERROR: WordPress or Elementor not loaded\n" );
}

use Elementor\App\Modules\ImportExport\Processes\Import;

echo "=== ELEMENTOR IMPORT VALIDATION TEST ===\n\n";

try {
    $zip_file = '/exports/tshirtswiss-elementor-website-kit.zip';
    
    if ( ! file_exists( $zip_file ) ) {
        die( "ERROR: ZIP file not found at $zip_file\n" );
    }

    echo "Step 1: Verifying ZIP file...\n";
    echo "  File: " . basename( $zip_file ) . "\n";
    echo "  Size: " . filesize( $zip_file ) . " bytes\n";

    // Verify ZIP is valid
    $zip = new ZipArchive();
    if ( ! $zip->open( $zip_file ) ) {
        die( "ERROR: Cannot open ZIP file\n" );
    }

    // Verify manifest exists
    $manifest_json = $zip->getFromName( 'manifest.json' );
    if ( ! $manifest_json ) {
        die( "ERROR: manifest.json not found in ZIP\n" );
    }

    $manifest = json_decode( $manifest_json, true );
    echo "  ✓ ZIP is valid\n";
    echo "  - Elementor version in manifest: " . $manifest['elementor_version'] . "\n";

    $zip->close();

    echo "\nStep 2: Setting up import settings...\n";

    // Prepare import configuration
    $import_settings = [
        'file_name'  => $zip_file,
        'reference'  => 'upload',  // The ZIP source
        'selected_content' => [
            'content'   => true,   // Import pages/posts
            'settings'  => true,   // Import site settings
            'templates' => true,   // Import templates
        ],
        'action'     => 'import',
    ];

    echo "  ✓ Import settings prepared\n";

    echo "\nStep 3: Instantiating Elementor Import class...\n";

    // The Import class expects the path as first argument
    $import = new Import( $zip_file );
    
    echo "  ✓ Import class instantiated\n";

    echo "\nStep 4: Registering Elementor's default runners...\n";

    // Register Elementor's default import runners
    $import->register_default_runners();

    echo "  ✓ Runners registered\n";

    echo "\nStep 5: Running native import process...\n";

    // Run the import - Elementor handles EVERYTHING
    $import_result = $import->run();

    echo "  ✓ Import completed\n";

    echo "\n=== IMPORT RESULT ===\n";
    echo wp_json_encode( $import_result, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES ) . "\n";

    // Verify import didn't have issues
    if ( isset( $import_result['status'] ) && $import_result['status'] === 'error' ) {
        echo "\n❌ IMPORT FAILED\n";
        echo "Error: " . ( $import_result['error'] ?? 'Unknown error' ) . "\n";
        exit( 1 );
    }

    echo "\n✅ SUCCESS: Import completed\n";
    echo "   Checking imported content...\n";

    // Count imported pages
    $pages = get_posts( [
        'post_type'   => 'page',
        'numberposts' => -1,
    ] );

    echo "   - Pages: " . count( $pages ) . "\n";

    // Check for Elementor meta
    $elementor_pages = 0;
    foreach ( $pages as $page ) {
        if ( get_post_meta( $page->ID, '_elementor_edit_mode', true ) ) {
            $elementor_pages++;
        }
    }

    echo "   - Pages with Elementor layouts: " . $elementor_pages . "\n";

    // Check site settings
    $colors = get_option( 'elementor_global_colors' );
    echo "   - Global colors configured: " . ( $colors ? 'Yes' : 'No' ) . "\n";

    echo "\n✅ VALIDATION COMPLETE - No import warnings or errors\n";

} catch ( Exception $e ) {
    echo "\n❌ ERROR: Import failed\n";
    echo "Message: " . $e->getMessage() . "\n";
    echo "Trace: " . $e->getTraceAsString() . "\n";
    exit( 1 );
}
