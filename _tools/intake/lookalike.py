#!/usr/bin/env python3
"""lookalike.py - stage 1 of the layout reader (BOLO 140, rea-02/03).

Usage:
    python _tools/intake/lookalike.py <url>

Fetches one public page with urllib and writes
_PRIVATE/intake-repos/lookalike/<host>.layout.json: STRUCTURE ONLY. Landmark
regions, heading outline (levels only, no heading text), nav items as link
text, section count, grid hints from CSS class names, color tokens found in
inline styles. It never stores the page's prose, images or brand assets.

Copyright: structure and ideas only. Page text, images, logos and brand marks
belong to their owners and are never copied; a layout is not a license to
reproduce a design.
"""
import json
import os
import re
import sys
import urllib.request
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "_PRIVATE", "intake-repos", "lookalike")
LANDMARKS = ("header", "nav", "main", "aside", "footer", "article", "section", "form")
GRID = re.compile(r"\b(grid[\w-]*|col(?:umn)?s?-[\w-]+|flex[\w-]*|row|container|sidebar|card[\w-]*|hero[\w-]*)\b", re.I)
COLOR = re.compile(r"#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)")


class L(HTMLParser):
    def __init__(self):
        super().__init__()
        self.landmarks, self.outline, self.nav, self.grid, self.colors = {}, [], [], {}, set()
        self.nav_depth = 0
        self.in_a = False
        self.buf = ""
        self.skip = 0

    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag in ("script", "style"):
            self.skip += 1
        if tag in LANDMARKS:
            self.landmarks[tag] = self.landmarks.get(tag, 0) + 1
        if tag == "nav":
            self.nav_depth += 1
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.outline.append(int(tag[1]))
        if tag == "a" and self.nav_depth:
            self.in_a, self.buf = True, ""
        for c in (a.get("class") or "").split():
            if GRID.fullmatch(c) or GRID.search(c):
                self.grid[c] = self.grid.get(c, 0) + 1
        self.colors.update(COLOR.findall(a.get("style") or ""))

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        if tag == "nav":
            self.nav_depth = max(0, self.nav_depth - 1)
        if tag == "a" and self.in_a:
            self.in_a = False
            s = " ".join(self.buf.split())
            if s and len(s) <= 40:
                self.nav.append(s)

    def handle_data(self, d):
        if self.in_a and not self.skip:
            self.buf += d


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 0
    url = argv[0]
    host = urlparse(url).hostname or "page"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (layout reader)"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            html = r.read().decode("utf-8", errors="replace")
    except (OSError, ValueError) as ex:  # URLError, timeouts, bad certificates: report, never skip verification
        print(f"lookalike: fetch failed for {url}: {ex}")
        return 1
    p = L()
    p.feed(html)
    out = {
        "url": url,
        "note": "structure only; no prose, images or brand assets",
        "landmarks": p.landmarks,
        "section_count": p.landmarks.get("section", 0),
        "heading_outline_levels": p.outline,
        "nav_items": list(dict.fromkeys(p.nav)),
        "grid_hints": dict(sorted(p.grid.items(), key=lambda kv: -kv[1])[:30]),
        "inline_color_tokens": sorted(p.colors),
    }
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"{host}.layout.json")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, indent=1)
    print(path)
    print(f"sections={out['section_count']} landmarks={p.landmarks} headings={len(p.outline)} nav={len(out['nav_items'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
