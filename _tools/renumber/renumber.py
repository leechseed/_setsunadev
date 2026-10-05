"""BOLO 103 · the system renumber + BOLO LEECHSEED rename (ruled 10/5, "All recs go").

Usage:  python _tools/renumber/renumber.py          (dry run: counts per file)
        python _tools/renumber/renumber.py --apply

Moves: 05 Operations → 09 · 06 Style → 07 · 07 Theme → 06 · 08 Tracking stays · 09 Worldbuilding → 05.
Rewrites, in the live tree only (never _LOG, _ARCHIVE, journals, cache notes, work/ or out/ dirs):
  folder names  0N_<NAME>           ssot_ file stems  ssot_0N_<name>     section refs  06.x → 07.x
  and the LEECHSEED rename (character side only; the setting slice keeps its name).
Then renames the folders and files on disk (SSOT + _DOCS), through temp names so no two collide.
"""
import io, os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
APPLY = "--apply" in sys.argv

FOLDER = {"05_OPERATIONS": "09_OPERATIONS", "06_STYLE_GUIDES": "07_STYLE_GUIDES",
          "07_THEME_SYSTEMS": "06_THEME_SYSTEMS", "09_WORLDBUILDING_SYSTEMS": "05_WORLDBUILDING_SYSTEMS"}
STEM = [(r"ssot_05_operations", "ssot_09_operations"), (r"ssot_06_(?=\d)", "ssot_07_"),
        (r"ssot_07_theme", "ssot_06_theme"), (r"ssot_09_worldbuilding", "ssot_05_worldbuilding")]
LEECH = [(r"12-Layer Character Database", "LEECHSEED Character System"),
         (r"12-layer character database", "LEECHSEED character system"),
         (r"12-Layer Character System", "LEECHSEED Character System"),
         (r"12-layer character system", "LEECHSEED character system"),
         (r"12-Layer Vertical Slice", "LEECHSEED Vertical Slice"),
         (r"12-layer vertical slice", "LEECHSEED vertical slice"),
         (r"12-Layer Feed Map", "LEECHSEED Feed Map"),
         (r"12-layer character record", "LEECHSEED character record")]

LIVE = ["ShroomsQ", "_tools", "_CANON_NODES", ".claude/skills", "SOP.md", "STATE.md", "BOLO.md",
        "PROJECTS.md", "CLAUDE.md", "README.md"]
SKIP = re.compile(r"(^|/)(_LOG|_ARCHIVE|_history|work|out|boards|node_modules|\.venv)(/|$)|\.session\.md$|"
                  r"(^|/)_tools/renumber/")
TEXT = re.compile(r"\.(md|py|json|html|js|jsx|txt|yaml|yml|css|cmd|ps1|sh)$", re.I)


def rewrite(t):
    n = 0
    def fold(m):
        return FOLDER[m.group(0)]
    t, k = re.subn(r"\b(05_OPERATIONS|06_STYLE_GUIDES|07_THEME_SYSTEMS|09_WORLDBUILDING_SYSTEMS)\b", fold, t); n += k
    # stems: one pass with a combined pattern so 06→07 and 07→06 never chain
    pat = re.compile("|".join(f"(?P<s{i}>{p})" for i, (p, _) in enumerate(STEM)))
    t, k = pat.subn(lambda m: STEM[int(m.lastgroup[1:])][1], t); n += k
    t, k = re.subn(r"(?<![\d.])06\.(2a|2b|1|2|3)(?![\d])", r"07.\1", t); n += k
    for a, b in LEECH:
        t, k = re.subn(a, b, t); n += k
    return t, n


def files():
    out = subprocess.run(["git", "ls-files", "-z", "--"] + LIVE, cwd=ROOT, capture_output=True).stdout
    for rel in out.decode("utf-8", "replace").split("\0"):
        if rel and TEXT.search(rel) and not SKIP.search(rel):
            yield rel


def main():
    total, touched = 0, 0
    for rel in files():
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        t = io.open(p, encoding="utf-8", errors="surrogateescape").read()
        new, n = rewrite(t)
        if n:
            touched += 1; total += n
            if not APPLY:
                print(f"{n:4d}  {rel}")
            else:
                io.open(p, "w", encoding="utf-8", errors="surrogateescape", newline="").write(new)
    print(f"{'APPLIED' if APPLY else 'DRY RUN'} · {touched} files · {total} rewrites")
    if not APPLY:
        return
    # renames on disk: files first (inside their old folders), then folders, via temp names
    moves = []
    for base in ("ShroomsQ/_CANON/_SSOT", "ShroomsQ/_CANON/_DOCS"):
        for old in FOLDER:
            d = os.path.join(ROOT, base, old)
            if not os.path.isdir(d):
                continue
            for dp, dns, fns in os.walk(d, topdown=False):
                for name in fns + dns:
                    nn, _ = rewrite(name)
                    if nn != name:
                        moves.append((os.path.join(dp, name), os.path.join(dp, nn)))
    for a, b in moves:
        os.rename(a, b)
    tmp = []
    for base in ("ShroomsQ/_CANON/_SSOT", "ShroomsQ/_CANON/_DOCS"):
        for old, new in FOLDER.items():
            a = os.path.join(ROOT, base, old)
            if os.path.isdir(a):
                os.rename(a, a + ".__mv"); tmp.append((a + ".__mv", os.path.join(ROOT, base, new)))
    for a, b in tmp:
        os.rename(a, b)
    print(f"renamed {len(moves)} files/dirs · {len(tmp)} system folders")


if __name__ == "__main__":
    main()
