# Design Bible

This document records approved TShirtSwiss v2 design decisions. Nothing here is final until a section is visually approved.

## Current design direction from existing homepage

The existing homepage establishes a strong industrial premium style:

- Black, white and red colour palette.
- High-contrast hero sections.
- Bold uppercase navigation and calls to action.
- Swiss-managed positioning.
- Trust and quality signals near the top of the page.
- Product and industry cards using clean SVG iconography.
- Generous spacing and strong grid structure.

## Colours

Initial palette from the current homepage CSS:

- Red: `#e1111a`
- Ink: `#111111`
- Muted text: `#555555`
- Line: `#e7e7e7`
- Soft background: `#f7f7f7`
- Header/footer black: near `#070707` to `#090909`

## Typography

Initial direction:

- Typeface: Inter, Arial, Helvetica, sans-serif.
- Headings: bold, compressed visual weight, tight line height.
- Navigation: uppercase, compact, heavy weight.
- Body copy: clear, readable and practical.

## Buttons

Primary CTA:

- Red background.
- White uppercase label.
- Heavy font weight.
- Small border radius.
- Strong but controlled shadow.

Secondary CTA:

- Transparent or outline style when used on dark backgrounds.

## Cards

Cards should feel clean, commercial and premium:

- White background.
- Light border or shadow.
- Subtle radius.
- Strong title hierarchy.
- SVG or image used with consistent sizing.

## Icons

- SVG icons must follow the spreadsheet mapping.
- Use a consistent visual weight across all icons.
- Prefer simple, strong shapes over decorative complexity.
- Approved icons belong in `v2/svg-library/approved/`.
- Draft icons belong in `v2/svg-library/draft/`.

## Layout

Initial reference from existing homepage:

- Main wrapper maximum width: around 1280px.
- Desktop layout uses strong multi-column grids.
- Tablet layout reduces to two or three columns where appropriate.
- Mobile layout prioritises stacked cards and readable text.

## Section approval record

| Section | Status | Notes |
|---|---|---|
| Header / Navigation | Review required | Current dropdown/nav must be stabilised before redesign. |
| Hero | Review required | Existing premium manufacturing positioning is the starting point. |
| Trust bar | Review required | SVG mapping must be checked. |
| Products | Review required | Card/icon consistency needed. |
| Footer | Review required | Needs full responsive and link QA. |
