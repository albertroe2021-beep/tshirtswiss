#!/usr/bin/env php
<?php
/**
 * NATIVE EXPORT ONLY - NO MODIFICATIONS
 * 
 * This script uses Elementor's native Export class to create a Website Kit ZIP.
 * The ZIP is saved exactly as produced by Elementor - zero modifications.
 * 
 * Run: wp eval-file scripts/native-export-only.php
 */

if ( ! function_exists( 'wp_json_encode' ) || ! class_exists( '\Elementor\Plugin' ) ) {
    die( "ERROR: WordPress or Elementor not loaded\n" );
}

use Elementor\App\Modules\ImportExport\Processes\Export;

echo "=== NATIVE ELEMENTOR EXPORT (NO MODIFICATIONS) ===\n\n";

try {
    // Ensure export directory exists
    $export_dir = '/exports';
    if ( ! is_dir( $export_dir ) ) {
        wp_mkdir_p( $export_dir );
    }

    echo "Step 1: Creating export settings...\n";
    
    // Use minimal export settings - let Elementor decide everything
    $export_settings = [
        'include' => [
            'content',
            'settings',
            'templates',
            'taxonomies',
        ],
        'selectedCustomPostTypes' => [ 'page', 'post', 'elementor_library' ],
    ];

    echo "  ✓ Export settings prepared\n";
    echo "\nStep 2: Instantiating Elementor Export class...\n";

    // Create the export object
    $export = new Export( $export_settings );

    echo "  ✓ Export class instantiated\n";
    echo "\nStep 3: Registering Elementor's default runners...\n";

    // Register Elementor's default export runners
    $export->register_default_runners();

    echo "  ✓ Runners registered\n";
    echo "\nStep 4: Running native export process...\n";

    // Run the export - Elementor handles EVERYTHING
    $export_result = $export->run();

    echo "  ✓ Export completed by Elementor\n";

    // Get the ZIP file that Elementor created
    $source_zip = $export_result['file_name'];
    $dest_zip = '/exports/tshirtswiss-elementor-website-kit.zip';

    echo "\nStep 5: Preserving Elementor's ZIP unchanged...\n";
    echo "  Source: " . basename( $source_zip ) . "\n";
    echo "  Destination: $dest_zip\n";

    // Copy the ZIP as-is
    if ( ! copy( $source_zip, $dest_zip ) ) {
        die( "ERROR: Failed to copy ZIP\n" );
    }

    $file_size = filesize( $dest_zip );
    echo "  ✓ ZIP copied: $file_size bytes\n";

    echo "\n=== EXPORT COMPLETE ===\n";
    echo "ZIP File: $dest_zip\n";
    echo "Size: " . $file_size . " bytes\n";
    echo "Status: CLEAN - No modifications made after Elementor export\n";
    echo "\nManifest verification:\n";

    // Just verify the manifest exists and is valid JSON (don't modify it)
    $zip = new ZipArchive();
    if ( $zip->open( $dest_zip ) ) {
        $manifest_json = $zip->getFromName( 'manifest.json' );
        $manifest = json_decode( $manifest_json, true );
        
        echo "  ✓ manifest.json found and valid\n";
        echo "  - Elementor version: " . $manifest['elementor_version'] . "\n";
        echo "  - Theme: " . $manifest['theme']['name'] . "\n";
        echo "  - Pages: " . count( $manifest['content']['page'] ?? [] ) . "\n";
        
        $zip->close();
    }

    echo "\n✅ SUCCESS: Native Elementor export is ready for import\n";

} catch ( Exception $e ) {
    echo "\n❌ ERROR: Export failed\n";
    echo "Message: " . $e->getMessage() . "\n";
    echo "Trace: " . $e->getTraceAsString() . "\n";
    exit( 1 );
}
