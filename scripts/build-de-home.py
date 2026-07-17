from pathlib import Path

source = Path('pages/home/index.html')
target = Path('de/home/index.html')
html = source.read_text(encoding='utf-8')

# Structural localisation for the German homepage.
html = html.replace('<html lang="en">', '<html lang="de-CH">')
html = html.replace('src="../', 'src="../../')
html = html.replace('href="../pages/', 'href="../')
html = html.replace('action="../pages/', 'action="../')
html = html.replace('<span