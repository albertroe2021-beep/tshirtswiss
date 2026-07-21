# TShirtSwiss Elementor Reference Kit – Import Instructions

## What's in this kit

This is a **native Elementor Export Kit** containing:
- **41 WordPress pages** (English, German, French variants)
- **16 reusable Elementor templates** (Headers, Footers, Product/Service/Industry child templates for each language)
- **Global Elementor styles** (colors, fonts, theme settings)
- **Elementor 4.1.5 configuration** (container settings, breakpoints, experiments)

## Requirements to import

- WordPress 6.8+
- Hello Elementor theme (3.4.9 or compatible)
- Elementor Free 4.1.5
- Flexbox Containers enabled
- Nested Elements enabled
- Editor V4 enabled

## Import steps

### 1. Prepare destination WordPress site

```bash
# Option A: Use the included wordpress-project docker setup
cd wordpress-project
cp .env.example .env
docker compose up -d
docker compose run --rm wpcli bash /scripts/setup_wordpress.sh
```

### 2. Import the kit

#### Option A: Manual import via WP Admin UI
1. Log in to WordPress Admin: `http://localhost:8088/wp-admin`
   - Username: `admin`
   - Password: `admin12345`
2. Navigate: **Elementor** → **Tools** → **Import & Export** → **Import Kit**
3. Upload: `tshirtswiss-reference-kit.zip`
4. Click **Import**

#### Option B: Import via WP-CLI (automated)
```bash
cd wordpress-project
docker compose run --rm wpcli bash -lc '
  cd /var/www/html
  unzip -o /exports/tshirtswiss-reference-kit.zip -d /tmp/kit-import
  wp --allow-root post list --post_type=page --format=count
  # Remaining steps are manual via UI or custom import script
'
```

### 3. Verify import

After import, check:

```bash
# Count imported pages
docker compose run --rm wpcli wp --allow-root post list --post_type=page --format=count

# List imported templates
docker compose run --rm wpcli wp --allow-root post list --post_type=elementor_library --format=table

# Check Elementor version
docker compose run --rm wpcli wp --allow-root plugin list | grep elementor
```

Expected results:
- 41 pages (including language roots, archives, singles)
- 16 templates (5 per language × 3 languages + 1 default)
- Elementor 4.1.5 active

### 4. Customize placeholder content

All pages and templates are seeded with **Lorem Ipsum placeholder content**.

To customize:

1. Open Elementor Editor on any page
2. Replace placeholder text with your own content
3. Update placeholder images with real product/service images
4. Verify links point to correct pages (language switcher, navigation)
5. Test forms (if custom form integration needed, configure via Elementor Form widget)
6. Publish

### 5. Test responsive behavior

In Elementor Editor, toggle preview widths:
- Desktop (1200px)
- Tablet (768px)
- Mobile (360px)

Ensure no overflow, broken containers, or text wrapping issues.

---

## Kit contents structure

```
manifest.json              # Export metadata and version info
content.json              # All pages, posts, and Elementor template data
styles.json               # Global colors, fonts, theme settings
theme-settings.json       # WordPress and Elementor configuration
```

## Known limitations

- Forms are Elementor Free placeholders; integrate with your form provider as needed
- Images are placeholders; replace with real product/service images
- Links point to local page slugs; verify navigation structure after import
- WooCommerce not included; can be added separately if needed

## Support

For issues or questions:
1. Check that WordPress, Hello Elementor, and Elementor 4.1.5 are installed
2. Ensure Flexbox Containers and Editor V4 are enabled in Elementor settings
3. Verify all pages loaded without console errors (check browser DevTools)
4. Check WordPress error logs: `wp-content/debug.log`

---

Generated: 2026-07-21  
Elementor Version: 4.1.5  
WordPress Version: 6.8.2  
Theme: Hello Elementor 3.4.9
