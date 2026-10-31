"""lookalike.py stage 1: the site-layout reader (BOLO 161, call 4, ruled 10/31 "take all recs").

One page in, its layout skeleton out. One fetch of the URL Chief names (urllib), or a local .html file.
No browser, no installs, no crawl: linked stylesheets are listed, never fetched.

It reports structure only:
  landmarks   header / nav / main / aside / footer / section / article (+ ARIA roles)
  headings    the h1-h6 tree (text cut to 80 chars)
  layout      grid / flex hints, grid templates, gaps, max-widths, media breakpoints
              (from <style> blocks and style="" attributes it can see in the HTML)
  tokens      CSS custom properties, colors, font families, font sizes, spacing values
  components  cards, lists, tables, forms, buttons, inputs, images, links, nav links

Usage:
  python -X utf8 _tools/lookalike/lookalike.py <url-or-file> [--json] [--out layout.json]
Exit codes: 0 ok · 1 fetch or read failed · 2 bad arguments.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

UA = "lookalike/1.0 (layout reader; one fetch, structure only; github.com/ggrimace)"
MAX_BYTES = 6 * 1024 * 1024
TIMEOUT = 25

LANDMARK_TAGS = ("header", "nav", "main", "aside", "footer", "section", "article")
ROLE_MAP = {
    "banner": "header", "navigation": "nav", "main": "main",
    "complementary": "aside", "contentinfo": "footer", "region": "section", "article": "article",
}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

# ---------------------------------------------------------------- fetch


def ssl_ctx():
    # the Windows store on this box carries an expired root ("certificate has expired" on big sites,
    # 10/31); certifi's bundle builds the right chain, as in _tools/bookmarks/dig.py. System store if absent.
    import ssl
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except (ImportError, OSError):
        return ssl.create_default_context()


def load(target: str) -> tuple[str, dict]:
    """Return (html, meta). Exactly one network request for a URL."""
    p = Path(target)
    if not re.match(r"^https?://", target, re.I):
        if not p.is_file():
            raise FileNotFoundError(f"not a URL and not a file: {target}")
        raw = p.read_bytes()[:MAX_BYTES]
        return decode(raw, None), {"source": "file", "path": str(p.resolve()), "status": None, "bytes": len(raw)}
    req = urllib.request.Request(target, headers={"User-Agent": UA, "Accept": "text/html,*/*;q=0.5"})
    with urllib.request.urlopen(req, timeout=TIMEOUT, context=ssl_ctx()) as r:
        raw = r.read(MAX_BYTES + 1)
        meta = {
            "source": "url", "final_url": r.geturl(), "status": r.status,
            "content_type": r.headers.get("Content-Type", ""), "bytes": min(len(raw), MAX_BYTES),
            "truncated": len(raw) > MAX_BYTES,
        }
        return decode(raw[:MAX_BYTES], r.headers.get_content_charset()), meta


def decode(raw: bytes, charset: str | None) -> str:
    if not charset:
        m = re.search(rb"<meta[^>]+charset=[\"']?([A-Za-z0-9_-]+)", raw[:4096], re.I)
        charset = m.group(1).decode("ascii", "ignore") if m else "utf-8"
    try:
        return raw.decode(charset, errors="replace")
    except LookupError:
        return raw.decode("utf-8", errors="replace")

# ---------------------------------------------------------------- parse


class Skeleton(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.landmarks: Counter = Counter()
        self.roles: Counter = Counter()
        self.headings: list[dict] = []
        self.tags: Counter = Counter()
        self.classes: Counter = Counter()
        self.styles: list[str] = []          # <style> block text
        self.style_attrs: list[str] = []     # style="" values
        self.linked_css: list[str] = []
        self.font_links: list[str] = []
        self.buttons = 0
        self.inputs: Counter = Counter()
        self.nav_links = 0
        self.title = ""
        self.viewport = ""
        self._in_style = False
        self._in_title = False
        self._skip = 0                       # inside script/noscript/template
        self._heading: dict | None = None
        self._nav_marks: list[int] = []      # stack depths where a nav / role=navigation opened
        self._stack: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        self.tags[tag] += 1
        if tag not in VOID:
            self._stack.append(tag)
        if tag in ("script", "noscript", "template"):
            self._skip += 1
        if tag == "style":
            self._in_style = True
        if tag == "title" and not self.title:   # the page title only; SVG <title> elements come later
            self._in_title = True
        if tag in LANDMARK_TAGS:
            self.landmarks[tag] += 1
        role = a.get("role", "").strip().lower()
        if role:
            self.roles[role] += 1
            if role == "button":
                self.buttons += 1
        if (tag == "nav" or role == "navigation") and tag not in VOID:
            self._nav_marks.append(len(self._stack))
        for c in a.get("class", "").split():
            self.classes[c.lower()] += 1
        if a.get("style"):
            self.style_attrs.append(a["style"])
        if tag == "link":
            rel = a.get("rel", "").lower()
            href = a.get("href", "")
            if "stylesheet" in rel and href:
                self.linked_css.append(href)
            if "fonts.googleapis" in href or "fonts.gstatic" in href or "typekit" in href:
                self.font_links.append(href)
        if tag == "meta" and a.get("name", "").lower() == "viewport":
            self.viewport = a.get("content", "")
        if tag == "button":
            self.buttons += 1
        if tag == "input":
            t = a.get("type", "text").lower()
            self.inputs[t] += 1
            if t in ("submit", "button", "reset"):
                self.buttons += 1
        if tag == "a" and self._nav_marks:
            self.nav_links += 1
        if tag in ("a",) and re.search(r"\b(btn|button)\b", a.get("class", ""), re.I):
            self.buttons += 1
        if re.fullmatch(r"h[1-6]", tag):
            self._heading = {"level": int(tag[1]), "text": "", "id": a.get("id", "")}

    def handle_endtag(self, tag):
        if tag in ("script", "noscript", "template") and self._skip:
            self._skip -= 1
        if tag == "style":
            self._in_style = False
        if tag == "title":
            self._in_title = False
        if self._heading and tag == f"h{self._heading['level']}":
            h = self._heading
            h["text"] = re.sub(r"\s+", " ", h["text"]).strip()[:80]
            self.headings.append(h)
            self._heading = None
        if tag in self._stack:
            while self._stack and self._stack.pop() != tag:
                pass
        while self._nav_marks and len(self._stack) < self._nav_marks[-1]:
            self._nav_marks.pop()

    def handle_data(self, data):
        if self._in_style:
            self.styles.append(data)
            return
        if self._in_title:
            self.title += data
        if self._skip:
            return
        if self._heading is not None:
            self._heading["text"] += data

# ---------------------------------------------------------------- css


COLOR_RE = re.compile(r"#[0-9a-fA-F]{8}\b|#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3,4}\b|\b(?:rgba?|hsla?|oklch|oklab|lab|lch)\([^)]*\)")
DECL_RE = re.compile(r"([a-zA-Z-]+)\s*:\s*([^;{}]+)")
VAR_RE = re.compile(r"(--[\w-]+)\s*:\s*([^;{}]+)")
MEDIA_RE = re.compile(r"@media[^{]*?\((?:min|max)-width\s*:\s*([\d.]+(?:px|em|rem))", re.I)
SPACING_PROPS = {"margin", "padding", "gap", "row-gap", "column-gap", "margin-top", "margin-bottom",
                 "padding-top", "padding-bottom", "padding-left", "padding-right", "margin-left", "margin-right"}


def top(c: Counter, n: int) -> list[dict]:
    return [{"value": k, "count": v} for k, v in c.most_common(n)]


def strip_comments(css: str) -> str:
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)


def read_css(blocks: list[str], attrs: list[str]) -> tuple[dict, dict]:
    css = strip_comments("\n".join(blocks))
    body = re.sub(r"@[a-zA-Z-]+[^{;]*\{", "{", css)   # drop @media/@supports preludes so "(max-width: 720px)" is not a declaration
    decls = [(p.lower(), v.strip()) for p, v in DECL_RE.findall(body)]
    for s in attrs:
        decls += [(p.lower(), v.strip()) for p, v in DECL_RE.findall(s)]
    display, templates, gaps, maxw, flexdir = Counter(), Counter(), Counter(), Counter(), Counter()
    fonts, sizes, spacing, colors = Counter(), Counter(), Counter(), Counter()
    for p, v in decls:
        v1 = re.sub(r"\s*!important", "", v)
        if p == "display" and re.search(r"grid|flex", v1):
            display[v1] += 1
        elif p in ("grid-template-columns", "grid-template-areas", "grid-template-rows"):
            templates[f"{p}: {v1[:80]}"] += 1
        elif p == "flex-direction" or p == "flex-wrap":
            flexdir[f"{p}: {v1}"] += 1
        elif p == "max-width" and re.search(r"\d", v1):
            maxw[v1] += 1
        elif p == "font-family":
            fonts[re.sub(r"\s+", " ", v1)[:100]] += 1
        elif p == "font-size":
            sizes[v1] += 1
        if p in ("gap", "row-gap", "column-gap", "grid-gap"):
            gaps[v1] += 1
        if p in SPACING_PROPS:
            spacing[v1] += 1
        for c in COLOR_RE.findall(v1):
            colors[c.lower().replace(" ", "")] += 1
    props = Counter()
    color_tokens = {}
    for name, val in VAR_RE.findall(css + "\n" + "\n".join(attrs)):
        val = val.strip()
        props[name] += 1
        if name not in color_tokens and COLOR_RE.search(val):
            color_tokens[name] = val[:60]
    bps = Counter(MEDIA_RE.findall(css))
    layout = {
        "display": top(display, 10),
        "grid_templates": top(templates, 12),
        "flex": top(flexdir, 8),
        "gaps": top(gaps, 10),
        "max_widths": top(maxw, 8),
        "media_breakpoints": sorted(bps, key=lambda s: float(re.match(r"[\d.]+", s).group())),
    }
    tokens = {
        "custom_properties": len(props),
        "color_tokens": [{"name": k, "value": v} for k, v in list(color_tokens.items())[:40]],
        "colors": top(colors, 24),
        "fonts": top(fonts, 10),
        "font_sizes": top(sizes, 12),
        "spacing": top(spacing, 12),
    }
    return layout, tokens

# ---------------------------------------------------------------- report


def components(s: Skeleton) -> dict:
    card_classes = sum(v for k, v in s.classes.items() if re.search(r"(^|[-_])cards?($|[-_])", k))
    return {
        "cards": card_classes,
        "lists": {"ul": s.tags["ul"], "ol": s.tags["ol"], "dl": s.tags["dl"], "items": s.tags["li"]},
        "tables": s.tags["table"],
        "forms": s.tags["form"],
        "buttons": s.buttons,
        "inputs": dict(s.inputs.most_common()) | ({"textarea": s.tags["textarea"]} if s.tags["textarea"] else {})
                  | ({"select": s.tags["select"]} if s.tags["select"] else {}),
        "images": s.tags["img"] + s.tags["picture"] + s.tags["svg"],
        "figures": s.tags["figure"],
        "links": s.tags["a"],
        "nav_links": s.nav_links,
        "iframes": s.tags["iframe"],
        "details": s.tags["details"],
    }


def build(target: str) -> dict:
    html, meta = load(target)
    s = Skeleton()
    s.feed(html)
    s.close()
    layout, tokens = read_css(s.styles, s.style_attrs)
    landmarks = {t: s.landmarks[t] for t in LANDMARK_TAGS}
    roles = {r: s.roles[r] for r in ROLE_MAP if s.roles[r]}
    base = meta.get("final_url") or target
    linked = [urllib.parse.urljoin(base, h) if meta["source"] == "url" else h for h in s.linked_css]
    notes = []
    if linked:
        notes.append(f"{len(linked)} linked stylesheet(s) not fetched (one-fetch rule); layout and tokens cover inline CSS only.")
    if not s.styles and not s.style_attrs:
        notes.append("no inline CSS seen; layout hints and tokens are empty.")
    if meta.get("truncated"):
        notes.append(f"page cut at {MAX_BYTES} bytes.")
    return {
        "tool": "lookalike", "stage": 1,
        "target": target,
        "read_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "fetch": meta,
        "title": re.sub(r"\s+", " ", s.title).strip()[:120],
        "viewport": s.viewport,
        "landmarks": landmarks,
        "aria_roles": roles,
        "headings": s.headings[:200],
        "heading_counts": {f"h{i}": sum(1 for h in s.headings if h["level"] == i) for i in range(1, 7)},
        "layout": layout,
        "tokens": tokens,
        "components": components(s),
        "top_classes": top(s.classes, 25),
        "stylesheets": {
            "inline_blocks": len([b for b in s.styles if b.strip()]),
            "inline_style_attrs": len(s.style_attrs),
            "linked": linked,
            "font_links": s.font_links,
        },
        "notes": notes,
    }


def text_view(d: dict) -> str:
    out = []
    f = d["fetch"]
    out.append(f"lookalike · {d['target']}")
    out.append(f"  {f.get('source')} · status {f.get('status')} · {f.get('bytes')} bytes · title: {d['title']}")
    out.append("landmarks  " + "  ".join(f"{k} {v}" for k, v in d["landmarks"].items()))
    if d["aria_roles"]:
        out.append("aria roles " + "  ".join(f"{k} {v}" for k, v in d["aria_roles"].items()))
    out.append("headings   " + "  ".join(f"{k} {v}" for k, v in d["heading_counts"].items()))
    for h in d["headings"][:25]:
        out.append("  " + "  " * (h["level"] - 1) + f"h{h['level']} {h['text']}")
    if len(d["headings"]) > 25:
        out.append(f"  ... {len(d['headings']) - 25} more")
    L = d["layout"]
    out.append("layout     display: " + (", ".join(f"{x['value']}×{x['count']}" for x in L["display"]) or "none seen"))
    for x in L["grid_templates"][:6]:
        out.append(f"  {x['value']}  ×{x['count']}")
    if L["gaps"]:
        out.append("  gaps: " + ", ".join(x["value"] for x in L["gaps"][:6]))
    if L["max_widths"]:
        out.append("  max-widths: " + ", ".join(x["value"] for x in L["max_widths"][:6]))
    if L["media_breakpoints"]:
        out.append("  breakpoints: " + ", ".join(L["media_breakpoints"]))
    T = d["tokens"]
    out.append(f"tokens     {T['custom_properties']} custom properties · {len(T['color_tokens'])} color tokens")
    if T["colors"]:
        out.append("  colors: " + ", ".join(x["value"] for x in T["colors"][:12]))
    for x in T["fonts"][:4]:
        out.append(f"  font: {x['value']}")
    C = d["components"]
    out.append(f"components cards {C['cards']} · lists ul {C['lists']['ul']} ol {C['lists']['ol']} ({C['lists']['items']} items)"
               f" · tables {C['tables']} · forms {C['forms']} · buttons {C['buttons']} · images {C['images']}"
               f" · links {C['links']} (nav {C['nav_links']})")
    S = d["stylesheets"]
    out.append(f"css        {S['inline_blocks']} <style> · {S['inline_style_attrs']} style= · {len(S['linked'])} linked (not fetched)")
    for n in d["notes"]:
        out.append(f"note       {n}")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="lookalike", description="Read one page's layout skeleton (one fetch, structure only).")
    ap.add_argument("target", help="an http(s) URL or a local .html file")
    ap.add_argument("--json", action="store_true", help="print the layout as JSON")
    ap.add_argument("--print", action="store_true", help="print the text view once (the default)")
    ap.add_argument("--out", help="also write the JSON to this path (e.g. layout.json)")
    try:
        a = ap.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code else 0
    try:
        d = build(a.target)
    except (urllib.error.URLError, OSError, ValueError) as e:
        msg = {"tool": "lookalike", "target": a.target, "error": str(e)}
        print(json.dumps(msg) if a.json else f"lookalike: {e}", file=sys.stdout if a.json else sys.stderr)
        return 1
    js = json.dumps(d, ensure_ascii=False, indent=2)
    if a.out:
        Path(a.out).write_text(js, encoding="utf-8")
    print(js if a.json else text_view(d))
    return 0


if __name__ == "__main__":
    sys.exit(main())
