# Page Inventory and Navigation Map

This document is the working navigation blueprint for TShirtSwiss v2.

It is based on the repository structure and existing project mapping files, not on assumptions.

## Sources checked

- `WEBSITE_PAGE_MAP.md`
- `scripts/shared_header.py`
- Verified page paths in `pages/`

## Migration principle

The GitHub HTML preview is the design prototype. WordPress and Elementor will become the long-term content management platform.

That means this map should be easy to recreate using:

- WordPress Pages
- WordPress Menus
- Elementor Theme Builder
- Elementor Header and Footer templates
- Elementor global colours and typography

No navigation design should require future code editing for normal content updates.

---

# Top-Level Navigation

## Header

1. Products
2. Industries
3. Services
4. Resources
5. About Us
6. Contact
7. Request a Quote

## CTA

Primary CTA: Request a Quote

Recommended URL in HTML preview: `/pages/request-a-quote/`

Recommended WordPress URL after migration: `/request-a-quote/`

---

# Main Pages

| Section | Title | Repository Path | WordPress URL | Header Role |
|---|---|---|---|---|
| Home | Home | `pages/home/index.html` | `/` | Logo/home |
| Products | Products | `pages/products/index.html` | `/products/` | Top-level menu |
| Industries | Industries | `pages/industries/index.html` | `/industries/` | Top-level menu |
| Services | Services | `pages/services/index.html` | `/services/` | Top-level menu |
| About | About Us | `pages/about-us/index.html` | `/about-us/` | Top-level menu |
| Production | Production | `pages/production/index.html` | `/production/` | About menu child |
| Case Studies | Case Studies | `pages/case-studies/index.html` | `/case-studies/` | Resources/About child |
| Resources | Resources | `pages/resources/index.html` | `/resources/` | Top-level menu |
| Blog | Blog | `pages/resources/blog/index.html` | `/resources/blog/` | Resources child |
| FAQ | FAQ | `pages/resources/faq/index.html` | `/resources/faq/` | Resources child |
| Request a Quote | Request a Quote | `pages/request-a-quote/index.html` | `/request-a-quote/` | Primary CTA |
| Contact | Contact | `pages/contact/index.html` | `/contact/` | Top-level menu |

---

# Products Menu

Rule: Products contains only pages under `pages/products/`.

| Menu Label | Repository Path | WordPress URL | Status |
|---|---|---|---|
| Custom T-Shirts | `pages/products/custom-t-shirts/index.html` | `/products/custom-t-shirts/` | Include |
| Custom Polos | `pages/products/custom-polos/index.html` | `/products/custom-polos/` | Include |
| Hoodies & Sweatshirts | `pages/products/hoodies-sweatshirts/index.html` | `/products/hoodies-sweatshirts/` | Include |
| Jackets & Softshells | `pages/products/jackets-softshells/index.html` | `/products/jackets-softshells/` | Include |
| Workwear | `pages/products/workwear/index.html` | `/products/workwear/` | Include |
| Healthcare Uniforms | `pages/products/healthcare-uniforms/index.html` | `/products/healthcare-uniforms/` | Include |
| Medical Scrubs | `pages/products/medical-scrubs/index.html` | `/products/medical-scrubs/` | Include |
| Corporate Apparel | `pages/products/corporate-apparel/index.html` | `/products/corporate-apparel/` | Include |
| Sportswear | `pages/products/sportswear/index.html` | `/products/sportswear/` | Include |
| Rashguards | `pages/products/rashguards/index.html` | `/products/rashguards/` | Include |
| MMA Shorts | `pages/products/mma-shorts/index.html` | `/products/mma-shorts/` | Include |
| Muay Thai Shorts | `pages/products/muay-thai-shorts/index.html` | `/products/muay-thai-shorts/` | Include |
| Caps & Headwear | `pages/products/caps-headwear/index.html` | `/products/caps-headwear/` | Include |
| Tote Bags | `pages/products/tote-bags/index.html` | `/products/tote-bags/` | Include |
| Promotional Merchandise | `pages/products/promotional-merchandise/index.html` | `/products/promotional-merchandise/` | Include |
| Private Label Clothing | `pages/products/private-label-clothing/index.html` | `/products/private-label-clothing/` | Include |

## Products mega menu presentation draft

This grouping is for visual presentation only. It does not change page hierarchy.

### Core Apparel

- Custom T-Shirts
- Custom Polos
- Hoodies & Sweatshirts
- Jackets & Softshells

### Work & Professional

- Workwear
- Healthcare Uniforms
- Medical Scrubs
- Corporate Apparel

### Sports & Performance

- Sportswear
- Rashguards
- MMA Shorts
- Muay Thai Shorts

### Accessories & Brand Support

- Caps & Headwear
- Tote Bags
- Promotional Merchandise
- Private Label Clothing

---

# Industries Menu

Rule: Industries contains only pages under `pages/industries/`.

| Menu Label | Repository Path | WordPress URL | Status |
|---|---|---|---|
| Construction & Trades | `pages/industries/construction-trades/index.html` | `/industries/construction-trades/` | Include |
| Healthcare | `pages/industries/healthcare/index.html` | `/industries/healthcare/` | Include |
| Hospitality | `pages/industries/hospitality/index.html` | `/industries/hospitality/` | Include |
| Sports & Fitness | `pages/industries/sports-fitness/index.html` | `/industries/sports-fitness/` | Include |
| Combat Sports | `pages/industries/combat-sports/index.html` | `/industries/combat-sports/` | Include |
| Corporate Apparel | `pages/industries/corporate-apparel/index.html` | `/industries/corporate-apparel/` | Include |
| Events & Merchandise | `pages/industries/events-merchandise/index.html` | `/industries/events-merchandise/` | Include |
| Ecommerce Brands | `pages/industries/ecommerce-brands/index.html` | `/industries/ecommerce-brands/` | Include |
| Influencers & Creator Brands | `pages/industries/influencers-creator-brands/index.html` | `/industries/influencers-creator-brands/` | Include |

## Industries mega menu presentation draft

### Business & Organisations

- Corporate Apparel
- Events & Merchandise
- Ecommerce Brands
- Influencers & Creator Brands

### Specialist Sectors

- Construction & Trades
- Healthcare
- Hospitality

### Sport & Active

- Sports & Fitness
- Combat Sports

---

# Services Menu

Rule: Services contains only pages under `pages/services/`.

| Menu Label | Repository Path | WordPress URL | Status |
|---|---|---|---|
| OEM Clothing Production | `pages/services/oem-clothing-production/index.html` | `/services/oem-clothing-production/` | Include |
| Private Label Manufacturing | `pages/services/private-label-manufacturing/index.html` | `/services/private-label-manufacturing/` | Include |
| Product Development | `pages/services/product-development/index.html` | `/services/product-development/` | Include |
| Sampling | `pages/services/sampling/index.html` | `/services/sampling/` | Include |
| Screen Printing | `pages/services/screen-printing/index.html` | `/services/screen-printing/` | Include |
| Embroidery | `pages/services/embroidery/index.html` | `/services/embroidery/` | Include |
| Sublimation Printing | `pages/services/sublimation-printing/index.html` | `/services/sublimation-printing/` | Include |
| Heat Transfer Printing | `pages/services/heat-transfer-printing/index.html` | `/services/heat-transfer-printing/` | Include |
| Custom Labels | `pages/services/custom-labels/index.html` | `/services/custom-labels/` | Include |
| Hang Tags | `pages/services/hang-tags/index.html` | `/services/hang-tags/` | Include |
| Packaging Solutions | `pages/services/packaging-solutions/index.html` | `/services/packaging-solutions/` | Include |
| Quality Control | `pages/services/quality-control/index.html` | `/services/quality-control/` | Include |
| Worldwide Shipping | `pages/services/worldwide-shipping/index.html` | `/services/worldwide-shipping/` | Include |

## Services mega menu presentation draft

### Production Planning

- Product Development
- Sampling
- OEM Clothing Production
- Private Label Manufacturing

### Branding & Decoration

- Screen Printing
- Embroidery
- Sublimation Printing
- Heat Transfer Printing

### Finishing & Delivery

- Custom Labels
- Hang Tags
- Packaging Solutions
- Quality Control
- Worldwide Shipping

---

# Resources Menu

Rule: Resources contains only resource/support pages. Case Studies may appear here as a resource-style page even though its repository path is top-level.

| Menu Label | Repository Path | WordPress URL | Status |
|---|---|---|---|
| Resources Hub | `pages/resources/index.html` | `/resources/` | Include |
| Blog | `pages/resources/blog/index.html` | `/resources/blog/` | Include |
| FAQ | `pages/resources/faq/index.html` | `/resources/faq/` | Include |
| Case Studies | `pages/case-studies/index.html` | `/case-studies/` | Include |

---

# About Menu

| Menu Label | Repository Path | WordPress URL | Status |
|---|---|---|---|
| About Us | `pages/about-us/index.html` | `/about-us/` | Include |
| Our Process / Production | `pages/production/index.html` | `/production/` | Include |
| Case Studies | `pages/case-studies/index.html` | `/case-studies/` | Optional duplicate with Resources |
| Contact Us | `pages/contact/index.html` | `/contact/` | Include |
| Request a Quote | `pages/request-a-quote/index.html` | `/request-a-quote/` | Include as CTA |

---

# Elementor Build Notes

## Recommended WordPress setup

- Create WordPress pages matching the final approved URL structure.
- Use WordPress Menus for Products, Industries, Services, Resources and About.
- Use Elementor Theme Builder for one global header and one global footer.
- Use Elementor containers for the mega menu layouts.
- Keep the visual grouping inside Elementor editable by the site owner.
- Do not rely on generated JSON or code-controlled menus after migration.

## Header/mega menu requirements

- Every child page remains editable through WordPress menus.
- The visual grouping can be recreated as Elementor columns/containers.
- The desktop and mobile menu must use the same WordPress menu items.
- Mobile menu must expose all child pages clearly.
- Request a Quote remains a persistent CTA.

---

# Open Checks

These need confirmation before locking the navigation:

1. Confirm whether Case Studies should appear under both Resources and About, or only Resources.
2. Confirm whether Production should be labelled `Production`, `Our Process`, or `How Production Works`.
3. Confirm whether Contact should be top-level only, or also inside About.
4. Confirm whether the WordPress URLs should be root-relative without `/pages/` after migration.
5. Confirm whether German navigation will be handled through WPML menus.
