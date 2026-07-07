from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

PAGES = {
    "pages/home/index.html": "../",
    "pages/industries/ecommerce-brands/index.html": "../../../",
    "pages/industries/retail-brands/index.html": "../../../",
    "pages/industries/education/index.html": "../../../",
}

PRODUCTS = [
    ("Custom T-Shirts", "pages/products/custom-t-shirts/"),
    ("Custom Polos", "pages/products/custom-polos/"),
    ("Hoodies &amp; Sweatshirts", "pages/products/hoodies-sweatshirts/"),
    ("Jackets &amp; Softshells", "pages/products/jackets-softshells/"),
    ("Workwear", "pages/products/workwear/"),
    ("Healthcare Uniforms", "pages/products/healthcare-uniforms/"),
    ("Medical Scrubs", "pages/products/medical-scrubs/"),
    ("Corporate Apparel", "pages/products/corporate-apparel/"),
    ("Sportswear", "pages/products/sportswear/"),
    ("Rashguards", "pages/products/rashguards/"),
    ("MMA Shorts", "pages/products/mma-shorts/"),
    ("Muay Thai Shorts", "pages/products/muay-thai-shorts/"),
    ("Caps &amp; Headwear", "pages/products/caps-headwear/"),
    ("Tote Bags", "pages/products/tote-bags/"),
    ("Promotional Merchandise", "pages/products/promotional-merchandise/"),
    ("Private Label Clothing", "pages/products/private-label-clothing/"),
]

INDUSTRIES = [
    ("Construction &amp; Trades", "pages/industries/construction-trades/"),
    ("Healthcare", "pages/industries/healthcare/"),
    ("Hospitality", "pages/industries/hospitality/"),
    ("Sports &amp; Fitness", "pages/industries/sports-fitness/"),
    ("Combat Sports", "pages/industries/combat-sports/"),
]

BUSINESSES = [
    ("Corporate Apparel", "pages/industries/corporate-apparel/"),
    ("Franchises", "pages/industries/franchises/"),
    ("Ecommerce Brands", "pages/industries/ecommerce-brands/"),
    ("Retail Brands", "pages/industries/retail-brands/"),
    ("Events &amp; Merchandise", "pages/industries/events-merchandise/"),
    ("Influencers &amp; Creator Brands", "pages/industries/influencers-creator-brands/"),
]

SERVICES = [
    ("OEM Clothing Production", "pages/services/oem-clothing-production/"),
    ("Private Label Manufacturing", "pages/services/private-label-manufacturing/"),
    ("Product Development", "pages/services/product-development/"),
    ("Sampling", "pages/services/sampling/"),
    ("Screen Printing", "pages/services/screen-printing/"),
    ("Embroidery", "pages/services/embroidery/"),
    ("Sublimation Printing", "pages/services/sublimation-printing/"),
    ("Heat Transfer Printing", "pages/services/heat-transfer-printing/"),
    ("Custom Labels", "pages/services/custom-labels/"),
    ("Hang Tags", "pages/services/hang-tags/"),
    ("Packaging Solutions", "pages/services/packaging-solutions/"),
    ("Quality Control", "pages/services/quality-control/"),
    ("Worldwide Shipping", "pages/services/worldwide-shipping/"),
]

RESOURCES = [
    ("Resources", "pages/resources/"),
    ("Blog", "pages/resources/blog/"),
    ("FAQ", "pages/resources/faq/"),
    ("Case Studies", "pages/case-studies/"),
]

ABOUT = [
    ("About Us", "pages/about-us/"),
    ("Production", "pages/production/"),
    ("Case Studies", "pages/case-studies/"),
    ("Contact", "pages/contact/"),
]

HEADER_CSS = ".dropdown.serve{min-width:720px;grid-template-columns:1fr 1fr}.drop-title{padding:10px 22px 6px;font-size:11px;font-weight:900;color:var(--red);text-transform:uppercase;letter-spacing:.08em}"


def href(base, path):
    return base + path


def links(base, items):
    return "".join(f'<a href="{href(base, path)}">{label}</a>' for label, path in items)


def header(base):
    return f'''<header class="header"><div class="wrap"><a class="logo" href="{href(base, 'v2/')}"><strong>TShirt<span>Swiss</span>.ch</strong><small>Swiss-managed apparel manufacturing</small></a><nav class="nav" aria-label="Main navigation"><div class="nav-item"><a class="nav-trigger has-dropdown" href="{href(base, 'pages/products/')}">Products</a><div class="dropdown wide">{links(base, PRODUCTS)}</div></div><div class="nav-item"><a class="nav-trigger has-dropdown" href="{href(base, 'pages/industries/')}">Who We Serve</a><div class="dropdown wide serve"><div><div class="drop-title">Industries</div>{links(base, INDUSTRIES)}</div><div><div class="drop-title">Businesses</div>{links(base, BUSINESSES)}</div></div></div><div class="nav-item"><a class="nav-trigger has-dropdown" href="{href(base, 'pages/services/')}">Services</a><div class="dropdown wide services">{links(base, SERVICES)}</div></div><div class="nav-item"><a class="nav-trigger has-dropdown" href="{href(base, 'pages/resources/')}">Resources</a><div class="dropdown">{links(base, RESOURCES)}</div></div><div class="nav-item"><a class="nav-trigger has-dropdown" href="{href(base, 'pages/about-us/')}">About Us</a><div class="dropdown">{links(base, ABOUT)}</div></div><a class="nav-trigger" href="{href(base, 'pages/contact/')}">Contact</a></nav><a class="btn" href="{href(base, 'pages/request-a-quote/')}">Request a Quote</a><button class="mobile-toggle" type="button" aria-label="Open menu" aria-controls="mobile-menu" aria-expanded="false">Menu</button></div></header>'''


def mobile(base):
    return f'''<div class="mobile-backdrop" data-mobile-close></div><aside class="mobile-panel" id="mobile-menu" aria-hidden="true"><div class="mobile-head"><strong>TShirt<span>Swiss</span>.ch</strong><button class="mobile-close" type="button" data-mobile-close>Close</button></div><div class="mobile-lang"><a href="{href(base, 'v2/')}">EN</a> | <a href="{href(base, 'de/')}">DE</a></div><nav class="mobile-menu"><details><summary>Products</summary><div class="children">{links(base, PRODUCTS)}</div></details><details><summary>Who We Serve</summary><div class="children">{links(base, INDUSTRIES + BUSINESSES)}</div></details><details><summary>Services</summary><div class="children">{links(base, SERVICES)}</div></details><details><summary>Resources</summary><div class="children">{links(base, RESOURCES)}</div></details><details><summary>About Us</summary><div class="children">{links(base, ABOUT)}</div></details><a class="mobile-direct" href="{href(base, 'pages/contact/')}">Contact</a><div class="mobile-quote"><a class="btn" href="{href(base, 'pages/request-a-quote/')}">Request a Quote</a></div></nav></aside>'''


def ensure_css(text):
    if ".dropdown.serve" not in text:
        text = text.replace("</style>", HEADER_CSS + "</style>", 1)
    return text


def replace_header_and_mobile(text, base):
    text = ensure_css(text)
    text, header_count = re.subn(r'<header class="(?:header|site-header)">.*?</header>', header(base), text, count=1, flags=re.S)
    if header_count != 1:
        raise RuntimeError(f"header replacement count {header_count}")
    text, mobile_count = re.subn(r'<div class="mobile-backdrop".*?</aside>', mobile(base), text, count=1, flags=re.S)
    if mobile_count == 0:
        # Education legacy page has no mobile menu. Insert after the header.
        text = text.replace(header(base), header(base) + "\n" + mobile(base), 1)
    return text


def main():
    changed = []
    for path_str, base in PAGES.items():
        path = ROOT / path_str
        text = path.read_text(encoding="utf-8")
        updated = replace_header_and_mobile(text, base)
        if updated != text:
            path.write_text(updated, encoding="utf-8")
            changed.append(path_str)
    print("Updated remaining menus:")
    for path in changed:
        print("-", path)


if __name__ == "__main__":
    main()
