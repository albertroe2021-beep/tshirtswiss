"""Shared V3 site header template for generated TShirtSwiss pages.

Use this module from page generators instead of hardcoding header HTML/CSS.
The helpers return project-root-relative links so the same header works from
any generated page depth on GitHub Pages.
"""

HEADER_CSS = r'''
.ts-topbar,.ts-header{font-family:Inter,Arial,Helvetica,sans-serif}.ts-topbar *,.ts-header *{box-sizing:border-box}.ts-topbar{background:#070707;color:#fff;font-size:12px;font-weight:800;text-transform:uppercase}.ts-wrap{width:min(1280px,calc(100% - 64px));margin:0 auto}.ts-topbar .ts-wrap{min-height:48px;display:flex;align-items:center;justify-content:space-between;gap:24px}.ts-top-items{display:flex;gap:26px;align-items:center;justify-content:center;flex-wrap:wrap}.ts-top-item{display:flex;align-items:center;gap:9px;color:#f1f1f1}.ts-top-ico{width:28px;height:28px;border:1px solid rgba(225,17,26,.55);border-radius:7px;background:rgba(225,17,26,.08);display:grid;place-items:center;color:#e1111a;font-weight:900}.ts-langs{display:flex;align-items:center;gap:10px;color:#fff}.ts-header{background:#fff;box-shadow:0 8px 30px rgba(0,0,0,.08);position:sticky;top:0;z-index:9999}.ts-header>.ts-wrap{min-height:108px;display:flex;align-items:center;justify-content:space-between;gap:28px}.ts-logo{text-decoration:none;color:#111;line-height:.9;font-weight:900;font-size:34px;letter-spacing:-1px;flex:0 0 auto}.ts-logo span{color:#e1111a}.ts-logo small{display:block;margin-top:9px;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:#111;font-weight:700}.ts-nav{display:flex;align-items:center;gap:24px;font-weight:900;font-size:12px;text-transform:uppercase}.ts-nav-item{position:relative}.ts-nav-trigger{display:inline-flex;align-items:center;gap:7px;padding:42px 0;color:#111!important;text-decoration:none!important;cursor:pointer}.ts-nav-trigger.has-dropdown:after{content:'v';font-size:10px;color:#e1111a}.ts-dropdown{position:absolute;top:100%;left:-22px;min-width:260px;max-height:calc(100vh - 170px);overflow:auto;background:#fff;border:1px solid #e7e7e7;box-shadow:0 24px 60px rgba(0,0,0,.16);padding:12px 0;opacity:0;visibility:hidden;transform:translateY(10px);transition:.18s ease;text-align:left;text-transform:none;z-index:120}.ts-nav-item:hover .ts-dropdown,.ts-nav-item:focus-within .ts-dropdown{opacity:1;visibility:visible;transform:translateY(0)}.ts-dropdown a{display:block;padding:10px 22px;font-size:13px;font-weight:750;line-height:1.25;color:#1d1d1d!important;text-decoration:none!important;white-space:nowrap}.ts-dropdown a:hover{background:#f7f7f7;color:#e1111a!important}.ts-dropdown.ts-wide{min-width:620px;display:grid;grid-template-columns:1fr 1fr}.ts-dropdown.ts-serve{min-width:720px}.ts-dropdown.ts-services{min-width:560px}.ts-drop-title{padding:10px 22px 6px;font-size:11px;color:#e1111a;font-weight:900;text-transform:uppercase;letter-spacing:.08em}.ts-btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;background:#e1111a;color:#fff!important;text-decoration:none!important;border:0;border-radius:4px;padding:18px 26px;font-size:12px;font-weight:900;text-transform:uppercase;box-shadow:0 14px 26px rgba(225,17,26,.25)}.ts-mobile-toggle,.ts-mobile-close{display:none;border:0;background:#111;color:#fff;border-radius:4px;padding:12px 14px;font-weight:900;text-transform:uppercase}.ts-mobile-panel,.ts-mobile-backdrop{display:none}@media(max-width:1180px){.ts-topbar{display:none}.ts-nav,.ts-header .ts-btn{display:none}.ts-mobile-toggle,.ts-mobile-close{display:inline-flex}.ts-header>.ts-wrap{min-height:84px}.ts-mobile-backdrop{display:none;position:fixed;inset:0;background:rgba(0,0,0,.45);z-index:10001}.ts-mobile-backdrop.is-open{display:block}.ts-mobile-panel{display:block;position:fixed;top:84px;right:0;bottom:0;width:min(430px,92vw);background:#fff;z-index:10002;transform:translateX(100%);transition:.22s ease;overflow:auto;box-shadow:-24px 0 60px rgba(0,0,0,.28)}.ts-mobile-panel.is-open{transform:translateX(0)}.ts-mobile-head{display:flex;align-items:center;justify-content:space-between;padding:22px;border-bottom:1px solid #e7e7e7}.ts-mobile-head strong{font-size:22px;color:#111}.ts-mobile-head span{color:#e1111a}.ts-mobile-lang{padding:16px;border-bottom:1px solid #e7e7e7;font-weight:900;text-align:center;color:#111}.ts-mobile-menu a,.ts-mobile-menu summary{display:block;padding:16px 22px;border-bottom:1px solid #e7e7e7;font-weight:900;text-transform:uppercase;color:#111!important;text-decoration:none!important;list-style:none;cursor:pointer}.ts-mobile-menu summary::-webkit-details-marker{display:none}.ts-mobile-menu .children a{font-size:14px;text-transform:none;font-weight:700;padding:10px 30px;border:0}.ts-mobile-menu a:hover{background:#f7f7f7;color:#e1111a!important}}@media(max-width:720px){.ts-wrap{width:min(100% - 32px,1280px)}.ts-logo{font-size:27px}}
'''

PRODUCT_LINKS = [
    ('Custom T-Shirts', 'pages/products/custom-t-shirts/'),
    ('Custom Polos', 'pages/products/custom-polos/'),
    ('Hoodies & Sweatshirts', 'pages/products/hoodies-sweatshirts/'),
    ('Jackets & Softshells', 'pages/products/jackets-softshells/'),
    ('Workwear', 'pages/products/workwear/'),
    ('Healthcare Uniforms', 'pages/products/healthcare-uniforms/'),
    ('Medical Scrubs', 'pages/products/medical-scrubs/'),
    ('Corporate Apparel', 'pages/products/corporate-apparel/'),
    ('Sportswear', 'pages/products/sportswear/'),
    ('Rashguards', 'pages/products/rashguards/'),
    ('MMA Shorts', 'pages/products/mma-shorts/'),
    ('Muay Thai Shorts', 'pages/products/muay-thai-shorts/'),
    ('Caps & Headwear', 'pages/products/caps-headwear/'),
    ('Tote Bags', 'pages/products/tote-bags/'),
    ('Promotional Merchandise', 'pages/products/promotional-merchandise/'),
    ('Private Label Clothing', 'pages/products/private-label-clothing/'),
]

INDUSTRY_LINKS = [
    ('Construction & Trades', 'pages/industries/construction-trades/'),
    ('Healthcare', 'pages/industries/healthcare/'),
    ('Hospitality', 'pages/industries/hospitality/'),
    ('Sports & Fitness', 'pages/industries/sports-fitness/'),
    ('Combat Sports', 'pages/industries/combat-sports/'),
]

BUSINESS_LINKS = [
    ('Corporate Apparel', 'pages/industries/corporate-apparel/'),
    ('Franchises', 'pages/industries/franchises/'),
    ('Ecommerce Brands', 'pages/industries/ecommerce-brands/'),
    ('Retail Brands', 'pages/industries/retail-brands/'),
    ('Events & Merchandise', 'pages/industries/events-merchandise/'),
    ('Influencers & Creator Brands', 'pages/industries/influencers-creator-brands/'),
]

SERVICE_LINKS = [
    ('OEM Clothing Production', 'pages/services/oem-clothing-production/'),
    ('Private Label Manufacturing', 'pages/services/private-label-manufacturing/'),
    ('Product Development', 'pages/services/product-development/'),
    ('Sampling', 'pages/services/sampling/'),
    ('Screen Printing', 'pages/services/screen-printing/'),
    ('Embroidery', 'pages/services/embroidery/'),
    ('Sublimation Printing', 'pages/services/sublimation-printing/'),
    ('Heat Transfer Printing', 'pages/services/heat-transfer-printing/'),
    ('Custom Labels', 'pages/services/custom-labels/'),
    ('Hang Tags', 'pages/services/hang-tags/'),
    ('Packaging Solutions', 'pages/services/packaging-solutions/'),
    ('Quality Control', 'pages/services/quality-control/'),
    ('Worldwide Shipping', 'pages/services/worldwide-shipping/'),
]

RESOURCE_LINKS = [
    ('Resources', 'pages/resources/'),
    ('Blog', 'pages/resources/blog/'),
    ('FAQ', 'pages/resources/faq/'),
    ('Case Studies', 'pages/case-studies/'),
]

ABOUT_LINKS = [
    ('About Us', 'pages/about-us/'),
    ('Production', 'pages/production/'),
    ('Case Studies', 'pages/case-studies/'),
    ('Contact', 'pages/contact/'),
]


def link(path, base=''):
    return f"{base}{path}"


def _dropdown(items, base='', wide=False, extra_class=''):
    classes = ['ts-dropdown']
    if wide:
        classes.append('ts-wide')
    if extra_class:
        classes.append(extra_class)
    body = ''.join(f'<a href="{link(path, base)}">{label}</a>' for label, path in items)
    return f'<div class="{" ".join(classes)}">{body}</div>'


def _serve_dropdown(base=''):
    industries = ''.join(f'<a href="{link(path, base)}">{label}</a>' for label, path in INDUSTRY_LINKS)
    businesses = ''.join(f'<a href="{link(path, base)}">{label}</a>' for label, path in BUSINESS_LINKS)
    return f'<div class="ts-dropdown ts-wide ts-serve"><div><div class="ts-drop-title">Industries</div>{industries}</div><div><div class="ts-drop-title">Businesses</div>{businesses}</div></div>'


def _mobile_group(title, items, base=''):
    body = ''.join(f'<a href="{link(path, base)}">{label}</a>' for label, path in items)
    return f'<details><summary>{title}</summary><div class="children">{body}</div></details>'


def build_header(base=''):
    mobile = ''.join([
        _mobile_group('Products', PRODUCT_LINKS, base),
        _mobile_group('Who We Serve', INDUSTRY_LINKS + BUSINESS_LINKS, base),
        _mobile_group('Services', SERVICE_LINKS, base),
        _mobile_group('Resources', RESOURCE_LINKS, base),
        _mobile_group('About Us', ABOUT_LINKS, base),
    ]) + f'<a href="{link("pages/contact/", base)}">Contact</a><a href="{link("pages/request-a-quote/", base)}">Request a Quote</a>'
    return f'''
<div class="ts-topbar"><div class="ts-wrap"><div class="ts-top-items"><div class="ts-top-item"><span class="ts-top-ico">+</span>Swiss Managed</div><div class="ts-top-item"><span class="ts-top-ico">F</span>Factory in Thailand</div><div class="ts-top-item"><span class="ts-top-ico">Q</span>Premium Quality</div><div class="ts-top-item"><span class="ts-top-ico">W</span>Worldwide Shipping</div></div><div class="ts-langs"><a href="{link('v2/', base)}">EN</a><span>|</span><a href="{link('de/', base)}">DE</a></div></div></div>
<header class="ts-header"><div class="ts-wrap"><a class="ts-logo" href="{link('v2/', base)}"><strong>TShirt<span>Swiss</span>.ch</strong><small>Swiss-managed apparel manufacturing</small></a><nav class="ts-nav" aria-label="Main navigation"><div class="ts-nav-item"><a class="ts-nav-trigger has-dropdown" href="{link('pages/products/', base)}">Products</a>{_dropdown(PRODUCT_LINKS, base, wide=True)}</div><div class="ts-nav-item"><a class="ts-nav-trigger has-dropdown" href="{link('pages/industries/', base)}">Who We Serve</a>{_serve_dropdown(base)}</div><div class="ts-nav-item"><a class="ts-nav-trigger has-dropdown" href="{link('pages/services/', base)}">Services</a>{_dropdown(SERVICE_LINKS, base, wide=True, extra_class='ts-services')}</div><div class="ts-nav-item"><a class="ts-nav-trigger has-dropdown" href="{link('pages/resources/', base)}">Resources</a>{_dropdown(RESOURCE_LINKS, base)}</div><div class="ts-nav-item"><a class="ts-nav-trigger has-dropdown" href="{link('pages/about-us/', base)}">About Us</a>{_dropdown(ABOUT_LINKS, base)}</div><a class="ts-nav-trigger" href="{link('pages/contact/', base)}">Contact</a></nav><a class="ts-btn" href="{link('pages/request-a-quote/', base)}">Request a Quote</a><button class="ts-mobile-toggle" type="button" onclick="document.body.classList.add('menu-open');document.querySelector('.ts-mobile-panel').classList.add('is-open');document.querySelector('.ts-mobile-backdrop').classList.add('is-open')">Menu</button></div><div class="ts-mobile-backdrop" onclick="document.body.classList.remove('menu-open');document.querySelector('.ts-mobile-panel').classList.remove('is-open');document.querySelector('.ts-mobile-backdrop').classList.remove('is-open')"></div><aside class="ts-mobile-panel"><div class="ts-mobile-head"><strong>TShirt<span>Swiss</span>.ch</strong><button class="ts-mobile-close" type="button" onclick="document.body.classList.remove('menu-open');document.querySelector('.ts-mobile-panel').classList.remove('is-open');document.querySelector('.ts-mobile-backdrop').classList.remove('is-open')">Close</button></div><div class="ts-mobile-lang"><a href="{link('v2/', base)}">EN</a> | <a href="{link('de/', base)}">DE</a></div><nav class="ts-mobile-menu">{mobile}</nav></aside></header>
'''


def header_style_tag():
    return f'<style id="ts-global-header-css">{HEADER_CSS}</style>'
