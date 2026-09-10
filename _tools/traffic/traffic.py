#!/usr/bin/env python3
"""TRAFFIC — the separate window.

Every text block Claude addresses to Papi is appended here, nothing else: no tool
narration, no status lines. The page renders to _tools/traffic/TRAFFIC.html and is
republished to the fixed artifact URL recorded in SOP.md §7 rule 10.

Usage
  python _tools/traffic/traffic.py add <block.md> [--session NAME] [--stamp "YYYY-MM-DD HH:MM"]
  python _tools/traffic/traffic.py render

The store is TRAFFIC.md at the repo root: newest block first, each block introduced by a
`<!-- block -->` line followed by `## <stamp> · <session>` and the body in markdown.
"""
import argparse
import datetime as dt
import html
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MD = ROOT / "TRAFFIC.md"
HTML_OUT = HERE / "TRAFFIC.html"
BLOCK = "<!-- block -->"

HEADER = """---
title: TRAFFIC — what Claude said to Papi, and nothing else
type: comms channel (SOP §7 rule 10)
status: living — newest block first; never edited after the fact, only appended
started: 2026-09-10
---

# TRAFFIC

The separate window. Only the text blocks addressed to Papi land here, in the order they were sent, newest first. No tool narration, no status lines. Add a block with `python _tools/traffic/traffic.py add <block.md> --session <name>`; the same command re-renders `_tools/traffic/TRAFFIC.html`, which republishes to the fixed artifact URL in SOP.md §7 rule 10.

"""

# ---------------------------------------------------------------- markdown (small)

def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<em>\1</em>", s)

    def link(m):
        text, href = m.group(1), m.group(2)
        if re.match(r"^https?://", href):
            return f'<a href="{href}">{text}</a>'
        return f"<code class=\"path\">{href}</code>" if text == href else f"{text} <code class=\"path\">{href}</code>"

    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)
    s = re.sub(r'(?<![\w"\'>=/])(https?://[^\s<]+)', r'<a href="\1">\1</a>', s)
    return s


def is_fence(l): return l.startswith("```")
def is_table(l): return l.startswith("|")
def is_heading(l): return re.match(r"^#{1,6}\s+", l) is not None
def is_bullet(l): return re.match(r"^\s*[-*]\s+", l) is not None
def is_number(l): return re.match(r"^\s*\d+[.)]\s+", l) is not None
def is_hr(l): return l.strip() == "---"
def is_blank(l): return l.strip() == ""
def is_block_start(l):
    return any(f(l) for f in (is_fence, is_table, is_heading, is_bullet, is_number, is_hr, is_blank))


def table(rows):
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    body = [r for r in cells if not all(re.match(r"^:?-{2,}:?$", c) or c == "" for c in r)]
    if not body:
        return ""
    head, rest = body[0], body[1:]
    h = "<tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr>"
    b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rest)
    return f'<div class="tw"><table><thead>{h}</thead><tbody>{b}</tbody></table></div>'


def render_body(md: str) -> str:
    lines = md.strip("\n").split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        if is_fence(line):
            j, buf = i + 1, []
            while j < n and not is_fence(lines[j]):
                buf.append(lines[j]); j += 1
            out.append("<pre><code>" + html.escape("\n".join(buf)) + "</code></pre>")
            i = j + 1; continue
        if is_table(line):
            j, rows = i, []
            while j < n and is_table(lines[j]):
                rows.append(lines[j]); j += 1
            out.append(table(rows)); i = j; continue
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            lvl = min(len(m.group(1)) + 2, 5)
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i += 1; continue
        if is_bullet(line):
            j, items = i, []
            while j < n and is_bullet(lines[j]):
                items.append(re.sub(r"^\s*[-*]\s+", "", lines[j])); j += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); i = j; continue
        if is_number(line):
            j, items = i, []
            while j < n and is_number(lines[j]):
                items.append(re.sub(r"^\s*\d+[.)]\s+", "", lines[j])); j += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>"); i = j; continue
        if is_hr(line):
            out.append("<hr>"); i += 1; continue
        if is_blank(line):
            i += 1; continue
        j, buf = i, []
        while j < n and (not is_block_start(lines[j]) or j == i):
            buf.append(lines[j]); j += 1
        out.append("<p>" + inline(" ".join(buf)) + "</p>"); i = j
    return "\n".join(out)

# ---------------------------------------------------------------- store

def read_blocks():
    if not MD.exists():
        return HEADER, []
    text = MD.read_text(encoding="utf-8")
    parts = text.split("\n" + BLOCK + "\n")
    header, blocks = parts[0], []
    for p in parts[1:]:
        p = p.strip("\n")
        if not p:
            continue
        first, _, body = p.partition("\n")
        m = re.match(r"^##\s+(.*?)\s+·\s+(.*)$", first.strip())
        stamp, session = (m.group(1), m.group(2)) if m else (first.strip("# ").strip(), "")
        blocks.append({"stamp": stamp, "session": session, "body": body.strip("\n")})
    return header if header.strip() else HEADER, blocks


def write_blocks(header, blocks):
    out = header.rstrip("\n") + "\n\n"
    for b in blocks:
        out += f"{BLOCK}\n## {b['stamp']} · {b['session']}\n\n{b['body'].strip()}\n\n"
    MD.write_text(out, encoding="utf-8", newline="\n")

# ---------------------------------------------------------------- page

PAGE = """<title>Net Traffic</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@800&family=Atkinson+Hyperlegible:ital,wght@0,400;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  :root {
    --bg: #EEF0F3; --surface: #FFFFFF; --ink: #14171C; --ink-2: #4B5260; --ink-3: #7A8291;
    --line: #CFD4DC; --accent: #FF5A1F; --accent-ink: #C23C0A; --code-bg: #E4E7EC;
    --display: "Barlow Condensed", "Arial Narrow", Arial, sans-serif;
    --body: "Atkinson Hyperlegible", "Segoe UI", Verdana, sans-serif;
    --mono: "IBM Plex Mono", Consolas, "Liberation Mono", monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg: #0F1216; --surface: #171B21; --ink: #E8EAEE; --ink-2: #A9B0BC; --ink-3: #7B8492;
      --line: #2B313B; --accent: #FF6B35; --accent-ink: #FF8F62; --code-bg: #1F242C;
    }
  }
  :root[data-theme="dark"] {
    --bg: #0F1216; --surface: #171B21; --ink: #E8EAEE; --ink-2: #A9B0BC; --ink-3: #7B8492;
    --line: #2B313B; --accent: #FF6B35; --accent-ink: #FF8F62; --code-bg: #1F242C;
  }
  * { box-sizing: border-box; }
  body { margin: 0; background: var(--bg); color: var(--ink); font-family: var(--body); font-size: 18px; line-height: 1.6; }
  a { color: var(--accent-ink); text-underline-offset: 3px; overflow-wrap: anywhere; }
  a:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }
  .mast { position: sticky; top: 0; z-index: 3; background: var(--bg); border-bottom: 1px solid var(--line); }
  .mast .in { max-width: 76ch; margin: 0 auto; padding: 12px 24px; display: flex; align-items: baseline; justify-content: space-between; gap: 16px; }
  .mast h1 { margin: 0; font-family: var(--display); font-weight: 800; font-size: 30px; text-transform: uppercase; letter-spacing: 0.02em; display: flex; align-items: center; gap: 10px; }
  .mast h1 i { width: 12px; height: 12px; background: var(--accent); display: inline-block; }
  .mast .meta { font-family: var(--mono); font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--ink-2); text-align: right; }
  main { max-width: 76ch; margin: 0 auto; padding: 8px 24px 96px; }
  .day { font-family: var(--mono); font-size: 12px; letter-spacing: 0.14em; text-transform: uppercase; color: var(--ink-3); margin: 40px 0 8px; padding-bottom: 6px; border-bottom: 2px solid var(--ink); }
  article { padding: 26px 0 30px; border-bottom: 1px solid var(--line); }
  article:last-child { border-bottom: 0; }
  .stamp { font-family: var(--mono); font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--accent-ink); font-weight: 500; margin-bottom: 12px; display: flex; gap: 14px; flex-wrap: wrap; }
  .stamp .s { color: var(--ink-3); }
  article p { margin: 0 0 14px; }
  article h3, article h4, article h5 { font-family: var(--display); font-weight: 800; text-transform: uppercase; letter-spacing: 0.01em; margin: 22px 0 10px; line-height: 1.05; text-wrap: balance; }
  article h3 { font-size: 30px; } article h4 { font-size: 24px; } article h5 { font-size: 20px; }
  article ul, article ol { margin: 0 0 14px; padding-left: 22px; }
  article li { margin: 0 0 8px; }
  article li p { margin: 0; }
  article code { font-family: var(--mono); font-size: 15px; background: var(--code-bg); padding: 1px 6px; }
  article code.path { color: var(--ink-2); }
  article pre { background: var(--code-bg); padding: 14px 16px; overflow-x: auto; margin: 0 0 14px; }
  article pre code { background: none; padding: 0; font-size: 15px; }
  .tw { overflow-x: auto; margin: 0 0 16px; }
  table { border-collapse: collapse; width: 100%; font-size: 16px; font-variant-numeric: tabular-nums; }
  th, td { text-align: left; padding: 8px 12px 8px 0; border-bottom: 1px solid var(--line); vertical-align: top; }
  th { font-family: var(--mono); font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--ink-3); font-weight: 500; }
  hr { border: 0; border-top: 1px solid var(--line); margin: 18px 0; }
  .empty { color: var(--ink-3); padding: 40px 0; }
</style>
<div class="mast"><div class="in"><h1><i></i>Net Traffic</h1><div class="meta">%(count)s blocks<br>last %(last)s</div></div></div>
<main>
%(entries)s
</main>
"""


def render():
    _, blocks = read_blocks()
    entries, day = [], None
    for b in blocks:
        d = b["stamp"][:10]
        if d != day:
            entries.append(f'<div class="day">{html.escape(d)}</div>')
            day = d
        t = b["stamp"][11:].strip() or b["stamp"]
        entries.append(
            f'<article><div class="stamp"><span>{html.escape(t)}</span>'
            f'<span class="s">{html.escape(b["session"])}</span></div>{render_body(b["body"])}</article>'
        )
    if not entries:
        entries.append('<p class="empty">No traffic yet.</p>')
    last = blocks[0]["stamp"] if blocks else "—"
    HTML_OUT.write_text(PAGE % {"count": len(blocks), "last": html.escape(last), "entries": "\n".join(entries)},
                        encoding="utf-8", newline="\n")
    return HTML_OUT


def add(path, session, stamp):
    body = pathlib.Path(path).read_text(encoding="utf-8").strip()
    if not body:
        sys.exit("empty block")
    header, blocks = read_blocks()
    stamp = stamp or dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    blocks.insert(0, {"stamp": stamp, "session": session, "body": body})
    write_blocks(header, blocks)
    return render()


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add"); a.add_argument("block"); a.add_argument("--session", default="setsunadev"); a.add_argument("--stamp", default=None)
    sub.add_parser("render")
    args = ap.parse_args()
    if args.cmd == "add":
        out = add(args.block, args.session, args.stamp)
    else:
        out = render()
    _, blocks = read_blocks()
    print(f"rendered {out} · {len(blocks)} blocks")


if __name__ == "__main__":
    main()
