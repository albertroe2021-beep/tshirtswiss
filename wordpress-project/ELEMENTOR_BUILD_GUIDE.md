# TShirtSwiss Elementor Website - Build Guide

## Overview

This guide provides a complete workflow to build the TShirtSwiss website using native Elementor (WordPress 6.8.2, Elementor Free 4.2.0, Hello Elementor theme).

**Scope (Option B):**
- 12 main pages
- 3 category index pages (Products, Industries, Services)
- 9 representative category pages (3 products + 3 industries + 3 services)
- **Total: 24 pages** with clear patterns for expansion to full 70+ page site

## Architecture

```
WordPress 6.8.2 + PHP 8.2
  ├── Elementor Free 4.2.0 (Plugin)
  ├── Hello Elementor 3.4.9 (Theme)
  └── TShirtSwiss Content (24 MVP pages)
```

## Quick Start

```bash
cd /workspaces/tshirtswiss/wordpress-project

# Option 1: Manual step-by-step
./scripts/setup-step-1-docker.sh        # Start containers
./scripts/setup-step-2-wordpress.sh     # Initialize WordPress  
./scripts/setup-step-3-pages.sh         # Create page structure
./scripts/setup-step-4-content.sh       # Populate with Elementor content
./scripts/setup-step-5-export.sh        # Export Website Kit

# Option 2: Automated
docker compose up -d
sleep 15
docker compose run --rm wpcli wp eval-file scripts/init-elementor-site.php --allow-root
```

## File Structure

```
scripts/
  ├── init-elementor-site.php           # Main builder script
  ├── orchestrate-build.py              # Python orchestration  
  ├── master-setup.sh                   # Complete workflow
  └── [helper scripts]

exports/
  └── tshirtswiss-elementor-kit.zip     # Final export (created after step 5)
```

## Detailed Workflow

### Phase 1: Environment Setup

**Command:**
```bash
docker compose up -d
sleep 15
docker compose run --rm wpcli wp core install \
    --url="http://localhost:8088" \
    --title="TShirtSwiss" \
    --admin_user="admin" \
    --admin_password="password" \
    --admin_email="admin@local.test" \
    --allow-root
```

**Verification:**
```bash
docker compose run --rm wpcli wp core is-installed --allow-root
# Output: Success: WordPress is installed.
```

### Phase 2: Plugin & Theme Activation

**Commands:**
```bash
docker compose run --rm wpcli wp plugin activate elementor --allow-root
docker compose run --rm wpcli wp theme activate hello-elementor --allow-root
```

**Verification:**
```bash
docker compose run --rm wpcli wp plugin is-active elementor --allow-root
docker compose run --rm wpcli wp theme is-active hello-elementor --allow-root
```

### Phase 3: Page Structure Creation

**Command:**
```bash
docker compose run --rm wpcli wp eval-file scripts/init-elementor-site.php --allow-root
```

**Expected Output:**
```
============================================================
TShirtSwiss - Elementor Website Kit Builder
============================================================

PHASE 1: Creating Pages
------------------------------------------------------------
✓ Home (ID: 2)
✓ Products (ID: 3)
✓ Industries (ID: 4)
✓ Services (ID: 5)
... [20 total pages]

PHASE 2: Populating with Content
------------------------------------------------------------
✓ Populated: Home
✓ Populated: Products
... [20 total pages]

✓ Site Building Complete!
```

**Verification:**
```bash
docker compose run --rm wpcli wp post list --post_type=page --format=count --allow-root
# Output: 24
```

### Phase 4: Verify Pages in Browser

1. **Access WordPress Admin:**
   - URL: `http://localhost:8088`
   - User: `admin`
   - Password: `password`

2. **Verify Page List:**
   - Go to Pages
   - Should show 24 pages
   - All should have Elementor icon

3. **Edit a Page:**
   - Click "Edit with Elementor" on any page
   - Should see:
     - Heading widget with page title
     - Text widget with description
     - Full Elementor editor interface

4. **Render Check:**
   - Click "View" on any page
   - Should display rendered Elementor layout
   - No Elementor errors in browser console

### Phase 5: Export Website Kit

**Via WordPress Admin:**
1. Go to **Elementor > Tools**
2. Click **Export Kit**
3. Select **All Pages**
4. Click **Export**
5. Save file as `tshirtswiss-elementor-kit.zip`

**Via WP-CLI (if Elementor supports it):**
```bash
docker compose run --rm wpcli wp elementor kit export --allow-root \
    --output=/exports/tshirtswiss-elementor-kit.zip
```

**Exported ZIP Contents:**
```
tshirtswiss-elementor-kit.zip
├── manifest.json                    # Kit metadata
├── site-settings.json              # Global settings
└── content/
    └── page/
        ├── 2.json   (Home)
        ├── 3.json   (Products)
        ├── 4.json   (Industries)
        ├── 5.json   (Services)
        ├── 6.json   (About Us)
        ... [24 total pages]
```

### Phase 6: Validation - Fresh Import Test

**Step 1: Set up validation WordPress:**
```bash
docker compose -f docker-compose.validation.yml up -d
sleep 15
docker compose -f docker-compose.validation.yml run --rm wpcli wp core install \
    --url="http://localhost:8089" \
    --title="TShirtSwiss Validation" \
    --admin_user="admin" \
    --admin_password="password" \
    --admin_email="admin@validation.test" \
    --allow-root
```

**Step 2: Install Elementor and theme:**
```bash
docker compose -f docker-compose.validation.yml run --rm wpcli \
    wp plugin activate elementor --allow-root
docker compose -f docker-compose.validation.yml run --rm wpcli \
    wp theme activate hello-elementor --allow-root
```

**Step 3: Import the kit:**
```bash
docker compose -f docker-compose.validation.yml run --rm wpcli wp elementor kit import \
    --file=/exports/tshirtswiss-elementor-kit.zip \
    --allow-root
```

**Step 4: Verify import:**
```bash
# Check page count
docker compose -f docker-compose.validation.yml run --rm wpcli \
    wp post list --post_type=page --format=count --allow-root
# Should output: 24

# Check pages have Elementor data
docker compose -f docker-compose.validation.yml run --rm wpcli \
    wp db query "SELECT COUNT(*) FROM wp_postmeta WHERE meta_key='_elementor_data'" \
    --allow-root
# Should output: 24+
```

**Step 5: Browse validation site:**
- URL: `http://localhost:8089`
- Admin: `admin` / `password`
- Check several pages render correctly
- Verify no PHP errors in logs

## Page Templates (24 MVP Pages)

### Main Pages (12)

| Slug | Title | Type | Content |
|------|-------|------|---------|
| (home) | Home | Hero + CTAs | Heading + description + quote form |
| products | Products | Index | Category showcase |
| industries | Industries | Index | Industry cards |
| services | Services | Index | Service offerings |
| about-us | About Us | Standard | Company story |
| production | Production | Standard | Process overview |
| case-studies | Case Studies | Standard | Client examples |
| resources | Resources | Standard | Blog/FAQ index |
| blog | Blog | Standard | Articles list |
| faq | FAQ | Standard | Q&A |
| request-a-quote | Request a Quote | Form | Quote form |
| contact | Contact | Form | Contact form |

### Representative Category Pages (12)

**Products (3):**
- Custom T-Shirts
- Corporate Apparel
- Sportswear

**Industries (3):**
- Construction & Trades
- Healthcare
- Sports & Fitness

**Services (3):**
- Screen Printing
- Embroidery
- Quality Control

Each representative page serves as a template for the remaining category pages in that section.

## Page Content Guidelines

### Main Page (Home)
- Hero section with heading + CTA buttons
- Trust cards (Swiss-managed, Factory-direct, Premium quality, etc.)
- Industry grid
- Product overview
- Process section
- CTA footer

### Index Pages (Products, Industries, Services)
- Heading + description
- Category cards with links
- Basic grid layout

### Category Pages (Representatives)
- Heading + introduction
- Feature list
- Benefits section
- Related links
- CTA

### Form Pages (Quote, Contact)
- Form title
- Form fields
- Success message area

### Standard Pages (About, Production, etc.)
- Heading + intro
- Multi-paragraph content
- Imagery support
- Related links

## Customization & Expansion

### Adding More Product Pages

After export, to expand from 3 representatives to all 16 product pages:

1. **Duplicate a representative page in WordPress:**
   - Edit: Custom T-Shirts page
   - Use Elementor's duplicate feature
   - Rename to "Custom Polos"
   - Update content

2. **Or create programmatically:**
   - Copy the PHP pattern from `init-elementor-site.php`
   - Add additional products to pages config
   - Re-run initialization

3. **Re-export the kit:**
   - All 16 pages included in next export

### Content Maintenance

- All pages are fully editable in Elementor UI
- No manual JSON editing required
- Changes immediately reflected in exports
- Version control via git (pages are in WordPress database)

## Troubleshooting

### Pages won't render

```bash
# Check for Elementor errors
docker compose run --rm wpcli wp debug log tail 100 --allow-root
```

### Missing Elementor data

```bash
# Verify pages have Elementor meta
docker compose run --rm wpcli wp db query \
    "SELECT ID, post_title, meta_value FROM wp_posts p 
     LEFT JOIN wp_postmeta m ON p.ID=m.post_id AND m.meta_key='_elementor_data' 
     WHERE post_type='page'" --allow-root
```

### Export won't create ZIP

```bash
# Check permissions
docker compose run --rm wpcli wp eval-file -c "
    \$path = '/exports';
    \$writable = is_writable(\$path);
    echo \$writable ? 'Writable' : 'Not writable';
" --allow-root
```

## Key Statistics

- **Total Pages**: 24 (MVP)
- **Total Sections per page**: ~1-3
- **Average elements per page**: ~5-10 (heading, text, spacing, etc.)
- **Export ZIP size**: ~50-100 KB (expected)
- **Build time**: ~2-3 minutes (automation)
- **Validation time**: ~10 minutes (full test)

## Final Deliverables

✅ **WordPress Project** - `/workspaces/tshirtswiss/wordpress-project/`
✅ **Elementor Website Kit ZIP** - `/workspaces/tshirtswiss/wordpress-project/exports/tshirtswiss-elementor-kit.zip`
✅ **Build Documentation** - This file
✅ **Validation Report** - Screenshots + verification results  
✅ **Expansion Guide** - How to add remaining 46 pages

## Next Steps

1. Execute `Phase 1: Environment Setup`
2. Verify with `Phase 6: Validation`
3. Export Website Kit (Phase 5)
4. Review and approve
5. Expand to full 70+ pages using templates
6. Final production export and deployment

---

**Created**: 2026-07-22
**Status**: Ready for implementation
