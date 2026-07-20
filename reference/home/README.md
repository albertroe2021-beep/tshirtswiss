# Homepage reference

Reference source: `de/home/index.html` on the static site. The English production build must follow the same visual structure and use the approved English content.

## Approved variance

The thin red preview/announcement strip above the black utility bar is intentionally excluded from the Elementor build.

## Page structure

1. Black utility bar
   - contact/trust items
   - language selector
2. Sticky white primary header
   - TShirtSwiss wordmark
   - desktop navigation and dropdowns
   - red quote CTA
   - responsive mobile menu trigger
3. Hero
   - dark photographic background with left-to-right overlay
   - primary headline, introduction, CTAs and trust pills
   - glass-style quote form card
4. Trust strip
   - five equal benefit cards
5. SEO introduction section
6. Industries grid
7. Products grid
8. Quality and production section
   - text/checklist column
   - image and statistics panel
9. Five-step process section
10. Dark CTA band
11. Footer

## Desktop layout constants

- Main content width: `min(1280px, calc(100% - 64px))`
- Main header height: approximately `108px`
- Utility bar height: approximately `48px`
- Hero minimum height: approximately `620px`
- Standard section vertical spacing: approximately `74px`
- Primary grid breakpoint target: desktop above `1024px`

## Core colours

| Token | Value | Use |
|---|---:|---|
| Brand red | `#e1111a` | CTAs, highlights, icons and active states |
| Ink | `#111111` | Primary text |
| Black | `#070707` | Utility bar and dark surfaces |
| Muted | `#555555` | Supporting copy |
| Border | `#e7e7e7` | Dividers and cards |
| Soft background | `#f7f7f7` | Alternating sections |
| White | `#ffffff` | Main background and reversed text |

## Typography

- Primary stack: `Inter, Arial, Helvetica, sans-serif`
- Headings: heavy weight, tight line-height and negative letter spacing
- Navigation and labels: bold uppercase with controlled tracking
- Body copy: regular/medium weight with generous line-height

## Elementor Free implementation notes

- Build the header and footer as importable saved sections, not Theme Builder templates.
- Use Flexbox Containers throughout.
- The quote form must be provided by WPForms Lite and selected after import.
- Store repeating values in the kit CSS variables and Elementor Site Settings where supported.
- Avoid relying on Elementor Pro widgets or dynamic tags.
- Preserve the static reference as the visual baseline and do not redesign sections during conversion.

## Validation checklist

- [ ] Red announcement strip absent
- [ ] Header and utility bar align with reference
- [ ] Hero overlay and content proportions match
- [ ] Quote card remains readable on all breakpoints
- [ ] Five trust cards remain balanced
- [ ] Industry and product grids collapse cleanly
- [ ] Statistics overlay is usable on tablet and mobile
- [ ] Mobile navigation is keyboard accessible
- [ ] Footer spacing and hierarchy match reference
