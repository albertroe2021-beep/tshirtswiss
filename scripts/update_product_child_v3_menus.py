from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
PRODUCT_ROOT = ROOT / "pages" / "products"

PRODUCT_PAGES = [
    "custom-t-shirts",
    "custom-polos",
    "hoodies-sweatshirts",
    "jackets-softshells",
    "workwear",
    "healthcare-uniforms",
    "medical-scrubs",
    "corporate-apparel",
    "sportswear",
    "rashguards",
    "mma-shorts",
    "muay-thai-shorts",
    "caps-headwear",
    "tote-bags",
    "promotional-merchandise",
    "private-label-clothing",
]

INDUSTRY_LINKS = [
    ("Construction & Trades", "../../industries/construction-trades/"),
    ("Healthcare", "../../industries/healthcare/"),
    ("Hospitality", "../../industries/hospitality/"),
    ("Sports & Fitness", "../../industries/sports-fitness/"),
    ("Combat Sports", "../../industries/combat-sports/"),
]

BUSINESS_LINKS = [
    ("Corporate Apparel", "../../industries/corporate-apparel/"),
    ("Franchises", "../../industries/franchises/"),
    ("Ecommerce Brands", "../../industries/ecommerce-brands/"),
    ("Retail Brands", "../../industries/retail-brands/"),
    ("Events & Merchandise", "../../industries/events-merchandise/"),
    ("Influencers & Creator Brands", "../../industries/influencers-creator-brands/"),
]


def links(items):
    return "".join(f'<a href="{href}">{label}</a>' for label, href in items)


def desktop_who_we_serve():
    return (
        '<div class="nav-item"><a class="nav-trigger has-dropdown" href="../../industries/">Who We Serve</a>'
        '<div class="dropdown wide serve">'
        '<div><div class="drop-title">Industries</div>' + links(INDUSTRY_LINKS) + '</div>'
        '<div><div class="drop-title">Businesses</div>' + links(BUSINESS_LINKS) + '</div>'
        '</div></div>'
    )


def mobile_who_we_serve():
    return '<details><summary>Who We Serve</summary><div class="children">' + links(INDUSTRY_LINKS + BUSINESS_LINKS) + '</div></details>'


def ensure_css(text):
    if ".dropdown.serve" not in text and ".dropdown.services" in text:
        text = text.replace(
            ".dropdown.services{min-width:560px}",
            ".dropdown.services{min-width:560px}.dropdown.serve{min-width:720px;grid-template-columns:1fr 1fr}.drop-title{padding:10px 22px 6px;font-size:11px;font-weight:900;color:var(--red);text-transform:uppercase;letter-spacing:.08em}",
        )
    return text


def update_page(path):
    text = path.read_text(encoding="utf-8")
    original = text
    text = ensure_css(text)

    text, desktop_count = re.subn(
        r'<div class="nav-item"><a class="nav-trigger has-dropdown" href="\.\./\.\./industries/">(?:Industries|Who We Serve)</a><div class="dropdown(?: wide)?">.*?</div></div><div class="nav-item"><a class="nav-trigger has-dropdown" href="\.\./\.\./services/">Services</a>',
        desktop_who_we_serve() + '<div class="nav-item"><a class="nav-trigger has-dropdown" href="../../services/">Services</a>',
        text,
        count=1,
        flags=re.S,
    )

    text, mobile_count = re.subn(
        r'<details><summary>(?:Industries|Who We Serve)</summary><div class="children">.*?</div></details><details><summary>Services</summary>',
        mobile_who_we_serve() + '<details><summary>Services</summary>',
        text,
        count=1,
        flags=re.S,
    )

    if desktop_count != 1 or mobile_count != 1:
        raise RuntimeError(f"navigation block not found cleanly: desktop={desktop_count}, mobile={mobile_count}")

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    changed = []
    for slug in PRODUCT_PAGES:
        path = PRODUCT_ROOT / slug / "index.html"
        if not path.exists():
            raise FileNotFoundError(path)
        if update_page(path):
            changed.append(slug)
    print("Updated product child menus:", ", ".join(changed) if changed else "none")


if __name__ == "__main__":
    main()
