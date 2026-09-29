#!/usr/bin/env python3
"""Run before every commit: stamps app.css / app.js / supabase.js links in index.html
with a short hash of their contents, so a tablet never mixes an old file with a new one
(and index.html changes, which is what the app's "new version" check looks at)."""
import hashlib, re, pathlib
root = pathlib.Path(__file__).parent
html = (root / 'index.html').read_text()
for f in ['app.css', 'app.js', 'supabase.js']:
    h = hashlib.sha256((root / f).read_bytes()).hexdigest()[:10]
    html = re.sub(re.escape(f) + r'\?v=[0-9a-z]+', f + '?v=' + h, html)
(root / 'index.html').write_text(html)
print('stamped', ', '.join(re.findall(r'(\w+\.\w+)\?v=(\w+)', html) and [a + '=' + b for a, b in re.findall(r'(\w+\.(?:css|js))\?v=(\w+)', html)]))
