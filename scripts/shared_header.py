"""Shared site header template for generated TShirtSwiss pages.

Use this module from page generators instead of hardcoding header HTML/CSS
inside each generator. The helpers return project-root-relative links so the
same header works from any generated page depth on GitHub Pages.
"""

HEADER_CSS = r'''
.ts-topbar,.ts-header{font-family:Inter,Arial,Helvetica,sans-serif}.ts-topbar{background:#070707;color:#fff;font-size:12px}.ts-topbar *,.ts-header *{box-sizing:border-box}.ts-wrap{width:min(1280px,calc(100% - 64px));margin:0 auto}.ts-topbar .ts-wrap{display:flex;justify-content:space-between;align-items:center;gap:22px;min-height:45px}.ts-top-items{display:flex;gap:48px;align-items:center;flex-wrap:wrap}.ts-top-item{display:flex;align-items:center;gap:10px;color:#e8e8e8}.ts-top-ico{color:#e1111a;font-weight:900}.ts-langs{display:flex;gap:10px;align-items:center;color:#f2f2f2}.ts-header{background:#fff;box-shadow:0 8px 30px rgba(0,0,0,.08);position:sticky;top:0;z-index:9999}.ts-header .ts-wrap{height:108px;display:flex;align-items:center;justify-content:space-between;gap:28px}.ts-logo{text-decoration:none;color:#111;line-height:.9;font-weight:900;font-size:34px;letter-spacing:-1.2px;flex:0 0 auto}.ts-logo span{color:#e1111a}.ts-logo small{display:block;margin-top:10px;font-size:9px;letter-spacing:.12em;text-transform:uppercase;color:#111;font-weight:700}.ts-nav{display:flex;align-items:center;gap:28px;font-weight:800;font-size:12px;text-transform:uppercase}.ts-nav-item{position:relative}.ts-nav-trigger{display:inline-flex;align-items:center;gap:8px;padding:42px 0;color:#111;text-decoration:none;cursor:pointer}.ts-nav-trigger::after{content:'⌄';font-size:12px}.ts-dropdown{position:absolute;top:100%;left:-22px;min-width:250px;background:#fff;border:1px solid rgba(17,17,17,.08);border-radius:0 0 12px 12px;box-shadow:0 26px 60px rgba(0,0,0,.16);padding:12px 0;opacity:0;visibility:hidden;transform:translateY(12px);transition:opacity .18s ease,transform .18s ease,visibility .18s ease;z-index:100;text-transform:none}.ts-nav-item:hover .ts-dropdown,.ts-nav-item:focus-within .ts-dropdown{opacity:1;visibility:visible;transform:translateY(0)}.ts-dropdown a{display:block;padding:11px 22px;font-size:13px;font-weight:750;line-height:1.25;color:#1d1d1d!important;text-decoration:none!important;white-space:nowrap}.ts-dropdown a:hover{background:#f7f7f7;color:#e1111a!important}.ts-dropdown.ts-wide{min-width:560px;display:grid;grid-template-columns:1fr 1fr;padding:12px}.ts-dropdown.ts-wide a{border-radius:6px}.ts-dropdown.ts-services{min-width:520px;grid-template-columns:1fr 1fr}.ts-btn{display:inline-flex;align-items:center;gap:12px;background:#e1111a;color:#fff!important;text-decoration:none!important;font-weight:900;text-transform:uppercase;border-radius:4px;padding:18px 26px;font-size:12px;letter-spacing:.02em;box-shadow:0 14px 26px rgba(225,17,26,.26)}.ts-mobile-toggle{display:none;background:#111;color:#fff;border:0;border-radius:4px;padding:13px 15px;font-weight:900;text-transform:uppercase}.ts-mobile-panel{display:none;background:#fff;border-top:1px solid #eee;box-shadow:0 18px 34px rgba(0,0,0,.12)}.ts-mobile-panel details{border-bottom:1px solid #eee}.ts-mobile-panel summary{cursor:pointer;list-style:none;padding:15px 22px;font-weight:900;text-transform:uppercase}.ts-mobile-panel summary::-webkit-details-marker{display:none}.ts-mobile-panel a{display:block;padding:10px 30px;color:#111!important;text-decoration:none!important;font-size:14px}.ts-mobile-panel a:hover{color:#e1111a!important;background:#f7f7f7}@media(max-width:1180px){.ts-nav{gap:18px}.ts-nav-trigger{font-size:11px}.ts-dropdown.ts-wide,.ts-dropdown.ts-services{min-width:460px}}@media(max-width:1100px){.ts-nav,.ts-header .ts-btn{display:none}.ts-mobile-toggle{display:inline-flex}.ts-header .ts-wrap{height:auto;padding:22px 0}.ts-wrap{width:min(100% - 32px,1280px)}.ts-mobile-panel.is-open{display:block}}@media(max-width:720px){.ts-topbar .ts-wrap{align-items:flex-start;flex-direction:column;padding:12px 0}.ts-top-items{gap:14px}.ts-logo{font-size:28px}}
'''

PRODUCT_LINKS = [
    ('Custom T-Shirts', 'pages/products/custom-t-shirts/'),
    ('Custom Polos', 'pages/products/custom-polos/'),
    ('Hoodies & Sweatshirts', 'pages/products/hoodies-sweatshirts/'),
    ('Workwear', 'pages/products/workwear/'),
    ('Corporate Apparel', 'pages/products/corporate-apparel/'),
    ('Private Label Clothing', 'pages/products/private-label-clothing/'),
    ('Sportswear', 'pages/products/sportswear/'),
    ('Rashguards', 'pages/products/rashguards/'),
    ('MMA Shorts', 'pages/products/mma-shorts/'),
    ('Muay Thai Shorts', 'pages/products/muay-thai-shorts/'),
    ('Healthcare Uniforms', 'pages/products/healthcare-uniforms/'),
    ('Medical Scrubs', 'pages/products/medical-scrubs/'),
    ('Caps & Headwear', 'pages/products/caps-headwear/'),
    ('Jackets & Softshells', 'pages/products/jackets-softshells/'),
    ('Tote Bags', 'pages/products/tote-bags/'),
    ('Promotional Merchandise', 'pages/products/promotional-merchandise/'),
]

INDUSTRY_LINKS = [
    ('Construction & Trades', 'pages/industries/construction-trades/'),
    ('Healthcare', 'pages/industries/healthcare/'),
    ('Hospitality', 'pages/industries/hospitality/'),
    ('Sports & Fitness', 'pages/industries/sports-fitness/'),
    ('Combat Sports', 'pages/industries/combat-sports/'),
    ('Corporate Apparel', 'pages/industries/corporate-apparel/'),
    ('Events & Merchandise', 'pages/industries/events-merchandise/'),
    ('Ecommerce Brands', 'pages/industries/ecommerce-brands/'),
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

ABOUT_LINKS = [
    ('About Us', 'pages/about-us/'),
    ('Our Process', 'pages/production/'),
    ('Case Studies', 'pages/case-studies/'),
    ('Contact Us', 'pages/contact/'),
    ('Request a Quote', 'pages/request-a-quote/'),
]

RESOURCE_LINKS = [
    ('Resources Hub', 'pages/resources/'),
    ('Blog', 'pages/resources/blog/'),
    ('FAQ', 'pages/resources/faq/'),
    ('Case Studies', 'pages/case-studies/'),
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


def _mobile_group(title, items, base=''):
    body = ''.join(f'<a href="{link(path, base)}">{label}</a>' for label, path in items)
    return f'<details><summary>{title}</summary>{body}</details>'


def build_header(base=''):
    mobile = ''.join([
        _mobile_group('Products', PRODUCT_LINKS, base),
        _mobile_group('Industries', INDUSTRY_LINKS, base),
        _mobile_group('Services', SERVICE_LINKS, base),
        _mobile_group('About Us', ABOUT_LINKS, base),
        _mobile_group('Resources', RESOURCE_LINKS, base),
    ]) + f'<a href="{link("pages/request-a-quote/", base)}">Request a Quote</a>'
    return f'''
<div class="ts-topbar"><div class="ts-wrap"><div class="ts-top-items"><div class="ts-top-item"><span class="ts-top-ico">✚</span>Swiss Management</div><div class="ts-top-item"><span class="ts-top-ico">▣</span>Factory in Thailand</div><div class="ts-top-item"><span class="ts-top-ico">♡</span>Premium Quality</div><div class="ts-top-item"><span class="ts-top-ico">▱</span>Worldwide Shipping</div></div><div class="ts-langs"><span>DE</span><span>|</span><span>EN</span><span>⌄</span></div></div></div>
<header class="ts-header"><div class="ts-wrap"><a class="ts-logo" href="{link('', base)}"><strong>TShirt<span>Swiss</span>.ch</strong><small>Swiss-managed apparel manufacturing</small></a><nav class="ts-nav" aria-label="Main navigation"><div class="ts-nav-item"><a class="ts-nav-trigger" href="{link('pages/products/', base)}">Products</a>{_dropdown(PRODUCT_LINKS, base, wide=True)}</div><div class="ts-nav-item"><a class="ts-nav-trigger" href="{link('pages/industries/', base)}">Industries</a>{_dropdown(INDUSTRY_LINKS, base)}</div><div class="ts-nav-item"><a class="ts-nav-trigger" href="{link('pages/services/', base)}">Services</a>{_dropdown(SERVICE_LINKS, base, wide=True, extra_class='ts-services')}</div><div class="ts-nav-item"><a class="ts-nav-trigger" href="{link('pages/about-us/', base)}">About Us</a>{_dropdown(ABOUT_LINKS, base)}</div><div class="ts-nav-item"><a class="ts-nav-trigger" href="{link('pages/resources/', base)}">Resources</a>{_dropdown(RESOURCE_LINKS, base)}</div></nav><a class="ts-btn" href="{link('pages/request-a-quote/', base)}">Request a Quote</a><button class="ts-mobile-toggle" type="button" onclick="document.querySelector('.ts-mobile-panel').classList.toggle('is-open')">Menu</button></div><div class="ts-mobile-panel">{mobile}</div></header>
'''


def header_style_tag():
    return f'<style id="ts-global-header-css">{HEADER_CSS}</style>'
