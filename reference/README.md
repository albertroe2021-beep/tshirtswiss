# Visual Reference Workspace

This directory stores the approved visual baseline for the Elementor rebuild.

## Directory plan

```text
reference/
  home/
  products/
  product-child/
  services/
  service-child/
  industries/
  industry-child/
  resources/
  about/
  contact/
  blog-archive/
  blog-post/
```

## Required files per page

- `desktop.png`
- `mobile.png`
- `sections.md`
- `design-notes.md`
- `content-map.md`

## Design grouping

The following pages must not be forced into a universal component layout:

- Home
- Products Hub
- Services Hub
- Who We Serve Hub
- Resources Hub
- About Us
- Contact
- Blog Archive
- Blog Post

Only these page groups are treated as visually identical templates:

- Product child pages
- Service child pages
- Who We Serve child pages

Small differences within unique pages should be preserved rather than normalised for reuse.
