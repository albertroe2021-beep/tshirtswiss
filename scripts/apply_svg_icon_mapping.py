#!/usr/bin/env python3
"""
Apply the TShirtSwiss spreadsheet-driven SVG icon mapping across the static site.

This script scans HTML files, finds icon/text cards containing mapped website phrases,
and replaces the existing icon markup with the SVG assigned to that phrase Ref#.

Usage from the repository root:

    python scripts/apply_svg_icon_mapping.py --dry-run
    python scripts/apply_svg_icon_mapping.py

Optional:

    python scripts/apply_svg_icon_mapping.py --root pages/home
    python scripts/apply_svg_icon_mapping.py --verbose

Notes:
- The phrase-to-Ref# mapping is based on `SVG number to phrase.xlsx`.
- The Ref#-to-SVG mapping is based on `docs/svg-icon-mapping-draft.md`.
- Icons are emitted as inline SVG using the standard site class `ts-inline-icon`.
- The standard visual style is controlled in CSS: red stroke, no fill, rounded caps/joins.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCAN_ROOTS = ["pages"]
SKIP_DIRS = {".git", "node_modules", "dist", "build", ".cache", "__pycache__"}

SVG_STYLE = 'class="ts-inline-icon" aria-hidden="true" focusable="false"'


# Canonical lightweight outline icons. These are intentionally normalised
# to a consistent 64x64-style viewport, currentColor stroke, no fill.
ICON_LIBRARY: dict[str, str] = {
    "swiss": '<svg {attrs} viewBox="14 14 36 36"><path d="M32 18l12 5v9c0 8-5 13-12 16-7-3-12-8-12-16v-9l12-5z"/><path d="M32 25v16M24 33h16"/></svg>',
    "factory": '<svg {attrs} viewBox="14 14 36 36"><path d="M20 43h27"/><path d="M22 43V30l8 5v-5l8 5v-5l8 5v8"/><path d="M42 34V20h5v23"/><path d="M25 39h4M34 39h4"/></svg>',
    "quality": '<svg {attrs} viewBox="14 14 36 36"><rect x="22" y="21" width="20" height="25" rx="2"/><path d="M28 20h8l2 4H26l2-4z"/><path d="M27 34l4 4 8-9"/></svg>',
    "award": '<svg {attrs} viewBox="14 14 36 36"><circle cx="32" cy="27" r="8"/><path d="M28 27l3 3 6-7"/><path d="M27 34l-2 12 7-4 7 4-2-12"/></svg>',
    "shipping": '<svg {attrs} viewBox="14 14 36 36"><path d="M18 38l28-16-9 24-6-9-9-2z"/><path d="M31 37l15-15"/></svg>',
    "stopwatch": '<svg {attrs} viewBox="14 14 36 36"><circle cx="32" cy="34" r="12"/><path d="M28 18h8M32 22v-4M32 34l6-6"/></svg>',
    "handshake": '<svg {attrs} viewBox="14 14 36 36"><path d="M20 34l8-8 6 6"/><path d="M44 34l-8-8-6 6"/><path d="M26 40l4 4c2 2 5 2 7 0l5-5"/><path d="M18 32l6 12M46 32l-6 12"/></svg>',
    "support": '<svg {attrs} viewBox="14 14 36 36"><circle cx="32" cy="28" r="7"/><path d="M21 36c2-4 6-6 11-6s9 2 11 6"/><path d="M20 29c0-7 5-12 12-12s12 5 12 12M44 32v3c0 3-2 5-5 5h-3"/></svg>',
    "chat": '<svg {attrs} viewBox="14 14 36 36"><path d="M20 26c0-5 5-9 12-9s12 4 12 9-5 9-12 9h-3l-6 5 1-7c-3-2-4-4-4-7z"/><path d="M28 41h10l5 4-1-5c3-1 5-4 5-7"/></svg>',
    "monitor": '<svg {attrs} viewBox="14 14 36 36"><rect x="20" y="21" width="24" height="16" rx="2"/><path d="M28 45h8M32 37v8"/></svg>',
    "review": '<svg {attrs} viewBox="14 14 36 36"><rect x="22" y="19" width="20" height="27" rx="2"/><path d="M27 31l4 4 8-9M27 40h10"/></svg>',
    "design": '<svg {attrs} viewBox="14 14 36 36"><path d="M22 42l4-12 13-13 5 5-13 13-9 7z"/><path d="M36 20l5 5M26 30l5 5"/></svg>',
    "sketch": '<svg {attrs} viewBox="14 14 36 36"><path d="M21 43h22"/><path d="M25 38l15-15 4 4-15 15-6 2z"/><path d="M24 25h10"/></svg>',
    "fabric": '<svg {attrs} viewBox="14 14 36 36"><path d="M20 26h18a7 7 0 010 14H20z"/><circle cx="38" cy="33" r="3.5"/><path d="M20 26v14M23 44l20-20M35 45l9-9"/></svg>',
    "sewing": '<svg {attrs} viewBox="14 14 36 36"><path d="M21 42h26"/><path d="M24 38h15c5 0 8-3 8-8v-3H30"/><path d="M30 27v-8h10v8M25 38v-8"/><circle cx="26" cy="44" r="2"/></svg>',
    "scissors": '<svg {attrs} viewBox="14 14 36 36"><circle cx="24" cy="40" r="4"/><circle cx="24" cy="24" r="4"/><path d="M28 37l16-15M28 27l16 15"/></svg>',
    "needle": '<svg {attrs} viewBox="14 14 36 36"><path d="M43 21L21 43"/><path d="M38 18c3 0 6 3 6 6"/><path d="M21 43c6-1 10 0 13 4"/></svg>',
    "print": '<svg {attrs} viewBox="14 14 36 36"><rect x="22" y="18" width="20" height="9"/><rect x="20" y="31" width="24" height="13" rx="2"/><path d="M25 36h14M25 40h10"/></svg>',
    "box": '<svg {attrs} viewBox="14 14 36 36"><path d="M21 27l11-6 11 6-11 6-11-6z"/><path d="M21 27v13l11 7 11-7V27M32 33v14"/></svg>',
    "tshirt": '<svg {attrs} viewBox="14 14 36 36"><path d="M25 24l7-4 7 4 6 2-3 8-4-2v15H26V32l-4 2-3-8 6-2z"/></svg>',
    "polo": '<svg {attrs} viewBox="14 14 36 36"><path d="M25 24l7-4 7 4 6 2-3 8-4-2v15H26V32l-4 2-3-8 6-2z"/><path d="M29 22l3 5 3-5M32 27v7"/></svg>',
    "hoodie": '<svg {attrs} viewBox="14 14 36 36"><path d="M23 27l9-6 9 6 4 5-5 4-2-3v14H26V33l-2 3-5-4 4-5z"/><path d="M27 27c1-4 9-4 10 0"/></svg>',
    "worker": '<svg {attrs} viewBox="14 14 36 36"><circle cx="32" cy="27" r="7"/><path d="M23 27h18M25 25c1-5 4-8 7-8s6 3 7 8M21 45c2-6 7-9 11-9s9 3 11 9"/></svg>',
    "shirt": '<svg {attrs} viewBox="14 14 36 36"><path d="M24 24l8-4 8 4 4 5-5 4v14H25V33l-5-4 4-5z"/><path d="M29 22l3 6 3-6M32 28v19"/></svg>',
    "team": '<svg {attrs} viewBox="14 14 36 36"><circle cx="24" cy="27" r="5"/><circle cx="40" cy="27" r="5"/><path d="M17 45c1-6 4-9 7-9s6 3 7 9M33 45c1-6 4-9 7-9s6 3 7 9"/></svg>',
    "swim": '<svg {attrs} viewBox="14 14 36 36"><path d="M21 37c4-4 8-4 12 0s8 4 12 0"/><path d="M21 45c4-4 8-4 12 0s8 4 12 0"/><circle cx="31" cy="23" r="4"/><path d="M35 27l8 5M28 28l-7 4"/></svg>',
    "shorts": '<svg {attrs} viewBox="14 14 36 36"><path d="M23 21h18l3 25h-9l-3-14-3 14h-9l3-25z"/><path d="M24 27h16"/></svg>',
    "doctor": '<svg {attrs} viewBox="14 14 36 36"><circle cx="32" cy="24" r="6"/><path d="M22 46c1-9 6-14 10-14s9 5 10 14"/><path d="M32 35v9M28 40h8"/></svg>',
    "cap": '<svg {attrs} viewBox="14 14 36 36"><path d="M20 35c2-8 8-12 15-10 5 1 8 5 9 10"/><path d="M20 35h25c4 0 6 2 5 5H18c-4 0-5-2-2-4 1-1 2-1 4-1z"/></svg>',
    "jacket": '<svg {attrs} viewBox="14 14 36 36"><path d="M25 22l7-3 7 3 5 5-4 5v15H24V32l-4-5 5-5z"/><path d="M32 22v25M27 33h-3M37 33h3"/></svg>',
    "bag": '<svg {attrs} viewBox="14 14 36 36"><path d="M22 27h20l2 20H20l2-20z"/><path d="M27 27c0-6 10-6 10 0"/></svg>',
    "tag": '<svg {attrs} viewBox="14 14 36 36"><path d="M21 24h16l8 8-16 16-8-8V24z"/><circle cx="29" cy="31" r="2"/></svg>',
    "barcode": '<svg {attrs} viewBox="14 14 36 36"><rect x="20" y="22" width="24" height="20" rx="2"/><path d="M25 27v10M29 27v10M34 27v10M39 27v10"/></svg>',
    "bamboo": '<svg {attrs} viewBox="14 14 36 36"><path d="M27 46l8-28M22 35c7 0 11-3 13-8M36 38c-6-1-9-4-10-9"/><path d="M36 46l7-24"/></svg>',
    "dry": '<svg {attrs} viewBox="14 14 36 36"><path d="M32 18c8 10 11 15 11 22 0 6-5 10-11 10s-11-4-11-10c0-7 3-12 11-22z"/><path d="M24 40h16"/></svg>',
    "germs": '<svg {attrs} viewBox="14 14 36 36"><circle cx="32" cy="32" r="8"/><path d="M32 18v6M32 40v6M18 32h6M40 32h6M22 22l4 4M38 38l4 4M42 22l-4 4M26 38l-4 4"/></svg>',
    "sun": '<svg {attrs} viewBox="14 14 36 36"><circle cx="32" cy="32" r="7"/><path d="M32 18v5M32 41v5M18 32h5M41 32h5M22 22l4 4M38 38l4 4M42 22l-4 4M26 38l-4 4"/></svg>',
    "hotel": '<svg {attrs} viewBox="14 14 36 36"><path d="M20 45h24M23 45V22h18v23"/><path d="M27 27h3M34 27h3M27 33h3M34 33h3"/><path d="M20 22h24"/></svg>',
    "facebook": '<svg {attrs} viewBox="14 14 36 36"><circle cx="32" cy="32" r="14"/><path d="M35 24h-3c-2 0-3 1-3 3v3h6l-1 5h-5v11"/></svg>',
    "concert": '<svg {attrs} viewBox="14 14 36 36"><path d="M20 44h24"/><path d="M27 40l5-18 5 18"/><path d="M24 28l8-6 8 6M22 36h20"/></svg>',
    "recycle": '<svg {attrs} viewBox="14 14 36 36"><path d="M29 20l5 0 3 5"/><path d="M25 37l-3 5 6 0"/><path d="M41 34l3-5-3-5"/><path d="M34 20c-5 1-9 5-10 10M22 42c4 3 10 4 15 1M44 29c-1 5-4 10-9 12"/></svg>',
    "water": '<svg {attrs} viewBox="14 14 36 36"><path d="M32 18c8 9 11 14 11 21 0 6-5 10-11 10s-11-4-11-10c0-7 3-12 11-21z"/></svg>',
    "download": '<svg {attrs} viewBox="14 14 36 36"><path d="M32 18v20M24 30l8 8 8-8"/><path d="M22 45h20"/></svg>',
    "book": '<svg {attrs} viewBox="14 14 36 36"><path d="M20 22h10c2 0 2 2 2 2v24s0-2-3-2h-9z"/><path d="M44 22H34c-2 0-2 2-2 2v24s0-2 3-2h9z"/></svg>',
    "search": '<svg {attrs} viewBox="14 14 36 36"><circle cx="29" cy="29" r="9"/><path d="M36 36l9 9"/></svg>',
    "whatsapp": '<svg {attrs} viewBox="14 14 36 36"><path d="M20 45l3-8c-2-3-3-6-3-9 0-8 6-14 14-14s14 6 14 14-6 14-14 14c-3 0-6-1-8-2l-6 5z"/><path d="M28 24c2 7 5 10 12 12"/></svg>',
    "email": '<svg {attrs} viewBox="14 14 36 36"><rect x="20" y="24" width="24" height="18" rx="2"/><path d="M20 27l12 9 12-9"/></svg>',
}

REF_TO_ICON = {
    1: "swiss", 2: "factory", 3: "award", 4: "quality", 5: "quality", 6: "shipping", 7: "stopwatch", 8: "handshake",
    9: "support", 10: "chat", 11: "monitor", 12: "review", 13: "design", 14: "monitor", 15: "sketch", 16: "review",
    17: "quality", 18: "fabric", 19: "design", 20: "factory", 21: "sewing", 22: "scissors", 23: "needle", 24: "print",
    25: "box", 26: "box", 27: "box", 28: "shipping", 29: "tshirt", 30: "polo", 31: "hoodie", 32: "worker",
    33: "shirt", 34: "team", 35: "swim", 36: "shorts", 37: "shorts", 38: "doctor", 39: "doctor", 40: "cap",
    41: "jacket", 42: "bag", 43: "team", 44: "barcode", 45: "barcode", 46: "tag", 47: "barcode", 48: "barcode",
    49: "box", 50: "bag", 51: "barcode", 52: "print", 53: "print", 54: "print", 55: "print", 56: "needle",
    57: "fabric", 58: "fabric", 59: "fabric", 60: "bamboo", 61: "fabric", 62: "dry", 63: "fabric", 64: "germs",
    65: "sun", 66: "worker", 67: "doctor", 68: "hotel", 69: "team", 70: "shorts", 71: "shirt", 72: "bag",
    73: "facebook", 74: "concert", 75: "bamboo", 76: "recycle", 77: "recycle", 78: "recycle", 79: "recycle", 80: "recycle",
    81: "water", 82: "recycle", 83: "monitor", 84: "monitor", 85: "download", 86: "book", 87: "book", 88: "book",
    89: "search", 90: "support", 91: "support", 92: "whatsapp", 93: "email", 94: "swiss", 95: "email", 96: "support",
}

# Phrase list from SVG number to phrase.xlsx. Longer phrases should appear first
# to avoid a shorter phrase matching inside a more specific one.
PHRASE_TO_REF: list[tuple[str, int]] = [
    ("Swiss Quality Standards", 1), ("Swiss-Managed Communication", 1), ("Swiss Managed", 1),
    ("Factory Direct Pricing", 2), ("Factory in Thailand", 2), ("Thailand Manufacturing Base", 2), ("PRODUCTION & DELIVERY", 2),
    ("Reliable Production", 2), ("Responsible Production", 2), ("Production Ready", 2), ("Bulk Production", 2), ("Factory Direct", 2),
    ("Bulk Orders", 2), ("Production", 2),
    ("Premium Quality", 3), ("Quality-First Approach", 3), ("Easy Care", 3), ("Verification", 3),
    ("Strict Quality Control", 4), ("Quality Control", 4), ("Sample Check", 4), ("Quality Check", 5), ("Quality", 17),
    ("Worldwide Shipping", 6), ("Packing & Shipping", 6), ("Shipment Handover", 6), ("Shipment Ready", 6), ("Easy Distribution", 6),
    ("Delivery Ready", 6), ("Shipping", 6), ("Deadline Focused", 7), ("Fast Response", 7),
    ("Long Term Partner", 8), ("Ethical Labour Practices", 8), ("No Obligation", 8), ("Brand-Safe Execution", 8),
    ("Request a Quote", 9), ("Transfer Plannning", 10), ("Sample Advice", 10), ("Consultation", 10), ("Feedback", 10),
    ("Branding Review", 11), ("Product Planning", 11), ("Professional Branding", 11), ("Brand Control", 11), ("Artwork Setup", 11),
    ("Campaigns", 11), ("Digitising", 11), ("Branding", 11), ("Finishing", 12), ("Concept Review", 12), ("Sample or Test", 12),
    ("Fit & Construction", 13), ("Fit & Sizes", 13), ("Sizes", 13), ("How should I brand apparel?", 14), ("PRIVATE LABEL", 14),
    ("Ecommerce Brands", 14), ("Brands", 14), ("Material Direction", 15), ("Panel Layout", 15), ("Spec Review", 15),
    ("Private Label", 15), ("Decoration", 15), ("Full Artwork", 15), ("Strong Artwork", 15), ("Artwork", 15),
    ("Review & Revision", 16), ("Sample & Approval", 16), ("Sample Review", 16), ("Requirement Review", 16), ("Branding Check", 16),
    ("Construction Check", 16), ("Artwork Review", 16), ("Sample/Test", 16), ("Sampling", 16),
    ("Final QC", 17), ("Brand Review", 17), ("Integration", 17), ("Material Planning", 18), ("Material Options", 18),
    ("Material Check", 18), ("Materials", 18), ("Fabric", 18), ("Fit & Closure", 19), ("Fit & Length", 19),
    ("Spec Planning", 19), ("SAMPLING & CUSTOMISATION", 19), ("Sample Build", 21), ("PRINTING & BRANDING", 21),
    ("Do I need a sample?", 22), ("Thread Planning", 23), ("Print Planning", 24), ("Colors", 24),
    ("Packing & Delivery", 27), ("Packing Setup", 27), ("Packing Check", 27), ("How do I prepare for shipping?", 27), ("Packing", 27),
    ("View All Products", 29), ("Custom Products", 29), ("Retail Ready", 29), ("Garment Check", 29), ("Promotional", 29), ("Garments", 29),
    ("Retail Lines", 30), ("Retail Feel", 30), ("Corporate Polos", 30), ("Private Label Support", 31), ("Fitness", 31),
    ("Workwear & Uniforms", 32), ("Safety First", 32), ("Training Durability", 32), ("Workwear", 32),
    ("Brand & Uniform Ready", 33), ("Professional Look", 33), ("Corporate Apparel", 33), ("Corporate Merch", 33),
    ("Team Identity", 34), ("Team Clarity", 34), ("Active Comfort", 34), ("Sportswear & Activewear", 34), ("Sportswear Options", 34),
    ("Sportswear", 34), ("Teamwear", 34), ("Rashguards", 35), ("Activewear Labels", 35), ("Muay Thai", 36),
    ("MMA Shorts", 36), ("Gym Apparel", 36), ("Uniforms", 38), ("Comfort First", 40), ("Private Label Brands", 40), ("Caps", 40),
    ("Streetwear Drops", 41), ("Fashion Brands", 41), ("Jackets", 41), ("Retail Collections", 42), ("Label Support", 44),
    ("Label Planning", 47), ("Drop Planning", 49), ("Packaging", 49), ("Handles", 50), ("Carton Labelling", 51),
    ("All Weather", 62), ("All Day Comfort", 67), ("Guest Ready", 68), ("Hospitality", 68), ("How do I develop a garment?", 71),
    ("Creator Merch", 73), ("Event Merchandise", 74), ("Audience Ready", 74), ("Event Ready", 74), ("Merch Drops", 74),
    ("Event Merch", 74), ("Audience", 74), ("Sustainable Options", 75), ("Reduced Waste Planning", 76), ("Waste-Aware Planning", 76),
    ("Information Planning", 86), ("Documentation", 86), ("Packing Plan", 88), ("Packaging Plan", 89),
    ("Reliable Reorders", 90), ("Consultation & Specs", 90), ("Delivery Review", 90), ("Brief Review", 90), ("Free Consultation", 90),
    ("ORDERING & PLANNING", 90), ("Brand Consultation", 96), ("WhatsApp", 92), ("Email Us", 95), ("Email", 95),
]
PHRASE_TO_REF.sort(key=lambda item: len(item[0]), reverse=True)

LEGACY_SYMBOLS = {
    "✚": 1, "▣": 2, "▤": 2, "▱": 2, "▻": 6, "◇": 3, "♡": 3, "✓": 4, "◎": 4,
    "◉": 29, "♙": 29, "♧": 29, "♢": 46, "▧": 86, "✉": 95, "⌕": 89, "☷": 10, "⚙": 2, "⌂": 29,
}


@dataclass
class Change:
    path: Path
    count: int


def icon_for_ref(ref: int) -> str:
    name = REF_TO_ICON.get(ref, "quality")
    return ICON_LIBRARY[name].format(attrs=SVG_STYLE)


def iter_html_files(root_paths: Iterable[str]) -> Iterable[Path]:
    for root in root_paths:
        root_path = (REPO_ROOT / root).resolve()
        if not root_path.exists():
            continue
        for path in root_path.rglob("*.html"):
            if any(part in SKIP_DIRS for part in path.parts):
                continue
            yield path


def replace_icon_inside_block(block: str, ref: int) -> tuple[str, int]:
    icon = icon_for_ref(ref)
    replacements = 0

    # Replace common icon containers first.
    icon_container_re = re.compile(
        r'(<(?:span|div)[^>]*class=["\'][^"\']*(?:top-ico|trust-icon|cat-icon|icon|ico|mail-icon|section-icon|feature-icon|process-icon|step-icon)[^"\']*["\'][^>]*>)'
        r'[\s\S]*?'
        r'(</(?:span|div)>)',
        re.IGNORECASE,
    )
    if icon_container_re.search(block):
        block, n = icon_container_re.subn(r"\1" + icon + r"\2", block, count=1)
        replacements += n
        return block, replacements

    # Then replace bare inline SVGs.
    svg_re = re.compile(r"<svg\b[\s\S]*?</svg>", re.IGNORECASE)
    if svg_re.search(block):
        block, n = svg_re.subn(icon, block, count=1)
        replacements += n
        return block, replacements

    return block, replacements


def replace_cards_by_phrase(html: str) -> tuple[str, int]:
    total = 0
    updated = html

    # Replace icons inside common card/item blocks containing the phrase.
    block_re_template = (
        r'(<(?:article|div|li)[^>]*class=["\'][^"\']*'
        r'(?:card|point|mini|item|step|tag|tile|feature|process|trust|value|resource)'
        r'[^"\']*["\'][^>]*>[\s\S]{0,1200}?%s[\s\S]{0,1200}?</(?:article|div|li)>)'
    )

    for phrase, ref in PHRASE_TO_REF:
        phrase_re = re.escape(phrase)
        block_re = re.compile(block_re_template % phrase_re, re.IGNORECASE)

        def block_repl(match: re.Match[str]) -> str:
            nonlocal total
            block = match.group(1)
            new_block, n = replace_icon_inside_block(block, ref)
            total += n
            return new_block

        updated = block_re.sub(block_repl, updated)

        # Also handle cases where the icon container immediately precedes the phrase.
        preceding_re = re.compile(
            r'(<(?:span|div)[^>]*class=["\'][^"\']*(?:icon|ico|trust-icon|feature-icon|cat-icon|process-icon|step-icon)[^"\']*["\'][^>]*>)'
            r'[\s\S]*?'
            r'(</(?:span|div)>)(?=[\s\S]{0,260}?' + phrase_re + r')',
            re.IGNORECASE,
        )
        updated, n = preceding_re.subn(r"\1" + icon_for_ref(ref) + r"\2", updated)
        total += n

    return updated, total


def replace_legacy_symbols(html: str) -> tuple[str, int]:
    total = 0
    updated = html
    for symbol, ref in LEGACY_SYMBOLS.items():
        symbol_re = re.compile(
            r'(<(?:span|div)[^>]*class=["\'][^"\']*(?:top-ico|trust-icon|cat-icon|icon|ico|mail-icon|section-icon|feature-icon|process-icon)[^"\']*["\'][^>]*>)'
            + re.escape(symbol)
            + r'(</(?:span|div)>)'
        )
        updated, n = symbol_re.subn(r"\1" + icon_for_ref(ref) + r"\2", updated)
        total += n
    return updated, total


def replace_use_references(html: str) -> tuple[str, int]:
    use_map = {
        "icon-swiss-cross": 1,
        "icon-factory": 2,
        "icon-award-check": 3,
        "icon-box-plane": 6,
        "icon-tshirt": 29,
        "icon-clipboard-check": 4,
        "icon-package": 27,
        "icon-mail": 95,
    }
    total = 0
    updated = html
    for icon_id, ref in use_map.items():
        pattern = re.compile(
            r'<svg\b[^>]*>\s*<use\s+href=["\']#' + re.escape(icon_id) + r'["\']\s*></use>\s*</svg>',
            re.IGNORECASE,
        )
        updated, n = pattern.subn(icon_for_ref(ref), updated)
        total += n
    return updated, total


def ensure_icon_css(html: str) -> tuple[str, int]:
    css = (
        ".ts-inline-icon{stroke:currentColor;fill:none;stroke-width:2.6;"
        "stroke-linecap:round;stroke-linejoin:round;display:inline-block;}"
        ".icon .ts-inline-icon,.ico .ts-inline-icon,.trust-icon .ts-inline-icon,"
        ".feature-icon .ts-inline-icon,.cat-icon .ts-inline-icon,.process-icon .ts-inline-icon{"
        "width:52px;height:52px;}"
    )
    marker = "data-ts-icon-standard"
    if marker in html:
        return html, 0
    if "</head>" not in html.lower():
        return html, 0
    style_tag = f'<style {marker}> {css} </style>'
    updated = re.sub(r"</head>", style_tag + "\n</head>", html, flags=re.IGNORECASE, count=1)
    return updated, 1


def process_html(html: str, add_css: bool = False) -> tuple[str, int]:
    total = 0
    for fn in (replace_use_references, replace_legacy_symbols, replace_cards_by_phrase):
        html, n = fn(html)
        total += n
    if add_css:
        html, n = ensure_icon_css(html)
        total += n
    return html, total


def run(root_paths: list[str], dry_run: bool, verbose: bool, add_css: bool) -> list[Change]:
    changes: list[Change] = []
    for path in iter_html_files(root_paths):
        original = path.read_text(encoding="utf-8")
        updated, count = process_html(original, add_css=add_css)
        if count and updated != original:
            rel = path.relative_to(REPO_ROOT)
            changes.append(Change(rel, count))
            if verbose:
                print(f"{rel}: {count} replacements")
            if not dry_run:
                path.write_text(updated, encoding="utf-8")
    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description="Apply TShirtSwiss SVG icon mapping across HTML pages.")
    parser.add_argument("--root", action="append", dest="roots", help="Root path to scan. Can be passed multiple times. Defaults to pages.")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files.")
    parser.add_argument("--verbose", action="store_true", help="Print each changed file.")
    parser.add_argument("--add-css", action="store_true", help="Inject standard icon CSS into each changed HTML file.")
    args = parser.parse_args()

    roots = args.roots or DEFAULT_SCAN_ROOTS
    changes = run(roots, dry_run=args.dry_run, verbose=args.verbose, add_css=args.add_css)

    action = "Would update" if args.dry_run else "Updated"
    print(f"{action} {len(changes)} HTML files.")
    print(f"Total icon replacements: {sum(c.count for c in changes)}")
    if not args.verbose and changes:
        print("Run with --verbose to see file-level details.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
