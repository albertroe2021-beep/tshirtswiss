#!/usr/bin/env python3
"""Apply the first approved homepage photography replacements.

This script intentionally changes only image URLs, image treatment and related
alt text. It does not alter the approved homepage layout, content or SVG maps.
"""

from pathlib import Path

PAGE = Path("pages/home/index.html")

REPLACEMENTS = {
    "https://images.unsplash.com/photo-1556905055-8f358a7a47b2?auto=format&fit=crop&w=1800&q=80":
        "https://images.pexels.com/photos/7679720/pexels-photo-7679720.jpeg?auto=compress&cs=tinysrgb&w=1800",
    "https://images.pexels.com/photos/3735218/pexels-photo-3735218.jpeg?auto=compress&cs=tinysrgb&w=1000":
        "https://images.pexels.com/photos/7679708/pexels-photo-7679708.jpeg?auto=compress&cs=tinysrgb&w=1200",
    "https://images.unsplash.com/photo-1581092335397-9583eb92d232?auto=format&fit=crop&w=1600&q=80":
        "https://images.pexels.com/photos/7679863/pexels-photo-7679863.jpeg?auto=compress&cs=tinysrgb&w=1600",
    'alt="Garment quality control"':
        'alt="Garment quality inspector reviewing finished apparel"',
}


def main() -> None:
    source = PAGE.read_text(encoding="utf-8")

    for old, new in REPLACEMENTS.items():
        if old not in source:
            raise SystemExit(f"Expected homepage source not found: {old}")
        source = source.replace(old, new, 1)

    old_cta_filter = ".cta-band::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.55),rgba(0,0,0,.96) 54%),url('https://images.pexels.com/photos/7679863/pexels-photo-7679863.jpeg?auto=compress&cs=tinysrgb&w=1600') center/cover no-repeat;filter:grayscale(1)}"
    new_cta_filter = ".cta-band::before{content:'';position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.55),rgba(0,0,0,.96) 54%),url('https://images.pexels.com/photos/7679863/pexels-photo-7679863.jpeg?auto=compress&cs=tinysrgb&w=1600') center/cover no-repeat;filter:saturate(.72) brightness(.72)}"

    if old_cta_filter not in source:
        raise SystemExit("Expected CTA image treatment was not found")
    source = source.replace(old_cta_filter, new_cta_filter, 1)

    PAGE.write_text(source, encoding="utf-8")


if __name__ == "__main__":
    main()
