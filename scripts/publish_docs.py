from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = ROOT / "docs"


def main() -> int:
    """Build the MkDocs site into docs/ for GitHub Pages."""
    cmd = [
        sys.executable,
        "-m",
        "mkdocs",
        "build",
        "--strict",
        "--site-dir",
        str(SITE_DIR),
    ]
    subprocess.run(cmd, cwd=ROOT, check=True)
    nojekyll = SITE_DIR / ".nojekyll"
    nojekyll.write_text("", encoding="utf-8")
    print(f"Docs published to {SITE_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
