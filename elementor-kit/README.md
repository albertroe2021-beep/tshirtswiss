# TShirtSwiss Elementor Kit

This directory is the source project and release builder for the TShirtSwiss Elementor website template.

## Target environment

- Elementor 4.1.5
- Elementor Pro: not required for page and site-settings import
- Hello Elementor theme
- Flexbox Containers enabled
- Nested Elements enabled
- Editor V4 enabled

## Supported active plugins

- Elementor
- WPForms Lite
- Yoast SEO
- LiteSpeed Cache

Royal Elementor Addons and Ultimate Addons for Elementor may remain installed, but the release must not require WooCommerce or Elementor Pro. TShirtSwiss is a manufacturing and lead-generation website, not an ecommerce store.

## Source layout

- `templates/pages/` - Elementor page-family exports
- `templates/components/` - reusable section exports
- `templates/globals/` - header and footer source exports
- `globals/` - TShirtSwiss design tokens
- `assets/` - multilingual header and footer assets
- `manifest/` - source template map
- `tools/` - validation and release builder

## Build the release archives

From the repository root, run:

```powershell
python elementor-kit/tools/build-elementor-kit.py --clean
```

On Windows, `py` may be used instead:

```powershell
py elementor-kit/tools/build-elementor-kit.py --clean
```

The builder validates every Elementor JSON source and creates:

```text
elementor-kit/dist/
  tshirtswiss-elementor-website-template.zip
  tshirtswiss-elementor-saved-templates.zip
  build-report.json
```

### Website template ZIP

`tshirtswiss-elementor-website-template.zip` uses Elementor import/export format 2.0. It contains:

- `manifest.json`
- `site-settings.json`
- `content/page/*.json`

Import it through Elementor's Website Templates import screen. This archive installs the eight page-family templates as editable WordPress pages and applies the TShirtSwiss global colours, typography and layout settings.

### Saved templates ZIP

`tshirtswiss-elementor-saved-templates.zip` contains the reusable components and multilingual global-part JSON files.

Elementor 4.1.5 checks for Elementor Pro before running its full-kit `templates` importer. Because this project deliberately does not require Pro, import the required JSON files from this companion archive through:

```text
WordPress Dashboard > Templates > Saved Templates > Import Templates
```

This is an Elementor product limitation, not missing source work. The page and site-settings archive remains fully automated and repeatable.

## GitHub Actions build

The workflow `.github/workflows/build-elementor-kit.yml` runs whenever `elementor-kit/**` changes on `agent/elementor-kit`, and can also be started manually from the Actions tab.

It publishes a downloadable artifact named:

```text
tshirtswiss-elementor-kit
```

The artifact contains both ZIP archives and the build report.

## Import sequence

1. Back up the staging WordPress site.
2. Confirm Hello Elementor and Elementor 4.1.5 are active.
3. Import `tshirtswiss-elementor-website-template.zip` from Elementor > Editor > Tools > Website Templates > Import.
4. Select Content and Site Settings.
5. Import the required reusable JSON templates from the companion saved-template archive.
6. Create the WPForms quote form and replace `{{WPFORMS_FORM_ID}}`.
7. Replace text, image and link placeholders.
8. Test desktop, tablet and mobile rendering.
9. Purge LiteSpeed Cache after final changes.

## Status

The source repository and automated packaging layer are complete. A live Elementor 4.1.5 staging import is the remaining release gate.
