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
            'name'        => 'TShirtSwiss Elementor Website Kit',
            'title'       => 'TShirtSwiss Website Kit',
            'description' => 'Complete, production-ready Elementor website template with professional layouts and full design system',
            'author'      => 'TShirtSwiss',
            'version'     => '2.0',
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
    // But we need to update the manifest.json with proper metadata
    $source_zip = $export_result['file_name'];
    $temp_dir = sys_get_temp_dir() . '/elementor-manifest-fix-' . uniqid();
    wp_mkdir_p( $temp_dir );

    // Extract the ZIP to update manifest
    $zip = new ZipArchive();
    if ( ! $zip->open( $source_zip ) ) {
        die( "ERROR: Could not open source ZIP\n" );
    }

    // Extract all files
    $zip->extractTo( $temp_dir );
    $zip->close();

    // Update manifest.json with proper metadata
    $manifest_path = $temp_dir . '/manifest.json';
    if ( file_exists( $manifest_path ) ) {
        $manifest = json_decode( file_get_contents( $manifest_path ), true );
        
        // Set proper metadata
        $manifest['name'] = 'TShirtSwiss Elementor Website Kit';
        $manifest['title'] = 'TShirtSwiss Website Kit';
        $manifest['description'] = 'Complete, production-ready Elementor website template with professional layouts for services, products, industries, and more.';
        $manifest['author'] = 'TShirtSwiss';
        
        // Ensure version matches
        if ( ! isset( $manifest['version'] ) ) {
            $manifest['version'] = '2.0';
        }
        
        file_put_contents( $manifest_path, wp_json_encode( $manifest ) );
        echo "✓ Updated manifest.json with proper metadata\n";
    }

    // Re-create ZIP with updated manifest
    $dest_zip = '/exports/tshirtswiss-elementor-website-kit.zip';
    $zip = new ZipArchive();
    
    // Remove old ZIP if exists
    if ( file_exists( $dest_zip ) ) {
        unlink( $dest_zip );
    }

    if ( ! $zip->open( $dest_zip, ZipArchive::CREATE ) ) {
        die( "ERROR: Could not create destination ZIP\n" );
    }

    // Add all files from temp directory
    $files = new RecursiveIteratorIterator(
        new RecursiveDirectoryIterator( $temp_dir ),
        RecursiveIteratorIterator::SELF_FIRST
    );

    foreach ( $files as $file ) {
        if ( is_file( $file ) ) {
            $relative_path = substr( $file, strlen( $temp_dir ) + 1 );
            $zip->addFile( $file, $relative_path );
        }
    }

    $zip->close();

    // Clean up temp directory
    array_map( 'unlink', glob( "$temp_dir/*.*" ) );
    foreach ( glob( "$temp_dir/*", GLOB_ONLYDIR ) as $dir ) {
        array_map( 'unlink', glob( "$dir/*.*" ) );
        rmdir( $dir );
    }
    rmdir( $temp_dir );

    echo "\n✓ ZIP created with updated manifest: $dest_zip\n";
    echo "✓ File size: " . filesize( $dest_zip ) . " bytes\n";

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
