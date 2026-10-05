#!/usr/bin/env python3
"""Convert a Claude Docs markdown export into a GitHub-ready study guide.

  python tools/convert_export.py <export.md> <dest.md> --title "Mini Study Guide 3: ..." \
      [--subtitle "..."] [--byline-replace "Midterm prep=Final exam prep"] [--image-map placeholder=path alt]

Fixes: ```latex -> ```math; escaped brackets/asterisks; bare dollar signs escaped (outside code);
export byline cleaned; back link to the index added.
"""
import argparse, re
from pathlib import Path


def fix_prose(seg: str) -> str:
    # leave inline code spans alone
    parts = re.split(r"(`[^`\n]*`)", seg)
    out = []
    for part in parts:
        if part.startswith("`") and part.endswith("`") and len(part) > 1:
            out.append(part)
            continue
        part = part.replace("\\[", "[").replace("\\]", "]").replace("\\*", "*")
        part = re.sub(r"(?<!\\)\$", r"\\$", part)
        out.append(part)
    return "".join(out)


def convert(text: str, args) -> str:
    lines = text.replace("\r\n", "\n").split("\n")
    # drop export H1 and byline (first non-empty lines)
    while lines and not lines[0].strip():
        lines.pop(0)
    assert lines[0].startswith("# "), "expected an H1 first"
    lines.pop(0)
    while lines and not lines[0].strip():
        lines.pop(0)
    if args.drop_line and lines and lines[0].startswith(args.drop_line):
        lines.pop(0)
        while lines and not lines[0].strip():
            lines.pop(0)
    byline = "" if args.no_byline else lines.pop(0).replace("@Jim Northey", "Jim Northey").strip()
    for rep in args.byline_replace or []:
        a, b = rep.split("=", 1)
        byline = byline.replace(a, b)
    body = "\n".join(lines).strip("\n")
    # $$ display math (single- or multi-line) -> GitHub math fence
    body = re.sub(r"^\$\$[ \t]*\n?(.*?)\n?[ \t]*\$\$[ \t]*$",
                  lambda m: "```math\n" + m.group(1).strip() + "\n```", body, flags=re.S | re.M)

    # split on fenced code blocks
    chunks = re.split(r"(^```[^\n]*\n.*?^```[ \t]*$)", body, flags=re.S | re.M)
    out = []
    for ch in chunks:
        if ch.startswith("```"):
            ch = re.sub(r"^```latex", "```math", ch)
            out.append(ch)
        else:
            out.append(fix_prose(ch))
    body = "".join(out)

    for spec in args.image or []:
        key, rest = spec.split("=", 1)
        path, alt = rest.split("|", 1)
        pat = re.compile(r"^&#91;embedded content: " + re.escape(key) + r"[^\n]*\n?", re.M)
        # the placeholder may have been unescaped already; handle both forms
        pat2 = re.compile(r"^\[embedded content: " + re.escape(key) + r"[^\n]*\n?", re.M)
        repl = f"![{alt}]({path})\n"
        body, n1 = pat.subn(repl, body)
        body, n2 = pat2.subn(repl, body)
        assert n1 + n2 == 1, f"placeholder {key!r} not found"
    assert "embedded content" not in body, "unreplaced embedded-content placeholder"

    head = [f"# {args.title}", ""]
    if args.subtitle:
        head += [f"*{args.subtitle}*", ""]
    head += ["[← All study guides](../../study-guide-index.md)", ""] + ([byline, ""] if byline else [])
    return "\n".join(head) + "\n" + body.strip("\n") + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dest")
    ap.add_argument("--title", required=True)
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--byline-replace", action="append")
    ap.add_argument("--no-byline", action="store_true", help="export has no byline line under the H1")
    ap.add_argument("--drop-line", default="", help="drop a first line (after the H1) that starts with this text")
    ap.add_argument("--image", action="append", help="'placeholder text start=relative/path.png|alt text'")
    a = ap.parse_args()
    Path(a.dest).write_text(convert(Path(a.src).read_text(encoding="utf-8"), a), encoding="utf-8")
    print("wrote", a.dest)


if __name__ == "__main__":
    main()
