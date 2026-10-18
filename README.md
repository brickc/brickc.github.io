# cameronbrick.com

Static site built by GitHub Pages (Jekyll). No server, database, or plugins to maintain.

## Everyday editing

- **Edit a page:** open the `.md` file on github.com, click the pencil, edit, and click *Commit changes*. The site updates in about a minute.
  - `index.md` is the front page; the other pages are named after their URL (`writing.md` is `/writing`).
- **Menu:** `_data/nav.yml`. Add or reorder entries there; every page uses it.
- **Images:** upload to `assets/img/` (*Add file > Upload files*), then reference them as `![](/assets/img/name.jpg)`.
- **Publications:** don't edit these here. They come from the CV on Dropbox (see below).

## Publications sync

Once a day, `.github/workflows/site.yml` downloads the CV from its Dropbox link, takes everything
between the "Peer-Reviewed Publications" and "Media Coverage" headings, and writes it to
`_includes/publications.html`, which the front page includes. If something changed, it commits and republishes.

- To update right away: *Actions* tab > *Update and publish site* > *Run workflow*.
- Dropbox `dl=0` PDF links are rewritten to `raw=1` so PDFs open in the browser.
- Keep overwriting the same Dropbox file (`Brick-CV.docx`) so the link never changes. If the link
  does change, update `CV_URL` in the workflow file and the CV entry in `_data/nav.yml`.
- If the download fails, the headings are renamed, or fewer than 50 entries are found, the run stops,
  the site is left as it was, and GitHub emails you.

## One-time setup

1. Create a **public** repository on your personal GitHub account named exactly
   `<username>.github.io`, and upload these files (or let Claude push them).
2. *Settings > Pages > Build and deployment > Source:* **GitHub Actions**.
3. *Actions* tab > *Update and publish site* > *Run workflow*. Preview the result at `https://<username>.github.io`.
4. *Settings > Pages > Custom domain:* `www.cameronbrick.com`. Save.
5. At NearlyFreeSpeech, *Domains > cameronbrick.com > DNS*: remove the Squarespace records
   (A records to Squarespace IPs, `www` CNAME to `ext-cust.squarespace.com`, any Squarespace verification CNAME), then add:

   | Name | Type | Value |
   |---|---|---|
   | (blank) | A | 185.199.108.153 |
   | (blank) | A | 185.199.109.153 |
   | (blank) | A | 185.199.110.153 |
   | (blank) | A | 185.199.111.153 |
   | www | CNAME | `<username>.github.io.` |

   **Leave any MX or TXT records for email alone.**
6. Back in *Settings > Pages*, wait for the DNS check to pass, then tick **Enforce HTTPS**.
7. Recommended: verify the domain under your GitHub profile *Settings > Pages > Verified domains*,
   so nobody else can claim it if the repo is ever deleted.
8. Check the live site, then cancel Squarespace.
