# TShirtSwiss v2 Image Replacement Register

Purpose: turn the full-site image audit into an implementation-ready register for reviewing, sourcing, approving and replacing imagery across the English-language website.

Reference website: `https://albertroe2021-beep.github.io/tshirtswiss/v2/`

Related documents:

- `v2/docs/FULL_SITE_IMAGE_AUDIT.md`
- `v2/docs/PAGE_INVENTORY_NAVIGATION_MAP.md`

## Status key

| Status | Meaning |
|---|---|
| Audit required | Current image source and crop still need to be recorded from the live page source. |
| Replace | Current image is generic, repeated, off-topic or insufficiently specific. |
| Review | Image may be usable but needs a visual and mobile-crop check. |
| Keep | Image is relevant, technically suitable and approved. |
| Sourced | Replacement candidate has been selected but not implemented. |
| Implemented | Replacement has been added to the page. |
| Approved | Desktop, tablet and mobile presentation has been signed off. |

## Image standards

- Hero images must identify the page topic immediately.
- Product pages must show the exact product, not just a general lifestyle or factory scene.
- Industry pages must show the relevant people wearing the garments in the correct environment.
- Service pages must show the actual process, machinery, material or production action.
- Avoid repeating the same generic office, factory, shipping or fashion image across unrelated pages.
- Use landscape images with useful negative space for hero copy.
- Check all crops at desktop, tablet and mobile widths before approval.
- Use page-specific alt text rather than generic descriptions such as `factory`, `team` or `clothing`.
- Prefer authentic factory, product and customer-context imagery over broad stock photography.
- Keep image treatment consistent: neutral colour temperature, premium B2B styling, controlled contrast and natural skin tones.

## Recommended aspect ratios

| Placement | Preferred ratio | Minimum working size |
|---|---:|---:|
| Full-width hero background | 16:9 or 2:1 | 1800 x 900 px |
| Split-section image | 4:3 | 1200 x 900 px |
| Gallery card | 4:3 | 900 x 675 px |
| Product/detail card | 1:1 or 4:3 | 800 x 800 px |
| CTA background | 2:1 | 1600 x 800 px |
| Blog thumbnail | 16:9 | 1200 x 675 px |

---

# A. Main and Supporting Pages

| ID | Page | URL / repository path | Image position | Current image/source | Audit decision | Replacement brief | Preferred ratio | Suggested alt text | Priority | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| M-001 | Home | `pages/home/index.html` | Hero background | Record during source audit | Replace | Premium garment-production environment with finished branded apparel in the foreground and useful negative space for headline text. | 2:1 | Premium branded apparel production managed for Swiss businesses | Critical | Audit required |
| M-002 | Home | `pages/home/index.html` | Product/category overview | Record during source audit | Replace/review | Coordinated collection of T-shirts, polos, hoodies, workwear, sportswear and caps photographed consistently. | 16:9 | Custom apparel product range for businesses, teams and brands | High | Audit required |
| M-003 | Home | `pages/home/index.html` | Manufacturing/process section | Record during source audit | Replace/review | Documentary production scene showing cutting, sewing or garment inspection rather than a generic factory exterior. | 4:3 | Garment production and quality inspection in Thailand | High | Audit required |
| M-004 | Home | `pages/home/index.html` | Quality/Swiss-management section | Record during source audit | Review | Production manager or quality specialist reviewing a finished garment, measurements or colour standards. | 4:3 | Swiss-managed quality review of a finished garment | High | Audit required |
| M-005 | Home | `pages/home/index.html` | CTA background | Record during source audit | Replace | Folded finished garments, branded labels and packed cartons prepared for delivery. Keep background visually quiet. | 2:1 | Finished custom garments prepared for international delivery | Medium | Audit required |
| M-006 | Products | `pages/products/index.html` | Hero background | Record during source audit | Replace | Curated product-family overview containing multiple apparel categories without looking like a consumer fashion catalogue. | 2:1 | Custom apparel product categories manufactured for Swiss businesses | High | Audit required |
| M-007 | Products | `pages/products/index.html` | Product category cards | Record during source audit | Replace/review | Each card must show its actual category: tee, polo, hoodie, jacket, workwear, scrubs, sportswear, fightwear, cap, tote and private label. | 4:3 | Page-specific category alt text | Critical | Audit required |
| M-008 | Industries | `pages/industries/index.html` | Hero background | Record during source audit | Replace | Cross-industry team composition featuring construction, healthcare, hospitality, sports and corporate apparel. | 2:1 | Branded uniforms and apparel for multiple industries | High | Audit required |
| M-009 | Industries | `pages/industries/index.html` | Industry cards | Record during source audit | Replace/review | Use environment-specific images with apparel clearly visible; avoid buildings, equipment or rooms without people wearing the products. | 4:3 | Page-specific industry alt text | Critical | Audit required |
| M-010 | Services | `pages/services/index.html` | Hero background | Record during source audit | Replace | Apparel production workflow featuring fabric preparation, sewing, decoration, inspection and packing. | 2:1 | End-to-end custom clothing manufacturing services | High | Audit required |
| M-011 | Services | `pages/services/index.html` | Service cards | Record during source audit | Replace/review | Each card must show the exact production service rather than a repeated generic factory photograph. | 4:3 | Page-specific service alt text | Critical | Audit required |
| M-012 | About Us | `pages/about-us/index.html` | Hero background | Record during source audit | Replace | Authentic management and factory-team interaction; avoid generic boardroom imagery. | 2:1 | TShirtSwiss management and garment production team | High | Audit required |
| M-013 | About Us | `pages/about-us/index.html` | Swiss/Thailand story section | Record during source audit | Replace/review | Project coordination or quality review linking Swiss management with Thai manufacturing capability. | 4:3 | Swiss-managed apparel production in Thailand | High | Audit required |
| M-014 | Production | `pages/production/index.html` | Hero background | Record during source audit | Replace | Active apparel production floor with garments visibly being cut, sewn or assembled. | 2:1 | Custom garment production floor in Thailand | Critical | Audit required |
| M-015 | Production | `pages/production/index.html` | Process imagery | Record during source audit | Replace | Chronological image set: fabric inspection, pattern/cutting, sewing, decoration, QC, packing and dispatch. | 4:3 | Page-specific production-step alt text | Critical | Audit required |
| M-016 | Case Studies | `pages/case-studies/index.html` | Hero background | Record during source audit | Replace | Finished branded apparel collection or project presentation rather than a generic meeting. | 2:1 | Completed custom apparel manufacturing projects | High | Audit required |
| M-017 | Case Studies | `pages/case-studies/index.html` | Case-study cards | Record during source audit | Replace | Project-specific outcome images: uniforms in use, product collections, branding details and packaging. | 4:3 | Page-specific project outcome alt text | High | Audit required |
| M-018 | Resources | `pages/resources/index.html` | Hero/support image | Record during source audit | Replace/review | Fabric swatches, garment sample, specification sheet and production-planning materials. | 16:9 | Apparel manufacturing guides and planning resources | Medium | Audit required |
| M-019 | Blog | `pages/resources/blog/index.html` | Hero image | Record during source audit | Review | Editorial apparel-development scene that supports educational content without appearing like a generic office blog. | 16:9 | Apparel manufacturing articles and practical guides | Medium | Audit required |
| M-020 | Blog | `pages/resources/blog/index.html` | Article thumbnails | Record during source audit | Replace/review | Assign distinct imagery by topic: materials, print, embroidery, product development, quality control, packaging and shipping. | 16:9 | Article-specific descriptive alt text | Medium | Audit required |
| M-021 | FAQ | `pages/resources/faq/index.html` | Hero/support image | Record during source audit | Review/remove | Prefer one restrained sample-review or consultation image. Remove decorative stock images that add no information. | 16:9 | Reviewing garment samples and production requirements | Low | Audit required |
| M-022 | Request a Quote | `pages/request-a-quote/index.html` | Hero/form background | Record during source audit | Replace | Garment samples, fabric swatches, colour references and measurement sheet on a clean worktable. | 2:1 | Garment samples and materials prepared for a custom clothing quote | Medium | Audit required |
| M-023 | Contact | `pages/contact/index.html` | Hero/support image | Record during source audit | Replace/review | Account manager reviewing garment samples with a business client or factory team. | 16:9 | TShirtSwiss apparel production consultation | Medium | Audit required |

---

# B. Product Pages

For each product page, audit the hero, gallery, manufacturing image, detail image and CTA background separately.

| ID | Product page | URL / repository path | Image position | Current image/source | Audit decision | Replacement brief | Preferred ratio | Suggested alt text | Priority | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| P-001 | Custom T-Shirts | `pages/products/custom-t-shirts/index.html` | Hero | Unsplash fashion/apparel image currently used in CSS | Replace | Branded custom T-shirts clearly visible on models or in a clean product arrangement; leave text-safe space. | 2:1 | Custom printed T-shirts manufactured for Swiss businesses and brands | Critical | Replace |
| P-002 | Custom T-Shirts | `pages/products/custom-t-shirts/index.html` | Product gallery | Record during source audit | Replace/review | Three distinct views: premium blank/fabric, printed team or event shirts, folded retail-ready shirts. | 4:3 | Custom T-shirt product and print examples | High | Audit required |
| P-003 | Custom T-Shirts | `pages/products/custom-t-shirts/index.html` | Production/split image | Record during source audit | Replace/review | Screen printing or garment production specifically involving T-shirts. | 4:3 | Screen printing a custom T-shirt | High | Audit required |
| P-004 | Custom T-Shirts | `pages/products/custom-t-shirts/index.html` | CTA background | Generic industrial Unsplash image currently used in CSS | Replace | Folded printed T-shirts, labels and packed order; avoid unrelated machinery. | 2:1 | Finished custom T-shirts prepared for delivery | High | Replace |
| P-005 | Custom Polos | `pages/products/custom-polos/index.html` | Hero | Record during source audit | Replace/review | Corporate or hospitality staff wearing premium embroidered polos with garments clearly visible. | 2:1 | Custom embroidered polos for corporate and hospitality teams | High | Audit required |
| P-006 | Custom Polos | `pages/products/custom-polos/index.html` | Gallery/detail | Record during source audit | Replace/review | Polo collar, placket, embroidery close-up, colour range and folded finished product. | 4:3 | Custom polo collar, fabric and embroidered logo details | High | Audit required |
| P-007 | Hoodies & Sweatshirts | `pages/products/hoodies-sweatshirts/index.html` | Hero | Record during source audit | Replace/review | Premium branded hoodie or crew sweatshirt in a lifestyle or retail-brand context. | 2:1 | Custom hoodies and sweatshirts for teams and merchandise brands | High | Audit required |
| P-008 | Hoodies & Sweatshirts | `pages/products/hoodies-sweatshirts/index.html` | Gallery/detail | Record during source audit | Replace/review | Fleece interior, print/embroidery, neck label, folded stack and ecommerce packaging. | 4:3 | Branded hoodie fabric, printing and label details | High | Audit required |
| P-009 | Jackets & Softshells | `pages/products/jackets-softshells/index.html` | Hero | Record during source audit | Replace/review | Branded technical softshell or jacket worn outdoors by a team. | 2:1 | Branded jackets and softshells for corporate and outdoor teams | High | Audit required |
| P-010 | Jackets & Softshells | `pages/products/jackets-softshells/index.html` | Gallery/detail | Record during source audit | Replace/review | Zips, shell fabric, seam construction, embroidery and weather-resistant garment details. | 4:3 | Custom softshell jacket construction and branding details | High | Audit required |
| P-011 | Workwear | `pages/products/workwear/index.html` | Hero | Record during source audit | Replace | Tradespeople wearing coordinated, clearly branded workwear in an authentic work environment. | 2:1 | Durable branded workwear for construction and trade teams | Critical | Audit required |
| P-012 | Workwear | `pages/products/workwear/index.html` | Gallery/detail | Record during source audit | Replace/review | Reinforced seams, utility pockets, embroidery, durable fabric and coordinated team garments. | 4:3 | Workwear pockets, reinforced stitching and embroidered branding | High | Audit required |
| P-013 | Healthcare Uniforms | `pages/products/healthcare-uniforms/index.html` | Hero | Record during source audit | Replace | Coordinated healthcare team wearing professional uniforms; garments must be the focal point. | 2:1 | Custom healthcare uniforms for clinic and care teams | Critical | Audit required |
| P-014 | Healthcare Uniforms | `pages/products/healthcare-uniforms/index.html` | Gallery/detail | Record during source audit | Replace/review | Easy-care fabric, pockets, logo embroidery, fit options and colour range. | 4:3 | Healthcare uniform fabric, pocket and embroidered logo details | High | Audit required |
| P-015 | Medical Scrubs | `pages/products/medical-scrubs/index.html` | Hero | Record during source audit | Replace | Doctors, nurses or clinic staff wearing modern scrub sets in an authentic clinical environment. | 2:1 | Custom medical scrubs for healthcare professionals | Critical | Audit required |
| P-016 | Medical Scrubs | `pages/products/medical-scrubs/index.html` | Gallery/detail | Record during source audit | Replace/review | Scrub pockets, stretch fabric, stitching, embroidered names/logos and multiple fits. | 4:3 | Medical scrub fabric, pocket and branding details | High | Audit required |
| P-017 | Corporate Apparel | `pages/products/corporate-apparel/index.html` | Hero | Record during source audit | Replace | Professional team wearing coordinated shirts, polos, jackets or knitwear; avoid generic meeting rooms. | 2:1 | Coordinated custom corporate apparel for business teams | High | Audit required |
| P-018 | Corporate Apparel | `pages/products/corporate-apparel/index.html` | Gallery/detail | Record during source audit | Replace/review | Uniform combinations, logo placement, embroidery, outerwear and colour matching. | 4:3 | Corporate uniform combinations and embroidered branding | High | Audit required |
| P-019 | Sportswear | `pages/products/sportswear/index.html` | Hero | Record during source audit | Replace/review | Athlete or team wearing a custom performance kit with apparel clearly visible in motion. | 2:1 | Custom performance sportswear for teams and fitness brands | High | Audit required |
| P-020 | Sportswear | `pages/products/sportswear/index.html` | Gallery/detail | Record during source audit | Replace/review | Moisture-wicking fabric, sublimated graphics, stretch panels and complete team kit. | 4:3 | Performance sportswear fabric and sublimated team graphics | High | Audit required |
| P-021 | Rashguards | `pages/products/rashguards/index.html` | Hero | Record during source audit | Replace | Athlete wearing a fitted custom rashguard during combat-sports training. | 2:1 | Custom sublimated rashguard for combat sports training | Critical | Audit required |
| P-022 | Rashguards | `pages/products/rashguards/index.html` | Gallery/detail | Record during source audit | Replace | Front/back garment views, sublimated artwork, reinforced seams and stretch-fabric close-up. | 4:3 | Rashguard sublimation, flatlock seams and stretch fabric | Critical | Audit required |
| P-023 | MMA Shorts | `pages/products/mma-shorts/index.html` | Hero | Record during source audit | Replace | Fighter wearing custom MMA shorts, with shorts unobscured and clearly framed. | 2:1 | Custom MMA shorts for training and competition | Critical | Audit required |
| P-024 | MMA Shorts | `pages/products/mma-shorts/index.html` | Gallery/detail | Record during source audit | Replace | Waist closure, side slit, stretch panels, artwork and front/back product views. | 4:3 | MMA shorts waistband, stretch panels and custom graphics | Critical | Audit required |
| P-025 | Muay Thai Shorts | `pages/products/muay-thai-shorts/index.html` | Hero | Record during source audit | Replace | Traditional Muay Thai shorts with distinctive waistband and custom artwork in a ring or training context. | 2:1 | Custom Muay Thai shorts with traditional high waistband | Critical | Audit required |
| P-026 | Muay Thai Shorts | `pages/products/muay-thai-shorts/index.html` | Gallery/detail | Record during source audit | Replace | Satin/performance fabric, embroidery, waistband, side panels and front/back views. | 4:3 | Muay Thai shorts embroidery, waistband and fabric details | Critical | Audit required |
| P-027 | Caps & Headwear | `pages/products/caps-headwear/index.html` | Hero | Record during source audit | Replace/review | Coordinated collection of branded caps photographed from useful angles. | 2:1 | Custom embroidered caps and branded headwear | High | Audit required |
| P-028 | Caps & Headwear | `pages/products/caps-headwear/index.html` | Gallery/detail | Record during source audit | Replace/review | Front logo, side embroidery, closure, internal label and embroidery production. | 4:3 | Cap embroidery, closure and internal branding details | High | Audit required |
| P-029 | Tote Bags | `pages/products/tote-bags/index.html` | Hero | Record during source audit | Replace/review | Branded tote bags shown clearly in retail, event or promotional use. | 2:1 | Custom branded tote bags for retail and events | High | Audit required |
| P-030 | Tote Bags | `pages/products/tote-bags/index.html` | Gallery/detail | Record during source audit | Replace/review | Handle construction, print, embroidery, fabric weights and internal label. | 4:3 | Tote bag printing, handles and fabric construction | High | Audit required |
| P-031 | Promotional Merchandise | `pages/products/promotional-merchandise/index.html` | Hero | Record during source audit | Replace/review | Cohesive campaign kit with apparel, tote, cap and selected branded items; avoid clutter. | 2:1 | Coordinated promotional merchandise and branded apparel kit | Medium | Audit required |
| P-032 | Promotional Merchandise | `pages/products/promotional-merchandise/index.html` | Gallery/application | Record during source audit | Replace/review | Event merchandise table, staff apparel, campaign packaging and brand consistency details. | 4:3 | Branded event merchandise and campaign apparel | Medium | Audit required |
| P-033 | Private Label Clothing | `pages/products/private-label-clothing/index.html` | Hero | Record during source audit | Replace | Cohesive retail-ready clothing collection presented as a brand launch. | 2:1 | Private label clothing collection ready for retail | Critical | Audit required |
| P-034 | Private Label Clothing | `pages/products/private-label-clothing/index.html` | Gallery/detail | Record during source audit | Replace | Woven labels, hang tags, size labels, custom packaging and folded garments. | 4:3 | Private label garment labels, hang tags and packaging | Critical | Audit required |

---

# C. Industry Pages

| ID | Industry page | URL / repository path | Image position | Current image/source | Audit decision | Replacement brief | Preferred ratio | Suggested alt text | Priority | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| I-001 | Construction & Trades | `pages/industries/construction-trades/index.html` | Hero | Record during source audit | Replace | Construction or trade team wearing coordinated branded workwear; avoid equipment-only imagery. | 2:1 | Branded workwear for construction and trade teams | Critical | Audit required |
| I-002 | Construction & Trades | same | Supporting imagery | Record during source audit | Replace/review | Work shirts, jackets, embroidery, utility details and team consistency on site. | 4:3 | Durable custom uniforms used by trade professionals | High | Audit required |
| I-003 | Healthcare | `pages/industries/healthcare/index.html` | Hero | Record during source audit | Replace | Healthcare team in coordinated scrubs or clinical uniforms; apparel must dominate the composition. | 2:1 | Custom healthcare uniforms for clinic and care staff | Critical | Audit required |
| I-004 | Healthcare | same | Supporting imagery | Record during source audit | Replace/review | Clinic branding, pockets, multiple roles and easy-care garment details. | 4:3 | Branded healthcare uniforms in a clinical environment | High | Audit required |
| I-005 | Hospitality | `pages/industries/hospitality/index.html` | Hero | Record during source audit | Replace | Restaurant, café or hotel team wearing coordinated uniforms. | 2:1 | Custom hospitality uniforms for restaurant and hotel teams | Critical | Audit required |
| I-006 | Hospitality | same | Supporting imagery | Record during source audit | Replace/review | Aprons, polos, shirts, chefwear, embroidery and front/back-of-house combinations. | 4:3 | Hospitality uniforms, aprons and embroidered staff apparel | High | Audit required |
| I-007 | Sports & Fitness | `pages/industries/sports-fitness/index.html` | Hero | Record during source audit | Replace/review | Fitness team, gym staff or athletes wearing custom performance apparel. | 2:1 | Custom sportswear for fitness teams and clubs | High | Audit required |
| I-008 | Sports & Fitness | same | Supporting imagery | Record during source audit | Replace/review | Training tops, shorts, jackets, team kits and technical-fabric details. | 4:3 | Coordinated custom fitness and team apparel | High | Audit required |
| I-009 | Combat Sports | `pages/industries/combat-sports/index.html` | Hero | Record during source audit | Replace | MMA, BJJ or Muay Thai athletes wearing page-relevant fightwear. | 2:1 | Custom combat sports apparel for fight teams and gyms | Critical | Audit required |
| I-010 | Combat Sports | same | Supporting imagery | Record during source audit | Replace | Rashguards, fight shorts, team sets, mat/ring context and garment details. | 4:3 | Custom rashguards and fight shorts used in training | Critical | Audit required |
| I-011 | Corporate Apparel | `pages/industries/corporate-apparel/index.html` | Hero | Record during source audit | Replace | Workplace team wearing coordinated branded apparel; avoid empty offices and generic meetings. | 2:1 | Branded corporate uniforms for professional teams | High | Audit required |
| I-012 | Corporate Apparel | same | Supporting imagery | Record during source audit | Replace/review | Reception, field staff, sales team, outerwear and embroidery details. | 4:3 | Coordinated corporate apparel across business roles | High | Audit required |
| I-013 | Franchises | `pages/industries/franchises/index.html` | Hero | Record during source audit | Replace | Multi-role or multi-location service team showing scalable uniform consistency. | 2:1 | Consistent custom uniforms for franchise teams | High | Audit required |
| I-014 | Franchises | same | Supporting imagery | Record during source audit | Replace/review | Branch-ready packaged orders, multiple staff roles and consistent colours/logos. | 4:3 | Uniform consistency and packaged orders for franchise locations | High | Audit required |
| I-015 | Ecommerce Brands | `pages/industries/ecommerce-brands/index.html` | Hero | Record during source audit | Replace | Online apparel collection, branded packaging and fulfilment in one composition. | 2:1 | Private label apparel and fulfilment for ecommerce brands | High | Audit required |
| I-016 | Ecommerce Brands | same | Supporting imagery | Record during source audit | Replace/review | Product photography, custom labels, polybags, order packing and unboxing. | 4:3 | Ecommerce apparel labels, packaging and order fulfilment | High | Audit required |
| I-017 | Retail Brands | `pages/industries/retail-brands/index.html` | Hero | Record during source audit | Replace | Curated retail clothing collection on racks or displays with garments clearly visible. | 2:1 | Retail-ready private label apparel collection | High | Audit required |
| I-018 | Retail Brands | same | Supporting imagery | Record during source audit | Replace/review | Labels, hang tags, folded products, merchandising and garment details. | 4:3 | Retail apparel presentation, labels and hang tags | High | Audit required |
| I-019 | Events & Merchandise | `pages/industries/events-merchandise/index.html` | Hero | Record during source audit | Replace | Event staff or attendees wearing branded shirts with a visible merchandise area. | 2:1 | Branded event apparel and merchandise | High | Audit required |
| I-020 | Events & Merchandise | same | Supporting imagery | Record during source audit | Replace/review | Merch table, campaign apparel, tote bags, caps, packaged stock and group use. | 4:3 | Event merchandise table and coordinated branded apparel | High | Audit required |
| I-021 | Influencers & Creator Brands | `pages/industries/influencers-creator-brands/index.html` | Hero | Record during source audit | Replace | Creator presenting or wearing their own merchandise collection. | 2:1 | Creator merchandise and private label apparel collection | High | Audit required |
| I-022 | Influencers & Creator Brands | same | Supporting imagery | Record during source audit | Replace/review | Content shoot, product drop, packaging, social-commerce setup and fulfilment. | 4:3 | Creator apparel product drop and branded packaging | High | Audit required |
| I-023 | Education | `pages/industries/education/index.html` | Hero | Generic office/team meeting image identified in audit | Replace | Students, university society, school team or campus staff wearing branded apparel. | 2:1 | Custom school and university apparel for students and staff | Critical | Replace |
| I-024 | Education | same | Supporting imagery | Record during source audit | Replace | School polos, sports kits, hoodies, student merchandise and campus events. | 4:3 | Branded education apparel for campus teams and student groups | Critical | Audit required |

---

# D. Service Pages

| ID | Service page | URL / repository path | Image position | Current image/source | Audit decision | Replacement brief | Preferred ratio | Suggested alt text | Priority | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| S-001 | OEM Clothing Production | `pages/services/oem-clothing-production/index.html` | Hero | Record during source audit | Replace | Active garment-production floor showing cutting, sewing or assembly. | 2:1 | OEM clothing production and garment assembly in Thailand | Critical | Audit required |
| S-002 | OEM Clothing Production | same | Supporting imagery | Record during source audit | Replace | Fabric preparation, sewing operators, production batches and workflow oversight. | 4:3 | End-to-end OEM garment manufacturing process | Critical | Audit required |
| S-003 | Private Label Manufacturing | `pages/services/private-label-manufacturing/index.html` | Hero | Record during source audit | Replace | Retail-ready garments with custom labels, hang tags and packaging. | 2:1 | Private label garments with custom branding and packaging | Critical | Audit required |
| S-004 | Private Label Manufacturing | same | Supporting imagery | Record during source audit | Replace | Label application, size tabs, folding, packaging and finished collections. | 4:3 | Private label garment finishing and packaging | Critical | Audit required |
| S-005 | Product Development | `pages/services/product-development/index.html` | Hero | Record during source audit | Replace | Designer or technician reviewing garment samples, specifications and materials. | 2:1 | Custom garment product development and specification review | Critical | Audit required |
| S-006 | Product Development | same | Supporting imagery | Record during source audit | Replace | Tech packs, measurements, patterns, swatches, colour standards and prototype review. | 4:3 | Apparel tech pack, fabric and prototype development | Critical | Audit required |
| S-007 | Sampling | `pages/services/sampling/index.html` | Hero | Record during source audit | Replace | First garment sample being inspected, measured or fitted. | 2:1 | Custom clothing sample review and fitting | Critical | Audit required |
| S-008 | Sampling | same | Supporting imagery | Record during source audit | Replace | Fit review, revision notes, stitching evaluation and approved sample comparison. | 4:3 | Garment prototype measurement and sample approval | Critical | Audit required |
| S-009 | Screen Printing | `pages/services/screen-printing/index.html` | Hero | Record during source audit | Replace/review | Operator or carousel printing directly onto a garment, with screen and ink visible. | 2:1 | Screen printing custom artwork onto a T-shirt | Critical | Audit required |
| S-010 | Screen Printing | same | Supporting imagery | Record during source audit | Replace/review | Screen setup, ink application, curing, print close-up and finished stack. | 4:3 | Screen printing setup, ink and finished garment detail | Critical | Audit required |
| S-011 | Embroidery | `pages/services/embroidery/index.html` | Hero | Record during source audit | Replace | Embroidery machine stitching a logo onto a polo, jacket or cap. | 2:1 | Machine embroidery of a custom logo on apparel | Critical | Audit required |
| S-012 | Embroidery | same | Supporting imagery | Record during source audit | Replace | Thread colours, hoop setup, stitch detail, garment examples and inspection. | 4:3 | Embroidery threads, hoop setup and stitched logo detail | Critical | Audit required |
| S-013 | Sublimation Printing | `pages/services/sublimation-printing/index.html` | Hero | Record during source audit | Replace | Sublimation transfer or printed sportswear panels with vivid full-colour artwork. | 2:1 | Full-colour sublimation printing for custom sportswear | Critical | Audit required |
| S-014 | Sublimation Printing | same | Supporting imagery | Record during source audit | Replace | Transfer sheet, printed panels, colour detail and finished team kit. | 4:3 | Sublimated fabric panels and finished performance apparel | Critical | Audit required |
| S-015 | Heat Transfer Printing | `pages/services/heat-transfer-printing/index.html` | Hero | Record during source audit | Replace | Heat press applying a logo or graphic to a garment. | 2:1 | Heat transfer logo application on custom apparel | Critical | Audit required |
| S-016 | Heat Transfer Printing | same | Supporting imagery | Record during source audit | Replace | Transfer film, alignment, press operation, peel stage and finished result. | 4:3 | Heat transfer film, press process and finished logo | Critical | Audit required |
| S-017 | Custom Labels | `pages/services/custom-labels/index.html` | Hero | Record during source audit | Replace | Macro image of woven or printed garment labels sewn into apparel. | 2:1 | Custom woven and printed labels for private label clothing | High | Audit required |
| S-018 | Custom Labels | same | Supporting imagery | Record during source audit | Replace | Neck labels, care labels, size tabs, folded edges and application. | 4:3 | Garment neck labels, care labels and size tabs | High | Audit required |
| S-019 | Hang Tags | `pages/services/hang-tags/index.html` | Hero | Record during source audit | Replace | Branded hang tag attached to a finished retail garment. | 2:1 | Custom branded hang tag attached to a garment | High | Audit required |
| S-020 | Hang Tags | same | Supporting imagery | Record during source audit | Replace | Tag stock, string/fasteners, barcode area, brand story and retail presentation. | 4:3 | Custom hang tag materials and retail garment presentation | High | Audit required |
| S-021 | Packaging Solutions | `pages/services/packaging-solutions/index.html` | Hero | Record during source audit | Replace | Folded garments being prepared in branded packaging. | 2:1 | Custom garment packaging for retail and ecommerce orders | High | Audit required |
| S-022 | Packaging Solutions | same | Supporting imagery | Record during source audit | Replace | Polybags, tissue paper, boxes, inserts, stickers and size labels. | 4:3 | Branded apparel packaging, inserts and labels | High | Audit required |
| S-023 | Quality Control | `pages/services/quality-control/index.html` | Hero | Record during source audit | Replace | Inspector measuring or examining a finished garment. | 2:1 | Quality inspection and measurement of a finished garment | Critical | Audit required |
| S-024 | Quality Control | same | Supporting imagery | Record during source audit | Replace | Seam inspection, colour comparison, print check and final checklist. | 4:3 | Garment seam, colour and print quality inspection | Critical | Audit required |
| S-025 | Worldwide Shipping | `pages/services/worldwide-shipping/index.html` | Hero | Record during source audit | Replace | Labelled garment cartons or palletised apparel orders ready for dispatch. | 2:1 | Custom apparel cartons prepared for worldwide shipping | High | Audit required |
| S-026 | Worldwide Shipping | same | Supporting imagery | Record during source audit | Replace/review | Packing, shipping labels, freight handling and destination documentation; aircraft or containers only as secondary context. | 4:3 | Packed garment orders and international shipping documentation | High | Audit required |

---

# E. Page-Level Source Capture Checklist

Complete this checklist before selecting a replacement image for each row:

- [ ] Record exact current image URL or repository asset path.
- [ ] Record whether the image is loaded through `<img>`, inline CSS or stylesheet background.
- [ ] Record the section heading and nearby body copy.
- [ ] Capture desktop screenshot.
- [ ] Capture tablet screenshot.
- [ ] Capture mobile screenshot.
- [ ] Confirm image aspect ratio and rendered dimensions.
- [ ] Check whether the same source image appears on other pages.
- [ ] Mark the image `Keep`, `Review` or `Replace`.
- [ ] Add one or more replacement candidates.
- [ ] Confirm commercial usage rights and source attribution requirements.
- [ ] Write final page-specific alt text.
- [ ] Implement without altering the approved page structure.
- [ ] Verify lazy loading, intrinsic dimensions and responsive behaviour.
- [ ] Approve desktop, tablet and mobile crops.

# F. Replacement Candidate Fields

When sourcing begins, add the following information to each relevant row or to a linked sourcing sheet:

| Field | Required information |
|---|---|
| Candidate source | Photographer, stock library, commissioned shoot or TShirtSwiss-owned asset |
| Candidate URL/path | Source URL or repository asset path |
| Licence | Commercial-use terms and attribution requirement |
| Original dimensions | Pixel width and height |
| Proposed crop | Desktop, tablet and mobile crop notes |
| Colour treatment | Natural, desaturated, dark overlay or other approved treatment |
| File output | AVIF/WebP primary plus JPG fallback where required |
| Filename | Descriptive lowercase filename using hyphens |
| Alt text | Concise, page-specific description |
| Approval | Reviewer and approval date |

# G. Naming Convention

Use descriptive filenames instead of stock-library IDs.

Examples:

- `custom-tshirts-screen-printing-hero.webp`
- `medical-scrubs-clinic-team-hero.webp`
- `muay-thai-shorts-waistband-detail.webp`
- `embroidery-machine-logo-detail.webp`
- `quality-control-garment-measurement.webp`
- `private-label-garment-packaging.webp`

Do not use filenames such as:

- `image1.jpg`
- `unsplash-12345.jpg`
- `factory-photo-final-final.jpg`

# H. Implementation Order

## Batch 1 — Main conversion pages

1. Home
2. Products
3. Industries
4. Services
5. Production

## Batch 2 — Critical product pages

1. Custom T-Shirts
2. Workwear
3. Healthcare Uniforms
4. Medical Scrubs
5. Rashguards
6. MMA Shorts
7. Muay Thai Shorts
8. Private Label Clothing

## Batch 3 — Critical industry pages

1. Construction & Trades
2. Healthcare
3. Hospitality
4. Combat Sports
5. Education

## Batch 4 — Critical service pages

1. OEM Clothing Production
2. Product Development
3. Sampling
4. Screen Printing
5. Embroidery
6. Sublimation Printing
7. Heat Transfer Printing
8. Quality Control

## Batch 5 — Remaining pages

Complete all remaining product, industry, service and supporting pages.

# I. Approval Rule

Do not replace images directly on an approved or live page without review.

For each batch:

1. Record current sources.
2. Select candidate imagery.
3. Review candidates against page content.
4. Implement on a controlled branch or approved prototype location.
5. Verify desktop, tablet and mobile crops.
6. Check image performance and alt text.
7. Record the change in the project change log.
8. Approve and lock the batch before moving to the next one.
