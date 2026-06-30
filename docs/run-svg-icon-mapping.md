# Running the SVG Icon Mapping Script

The repository includes a script for applying the spreadsheet-driven SVG icon mapping across the static HTML pages.

Script path:

`scripts/apply_svg_icon_mapping.py`

Run from the repository root.

Dry run first:

`python scripts/apply_svg_icon_mapping.py --dry-run --verbose`

Apply the changes:

`python scripts/apply_svg_icon_mapping.py --verbose`

Then review and commit the generated page changes.

The script uses:

- `SVG number to phrase.xlsx` as the placement guide
- the master Ref# to SVG registry
- the standard TShirtSwiss red outline icon style

Recommended workflow:

1. Pull the latest repository.
2. Run the dry run command.
3. Review the reported files and replacement counts.
4. Run the apply command.
5. Review the changed HTML pages.
6. Commit and push the result.

## Browser-only option

Use GitHub Codespaces from the repository page if you do not have a local development environment.

1. Open the repository on GitHub.
2. Click **Code**.
3. Open the **Codespaces** tab.
4. Create a codespace on `main`.
5. Open a terminal in the browser.
6. Run the dry-run command above.
7. Run the apply command above.
8. Commit and push from the Codespaces Source Control panel.

## Current implementation status

The repository also contains a service-worker based icon mapping layer in `site-header-sw.js`. That layer performs live icon normalisation on navigated HTML pages. The Python script is intended for permanent static HTML updates so the mapped icons are written directly into each page.
