#!/usr/bin/env python3
"""Build TShirtSwiss Elementor 4.1.5 release archives from source files.

Outputs:
  dist/tshirtswiss-elementor-website-template.zip
  dist/tshirtswiss-elementor-saved-templates.zip
  dist/build-report.json

The website-template archive uses Elementor import/export format 2.0 and places
page-family templates under content/page so Elementor Free can import them.
The saved-template archive contains the reusable section/global JSON exports for
manual import into Elementor's Templates library. Elementor 4.1.5 gates the
full-kit saved-template runner behind Elementor Pro, so the split is deliberate.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DIST = ROOT / "dist"
ELEMENTOR_VERSION = "4.1.5"
FORMAT_VERSION = "2.0"


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object: {path.relative_to(ROOT)}")
    return value


def stable_id(relative_path: str, namespace: int) -> int:
    digest = hashlib.sha256(relative_path.encode("utf-8")).hexdigest()
    return namespace + (int(digest[:8], 16) % 800000)


def validate_template(path: Path, data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for key in ("version", "title", "type", "content"):
        if key not in data:
            errors.append(f"{path.relative_to(ROOT)}: missing '{key}'")
    if "content" in data and not isinstance(data["content"], list):
        errors.append(f"{path.relative_to(ROOT)}: 'content' must be an array")
    if data.get("type") not in {"page", "section", "header", "footer", "kit"}:
        errors.append(f"{path.relative_to(ROOT)}: unsupported type '{data.get('type')}'")
    return errors


def px(value: float | int) -> dict[str, Any]:
    return {"unit": "px", "size": value, "sizes": []}


def typography_value(token: dict[str, Any]) -> dict[str, Any]:
    return {
        "typography_typography": "custom",
        "typography_font_family": "Inter",
        "typography_font_size": px(token["fontSize"]),
        "typography_font_weight": str(token["fontWeight"]),
        "typography_line_height": {"unit": "em", "size": token["lineHeight"], "sizes": []},
        "typography_letter_spacing": px(token.get("letterSpacing", 0)),
        "typography_text_transform": token.get("textTransform", "none"),
    }


def build_site_settings() -> dict[str, Any]:
    colors = read_json(ROOT / "globals/colors.json")["tokens"]
    typography = read_json(ROOT / "globals/typography.json")["tokens"]
    containers = read_json(ROOT / "globals/containers.json")

    system_colors = [
        {"_id": "primary", "title": colors["primary"]["name"], "color": colors["primary"]["value"]},
        {"_id": "secondary", "title": colors["black"]["name"], "color": colors["black"]["value"]},
        {"_id": "text", "title": colors["ink"]["name"], "color": colors["ink"]["value"]},
        {"_id": "accent", "title": colors["primary"]["name"], "color": colors["primary"]["value"]},
    ]
    custom_colors = [
        {"_id": key, "title": item["name"], "color": item["value"]}
        for key, item in colors.items()
        if key not in {"primary", "black", "ink"}
    ]

    system_typography = [
        {"_id": "primary", "title": "Primary", **typography_value(typography["h1"])},
        {"_id": "secondary", "title": "Secondary", **typography_value(typography["h3"])},
        {"_id": "text", "title": "Text", **typography_value(typography["body"])},
        {"_id": "accent", "title": "Accent", **typography_value(typography["button"])},
    ]
    custom_typography = [
        {"_id": key, "title": key, **typography_value(value)}
        for key, value in typography.items()
    ]

    settings = {
        "system_colors": system_colors,
        "custom_colors": custom_colors,
        "system_typography": system_typography,
        "custom_typography": custom_typography,
        "default_generic_fonts": "Arial, Helvetica, sans-serif",
        "container_width": px(containers["tokens"]["wide"]["maxWidth"]),
        "viewport_md": containers["breakpoints"]["mobile"],
        "viewport_lg": containers["breakpoints"]["tablet"],
        "space_between_widgets": px(20),
        "page_title_selector": "h1.entry-title",
        "active_breakpoints": ["viewport_mobile", "viewport_tablet"],
    }

    return {
        "version": "0.4",
        "title": "TShirtSwiss Site Settings",
        "type": "kit",
        "content": [],
        "settings": settings,
        "page_settings": [],
        "theme": {
            "name": "Hello Elementor",
            "theme_uri": "https://elementor.com/hello-theme/",
            "version": "3.x",
            "slug": "hello-elementor",
        },
    }


def normalise_export(data: dict[str, Any]) -> dict[str, Any]:
    result = dict(data)
    result.setdefault("version", "0.4")
    result.setdefault("page_settings", [])
    return result


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def zip_directory(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(source).as_posix())


def build(dist: Path) -> dict[str, Any]:
    template_paths = sorted((ROOT / "templates").rglob("*.json"))
    validation_errors: list[str] = []
    parsed: dict[Path, dict[str, Any]] = {}

    for path in template_paths:
        data = read_json(path)
        parsed[path] = data
        validation_errors.extend(validate_template(path, data))

    if validation_errors:
        raise ValueError("\n".join(validation_errors))

    dist.mkdir(parents=True, exist_ok=True)
    for old in dist.glob("tshirtswiss-elementor-*.zip"):
        old.unlink()

    generated = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    website_zip = dist / "tshirtswiss-elementor-website-template.zip"
    templates_zip = dist / "tshirtswiss-elementor-saved-templates.zip"

    with tempfile.TemporaryDirectory(prefix="tss-elementor-") as temp_name:
        temp = Path(temp_name)
        website_root = temp / "website-template"
        saved_root = temp / "saved-templates"

        content_manifest: dict[str, dict[str, Any]] = {"page": {}}
        template_manifest: dict[str, dict[str, Any]] = {}

        for path, data in parsed.items():
            rel = path.relative_to(ROOT).as_posix()
            export_data = normalise_export(data)
            category = path.parent.name

            if category == "pages":
                old_id = stable_id(rel, 100000)
                content_manifest["page"][str(old_id)] = {
                    "title": data["title"],
                    "excerpt": "TShirtSwiss Elementor page-family template",
                    "doc_type": "wp-page",
                    "thumbnail": False,
                    "url": "",
                    "terms": [],
                }
                write_json(website_root / "content/page" / f"{old_id}.json", export_data)
            else:
                old_id = stable_id(rel, 1000000)
                doc_type = data.get("type", "section")
                template_manifest[str(old_id)] = {
                    "title": data["title"],
                    "doc_type": doc_type,
                    "thumbnail": False,
                }
                write_json(saved_root / category / path.name, export_data)

        site_settings = build_site_settings()
        write_json(website_root / "site-settings.json", site_settings)

        manifest = {
            "name": "tshirtswiss-elementor-website-template",
            "title": "TShirtSwiss Elementor Website Template",
            "description": "TShirtSwiss page-family templates and global design settings for Elementor Free 4.1.5.",
            "author": "TShirtSwiss",
            "version": FORMAT_VERSION,
            "elementor_version": ELEMENTOR_VERSION,
            "created": generated.replace("T", " ").replace("+00:00", ""),
            "thumbnail": False,
            "site": "https://tshirtswiss.ch",
            "content": content_manifest,
            "site-settings": [
                "settings-global-colors",
                "settings-global-typography",
                "settings-layout",
                "settings-lightbox",
            ],
            "theme": site_settings["theme"],
        }
        write_json(website_root / "manifest.json", manifest)

        saved_index = {
            "title": "TShirtSwiss Saved Templates",
            "elementor_version": ELEMENTOR_VERSION,
            "generated": generated,
            "templates": template_manifest,
            "instructions": "Import JSON files through Templates > Saved Templates > Import Templates. Elementor 4.1.5 Free does not run the full-kit saved-template importer.",
        }
        write_json(saved_root / "index.json", saved_index)

        zip_directory(website_root, website_zip)
        zip_directory(saved_root, templates_zip)

    report = {
        "status": "built",
        "generated": generated,
        "elementorVersion": ELEMENTOR_VERSION,
        "formatVersion": FORMAT_VERSION,
        "sourceTemplates": len(parsed),
        "pageTemplates": len([p for p in parsed if p.parent.name == "pages"]),
        "savedTemplates": len([p for p in parsed if p.parent.name != "pages"]),
        "artifacts": [website_zip.name, templates_zip.name],
        "notes": [
            "Website archive imports pages and site settings in Elementor Free.",
            "Reusable components and global parts are provided as individual JSON templates because Elementor 4.1.5 gates kit template import behind Pro.",
            "A live staging import remains the final compatibility test.",
        ],
    }
    write_json(dist / "build-report.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, default=DEFAULT_DIST, help="Output directory")
    parser.add_argument("--clean", action="store_true", help="Remove the output directory before building")
    args = parser.parse_args()

    dist = args.dist.resolve()
    if args.clean and dist.exists():
        shutil.rmtree(dist)

    try:
        report = build(dist)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
