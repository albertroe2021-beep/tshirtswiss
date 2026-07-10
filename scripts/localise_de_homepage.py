#!/usr/bin/env python3
"""Generate the Swiss German homepage from the approved English master.

The script deliberately uses exact string replacement so the HTML structure,
CSS, JavaScript, classes, IDs and asset references remain unchanged.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "translations" / "de-CH" / "homepage.json"


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def apply_replacements(content: str, replacements: dict[str, str], label: str) -> str:
    missing: list[str] = []
    for source, target in replacements.items():
        if source not in content:
            missing.append(source)
            continue
        content = content.replace(source, target)

    if missing:
        preview = "\n".join(f"  - {item[:120]}" for item in missing)
        raise RuntimeError(
            f"{label}: {len(missing)} expected source strings were not found.\n{preview}\n"
            "The English master may have changed. Review the translation map before regenerating."
        )
    return content


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--check", action="store_true", help="Validate without writing the target file")
    args = parser.parse_args()

    config = load_config(args.config)
    source = ROOT / config["source"]
    target = ROOT / config["target"]

    if not source.exists():
        raise FileNotFoundError(f"English homepage not found: {source}")

    content = source.read_text(encoding="utf-8")
    content = apply_replacements(content, config["replacements"], "Content translations")
    content = apply_replacements(content, config["link_replacements"], "German link mapping")

    # Swiss Standard German uses ss rather than the German ß character.
    if "ß" in content:
        raise RuntimeError("Swiss German output contains ß. Replace it with ss before publishing.")

    # Catch the most important routing and locale regressions.
    required = (
        '<html lang="de-CH">',
        'href="./products/"',
        'href="./industries/"',
        'href="./services/"',
        'href="./request-a-quote/"',
    )
    for marker in required:
        if marker not in content:
            raise RuntimeError(f"Required German homepage marker missing: {marker}")

    if "../pages/" in content:
        raise RuntimeError("English /pages/ links remain in the generated German homepage.")

    if args.check:
        print(f"Validated {target.relative_to(ROOT)} successfully.")
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    print(f"Generated {target.relative_to(ROOT)} from {source.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
