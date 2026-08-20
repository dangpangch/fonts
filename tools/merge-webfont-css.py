#!/usr/bin/env python3
"""Merge the per-family webfont CSS files into `zira/fonts.css`.

The CI workflow copies Iosevka's generated stylesheet for each family into
`zira/<sub>/<Plan>.css` (e.g. `zira/mono/ZiraMono.css`), next to its `WOFF2/`
and `TTF/` directories. This script concatenates all of them into
`zira/fonts.css`, rewriting the relative font URLs so they resolve from the
`zira/` root:

    url('WOFF2/ZiraMono-Regular.woff2')  ->  url('mono/WOFF2/ZiraMono-Regular.woff2')

Run from anywhere; paths are resolved relative to this script.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZIRA_DIR = ROOT / "zira"

HEADER = "/* Merged by tools/merge-webfont-css.py - do not edit by hand. */\n"

URL_RE = re.compile(r"url\('(WOFF2|TTF)/")


def main():
    parts: list[str] = []
    for sub in sorted(p for p in ZIRA_DIR.iterdir() if p.is_dir()):
        css_files = sorted(sub.glob("*.css"))
        if not css_files:
            continue
        for css_file in css_files:
            text = css_file.read_text(encoding="utf-8")
            text = URL_RE.sub(lambda m: f"url('{sub.name}/{m.group(1)}/", text)
            parts.append(f"/* ===== {sub.name}/{css_file.name} ===== */\n" + text.strip() + "\n")
    if not parts:
        print("ERROR: no family CSS files found under zira/; nothing to merge", file=sys.stderr)
        return 1
    (ZIRA_DIR / "fonts.css").write_text(HEADER + "\n".join(parts), encoding="utf-8")
    print(f"Wrote {ZIRA_DIR / 'fonts.css'} merged from {len(parts)} CSS file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
