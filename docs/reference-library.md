# TShirtSwiss Elementor Reference Library

This document defines the visual reference set used to reproduce the static TShirtSwiss website in Elementor Free.

## Project rules

- The GitHub Pages website is the read-only visual baseline.
- The red announcement strip above the main header is intentionally excluded.
- Unique hub and information pages are recreated individually.
- Product child pages share one design template.
- Service child pages share one design template.
- Who We Serve child pages share one design template.
- Elementor Pro Theme Builder features are not required.
- Header and footer are supplied as Elementor Free saved sections.
- Forms are implemented with WPForms Lite and documented separately from Elementor JSON.

## Reference pages

| ID | Page | Reference URL | Treatment |
|---|---|---|---|
| home | Home | https://albertroe2021-beep.github.io/tshirtswiss/pages/home/index.html | Unique page |
| products | Products Hub | https://albertroe2021-beep.github.io/tshirtswiss/pages/products/ | Unique page |
| product-child | Product Child | https://albertroe2021-beep.github.io/tshirtswiss/pages/products/custom-t-shirts/ | Shared child template |
| services | Services Hub | https://albertroe2021-beep.github.io/tshirtswiss/pages/services/ | Unique page |
| service-child | Service Child | https://albertroe2021-beep.github.io/tshirtswiss/pages/services/oem-clothing-production/ | Shared child template |
| industries | Who We Serve Hub | https://albertroe2021-beep.github.io/tshirtswiss/pages/industries/ | Unique page |
| industry-child | Who We Serve Child | Child pages under `/pages/industries/` | Shared child template |
| resources | Resources Hub | https://albertroe2021-beep.github.io/tshirtswiss/pages/resources/ | Unique page |
| about | About Us | https://albertroe2021-beep.github.io/tshirtswiss/pages/about-us/ | Unique page |
| contact | Contact | https://albertroe2021-beep.github.io/tshirtswiss/pages/contact/ | Unique page |
| blog-archive | Blog Archive | New Elementor page matching site styling | Unique page |
| blog-post | Blog Post | New Elementor page matching site styling | Unique page |

## Capture set for each reference

Each reference directory should contain:

- `desktop.png` — full-page desktop capture
- `mobile.png` — full-page mobile capture
- `sections.md` — ordered section inventory
- `design-notes.md` — typography, colour, spacing, controls and responsive behaviour
- `content-map.md` — headings, copy, links, images and icons

## Completion criteria

A page is complete only when:

1. The desktop layout matches the reference closely.
2. The mobile layout preserves the same hierarchy and content.
3. Header and footer use the agreed Free-compatible delivery method.
4. Required forms work through WPForms Lite.
5. No Elementor Pro-only widget is required.
6. Assets resolve from the packaged kit paths.
