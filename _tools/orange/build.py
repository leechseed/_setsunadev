# -*- coding: utf-8 -*-
"""The ORANGE board (BOLO 98, ordered 10/4). Zero tokens: reads BOLO.md, keeps every row whose trunk names ORANGE,
groups the rows into lanes, writes ORANGE.html at the repo root and a fragment for the Artifact tool.
Usage:  python _tools/orange/build.py
A new ORANGE row lands in its lane by number (LANES below) or in "Unsorted" until it is placed."""
import html, io, json, os, re, sys, tempfile, datetime
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
e = lambda s: html.escape(str(s or ""), quote=True)

LANES = [  # (key, name, purpose, BOLO numbers)
 ("library", "The library", "The books behind the work: the sexuality shelf and its distills, read into the character system.", [88, 97]),
 ("video", "Video and curation", "Stash, the deck, the goon agent and the playlists: what gets watched, tagged and queued.", [27, 28, 74, 75, 76]),
 ("studio", "The studio launch", "Ultrasin as a studio: the Blender stills, the shoots, the creator cases, voice work.", [10, 11, 12, 24, 45, 57]),
 ("engine", "The taxonomy engine", "DARKROOM and the image corpus: hashing, tagging, physique and performer references.", [13, 14, 23, 42, 43, 44]),
 ("games", "Games", "Engines and the roguelite.", [85, 94]),
 ("ops", "The trunk itself", "This board, the standards campaign, and the cleanup that touches ORANGE: removal tickets and strip follow-ons.", [98, 8, 9, 16, 19, 21, 22, 50]),
]
STATE = [("✅", "done"), ("🟢", "live"), ("🟡", "open"), ("🔴", "hot"), ("⏸", "parked")]

def clean(s):
    s = re.sub(r"\[\[[^\]|]+\|([^\]]+)\]\]", r"\1", s); s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return re.sub(r"\*\*|`|<br>", "", s).strip()

rows = []
for line in io.open(os.path.join(ROOT, "BOLO.md"), encoding="utf-8"):
    m = re.match(r"\| (\d+) \| \*\*(.+?)\*\* \[([^\]]*)\]", line)
    if not m or "ORANGE" not in m.group(3).split(";")[0]: continue
    cells = line.rstrip().rstrip("|").split(" | ")
    status = clean(cells[-1]) if len(cells) >= 4 else ""
    latest = re.split(r" · (?=[🟢🟡🔴✅⏸⏳])", status)[0]
    st = next((k for sym, k in STATE if latest.startswith(sym)), "open")
    date = cells[-2].strip() if len(cells) >= 4 and re.match(r"\d{4}-\d\d-\d\d", cells[-2].strip()) else ""
    rows.append({"n": int(m.group(1)), "title": clean(m.group(2)), "trunk": m.group(3).split(";")[0].strip(), "state": st,
                 "latest": latest[:420], "opened": date})

placed = {n for _, _, _, ns in LANES for n in ns}
lanes = [(k, nm, pur, [r for r in rows if r["n"] in ns]) for k, nm, pur, ns in LANES]
extra = [r for r in rows if r["n"] not in placed]
if extra: lanes.append(("unsorted", "Unsorted", "New ORANGE rows land here until they get a lane.", extra))
order = {"hot": 0, "live": 1, "open": 2, "parked": 3, "done": 4}
for _, _, _, rs in lanes: rs.sort(key=lambda r: (order[r["state"]], -r["n"]))
from collections import Counter
cnt = Counter(r["state"] for r in rows)

def card(r):
    return ('<li class="row s-%s" id="b%d"><div class="hd"><span class="no">%d</span><b>%s</b><span class="chip">%s</span></div>'
            '<p class="st">%s</p><div class="ft"><span>%s</span><span>%s</span></div></li>') % (
        r["state"], r["n"], r["n"], e(r["title"]), r["state"], e(r["latest"]), e(r["trunk"]), e("opened " + r["opened"]) if r["opened"] else "")
lanes_html = "".join('<section class="lane" id="%s"><header><h2>%s <em>%d</em></h2><p>%s</p></header><ul>%s</ul></section>' % (
    k, e(nm), len(rs), e(pur), "".join(card(r) for r in rs)) for k, nm, pur, rs in lanes if rs)
nav = "".join('<a href="#%s">%s <em>%d</em></a>' % (k, e(nm), len(rs)) for k, nm, _, rs in lanes if rs)
tiles = "".join('<span class="t s-%s"><b>%d</b>%s</span>' % (k, cnt.get(k, 0), lbl) for k, lbl in (("hot", "hot"), ("live", "live"), ("open", "open"), ("parked", "parked"), ("done", "done")))
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
tpl = io.open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
frag = tpl.replace("{{LANES}}", lanes_html).replace("{{NAV}}", nav).replace("{{TILES}}", tiles).replace("{{N}}", str(len(rows))).replace("{{WHEN}}", now)
io.open(os.path.join(ROOT, "ORANGE.html"), "w", encoding="utf-8", newline="\n").write(frag)
fp = os.path.join(tempfile.gettempdir(), "ORANGE.fragment.html"); io.open(fp, "w", encoding="utf-8", newline="\n").write(frag)
print("ORANGE board ·", len(rows), "rows ·", dict(cnt), "·", len(extra), "unsorted"); print("fragment", fp)
