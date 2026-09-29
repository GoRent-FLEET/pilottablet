# Go Rent 4×4 — Tablet App

Live: https://gorent-fleet.github.io/tablet/

Files:
- `index.html` — the page (menus, sign-in screens)
- `app.css` — styles
- `app.js` — the app
- `supabase.js` — database library (pinned v2.117.2, kept here so tablets never depend on a CDN)
- `view.html` — client-facing report viewer

**Before every commit run `python3 stamp.py`.** It stamps the file links in index.html with a hash
of their contents, so tablets never mix an old app.js with a new page, and the app's
"new version available" check (which watches index.html) notices the update.

Who may do what: the `ROLE` map at the top of app.js (staff / manager / peter).
