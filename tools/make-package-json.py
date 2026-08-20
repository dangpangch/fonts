#!/usr/bin/env python3
"""Generate package.json for the zira-font npm package.

Usage:
    python3 tools/make-package-json.py <version> <output_dir>

The package ships the web build (WOFF2 + CSS, under `zira/`) so it can be
served by the jsDelivr npm CDN:

    https://cdn.jsdelivr.net/npm/zira-font@latest/zira/fonts.css
"""

import json
import re
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {Path(sys.argv[0]).name} <version> <output_dir>", file=sys.stderr)
        return 1
    version = sys.argv[1].strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+(-[0-9A-Za-z.-]+)?(\+[0-9A-Za-z.-]+)?", version):
        print(f"ERROR: invalid npm version '{version}' (expected semver, e.g. 0.1.0)",
              file=sys.stderr)
        return 1
    out_dir = Path(sys.argv[2])
    pkg = {
        "name": "zira-font",
        "version": version,
        "description": (
            "Zira Mono, Zira Sans and Zira Serif - custom fonts built from Iosevka "
            "(web build: WOFF2 + CSS)"
        ),
        "license": "OFL-1.1",
        "files": ["zira"],
        "keywords": ["font", "fonts", "woff2", "iosevka", "zira"],
        "repository": {"type": "git", "url": "https://github.com/dangpang/zira-font.git"},
        "homepage": "https://github.com/dangpang/zira-font",
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "package.json").write_text(json.dumps(pkg, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_dir / 'package.json'} (version {version})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
