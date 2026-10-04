"""Library pass (BOLO 100 / BOLO 18 stage 2): which distills are tagged to a system that its docs never cite.
Reads every distill's `feeds:` layer tags (L1-L12 character, SETTING/S1-S12 setting, P plot, T texture, G genre)
and checks each id against the text of that system's SSOT folder. Writes _tools/bolostatus/work/100/LIBRARY-GAP.md."""
import glob, os, re, collections
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SSOT = os.path.join(ROOT, "ShroomsQ", "_CANON", "_SSOT")
SYS = {"character": ["02_CHARACTER_SYSTEMS"], "setting": ["03_SETTING_SYSTEMS"], "plot": ["04_PLOT_SYSTEMS"],
       "texture": ["01_NARRATIVE_FRAMEWORKS"], "genre": ["01_NARRATIVE_FRAMEWORKS"], "theme": ["07_THEME_SYSTEMS"]}
def sys_of(tag):
    if re.fullmatch(r"L(1[0-2]|[1-9])", tag): return "character"
    if tag.startswith("SETTING") or re.fullmatch(r"S\d{1,2}", tag): return "setting"
    if re.fullmatch(r"P\d{1,2}", tag): return "plot"
    if re.fullmatch(r"T\d{1,2}", tag): return "texture"
    if re.fullmatch(r"G\d{1,2}", tag): return "genre"
    return None
text = {k: " ".join(open(f, encoding="utf-8").read() for d in v for f in glob.glob(os.path.join(SSOT, d, "*.md"))) for k, v in SYS.items()}
gap = collections.defaultdict(list); stats = collections.Counter(); untagged = []
for f in sorted(glob.glob(os.path.join(ROOT, "_0.1_BVX_LEARN", "KNOWLEDGE_AREAS", "**", "*.md"), recursive=True)):
    if "_vocab" in f: continue
    m = re.search(r"([A-Z]{3}\.\d+)", os.path.basename(f))  # many distill names start with an emoji
    if not m: continue
    t = open(f, encoding="utf-8", errors="ignore").read()
    fm = t[4:t.find("\n---", 4)] if t.startswith("---") else ""
    title = (re.search(r'^title:\s*"?([^"\n]+)', fm, re.M) or [None, "?"])[1]
    systems = {s for s in (sys_of(x) for x in re.findall(r"layer:\s*(\S+)", fm)) if s}
    if not systems: untagged.append((m[1], title)); continue
    for s in systems:
        stats[(s, m[1] in text[s])] += 1
        if m[1] not in text[s]:
            lay = sorted({x for x in re.findall(r"layer:\s*(\S+)", fm) if sys_of(x) == s})
            gap[s].append((m[1], title[:70], " ".join(lay), os.path.relpath(f, ROOT).replace("\\", "/")))
out = ["# LIBRARY GAP · BOLO 100 library pass", "", "Distills tagged to a system (by `feeds: layer`) that the system's docs never cite. Built by `_tools/review/library_gap.py`.", ""]
for s in sorted({k[0] for k in stats}):
    out.append(f"- **{s}**: {stats[(s, True)]} cited · {stats[(s, False)]} uncited")
out.append(f"- **untagged** (no feeds layer): {len(untagged)}")
for s, rows in sorted(gap.items()):
    out += ["", f"## {s} · {len(rows)} uncited", "", "| id | title | layers | path |", "|---|---|---|---|"]
    out += [f"| {i} | {t} | {l} | {p} |" for i, t, l, p in rows]
out += ["", f"## untagged · {len(untagged)}", ""] + [f"- {i} · {t}" for i, t in untagged]
dst = os.path.join(ROOT, "_tools", "bolostatus", "work", "100", "LIBRARY-GAP.md")
open(dst, "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
for s in sorted({k[0] for k in stats}): print(s, "cited", stats[(s, True)], "uncited", stats[(s, False)])
print("untagged", len(untagged))
