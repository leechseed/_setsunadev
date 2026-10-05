"""BOLO 103 follow-up: old system numbers left in prose (a number paired with its OLD system's name).
Usage: python _tools/renumber/prose.py [--apply]"""
import io, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OLD = {"05": ("Operations", "09"), "06": ("Style", "07"), "07": ("Theme", "06"), "09": ("Worldbuilding", "05")}
pats = []
for old, (name, new) in OLD.items():
    n = name
    pats.append((re.compile(rf"\b{old}(\s*(?:·\s*)?)({n}|{n.upper()})\b"), rf"{new}\1\2"))          # 07 Theme · 09 WORLDBUILDING
    pats.append((re.compile(rf"\b({n}|{n.upper()})(\s*)\({old}\)"), rf"\1\2({new})"))                  # Theme (07)
pats.append((re.compile(r"ssot_06_style_guides"), "ssot_07_style_guides"))
APPLY = "--apply" in sys.argv
tot = 0
for base in ("ShroomsQ/_CANON/_SSOT", "ShroomsQ/_CANON/_DOCS", "_tools/docs/landing.md"):
    b = os.path.join(ROOT, base)
    files = [b] if os.path.isfile(b) else [os.path.join(dp, f) for dp, _, fs in os.walk(b) for f in fs if f.endswith(".md")]
    for p in files:
        if "_history" in p or "_decisions" in p:
            continue
        t = io.open(p, encoding="utf-8", errors="surrogateescape", newline="").read()
        n0 = t
        k = 0
        for rx, rp in pats:
            t, c = rx.subn(rp, t); k += c
        if k:
            tot += k
            print(f"{k:3d} {os.path.relpath(p, ROOT)}")
            if APPLY:
                io.open(p, "w", encoding="utf-8", errors="surrogateescape", newline="").write(t)
print(("APPLIED" if APPLY else "DRY"), tot)
