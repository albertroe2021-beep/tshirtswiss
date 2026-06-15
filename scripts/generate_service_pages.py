from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERVICES_DIR = ROOT / 'wordpress' / 'pages' / 'services'

service_pages = {
    'custom-labels': {
        'title': 'Custom Labels',
        'subtitle': 'Premium labels and woven tags for exceptional brand presentation.',
        'description': 'Create brand labels, care tags and woven finishes that elevate apparel, uniforms and promotional merchandise with a premium feel.',
        'advantage_title': 'Why Custom Labels Matter',
        'advantage_text': 'Custom labels and tags make your brand feel premium, consistent and professional. We handle material selection, print fidelity and production quality with Swiss-managed oversight.',
        'advantage_image_text': 'Custom labels',
        'premium_title': 'Premium Materials & Quality Finishes',
        'premium_text': 'We use premium woven and printed label materials that remain crisp, comfortable and durable through repeated washing and wear.',
        'left_points': [
            ('Woven labels', 'Precise woven labels with rich texture and durability.'),
            ('Printed care labels', 'Clear washing instructions and branding on soft labels.'),
            ('Size labels', 'Consistent sizing labels for ready-to-wear apparel.'),
        ],
        'right_points': [
            ('Brand identity', 'Labels that reinforce your premium brand story.'),
            ('Custom shapes', 'Unique tag shapes and trims for higher perceived value.'),
            ('Durable finish', 'Built to last in apparel production and use.'),
        ],
    },
    'embroidery': {
        'title': 'Embroidery',
        'subtitle': 'Premium stitched branding for uniforms, workwear and merchandise.',
        'description': 'Embroidery delivers a tactile, premium brand finish. We produce high-quality stitched logos and patches for apparel, caps and branded merchandise.',
        'advantage_title': 'Embroidery That Stands Out',
        'advantage_text': 'Our embroidery service combines Swiss-managed quality control with high-precision stitching for clean, long-lasting logos on textiles and garments.',
        'advantage_image_text': 'Embroidery machine',
        'premium_title': 'Premium Threads & Detailed Stitching',
        'premium_text': 'We source quality threads and offer detailed embroidery techniques for sharp branding across uniforms, jackets and promotional apparel.',
        'left_points': [
            ('Computerized embroidery', 'Precise stitching for logos, text and emblems.'),
            ('Patch creation', 'Custom embroidered patches for premium branding.'),
            ('Cap embroidery', 'Strong, clean branding for headwear and caps.'),
        ],
        'right_points': [
            ('Durability', 'Stitching designed to stand up to repeated wear.'),
            ('Color consistency', 'Thread colors matched to your brand palette.'),
            ('Professional finish', 'A premium appearance for any apparel item.'),
        ],
    },
    'hang-tags': {
        'title': 'Hang Tags',
        'subtitle': 'Premium hang tags that elevate packaging and product presence.',
        'description': 'Hang tags are a powerful branding touchpoint. We create premium tags with custom materials, print finishes and presentation details for apparel and merchandise.',
        'advantage_title': 'Hang Tags Designed for Retail Impact',
        'advantage_text': 'Our hang tags communicate quality and story while protecting the garment. We manage materials, finishing and presentation for a polished retail experience.',
        'advantage_image_text': 'Hang tags',
        'premium_title': 'Quality Materials for Brand Presentation',
        'premium_text': 'We use premium card stocks, coatings and finishing techniques to ensure every hang tag feels valuable and aligned with your brand.',
        'left_points': [
            ('Custom shapes', 'Unique tag shapes to make your brand stand out.'),
            ('Premium finishes', 'Embossing, foil and matte coatings for luxury appeal.'),
            ('Durable materials', 'Strong card stocks built for retail handling.'),
        ],
        'right_points': [
            ('Brand storytelling', 'Tag copy that communicates product quality.'),
            ('Clear information', 'Sizing, care, and material details presented cleanly.'),
            ('Retail-ready', 'Designed for shelves, racks and premium display.'),
        ],
    },
    'heat-transfer-printing': {
        'title': 'Heat Transfer Printing',
        'subtitle': 'Durable branding for textiles, sportswear and corporate apparel.',
        'description': 'Heat transfer printing offers strong, flexible graphics on a wide range of fabrics. We deliver vibrant, consistent prints with a professional finish.',
        'advantage_title': 'Heat Transfer That Performs',
        'advantage_text': 'Our heat transfer process is ideal for complex designs, color-rich graphics and flexible branding on uniforms, teamwear and promotional apparel.',
        'advantage_image_text': 'Heat transfer',
        'premium_title': 'Quality Transfers & Durable Results',
        'premium_text': 'We use premium transfer films and exact heat application to produce prints that stay bold and intact through wear and wash cycles.',
        'left_points': [
            ('Vibrant color transfers', 'Rich, accurate graphics for apparel branding.'),
            ('Flexible finishes', 'Soft-to-touch results that move with the fabric.'),
            ('Small batch support', 'Perfect for lower quantities and customized orders.'),
        ],
        'right_points': [
            ('Fast turnaround', 'Efficient setup and production for timely delivery.'),
            ('Accurate placement', 'Precise positioning for every garment.'),
            ('Suitable for many fabrics', 'Works well on cotton, blends and performance textiles.'),
        ],
    },
    'oem-clothing-production': {
        'title': 'OEM Clothing Production',
        'subtitle': 'Factory-ready manufacturing for apparel brands and private label.',
        'description': 'Our OEM service supports apparel brands with factory-managed production, materials sourcing and consistent quality control for reliable shipments.',
        'advantage_title': 'OEM Production With Swiss Oversight',
        'advantage_text': 'We manage the full manufacturing flow for OEM orders, ensuring your apparel is produced with consistent quality, accurate branding and transparent timelines.',
        'advantage_image_text': 'OEM production',
        'premium_title': 'Reliable Production, Brand-Ready Results',
        'premium_text': 'From fabric sourcing to final packing, we deliver OEM clothing production that meets premium brand standards and regulatory expectations.',
        'left_points': [
            ('Factory coordination', 'Swiss-managed production tracking and oversight.'),
            ('Fabric sourcing', 'Premium materials matched to your product specs.'),
            ('Consistent quality', 'Repeatable production for every order batch.'),
        ],
        'right_points': [
            ('Transparent communication', 'Clear updates at every production stage.'),
            ('Custom finishes', 'Labels, hang tags and packaging aligned with your brand.'),
            ('Global delivery', 'Shipping to Switzerland, Europe and beyond.'),
        ],
    },
    'packaging-solutions': {
        'title': 'Packaging Solutions',
        'subtitle': 'Premium packaging and finishing for apparel and merchandise.',
        'description': 'We design and source high-quality packaging solutions that protect products and reinforce your brand message through every customer touchpoint.',
        'advantage_title': 'Packaging That Elevates Your Brand',
        'advantage_text': 'Our packaging solutions combine sturdy materials with premium design, making every order feel polished and ready for retail or direct customer delivery.',
        'advantage_image_text': 'Packaging solutions',
        'premium_title': 'Premium Packaging & Presentation',
        'premium_text': 'From branded boxes to protective inserts, we deliver packaging solutions that look premium and keep apparel safe in transit.',
        'left_points': [
            ('Custom packaging', 'Branded boxes, bags and wrapping with a premium feel.'),
            ('Protective inserts', 'Secure packaging that preserves product quality.'),
            ('Retail-ready design', 'Presentation that supports premium brand positioning.'),
        ],
        'right_points': [
            ('Sustainable options', 'Eco-conscious materials and reduced waste.'),
            ('Order labeling', 'Clear shipping and product information for logistics.'),
            ('Quality finish', 'Sharp printing, logo placement and material feel.'),
        ],
    },
    'private-label-manufacturing': {
        'title': 'Private Label Manufacturing',
        'subtitle': 'End-to-end apparel production for your own brand line.',
        'description': 'We manage private label production from design and sampling through full manufacturing, helping brands deliver premium apparel with full control.',
        'advantage_title': 'Private Label Production Simplified',
        'advantage_text': 'Our private label service supports brand owners with complete manufacturing oversight, from materials to final packing and delivery.',
        'advantage_image_text': 'Private label',
        'premium_title': 'Complete Brand Manufacturing Support',
        'premium_text': 'We deliver private label apparel with color consistency, fit quality and premium finishing that reflect your brand identity.',
        'left_points': [
            ('Brand-focused production', 'Your brand requirements guide every product decision.'),
            ('Sample validation', 'Make sure fit and finish are exactly right before full production.'),
            ('Custom packaging', 'Brand-ready packaging and labels included.'),
        ],
        'right_points': [
            ('Flexible volumes', 'Support for small runs and larger orders.'),
            ('Premium quality control', 'Swiss-managed checks across every garment.'),
            ('Global delivery', 'Ship finished products to your markets with confidence.'),
        ],
    },
    'product-development': {
        'title': 'Product Development',
        'subtitle': 'Design and development support for premium apparel collections.',
        'description': 'We help turn apparel concepts into finished products with technical fit, fabric selection and manufacturing-ready samples.',
        'advantage_title': 'From Concept to Production',
        'advantage_text': 'Our product development service guides your apparel project from sketch to production-ready sample, ensuring quality and manufacturability.',
        'advantage_image_text': 'Product development',
        'premium_title': 'Design-Led Development & Production',
        'premium_text': 'We ensure every product is designed for premium quality, brand alignment and efficient manufacturing.',
        'left_points': [
            ('Technical design', 'Detailed patterns and specs for reliable manufacturing.'),
            ('Fabric selection', 'Choose materials that match the product performance.'),
            ('Sample creation', 'Approve prototypes before full production begins.'),
        ],
        'right_points': [
            ('Fit testing', 'Validate sizing, comfort and movement.'),
            ('Quality review', 'Check constructions and finishes before production.'),
            ('Production readiness', 'Finalize details for smooth factory execution.'),
        ],
    },
    'quality-control': {
        'title': 'Quality Control',
        'subtitle': 'Rigorous inspections and checks across every production stage.',
        'description': 'Our quality control service ensures apparel batches meet premium standards for fit, finish, color and construction.',
        'advantage_title': 'Quality You Can Trust',
        'advantage_text': 'We apply Swiss-managed quality control to every order, inspecting samples, in-process production and final goods before shipment.',
        'advantage_image_text': 'Quality control',
        'premium_title': 'Inspection & Assurance at Every Step',
        'premium_text': 'We monitor quality through sampling, production checks and final inspection to maintain consistent, premium results.',
        'left_points': [
            ('Sample approval', 'Confirm product quality before mass production.'),
            ('In-process checks', 'Inspect throughout the manufacturing cycle.'),
            ('Final inspection', 'Verify finished garments before packing.'),
        ],
        'right_points': [
            ('Color accuracy', 'Ensure prints, dyes and materials match your brand.'),
            ('Fit consistency', 'Check sizing and construction across runs.'),
            ('Packaging verification', 'Confirm orders are packed correctly for delivery.'),
        ],
    },
    'sampling': {
        'title': 'Sampling',
        'subtitle': 'Fast, accurate samples to approve fit, print and finish.',
        'description': 'Our sampling service helps you validate product designs and production details before committing to a full manufacturing run.',
        'advantage_title': 'Sample With Confidence',
        'advantage_text': 'We produce high-quality samples quickly, so you can review fit, color and construction before full production begins.',
        'advantage_image_text': 'Sampling process',
        'premium_title': 'Accurate Samples, Reliable Decisions',
        'premium_text': 'Each sample is produced with the same quality controls as full production, giving you a dependable preview of the final product.',
        'left_points': [
            ('Design proofing', 'Validate artwork, print placement and branding.'),
            ('Fit samples', 'Test sizing and comfort before production.'),
            ('Material samples', 'Confirm fabric choice and performance.'),
        ],
        'right_points': [
            ('Rapid delivery', 'Get samples delivered quickly for approval.'),
            ('Production-ready', 'Samples built with production-level quality.'),
            ('Clear feedback steps', 'Review and revise before finalizing orders.'),
        ],
    },
    'screen-printing': {
        'title': 'Screen Printing',
        'subtitle': 'High quality. Any design. Built to last.',
        'description': 'Screen printing is one of the most durable and cost-effective methods for custom apparel. It delivers vivid colors, sharp details and long-lasting results—perfect for workwear, uniforms, promotional apparel, sportswear and fashion brands.',
        'advantage_title': 'Reliable, Versatile and Perfect for Every Business',
        'advantage_text': 'Screen printing has been the industry standard for decades—and for good reason. It offers exceptional durability, vibrant color options and the ability to print on a wide range of fabrics. Whether you need bold logos on workwear, detailed designs on sportswear or large quantities for events, screen printing ensures your brand looks its best and stays that way.',
        'advantage_image_text': 'Screen printing advantage',
        'premium_title': 'Premium Inks & Quality Materials',
        'premium_text': 'We use premium plastisol and water-based inks from world-leading suppliers. Our inks are vibrant, flexible, and built to withstand heavy use, industrial washing and everyday wear.',
        'left_points': [
            ('Plastisol inks', 'Excellent opacity and color vibrancy.'),
            ('Highly durable', 'Wash resistant and long lasting.'),
            ('Ideal for workwear', 'Great for bold and solid designs.'),
        ],
        'right_points': [
            ('Water-based inks', 'Soft feel with no heavy ink build.'),
            ('Eco-friendly', 'Breathable and gentle on fabric.'),
            ('Perfect for fashion', 'Ideal for light colors and subtle prints.'),
        ],
    },
    'sublimation-printing': {
        'title': 'Sublimation Printing',
        'subtitle': 'Vibrant all-over prints for performance apparel.',
        'description': 'Sublimation printing delivers seamless, photo-quality graphics that become part of the fabric. It is ideal for sportswear, team kits and technical apparel with vibrant, long-lasting imagery.',
        'advantage_title': 'Perfect for Performance Apparel',
        'advantage_text': 'Sublimation delivers sharp, durable prints on polyester and synthetic textiles, making it ideal for activewear, sports apparel and branded garments that need a premium visual finish.',
        'advantage_image_text': 'Sublimation printing',
        'premium_title': 'High-Performance Printing Materials',
        'premium_text': 'We use premium dyes and fabrics to produce sublimation prints that resist fading, cracking and wear while maintaining dynamic color quality.',
        'left_points': [
            ('All-over prints', 'Seamless designs across the entire garment.'),
            ('Vivid colors', 'Bright, saturated imagery that lasts.'),
            ('Lightweight finish', 'Soft, breathable feel on technical fabrics.'),
        ],
        'right_points': [
            ('Performance textiles', 'Great for sportswear and active brands.'),
            ('Color durability', 'Prints hold up to repeated washing.'),
            ('High-resolution detail', 'Sharp graphics and photo-quality results.'),
        ],
    },
    'worldwide-shipping': {
        'title': 'Worldwide Shipping',
        'subtitle': 'Global delivery for apparel production and finished goods.',
        'description': 'Our shipping service moves products from Thailand to Switzerland, Europe and beyond with reliable tracking, packaging and customs support.',
        'advantage_title': 'Reliable Global Logistics',
        'advantage_text': 'We manage international shipping, customs documentation and secure transport so your apparel arrives on time and in perfect condition.',
        'advantage_image_text': 'Worldwide shipping',
        'premium_title': 'Safe Packaging & On-Time Delivery',
        'premium_text': 'We pack products carefully and coordinate logistics to ensure your order reaches its destination with minimal disruption and excellent protection.',
        'left_points': [
            ('Secure shipping', 'Packages protected for long-distance transport.'),
            ('Customs handling', 'Clear documentation for smooth cross-border delivery.'),
            ('Tracking updates', 'Transparent status updates on every shipment.'),
        ],
        'right_points': [
            ('Global partners', 'Trusted carriers across Europe and beyond.'),
            ('Fast transit', 'Optimized routes for timely delivery.'),
            ('Premium care', 'Handled with the attention your brand deserves.'),
        ],
    },
}

feature_icons = [
    ('Vibrant colors', 'Brilliant prints and rich brand color fidelity.'),
    ('Durable & long lasting', 'Built to retain quality through wear and wash.'),
    ('Cost effective', 'Reliable pricing for volume orders and quality output.'),
    ('Bulk order specialists', 'Scalable production for larger apparel runs.'),
    ('Consistent quality', 'Swiss-managed checks at every step.'),
]

applications = [
    ('Workwear & Uniforms', 'Durable apparel for teams, trade and hospitality.'),
    ('Corporate Apparel', 'Premium branded uniforms and office wear.'),
    ('Sportswear & Activewear', 'Performance clothing for teams and training.'),
    ('Promotional T-Shirts', 'Campaign and event apparel with strong branding.'),
    ('Event & Merchandise', 'Branded goods for activations and retail.'),
    ('School & University Wear', 'Team and campus apparel for institutions.'),
    ('Fashion Brands', 'Premium apparel with standout design and finish.'),
]

quality_points = [
    ('Pre-production sample approval', 'We verify every detail before full production.'),
    ('In-process quality inspections', 'Ongoing checks during manufacturing.'),
    ('Color accuracy and consistency checks', 'Colors are matched and maintained across the run.'),
    ('Final inspection before packing', 'Finished goods are reviewed before shipping.'),
]

sustainability_points = [
    ('Eco-Friendly Inks Available', 'Low-impact materials and better environmental performance.'),
    ('Reduced Water Consumption', 'Efficient processes that lower water use.'),
    ('Responsible Waste Management', 'Waste streams are minimized and managed carefully.'),
    ('Ethical Labor Practices', 'Swiss-managed oversight protects fair production.'),
]

faq_items = [
    ('What is the minimum order quantity (MOQ)?', 'Minimum quantities vary by service, but we support both smaller sample runs and larger production orders.'),
    ('How many colors can I use in my design?', 'Most services can support multiple colors, including detailed logos and artwork.'),
    ('How long does production take?', 'Production timelines depend on service type and order size, but we target fast, reliable delivery.'),
    ('What types of fabrics can be used?', 'We work with a wide range of fabrics from cotton to technical performance textiles.'),
    ('Is this service durable?', 'Yes — we focus on highly durable finishes, quality control and reliable materials.'),
    ('Can you match Pantone colors?', 'We can match Pantone colors for many print, embroidery and branding services.'),
]


def build_menu_items():
    return [
        ('Custom Labels', '/pages/services/custom-labels/'),
        ('Embroidery', '/pages/services/embroidery/'),
        ('Hang Tags', '/pages/services/hang-tags/'),
        ('Heat Transfer Printing', '/pages/services/heat-transfer-printing/'),
        ('OEM Clothing Production', '/pages/services/oem-clothing-production/'),
        ('Packaging Solutions', '/pages/services/packaging-solutions/'),
        ('Private Label Manufacturing', '/pages/services/private-label-manufacturing/'),
        ('Product Development', '/pages/services/product-development/'),
        ('Quality Control', '/pages/services/quality-control/'),
        ('Sampling', '/pages/services/sampling/'),
        ('Screen Printing', '/pages/services/screen-printing/'),
        ('Sublimation Printing', '/pages/services/sublimation-printing/'),
        ('Worldwide Shipping', '/pages/services/worldwide-shipping/'),
    ]


def create_service_html(data, product_menu_items):
    title = data['title']
    subtitle = data['subtitle']
    description = data['description']
    advantage_title = data['advantage_title']
    advantage_text = data['advantage_text']
    advantage_image_text = data['advantage_image_text']
    premium_title = data['premium_title']
    premium_text = data['premium_text']
    left_points = data['left_points']
    right_points = data['right_points']

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
.topbar .wrapper {{ max-width: 1280px; margin: 0 auto; padding: 12px 24px; display: flex; justify-content: space-between; gap: 16px; flex-wrap: wrap; align-items: center; }}
.topbar .status {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }}
.topbar .status span {{ opacity: .78; }}
.site-header {{ background: #fff; position: sticky; top: 0; z-index: 30; border-bottom: 1px solid rgba(17,17,17,.08); }}
.site-header .wrapper {{ max-width: 1280px; margin: 0 auto; padding: 22px 24px; display: flex; align-items: center; justify-content: space-between; gap: 18px; flex-wrap: wrap; }}
.brand {{ font-size: 1.05rem; font-weight: 800; letter-spacing: .18em; text-transform: uppercase; color: #111; }}
.nav {{ display: flex; gap: 24px; flex-wrap: wrap; font-size: .95rem; }}
.nav a {{ color: #111; opacity: .88; transition: opacity .2s, color .2s; }}
.nav a:hover {{ opacity: 1; color: #D52B1E; }}
.cta-button {{ padding: 14px 26px; background: #D52B1E; color: #fff; border-radius: 999px; font-weight: 700; box-shadow: 0 18px 50px rgba(213,43,30,.16); }}
main {{ flex: 1; max-width: 1280px; margin: 0 auto; padding: 36px 24px 60px; }}
.breadcrumb {{ display: flex; gap: 10px; flex-wrap: wrap; align-items: center; font-size: .92rem; color: #555; margin: 20px 0 6px; }}
.breadcrumb a {{ color: #111; opacity: .82; }}
.breadcrumb span {{ opacity: .65; }}
.hero {{ display: grid; grid-template-columns: 1.05fr .95fr; gap: 36px; align-items: center; min-height: 76vh; padding: 32px 0 40px; }}
.hero-copy {{ max-width: 620px; }}
.hero-eyebrow {{ font-size: .82rem; text-transform: uppercase; letter-spacing: .26em; color: #D52B1E; font-weight: 700; margin-bottom: 16px; }}
.hero-title {{ font-size: clamp(3.2rem, 4vw, 4.8rem); line-height: .98; margin: 0; color: #111; }}
.hero-subtitle {{ margin: 24px 0 0; font-size: 1.25rem; line-height: 1.65; color: #111; font-weight: 700; }}
.hero-text {{ margin: 28px 0 0; font-size: 1rem; line-height: 1.85; color: #4b4b4b; max-width: 40rem; }}
.icon-grid {{ display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 16px; margin-top: 28px; }}
.icon-card {{ display: flex; flex-direction: column; align-items: flex-start; gap: 10px; padding: 18px 14px; background: #fff; border: 1px solid rgba(17,17,17,.08); border-radius: 20px; }}
.icon-card .icon {{ width: 44px; height: 44px; display: grid; place-items: center; background: #F6E8E7; color: #D52B1E; border-radius: 16px; font-weight: 800; }}
.icon-card strong {{ display: block; font-size: .95rem; color: #111; }}
.icon-card span {{ display: block; color: #555; font-size: .92rem; line-height: 1.5; }}
.hero-actions {{ display: flex; flex-wrap: wrap; gap: 16px; margin-top: 32px; }}
.hero-actions a {{ display: inline-flex; align-items: center; justify-content: center; gap: 10px; padding: 15px 28px; border-radius: 999px; font-weight: 700; transition: transform .2s, box-shadow .2s; }}
.hero-actions a.primary {{ background: #D52B1E; color: #fff; }}
.hero-actions a.secondary {{ border: 1px solid rgba(17,17,17,.12); color: #111; background: #fff; }}
.hero-visual {{ border-radius: 32px; overflow: hidden; box-shadow: 0 35px 100px rgba(17,17,17,.12); }}
.hero-visual img {{ width: 100%; height: auto; }}
.section {{ padding: 72px 0; }}
.section--white {{ background: #fff; }}
.section__inner {{ display: grid; gap: 36px; max-width: 1280px; margin: 0 auto; }}
.section--split .section__inner {{ grid-template-columns: repeat(2, minmax(0, 1fr)); align-items: center; }}
.section-title {{ display: flex; flex-direction: column; gap: 18px; }}
.section-title h2 {{ margin: 0; font-size: clamp(2.4rem, 3vw, 3.2rem); line-height: 1.05; font-weight: 800; color: #111; }}
.section-title p {{ margin: 0; max-width: 44rem; color: #545454; line-height: 1.75; font-size: 1rem; }}
.section .section-image {{ border-radius: 28px; overflow: hidden; }}
.section .section-image img {{ width: 100%; height: auto; display: block; }}
.process-grid {{ display: grid; gap: 18px; grid-template-columns: repeat(3, minmax(0, 1fr)); margin-top: 28px; }}
.process-step {{ background: #fff; border: 1px solid rgba(17,17,17,.08); border-radius: 24px; padding: 24px; display: flex; gap: 18px; align-items: flex-start; box-shadow: 0 18px 45px rgba(17,17,17,.05); }}
.process-step .icon {{ min-width: 52px; min-height: 52px; border-radius: 16px; background: #F9F0EF; color: #D52B1E; display: grid; place-items: center; font-weight: 800; }}
.process-step h3 {{ margin: 0 0 10px; font-size: 1rem; font-weight: 700; color: #111; }}
.process-step p {{ margin: 0; color: #575757; line-height: 1.75; font-size: .96rem; }}
.split-grid {{ display: grid; gap: 32px; grid-template-columns: 1.4fr .6fr; align-items: center; }}
.text-block {{ display: grid; gap: 20px; }}
.text-block h3 {{ margin: 0; font-size: 1.4rem; color: #111; }}
.text-block p {{ margin: 0; color: #555; line-height: 1.85; }}
.feature-columns {{ display: grid; gap: 18px; grid-template-columns: repeat(2, minmax(0, 1fr)); margin-top: 24px; }}
.feature-card-alt {{ background: #fff; border-radius: 24px; padding: 24px; border: 1px solid rgba(17,17,17,.08); box-shadow: 0 18px 45px rgba(17,17,17,.05); }}
.feature-card-alt h3 {{ margin: 0 0 10px; font-size: 1rem; font-weight: 700; color: #111; }}
.feature-card-alt p {{ margin: 0; color: #575757; font-size: .95rem; line-height: 1.75; }}
.applications {{ display: grid; gap: 18px; grid-template-columns: repeat(4, minmax(0, 1fr)); margin-top: 28px; }}
.application {{ background: #fff; border-radius: 24px; padding: 22px; border: 1px solid rgba(17,17,17,.08); box-shadow: 0 20px 50px rgba(17,17,17,.05); display: flex; flex-direction: column; gap: 12px; }}
.application h3 {{ margin: 0; font-size: 1rem; color: #111; }}
.application p {{ margin: 0; color: #5a5a5a; font-size: .95rem; line-height: 1.75; }}
.ideal-card {{ background: #fff; border-radius: 28px; padding: 28px; border: 1px solid rgba(17,17,17,.08); box-shadow: 0 20px 50px rgba(17,17,17,.05); }}
.ideal-card h3 {{ margin: 0 0 18px; font-size: 1.2rem; color: #111; }}
.ideal-card ul {{ margin: 0; padding: 0; list-style: none; display: grid; gap: 12px; }}
.ideal-card li {{ display: flex; gap: 12px; align-items: flex-start; color: #4e4e4e; line-height: 1.7; }}
.ideal-card li::before {{ content: '•'; color: #D52B1E; font-weight: 800; margin-top: 3px; }}
.trust-row {{ display: grid; gap: 24px; grid-template-columns: 1.4fr .6fr; align-items: center; }}
.trust-copy {{ display: grid; gap: 18px; }}
.trust-copy h2 {{ margin: 0; font-size: clamp(2.3rem, 3vw, 2.9rem); line-height: 1.05; color: #111; }}
.trust-copy p {{ margin: 0; color: #4c4c4c; line-height: 1.8; font-size: 1rem; }}
.metrics {{ display: grid; gap: 18px; grid-template-columns: repeat(4, minmax(0, 1fr)); margin-top: 28px; }}
.metric {{ background: #111; color: #fff; border-radius: 24px; padding: 28px; display: grid; gap: 12px; box-shadow: 0 18px 45px rgba(17,17,17,.05); }}
.metric .label {{ color: #d7d7d7; font-size: .95rem; line-height: 1.6; }}
.sustainability {{ display: grid; gap: 18px; grid-template-columns: repeat(4, minmax(0, 1fr)); margin-top: 28px; }}
.sustainability-card {{ background: #fff; border-radius: 24px; padding: 24px; border: 1px solid rgba(17,17,17,.08); box-shadow: 0 20px 50px rgba(17,17,17,.05); text-align: center; }}
.sustainability-card strong {{ display: block; margin-bottom: 8px; font-size: 1rem; color: #111; }}
.sustainability-card p {{ margin: 0; color: #575757; line-height: 1.7; font-size: .95rem; }}
.accordion {{ margin-top: 32px; }}
.accordion-item {{ border-top: 1px solid rgba(17,17,17,.12); }}
.accordion-item button {{ width: 100%; padding: 22px 0; text-align: left; border: none; background: transparent; font-size: 1rem; font-weight: 700; color: #111; display: flex; justify-content: space-between; align-items: center; cursor: pointer; }}
.accordion-item p {{ margin: 0; padding: 0 0 22px; color: #575757; line-height: 1.8; }}
.accordion-item button::after {{ content: '+'; color: #D52B1E; font-size: 1.3rem; }}
.accordion-item button[aria-expanded='true']::after {{ content: '-'; }}
.cta-panel {{ background: #111; color: #fff; border-radius: 36px; padding: 46px 42px; display: grid; grid-template-columns: 1.4fr .6fr; gap: 34px; align-items: center; }}
.cta-panel h2 {{ margin: 0; font-size: clamp(2.3rem, 3vw, 3.1rem); line-height: 1.05; }}
.cta-panel p {{ margin: 18px 0 0; color: #d7d7d7; line-height: 1.8; max-width: 38rem; }}
.cta-group {{ display: flex; flex-wrap: wrap; gap: 16px; margin-top: 28px; }}
.cta-group a {{ display: inline-flex; align-items: center; justify-content: center; padding: 15px 28px; border-radius: 999px; font-weight: 700; }}
.cta-group a.primary {{ background: #D52B1E; color: #fff; }}
.footer {{ background: #111; color: #d8d8d8; padding: 60px 24px; }}
.footer .wrapper {{ max-width: 1280px; margin: 0 auto; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }}
.footer h3 {{ margin: 0 0 18px; color: #fff; font-size: 1rem; }}
.footer p, .footer a {{ margin: 0 0 14px; color: #d8d8d8; line-height: 1.8; font-size: .95rem; }}
.footer a:hover {{ opacity: 1; }}
@media (max-width: 1080px) {{
  .hero {{ grid-template-columns: 1fr; }}
  .section--split .section__inner,
  .split-grid,
  .trust-row,
  .cta-panel {{ grid-template-columns: 1fr; }}
  .applications {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
  .feature-columns {{ grid-template-columns: 1fr; }}
}}
@media (max-width: 720px) {{
  main {{ padding: 24px 18px 48px; }}
  .topbar .wrapper, .site-header .wrapper {{ padding-left: 18px; padding-right: 18px; }}
  .nav {{ gap: 16px; }}
  .hero-title {{ font-size: 2.8rem; }}
  .icon-grid {{ grid-template-columns: 1fr; }}
  .applications {{ grid-template-columns: 1fr; }}
  .feature-columns {{ grid-template-columns: 1fr; }}
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
          <a href="/pages/products/">Products</a>
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
        <a href="/pages/services/">Services</a>
        <span>/</span>
        <span>{title}</span>
      </div>
      <section class="hero">
        <div class="hero-copy">
          <div class="hero-eyebrow">Our Services</div>
          <h1 class="hero-title">{title}</h1>
          <div class="hero-subtitle">{subtitle}</div>
          <p class="hero-text">{description}</p>
          <div class="icon-grid">
{''.join(f'            <div class="icon-card"><div class="icon">{i+1}</div><strong>{name}</strong><span>{desc}</span></div>\n' for i, (name, desc) in enumerate(feature_icons))}
          </div>
          <div class="hero-actions">
            <a class="primary" href="/pages/request-a-quote/">Request a Quote</a>
            <a class="secondary" href="#faq">Download Service Guide</a>
          </div>
        </div>
        <div class="hero-visual">
          <img src="https://via.placeholder.com/1080x760.png?text={title.replace(' ', '+')}" alt="{title}">
        </div>
      </section>

      <section class="section section--white section--split">
        <div class="section__inner">
          <div>
            <div class="section-title"><h2>{advantage_title}</h2><p>{advantage_text}</p></div>
          </div>
          <div class="section-image"><img src="https://via.placeholder.com/1200x760.png?text={advantage_image_text.replace(' ', '+')}" alt="{advantage_image_text}"></div>
        </div>
      </section>

      <section class="section">
        <div class="section__inner">
          <div class="section-title"><h2>Our {title} Process</h2><p>We follow a clear, consistent workflow to ensure your service is delivered with premium quality and reliable timing.</p></div>
          <div class="process-grid">
{''.join(f'            <article class="process-step"><div class="icon">{i+1}</div><div><h3>{step[0]}</h3><p>{step[1]}</p></div></article>\n' for i, step in enumerate([
                ('Consultation & Artwork', 'You send us your logo or design, and we review the details to recommend the best service solution.'),
                ('Preparation', 'We prepare the artwork, materials or production setup with premium attention to quality.'),
                ('Production', 'Your service is executed with Swiss-managed manufacturing and quality oversight.'),
                ('Finishing', 'The finished product is prepared, inspected and packaged with care.'),
                ('Quality Check', 'Every item is inspected for consistency, fit, color and finish.'),
                ('Packing & Shipping', 'Your order is packed securely and shipped to Switzerland or anywhere in Europe.')
            ]))}
          </div>
        </div>
      </section>

      <section class="section section--white">
        <div class="section__inner split-grid">
          <div>
            <div class="section-title"><h2>{premium_title}</h2><p>{premium_text}</p></div>
            <div class="feature-columns">
              <article class="feature-card-alt"><h3>{left_points[0][0]}</h3><p>{left_points[0][1]}</p></article>
              <article class="feature-card-alt"><h3>{left_points[1][0]}</h3><p>{left_points[1][1]}</p></article>
            </div>
            <div class="feature-columns">
              <article class="feature-card-alt"><h3>{right_points[0][0]}</h3><p>{right_points[0][1]}</p></article>
              <article class="feature-card-alt"><h3>{right_points[1][0]}</h3><p>{right_points[1][1]}</p></article>
            </div>
          </div>
          <div class="section-image"><img src="https://via.placeholder.com/1200x760.png?text={title.replace(' ', '+')}+Materials" alt="{title} materials"></div>
        </div>
      </section>

      <section class="section">
        <div class="section__inner split-grid">
          <div>
            <div class="section-title"><h2>One Method. Many Applications.</h2><p>These service capabilities work across a wide variety of brand use cases and apparel categories.</p></div>
            <div class="applications">
{''.join(f'              <article class="application"><h3>{name}</h3><p>{desc}</p></article>\n' for name, desc in applications)}
            </div>
          </div>
          <div class="ideal-card">
            <h3>Ideal For</h3>
            <ul>
              <li>Large quantity orders</li>
              <li>Simple to complex designs</li>
              <li>Multi-color logos and artwork</li>
              <li>Bold, vibrant and durable finishes</li>
              <li>Long term brand visibility</li>
            </ul>
          </div>
        </div>
      </section>

      <section class="section section--white">
        <div class="section__inner trust-row">
          <div class="trust-copy">
            <div class="section-title"><h2>Strict Quality Control At Every Step</h2><p>We follow strict quality control procedures throughout the entire process. From sample review to final inspection, every detail matters.</p></div>
            <div class="metrics">
{''.join(f'              <div class="metric"><div class="label">{point[0]}</div></div>\n' for point in quality_points)}
            </div>
          </div>
          <div class="section-image"><img src="https://via.placeholder.com/1200x760.png?text={title.replace(' ', '+')}+Quality" alt="{title} quality"></div>
        </div>
      </section>

      <section class="section">
        <div class="section__inner">
          <div class="section-title"><h2>Our Commitment</h2><p>We care about people and the planet, which is why we use eco-friendly practices, reduce waste and follow ethical production standards.</p></div>
          <div class="sustainability">
{''.join(f'              <article class="sustainability-card"><strong>{title}</strong><p>{desc}</p></article>\n' for title, desc in sustainability_points)}
          </div>
        </div>
      </section>

      <section class="section section--white" id="faq">
        <div class="section__inner">
          <div class="section-title"><h2>{title} Questions</h2><p>Answers to the most common questions about our service and process.</p></div>
          <div class="accordion">
{''.join(f'            <div class="accordion-item"><button aria-expanded="false">{q}</button><p>{a}</p></div>\n' for q, a in faq_items)}
          </div>
        </div>
      </section>

      <section class="section">
        <div class="section__inner cta-panel">
          <div>
            <h2>Ready to print your brand?</h2>
            <p>Get a free quote within 24 hours and start your Swiss-managed service with confidence.</p>
            <div class="cta-group">
              <a class="primary" href="/pages/request-a-quote/">Request a Quote</a>
            </div>
          </div>
          <div>
            <div class="section-image"><img src="https://via.placeholder.com/900x560.png?text=Ready+to+Quote" alt="Ready to quote"></div>
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
</html>
'''


def main():
    menu_items = build_menu_items()
    for folder, data in service_pages.items():
        page_dir = SERVICES_DIR / folder
        page_dir.mkdir(parents=True, exist_ok=True)
        page_file = page_dir / 'index.html'
        page_file.write_text(create_service_html(data, menu_items), encoding='utf-8')

    print('Service pages regenerated successfully.')


if __name__ == '__main__':
    main()
