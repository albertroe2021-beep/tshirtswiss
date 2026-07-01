# SVG Reference Library

## Rule

The spreadsheet is the master source for SVG mappings. Repository files and HTML references must be checked against the spreadsheet before approval.

## Current homepage SVG references to verify

The current homepage uses SVG references such as:

- `shield-with-cross-svgrepo-com (1).svg`
- `factory-building-svgrepo-com.svg`
- `quality-5-svgrepo-com.svg`
- `plane-svgrepo-com (1).svg`

These are visible in the topbar of `pages/home/index.html` and must be verified against the spreadsheet mapping before being reused in v2.

## Proposed library structure

- `v2/svg-library/mapping/` spreadsheet exports and mapping notes
- `v2/svg-library/draft/` draft generated SVGs
- `v2/svg-library/approved/` final approved SVGs
- `v2/svg-library/preview/` browser preview page and screenshots

## Naming convention

Use clear, stable names:

`category-purpose-version.svg`

Examples:

- `trust-swiss-managed-v1.svg`
- `trust-thailand-factory-v1.svg`
- `product-custom-tshirt-v1.svg`
- `industry-construction-v1.svg`

## Approval checklist

For every SVG:

- Matches spreadsheet description.
- Uses approved stroke/fill style.
- Looks consistent at small card sizes.
- Has clean viewBox.
- Has no embedded raster image.
- Has no unnecessary metadata.
- Is previewed in context.
- Is recorded in the mapping document.
