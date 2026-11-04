"""Extract the publications section from the CV (.docx).

Writes two files:
  _includes/publications.html         the full list (shown on /publications)
  _includes/publications-recent.html  the most recent entries (shown on the front page)

Usage: python3 scripts/update_publications.py CV.docx [_includes/publications.html]

Takes everything after the "Peer-Reviewed Publications" heading (skipping the summary
table) up to the "Media Coverage" heading. Exits with an error, leaving the existing file
untouched, if the result looks wrong.
"""
import re, subprocess, sys
from bs4 import BeautifulSoup

START, END, MIN_ITEMS = 'Peer-Reviewed Publications', 'Media Coverage', 50
N_RECENT = 5   # entries shown on the front page

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

# Front page: highlighted papers listed in highlights.txt (by DOI), from the last HIGHLIGHT_YEARS
# years; if none qualify, fall back to the most recent N_RECENT entries (the CV lists newest first).
import datetime, os
HIGHLIGHT_YEARS = 5
all_items = BeautifulSoup(result, 'html.parser').find_all('li')

def item_year(li):
    m = re.search(r'\((\d{4})', li.get_text(' '))
    return int(m.group(1)) if m else None

def item_dois(li):
    return {m.group(1).lower().rstrip('.') for a in li.find_all('a', href=True)
            for m in [re.search(r'(10\.\d{4,9}/[^\s?#]+)', a['href'])] if m}

wanted = []
if os.path.exists('highlights.txt'):
    wanted = [l.strip().lower() for l in open('highlights.txt', encoding='utf-8')
              if l.strip() and not l.lstrip().startswith('#')]
    wanted = [re.sub(r'^(https?://)?(dx\.)?doi\.org/', '', d).rstrip('.') for d in wanted]
cutoff = datetime.date.today().year - HIGHLIGHT_YEARS + 1
chosen = []
for d in wanted:
    match = next((li for li in all_items if d in item_dois(li)), None)
    if match is None:
        print(f'::warning::Highlight DOI {d} not found in the CV publications')
    elif (item_year(match) or 9999) < cutoff:
        print(f'Highlight {d} is older than {HIGHLIGHT_YEARS} years; skipped')
    else:
        chosen.append(match)

heading = 'Highlights' if chosen else 'Recent'
items = chosen or all_items[:N_RECENT]
recent_out = out.replace('publications.html', 'publications-recent.html')
with open(recent_out, 'w', encoding='utf-8') as f:
    f.write('<!-- Generated from the CV by scripts/update_publications.py. Do not edit by hand. -->\n'
            f'<h3>{heading}</h3>\n'
            '<ul class="publications pub-recent">\n' + '\n'.join(str(li) for li in items) + '\n</ul>\n'
            f'<p><a href="/publications">All {n_items} publications →</a></p>\n')
print(f'Wrote {len(items)} {heading.lower()} publications to {recent_out}')
