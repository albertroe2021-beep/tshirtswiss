<?php
/**
 * Populate Elementor Page Layouts - SIMPLIFIED VERSION
 * Uses proper Elementor Container + Widget structure
 * 
 * Usage: wp eval-file populate_elementor_layouts_v2.php
 */

if (!function_exists('wp_get_current_user')) {
    require_once '/var/www/html/wp-load.php';
}

use Elementor\Core\Documents_Manager;
use Elementor\Plugin as ElementorPlugin;

/**
 * Helper: Create Section with Elementor Container
 */
function create_container($background = '', $padding = '40px 20px', $children = []) {
    return [
        'id' => 'container_' . uniqid(),
        'elType' => 'container',
        'settings' => array_filter([
            'background_color' => $background ?: '',
            'padding' => $padding,
            'content_width' => 'boxed',
            'gap' => 'default',
        ]),
        'elements' => $children,
    ];
}

/**
 * Helper: Create Heading Widget
 */
function create_heading($text, $level = 'h2', $size = '32', $color = '#111') {
    return [
        'id' => 'heading_' . uniqid(),
        'elType' => 'widget',
        'widgetType' => 'heading',
        'settings' => [
            'title' => $text,
            'header_size' => $level,
            'title_color' => $color,
            'typography_typography' => 'custom',
            'typography_font_size' => ['size' => $size, 'unit' => 'px'],
            'alignment' => 'center',
        ],
        'elements' => [],
    ];
}

/**
 * Helper: Create Text Widget
 */
function create_text($text, $color = '#666') {
    return [
        'id' => 'text_' . uniqid(),
        'elType' => 'widget',
        'widgetType' => 'text-editor',
        'settings' => [
            'editor' => "<p>$text</p>",
            'editor_color' => $color,
            'typography_typography' => 'custom',
            'typography_font_size' => ['size' => '16', 'unit' => 'px'],
            'alignment' => 'center',
        ],
        'elements' => [],
    ];
}

/**
 * Helper: Create Button Widget
 */
function create_button($text, $url = '#', $style = 'primary') {
    if ($style === 'primary') {
        $bg_color = '#e1111a';
        $text_color = '#fff';
    } else {
        $bg_color = 'transparent';
        $text_color = '#111';
    }
    
    return [
        'id' => 'button_' . uniqid(),
        'elType' => 'widget',
        'widgetType' => 'button',
        'settings' => [
            'text' => $text,
            'link' => ['url' => $url],
            'button_background_color' => $bg_color,
            'button_text_color' => $text_color,
            'button_border_border' => $style === 'outline' ? 'solid' : 'none',
            'button_border_width' => ['size' => '1', 'unit' => 'px'],
            'button_border_color' => $style === 'outline' ? '#111' : 'transparent',
            'alignment' => 'center',
        ],
        'elements' => [],
    ];
}

/**
 * Build HOME Page
 */
function build_home_content() {
    $elements = [];
    
    // Hero Section
    $elements[] = create_container('#f7f7f7', '60px 20px', [
        create_heading('Swiss-Managed Apparel Manufacturing', 'h1', '48', '#111'),
        create_heading('For Businesses That Expect Quality', 'h2', '28', '#e1111a'),
        create_text('We help Swiss businesses manufacture premium custom apparel through a fully managed production process in Thailand. From concept and sampling to production, quality control and worldwide delivery.'),
        create_button('Request a Quote', '../request-a-quote/', 'primary'),
    ]);
    
    // Trust Section (5 items)
    $trust_items = [
        'Swiss Quality Standards',
        'Factory Direct Pricing',
        'Strict Quality Control',
        'Worldwide Shipping',
        'Long Term Partner',
    ];
    
    $trust_children = [];
    foreach ($trust_items as $item) {
        $trust_children[] = create_container('', '20px 10px', [
            create_heading($item, 'h3', '18', '#111'),
        ]);
    }
    
    $elements[] = create_container('#fff', '40px 20px', $trust_children);
    
    // Industries Section
    $elements[] = create_container('#f7f7f7', '40px 20px', [
        create_heading('Industries We Serve', 'h2', '36', '#111'),
        create_text('Every industry has different requirements for branded apparel. TShirtSwiss serves construction, healthcare, hospitality, sports, corporate and many other sectors.'),
    ]);
    
    // Process Section
    $process_items = ['Product Consultation', 'Sample & Approval', 'Managed Production', 'Quality Check', 'International Delivery'];
    $process_children = [];
    foreach ($process_items as $item) {
        $process_children[] = create_container('', '20px 10px', [
            create_heading($item, 'h3', '16', '#111'),
        ]);
    }
    
    $elements[] = create_container('#fff', '40px 20px', $process_children);
    
    // CTA Section
    $elements[] = create_container('#e1111a', '60px 20px', [
        create_heading('Ready to Manufacture Clothing?', 'h2', '36', '#fff'),
        create_text('Speak with our Swiss-managed team to discuss your project.', '#fff'),
        create_button('Request Your Quote', '../request-a-quote/', 'primary'),
    ]);
    
    return $elements;
}

/**
 * Build PRODUCTS Page
 */
function build_products_content() {
    $elements = [];
    
    // Hero
    $elements[] = create_container('#f7f7f7', '60px 20px', [
        create_heading('Custom Apparel Products', 'h1', '48', '#111'),
        create_text('Explore custom t-shirts, polos, hoodies, workwear, uniforms, sportswear and merchandise.'),
    ]);
    
    // Products Grid
    $products = ['Custom T-Shirts', 'Custom Polos', 'Hoodies & Sweatshirts', 'Jackets & Softshells', 'Workwear', 'Healthcare Uniforms'];
    $product_children = [];
    foreach ($products as $product) {
        $product_children[] = create_container('', '20px 10px', [
            create_heading($product, 'h3', '18', '#111'),
        ]);
    }
    
    $elements[] = create_container('#fff', '40px 20px', $product_children);
    
    // CTA
    $elements[] = create_container('#e1111a', '60px 20px', [
        create_heading('Need Help Choosing?', 'h2', '36', '#fff'),
        create_button('Request a Quote', '../request-a-quote/', 'primary'),
    ]);
    
    return $elements;
}

/**
 * Build SERVICES Page
 */
function build_services_content() {
    $elements = [];
    
    // Hero
    $elements[] = create_container('#f7f7f7', '60px 20px', [
        create_heading('Apparel Manufacturing Services', 'h1', '48', '#111'),
        create_text('OEM production, private label manufacturing, product development, printing, embroidery and more.'),
    ]);
    
    // Services
    $services = ['OEM Production', 'Private Label', 'Product Development', 'Sampling', 'Quality Control', 'Worldwide Shipping'];
    $service_children = [];
    foreach ($services as $service) {
        $service_children[] = create_container('', '20px 10px', [
            create_heading($service, 'h3', '18', '#111'),
        ]);
    }
    
    $elements[] = create_container('#fff', '40px 20px', $service_children);
    
    return $elements;
}

/**
 * Build INDUSTRIES Page
 */
function build_industries_content() {
    $elements = [];
    
    // Hero
    $elements[] = create_container('#f7f7f7', '60px 20px', [
        create_heading('Industries We Serve', 'h1', '48', '#111'),
        create_text('Custom apparel solutions tailored to every industry.'),
    ]);
    
    // Industries Grid
    $industries = ['Construction & Trades', 'Healthcare', 'Hospitality', 'Sports & Fitness', 'Combat Sports', 'Corporate Apparel'];
    $industry_children = [];
    foreach ($industries as $industry) {
        $industry_children[] = create_container('', '20px 10px', [
            create_heading($industry, 'h3', '18', '#111'),
        ]);
    }
    
    $elements[] = create_container('#fff', '40px 20px', $industry_children);
    
    return $elements;
}

/**
 * Build RESOURCES Page
 */
function build_resources_content() {
    $elements = [];
    
    // Hero
    $elements[] = create_container('#f7f7f7', '60px 20px', [
        create_heading('Resources & Support', 'h1', '48', '#111'),
        create_text('Blog articles, FAQ, case studies and production guides to help your project succeed.'),
    ]);
    
    return $elements;
}

/**
 * Build ABOUT Page
 */
function build_about_content() {
    $elements = [];
    
    // Hero
    $elements[] = create_container('#f7f7f7', '60px 20px', [
        create_heading('About TShirtSwiss', 'h1', '48', '#111'),
        create_text('Swiss-managed apparel manufacturing in Thailand.'),
    ]);
    
    // Story
    $elements[] = create_container('#fff', '40px 20px', [
        create_heading('Our Story', 'h2', '36', '#111'),
        create_text('TShirtSwiss combines Swiss communication standards with competitive apparel manufacturing in Thailand, making international production easier for Swiss businesses.'),
    ]);
    
    return $elements;
}

/**
 * Build CONTACT Page
 */
function build_contact_content() {
    $elements = [];
    
    // Hero
    $elements[] = create_container('#f7f7f7', '60px 20px', [
        create_heading('Contact Us', 'h1', '48', '#111'),
        create_text('Get in touch with our Swiss-managed team. We respond within one business day.'),
    ]);
    
    return $elements;
}

/**
 * Build CASE STUDIES Page
 */
function build_case_studies_content() {
    $elements = [];
    
    // Hero
    $elements[] = create_container('#f7f7f7', '60px 20px', [
        create_heading('Case Studies', 'h1', '48', '#111'),
        create_text('Real examples of successful apparel manufacturing projects from our clients.'),
    ]);
    
    return $elements;
}

/**
 * Build Child Page (Product, Service, Industry)
 */
function build_child_page_content($parent_type, $name) {
    $elements = [];
    
    // Hero
    $elements[] = create_container('#f7f7f7', '60px 20px', [
        create_heading($name, 'h1', '48', '#111'),
        create_text("Professional $parent_type solutions designed for your specific business needs with quality, reliability and Swiss-managed communication."),
    ]);
    
    // Content
    $elements[] = create_container('#fff', '40px 20px', [
        create_heading("About " . $name, 'h2', '36', '#111'),
        create_text("This page covers $parent_type options tailored to your industry and business requirements. Contact us for more details."),
    ]);
    
    return $elements;
}

/**
 * Update Elementor Page
 */
function update_elementor_page($page_id, $elements) {
    if (!$page_id) {
        return false;
    }
    
    try {
        $document = ElementorPlugin::$instance->documents->get($page_id);
        if (!$document) {
            echo "  ⚠ Could not get document for page $page_id\n";
            return false;
        }
        
        // Use WordPress post meta to store Elementor content
        $elementor_data = [
            'content' => $elements,
            'settings' => ['template' => 'default'],
            'metadata' => [],
        ];
        
        update_post_meta($page_id, '_elementor_data', wp_json_encode($elementor_data));
        update_post_meta($page_id, '_elementor_edit_mode', 'builder');
        
        // Mark as edited by Elementor
        wp_update_post([
            'ID' => $page_id,
            'post_modified' => current_time('mysql'),
            'post_modified_gmt' => current_time('mysql', 1),
        ]);
        
        echo "  ✓ Updated page $page_id\n";
        return true;
    } catch (Exception $e) {
        echo "  ⚠ Error updating page $page_id: " . $e->getMessage() . "\n";
        return false;
    }
}

/**
 * Main Function
 */
function populate_layouts() {
    echo "\n=== Populating Elementor Layouts ===\n\n";
    
    global $wpdb;
    
    $page_layouts = [
        'home' => 'build_home_content',
        'products' => 'build_products_content',
        'services' => 'build_services_content',
        'industries' => 'build_industries_content',
        'resources' => 'build_resources_content',
        'about-us' => 'build_about_content',
        'contact' => 'build_contact_content',
        'case-studies' => 'build_case_studies_content',
    ];
    
    // Main Pages
    echo "📄 Main Pages:\n";
    foreach ($page_layouts as $slug => $builder_func) {
        $page = get_page_by_path($slug);
        if ($page) {
            $elements = call_user_func($builder_func);
            update_elementor_page($page->ID, $elements);
        } else {
            echo "  ⚠ Not found: $slug\n";
        }
    }
    
    // Child Pages
    echo "\n📄 Child Pages:\n";
    $child_pages = $wpdb->get_results("
        SELECT ID, post_name, post_parent FROM {$wpdb->posts}
        WHERE post_type = 'page' AND post_status = 'publish' AND post_parent > 0
        ORDER BY post_parent, ID
    ");
    
    foreach ($child_pages as $page) {
        $parent = get_post($page->post_parent);
        if ($parent) {
            $parent_slug = $parent->post_name;
            $page_name = ucwords(str_replace('-', ' ', $page->post_name));
            
            $elements = build_child_page_content($parent_slug, $page_name);
            update_elementor_page($page->ID, $elements);
        }
    }
    
    echo "\n✅ Layout population complete!\n\n";
}

// Execute
populate_layouts();
?>
