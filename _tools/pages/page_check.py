#!/usr/bin/env python3
"""page_check.py - zero-token static page check: glass_lint plus design-review phases.

Usage:
    python _tools/pages/page_check.py <file.html> [...]

Prints `phase | check | result` per check, then a summary. Exit 1 on any FAIL.
Phases (static only, no browser): first-paint content present, every control
labelled, focus styles, headings in order, no empty links, reduced-motion respected.
Idea from the design-review phases in OneRedOak/claude-code-workflows (MIT,
Patrick Ellis); checks and code are ours.
"""
import os
import re
import sys
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import glass_lint  # noqa: E402

# importing glass_lint already switches stdout to UTF-8


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.heads, self.ctrls, self.links = [], [], [], []
        self.text_in_body = 0
        self.skip = 0
        self.labels_for = set()
        self.in_label = 0

    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "label":
            self.in_label += 1
            if a.get("for"):
                self.labels_for.add(a["for"])
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.heads.append(int(tag[1]))
        if tag in ("button", "input", "select", "textarea", "a"):
            self.stack.append({"tag": tag, "a": a, "text": "", "inlabel": bool(self.in_label)})
        if tag == "img" and self.stack:
            self.stack[-1]["text"] += (a.get("alt") or "")
        if tag == "svg" and self.stack:
            self.stack[-1]["text"] += (a.get("aria-label") or "")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        if tag == "label":
            self.in_label = max(0, self.in_label - 1)
        if self.stack and self.stack[-1]["tag"] == tag:
            n = self.stack.pop()
            (self.links if tag == "a" else self.ctrls).append(n)

    def handle_data(self, d):
        if self.skip:
            return
        s = d.strip()
        self.text_in_body += len(s)
        if self.stack:
            self.stack[-1]["text"] += s


def check(path):
    html = open(path, encoding="utf-8", errors="replace").read()
    R = []
    p = P()
    p.feed(html)
    bare = re.sub(r"<(script|style)\b.*?</\1>", "", html, flags=re.S | re.I)
    # phase 1: first paint
    n = p.text_in_body
    R.append(("first-paint", "text in static markup", ("PASS" if n > 200 else "FAIL") + f" ({n} chars)"))
    # phase 2: labels
    bad = []
    for c in p.ctrls:
        a = c["a"]
        if c["tag"] == "input" and a.get("type") in ("hidden", "submit", "button"):
            if a.get("type") == "hidden" or a.get("value"):
                continue
        ok = c["text"].strip() or a.get("aria-label") or a.get("aria-labelledby") or a.get("title") or c["inlabel"] or a.get("id") in p.labels_for
        if not ok:
            bad.append(c["tag"] + (f"#{a['id']}" if a.get("id") else ""))
    R.append(("controls", "every control has a label", "PASS" if not bad else f"FAIL ({len(bad)}: {', '.join(bad[:5])})"))
    # phase 3: focus styles
    css = " ".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S | re.I))
    foc = bool(re.search(r":focus(-visible)?\b", css))
    kills = re.findall(r":focus[^{]*\{[^}]*outline\s*:\s*(?:none|0)", css)
    if not foc and not kills:
        r = "WARN (no :focus rule, browser default applies)"
    elif kills and not re.search(r":focus(-visible)?[^{]*\{[^}]*(outline|box-shadow|border)\s*:\s*(?!none|0\b)", css):
        r = "FAIL (outline removed, no replacement)"
    else:
        r = "PASS"
    R.append(("focus", "focus styles", r))
    # phase 4: headings
    hs, issues = p.heads, []
    if hs.count(1) != 1:
        issues.append(f"{hs.count(1)} h1")
    for a, b in zip(hs, hs[1:]):
        if b > a + 1:
            issues.append(f"h{a}->h{b}")
    R.append(("headings", "one h1, no skipped levels", "PASS" if not issues else "FAIL (" + ", ".join(issues[:4]) + ")"))
    # phase 5: links
    empty = [l for l in p.links if not (l["text"].strip() or l["a"].get("aria-label") or l["a"].get("title"))]
    R.append(("links", "no empty links", "PASS" if not empty else f"FAIL ({len(empty)})"))
    # phase 6: reduced motion
    anim = bool(re.search(r"\b(animation|transition)\s*:", css))
    rm = "prefers-reduced-motion" in css
    R.append(("motion", "reduced-motion respected", "PASS" if (rm or not anim) else "FAIL (motion CSS, no prefers-reduced-motion)"))
    # glass_lint
    gl = glass_lint.lint(path, html)
    e = sum(1 for x in gl if x[0] == "ERROR")
    w = sum(1 for x in gl if x[0] == "WARN")
    R.append(("glass_lint", "page rules", ("PASS" if not e else "FAIL") + f" ({e} error, {w} warn)"))
    return R


def main(argv):
    if not argv:
        print(__doc__)
        return 0
    fails = 0
    for path in argv:
        print(f"# {path}")
        try:
            rows = check(path)
        except OSError as ex:
            print(f"load | {path} | FAIL ({ex})")
            fails += 1
            continue
        for ph, ck, r in rows:
            print(f"{ph} | {ck} | {r}")
            fails += r.startswith("FAIL")
    print(f"page_check: {len(argv)} file(s), {fails} fail(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
