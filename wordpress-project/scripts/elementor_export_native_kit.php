<?php
/**
 * Native Elementor Export Kit Generator
 * Run via: wp eval-file scripts/elementor_export_native_kit.php
 */

if ( ! defined( 'ABSPATH' ) ) {
    define( 'ABSPATH', dirname( __DIR__ ) . '/' );
}

// Ensure Elementor is loaded
if ( ! function_exists( 'elementor_pro' ) && ! class_exists( '\Elementor\Plugin' ) ) {
    die( "Elementor not loaded.\n" );
}

// Get the export manager
$export_dir = '/exports/native-elementor-kit';
if ( ! is_dir( $export_dir ) ) {
    mkdir( $export_dir, 0755, true );
}

// Gather all pages and posts
$posts = get_posts( array(
    'post_type'      => array( 'page', 'post' ),
    'posts_per_page' => -1,
) );

$templates = get_posts( array(
    'post_type'      => 'elementor_library',
    'posts_per_page' => -1,
) );

$all_content = array_merge( $posts, $templates );

// Create manifest
$manifest = array(
    'version'     => ELEMENTOR_VERSION,
    'site_url'    => get_option( 'siteurl' ),
    'home_url'    => get_option( 'home' ),
    'title'       => get_option( 'blogname' ),
    'description' => get_option( 'blogdescription' ),
    'pages'       => count( $posts ),
    'templates'   => count( $templates ),
    'export_date' => current_time( 'c' ),
);

file_put_contents(
    $export_dir . '/manifest.json',
    wp_json_encode( $manifest, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES )
);

// Export content records
$content_export = array();

foreach ( $all_content as $post ) {
    $elementor_data = get_post_meta( $post->ID, '_elementor_data', true );
    $elementor_settings = get_post_meta( $post->ID, '_elementor_page_settings', true );
    
    $record = array(
        'id'              => $post->ID,
        'title'           => $post->post_title,
        'slug'            => $post->post_name,
        'type'            => $post->post_type,
        'parent'          => $post->post_parent,
        'status'          => $post->post_status,
        'content'         => $post->post_content,
        'elementor_data'  => $elementor_data ? json_decode( $elementor_data, true ) : null,
        'elementor_settings' => $elementor_settings ? json_decode( $elementor_settings, true ) : null,
    );
    
    $content_export[] = $record;
}

file_put_contents(
    $export_dir . '/content.json',
    wp_json_encode( $content_export, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES )
);

// Export global styles
$global_colors = get_option( 'elementor_global_colors' );
$global_fonts = get_option( 'elementor_global_fonts' );
$global_settings = get_option( 'elementor_general_settings' );

$styles_export = array(
    'global_colors'   => $global_colors ? json_decode( $global_colors, true ) : array(),
    'global_fonts'    => $global_fonts ? json_decode( $global_fonts, true ) : array(),
    'site_settings'   => $global_settings ? json_decode( $global_settings, true ) : array(),
);

file_put_contents(
    $export_dir . '/styles.json',
    wp_json_encode( $styles_export, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES )
);

// Create theme settings snapshot
$theme_settings = array(
    'theme'           => get_template(),
    'theme_version'   => wp_get_theme()->get( 'Version' ),
    'wp_version'      => get_bloginfo( 'version' ),
    'elementor_version' => defined( 'ELEMENTOR_VERSION' ) ? ELEMENTOR_VERSION : 'unknown',
    'site_url'        => get_option( 'siteurl' ),
    'permalink_structure' => get_option( 'permalink_structure' ),
);

file_put_contents(
    $export_dir . '/theme-settings.json',
    wp_json_encode( $theme_settings, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES )
);

echo "Elementor export generated to: {$export_dir}\n";
echo "Files created:\n";
echo "  - manifest.json\n";
echo "  - content.json\n";
echo "  - styles.json\n";
echo "  - theme-settings.json\n";
