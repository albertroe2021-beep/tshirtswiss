#!/usr/bin/env python3
"""Audit HTML image usage across the TShirtSwiss repository.

The audit reports:
- remote image URLs in img/src, source/srcset and CSS url(...)
- missing local image files
- empty or missing alt text on informative <img> elements
- duplicate photographic sources reused across multiple pages

Usage:
    python scripts/audit_image_assets.py
    python scripts/audit_image_assets.py --root . --output image-audit-report.md

The script uses only the Python standard library so it can run locally and in
GitHub Actions without installing dependencies.
"""

from __future__ import annotations

import argparse
import html.parser
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse

REMOTE_SCHEMES = ("http://", "https://", "//")
IMAGE_EXTENSIONS = {
    ".avif",
    ".gif",
    ".jpeg",
    ".jpg",
    ".png",
    ".svg",
    ".webp",
}
SKIP_DIRS = {".git", ".github", "node_modules", "vendor"}
CSS_URL_RE = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.IGNORECASE)
SRCSET_SPLIT_RE = re.compile(r"\s*,\s*")


@dataclass(frozen=True)
class ImageReference:
    page: Path
    source: str
    kind: str
    line: int | None = None
    alt: str | None = None


@dataclass
class AuditResult:
    remote: list[ImageReference] = field(default_factory=list)
    missing_local: list[ImageReference] = field(default_factory=list)
    alt_issues: list[ImageReference] = field(default_factory=list)
    all_refs: list[ImageReference] = field(default_factory=list)


class HTMLImageParser(html.parser.HTMLParser):
    def __init__(self, page: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.page = page
        self.references: list[ImageReference] = []
        self.alt_issues: list[ImageReference] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {key.lower(): value for key, value in attrs}
        line, _ = self.getpos()
        tag = tag.lower()

        if tag == "img":
            src = (attr_map.get("src") or "").strip()
            alt = attr_map.get("alt")
            role = (attr_map.get("role") or "").strip().lower()
            aria_hidden = (attr_map.get("aria-hidden") or "").strip().lower()

            if src:
                self.references.append(
                    ImageReference(self.page, src, "img-src", line=line, alt=alt)
                )

            if alt is None:
                self.alt_issues.append(
                    ImageReference(self.page, src or "(no src)", "missing-alt", line=line)
                )
            elif not alt.strip() and role != "presentation" and aria_hidden != "true":
                # Empty alt is valid for decorative images. Flag for manual review rather
                # than treating it as an unconditional error.
                self.alt_issues.append(
                    ImageReference(self.page, src or "(no src)", "empty-alt-review", line=line, alt=alt)
                )

            srcset = (attr_map.get("srcset") or "").strip()
            self._append_srcset(srcset, line, "img-srcset")

        elif tag == "source":
            srcset = (attr_map.get("srcset") or "").strip()
            self._append_srcset(srcset, line, "source-srcset")

        style = attr_map.get("style") or ""
        for source in extract_css_urls(style):
            self.references.append(
                ImageReference(self.page, source, "inline-style", line=line)
            )

    def handle_data(self, data: str) -> None:
        # Style blocks are collected by HTMLParser as raw data, but identifying
        # whether data belongs to <style> requires state. This parser instead
        # relies on a separate whole-document CSS scan performed after parsing.
        return

    def _append_srcset(self, srcset: str, line: int, kind: str) -> None:
        if not srcset:
            return
        for candidate in SRCSET_SPLIT_RE.split(srcset):
            source = candidate.strip().split()[0] if candidate.strip() else ""
            if source:
                self.references.append(
                    ImageReference(self.page, source, kind, line=line)
                )


def extract_css_urls(text: str) -> Iterable[str]:
    for match in CSS_URL_RE.finditer(text):
        source = match.group(2).strip()
        if source and not source.startswith("data:"):
            yield source


def is_remote(source: str) -> bool:
    return source.lower().startswith(REMOTE_SCHEMES)


def is_image_like(source: str) -> bool:
    clean = source.split("?", 1)[0].split("#", 1)[0]
    suffix = Path(unquote(urlparse(clean).path)).suffix.lower()
    return suffix in IMAGE_EXTENSIONS


def local_target(page: Path, root: Path, source: str) -> Path | None:
    clean = source.split("?", 1)[0].split("#", 1)[0]
    clean = unquote(clean.strip())
    if not clean or clean.startswith(("data:", "mailto:", "tel:", "#")):
        return None
    if clean.startswith("/"):
        return root / clean.lstrip("/")
    return (page.parent / clean).resolve()


def iter_html_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.html"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def audit(root: Path) -> AuditResult:
    result = AuditResult()
    root = root.resolve()

    for page in iter_html_files(root):
        text = page.read_text(encoding="utf-8", errors="replace")
        parser = HTMLImageParser(page)
        parser.feed(text)

        references = list(parser.references)
        for source in extract_css_urls(text):
            references.append(ImageReference(page, source, "css-url"))

        result.alt_issues.extend(parser.alt_issues)

        seen: set[tuple[str, str, int | None]] = set()
        for ref in references:
            key = (ref.source, ref.kind, ref.line)
            if key in seen:
                continue
            seen.add(key)
            result.all_refs.append(ref)

            if is_remote(ref.source):
                if is_image_like(ref.source):
                    result.remote.append(ref)
                continue

            target = local_target(page, root, ref.source)
            if target is not None and is_image_like(ref.source) and not target.exists():
                result.missing_local.append(ref)

    return result


def relative(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve())).replace(os.sep, "/")
    except ValueError:
        return str(path).replace(os.sep, "/")


def markdown_report(result: AuditResult, root: Path) -> str:
    lines: list[str] = [
        "# TShirtSwiss Image Audit Report",
        "",
        "Generated by `scripts/audit_image_assets.py`.",
        "",
        "## Summary",
        "",
        f"- Total image references: **{len(result.all_refs)}**",
        f"- Remote photographic/image references: **{len(result.remote)}**",
        f"- Missing local image files: **{len(result.missing_local)}**",
        f"- Alt-text review items: **{len(result.alt_issues)}**",
        "",
    ]

    def table(title: str, rows: list[ImageReference]) -> None:
        lines.extend([f"## {title}", ""])
        if not rows:
            lines.extend(["None.", ""])
            return
        lines.extend([
            "| Page | Line | Kind | Source |",
            "|---|---:|---|---|",
        ])
        for ref in sorted(rows, key=lambda item: (str(item.page), item.line or 0, item.source)):
            source = ref.source.replace("|", "%7C")
            lines.append(
                f"| `{relative(ref.page, root)}` | {ref.line or ''} | `{ref.kind}` | `{source}` |"
            )
        lines.append("")

    table("Remote image references", result.remote)
    table("Missing local image files", result.missing_local)
    table("Alt-text review", result.alt_issues)

    by_source: dict[str, set[str]] = defaultdict(set)
    for ref in result.remote:
        by_source[ref.source].add(relative(ref.page, root))
    duplicates = {source: pages for source, pages in by_source.items() if len(pages) > 1}

    lines.extend(["## Remote sources reused across pages", ""])
    if not duplicates:
        lines.extend(["None.", ""])
    else:
        lines.extend(["| Source | Pages |", "|---|---:|"])
        for source, pages in sorted(duplicates.items(), key=lambda item: (-len(item[1]), item[0])):
            lines.append(f"| `{source.replace('|', '%7C')}` | {len(pages)} |")
        lines.append("")

    lines.extend([
        "## Pass criteria for the image-replacement branch",
        "",
        "- No unapproved remote photographic URLs on implemented pages.",
        "- No missing local image files.",
        "- Every informative image has meaningful alt text.",
        "- Decorative images use intentional empty alt text or CSS backgrounds.",
        "- Page-specific hero photography is not reused across unrelated pages.",
        "",
    ])
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit website image references")
    parser.add_argument("--root", default=".", help="Repository root directory")
    parser.add_argument(
        "--output",
        default="image-audit-report.md",
        help="Markdown report output path",
    )
    parser.add_argument(
        "--fail-on-missing",
        action="store_true",
        help="Return non-zero when local image files are missing",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    output = Path(args.output)
    if not output.is_absolute():
        output = root / output

    result = audit(root)
    output.write_text(markdown_report(result, root), encoding="utf-8")

    print(f"Image audit report: {output}")
    print(f"Remote image references: {len(result.remote)}")
    print(f"Missing local files: {len(result.missing_local)}")
    print(f"Alt-text review items: {len(result.alt_issues)}")

    if args.fail_on_missing and result.missing_local:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
