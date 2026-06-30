# Manual SVG Update Progress

This tracker records the manual SVG icon standardisation work based on:

- `SVG number to phrase.xlsx`
- `docs/svg-icon-mapping-draft.md`
- `scripts/apply_svg_icon_mapping.py`
- `site-header-sw.js`

## Current Status

The repository currently has two layers of icon standardisation:

1. **Runtime layer** via `site-header-sw.js`
   - Applies the Ref# icon registry and phrase-to-icon mapping at runtime.
   - Standardises trust icons and process icons globally.
   - Uses the red outline style and 2.6 stroke weight.

2. **Static update layer** via `scripts/apply_svg_icon_mapping.py`
   - Intended to permanently write mapped icons directly into HTML pages.
   - Requires execution in Codespaces, local terminal, or another GitHub execution environment.

## Manual Static Update Batches

Because the current GitHub connector can update files individually but cannot execute the Python script inside the repository, static HTML updates need to be handled in batches.

| Batch | Area | Status | Notes |
|---:|---|---|---|
| 1 | Global runtime mapping | Completed | `site-header-sw.js` contains Ref# mapping and phrase matching. |
| 2 | Home page | Pending static rewrite | Runtime mapping currently applies on page load. |
| 3 | Product pages | Pending static rewrite | Product process section already standardised through runtime mapping. |
| 4 | Industry pages | Pending static rewrite | Trust row standardised through runtime mapping. |
| 5 | Service pages | Pending static rewrite | Trust row standardised through runtime mapping. |
| 6 | Resources / Contact / Quote pages | Pending static rewrite | To be handled after product, industry, and service pages. |

## Manual Update Rules

When editing a page manually:

1. Identify cards, trust rows, process steps, feature cards, or CTA/icon rows containing a phrase from the placement sheet.
2. Find the Ref# for that phrase in `docs/svg-icon-mapping-draft.md`.
3. Replace the current icon with the matching SVG from the registry.
4. Use the standard class:

```html
<svg class="ts-inline-icon" aria-hidden="true" focusable="false" ...>
```

5. Preserve surrounding page layout and text.
6. Do not add rounded icon boxes unless already required by the section design.
7. Keep icons red via `currentColor` and the existing CSS color rules.

## Important Note

The runtime service-worker mapping is currently the safest global implementation because it updates all navigated HTML pages without requiring each static HTML file to be rewritten one by one.

Static page rewrites should be completed gradually and verified page by page.
