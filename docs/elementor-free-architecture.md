# Elementor Free Architecture

## Supported stack

- WordPress
- Hello Elementor
- Elementor Free 4.1.5 or compatible
- Flexbox Containers enabled
- Editor V4 enabled
- WPForms Lite
- Yoast SEO
- LiteSpeed Cache

## Delivery model

### Pages

Unique pages are delivered as Elementor page templates.

### Shared child designs

Three shared designs are maintained:

- Product child page
- Service child page
- Who We Serve child page

Because Elementor Free does not provide Theme Builder display conditions, these are distributed as reusable page templates. Each child page is created from the relevant template and then populated with page-specific content.

### Header and footer

Elementor Free cannot assign Theme Builder headers and footers. The framework therefore supplies:

- Global Header EN as a saved section
- Global Footer EN as a saved section
- Equivalent language variants as they are completed

The preferred production options are:

1. Insert the saved header and footer sections into each Elementor page, or
2. Load them through the existing lightweight theme/plugin integration where available.

The implementation must not require Elementor Pro.

### Forms

Elementor Free does not include the Pro Form widget. Forms are built with WPForms Lite.

Elementor templates can include a WPForms widget or shortcode location, but WPForms form definitions are stored by WPForms and must be imported or recreated separately. Each form must therefore have:

- A documented form name
- A field map
- Notification settings
- Confirmation behaviour
- The target Elementor page and section

## Package structure

```text
elementor-kit/
  templates/
    globals/
    pages/
    child-templates/
  assets/
  forms/
  manifest/

docs/
reference/
```

## Compatibility rules

- Use only widgets available in Elementor Free unless a plugin dependency is explicitly documented.
- Avoid Theme Builder display conditions.
- Avoid dynamic tags that require Elementor Pro.
- Avoid Pro nav menu, posts, portfolio, slides and form widgets.
- Prefer native containers, headings, text, images, icons, buttons, HTML and shortcodes.
- Keep custom CSS packaged as normal asset files rather than Elementor Pro Custom CSS.
- Treat every external plugin widget as an explicit dependency.

## Blog limitation

Elementor Free cannot replace the theme's native single-post and archive templates through Theme Builder. The initial framework can provide visually matched Elementor page designs for blog archive and post examples, but automatic WordPress post templating requires either:

- A compatible free theme/plugin solution,
- A small custom theme integration, or
- Elementor Pro later.

This limitation must be stated clearly in the installation documentation.
