# TShirtSwiss Elementor Reference Kit – Import Instructions

## Download the Kit

**Direct download link:**
```
https://github.com/albertroe2021-beep/tshirtswiss/raw/elementor-reference-library/wordpress-project/exports/tshirtswiss-reference-kit.zip
```

Or use this shortened version:
- Right-click and "Save link as..." to your computer

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

### For your live WordPress site (tshirtswiss.ch)

#### Prerequisites
Before importing, ensure your WordPress installation has:
- ✅ WordPress 6.8+
- ✅ Hello Elementor theme (3.4.9+) installed and activated
- ✅ Elementor Free (4.1.5) installed and activated
- ✅ Flexbox Containers enabled (Elementor → Settings → Features → Flexbox Containers)
- ✅ Nested Elements enabled (Elementor → Settings → Features → Nested Elements)
- ✅ Editor V4 enabled (Elementor → Settings → Features → Editor Improvements)

#### Import Steps

1. **Log in to WordPress Admin**
   - Go to: `http://tshirtswiss.ch/wp-admin`
   - Enter your credentials

2. **Navigate to Elementor Import**
   - Click **Elementor** in the left sidebar
   - Click **Tools**
   - Click **Import & Export**

3. **Upload the kit**
   - Click **Import Kit** tab
   - Click **Choose File**
   - Select the downloaded `tshirtswiss-reference-kit.zip`
   - Click **Open**

4. **Start the import**
   - Click the **Import** button
   - Wait for the import to complete (this may take a few minutes)
   - You should see a success message

5. **View imported pages**
   - Go to **Pages** in the left sidebar
   - You should see 41 new pages (English, German, French variants)
   - Go to **Elementor Library** to see 16 imported templates

### Alternative: For local testing (Docker setup)

```bash
# Option A: Use the included wordpress-project docker setup
cd wordpress-project
cp .env.example .env
docker compose up -d
docker compose run --rm wpcli bash /scripts/setup_wordpress.sh
```

Then follow the same import steps above but at `http://localhost:8088/wp-admin`

### Verify import was successful

After import completes:

1. **Check Pages dashboard**
   - WordPress Admin → **Pages**
   - Should show 41 pages total
   - Look for pages like: Home, Products, Services, Industries, etc. (in English, German, and French)

2. **Check Templates**
   - WordPress Admin → **Elementor Library**
   - Should show 16 templates
   - Templates like: "EN Header", "DE Footer", "FR Product Child", etc.

3. **Check a page in Elementor Editor**
   - Open any page (e.g., Home)
   - Click **Edit with Elementor**
   - Verify you see Lorem Ipsum placeholder content and the layout structure

**If import fails:**
- Check browser console (F12) for errors
- Verify Elementor and Hello theme are activated
- Check WordPress error log: `wp-content/debug.log`
- Try importing in smaller batches if the file size causes timeout

### Customize placeholder content after import

All pages and templates are seeded with **Lorem Ipsum placeholder content**.

To customize:

1. Go to **Pages** in WordPress Admin
2. Open any page (e.g., "Home")
3. Click **Edit with Elementor** button
4. Replace placeholder text with your own content
5. Update placeholder images with real product/service images
6. Verify navigation links point to correct pages
7. Test forms and configure with your form provider if needed
8. Check responsive layout at different widths (desktop 1200px, tablet 768px, mobile 360px)
9. Click **Publish** when satisfied

Repeat for all pages and templates.

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
