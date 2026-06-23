"""Apply the shared TShirtSwiss header to generated HTML pages.

This script is intended to be run from the repository root. It replaces each
page's old hardcoded topbar/header with the shared dropdown header from
scripts/shared_header.py and injects the shared header CSS into <head>.
"""

from pathlib import Path
import re

from shared_header import build_header, header_style_tag

ROOT = Path(__file__).resolve().parent.parent
TARGETS = sorted((ROOT / "pages").glob("**/*.html"))

HEADER_RE = re.compile(
    r'<div\s+class="(?:topbar|ts-topbar)"[\s\S]*?<header\s+class="(?:site-header|header|ts-header)"[\s\S]*?</header>',
    re.IGNORECASE,
)
STYLE_RE = re.compile(r'<style\s+id="ts-global-header-css">[\s\S]*?</style>\s*', re.IGNORECASE)
BODY_RE = re.compile(r'<body([^>]*)>', re.IGNORECASE)
HEAD_CLOSE_RE = re.compile(r'</head>', re.IGNORECASE)


def prefix_for(path: Path) -> str:
    relative = Path(path).parent.relative_to(ROOT)
    prefix = Path(".").relative_to(Path(".")) if False else None
    rel = Path(*([".."] * len(relative.parts))) if relative.parts else Path(".")
    value = rel.as_posix()
    return "" if value == "." else value + "/"


def apply_to_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    html = STYLE_RE.sub("", original)

    prefix = prefix_for(path)
    header = build_header(prefix)

    if HEADER_RE.search(html):
        html = HEADER_RE.sub(header, html, count=1)
    else:
        html = BODY_RE.sub(lambda m: f'<body{m.group(1)}>\n{header}', html, count=1)

    html = HEAD_CLOSE_RE.sub(f'{header_style_tag()}\n</head>', html, count=1)

    if html != original:
        path.write_text(html, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed = []
    for path in TARGETS:
        if apply_to_file(path):
            changed.append(path.relative_to(ROOT).as_posix())

    print(f"Updated {len(changed)} HTML pages with shared header.")
    for item in changed:
        print(item)


if __name__ == "__main__":
    main()
