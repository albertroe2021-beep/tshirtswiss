<?php
/**
 * Populate Elementor Layouts from HTML Repository
 * 
 * This script extracts section layouts from repository HTML pages
 * and creates Elementor page designs for import kit.
 * 
 * Usage: wp eval-file populate_elementor_layouts.php
 */

if (!function_exists('wp_get_current_user')) {
    require_once '/var/www/html/wp-load.php';
}

use Elementor\Plugin as ElementorPlugin;
use Elementor\Core\Documents_Manager;

/**
 * Helper: Create Elementor Section
 */
function create_elementor_section($columns = 1, $background_color = '', $padding = '20 20 20 20') {
    return [
        'id' => 'section_' . uniqid(),
        'elType' => 'section',
        'settings' => array_filter([
            'background_color' => $background_color ?: '',
            'padding' => $padding,
        ]),
        'elements' => [],
        'isInner' => false,
    ];
}

/**
 * Helper: Create Elementor Column
 */
function create_elementor_column($width = 100, $elements = []) {
    return [
        'id' => 'column_' . uniqid(),
        'elType' => 'column',
        'settings' => [
            '_column_size' => $width,
        ],
        'elements' => $elements,
    ];
}

/**
 * Helper: Create Elementor Text Widget
 */
function create_text_widget($text, $tag = 'p', $font_size = '16', $color = '#111') {
    return [
        'id' => 'text_' . uniqid(),
        'elType' => 'widget',
        'settings' => [
            'editor' => $text,
            'title_size' => $tag,
            'title_color' => $color,
            'typography_typography' => 'custom',
            'typography_font_size' => $font_size,
        ],
        'widgetType' => 'text-editor',
    ];
}

/**
 * Helper: Create Elementor Heading Widget
 */
function create_heading_widget($text, $level = 'h2', $font_size = '36', $color = '#111') {
    return [
        'id' => 'heading_' . uniqid(),
        'elType' => 'widget',
        'settings' => [
            'title' => $text,
            'header_size' => $level,
            'title_color' => $color,
            'typography_typography' => 'custom',
            'typography_font_size' => $font_size,
            'alignment' => 'center',
        ],
        'widgetType' => 'heading',
    ];
}

/**
 * Helper: Create Elementor Button
 */
function create_button_widget($text, $url = '#', $style = 'primary') {
    $bg_color = $style === 'primary' ? '#e1111a' : 'transparent';
    $text_color = $style === 'primary' ? '#fff' : '#111';
    $border = $style === 'primary' ? 'none' : '1px solid #111';
    
    return [
        'id' => 'button_' . uniqid(),
        'elType' => 'widget',
        'settings' => [
            'text' => $text,
            'link' => ['url' => $url],
            'button_background_color' => $bg_color,
            'button_text_color' => $text_color,
            'button_border' => $border,
        ],
        'widgetType' => 'button',
    ];
}

/**
 * Helper: Create Elementor Image Widget
 */
function create_image_widget($url, $alt = '', $width = '100%') {
    return [
        'id' => 'image_' . uniqid(),
        'elType' => 'widget',
        'settings' => [
            'image' => ['url' => $url],
            'image_size' => 'full',
            'align' => 'center',
            'caption_text' => $alt,
        ],
        'widgetType' => 'image',
    ];
}

/**
 * Build Home Page Layout
 */
function build_home_page() {
    $page_elements = [];
    
    // Hero Section
    $hero_section = create_elementor_section(1, '#f7f7f7', '60 20 60 20');
    $hero_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Swiss-Managed Apparel Manufacturing', 'h1', '48', '#111'),
        create_text_widget('For Businesses That Expect Quality', 'h3', '24', '#e1111a'),
        create_text_widget('We help Swiss businesses manufacture premium custom apparel through a fully managed production process in Thailand.', 'p', '16', '#555'),
    ]);
    $page_elements[] = $hero_section;
    
    // Trust Section (5 Cards)
    $trust_section = create_elementor_section(1, '#fff', '40 20 40 20');
    $trust_cols = [];
    
    $trust_items = [
        ['Swiss Quality Standards', 'High standards and reliable communication.'],
        ['Factory Direct Pricing', 'Competitive production without unnecessary middlemen.'],
        ['Strict Quality Control', 'Quality checks at every production step.'],
        ['Worldwide Shipping', 'Delivery to Switzerland, Europe and worldwide.'],
        ['Long Term Partner', 'We support reliable reorders and ongoing production.'],
    ];
    
    foreach ($trust_items as $item) {
        $card_elements = [
            create_heading_widget($item[0], 'h3', '18', '#111'),
            create_text_widget($item[1], 'p', '14', '#555'),
        ];
        $trust_cols[] = create_elementor_column(20, $card_elements);
    }
    
    $trust_section['elements'] = $trust_cols;
    $page_elements[] = $trust_section;
    
    // Industries Section
    $industries_section = create_elementor_section(1, '#f7f7f7', '40 20 40 20');
    $industries_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Industries We Serve', 'h2', '36', '#111'),
        create_text_widget('Every industry has different requirements for branded apparel.', 'p', '16', '#555'),
    ]);
    $page_elements[] = $industries_section;
    
    // Products Section
    $products_section = create_elementor_section(1, '#fff', '40 20 40 20');
    $products_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Custom Products We Manufacture', 'h2', '36', '#111'),
        create_text_widget('From custom t-shirts and polos to premium corporate uniforms and private label collections.', 'p', '16', '#555'),
    ]);
    $page_elements[] = $products_section;
    
    // Process Section
    $process_section = create_elementor_section(1, '#f7f7f7', '40 20 40 20');
    $process_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Our Simple Process', 'h2', '36', '#111'),
    ]);
    
    $process_items = [
        'Product Consultation',
        'Sample & Approval',
        'Managed Production',
        'Quality Check',
        'International Delivery',
    ];
    
    $process_cols = [];
    foreach ($process_items as $process) {
        $process_cols[] = create_elementor_column(20, [
            create_heading_widget($process, 'h3', '16', '#111'),
        ]);
    }
    $process_section['elements'] = array_merge($process_section['elements'], $process_cols);
    $page_elements[] = $process_section;
    
    // CTA Section
    $cta_section = create_elementor_section(1, '#e1111a', '40 20 40 20');
    $cta_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Ready to Manufacture Clothing?', 'h2', '36', '#fff'),
        create_text_widget('Speak with our Swiss-managed team to discuss your project.', 'p', '16', '#fff'),
        create_button_widget('Request Your Quote', '/request-a-quote/', 'primary'),
    ]);
    $page_elements[] = $cta_section;
    
    return $page_elements;
}

/**
 * Build Products Page Layout
 */
function build_products_page() {
    $page_elements = [];
    
    // Hero Section
    $hero_section = create_elementor_section(1, '#f7f7f7', '60 20 60 20');
    $hero_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Custom Apparel Products', 'h1', '48', '#111'),
        create_text_widget('Explore custom t-shirts, polos, hoodies, workwear, uniforms, sportswear and merchandise.', 'p', '18', '#555'),
    ]);
    $page_elements[] = $hero_section;
    
    // Product Categories Section
    $products_section = create_elementor_section(1, '#fff', '40 20 40 20');
    $products_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Product Categories', 'h2', '36', '#111'),
    ]);
    
    $products = [
        'Custom T-Shirts',
        'Custom Polos',
        'Hoodies & Sweatshirts',
        'Jackets & Softshells',
        'Workwear',
        'Healthcare Uniforms',
    ];
    
    foreach ($products as $product) {
        $products_section['elements'][] = create_elementor_column(50, [
            create_heading_widget($product, 'h3', '18', '#111'),
        ]);
    }
    $page_elements[] = $products_section;
    
    // CTA Section
    $cta_section = create_elementor_section(1, '#e1111a', '40 20 40 20');
    $cta_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Need Help Choosing?', 'h2', '36', '#fff'),
        create_button_widget('Request a Quote', '/request-a-quote/', 'primary'),
    ]);
    $page_elements[] = $cta_section;
    
    return $page_elements;
}

/**
 * Build Services Page Layout
 */
function build_services_page() {
    $page_elements = [];
    
    // Hero Section
    $hero_section = create_elementor_section(1, '#f7f7f7', '60 20 60 20');
    $hero_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Apparel Manufacturing Services', 'h1', '48', '#111'),
        create_text_widget('OEM production, private label manufacturing, product development, printing, embroidery and more.', 'p', '18', '#555'),
    ]);
    $page_elements[] = $hero_section;
    
    // Services Grid Section
    $services_section = create_elementor_section(1, '#fff', '40 20 40 20');
    $services_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Core Services', 'h2', '36', '#111'),
    ]);
    
    $services = [
        'OEM Clothing Production',
        'Private Label Manufacturing',
        'Product Development',
        'Sampling',
        'Quality Control',
        'Worldwide Shipping',
    ];
    
    foreach (array_chunk($services, 2) as $row) {
        foreach ($row as $service) {
            $services_section['elements'][] = create_elementor_column(50, [
                create_heading_widget($service, 'h3', '18', '#111'),
            ]);
        }
    }
    $page_elements[] = $services_section;
    
    return $page_elements;
}

/**
 * Build Industries Page Layout
 */
function build_industries_page() {
    $page_elements = [];
    
    // Hero Section
    $hero_section = create_elementor_section(1, '#f7f7f7', '60 20 60 20');
    $hero_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Industries We Serve', 'h1', '48', '#111'),
        create_text_widget('Custom apparel solutions for every industry type.', 'p', '18', '#555'),
    ]);
    $page_elements[] = $hero_section;
    
    // Industries Grid
    $industries_section = create_elementor_section(1, '#fff', '40 20 40 20');
    $industries = [
        'Construction & Trades',
        'Healthcare',
        'Hospitality',
        'Sports & Fitness',
        'Combat Sports',
        'Corporate Apparel',
        'Franchises',
        'Ecommerce Brands',
    ];
    
    foreach (array_chunk($industries, 2) as $row) {
        foreach ($row as $industry) {
            $industries_section['elements'][] = create_elementor_column(50, [
                create_heading_widget($industry, 'h3', '18', '#111'),
            ]);
        }
    }
    $page_elements[] = $industries_section;
    
    return $page_elements;
}

/**
 * Build Resources Page Layout
 */
function build_resources_page() {
    $page_elements = [];
    
    // Hero Section
    $hero_section = create_elementor_section(1, '#f7f7f7', '60 20 60 20');
    $hero_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Resources & Support', 'h1', '48', '#111'),
        create_text_widget('Blog articles, FAQ, case studies and production guides.', 'p', '18', '#555'),
    ]);
    $page_elements[] = $hero_section;
    
    return $page_elements;
}

/**
 * Build About Page Layout
 */
function build_about_page() {
    $page_elements = [];
    
    // Hero Section
    $hero_section = create_elementor_section(1, '#f7f7f7', '60 20 60 20');
    $hero_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('About TShirtSwiss', 'h1', '48', '#111'),
        create_text_widget('Swiss-managed apparel manufacturing in Thailand.', 'p', '18', '#555'),
    ]);
    $page_elements[] = $hero_section;
    
    // Company Story
    $story_section = create_elementor_section(1, '#fff', '40 20 40 20');
    $story_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Our Story', 'h2', '36', '#111'),
        create_text_widget('TShirtSwiss combines Swiss communication standards with competitive apparel manufacturing in Thailand.', 'p', '16', '#555'),
    ]);
    $page_elements[] = $story_section;
    
    return $page_elements;
}

/**
 * Build Contact Page Layout
 */
function build_contact_page() {
    $page_elements = [];
    
    // Hero Section
    $hero_section = create_elementor_section(1, '#f7f7f7', '60 20 60 20');
    $hero_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Contact Us', 'h1', '48', '#111'),
        create_text_widget('Get in touch with our Swiss-managed team.', 'p', '18', '#555'),
    ]);
    $page_elements[] = $hero_section;
    
    return $page_elements;
}

/**
 * Build QA/Case Studies Page Layout
 */
function build_case_studies_page() {
    $page_elements = [];
    
    // Hero Section
    $hero_section = create_elementor_section(1, '#f7f7f7', '60 20 60 20');
    $hero_section['elements'][] = create_elementor_column(100, [
        create_heading_widget('Case Studies', 'h1', '48', '#111'),
        create_text_widget('Real examples of successful apparel manufacturing projects.', 'p', '18', '#555'),
    ]);
    $page_elements[] = $hero_section;
    
    return $page_elements;
}

/**
 * Build Child Page Layout (Product, Service, Industry)
 */
function build_child_page($parent_type, $name) {
    $page_elements = [];
    
    // Hero Section
    $hero_section = create_elementor_section(1, '#f7f7f7', '60 20 60 20');
    $hero_section['elements'][] = create_elementor_column(100, [
        create_heading_widget($name, 'h1', '48', '#111'),
        create_text_widget("Professional $parent_type solutions for your business.", 'p', '18', '#555'),
    ]);
    $page_elements[] = $hero_section;
    
    // Content Section
    $content_section = create_elementor_section(1, '#fff', '40 20 40 20');
    $content_section['elements'][] = create_elementor_column(100, [
        create_heading_widget("About $name", 'h2', '36', '#111'),
        create_text_widget("This $parent_type is tailored to meet specific business needs with quality, reliability and Swiss-managed communication.", 'p', '16', '#555'),
    ]);
    $page_elements[] = $content_section;
    
    return $page_elements;
}

/**
 * Update Page with Elementor Content
 */
function update_page_elementor_content($page_id, $page_elements) {
    if (!$page_id) {
        return false;
    }
    
    $document = ElementorPlugin::$instance->documents->get($page_id);
    
    if (!$document) {
        echo "Error: Could not get document for page $page_id\n";
        return false;
    }
    
    // Set page elements
    $document->set_elements_data($page_elements);
    $document->save();
    
    echo "✓ Updated page $page_id with Elementor content\n";
    return true;
}

/**
 * Main Execution
 */
function populate_elementor_layouts() {
    global $wpdb;
    
    echo "=== Populating Elementor Page Layouts ===\n\n";
    
    // Map page slugs to layout builders
    $page_layouts = [
        'home' => 'build_home_page',
        'products' => 'build_products_page',
        'services' => 'build_services_page',
        'industries' => 'build_industries_page',
        'resources' => 'build_resources_page',
        'about-us' => 'build_about_page',
        'contact' => 'build_contact_page',
        'case-studies' => 'build_case_studies_page',
    ];
    
    // Process main pages
    foreach ($page_layouts as $slug => $builder_func) {
        $page = get_page_by_path($slug);
        if ($page) {
            echo "\n📄 Processing: $slug (ID: {$page->ID})\n";
            $elements = call_user_func($builder_func);
            update_page_elementor_content($page->ID, $elements);
        } else {
            echo "⚠ Skipped: $slug (not found)\n";
        }
    }
    
    // Process child pages
    $child_pages = $wpdb->get_results("
        SELECT ID, post_name, post_parent
        FROM $wpdb->posts
        WHERE post_type = 'page'
        AND post_status = 'publish'
        AND post_parent > 0
        LIMIT 20
    ");
    
    echo "\n\n=== Processing Child Pages ===\n";
    foreach ($child_pages as $page) {
        $parent = get_post($page->post_parent);
        if ($parent) {
            $parent_slug = $parent->post_name;
            $page_name = ucwords(str_replace('-', ' ', $page->post_name));
            
            echo "\n📄 Processing child: $page_name (Parent: $parent_slug, ID: {$page->ID})\n";
            $elements = build_child_page($parent_slug, $page_name);
            update_page_elementor_content($page->ID, $elements);
        }
    }
    
    echo "\n✅ Elementor layout population complete!\n";
}

// Run the script
populate_elementor_layouts();
?>
