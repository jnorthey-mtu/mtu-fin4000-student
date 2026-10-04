#!/usr/bin/env python3
"""Build a PDF for each study guide markdown file.

Usage:  python tools/build_pdfs.py [path/to/guide.md ...]
With no arguments, every study-guides/<type>/<prefix>-NN-*.md is rebuilt.
PDFs land in the pdf/ folder beside the markdown, with the same file name stem.

GitHub math syntax is converted for pandoc first:
  ```math ... ```  ->  $$ ... $$        $`x`$  ->  $x$
Requires pandoc and xelatex.
"""
import re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDES = ROOT / "study-guides"
TYPES = ("general", "mini", "current-events", "supplements")


def to_pandoc(md: str) -> str:
    md = re.sub(r"```math\n(.*?)\n```", lambda m: "$$\n" + m.group(1) + "\n$$", md, flags=re.S)
    md = re.sub(r"\$`(.+?)`\$", r"$\1$", md)
    md = md.replace("\u2610", "\u25a1")  # ballot box missing from the serif font
    # Back link points at the index, which is not part of a standalone PDF.
    md = re.sub(r"^\[← All study guides\]\([^)]*\)\n\n?", "", md, flags=re.M)
    return md


def build(src: Path) -> Path:
    out_dir = src.parent / "pdf"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / (src.stem + ".pdf")
    with tempfile.TemporaryDirectory() as tmp:
        tmp_md = Path(tmp) / src.name
        tmp_md.write_text(to_pandoc(src.read_text(encoding="utf-8")), encoding="utf-8")
        subprocess.run(
            ["pandoc", str(tmp_md), "-f", "markdown-smart+task_lists+tex_math_dollars",
             "-o", str(out), "--pdf-engine=xelatex", "--resource-path", str(src.parent), "--template", str(ROOT / "tools" / "guide.latex"),
             "-V", "geometry:margin=0.9in", "-V", "fontsize=10.5pt",
             "-V", "mainfont=DejaVu Serif", "-V", "monofont=DejaVu Sans Mono",
             "-V", "colorlinks=true", "-V", "linkcolor=blue", "-V", "urlcolor=blue"],
            check=True)
    return out


def main(argv):
    files = [Path(a) for a in argv] or sorted(
        p for t in TYPES for p in (GUIDES / t).glob("*-[0-9][0-9]-*.md"))
    for f in files:
        print("built", build(f.resolve()).relative_to(ROOT))


if __name__ == "__main__":
    main(sys.argv[1:])
