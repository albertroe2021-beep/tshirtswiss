# TShirtSwiss v2

This folder is the controlled workspace for the TShirtSwiss v2 redesign and Elementor migration.

## Mission

Design and build the definitive version of the TShirtSwiss website, then use the approved HTML as the master source for a complete WordPress Elementor implementation.

## Core principles

- Never rush changes.
- Never overwrite live or approved pages without verification.
- Work one approved section at a time.
- The spreadsheet is the master source for SVG mappings.
- The approved HTML is the master design.
- Elementor is built only after the HTML design is signed off.
- Every design decision must be documented.

## Workflow

1. Review the current section.
2. Agree on the exact changes.
3. Implement the changes in the v2 branch only.
4. Verify visually on desktop, tablet and mobile.
5. Record QA notes.
6. Approve and lock the section.
7. Move to the next section.

## Current source reference

The current repository and GitHub Pages site remain the reference for content layout and design direction. Existing pages should be studied before creating the v2 HTML equivalent.

Reference homepage source: `pages/home/index.html`

## Folder map

- `v2/docs/` living project documents
- `v2/html-master/` approved HTML prototypes by page
- `v2/svg-library/` SVG mapping notes, draft icons, approved icons and previews
- `v2/elementor/` Elementor migration notes and template planning
- `v2/qa/` visual, accessibility, performance and responsive QA records
- `v2/assets/` v2-specific images, icons, downloads and supporting files
