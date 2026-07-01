# Elementor Migration Plan

## Rule

Elementor is a faithful implementation target. Design decisions are made in the approved HTML process first.

No Elementor build begins until the matching HTML page is approved.

## Migration sequence

1. Approve the HTML section.
2. Record the section components in the Design Bible.
3. Map the section to Elementor containers and widgets.
4. Build the section in Elementor.
5. Compare Elementor output against the approved HTML.
6. Check desktop, tablet and mobile.
7. Approve the Elementor section.

## Global settings to define

- Site colours
- Typography scale
- Button styles
- Container widths
- Breakpoints
- Form styles
- Card styles
- Icon sizing
- Header template
- Footer template

## Page template mapping

| HTML page | Elementor template | Status |
|---|---|---|
| Home | Homepage template | Not started |
| Products | Products landing template | Not started |
| Industries | Industries landing template | Not started |
| Services | Services landing template | Not started |
| Resources | Resources landing template | Not started |
| About | About template | Not started |
| Contact | Contact template | Not started |

## QA notes

- Match spacing to approved HTML.
- Avoid Elementor design drift.
- Keep reusable sections as reusable templates.
- Keep global styles centralised.
- Document any one-off values.
