# Project Charter

## Project

TShirtSwiss v2 website redesign and Elementor implementation.

## Mission

Create the definitive version of the TShirtSwiss website in approved HTML first, then use that approved HTML as the master source for the WordPress Elementor build.

## Non-negotiables

- Do not overwrite the current live site while v2 is being designed.
- Do not make design decisions directly inside Elementor.
- Do not move a page into Elementor until the HTML page is approved.
- Do not modify approved sections without logging a change request.
- Keep SVG mappings controlled by the spreadsheet.

## Phases

1. Recovery and stabilisation
2. Homepage design
3. Design Bible
4. Products
5. Industries
6. Services
7. Resources
8. About
9. Contact
10. Final QA
11. Elementor build
12. Launch

## Master sources

- SVG mappings: spreadsheet
- Design system: `v2/docs/DESIGN_BIBLE.md`
- Approved HTML: `v2/html-master/`
- QA: `v2/qa/`
- Elementor migration: `v2/elementor/`
- Decisions and changes: `v2/docs/DECISIONS_LOG.md` and `v2/docs/CHANGE_LOG.md`

## Success criteria

- Every page has an approved HTML version before Elementor work begins.
- Navigation, responsiveness and SVG usage are visually verified.
- All major components are documented in the Design Bible.
- The final Elementor build matches the approved HTML design.
- The launch has a rollback plan and post-launch QA checklist.
