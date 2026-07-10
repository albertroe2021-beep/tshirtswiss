from pathlib import Path
import os
import re

repo = Path('/workspaces/tshirtswiss')


def counterpart_path(path: Path) -> str | None:
    rel = path.relative_to(repo).as_posix()
    if rel == 'de/index.html':
        return 'pages/home/index.html'
    if rel == 'pages/home/index.html':
        return 'de/home/index.html'
    if rel == 'pages/home/preview.html':
        return 'de/home/preview.html'
    if rel == 'de/home/preview.html':
        return 'pages/home/preview.html'
    if rel.startswith('pages/'):
        return rel.replace('pages/', 'de/', 1)
    if rel.startswith('de/'):
        return rel.replace('de/', 'pages/', 1)
    return None


def relative_link(current_path: Path, target_rel: str) -> str:
    target_path = repo / target_rel
    target_dir = target_path.parent if target_path.name in {'index.html', 'preview.html'} else target_path
    rel = os.path.relpath(target_dir, current_path.parent).replace('\\', '/')
    if rel == '.':
        return './'
    if not rel.startswith('.'):
        rel = './' + rel
    return rel.rstrip('/') + '/'


for path in sorted([*repo.glob('pages/**/*.html'), *repo.glob('de/**/*.html')]):
    if not path.is_file():
        continue
    text = path.read_text(encoding='utf-8', errors='ignore')
    if 'class="langs"' not in text and 'class="mobile-lang"' not in text:
        continue

    target_rel = counterpart_path(path)
    if not target_rel:
        continue

    current_is_german = path.relative_to(repo).as_posix().startswith('de/') or path.name == 'index.html' and path.parent.name == 'de'
    target_link = relative_link(path, target_rel)
    if current_is_german:
        en_link = target_link
        de_link = './'
    else:
        en_link = './'
        de_link = target_link

    replacement = f'<div class="langs"><a href="{en_link}">EN</a><span>|</span><a href="{de_link}">DE</a></div>'

    new_text = text
    pattern = re.compile(r'(<div class="langs"[^>]*>).*?</div>', re.S)
    new_text, count = pattern.subn(lambda m: replacement, new_text, count=1)
    if count == 0:
        pattern = re.compile(r'(<div class="mobile-lang"[^>]*>).*?</div>', re.S)
        new_text, count = pattern.subn(lambda m: replacement.replace('class="langs"', 'class="mobile-lang"'), new_text, count=1)

    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        print(path.relative_to(repo).as_posix())
