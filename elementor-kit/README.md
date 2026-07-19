# TShirtSwiss Elementor Kit

This directory contains the source scaffold for converting every existing TShirtSwiss static page into an Elementor Free website kit.

## Target environment

- Elementor 4.1.5
- Elementor Pro: not required
- Hello Elementor theme
- Flexbox Containers enabled
- Nested Elements enabled
- Editor V4 enabled

## Supported active plugins

- Elementor
- Royal Elementor Addons
- Ultimate Addons for Elementor
- WPForms Lite
- Yoast SEO
- LiteSpeed Cache

The kit must not depend on WooCommerce or Elementor Pro. TShirtSwiss is a manufacturing and lead-generation website, not an ecommerce store.

## Build approach

1. Inventory every HTML page in the English, German and French site trees.
2. Convert shared visual tokens into Elementor global colours, typography and spacing.
3. Rebuild shared header, navigation, footer, quote form and CTA sections as reusable templates.
4. Convert each existing page into an editable Elementor page template.
5. Package templates, site settings and import documentation into an Elementor-compatible ZIP.
6. Validate desktop, tablet and mobile layouts against the current GitHub Pages site.

## Status

Scaffolding started on branch `agent/elementor-kit`.
