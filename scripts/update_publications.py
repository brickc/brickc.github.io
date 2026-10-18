"""Extract the publications section from the CV (.docx) into _includes/publications.html.

Usage: python3 scripts/update_publications.py CV.docx [_includes/publications.html]

Takes everything after the "Peer-Reviewed Publications" heading (skipping the summary
table) up to the "Media Coverage" heading. Exits with an error, leaving the existing file
untouched, if the result looks wrong.
"""
import re, subprocess, sys
from bs4 import BeautifulSoup

START, END, MIN_ITEMS = 'Peer-Reviewed Publications', 'Media Coverage', 50

cv = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else '_includes/publications.html'

html = subprocess.run(['pandoc', cv, '-f', 'docx', '-t', 'html', '--wrap=none'],
                      capture_output=True, text=True, check=True).stdout
body = BeautifulSoup(html, 'html.parser')

nodes = list(body.children)
def text(n): return n.get_text(' ', strip=True) if hasattr(n, 'get_text') else str(n).strip()

try:
    i = next(k for k, n in enumerate(nodes) if START in text(n))
    j = next(k for k, n in enumerate(nodes) if k > i and text(n).startswith(END))
except StopIteration:
    sys.exit(f'Could not find "{START}" ... "{END}" in the CV. Were the headings renamed?')

section = [n for n in nodes[i + 1:j] if getattr(n, 'name', None) != 'table']

parts = []
for n in section:
    t = text(n)
    if not t:
        continue
    if getattr(n, 'name', None) == 'p' and re.fullmatch(r'(19|20)\d\d', t):
        parts.append(f'<h3 class="pub-year">{t}</h3>')   # year headings
    else:
        parts.append(str(n))
result = '\n'.join(parts)

# Dropbox links open in the browser instead of the Dropbox page
result = re.sub(r'(https://www\.dropbox\.com/[^"\s]*?)(\?|&amp;|&)dl=[01]', r'\1\2raw=1', result)
# Strip Word bookmarks pandoc carries over
result = re.sub(r'<span id="[^"]*" class="anchor"></span>', '', result)

n_items = result.count('<li')
if n_items < MIN_ITEMS:
    sys.exit(f'Only {n_items} publications found (expected at least {MIN_ITEMS}); not updating.')

with open(out, 'w', encoding='utf-8') as f:
    f.write('<!-- Generated from the CV by scripts/update_publications.py. Do not edit by hand; '
            'edits are overwritten on the next CV sync. -->\n<div class="publications">\n'
            + result + '\n</div>\n')
print(f'Wrote {n_items} publications to {out}')
