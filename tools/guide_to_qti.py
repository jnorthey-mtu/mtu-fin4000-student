#!/usr/bin/env python3
"""Build a Canvas-importable QTI zip from the CFA-style questions in a study guide.

  python tools/guide_to_qti.py study-guides/mini/mini-03-mutual-fund-costs.md   # one guide
  python tools/guide_to_qti.py --all                                          # every guide with questions
  python tools/guide_to_qti.py --check                                        # parse only, report counts

Questions are three-choice (A-C). The guide's answer key supplies the correct answer and the
explanation, which Canvas shows as feedback. Output: <type>/qti/<guide-stem>-qti.zip
Requires: pip install text2qti
"""
import re, sys, json, subprocess, tempfile, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUIDES = ROOT / "study-guides"
TYPES = ("general", "mini", "current-events", "supplements")

STEM_BOLD = re.compile(r"^\*\*(?:Q)?(\d+)[ .]*(?:[\[(][^\])]*[\])])?\.?\*\*\s*(.*)$")
STEM_LIST = re.compile(r"^(\d+)\. (?![A-C]\. )(.+)$")
OPT = re.compile(r"^\s*(?:- )?([A-C])\. (.+)$")
ANS_TABLE = re.compile(r"^\|\s*(\d+)\s*\|\s*([A-C])\s*\|\s*(.*?)\s*\|?\s*$")
ANS_LIST = re.compile(r"^(\d+)\. (?:\*\*([A-C])\.?\*\*|([A-C])\.) ?(.*)$")


def clean(s: str) -> str:
    s = re.sub(r"\$`(.+?)`\$", r"\1", s)              # GitHub inline math -> plain text
    s = re.sub(r"\[([^\]]+)\]\((?:[^)]+)\)", r"\1", s)  # links -> text
    return s.strip()


def parse(path: Path):
    lines = path.read_text(encoding="utf-8").split("\n")
    questions, answers = [], {}
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        mb = STEM_BOLD.match(ln)
        m = mb or STEM_LIST.match(ln)
        if m:
            num, stem = int(m.group(1)), m.group(2)
            j, opts = i + 1, {}
            while j < len(lines) and len(opts) < 3:
                raw = lines[j].rstrip()
                o = OPT.match(raw)
                if o:
                    opts[o.group(1)] = o.group(2)
                elif raw.strip():
                    break                     # any other text ends the question block
                elif not mb:
                    break                     # list-style stems need options on the next lines
                j += 1
            if sorted(opts) == ["A", "B", "C"] and stem.strip():
                questions.append({"n": num, "stem": clean(stem), "opts": {k: clean(v) for k, v in opts.items()}})
                i = j
                continue
        t = ANS_TABLE.match(ln)
        if t:
            answers[int(t.group(1))] = (t.group(2), clean(t.group(3)))
        else:
            a = ANS_LIST.match(ln)
            if a:
                answers[int(a.group(1))] = (a.group(2) or a.group(3), clean(a.group(4)))
        i += 1
    return questions, answers


def title_of(path: Path) -> str:
    h1 = path.read_text(encoding="utf-8").split("\n", 1)[0].lstrip("# ").strip()
    return h1


def quiz_text(path: Path, questions, answers, overrides=None):
    h1 = title_of(path)
    out = [f"Quiz title: {h1}: Practice Quiz",
           f"Quiz description: Practice questions from the FIN 4000 study guide \"{h1}\". Each answer shows an explanation after submission.",
           "Shuffle answers: true", "Show correct answers: true", ""]
    for q in questions:
        key, expl = answers[q["n"]]
        stem = (overrides or {}).get(q["n"], q["stem"])
        out.append(f"{q['n']}. {stem}")
        if expl:
            out.append(f"... {expl}")
        for letter in "ABC":
            out.append(f"{'*' if letter == key else ''}{letter.lower()}) {q['opts'][letter]}")
        out.append("")
    return "\n".join(out)


def build(path: Path, check_only=False):
    questions, answers = parse(path)
    if not questions:
        return None
    nums = [q["n"] for q in questions]
    missing = [n for n in nums if n not in answers]
    if missing:
        raise SystemExit(f"{path.name}: no answer found for questions {missing}")
    if check_only:
        return len(questions)
    ov_file = Path(__file__).with_name("qti_overrides.json")
    overrides = json.loads(ov_file.read_text(encoding="utf-8")).get(path.name, {}) if ov_file.exists() else {}
    overrides = {int(k): v for k, v in overrides.items()}
    out_dir = path.parent / "qti"
    out_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / (path.stem + "-qti.txt")
        src.write_text(quiz_text(path, questions, answers, overrides), encoding="utf-8")
        subprocess.run(["text2qti", str(src)], check=True, cwd=tmp, capture_output=True)
        zip_src = Path(tmp) / (path.stem + "-qti.zip")
        (out_dir / zip_src.name).write_bytes(zip_src.read_bytes())
    return len(questions)


# Guides that already have a hand-built QTI package elsewhere (not regenerated here).
HAS_QTI = {"gen-09-ipo-process-and-underwriters-role.md",
           "ce-03-why-bond-yields-are-rising.md",
           "ce-05-treasury-buybacks-and-bond-yields.md"}


def all_guides():
    return sorted(p for t in TYPES for p in (GUIDES / t).glob("*-[0-9][0-9]-*.md") if p.name not in HAS_QTI)


if __name__ == "__main__":
    args = sys.argv[1:]
    check = "--check" in args
    files = all_guides() if ("--all" in args or check) else [Path(a).resolve() for a in args if not a.startswith("--")]
    for f in files:
        try:
            n = build(f, check_only=check)
        except SystemExit as e:
            print(f"PROBLEM {e}")
            continue
        if n:
            print(f"{f.name}: {n} questions" + ("" if check else " -> qti/"))
        else:
            print(f"{f.name}: no A-C questions found (skipped)")
