"""The Command theme (BOLO 171): one look for every page the launch opens.

theme.css holds the tokens (the Console's look). This module puts them into a page as one marked block:
    <!-- cmd-theme --> <link Plex Mono> <style id="cmd-theme"> theme.css + pages/<name>.css </style> <!-- /cmd-theme -->
The block goes after the page's last </style>, so it wins the cascade. Applying twice replaces the block,
so it is safe to run on a page that already has it.

Builders:   from theme import apply  ->  html = apply(html, "sitrep")      (never raises; returns html unchanged on error)
CLI:        python _tools/brand/theme.py apply-all [--json]                  every hand-made page and current output
            python _tools/brand/theme.py apply <name|path> [--page NAME] [--json]
            python _tools/brand/theme.py check [--json]                      which pages carry the current block
"""
import io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
CSS_FILE = os.path.join(HERE, "theme.css")
PAGE_DIR = os.path.join(HERE, "pages")
FONT = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap">'
START, END = "<!-- cmd-theme -->", "<!-- /cmd-theme -->"
BLOCK_RE = re.compile(re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)

# every page the launch opens that the theme reaches: name -> file. Built pages are listed too, so
# apply-all refreshes their current output; their builders call apply() on every build.
PAGES = {
    "judy-console": os.path.join(ROOT, "_tools", "dictation", "console.html"),        # :8787/  (read per request)
    "faces": os.path.join(ROOT, "_tools", "dictation", "faces.html"),                 # :8787/faces (read per request)
    "stash-deck": os.path.join(ROOT, "_PRIVATE", "stash_deck", "index.html"),
    "darkroom": r"Q:\fun\.2026picstach8252026\DARKROOM.html",                         # :8484/ (static, read per request)
    "fabula-graph": os.path.join(ROOT, "_PRIVATE", "intake-repos", "d3__d3", "fabula-graph.html"),
    "stash-erd": os.path.join(ROOT, "_PRIVATE", "reference", "erd", "stash-erd.html"),
    "zotero-erd": os.path.join(ROOT, "_PRIVATE", "reference", "erd", "zotero-erd.html"),
    # built: the builder applies the theme; these entries refresh the current output in place
    "sitrep": os.path.join(ROOT, "SITREP.html"),                                      # _tools/sitrep/build.py
    "desk": os.path.join(ROOT, "_PRIVATE", "reference", "desk", "command-desk.html"), # _tools/desk/build_desk.py
    "pullqueue": os.path.join(ROOT, "_PRIVATE", "reference", "pullqueue", "pull-queue.html"),  # pull_glass.py
    "roster": os.path.join(ROOT, "_tools", "roster", "roster.html"),                  # _tools/roster/build.py
    "armory": os.path.join(ROOT, "_PRIVATE", "reference", "armory", "armory.html"),   # _tools/armory/armory.py
    "europatch": os.path.join(ROOT, "_tools", "europatch", "patchbay.html"),          # europatch.py build (BOLO 173)
}
# served from a .py string, so apply() runs at import: traffic (_tools/dictation/traffic.py, :8787/traffic)


def block(page=None):
    css = io.open(CSS_FILE, encoding="utf-8").read()
    if page:
        extra = os.path.join(PAGE_DIR, page + ".css")
        if os.path.exists(extra):
            css += "\n/* page: %s */\n" % page + io.open(extra, encoding="utf-8").read()
    return START + "\n" + FONT + '\n<style id="cmd-theme">\n' + css.strip() + "\n</style>\n" + END + "\n"


def apply(html, page=None):
    """Return html with the theme block in place (after the last </style>). Never raises."""
    try:
        b = block(page)
        html = BLOCK_RE.sub("", html)
        i = html.rfind("</style>")
        if i >= 0:
            i += len("</style>")
            return html[:i] + "\n" + b + html[i:].lstrip("\n")
        j = html.find("</head>")
        if j >= 0:
            return html[:j] + b + html[j:]
        return b + html
    except Exception:
        return html


def apply_file(path, page=None):
    s = io.open(path, encoding="utf-8").read()
    out = apply(s, page)
    if out != s:
        with io.open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(out)
    return {"page": page, "path": path, "changed": out != s}


def check():
    rows = []
    for name, path in PAGES.items():
        if not os.path.exists(path):
            rows.append({"page": name, "path": path, "state": "missing"}); continue
        s = io.open(path, encoding="utf-8").read()
        m = BLOCK_RE.search(s)
        rows.append({"page": name, "path": path,
                     "state": "current" if m and m.group(0).rstrip("\n") == block(name).rstrip("\n") else ("stale" if m else "none")})
    return rows


def main(argv):
    js = "--json" in argv
    argv = [a for a in argv if a != "--json"]
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    verb = argv[0]
    if verb == "apply-all":
        rows = [apply_file(p, n) if os.path.exists(p) else {"page": n, "path": p, "changed": False, "missing": True}
                for n, p in PAGES.items()]
    elif verb == "apply" and len(argv) >= 2:
        page = argv[argv.index("--page") + 1] if "--page" in argv else None
        target = argv[1]
        if target in PAGES:
            page, target = page or target, PAGES[target]
        rows = [apply_file(target, page)]
    elif verb == "check":
        rows = check()
    else:
        print(__doc__); return 2
    if js:
        print(json.dumps(rows, indent=1))
    else:
        for r in rows:
            print("%-13s %-8s %s" % (r["page"], r.get("state") or ("missing" if r.get("missing") else ("applied" if r["changed"] else "same")), r["path"]))
    return 1 if any(r.get("state") in ("missing", "none", "stale") or r.get("missing") for r in rows) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
