"""The Subreddit Sheet: a keep-or-cut ballot (BOLO 99 side task, 10/4).
Reads _CANON_NODES/subreddit-list.md (the women register) + _tools/subsheet/extra.json,
writes _tools/subsheet/out/subreddit-sheet.html. Votes live in the artifact's db:
collection `keep`, one doc per sub (id = sub name), body {keep: bool, section}."""
import re, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
md = open(os.path.join(ROOT, "_CANON_NODES", "subreddit-list.md"), encoding="utf-8").read()
LINK = r"\[(r/[^\]]+)\]\((https://www\.reddit\.com/r/[^)]+)\)"
sections = []
for s in re.split(r"^## ", md, flags=re.M)[1:]:
    title, body = s.split("\n", 1)
    rows = []
    for line in body.split("\n"):
        if not line.startswith("| ") or line.startswith("| Person") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        note = " · ".join(re.sub(r"[*]", "", c) for c in cells[1:] if "reddit.com" not in c and c and c != "—")
        for n, u in re.findall(LINK, line):
            rows.append({"p": cells[0], "note": note, "sub": n[2:], "u": u})
    if not rows:
        rows = [{"p": n, "note": "multi-person hub", "sub": n[2:], "u": u} for n, u in re.findall(LINK, body)]
    sections.append({"t": "Women · " + title.strip(), "rows": rows})
for g in json.load(open(os.path.join(ROOT, "_tools", "subsheet", "extra.json"), encoding="utf-8")):
    sections.append({"t": g["t"], "rows": [{"p": p, "note": " · ".join(x for x in (note, m + " members") if x), "sub": sub,
                     "u": f"https://www.reddit.com/r/{sub}/"} for p, note, sub, m in g["rows"]]})
seen = set()
for g in sections:
    g["rows"] = [r for r in g["rows"] if not (r["sub"].lower() in seen or seen.add(r["sub"].lower()))]
tpl = open(os.path.join(ROOT, "_tools", "subsheet", "template.html"), encoding="utf-8").read()
out = os.path.join(ROOT, "_tools", "subsheet", "out")
os.makedirs(out, exist_ok=True)
open(os.path.join(out, "subreddit-sheet.html"), "w", encoding="utf-8").write(tpl.replace("__DATA__", json.dumps(sections, ensure_ascii=False)))
print(len(sections), "sections ·", sum(len(g["rows"]) for g in sections), "subs")
