# cameronbrick.com

Static site built by GitHub Pages (Jekyll) and Claude.

## Editing

- **Edit a page:** open the `.md` file on github.com, click the pencil, edit, and click *Commit changes*. The site updates in about a minute.
  - `index.md` is the front page; the other pages are named after their URL (`writing.md` is `/writing`).
- **Menu:** `_data/nav.yml`. Add or reorder entries there; every page uses it.
- **Images:** upload to `assets/img/` (*Add file > Upload files*), then reference them as `![](/assets/img/name.jpg)`.

## Publications sync

Once a day, `.github/workflows/site.yml` downloads the CV from its Dropbox link, takes everything
between the "Peer-Reviewed Publications" and "Media Coverage" headings, and writes it to
`_includes/publications.html`, which the front page includes. If something changed, it commits and republishes.

- When the CV on Dropbox changes, the job also converts it to PDF and publishes it at `/cv.pdf`
  (the CV links in the menu and on the front page). Fonts: Times New Roman is replaced by the
  metrically identical Liberation Serif, so the layout is unchanged.
- To update right away: *Actions* tab > *Update and publish site* > *Run workflow*.
- Dropbox `dl=0` PDF links are rewritten to `raw=1` so PDFs open in the browser.
- Keep overwriting the same Dropbox file (`Brick-CV.docx`) so the link never changes. If the link
  does change, update `CV_URL` in the workflow file.
- If the download fails, the headings are renamed, or fewer than 50 entries are found, the run stops,
  the site is left as it was, and GitHub emails you.
