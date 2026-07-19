# Global Header Source Audit

## Status

This document is the implementation contract for recreating the established TShirtSwiss GitHub Pages header in Elementor Free.

The current GitHub website is the source of truth. The Elementor implementation must preserve the established design and must not replace it with a simplified header.

One intentional design change has been approved: the red preview notice bar at the very top of the existing GitHub header must not be included in the Elementor version. This is the only approved omission recorded by this specification.

## Source reviewed

Primary reference:

- `de/home/index.html`

The same header system is expected to be reused across the English, German and French page families, with language-specific labels and URLs.

## Non-negotiable fidelity rule

Except for the approved removal of the red preview notice bar, the Elementor version must preserve, as closely as the WordPress and Elementor Free environment permits:

- section order
- content hierarchy
- desktop and mobile layouts
- navigation depth
- dropdown and drawer interactions
- spacing and proportions
- typography weight and casing
- colours, borders, shadows and radii
- sticky behaviour
- language navigation
- quote call-to-action prominence

