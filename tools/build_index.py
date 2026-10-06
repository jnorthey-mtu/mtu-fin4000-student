#!/usr/bin/env python3
"""Regenerate study-guide-index.md from study-guides/guides.json.

Only guides whose markdown file exists are listed. A PDF link is added when the
matching pdf/ file exists. Run after adding or renaming a guide:
    python tools/build_index.py
"""
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDES = ROOT / "study-guides"
SECTIONS = [
    ("midterm", "Midterm study guide", "Review of everything the midterm covers, chapter by chapter."),
    ("general", "General study guides", "In-depth guides on a topic, with worked examples, calculator and spreadsheet steps, and practice questions."),
    ("mini", "Mini study guides", "Short guides on one under-covered idea: learning objectives, worked examples with BA II Plus keystrokes, pitfalls, and CFA-style questions with an answer key."),
    ("current-events", "Current-events study guides", "Course concepts applied to what is happening in the markets now."),
    ("supplements", "Supplements", "Reference material that supports the guides, such as conventions and notation."),
]


def number(name):
    m = re.match(r"[a-z]+-(\d\d)-", name)
    return m.group(1) if m else "—"


def main():
    meta = json.loads((GUIDES / "guides.json").read_text(encoding="utf-8"))
    out = [
        "# FIN 4000 Study Guide Index", "",
        "Study guides for MTU FIN 4000 (Investments), aligned with Bodie, Kane & Marcus, *Investments*, 13th edition. "
        "Each guide is a GitHub markdown file with a matching downloadable PDF.", "",
        "File names follow `<type>-<NN>-<title>`: `gen-` general, `mini-` mini, `ce-` current events, `supp-` supplements. "
        "Each type is numbered separately.", "",
    ]
    for folder, heading, blurb in SECTIONS:
        out += [f"## {heading}", "", blurb, ""]
        rows = []
        for rel, m in sorted(meta.items()):
            if not rel.startswith(folder + "/") or not (GUIDES / rel).exists():
                continue
            p = Path(rel)
            pdf = GUIDES / folder / "pdf" / (p.stem + ".pdf")
            links = f"[md](study-guides/{rel})"
            if pdf.exists():
                links += f" · [pdf](study-guides/{folder}/pdf/{p.stem}.pdf)"
            qti = GUIDES / folder / "qti" / (p.stem + "-qti.zip")
            if qti.exists():
                links += f" · [qti](study-guides/{folder}/qti/{p.stem}-qti.zip)"
            ch = m["chapters"] or "\u2014"
            rows.append(f"| {number(p.name)} | {m['title']} | {ch} | {m['summary']} | {links} |")
        if rows:
            out += ["| # | Guide | BKM Ch. | Topics | Files |", "| --- | --- | --- | --- | --- |"] + rows + [""]
        else:
            out += ["*None yet.*", ""]
    out += ["## Notes", "",
            "- Equations use GitHub's protected math syntax: ```` ```math ```` blocks and `` $`...`$ `` inline.",
            "- PDFs are built from the markdown with `python tools/build_pdfs.py`; this index is built with `python tools/build_index.py`.",
            "- CFA-style questions are original and are not CFA Institute material.", ""]
    (ROOT / "study-guide-index.md").write_text("\n".join(out), encoding="utf-8")
    print("wrote study-guide-index.md")


if __name__ == "__main__":
    main()
