# Product Child Page V3 Audit Tracker

This tracker defines the audit standard for every product child page in the TShirtSwiss GitHub Pages prototype.

Reference layout: `pages/products/custom-t-shirts/index.html`

## Audit scope

Product child pages to audit:

- `pages/products/custom-t-shirts/index.html`
- `pages/products/custom-polos/index.html`
- `pages/products/hoodies-sweatshirts/index.html`
- `pages/products/jackets-softshells/index.html`
- `pages/products/workwear/index.html`
- `pages/products/healthcare-uniforms/index.html`
- `pages/products/medical-scrubs/index.html`
- `pages/products/corporate-apparel/index.html`
- `pages/products/sportswear/index.html`
- `pages/products/rashguards/index.html`
- `pages/products/mma-shorts/index.html`
- `pages/products/muay-thai-shorts/index.html`
- `pages/products/caps-headwear/index.html`
- `pages/products/tote-bags/index.html`
- `pages/products/promotional-merchandise/index.html`
- `pages/products/private-label-clothing/index.html`

## Required checks

Each page must be checked against the following before being marked complete.

### 1. V3 navigation

- Full V3 desktop navigation present.
- Full Products dropdown present.
- Full Who We Serve dropdown present with Industries and Businesses columns.
- Full Services dropdown present.
- Resources dropdown present.
- About Us dropdown present.
- Contact link present.
- Request a Quote CTA present.
- Top utility bar present with icons.
- Mobile menu present and scrollable.
- Mobile menu includes Products, Who We Serve, Services, Resources, About Us, Contact and Request a Quote.
- Relative paths are correct for product child depth.

### 2. Layout parity with Custom T-Shirts reference

- Same hero structure.
- Same hero form placement.
- Same trust strip structure.
- Same section rhythm.
- Same card spacing.
- Same gallery/image treatment where applicable.
- Same FAQ pattern.
- Same closing CTA pattern.
- Same footer structure.

### 3. Spacing and typography

- Header height consistent.
- Hero padding consistent.
- Section top and bottom padding consistent.
- Card padding consistent.
- Heading scale consistent.
- Paragraph width and line-height consistent.
- Button spacing consistent.
- No oversized gaps between sections.
- No cramped mobile sections.

### 4. Mobile audit

Check at approximately 320px, 375px, 390px, 414px, 768px, 820px and 1024px:

- No horizontal scrolling.
- Header does not overflow.
- Mobile menu opens and scrolls.
- Hero stacks correctly.
- Hero form remains readable.
- Buttons do not collide.
- Cards stack cleanly.
- Images crop acceptably.
- Tables, if present, remain usable.
- Footer columns stack cleanly.

### 5. SEO and content

- Unique title tag.
- Unique meta description.
- One clear H1.
- Logical H2 section hierarchy.
- Product-specific hero copy.
- Product-specific image alt text.
- Product-specific FAQ.
- Related service links.
- Related product links.
- Request quote path correct.

## Initial source audit findings

### Custom T-Shirts

Status: Reference page.

Findings:

- The current page is the reference layout for the product child pages.
- It has the expected product-page structure and spacing rhythm.
- It still needs a V3 navigation/header pass because the product child navigation does not yet include the full V3 Who We Serve mega menu structure.

### Custom Polos

Status: Inspected, not yet modified.

Findings:

- Layout appears to match the same product-page template family as the Custom T-Shirts page.
- Hero, trust strip and content structure are broadly aligned with the reference layout.
- It needs the same V3 navigation/header pass.
- Mobile menu should be checked after the V3 header replacement.

## Implementation rule

Do not redesign product child pages from scratch. Preserve the Custom T-Shirts page layout pattern and update only what is required to bring each page into V3 navigation, spacing, responsive and SEO compliance.

Each page should be committed separately or in small batches with a clear commit message so changes can be reviewed and reverted safely.