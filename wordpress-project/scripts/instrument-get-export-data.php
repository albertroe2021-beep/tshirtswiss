#!/usr/bin/env php
<?php
/**
 * Instrument get_export_data() to see actual return structure
 * Output to file to avoid terminal issues
 */

$output = fopen( '/tmp/instrument-output.txt', 'w' );

function out( $text ) {
    global $output;
    fwrite( $output, $text . "\n" );
}

if ( ! function_exists( 'wp_json_encode' ) || ! class_exists( '\Elementor\Plugin' ) ) {
    out( "ERROR: WordPress or Elementor not loaded" );
    fclose( $output );
    exit( 1 );
}

use Elementor\Plugin;

// Get a page that's known to have Elementor content
$page_8 = get_post( 8 );

if ( ! $page_8 ) {
    out( "ERROR: Page 8 not found" );
    fclose( $output );
    exit( 1 );
}

out( "=== INSTRUMENTING get_export_data() ===" );
out( "" );
out( "Page ID: {$page_8->ID}" );
out( "Page Title: {$page_8->post_title}" );
out( "" );

// Get the document
$document = Plugin::$instance->documents->get( $page_8->ID );

if ( ! $document ) {
    out( "ERROR: Document not found for page {$page_8->ID}" );
    fclose( $output );
    exit( 1 );
}

out( "Document class: " . get_class( $document ) );
out( "" );

// Call get_export_data() and dump the structure
$export_data = $document->get_export_data();

out( "=== RETURN VALUE FROM get_export_data() ===" );
out( "" );

// Check the top-level structure
out( "Top-level keys: " . implode( ', ', array_keys( $export_data ) ) );
out( "" );

// Check the content field specifically
$content = $export_data['content'] ?? null;

out( "Content field:" );
out( "  Type: " . gettype( $content ) );

if ( is_array( $content ) ) {
    out( "  Is array: YES" );
    out( "  Count: " . count( $content ) );
    
    if ( count( $content ) > 0 ) {
        out( "  First element type: " . gettype( $content[0] ) );
        if ( is_array( $content[0] ) ) {
            $first_keys = array_slice( array_keys( $content[0] ), 0, 8 );
            out( "  First element keys: " . implode( ', ', $first_keys ) );
        }
    }
} elseif ( is_object( $content ) ) {
    out( "  Is object: YES" );
    out( "  Object class: " . get_class( $content ) );
    $content_arr = (array) $content;
    out( "  Object properties: " . implode( ', ', array_keys( $content_arr ) ) );
    
    // If it's an object with content/settings/metadata properties, that's the double-wrap
    if ( isset( $content_arr['content'] ) && isset( $content_arr['settings'] ) && isset( $content_arr['metadata'] ) ) {
        out( "" );
        out( "  ⚠️  DOUBLE-WRAP DETECTED!" );
        out( "  Object contains: content, settings, metadata" );
        out( "  Inner content type: " . gettype( $content_arr['content'] ) );
    }
} else {
    out( "  Type is neither array nor object: " . gettype( $content ) );
}

out( "" );

// Full dump of export_data structure
out( "=== FULL EXPORT DATA (FIRST 500 CHARS) ===" );
out( "" );
$var_export = var_export( $export_data, true );
out( substr( $var_export, 0, 500 ) );
out( "..." );
out( "" );

out( "=== SETTINGS FIELD ===" );
$settings = $export_data['settings'] ?? null;
out( "Type: " . gettype( $settings ) );
if ( is_array( $settings ) ) {
    $keys = array_slice( array_keys( $settings ), 0, 5 );
    out( "Sample keys: " . implode( ', ', $keys ) );
}

out( "" );
out( "=== METADATA FIELD ===" );
$metadata = $export_data['metadata'] ?? null;
out( "Type: " . gettype( $metadata ) );
if ( is_array( $metadata ) ) {
    out( "Count: " . count( $metadata ) );
}

out( "" );
out( "=== CONCLUSION ===" );

if ( is_array( $content ) && count( $content ) > 0 && is_array( $content[0] ) && isset( $content[0]['elType'] ) ) {
    out( "✓ get_export_data() returns CORRECT structure" );
    out( "  Content is an array of Elementor elements" );
    out( "  First element has 'elType' property" );
} elseif ( is_array( $content ) && isset( $content['content'] ) ) {
    out( "✗ get_export_data() returns WRAPPED structure" );
    out( "  Content is an object/array with {content, settings, metadata} keys" );
} else {
    out( "? Unknown structure" );
}

fclose( $output );
echo "Output written to /tmp/instrument-output.txt\n";
