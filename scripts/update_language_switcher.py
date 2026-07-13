from pathlib import Path
import os
import re

repo = Path('/workspaces/tshirtswiss')


def counterpart_paths(path: Path) -> tuple[str, str] | None:
    rel = path.relative_to(repo).as_posix()

    if rel == 'pages/home/index.html':
        return 'de/home/index.html', 'fr/home/index.html'
    if rel == 'pages/home/preview.html':
        return 'de/home/preview.html', 'fr/home/preview.html'
    if rel == 'de/index.html':
        return 'pages/home/index.html', 'fr/index.html'
    if rel == 'fr/index.html':
        return 'pages/home/index.html', 'de/index.html'
    if rel == 'de/home/index.html':
        return 'pages/home/index.html', 'fr/home/index.html'
    if rel == 'fr/home/index.html':
        return 'pages/home/index.html', 'de/home/index.html'
    if rel.startswith('pages/'):
        return rel.replace('pages/', 'de/', 1), rel.replace('pages/', 'fr/', 1)
    if rel.startswith('de/'):
        return rel.replace('de/', 'pages/', 1), rel.replace('de/', 'fr/', 1)
    if rel.startswith('fr/'):
        return rel.replace('fr/', 'pages/', 1), rel.replace('fr/', 'de/', 1)
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


for path in sorted([*repo.glob('pages/**/*.html'), *repo.glob('de/**/*.html'), *repo.glob('fr/**/*.html'), *repo.glob('v2/**/*.html')]):
    if not path.is_file():
        continue
    text = path.read_text(encoding='utf-8', errors='ignore')
    if 'class="langs"' not in text and 'class="mobile-lang"' not in text:
        continue

    target_paths = counterpart_paths(path)
    if not target_paths:
        continue

    en_target, de_target, fr_target = None, None, None
    rel = path.relative_to(repo).as_posix()
    if rel.startswith('de/'):
        en_target, fr_target = target_paths
        de_target = './'
    elif rel.startswith('fr/'):
        en_target, de_target = target_paths
        fr_target = './'
    else:
        en_target = './'
        de_target, fr_target = target_paths

    if not en_target or not de_target or not fr_target:
        continue

    links = {
        'EN': relative_link(path, en_target) if en_target != './' else './',
        'DE': relative_link(path, de_target) if de_target != './' else './',
        'FR': relative_link(path, fr_target) if fr_target != './' else './',
    }

    new_text = text
    for class_name in ['langs', 'mobile-lang']:
        pattern = re.compile(rf'(<div class="{class_name}"[^>]*>).*?</div>', re.S)
        replacement = f'<div class="{class_name}"><a href="{links["EN"]}">EN</a><span>|</span><a href="{links["DE"]}">DE</a><span>|</span><a href="{links["FR"]}">FR</a></div>'
        new_text, count = pattern.subn(lambda m: replacement, new_text, count=1)

    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        print(path.relative_to(repo).as_posix())
