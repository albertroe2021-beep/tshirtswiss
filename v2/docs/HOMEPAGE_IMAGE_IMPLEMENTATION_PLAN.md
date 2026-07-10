# Homepage Image Implementation Plan

Branch: `feature/image-replacement-phase-1`

Page: `pages/home/index.html`

Public preview: `https://albertroe2021-beep.github.io/tshirtswiss/v2/`

## Objective

Replace irrelevant or overly generic homepage photography without changing the approved page structure, copy, SVG mappings, forms, navigation or footer.

## Current homepage image inventory

| Ref | Section | Current source | Type | Current alt text | Assessment | Replacement ID | Required replacement |
|---|---|---|---|---|---|---|---|
| H-001 | Hero | `https://images.unsplash.com/photo-1556905055-8f358a7a47b2?...` | CSS background | Not applicable | Broad fashion/apparel image; does not clearly communicate Swiss-managed manufacturing, product range or factory capability. | M-001 / A-001 | Premium finished branded apparel in a real garment-production environment, with the main subject positioned right and clear text-safe space left. |
| H-002 | Industries: Construction & Trades | `https://images.pexels.com/photos/8961065/pexels-photo-8961065.jpeg?...` | `<img>` | `Construction and trades workwear` | Review. Keep only if workwear is clearly visible, correctly fitted and appropriate to the Swiss trades/construction audience. | M-009 | Construction or trade team wearing coordinated branded workwear in a credible site environment. |
| H-003 | Industries: Healthcare | `https://images.unsplash.com/photo-1584515933487-779824d29309?...` | `<img>` | `Healthcare uniforms` | Review. Must show uniforms rather than relying on a general healthcare setting. | M-009 | Clinic or healthcare team wearing coordinated uniforms or scrubs. |
| H-004 | Industries: Hospitality | `https://images.pexels.com/photos/3184192/pexels-photo-3184192.jpeg?...` | `<img>` | `Hospitality uniforms` | Replace/review. Generic workplace/team photography may not clearly show hospitality uniforms. | M-009 | Restaurant, cafe or hotel staff wearing coordinated branded uniforms. |
| H-005 | Industries: Fitness | `https://images.pexels.com/photos/416778/pexels-photo-416778.jpeg?...` | `<img>` | `Fitness apparel` | Review. Keep only if the performance clothing is a clear focal point. | M-009 | Fitness team or athletes wearing coordinated custom performance apparel. |
| H-006 | Industries: Combat Sports | `https://images.pexels.com/photos/6295765/pexels-photo-6295765.jpeg?...` | `<img>` | `Combat sports apparel` | Replace/review. Must show correct combat-sports clothing, not only gloves or a generic fighter. | M-009 | Athlete or fight team wearing rashguards, MMA shorts or Muay Thai shorts. |
| H-007 | Industries: Corporate Apparel | `https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?...` | `<img>` | `Corporate apparel` | Replace. Generic office/team imagery does not demonstrate coordinated corporate apparel. | M-009 | Professional team wearing coordinated polos, shirts, jackets or branded knitwear. |
| H-008 | Industries: Event Merchandise | `https://images.pexels.com/photos/1763075/pexels-photo-1763075.jpeg?...` | `<img>` | `Events merchandise` | Replace. A crowd or concert image does not show merchandise manufacturing or branded event apparel. | M-009 | Event staff or attendees wearing branded shirts beside a clearly visible merchandise display. |
| H-009 | Industries: Ecommerce Brands | `https://images.pexels.com/photos/7679863/pexels-photo-7679863.jpeg?...` | `<img>` | `Ecommerce brand packing` | Review. Suitable only if garments, labels and branded packaging are clearly visible. | M-009 | Apparel ecommerce order being folded, labelled and packed in branded packaging. |
| H-010 | Quality Control | `https://images.pexels.com/photos/3735218/pexels-photo-3735218.jpeg?...` | `<img>` | `Garment quality control` | Replace/review. Must show an identifiable garment inspection, measurement, stitching check or colour comparison. | M-004 / A-004 | Inspector measuring a finished garment against a specification sheet. |
| H-011 | CTA | `https://images.unsplash.com/photo-1581092335397-9583eb92d232?...` | CSS background | Not applicable | Replace. Generic industrial image is unrelated to completed custom apparel orders. | M-005 / A-005 | Folded branded garments, labels and cartons prepared for international dispatch. |

## SVG and decorative assets retained

The following homepage assets are approved as SVG interface or category icons and are outside the photography replacement scope unless the SVG master mapping changes:

- `shield-with-cross-svgrepo-com (1).svg`
- `factory-building-svgrepo-com.svg`
- `quality-5-svgrepo-com.svg`
- `plane-svgrepo-com (1).svg`
- `handshake-svgrepo-com.svg`
- Product category SVGs used in the Products section
- Process SVGs used in the production-process cards
- Footer contact SVGs

## Approved target assets

| Asset ID | Final filename | Placement | Ratio | Desktop target | Mobile target | Alt text / accessibility |
|---|---|---|---:|---:|---:|---|
| A-001 | `home-apparel-production-hero.webp` | Hero background | 2:1 | 2000 x 1000 | 900 x 1200 alternate crop where needed | Decorative CSS background; page heading already provides context. |
| A-002 | `home-construction-workwear-card.webp` | Construction card | 1.35:1 | 900 x 667 | Same source with focal crop | `Construction and trade team wearing branded workwear` |
| A-003 | `home-healthcare-uniforms-card.webp` | Healthcare card | 1.35:1 | 900 x 667 | Same source with focal crop | `Healthcare team wearing coordinated custom uniforms` |
| A-004 | `home-hospitality-uniforms-card.webp` | Hospitality card | 1.35:1 | 900 x 667 | Same source with focal crop | `Hospitality team wearing coordinated staff uniforms` |
| A-005 | `home-fitness-apparel-card.webp` | Fitness card | 1.35:1 | 900 x 667 | Same source with focal crop | `Fitness team wearing custom performance apparel` |
| A-006 | `home-combat-sports-apparel-card.webp` | Combat Sports card | 1.35:1 | 900 x 667 | Same source with focal crop | `Combat sports athletes wearing custom fightwear` |
| A-007 | `home-corporate-apparel-card.webp` | Corporate Apparel card | 1.35:1 | 900 x 667 | Same source with focal crop | `Professional team wearing coordinated corporate apparel` |
| A-008 | `home-event-merchandise-card.webp` | Event Merchandise card | 1.35:1 | 900 x 667 | Same source with focal crop | `Branded event apparel and merchandise display` |
| A-009 | `home-ecommerce-packing-card.webp` | Ecommerce Brands card | 1.35:1 | 900 x 667 | Same source with focal crop | `Branded apparel order being packed for ecommerce delivery` |
| A-010 | `home-garment-quality-review.webp` | Quality Control section | 4:3 | 1400 x 1050 | 900 x 900 focal crop | `Inspector measuring a finished garment during quality control` |
| A-011 | `home-finished-garment-shipment.webp` | CTA background | 2:1 | 1800 x 900 | 900 x 1200 alternate crop where needed | Decorative CSS background; CTA text supplies context. |

## Repository target paths

Store final files under:

```text
v2/assets/images/home/
```

Recommended structure:

```text
v2/assets/images/home/
  hero/
  industries/
  quality-control/
  cta/
  originals/
```

Only web-optimised files should be referenced by the page. Licensed originals should be stored separately only when repository policy and licence terms permit it.

## HTML/CSS implementation rules

### Hero

Replace the external Unsplash URL in `.hero::before` with the approved repository asset.

Target relative path from `pages/home/index.html`:

```css
url('../../v2/assets/images/home/hero/home-apparel-production-hero.webp')
```

Before implementation, confirm the exact final relative path in the GitHub Pages deployment structure.

Add a mobile-specific source or background-position rule if the desktop crop loses the garment or production context below 700 px.

### Industry cards

Replace each external Pexels or Unsplash URL with a repository-hosted WebP/AVIF asset.

Preserve:

- Existing card order
- Existing links
- `class="photo"`
- Existing 1.35:1 rendered aspect ratio

Update alt text to the approved descriptions in this document.

### Quality Control

Replace the external Pexels URL with `home-garment-quality-review.webp`.

Preserve:

- Existing `quality-visual` structure
- Existing stats overlay
- Existing 420 px desktop image height

Check that the inspector and garment remain visible behind the right-hand stats panel. The primary subject should sit left or centre-left.

### CTA

Replace the external Unsplash URL in `.cta-band::before` with the approved repository asset.

Retain the current dark overlay unless contrast testing shows it should be adjusted. Remove `filter:grayscale(1)` unless the approved image treatment specifically requires monochrome output.

## Sourcing acceptance criteria

A candidate can be approved only when:

- It directly matches the page section.
- Garments or apparel production are clearly visible.
- It can be commercially used and the licence is recorded.
- Original resolution meets or exceeds the target.
- It has no visible third-party trademarks requiring clearance.
- Desktop and mobile crops work.
- It matches the Brand Photography Style Guide.
- It does not duplicate another page hero.

## Implementation sequence

1. Source and approve A-001 hero.
2. Source and approve A-010 quality-control image.
3. Source and approve A-011 CTA image.
4. Source and approve all eight industry-card images as one coherent visual set.
5. Optimise and add files to `v2/assets/images/home/`.
6. Update `pages/home/index.html` on this feature branch.
7. Record final sources in `IMAGE_ASSET_REGISTER.md`.
8. Update `IMAGE_IMPLEMENTATION_TRACKER.md`.
9. Run desktop, tablet, mobile, accessibility and performance QA.
10. Open a pull request for review; do not merge until approved.

## Current implementation status

| Task | Status |
|---|---|
| Current homepage source inspected | Complete |
| Current photography URLs recorded | Complete |
| Replacement IDs assigned | Complete |
| Final filenames assigned | Complete |
| Source candidates selected | Pending |
| Licences verified | Pending |
| Web assets optimised | Pending |
| Homepage code updated | Pending |
| Responsive QA | Pending |
| Approval | Pending |
