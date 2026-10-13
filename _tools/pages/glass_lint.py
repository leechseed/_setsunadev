#!/usr/bin/env python3
"""glass_lint.py - check built pages against the Command's page rules.

Usage:
    python _tools/pages/glass_lint.py <file.html> [...]

One line per finding: file · rule · detail (prefixed ERROR or WARN), then a
summary. Exit 1 if any ERROR. Rules (ruled 9/10-10/12): DARK only, the orange
palette, thin chrome (one ~44px header strip), the hover layer (.t/.tip) on
dense pages, Google Fonts as the only external stylesheets, scripts only from
allowed CDNs, a 2-4 word <title>, a viewport meta, no script-injected mermaid;
plus AI-generic design tells from the taste-skill redesign audit.
"""
import io
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ALLOWED_SCRIPT = ("cdnjs.cloudflare.com", "cdn.jsdelivr.net", "unpkg.com", "cdn.tailwindcss.com", "code.jquery.com")
ACCENTS_OK = {"ff5a1f", "e04e18", "ff6b35", "a83409", "ff8f62", "ffb08f", "ff7a45", "c2410c"}
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-⛿✀-➿]")
GENERIC_COPY = re.compile(r"\b(welcome to|elevate your|seamless(?:ly)?|unleash|next-gen|game-?changer|"
                          r"in the world of|john doe|jane smith|acme corp|lorem ipsum)\b", re.I)


def hexrgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def sat_hue(h):
    r, g, b = [x / 255 for x in hexrgb(h)]
    mx, mn = max(r, g, b), min(r, g, b)
    if mx == mn:
        return 0.0, 0.0, mx
    d = mx - mn
    s = d / (1 - abs(mx + mn - 1)) if 0 < mx + mn < 2 else 0
    if mx == r:
        hue = 60 * (((g - b) / d) % 6)
    elif mx == g:
        hue = 60 * ((b - r) / d + 2)
    else:
        hue = 60 * ((r - g) / d + 4)
    return s, hue, (mx + mn) / 2


def lum(h):
    r, g, b = hexrgb(h)
    return (0.299 * r + 0.587 * g + 0.114 * b) / 255


def lint(name, html):
    f = []  # (level, rule, detail)
    E = lambda r, d: f.append(("ERROR", r, d))
    W = lambda r, d: f.append(("WARN", r, d))
    style = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S | re.I))
    css = re.sub(r"/\*.*?\*/", "", style, flags=re.S)
    body_text = re.sub(r"<(script|style)\b.*?</\1>", " ", html, flags=re.S | re.I)
    body_text = re.sub(r"<[^>]+>", " ", body_text)

    # --- DARK only ---
    rootm = re.search(r":root\s*\{([^}]*)\}", css)
    if rootm:
        rb = rootm.group(1)
        if re.search(r"color-scheme\s*:\s*light(?!\s+dark)", rb):
            # tolerated only if a later bare :root block sets dark (SITREP pattern)
            later = re.findall(r":root\s*\{([^}]*)\}", css)
            if not any(re.search(r"color-scheme\s*:\s*dark", b) for b in later[1:]):
                E("dark-only", "color-scheme:light is the page scheme")
        bg = re.search(r"--bg\s*:\s*(#[0-9a-fA-F]{3,6})\b", rb)
        if bg and lum(bg.group(1)) > 0.45:
            blocks = re.findall(r":root\s*\{([^}]*)\}", css)
            last_bg = [re.search(r"--bg\s*:\s*(#[0-9a-fA-F]{3,6})\b", b) for b in blocks]
            last_bg = [m.group(1) for m in last_bg if m]
            if last_bg and lum(last_bg[-1]) > 0.45:
                E("dark-only", f"light --bg {last_bg[-1]}")
    if not re.search(r"color-scheme\s*:\s*dark", css):
        W("dark-only", "no color-scheme:dark declared")
    for m in re.finditer(r"background(?:-color)?\s*:\s*(#fff(?:fff)?|white)\b", css, re.I):
        E("dark-only", f"white background ({m.group(0)})")
    if re.search(r"theme-?toggle|id=[\"']theme|data-theme\s*=\s*[\"']light|prefers-color-scheme\s*:\s*light|class=[\"'][^\"']*\btoggle-theme", html, re.I):
        E("dark-only", "theme toggle / light-theme hook present")

    # --- palette ---
    accs = re.findall(r"--accent(?:-ink|-soft)?\s*:\s*(#[0-9a-fA-F]{3,6})", css)
    main_acc = re.findall(r"--accent\s*:\s*(#[0-9a-fA-F]{3,6})", css)
    for a in main_acc:
        if a.lstrip("#").lower() not in ACCENTS_OK and not any(
                a.lstrip("#").lower() == x for x in ACCENTS_OK):
            s, hue, l = sat_hue(a)
            if not (8 <= hue <= 28 and s > 0.6):
                E("palette", f"--accent {a} is not the orange (#FF5A1F / #E04E18 family)")
    if not main_acc and not re.search(r"ff5a1f|e04e18|ff6b35", css, re.I):
        W("palette", "no orange accent token found")
    stray = set()
    for h in re.findall(r"#([0-9a-fA-F]{6})\b", css):
        s, hue, l = sat_hue(h)
        if s > 0.8 and 0.25 < l < 0.75 and not (5 <= hue <= 40) and not (95 <= hue <= 160):
            stray.add("#" + h.upper())
    if stray:
        W("palette", "stray saturated colors: " + ", ".join(sorted(stray)[:6]))

    # --- thin chrome ---
    headers = re.findall(r"<header\b", html, re.I)
    if len(headers) > 1:
        W("chrome", f"{len(headers)} <header> elements; one strip only")
    for m in re.finditer(r"(?:header|\.strip|\.head|\.masthead)[^{]*\{([^}]*)\}", css, re.I):
        hm = re.search(r"(?<!min-)(?<!max-)height\s*:\s*(\d+)px", m.group(1))
        if hm and int(hm.group(1)) > 72:
            E("chrome", f"header fixed height {hm.group(1)}px (limit ~72, aim 44)")

    # --- hover layer ---
    if len(body_text.split()) * 6 > 8192 and not re.search(r'class=["\'][^"\']*\b(t|tip)\b', html):
        W("hover-layer", f"page has ~{len(body_text)//1024} KB of text and no .t/.tip hover terms")

    # --- externals ---
    for m in re.finditer(r"<link\b[^>]*>", html, re.I):
        tag = m.group(0)
        if re.search(r"rel=[\"']?stylesheet", tag, re.I):
            h = re.search(r"href=[\"']?(https?:)?//([^/\"' >]+)", tag, re.I)
            if h and h.group(2) not in ("fonts.googleapis.com", "fonts.gstatic.com"):
                E("externals", f"external stylesheet from {h.group(2)} (Google Fonts only)")
    for m in re.finditer(r"<script\b[^>]*\bsrc=[\"']?(?:https?:)?//([^/\"' >]+)", html, re.I):
        if m.group(1) not in ALLOWED_SCRIPT:
            E("externals", f"script from {m.group(1)} not on the allowed CDN list")

    # --- title / viewport / mermaid ---
    t = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    if not t:
        E("title", "no <title>")
    else:
        n = len(t.group(1).split())
        if not 2 <= n <= 4 and t.group(1).strip().lower() not in ("sitrep",):
            W("title", f"title has {n} word(s): \"{t.group(1).strip()[:40]}\" (want 2-4)")
    if not re.search(r"<meta[^>]+name=[\"']viewport", html, re.I):
        E("viewport", "no viewport meta")
    scripts = "\n".join(re.findall(r"<script\b[^>]*>(.*?)</script>", html, re.S | re.I))
    if re.search(r"class=[\"']?mermaid|pre\.mermaid|mermaid", scripts) and re.search(
            r"innerHTML|createElement|insertAdjacent|appendChild", scripts) and re.search(r"mermaid", scripts):
        if re.search(r"(createElement\([\"']pre[\"']\)|class(Name)?\s*=\s*[\"']mermaid|innerHTML[^;]*mermaid)", scripts):
            E("mermaid", "<pre class=\"mermaid\"> injected by script; write it static")

    # --- taste-skill redesign audit (static-catchable) ---
    for m in re.finditer(r"background-clip\s*:\s*text|-webkit-text-fill-color\s*:\s*transparent", css):
        if re.search(r"gradient", css[max(0, m.start() - 200):m.end() + 200]):
            W("ai-generic", "gradient-text heading (background-clip:text)")
            break
    for m in re.finditer(r"gradient\([^;]*", css):
        hexes = [h for h in re.findall(r"#([0-9a-fA-F]{6})\b", m.group(0))]
        if any(210 <= sat_hue(h)[1] <= 300 and sat_hue(h)[0] > 0.35 for h in hexes):
            W("ai-generic", "purple/blue gradient (the AI default look)")
            break
    if re.search(r"#000(?:000)?\b(?=\s*[;}])", re.sub(r"(box-shadow|text-shadow|color)\s*:[^;}]*", "", css)) and \
            re.search(r"background(?:-color)?\s*:\s*#000(?:000)?\s*[;}]|--bg\s*:\s*#000(?:000)?\s*[;}]", css):
        W("ai-generic", "pure #000 background; use off-black")
    if re.search(r"<li[^>]*>\s*(?:[✅❌✨\U0001F680\U0001F4A1\U0001F525⚡⭐])", html):
        W("ai-generic", "emoji bullets in list items")
    gc = GENERIC_COPY.search(body_text)
    if gc:
        W("ai-generic", f"stock hero/copy cliche: \"{gc.group(0)}\"")
    if re.search(r"z-index\s*:\s*\d{4,}", css):
        W("ai-generic", "arbitrary z-index (1000+)")
    if re.search(r"href=[\"']#[\"']", html):
        W("ai-generic", "dead href=\"#\" links")
    if re.search(r"box-shadow\s*:[^;]*rgba\(\s*0\s*,\s*0\s*,\s*0\s*,\s*\.?0?[5-9]", css) and False:
        pass
    if len(re.findall(r"font-family\s*:\s*[\"']?Inter\b", css)) and not re.search(r"--display|Barlow", css):
        W("ai-generic", "Inter-everywhere typography")
    return f


def main(argv):
    if not argv:
        print(__doc__)
        return 0
    errs = warns = 0
    for p in argv:
        try:
            with open(p, encoding="utf-8", errors="replace") as fh:
                html = fh.read()
        except OSError as e:
            print(f"{p} · ERROR · {e}")
            errs += 1
            continue
        for lvl, rule, detail in lint(p, html):
            print(f"{p} · {rule} · {lvl}: {detail}")
            errs += lvl == "ERROR"
            warns += lvl == "WARN"
    print(f"glass_lint: {len(argv)} file(s), {errs} error(s), {warns} warning(s)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# adapted from Leonxlnx/taste-skill (MIT) + conorbronsdon/avoid-ai-writing (MIT) · BOLO 140 · 2026-10-12
