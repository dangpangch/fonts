#!/usr/bin/env python3
"""Generate package.json for the @dangpang/zira-fonts npm package.

Usage:
    python3 tools/make-package-json.py <version> <output_dir>

The package ships the web build (WOFF2 + CSS, under `zira/`) so it can be
served by the jsDelivr npm CDN:

    https://cdn.jsdelivr.net/npm/@dangpang/zira-fonts@latest/zira/fonts.css
"""

import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {Path(sys.argv[0]).name} <version> <output_dir>", file=sys.stderr)
        return 1
    version, out_dir = sys.argv[1], Path(sys.argv[2])
    pkg = {
        "name": "@dangpang/zira-fonts",
        "version": version,
        "description": (
            "Zira Mono, Zira Sans and Zira Serif - custom fonts built from Iosevka "
            "(web build: WOFF2 + CSS)"
        ),
        "license": "OFL-1.1",
        "files": ["zira"],
        "keywords": ["font", "fonts", "woff2", "iosevka", "zira"],
        "repository": {"type": "git", "url": "https://github.com/dangpangch/fonts.git"},
        "homepage": "https://github.com/dangpangch/fonts",
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "package.json").write_text(json.dumps(pkg, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_dir / 'package.json'} (version {version})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
