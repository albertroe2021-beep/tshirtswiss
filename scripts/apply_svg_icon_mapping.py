#!/usr/bin/env python3
"""Apply exact TShirtSwiss SVG Ref# mappings across static HTML files.

This phrase-aware replacement engine uses the exact rows from
`SVG number to phrase(2).xlsx`:

    Term in Website -> Ref# -> SVG filename

It removes legacy inline SVG sprites, replaces old `<use>` SVGs, and updates the
icon next to each mapped phrase without guessing by category.
"""
from __future__ import annotations

import argparse
import csv
import os
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ROOTS = ["pages"]
SKIP_DIRS = {".git", "node_modules", "dist", "build", ".cache", "__pycache__"}

REF_TO_FILE = {
    "1": "shield-with-cross-svgrepo-com (1).svg",
    "2": "factory-building-svgrepo-com.svg",
    "3": "quality-5-svgrepo-com.svg",
    "4": "quality-5-svgrepo-com.svg",
    "5": "quality-5-svgrepo-com.svg",
    "6": "plane-svgrepo-com (1).svg",
    "7": "stopwatch-svgrepo-com.svg",
    "8": "handshake-svgrepo-com.svg",
    "9": "person-with-headset-thin-outline-symbol-in-a-circle-svgrepo-com (1).svg",
    "10": "speech-bubbles-conversation-svgrepo-com (1).svg",
    "11": "computer-monitor-svgrepo-com.svg",
    "12": "review-checkmark-svgrepo-com.svg",
    "13": "design-svgrepo-com.svg",
    "14": "computer-monitor-svgrepo-com.svg",
    "15": "sketch-svgrepo-com.svg",
    "16": "review-checkmark-svgrepo-com.svg",
    "17": "quality-5-svgrepo-com.svg",
    "18": "fabric-material-svgrepo-com.svg",
    "19": "design-svgrepo-com.svg",
    "20": "factory-building-svgrepo-com.svg",
    "21": "sewing-machine-sew-svgrepo-com (1).svg",
    "22": "scissors-svgrepo-com.svg",
    "23": "needle-svgrepo-com.svg",
    "24": "paint-roller-svgrepo-com.svg",
    "25": "airport-baggage-conveyor-svgrepo-com.svg",
    "26": "airport-baggage-conveyor-svgrepo-com.svg",
    "27": "box-svgrepo-com.svg",
    "28": "plane-svgrepo-com (1).svg",
    "29": "tshirt-svgrepo-com (2).svg",
    "30": "cotton-polo-shirt-svgrepo-com.svg",
    "31": "sweatshirt-svgrepo-com.svg",
    "32": "construction-worker-svgrepo-com.svg",
    "33": "shirt-svgrepo-com.svg",
    "34": "team-uniform-svgrepo-com.svg",
    "35": "paralympic-swimming-silhouette-svgrepo-com.svg",
    "36": "boxing-shorts-svgrepo-com.svg",
    "37": "boxing-shorts-svgrepo-com.svg",
    "38": "doctor-female-svgrepo-com.svg",
    "39": "doctor-female-svgrepo-com.svg",
    "40": "cap-svgrepo-com.svg",
    "41": "jacket-svgrepo-com.svg",
    "42": "shopping-bag-svgrepo-com.svg",
    "43": "team-uniform-svgrepo-com.svg",
    "44": "barcode-sticker-svgrepo-com.svg",
    "45": "barcode-sticker-svgrepo-com.svg",
    "46": "tag-2-svgrepo-com.svg",
    "47": "barcode-sticker-svgrepo-com.svg",
    "48": "barcode-sticker-svgrepo-com.svg",
    "49": "box-svgrepo-com.svg",
    "50": "shopping-bag-svgrepo-com.svg",
    "51": "barcode-sticker-svgrepo-com.svg",
    "52": "print-products-svgrepo-com (1).svg",
    "53": "print-products-svgrepo-com (1).svg",
    "54": "print-products-svgrepo-com (1).svg",
    "55": "print-products-svgrepo-com (1).svg",
    "56": "needle-svgrepo-com.svg",
    "57": "fabric-material-svgrepo-com.svg",
    "58": "fabric-material-svgrepo-com.svg",
    "59": "fabric-material-svgrepo-com.svg",
    "60": "bamboo-svgrepo-com.svg",
    "61": "fabric-material-svgrepo-com.svg",
    "62": "keep-dry-svgrepo-com.svg",
    "63": "fabric-material-svgrepo-com.svg",
    "64": "germs-svgrepo-com.svg",
    "65": "sun-cream-sun-protection-svgrepo-com.svg",
    "66": "construction-worker-svgrepo-com.svg",
    "67": "doctor-female-svgrepo-com.svg",
    "68": "hotel-reception-svgrepo-com.svg",
    "69": "team-uniform-svgrepo-com.svg",
    "70": "boxing-shorts-svgrepo-com.svg",
    "71": "shirt-svgrepo-com.svg",
    "72": "shopping-bag-svgrepo-com.svg",
    "73": "facebook-svgrepo-com.svg",
    "74": "rock-and-roll-concert-svgrepo-com.svg",
    "75": "bamboo-svgrepo-com.svg",
    "76": "recycling-arrows-svgrepo-com.svg",
    "77": "recycling-arrows-svgrepo-com.svg",
    "78": "recycling-arrows-svgrepo-com.svg",
    "79": "recycling-arrows-svgrepo-com.svg",
    "80": "recycling-arrows-svgrepo-com.svg",
    "81": "water-drop-svgrepo-com.svg",
    "82": "recycling-arrows-svgrepo-com.svg",
    "83": "computer-monitor-svgrepo-com.svg",
    "84": "computer-monitor-svgrepo-com.svg",
    "85": "downloads-svgrepo-com.svg",
    "86": "book-svgrepo-com.svg",
    "87": "book-svgrepo-com.svg",
    "88": "book-svgrepo-com.svg",
    "89": "search-alt-2-svgrepo-com.svg",
    "90": "person-with-headset-thin-outline-symbol-in-a-circle-svgrepo-com (1).svg",
    "91": "person-with-headset-thin-outline-symbol-in-a-circle-svgrepo-com (1).svg",
    "92": "whatsapp-svgrepo-com.svg",
    "93": "email-svgrepo-com.svg",
    "94": "shield-with-cross-svgrepo-com (1).svg",
    "95": "email-svgrepo-com.svg",
    "96": "person-with-headset-thin-outline-symbol-in-a-circle-svgrepo-com (1).svg"
}

PHRASE_TO_REF = [[1,"Swiss Managed"],[2,"Factory in Thailand"],[3,"Premium Quality"],[6,"Worldwide Shipping"],[1,"Swiss Quality Standards"],[2,"Factory Direct Pricing"],[4,"Strict Quality Control"],[18,"Fabric"],[24,"Colors"],[13,"Fit & Sizes"],[15,"Decoration"],[12,"Finishing"],[10,"Consultation"],[16,"Sample & Approval"],[2,"Production"],[5,"Quality Check"],[6,"Shipping"],[2,"Factory Direct"],[4,"Quality Control"],[8,"Long Term Partner"],[29,"View All Products"],[29,"Custom Products"],[33,"Brand & Uniform Ready"],[34,"Sportswear Options"],[31,"Private Label Support"],[29,"Garments"],[11,"Branding"],[27,"Packing"],[19,"Fit & Length"],[19,"Fit & Closure"],[18,"Materials"],[13,"Sizes"],[50,"Handles"],[15,"Artwork"],[33,"Team Identity"],[11,"Campaigns"],[74,"Audience"],[32,"Safety First"],[62,"All Weather"],[3,"Easy Care"],[34,"Team Identity"],[75,"Sustainable Options"],[40,"Comfort First"],[34,"Team Clarity"],[11,"Professional Branding"],[90,"Reliable Reorders"],[68,"Guest Ready"],[67,"All Day Comfort"],[34,"Active Comfort"],[29,"Retail Ready"],[74,"Event Ready"],[32,"Training Durability"],[15,"Full Artwork"],[33,"Professional Look"],[11,"Brand Control"],[16,"Team Planning"],[7,"Deadline Focused"],[15,"Strong Artwork"],[6,"Easy Distribution"],[44,"Label Support"],[49,"Drop Planning"],[49,"Packaging"],[74,"Audience Ready"],[11,"Brand Details"],[30,"Retail Feel"],[90,"Consultation & Specs"],[18,"Material Planning"],[16,"Sampling"],[2,"Bulk Production"],[6,"Packing & Shipping"],[32,"Workwear & Uniforms"],[33,"Corporate Apparel"],[34,"Sportswear & Activewear"],[40,"Private Label Brands"],[74,"Event Merchandise"],[42,"Retail Collections"],[41,"Fashion Brands"],[18,"Material Options"],[76,"Reduced Waste Planning"],[2,"Responsible Production"],[8,"Ethical Labour Practices"],[12,"Concept Review"],[15,"Material Direction"],[13,"Fit & Construction"],[16,"Review & Revision"],[2,"Production Ready"],[15,"Private Label"],[14,"Ecommerce Brands"],[34,"Sportswear"],[32,"Workwear"],[30,"Retail Lines"],[74,"Merch Drops"],[16,"Artwork Review"],[24,"Print Planning"],[29,"Garment Check"],[16,"Sample/Test"],[2,"Production"],[17,"Final QC"],[74,"Event Merch"],[29,"Promotional"],[38,"Uniforms"],[36,"Gym Apparel"],[14,"Brands"],[2,"Bulk Orders"],[15,"Panel Layout"],[35,"Rashguards"],[36,"MMA Shorts"],[36,"Muay Thai"],[34,"Teamwear"],[34,"Sportswear"],[31,"Fitness"],[17,"Brand Review"],[47,"Label Planning"],[11,"Artwork Setup"],[16,"Sample Review"],[17,"Integration"],[16,"Requirement Review"],[89,"Packaging Plan"],[27,"Packing Setup"],[3,"Verification"],[6,"Delivery Ready"],[90,"Delivery Review"],[88,"Packing Plan"],[51,"Carton Labelling"],[86,"Documentation"],[6,"Shipment Handover"],[96,"Brand Consultation"],[11,"Product Planning"],[2,"Production"],[27,"Packing & Delivery"],[73,"Creator Merch"],[41,"Streetwear Drops"],[35,"Activewear Labels"],[33,"Corporate Merch"],[76,"Waste-Aware Planning"],[2,"Reliable Production"],[90,"Brief Review"],[19,"Spec Planning"],[21,"Sample Build"],[16,"Branding Check"],[10,"Feedback"],[3,"Approval"],[90,"Free Consultation"],[10,"Sample Advice"],[8,"No Obligation"],[7,"Fast Response"],[11,"Digitising"],[23,"Thread Planning"],[4,"Sample Check"],[2,"Production"],[30,"Corporate Polos"],[40,"Caps"],[41,"Jackets"],[68,"Hospitality"],[32,"Workwear"],[10,"Transfer Plannning"],[12,"Sample or Test"],[86,"Information Planning"],[27,"Final Packing"],[15,"Spec Review"],[18,"Material Check"],[16,"Construction Check"],[11,"Branding Review"],[27,"Packing Check"],[6,"Shipment Ready"],[1,"Swiss-Managed Communication"],[2,"Thailand Manufacturing Base"],[3,"Quality-First Approach"],[8,"Brand-Safe Execution"],[9,"Request a Quote"],[95,"Email"],[71,"How do I develop a garment?"],[22,"Do I need a sample?"],[14,"How should I brand apparel?"],[27,"How do I prepare for shipping?"],[90,"ORDERING & PLANNING"],[19,"SAMPLING & CUSTOMISATION"],[21,"PRINTING & BRANDING"],[2,"PRODUCTION & DELIVERY"],[14,"PRIVATE LABEL"]]
PHRASE_TO_REF.sort(key=lambda item: len(item[1]), reverse=True)

LEGACY_USE_TO_REF = {
    "icon-swiss-cross": 1,
    "icon-factory": 2,
    "icon-award-check": 3,
    "icon-box-plane": 6,
    "icon-handshake": 8,
    "icon-chat": 10,
    "icon-tshirt": 29,
    "icon-clipboard-check": 4,
    "icon-package": 27,
    "icon-mail": 95,
    "icon-phone": 91,
    "icon-location": 94,
}

ICON_CLASS_PARTS = ("top-ico", "trust-icon", "feature-icon", "cat-icon", "process-icon", "step-icon", "section-icon", "mail-icon", "icon", "ico")
BLOCK_CLASS_PARTS = ("card", "item", "step", "tile", "feature", "trust", "resource", "process", "value", "service", "product", "industry", "mini", "tag")

@dataclass
class Replacement:
    path: str
    phrase: str
    ref: int
    svg_file: str
    count: int


def html_src_for(path: Path, ref: int) -> str:
    filename = REF_TO_FILE.get(str(int(ref)), REF_TO_FILE["4"])
    rel = os.path.relpath(REPO_ROOT / filename, path.parent).replace(os.sep, "/")
    return quote(rel, safe="/().-_")


def icon_img(path: Path, ref: int) -> str:
    filename = REF_TO_FILE.get(str(int(ref)), REF_TO_FILE["4"])
    return f'<img class="svg-icon ts-svg-mapped-icon" src="{html_src_for(path, ref)}" alt="" aria-hidden="true" data-ref="{ref}" data-svg-file="{filename}">'


def esc(text: str) -> str:
    return re.escape(text)


def class_regex(parts: tuple[str, ...]) -> str:
    return r"(?:" + "|".join(re.escape(p) for p in parts) + r")"


def iter_html_files(roots: list[str]):
    for root in roots:
        root_path = (REPO_ROOT / root).resolve()
        if not root_path.exists():
            continue
        if root_path.is_file() and root_path.suffix.lower() == ".html":
            yield root_path
            continue
        for path in root_path.rglob("*.html"):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            yield path


def ensure_css(html: str) -> tuple[str, int]:
    marker = "ts-svg-mapped-icon-style"
    if marker in html:
        return html, 0
    css = ('<style id="ts-svg-mapped-icon-style">'
        '.ts-svg-mapped-icon{display:inline-block;object-fit:contain}'
        '.top-ico .ts-svg-mapped-icon{width:17px;height:17px}'
        '.trust-icon .ts-svg-mapped-icon,.feature-icon .ts-svg-mapped-icon,.cat-icon .ts-svg-mapped-icon,.icon .ts-svg-mapped-icon,.ico .ts-svg-mapped-icon{width:52px;height:52px}'
        '.process-icon .ts-svg-mapped-icon,.step-icon .ts-svg-mapped-icon{width:44px;height:44px}'
        '.contact-item .ts-svg-mapped-icon{width:18px;height:18px}'
        '.svg-defs{display:none!important}'
        '</style>')
    if re.search(r"</head>", html, flags=re.I):
        return re.sub(r"</head>", css + "\n</head>", html, count=1, flags=re.I), 1
    return html, 0


def remove_legacy_sprite(html: str) -> tuple[str, int]:
    return re.subn(r"<svg\s+class=[\"']svg-defs[\"'][\s\S]*?</svg>\s*", "", html, flags=re.I)


def replace_legacy_use_icons(html: str, path: Path) -> tuple[str, int]:
    count = 0
    def repl(match: re.Match[str]) -> str:
        nonlocal count
        ref = LEGACY_USE_TO_REF.get(match.group(1))
        if not ref:
            return match.group(0)
        count += 1
        return icon_img(path, ref)
    pattern = r"<svg\b[^>]*>\s*<use\s+href=[\"']#([^\"']+)[\"']\s*></use>\s*</svg>"
    html = re.sub(pattern, repl, html, flags=re.I)
    return html, count


def replace_icon_inside_block(block: str, path: Path, ref: int) -> tuple[str, int]:
    img = icon_img(path, ref)
    icon_holder = re.compile(
        r"(<(?:span|div)[^>]*class=[\"'][^\"']*" + class_regex(ICON_CLASS_PARTS) + r"[^\"']*[\"'][^>]*>)"
        r"[\s\S]*?"
        r"(</(?:span|div)>)",
        re.I,
    )
    if icon_holder.search(block):
        return icon_holder.sub(lambda m: m.group(1) + img + m.group(2), block, count=1), 1

    old_svg_or_svg_img = re.compile(r"<svg\b[\s\S]*?</svg>|<img\b[^>]*src=[\"'][^\"']*\.svg[^\"']*[\"'][^>]*>", re.I)
    if old_svg_or_svg_img.search(block):
        return old_svg_or_svg_img.sub(img, block, count=1), 1

    return block, 0


def replace_by_phrase(html: str, path: Path) -> tuple[str, list[Replacement]]:
    changes: list[Replacement] = []
    for ref, phrase in PHRASE_TO_REF:
        q = esc(phrase)
        file_name = REF_TO_FILE.get(str(int(ref)), REF_TO_FILE["4"])
        phrase_count = 0
        block_re = re.compile(
            r"(<(?:article|div|li|a)[^>]*class=[\"'][^\"']*" + class_regex(BLOCK_CLASS_PARTS) + r"[^\"']*[\"'][^>]*>"
            r"[\s\S]{0,2200}?" + q + r"[\s\S]{0,2200}?"
            r"</(?:article|div|li|a)>)",
            re.I,
        )

        def block_repl(match: re.Match[str]) -> str:
            nonlocal phrase_count
            new_block, n = replace_icon_inside_block(match.group(1), path, int(ref))
            phrase_count += n
            return new_block

        html = block_re.sub(block_repl, html)

        icon_before_text = re.compile(
            r"(<(?:span|div)[^>]*class=[\"'][^\"']*" + class_regex(ICON_CLASS_PARTS) + r"[^\"']*[\"'][^>]*>)"
            r"[\s\S]*?"
            r"(</(?:span|div)>)(?=[\s\S]{0,420}?" + q + r")",
            re.I,
        )
        html, n = icon_before_text.subn(lambda m: m.group(1) + icon_img(path, int(ref)) + m.group(2), html)
        phrase_count += n

        if phrase_count:
            changes.append(Replacement(str(path.relative_to(REPO_ROOT)), phrase, int(ref), file_name, phrase_count))
    return html, changes


def process_file(path: Path, add_css: bool = True) -> tuple[str, list[Replacement], int]:
    original = path.read_text(encoding="utf-8")
    html = original
    total_non_phrase = 0
    if add_css:
        html, n = ensure_css(html)
        total_non_phrase += n
    html, n = remove_legacy_sprite(html)
    total_non_phrase += n
    html, n = replace_legacy_use_icons(html, path)
    total_non_phrase += n
    html, changes = replace_by_phrase(html, path)
    return html, changes, total_non_phrase


def run(roots: list[str], dry_run: bool, verbose: bool, report: str | None, add_css: bool) -> int:
    all_changes: list[Replacement] = []
    changed_files = 0
    for path in iter_html_files(roots):
        original = path.read_text(encoding="utf-8")
        new_html, changes, non_phrase = process_file(path, add_css=add_css)
        if new_html != original:
            changed_files += 1
            all_changes.extend(changes)
            if verbose:
                rel = path.relative_to(REPO_ROOT)
                print(f"{rel}: {len(changes)} phrase groups, {sum(c.count for c in changes)} icon replacements, {non_phrase} cleanup/style changes")
            if not dry_run:
                path.write_text(new_html, encoding="utf-8")

    if report:
        report_path = REPO_ROOT / report
        if not dry_run:
            report_path.parent.mkdir(parents=True, exist_ok=True)
            with report_path.open("w", newline="", encoding="utf-8") as fh:
                writer = csv.writer(fh)
                writer.writerow(["path", "phrase", "ref", "svg_file", "count"])
                for change in all_changes:
                    writer.writerow([change.path, change.phrase, change.ref, change.svg_file, change.count])
        if verbose:
            print(f"Report: {report_path}")

    action = "Would update" if dry_run else "Updated"
    print(f"{action} {changed_files} HTML files")
    print(f"Phrase icon replacements: {sum(c.count for c in all_changes)}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply exact spreadsheet SVG Ref# mappings to TShirtSwiss HTML pages.")
    parser.add_argument("--root", action="append", dest="roots", help="Root path/file to scan. Can be repeated. Defaults to pages.")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files.")
    parser.add_argument("--verbose", action="store_true", help="Print file-level details.")
    parser.add_argument("--report", default=None, help="Optional CSV report path, e.g. docs/svg-icon-mapping-report.csv")
    parser.add_argument("--no-css", action="store_true", help="Do not inject the standard mapped-icon CSS block.")
    args = parser.parse_args()
    return run(args.roots or DEFAULT_ROOTS, args.dry_run, args.verbose, args.report, not args.no_css)


if __name__ == "__main__":
    raise SystemExit(main())
