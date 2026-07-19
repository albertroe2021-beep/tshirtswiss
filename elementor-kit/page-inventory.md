# TShirtSwiss Elementor Page Inventory

## Build principle

Every existing public HTML page will be represented in the Elementor kit. Pages are grouped by a shared template family so that repeated structure remains maintainable while page-specific copy, images, links and SEO metadata remain independent.

## Language roots

- English legacy/master routes: `/pages/`
- English mirrored routes: `/en/`
- German routes: `/de/`
- French routes: `/fr/`

The final kit will preserve the current URL intent but WordPress page slugs can be mapped during import or deployment.

## Core pages per language

- Home
- About Us
- Case Studies
- Contact
- Request a Quote
- Services overview
- Resources / Blog
- FAQ
- Production
- Under Construction

## Product page family

- Custom T-Shirts
- Custom Polos
- Hoodies and Sweatshirts
- Workwear
- Sportswear
- Uniforms
- Merchandise
- Private Label Apparel

Additional product routes found in the repository will be added to this family as conversion proceeds.

## Service page family

- Screen Printing
- Embroidery
- Sublimation Printing
- Heat Transfer Printing
- Custom Labels
- Hang Tags
- Packaging Solutions
- Sampling
- Quality Control
- Worldwide Shipping

## Industry page family

- Combat Sports
- Corporate Apparel
- Franchises
- Ecommerce Brands
- Retail Brands
- Education
- Hospitality
- Trades and Workwear
- Sports Clubs and Teams

Additional industry routes found in the repository will be added to this family as conversion proceeds.

## Shared Elementor templates

1. Site announcement / preview bar
2. Utility top bar
3. Desktop header and navigation
4. Mobile navigation
5. Quote form block using WPForms Lite
6. Standard hero
7. Hero with quote form
8. Trust / benefit strip
9. Card grid
10. Product grid
11. Industry grid
12. Process steps
13. Quality split section
14. FAQ accordion
15. CTA band
16. Footer

## Elementor Free implementation

Because Elementor Pro is not available:

- Headers and footers will be supplied as reusable saved templates and installation instructions will identify the Royal Elementor Addons header/footer mechanism.
- Forms will use WPForms Lite shortcodes.
- Repeating grids will use native containers and widgets, with Royal Elementor Addons or Ultimate Addons only where Elementor Free lacks an equivalent.
- No WooCommerce, Loop Grid, Theme Builder, dynamic tags, popup builder or Pro forms will be used.

## Conversion status

- [x] Build target and plugin constraints recorded
- [x] Global design tokens started
- [x] Page families inventoried
- [x] Shared template architecture defined
- [x] English home template conversion started
- [ ] Shared header and footer JSON
- [ ] Remaining English pages
- [ ] German pages
- [ ] French pages
- [ ] Media mapping
- [ ] Import manifest and ZIP validation
