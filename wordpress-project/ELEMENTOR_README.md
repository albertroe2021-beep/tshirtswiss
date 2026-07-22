# TShirtSwiss Elementor Website - Build & Deploy

## Quick Summary

This project builds a production-ready WordPress + Elementor website for TShirtSwiss with:

- **24 pages** MVP (main pages + representative categories)
- **Native Elementor** (no manual JSON generation)
- **Hello Elementor theme**
- **Complete export** as Website Kit ZIP
- **Fresh WordPress validation** workflow

## Quick Start

```bash
cd /workspaces/tshirtswiss/wordpress-project

# Execute step-by-step
./scripts/setup-step-1-docker.sh          # ~20 seconds
./scripts/setup-step-2-wordpress.sh       # ~30 seconds
./scripts/setup-step-3-pages.sh           # ~2 minutes
./scripts/setup-step-4-verify.sh          # ~10 seconds
# [Manual: Export via WordPress admin UI]
./scripts/setup-step-5-export.sh          # Instructions
./scripts/setup-step-6-validate.sh        # ~3 minutes
```

**Total time: ~6-7 minutes (plus manual export step)**

## What You Get

```
WordPress 6.8.2 + Elementor 4.2.0 + Hello Elementor
├── 12 Main Pages
│   ├── Home
│   ├── Products
│   ├── Industries
│   ├── Services
│   ├── About Us
│   ├── Production
│   ├── Case Studies
│   ├── Resources
│   ├── Blog
│   ├── FAQ
│   ├── Request a Quote
│   └── Contact
├── 3 Category Indexes (Products, Industries, Services)
├── 9 Representative Category Pages (3 each category)
└── exports/tshirtswiss-elementor-kit.zip (Website Kit)
```

## File Structure

```
/workspaces/tshirtswiss/wordpress-project/
├── scripts/
│   ├── init-elementor-site.php        (Main builder)
│   ├── setup-step-1-docker.sh         (Environment)
│   ├── setup-step-2-wordpress.sh      (WordPress install)
│   ├── setup-step-3-pages.sh          (Create pages)
│   ├── setup-step-4-verify.sh         (Verify)
│   ├── setup-step-5-export.sh         (Export instructions)
│   └── setup-step-6-validate.sh       (Fresh import test)
├── docker-compose.yml                 (Main environment)
├── docker-compose.validation.yml      (Validation environment)
├── ELEMENTOR_BUILD_GUIDE.md           (Detailed guide)
├── README.md                          (This file)
└── exports/
    └── tshirtswiss-elementor-kit.zip  (Created by export step)
```

## Step-by-Step Instructions

### Step 1: Docker Environment
Brings up fresh WordPress + MySQL + WP-CLI containers

```bash
./scripts/setup-step-1-docker.sh
```

**Expected:**
- Docker containers running
- MySQL database ready
- WordPress directory mounted

**Access:**
- MySQL: `localhost:3306`
- WordPress: Not yet installed

---

### Step 2: WordPress Installation
Installs WordPress, activates Elementor plugin and Hello Elementor theme

```bash
./scripts/setup-step-2-wordpress.sh
```

**Expected:**
- WordPress installed and configured
- Elementor plugin active
- Hello Elementor theme active
- Admin access ready

**Access:**
- WordPress Admin: `http://localhost:8088/wp-admin/`
- User: `admin`
- Password: `password`

---

### Step 3: Page Creation
Creates all 24 pages with Elementor structure

```bash
./scripts/setup-step-3-pages.sh
```

**Expected:**
- 24 pages created in WordPress
- Each page has Elementor enabled
- Each page has basic content (heading + description)
- Pages are published

**Access:**
- Check pages: `http://localhost:8088/wp-admin/edit.php?post_type=page`

---

### Step 4: Verification
Verifies page creation and Elementor integration

```bash
./scripts/setup-step-4-verify.sh
```

**Expected Output:**
```
Listing all created pages:
ID    post_title
2     Home
3     Products
...
25    Quality Control

Pages with Elementor content:
pages_with_elementor
24
```

---

### Step 5: Export Website Kit
**Manual step** - Export via WordPress admin UI

1. **Open WordPress Admin:**
   ```
   URL: http://localhost:8088/wp-admin/
   User: admin
   Password: password
   ```

2. **Export the Kit:**
   - Go to menu: **Elementor** > **Tools**
   - Click: **Export Kit**
   - Select: **All Pages**
   - Click: **Export**
   - Save: `/workspaces/tshirtswiss/wordpress-project/exports/tshirtswiss-elementor-kit.zip`

3. **Verify Export:**
   ```bash
   ls -lh exports/tshirtswiss-elementor-kit.zip
   unzip -l exports/tshirtswiss-elementor-kit.zip | head -20
   ```

---

### Step 6: Validation - Fresh Import Test
Tests importing the exported kit on a fresh WordPress installation

```bash
./scripts/setup-step-6-validate.sh
```

**Expected:**
- Fresh WordPress installed on `localhost:8089`
- Website Kit imported
- All 24 pages present
- Pages render without errors

**Verification:**
- URL: `http://localhost:8089`
- Admin: `http://localhost:8089/wp-admin/`
- User: `admin`
- Password: `password`

**Manual checks:**
1. Browse to `http://localhost:8089` - should show homepage
2. Check "Pages" in admin - should list 24 pages
3. Click "Edit with Elementor" on a page - should open editor
4. Click "View" - page should render
5. Check browser console - no errors

---

## Usage

### Access Running WordPress

**Development (with pages):**
```
URL: http://localhost:8088
Admin: http://localhost:8088/wp-admin
User: admin / password
```

**Validation (after import):**
```
URL: http://localhost:8089
Admin: http://localhost:8089/wp-admin
User: admin / password
```

### Edit Pages in Elementor

1. Go to WordPress Admin
2. Pages > Edit any page
3. Click "Edit with Elementor"
4. Edit in Elementor visual editor
5. Publish changes
6. Changes reflected immediately

### View Exported Kit

```bash
# Contents of export ZIP
unzip -l exports/tshirtswiss-elementor-kit.zip

# Extract and inspect
unzip -d /tmp/kit-inspection exports/tshirtswiss-elementor-kit.zip
cat /tmp/kit-inspection/manifest.json | jq .
cat /tmp/kit-inspection/content/page/2.json | jq . | head -50
```

## Troubleshooting

### Containers won't start
```bash
# Check logs
docker compose logs wordpress
docker compose logs db

# Reset and try again
docker compose down -v
docker compose up -d
sleep 15
```

### WordPress won't install
```bash
# Check database connection
docker compose run --rm wpcli wp db check --allow-root

# Reset database
docker compose run --rm wpcli wp db reset --yes --allow-root
docker compose run --rm wpcli wp core install ...
```

### Export file not created
```bash
# Check export directory permissions
docker compose run --rm wpcli wp eval-file -c "
    echo is_writable('/exports') ? 'OK' : 'NOT WRITABLE';
" --allow-root

# Export should be saved to:
/workspaces/tshirtswiss/wordpress-project/exports/tshirtswiss-elementor-kit.zip
```

### Import fails on validation
```bash
# Check validation WordPress installation
docker compose -f docker-compose.validation.yml run --rm wpcli wp core is-installed --allow-root

# Check Elementor is active
docker compose -f docker-compose.validation.yml run --rm wpcli wp plugin is-active elementor --allow-root

# Check theme is active
docker compose -f docker-compose.validation.yml run --rm wpcli wp theme is-active hello-elementor --allow-root
```

## Customization Guide

### Add More Pages (Expand from 24 to 70+)

1. **Duplicate existing pages in WordPress:**
   - Edit: "Custom T-Shirts" page
   - Use Elementor's duplicate feature
   - Rename: "Custom Polos"
   - Update content
   - Publish

2. **Or create programmatically:**
   - Edit `init-elementor-site.php`
   - Add to `get_pages_config()` method
   - Re-run: `docker compose run --rm wpcli wp eval-file scripts/init-elementor-site.php --allow-root`

3. **Re-export:**
   - Follow Step 5 again
   - All new pages included in export

### Customize Content

All pages are fully editable in Elementor:
- Add/remove sections
- Edit text, headings, images
- Add buttons, forms, galleries
- Change layouts, colors, fonts
- Add custom CSS

Changes are immediately available for re-export.

### Change Theme/Styling

1. **Theme options:**
   - Appearance > Customize
   - Elementor-specific settings

2. **Global colors/fonts:**
   - Elementor > Global Settings
   - Define brand colors, fonts
   - Apply to all pages

3. **Custom CSS:**
   - Elementor > Custom Code
   - Add custom CSS/JS

## Key Information

| Property | Value |
|----------|-------|
| WordPress Version | 6.8.2 |
| Elementor Version | Free 4.2.0 |
| Theme | Hello Elementor 3.4.9 |
| PHP Version | 8.2 |
| MySQL Version | 8.0 |
| Pages (MVP) | 24 |
| Build Time | ~7 minutes |
| Export Size | ~50-100 KB |
| Admin User | admin |
| Admin Password | password |
| Dev URL | http://localhost:8088 |
| Validation URL | http://localhost:8089 |

## What's Included

✅ **Complete WordPress Installation**
✅ **Elementor Plugin + Hello Elementor Theme**
✅ **24 Pre-built Pages**
✅ **Elementor Page Structures**
✅ **Export as Website Kit ZIP**
✅ **Fresh Import Validation**
✅ **Docker Compose Setup**
✅ **Step-by-step Scripts**
✅ **Documentation**

## What's NOT Included

❌ Content is minimal (structure only)
❌ Images are not included
❌ CSS customization beyond defaults
❌ Multi-language setup (WPML)
❌ SEO plugins

These can be added after initial build/validation.

## Next Steps After Validation

1. ✅ **Site Building Complete**
2. ✅ **Export Validated**
3. **→ Expand to 70+ pages** (duplicate templates)
4. **→ Add real content** (via Elementor editor)
5. **→ Add images** (media library)
6. **→ Customize styling** (Elementor global settings)
7. **→ Final export** (with full content)
8. **→ Deploy to production** (via Website Kit import)

## Support

**For detailed build process:** See `ELEMENTOR_BUILD_GUIDE.md`

**For environment setup:** See `docker-compose.yml` and `.env.example`

**For Elementor documentation:** https://elementor.com/docs/

## License

This project uses:
- WordPress (GPL)
- Elementor Free (GPL)
- Hello Elementor (GPL)

See individual project licenses.

---

**Created:** 2026-07-22
**Status:** Ready for execution
**Version:** MVP Phase (24 pages)
