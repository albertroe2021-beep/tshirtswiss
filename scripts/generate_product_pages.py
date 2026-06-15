import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRODUCTS_DIR = ROOT / 'wordpress' / 'pages' / 'products'

page_info = {
    'index': {
        'title': 'Products',
        'subtitle': 'Swiss-managed apparel production built for premium B2B brands.',
        'lede': 'Browse our product categories for corporate apparel, uniforms, sportswear and private label clothing manufactured with Swiss quality oversight in Thailand.',
        'button_text': 'Request a Quote',
        'button_secondary': 'Contact Sales',
        'button_secondary_link': '/pages/contact/',
        'hero_image_text': 'Products Overview',
        'feature_title': 'Products built for Swiss business',
        'feature_text': 'Our product range is designed for Swiss enterprises seeking reliable quality, transparent production and premium end-use apparel.',
        'feature_image_text': 'Product range',
        'cards': [
            ('Custom T-Shirts', '/pages/products/custom-t-shirts/'),
            ('Custom Polos', '/pages/products/custom-polos/'),
            ('Hoodies & Sweatshirts', '/pages/products/hoodies-sweatshirts/'),
            ('Jackets & Softshells', '/pages/products/jackets-softshells/'),
            ('Workwear', '/pages/products/workwear/'),
            ('Healthcare Uniforms', '/pages/products/healthcare-uniforms/'),
            ('Medical Scrubs', '/pages/products/medical-scrubs/'),
            ('Corporate Apparel', '/pages/products/corporate-apparel/'),
            ('Sportswear', '/pages/products/sportswear/'),
            ('Rashguards', '/pages/products/rashguards/'),
            ('MMA Shorts', '/pages/products/mma-shorts/'),
            ('Muay Thai Shorts', '/pages/products/muay-thai-shorts/'),
            ('Private Label Clothing', '/pages/products/private-label-clothing/'),
            ('Promotional Merchandise', '/pages/products/promotional-merchandise/'),
            ('Tote Bags', '/pages/products/tote-bags/'),
            ('Caps & Headwear', '/pages/products/caps-headwear/')
        ],
    }
}

product_pages = {
    'caps-headwear': {
        'title': 'Caps & Headwear',
        'subtitle': 'Premium headwear production for corporate, events and retail.',
        'lede': 'Swiss-managed manufacturing for branded caps, hats and headwear with accurate embroidery, print and finishing tailored for your brand.',
        'hero_image_text': 'Caps & Headwear',
        'feature_title': 'Protective headwear with strong brand presence',
        'feature_text': 'Our headwear solutions deliver precise branding, durable fabrics and reliable fit for hospitality, retail and promotional campaigns.',
        'feature_image_text': 'Cap production',
        'process_title': 'Our Headwear Production Process',
        'process_steps': [
            ('Design review', 'We review logo placement, color, and construction for every cap style.'),
            ('Material selection', 'Choose premium cotton, twill, or performance blends for durability and comfort.'),
            ('Embroidery & printing', 'Apply branding with high-definition embroidery or screen-printed logos.'),
            ('Finishing', 'Complete with labels, tags, and careful stitching for a premium feel.'),
            ('Quality check', 'Inspect fit, finish and branding accuracy before packing.'),
            ('Shipping', 'Deliver finished headwear to Switzerland or Europe on time.')
        ],
    },
    'corporate-apparel': {
        'title': 'Corporate Apparel',
        'subtitle': 'Executive apparel and workwear for modern Swiss businesses.',
        'lede': 'Create premium corporate uniforms and branded garments that reflect Swiss precision and professional quality.',
        'hero_image_text': 'Corporate Apparel',
        'feature_title': 'Professional corporate apparel with lasting polish',
        'feature_text': 'From executive shirts to branded outerwear, we manufacture corporate apparel that elevates your business image and supports daily wear.',
        'feature_image_text': 'Corporate clothing',
        'process_title': 'Our Corporate Apparel Workflow',
        'process_steps': [
            ('Brand briefing', 'We capture your corporate guidelines, colors and uniform needs.'),
            ('Fabric sourcing', 'Select premium materials suited to business uniforms and client comfort.'),
            ('Sample approval', 'Approve cut, fit and branding before full production begins.'),
            ('Production run', 'We produce uniforms with consistent quality and finish.'),
            ('Inspection', 'Every garment is checked for stitching, color and brand accuracy.'),
            ('Delivery', 'Ship uniforms safely with packaging and labeling that match your schedule.')
        ],
    },
    'custom-polos': {
        'title': 'Custom Polos',
        'subtitle': 'Performance polos crafted for teams, hospitality and branded events.',
        'lede': 'Swiss-managed polo production with crisp logos, reliable fit and premium fabric choices for corporate and lifestyle use.',
        'hero_image_text': 'Custom Polos',
        'feature_title': 'Polos tailored for brand comfort and style',
        'feature_text': 'Our polos combine polished design with durable construction, ideal for teams, hospitality staff and promotional campaigns.',
        'feature_image_text': 'Polo production',
        'process_title': 'Our Polo Production Process',
        'process_steps': [
            ('Concept & branding', 'Define the fit and logo placement for your polo range.'),
            ('Fabric selection', 'Choose breathable, durable knit fabrics for everyday wear.'),
            ('Printing & embroidery', 'Apply logos with precise embroidery or soft print techniques.'),
            ('Stitching', 'Use reinforced seams and premium finishing for long-lasting use.'),
            ('Quality inspection', 'Check each polo for fit, color and craftsmanship.'),
            ('Shipment', 'Deliver completed polos with clear packaging and documentation.')
        ],
    },
    'custom-t-shirts': {
        'title': 'Custom T-Shirts',
        'subtitle': 'Made-to-order t-shirts for branding, events and teamwear.',
        'lede': 'Swiss-managed manufacturing for custom t-shirts with bold prints, fine details and consistent quality across every order.',
        'hero_image_text': 'Custom T-Shirts',
        'feature_title': 'Custom t-shirts built to represent your brand',
        'feature_text': 'From performance tees to soft everyday shirts, our production process delivers precise printing and premium fabric performance.',
        'feature_image_text': 'T-shirt production',
        'process_title': 'Our Custom T-Shirt Process',
        'process_steps': [
            ('Design review', 'We advise on artwork placement and print methods for each shirt.'),
            ('Fabric choice', 'Select soft, durable materials that match your brand and usage.'),
            ('Print setup', 'Prepare screens and files for sharp, enduring prints.'),
            ('Production', 'Run the print and assembly process with Swiss-managed oversight.'),
            ('Quality control', 'Inspect each shirt for print clarity and fabric finish.'),
            ('Packing', 'Package shirts carefully for safe delivery to your team or clients.')
        ],
    },
    'healthcare-uniforms': {
        'title': 'Healthcare Uniforms',
        'subtitle': 'Professional uniforms for healthcare teams and clinical environments.',
        'lede': 'Swiss-managed production of healthcare uniforms with durable fabrics, clear branding and quality control to meet clinical requirements.',
        'hero_image_text': 'Healthcare Uniforms',
        'feature_title': 'Uniforms designed for medical teams',
        'feature_text': 'Our healthcare uniforms combine function, comfort and hygiene with premium manufacturing standards and Swiss project management.',
        'feature_image_text': 'Medical uniforms',
        'process_title': 'Our Healthcare Uniform Workflow',
        'process_steps': [
            ('Fit consultation', 'Define the right fits and fabric performance for clinical teams.'),
            ('Material selection', 'Choose breathable, easy-care fabrics for daily medical use.'),
            ('Branding', 'Apply logos and name tags clearly and professionally.'),
            ('Production', 'Manufacture uniforms with strict quality and hygiene checks.'),
            ('Inspection', 'Conduct final checks for seam strength and color accuracy.'),
            ('Delivery', 'Ship uniforms ready for immediate use in Switzerland or Europe.')
        ],
    },
    'hoodies-sweatshirts': {
        'title': 'Hoodies & Sweatshirts',
        'subtitle': 'Premium outerwear for teams, events and branded merchandise.',
        'lede': 'Swiss-managed hoodie and sweatshirt production with strong branding, cozy fabrics and reliable finishing for every order.',
        'hero_image_text': 'Hoodies & Sweatshirts',
        'feature_title': 'Premium hoodies built for comfort and impact',
        'feature_text': 'Our hoodies and sweatshirts are made with robust fabrics and precise branding to support teamwear, retail lines and promotional collections.',
        'feature_image_text': 'Hoodie production',
        'process_title': 'Our Hoodie & Sweatshirt Process',
        'process_steps': [
            ('Style selection', 'Choose hoodies, crews or zip-front styles that fit your brand.'),
            ('Fabric sourcing', 'Select plush, durable materials for every season.'),
            ('Brand application', 'Use prints, embroidery and labels for premium finishing.'),
            ('Assembly', 'Manufacture with care and attention to seam quality.'),
            ('Quality review', 'Inspect each item for comfort, consistency and branding.'),
            ('Shipping', 'Pack and ship hoodies with protection and documentation.')
        ],
    },
    'jackets-softshells': {
        'title': 'Jackets & Softshells',
        'subtitle': 'Functional outerwear for corporate teams, events and active use.',
        'lede': 'Swiss-managed jacket production for premium outerwear with weather resistance, branding and tailored finishes.',
        'hero_image_text': 'Jackets & Softshells',
        'feature_title': 'Outerwear designed for performance and polish',
        'feature_text': 'From softshells to insulated jackets, we deliver branded outerwear that supports Swiss business standards and outdoor use.',
        'feature_image_text': 'Jacket production',
        'process_title': 'Our Jacket Production Process',
        'process_steps': [
            ('Requirement review', 'Define weather performance, fit and branding needs.'),
            ('Fabric selection', 'Choose technical shells and durable finishes.'),
            ('Brand application', 'Add logos with embroidery, heat transfer or embossing.'),
            ('Assembly', 'Craft jackets with reinforced seams and quality hardware.'),
            ('Inspection', 'Check every outerwear piece for fit, finish and durability.'),
            ('Delivery', 'Ship finished jackets with premium packaging and labels.')
        ],
    },
    'medical-scrubs': {
        'title': 'Medical Scrubs',
        'subtitle': 'Clean, comfortable scrubs for healthcare professionals.',
        'lede': 'Swiss-managed scrub manufacturing with premium fabric, reliable branding and fit designed for clinical teams.',
        'hero_image_text': 'Medical Scrubs',
        'feature_title': 'Scrubs crafted for daily clinical wear',
        'feature_text': 'Our scrubs combine practical design with durable fabrics and Swiss-quality control to support healthcare environments.',
        'feature_image_text': 'Scrub production',
        'process_title': 'Our Medical Scrub Process',
        'process_steps': [
            ('Requirement analysis', 'Understand your scrub needs for fit, color and performance.'),
            ('Fabric selection', 'Choose lightweight, breathable materials for long shifts.'),
            ('Branding', 'Apply logos and details while maintaining clean lines.'),
            ('Production', 'Manufacture with strict quality and hygienic oversight.'),
            ('Inspection', 'Check each scrub for stitching, color and sizing accuracy.'),
            ('Shipping', 'Deliver scrubs packaged for healthcare teams and facilities.')
        ],
    },
    'mma-shorts': {
        'title': 'MMA Shorts',
        'subtitle': 'High-performance shorts for combat sports and fight teams.',
        'lede': 'Swiss-managed MMA short production with technical fit, bold branding and durable materials for training and competition.',
        'hero_image_text': 'MMA Shorts',
        'feature_title': 'Shorts built for competition and team branding',
        'feature_text': 'We produce MMA shorts that balance mobility, durability and premium visual appeal for fight brands and clubs.',
        'feature_image_text': 'MMA production',
        'process_title': 'Our MMA Shorts Process',
        'process_steps': [
            ('Briefing', 'Capture your design direction, fit and performance needs.'),
            ('Material sourcing', 'Choose stretch, quick-dry fabrics for fightwear.'),
            ('Brand application', 'Add logos and artwork with crisp print or embroidery.'),
            ('Cutting & sewing', 'Assemble shorts with precise panels and reinforcement.'),
            ('Quality inspection', 'Validate fit, durability and print quality on every pair.'),
            ('Shipping', 'Deliver fight shorts packaged for teams and athletes.')
        ],
    },
    'muay-thai-shorts': {
        'title': 'Muay Thai Shorts',
        'subtitle': 'Premium fight shorts for Muay Thai teams and brands.',
        'lede': 'Swiss-managed Muay Thai short production with bold graphics, sturdy construction and exacting quality control.',
        'hero_image_text': 'Muay Thai Shorts',
        'feature_title': 'Shorts that support fight performance and visual impact',
        'feature_text': 'Our Muay Thai shorts are crafted for movement, durability and sharp branding that stands out in training and competition.',
        'feature_image_text': 'Muay Thai production',
        'process_title': 'Our Muay Thai Production Process',
        'process_steps': [
            ('Design alignment', 'Define the exact look, logo placement and construction details.'),
            ('Fabric choice', 'Use lightweight, flexible materials for fight performance.'),
            ('Logo application', 'Add premium branding with bold prints and finishes.'),
            ('Assembly', 'Sew shorts with reinforced seams and comfort panels.'),
            ('Final review', 'Inspect each pair for fit, print fidelity and durability.'),
            ('Delivery', 'Ship shorts ready for fighters and team distribution.')
        ],
    },
    'private-label-clothing': {
        'title': 'Private Label Clothing',
        'subtitle': 'Full private-label production for premium apparel brands.',
        'lede': 'Swiss-managed private label manufacturing from fabric sourcing to brand-ready finished garments.',
        'hero_image_text': 'Private Label Clothing',
        'feature_title': 'Private label apparel made for your brand',
        'feature_text': 'We support end-to-end private label clothing production with quality control, custom finishes and Swiss-managed process oversight.',
        'feature_image_text': 'Private label',
        'process_title': 'Our Private Label Process',
        'process_steps': [
            ('Brand consultation', 'Define the concept, materials and packaging for your label.'),
            ('Fabric & trim sourcing', 'Choose premium materials and brand details.'),
            ('Prototype development', 'Approve samples and refine the design.'),
            ('Production run', 'Manufacture with consistent quality and brand accuracy.'),
            ('Inspection', 'Check fit, finish and consistency across every garment.'),
            ('Packaging', 'Prepare brand-ready packaging for retail or direct delivery.')
        ],
    },
    'promotional-merchandise': {
        'title': 'Promotional Merchandise',
        'subtitle': 'Branded merchandise for events, campaigns and retail.',
        'lede': 'Swiss-managed promotional merchandise production for high-quality branded items and apparel that support campaigns and brand visibility.',
        'hero_image_text': 'Promotional Merchandise',
        'feature_title': 'Merchandise designed for strong brand recall',
        'feature_text': 'We produce promotional garments and goods that maintain premium quality while driving brand awareness at events, activations and retail.',
        'feature_image_text': 'Merchandise',
        'process_title': 'Our Promotional Merchandise Process',
        'process_steps': [
            ('Campaign briefing', 'Define your event, audience and merchandise goals.'),
            ('Product selection', 'Choose the right apparel and items for your brand.'),
            ('Brand application', 'Apply logos and artwork with clear, vibrant results.'),
            ('Production oversight', 'Manufacture merchandise with consistent quality standards.'),
            ('Quality checking', 'Verify durability and brand presentation before shipping.'),
            ('Distribution', 'Deliver promotional goods ready for event use or retail.')
        ],
    },
    'rashguards': {
        'title': 'Rashguards',
        'subtitle': 'Technical rashguards for sports, teams and active brands.',
        'lede': 'Swiss-managed rashguard manufacturing for performance sportswear with sharp branding and durable stretch fabrics.',
        'hero_image_text': 'Rashguards',
        'feature_title': 'Rashguards made for active performance',
        'feature_text': 'Our rashguards combine technical fabrics, precise branding and a premium fit, ideal for combat sports, water sports and athletic teams.',
        'feature_image_text': 'Rashguard production',
        'process_title': 'Our Rashguard Production Process',
        'process_steps': [
            ('Fit and fabric briefing', 'Choose the right stretch and protective materials for your rashguards.'),
            ('Artwork setup', 'Prepare high-impact graphics for sharp prints.'),
            ('Printing and assembly', 'Produce rashguards with accurate logos and fixtures.'),
            ('Quality control', 'Inspect every garment for fit, durability and print clarity.'),
            ('Finishing', 'Complete with labels and packaging suited to sports brands.'),
            ('Delivery', 'Ship rashguards ready for training, competition or retail.')
        ],
    },
    'sportswear': {
        'title': 'Sportswear',
        'subtitle': 'Performance apparel for fitness brands, teams and events.',
        'lede': 'Swiss-managed sportswear production for premium athletes, gyms and sports brands that need quality, fit and mobility.',
        'hero_image_text': 'Sportswear',
        'feature_title': 'Sportswear designed for movement and durability',
        'feature_text': 'We manufacture active apparel that keeps pace with training, teamwear and lifestyle use while maintaining premium Swiss-managed quality.',
        'feature_image_text': 'Sportswear production',
        'process_title': 'Our Sportswear Production Process',
        'process_steps': [
            ('Performance planning', 'Define the ideal fit, fabric and brand presentation for your sportswear.'),
            ('Material sourcing', 'Use stretch, moisture-wicking and high-performance textiles.'),
            ('Brand application', 'Print or embroider logos with sharp detail and durability.'),
            ('Assembly', 'Construct sportswear with reinforced seams and comfort features.'),
            ('Inspection', 'Verify fit, fabric performance and branding consistency.'),
            ('Shipping', 'Deliver finished apparel with protective packaging and labels.')
        ],
    },
    'tote-bags': {
        'title': 'Tote Bags',
        'subtitle': 'Branded tote bags for retail, events and hospitality.',
        'lede': 'Swiss-managed tote bag manufacturing for reusable branded bags with quality materials and crisp printing.',
        'hero_image_text': 'Tote Bags',
        'feature_title': 'Tote bags with premium print and durability',
        'feature_text': 'Our tote bags are crafted for everyday use, retail sales and branded events, with clean printing and strong construction.',
        'feature_image_text': 'Tote bag production',
        'process_title': 'Our Tote Bag Process',
        'process_steps': [
            ('Material selection', 'Choose durable canvas, cotton or recycled blends for your bags.'),
            ('Design review', 'Align logo placement and print style with your brand.'),
            ('Printing', 'Apply branding with vivid, long-lasting inks.'),
            ('Assembly', 'Construct bags with strong stitching and sturdy handles.'),
            ('Quality review', 'Inspect each bag for durability and print accuracy.'),
            ('Packing', 'Deliver tote bags ready for retail or event distribution.')
        ],
    },
    'workwear': {
        'title': 'Workwear',
        'subtitle': 'Durable uniforms and protective apparel for trades and teams.',
        'lede': 'Swiss-managed workwear production for heavy-duty uniforms, safety clothing and branded trade apparel.',
        'hero_image_text': 'Workwear',
        'feature_title': 'Workwear built for durability and reliability',
        'feature_text': 'We manufacture workwear that meets demanding environments while delivering premium Swiss-managed quality and consistent branding.',
        'feature_image_text': 'Workwear production',
        'process_title': 'Our Workwear Production Process',
        'process_steps': [
            ('Requirements briefing', 'Define protective needs, durability and brand expectations.'),
            ('Fabric selection', 'Choose heavy-duty textiles built for tough use.'),
            ('Branding', 'Add logos and details that withstand worksite wear.'),
            ('Construction', 'Assemble garments with reinforced seams and finishes.'),
            ('Inspection', 'Verify durability, fit and branding accuracy.'),
            ('Delivery', 'Ship workwear ready for teams and job sites.')
        ],
    },
}

feature_icons = [
    ('Vibrant colors', 'Bright, consistent prints for every design.'),
    ('Durable & long lasting', 'Premium inks and fabrics that keep their quality.'),
    ('Cost effective', 'Smart production methods that preserve value.'),
    ('Bulk order specialists', 'Reliable supply for larger apparel runs.'),
    ('Consistent quality', 'Swiss-managed checks at every step.')
]

process_labels = [
    'Consultation & Artwork',
    'Screen Preparation',
    'Printing',
    'Curing',
    'Quality Check',
    'Packing & Shipping'
]

applications = [
    ('Workwear & Uniforms', 'Professional uniforms and branded workwear.'),
    ('Corporate Apparel', 'Executive uniforms and office wear.'),
    ('Sportswear & Activewear', 'Performance apparel for teams and brands.'),
    ('Promotional T-Shirts', 'Event apparel and campaign garments.'),
    ('Event & Merchandise', 'Branded merchandise for activations.'),
    ('School & University Wear', 'Team and campus apparel.')
]

sustainability_points = [
    ('Eco-Friendly inks available', 'Low-impact inks for responsible production.'),
    ('Reduced water consumption', 'Efficient dyeing and finishing practices.'),
    ('Responsible waste management', 'Minimized waste from fabric to packaging.'),
    ('Ethical labor practices', 'Swiss-managed teams monitoring fair production.')
]

faq_items = [
    ('What is the minimum order quantity (MOQ)?', 'Minimum quantities vary by product. We can support both smaller sample runs and larger production batches.'),
    ('How many colors can I use?', 'Most products support multiple colors, including complex logos and multi-color artwork.'),
    ('How long does production take?', 'Typical lead times depend on product type and order size, but we target fast, reliable delivery.'),
    ('What fabrics are available?', 'We offer a range of premium fabrics from cotton blends to technical performance textiles.'),
    ('Is this durable?', 'Yes — all products are manufactured with durable materials, premium inks and Swiss-managed quality control.'),
    ('Can you match Pantone colors?', 'We can match Pantone colors for many print and branding processes when required.')
]

cta_features = [
    'Free Consultation',
    'Competitive Pricing',
    'No Obligation',
    'Fast Response'
]


def generate_html(title, subtitle, lede, hero_image_text, feature_title, feature_text, feature_image_text, process_title=None, process_steps=None, cards=None, page_path='/pages/products/', product_menu_items=None):
    if process_title is None:
        process_title = 'Our Production Process'
    if process_steps is None:
        process_steps = [
            ('Consultation & Artwork', 'We define your brand goals, artwork and delivery requirements.'),
            ('Screen Preparation', 'Screens and production files are prepared with precision.'),
            ('Printing', 'The selected product is printed using premium materials.'),
            ('Curing', 'Garments are cured for durability and wash resistance.'),
            ('Quality Check', 'Each order is inspected for consistent quality.'),
            ('Packing & Shipping', 'Items are carefully packed and shipped on time.')
        ]
    if product_menu_items is None:
        product_menu_items = page_info['index']['cards']

    cards_html = ''
    if cards:
        cards_html = '\n'.join(
            f'            <article class="card"><h3>{name}</h3><p>{description}</p><a class="card-link" href="{link}">View page</a></article>'
            for name, link, description in cards
        )
    else:
        cards_html = '\n'.join(
            f'            <article class="card"><h3>{name}</h3><p>{description}</p><a class="card-link" href="{link}">View page</a></article>'
            for name, link, description in [
                (name, link, 'Explore details and request a quote for this product.')
                for name, link in page_info['index']['cards']
            ]
        )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | TShirtSwiss.ch</title>
  <style>
:root {{
  color-scheme: light;
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  color: #111;
  background: #f7f7f7;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: #f7f7f7; color: #111; }}
a {{ color: inherit; text-decoration: none; }}
img {{ max-width: 100%; display: block; }}
.page-shell {{ display: flex; flex-direction: column; min-height: 100vh; }}
.topbar {{ background: #111; color: #f5f5f5; font-size: .82rem; letter-spacing: .12em; text-transform: uppercase; }}
.topbar .wrapper {{ max-width: 1280px; margin: 0 auto; padding: 12px 24px; display: flex; justify-content: space-between; gap: 18px; flex-wrap: wrap; align-items: center; }}
.topbar .status {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }}
.topbar .status span {{ opacity: .78; }}
.site-header {{ background: #fff; position: sticky; top: 0; z-index: 30; border-bottom: 1px solid rgba(17,17,17,.08); }}
.site-header .wrapper {{ max-width: 1280px; margin: 0 auto; padding: 24px; display: flex; align-items: center; justify-content: space-between; gap: 18px; flex-wrap: wrap; }}
.brand {{ font-size: 1.05rem; font-weight: 800; letter-spacing: .18em; text-transform: uppercase; color: #111; }}
.nav {{ display: flex; gap: 28px; flex-wrap: wrap; font-size: .95rem; align-items: center; }}
.nav a {{ color: #111; opacity: .88; transition: opacity .2s, color .2s; }}
.nav a:hover {{ opacity: 1; color: #D52B1E; }}
.nav-dropdown {{ position: relative; }}
.nav-dropdown > a::after {{ content: '▾'; margin-left: 8px; font-size: .75rem; opacity: .75; }}
.dropdown-menu {{ position: absolute; top: 100%; left: 0; min-width: 220px; background: #fff; border: 1px solid rgba(17,17,17,.12); border-radius: 20px; box-shadow: 0 24px 60px rgba(17,17,17,.12); opacity: 0; visibility: hidden; transform: translateY(12px); transition: opacity .2s ease, visibility .2s ease, transform .2s ease; z-index: 100; padding: 10px 0; }}
.nav-dropdown:hover .dropdown-menu,
.nav-dropdown:focus-within .dropdown-menu {{ opacity: 1; visibility: visible; transform: translateY(0); }}
.dropdown-menu a {{ display: block; padding: 12px 22px; color: #111; opacity: .9; white-space: nowrap; transition: background .2s, opacity .2s; }}
.dropdown-menu a:hover {{ background: rgba(213,43,30,.06); opacity: 1; }}
.cta-button {{ padding: 16px 30px; background: #D52B1E; color: #fff; border-radius: 999px; font-weight: 700; box-shadow: 0 20px 45px rgba(213,43,30,.18); }}
main {{ flex: 1; max-width: 1280px; margin: 0 auto; padding: 36px 24px 60px; }}
.breadcrumb {{ display: flex; gap: 10px; flex-wrap: wrap; align-items: center; font-size: .92rem; color: #555; margin: 24px 0 14px; }}
.breadcrumb a {{ color: #111; opacity: .8; }}
.breadcrumb span {{ opacity: .65; }}
.hero {{ display: grid; grid-template-columns: 1.05fr .95fr; gap: 36px; align-items: center; min-height: 78vh; padding: 40px 0 48px; }}
.hero-copy {{ max-width: 670px; }}
.hero-eyebrow {{ font-size: .82rem; text-transform: uppercase; letter-spacing: .26em; color: #D52B1E; font-weight: 700; margin-bottom: 20px; }}
.hero-title {{ font-size: clamp(3rem, 4vw, 4.8rem); line-height: .96; margin: 0; color: #111; }}
.hero-subtitle {{ margin: 24px 0 0; font-size: 1.15rem; line-height: 1.8; color: #4a4a4a; max-width: 45rem; }}
.hero-text {{ margin: 32px 0 0; font-size: 1rem; line-height: 1.8; color: #555; max-width: 40rem; }}
.feature-list {{ display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 16px; margin-top: 34px; }}
.feature-card {{ background: #fff; border: 1px solid rgba(17,17,17,.08); border-radius: 16px; padding: 18px 16px; display: flex; flex-direction: column; gap: 10px; min-height: 120px; box-shadow: 0 18px 40px rgba(17,17,17,.05); }}
.feature-card strong {{ font-size: .95rem; display: block; color: #111; }}
.feature-card span {{ color: #555; font-size: .92rem; line-height: 1.6; }}
.hero-actions {{ display: flex; flex-wrap: wrap; gap: 16px; margin-top: 30px; }}
.hero-actions a {{ display: inline-flex; align-items: center; justify-content: center; gap: 10px; border-radius: 999px; padding: 16px 28px; font-weight: 700; transition: transform .2s, box-shadow .2s; }}
.hero-actions a.primary {{ background: #D52B1E; color: #fff; }}
.hero-actions a.secondary {{ border: 1px solid rgba(17,17,17,.12); color: #111; background: #fff; }}
.hero-visual {{ border-radius: 32px; overflow: hidden; background: linear-gradient(180deg, #f5f5f5 0%, #e7e7e7 100%); box-shadow: 0 35px 100px rgba(17,17,17,.12); }}
.hero-visual img {{ width: 100%; height: auto; }}
.section {{ padding: 72px 0; }}
.section--white {{ background: #fff; }}
.section__inner {{ display: grid; gap: 36px; max-width: 1280px; margin: 0 auto; }}
.section--split .section__inner {{ grid-template-columns: repeat(2, minmax(0, 1fr)); align-items: center; }}
.section-title {{ display: flex; flex-direction: column; gap: 18px; }}
.section-title h2 {{ margin: 0; font-size: clamp(2.4rem, 3vw, 3.2rem); line-height: 1.04; font-weight: 800; color: #111; }}
.section-title p {{ margin: 0; max-width: 44rem; color: #545454; line-height: 1.85; font-size: 1rem; }}
.section .section-image {{ border-radius: 28px; overflow: hidden; }}
.section .section-image img {{ width: 100%; height: auto; display: block; }}
.process-grid {{ display: grid; gap: 18px; grid-template-columns: repeat(3, minmax(0, 1fr)); margin-top: 28px; }}
.process-step {{ background: #fff; border: 1px solid rgba(17,17,17,.08); border-radius: 24px; padding: 24px; display: flex; gap: 18px; align-items: flex-start; box-shadow: 0 18px 45px rgba(17,17,17,.05); }}
.process-step .icon {{ min-width: 52px; min-height: 52px; border-radius: 16px; background: #F9F0EF; color: #D52B1E; display: grid; place-items: center; font-weight: 800; }}
.process-step h3 {{ margin: 0 0 10px; font-size: 1rem; font-weight: 700; color: #111; }}
.process-step p {{ margin: 0; color: #575757; line-height: 1.75; font-size: .95rem; }}
.split-grid {{ display: grid; gap: 32px; grid-template-columns: 1.2fr .8fr; align-items: center; }}
.benefits-block {{ display: grid; gap: 24px; grid-template-columns: repeat(2, minmax(0, 1fr)); }}
.benefit-card {{ background: #fff; border-radius: 28px; padding: 28px; box-shadow: 0 24px 70px rgba(17,17,17,.06); }}
.benefit-card h3 {{ margin: 0 0 14px; font-size: 1.1rem; font-weight: 700; color: #111; }}
.benefit-card p {{ margin: 0; color: #575757; line-height: 1.8; font-size: .96rem; }}
.applications {{ display: grid; gap: 18px; grid-template-columns: repeat(4, minmax(0, 1fr)); margin-top: 28px; }}
.application {{ background: #fff; border-radius: 24px; padding: 22px; border: 1px solid rgba(17,17,17,.08); box-shadow: 0 20px 50px rgba(17,17,17,.05); display: flex; flex-direction: column; gap: 12px; }}
.application h3 {{ margin: 0; font-size: 1rem; color: #111; }}
.application p {{ margin: 0; color: #5a5a5a; font-size: .95rem; line-height: 1.75; }}
.ideal-card {{ background: #fff; border-radius: 28px; padding: 28px; border: 1px solid rgba(17,17,17,.08); box-shadow: 0 20px 50px rgba(17,17,17,.05); }}
.ideal-card h3 {{ margin: 0 0 18px; font-size: 1.2rem; color: #111; }}
.ideal-card ul {{ margin: 0; padding: 0; list-style: none; display: grid; gap: 12px; }}
.ideal-card li {{ display: flex; gap: 12px; align-items: flex-start; color: #4e4e4e; line-height: 1.7; }}
.ideal-card li::before {{ content: '•'; color: #D52B1E; font-weight: 800; margin-top: 2px; }}
.trust-row {{ display: grid; gap: 24px; grid-template-columns: 1.4fr .6fr; align-items: center; }}
.trust-copy {{ display: grid; gap: 18px; }}
.trust-copy h2 {{ margin: 0; font-size: clamp(2.3rem, 3vw, 2.9rem); line-height: 1.05; color: #111; }}
.trust-copy p {{ margin: 0; color: #4c4c4c; line-height: 1.8; font-size: 1rem; }}
.metrics {{ display: grid; gap: 18px; grid-template-columns: repeat(4, minmax(0, 1fr)); margin-top: 28px; }}
.metric {{ background: #fff; border-radius: 24px; padding: 28px; border: 1px solid rgba(17,17,17,.08); display: grid; gap: 12px; box-shadow: 0 18px 45px rgba(17,17,17,.05); }}
.metric .label {{ color: #555; font-size: .95rem; line-height: 1.6; }}
.cta-panel {{ background: #111; color: #fff; border-radius: 36px; padding: 50px 42px; display: grid; grid-template-columns: 1.45fr .55fr; gap: 36px; align-items: center; }}
.cta-panel h2 {{ margin: 0; font-size: clamp(2.4rem, 3vw, 3.1rem); line-height: 1.05; }}
.cta-panel p {{ margin: 20px 0 0; color: #d7d7d7; line-height: 1.8; max-width: 38rem; }}
.cta-panel .cta-group {{ display: flex; flex-wrap: wrap; gap: 16px; margin-top: 30px; }}
.cta-panel a {{ display: inline-flex; align-items: center; justify-content: center; padding: 16px 28px; border-radius: 999px; font-weight: 700; }}
.cta-panel a.primary {{ background: #D52B1E; color: #fff; }}
.accordion {{ margin-top: 32px; }}
.accordion-item {{ border-top: 1px solid rgba(17,17,17,.12); }}
.accordion-item button {{ width: 100%; padding: 20px 0; text-align: left; border: none; background: transparent; font-size: 1rem; font-weight: 700; color: #111; display: flex; justify-content: space-between; align-items: center; cursor: pointer; }}
.accordion-item p {{ margin: 0; padding: 0 0 22px; color: #575757; line-height: 1.8; }}
.accordion-item button::after {{ content: '+'; color: #D52B1E; font-size: 1.3rem; }}
.accordion-item button[aria-expanded='true']::after {{ content: '-'; }}
.footer {{ background: #111; color: #d8d8d8; padding: 60px 24px; }}
.footer .wrapper {{ max-width: 1280px; margin: 0 auto; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }}
.footer h3 {{ margin: 0 0 18px; color: #fff; font-size: 1rem; }}
.footer p, .footer a {{ margin: 0 0 14px; color: #d8d8d8; line-height: 1.8; font-size: .95rem; }}
.footer a:hover {{ opacity: 1; }}
@media (max-width: 1080px) {{
  .hero {{ grid-template-columns: 1fr; }}
  .split-grid, .trust-row, .cta-panel {{ grid-template-columns: 1fr; }}
  .applications {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
}}
@media (max-width: 720px) {{
  main {{ padding: 24px 18px 48px; }}
  .topbar .wrapper, .site-header .wrapper {{ padding-left: 18px; padding-right: 18px; }}
  .nav {{ gap: 14px; }}
  .hero-title {{ font-size: 2.8rem; }}
  .feature-list {{ grid-template-columns: 1fr; }}
  .applications {{ grid-template-columns: 1fr; }}
}}
  </style>
</head>
<body>
  <div class="page-shell">
    <div class="topbar">
      <div class="wrapper">
        <div class="status">
          <span>Swiss Managed</span>
          <span>Factory in Thailand</span>
          <span>Premium Quality</span>
          <span>Worldwide Shipping</span>
        </div>
        <div class="status">
          <span>+41 76 123 45 67</span>
          <span>DE | EN</span>
        </div>
      </div>
    </div>
    <header class="site-header">
      <div class="wrapper">
        <a class="brand" href="/pages/home/index.html">TShirtSwiss.ch</a>
        <nav class="nav">
          <div class="nav-dropdown">
            <a href="/pages/products/">Products</a>
            <div class="dropdown-menu">
{''.join(f'              <a href="{link}">{name}</a>\n' for name, link in (product_menu_items or []))}
            </div>
          </div>
          <a href="/pages/industries/">Industries</a>
          <a href="/pages/services/">Services</a>
          <a href="/pages/about-us/">About Us</a>
          <a href="/pages/resources/">Resources</a>
        </nav>
        <a class="cta-button" href="/pages/request-a-quote/">Request a Quote</a>
      </div>
    </header>
    <main>
      <div class="breadcrumb">
        <a href="/pages/home/index.html">Home</a>
        <span>/</span>
        <a href="/pages/products/">Products</a>
        <span>/</span>
        <span>{title}</span>
      </div>

      <section class="hero">
        <div class="hero-copy">
          <div class="hero-eyebrow">{title}</div>
          <h1 class="hero-title">{title}</h1>
          <div class="hero-subtitle">{subtitle}</div>
          <p class="hero-text">{lede}</p>
          <div class="feature-list">
{''.join(f'            <div class="feature-card"><strong>{name}</strong><span>{desc}</span></div>\n' for name, desc in feature_icons)}
          </div>
          <div class="hero-actions">
            <a class="primary" href="/pages/request-a-quote/">Request a Quote</a>
            <a class="secondary" href="/pages/contact/">Contact Us</a>
          </div>
        </div>
        <div class="hero-visual">
          <img src="https://via.placeholder.com/1080x760.png?text={hero_image_text.replace(' ', '+')}" alt="{hero_image_text} image">
        </div>
      </section>

      <section class="section section--white section--split">
        <div class="section__inner">
          <div>
            <div class="section-title"><h2>{feature_title}</h2><p>{feature_text}</p></div>
          </div>
          <div class="section-image"><img src="https://via.placeholder.com/1200x700.png?text={feature_image_text.replace(' ', '+')}" alt="{feature_image_text}"></div>
        </div>
      </section>

      <section class="section">
        <div class="section__inner">
          <div class="section-title"><h2>{process_title}</h2><p>We manage every stage of production with transparent communication, premium materials and Swiss-managed quality control.</p></div>
          <div class="process-grid">
{''.join(f'            <article class="process-step"><div class="icon">{i+1}</div><div><h3>{step[0]}</h3><p>{step[1]}</p></div></article>\n' for i, step in enumerate(process_steps))}
          </div>
        </div>
      </section>

      <section class="section section--white">
        <div class="section__inner split-grid">
          <div class="benefits-block">
            <article class="benefit-card"><h3>Premium inks & materials</h3><p>We use premium inks, fabrics and finishes that support long-term durability and sharp branding for every product.</p></article>
            <article class="benefit-card"><h3>Scalable production</h3><p>From sample runs to larger volumes, our Swiss-managed factory process supports consistent quality and reliable delivery.</p></article>
          </div>
          <div class="section-image"><img src="https://via.placeholder.com/1200x760.png?text=Premium+Materials" alt="Premium materials image"></div>
        </div>
      </section>

      <section class="section">
        <div class="section__inner split-grid">
          <div>
            <div class="section-title"><h2>One Method. Many Applications.</h2><p>Our production expertise applies to a wide range of brand applications and apparel categories.</p></div>
            <div class="applications">
{''.join(f'              <article class="application"><h3>{name}</h3><p>{desc}</p></article>\n' for name, desc in applications)}
            </div>
          </div>
          <div class="ideal-card">
            <h3>Ideal for</h3>
            <ul>
              <li>Large quantity orders</li>
              <li>Simple to complex designs</li>
              <li>Multi-color logos and artwork</li>
              <li>Bold, vibrant and durable prints</li>
              <li>Long term brand visibility</li>
            </ul>
          </div>
        </div>
      </section>

      <section class="section section--white">
        <div class="section__inner trust-row">
          <div class="trust-copy">
            <div class="section-title"><h2>Strict Quality Control At Every Step</h2><p>We follow strict quality control procedures across the entire manufacturing process. Every detail is reviewed so your product ships with the quality your brand deserves.</p></div>
            <div class="metrics">
              <div class="metric"><div class="label">Pre-production sample approval</div></div>
              <div class="metric"><div class="label">In-process quality inspections</div></div>
              <div class="metric"><div class="label">Color accuracy and consistency checks</div></div>
              <div class="metric"><div class="label">Final inspection before packing</div></div>
            </div>
          </div>
          <div class="section-image"><img src="https://via.placeholder.com/1200x760.png?text=Quality+Inspection" alt="Quality inspection"></div>
        </div>
      </section>

      <section class="section">
        <div class="section__inner">
          <div class="section-title"><h2>Sustainable Printing. Responsible Production.</h2><p>We care about people and the planet, which is why we use eco-conscious inks, reduce waste and manage production ethically.</p></div>
          <div class="applications">
{''.join(f'              <article class="application"><h3>{name}</h3><p>{desc}</p></article>\n' for name, desc in sustainability_points)}
          </div>
        </div>
      </section>

      <section class="section section--white">
        <div class="section__inner">
          <div class="section-title"><h2>Frequently Asked Questions</h2><p>Answers to the most common product and production questions.</p></div>
          <div class="accordion">
{''.join(f'            <div class="accordion-item"><button aria-expanded="false">{question}</button><p>{answer}</p></div>\n' for question, answer in faq_items)}
          </div>
        </div>
      </section>

      <section class="section">
        <div class="section__inner cta-panel">
          <div>
            <h2>Ready to make your product vision real?</h2>
            <p>Get a free quote within 24 hours and start your Swiss-managed apparel production with confidence.</p>
            <div class="cta-group">
              <a class="primary" href="/pages/request-a-quote/">Request a Quote</a>
            </div>
          </div>
          <div>
            <div class="section-image"><img src="https://via.placeholder.com/900x560.png?text=Quote+Ready" alt="Ready to quote"></div>
          </div>
        </div>
      </section>
    </main>

    <footer class="footer">
      <div class="wrapper">
        <div>
          <h3>About TShirtSwiss.ch</h3>
          <p>Swiss-managed premium apparel manufacturing in Thailand for B2B clients seeking quality, control, and global delivery.</p>
        </div>
        <div>
          <h3>Services</h3>
          <a href="/pages/production/">Production</a>
          <a href="/pages/services/">Services</a>
          <a href="/pages/request-a-quote/">Quote</a>
        </div>
        <div>
          <h3>Contact</h3>
          <p>hello@tshirtswiss.ch</p>
          <p>+41 76 123 45 67</p>
        </div>
      </div>
    </footer>
  </div>
</body>
</html>'''


def make_cards():
    return [(name, link, 'Explore details and request a quote for this product.') for name, link in page_info['index']['cards']]


if __name__ == '__main__':
    # Generate overview page
    overview_path = PRODUCTS_DIR / 'index.html'
    overview_html = generate_html(
        title=page_info['index']['title'],
        subtitle=page_info['index']['subtitle'],
        lede=page_info['index']['lede'],
        hero_image_text=page_info['index']['hero_image_text'],
        feature_title=page_info['index']['feature_title'],
        feature_text=page_info['index']['feature_text'],
        feature_image_text=page_info['index']['feature_image_text'],
        process_title='Our Product Categories',
        process_steps=[
            ('Explore categories', 'Review product categories built for Swiss businesses.'),
            ('Select your solution', 'Choose apparel or merchandise for your brand needs.'),
            ('Request a quote', 'Share your requirements and receive a fast proposal.'),
            ('Approve details', 'Confirm fabrics, artwork and delivery timing.'),
            ('Production', 'We manufacture with Swiss-managed quality control.'),
            ('Delivery', 'Receive your order on schedule with full support.')
        ],
        cards=make_cards()
    )
    overview_path.write_text(overview_html, encoding='utf-8')

    # Generate each product category page
    for folder, info in product_pages.items():
        page_dir = PRODUCTS_DIR / folder
        page_dir.mkdir(parents=True, exist_ok=True)
        page_path = page_dir / 'index.html'
        page_html = generate_html(
            title=info['title'],
            subtitle=info['subtitle'],
            lede=info['lede'],
            hero_image_text=info['hero_image_text'],
            feature_title=info['feature_title'],
            feature_text=info['feature_text'],
            feature_image_text=info['feature_image_text'],
            process_title=info['process_title'],
            process_steps=info['process_steps']
        )
        page_path.write_text(page_html, encoding='utf-8')

    print('Product pages regenerated successfully.')
