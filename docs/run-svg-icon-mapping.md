# Running the SVG Icon Mapping Script

The repository includes a script for applying the spreadsheet-driven SVG icon mapping across the static HTML pages.

Script path:

`script/apply_svg_icon_mapping.py`

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
