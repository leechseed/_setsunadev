"""bearings/collect.py — THE BEARINGS (10/14): the three tables Chief ordered on one glass, as data.

Chief, 10/14: "glass the list of github repos i got … another table we will list all the skills that we have been using
for running bold venture … match those processes to the github repo … another table with already created SOP and how
many times its run etc performance data … once thats done we should have an idea what we have on our bearings."

Zero tokens. Reads:
  repos  _PRIVATE/intake-repos/<owner>__<repo>/note.md + picks.json (BOLO 140, the intake)
  kit    .claude/skills · .claude/agents · hooks · workflows (the Kit's own reader, _tools/kit/build.py)
  sops   SOP.md headings (§1 prowords and the numbered procedures)
  runs   every session transcript under ~/.claude/projects/<this repo>/ : Skill calls, Agent calls by type,
         proword hits in Chief's own messages; each with the date and the minutes until Chief's next message.
Writes _tools/bearings/data/{repos,kit,sops,runs}.json. The specialists add briefs.json and match.json beside them.
Usage: python _tools/bearings/collect.py
"""
import glob
import importlib.util
import io
import json
import os
import re
import statistics
import sys
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA = os.path.join(os.path.dirname(__file__), "data")
REPOS = os.path.join(ROOT, "_PRIVATE", "intake-repos")
TRANSCRIPTS = os.path.join(os.path.expanduser("~"), ".claude", "projects", "c--Users-U01-LEECHSEED-Desktop--setsunadev")


def load_kit_module():
    spec = importlib.util.spec_from_file_location("kitbuild", os.path.join(ROOT, "_tools", "kit", "build.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------- repos ----------
def first_para(note, head):
    m = re.search(rf"^##\s*\({head}\).*?\n(.*?)(?=^##|\Z)", note, re.S | re.M)
    body = (m.group(1) if m else "").strip()
    para = body.split("\n\n")[0] if body else ""
    return re.sub(r"\s+", " ", para.replace("**", "")).strip()


def repos():
    out = []
    for d in sorted(glob.glob(os.path.join(REPOS, "*__*"))):
        if not os.path.isdir(d):
            continue
        slug = os.path.basename(d).replace("__", "/", 1)
        note = open(os.path.join(d, "note.md"), encoding="utf-8", errors="replace").read() if os.path.exists(os.path.join(d, "note.md")) else ""
        try:
            picks = json.load(open(os.path.join(d, "picks.json"), encoding="utf-8"))
        except Exception:
            picks = []
        lines = note.split("\n")
        intro = next((l.strip() for l in lines[1:8] if l.strip() and not l.startswith("#")), "")
        lic = re.search(r"\b(MIT|Apache[- ]2\.0|BSD[\w-]*|GPL[\w.-]*|AGPL[\w.-]*|MPL[\w.-]*|CC[\w.-]*|no license|unlicensed)\b", note, re.I)
        out.append({
            "repo": slug, "url": f"https://github.com/{slug}",
            "what": first_para(note, "a") or intro,
            "intro": intro,
            "license": lic.group(1) if lic else "",
            "picks": [{k: p.get(k, "") for k in ("id", "kind", "plain", "rec", "replaces", "risk")} for p in picks if isinstance(p, dict)],
        })
    return out


# ---------- kit ----------
def kit(mod):
    items = []
    for p in sorted(glob.glob(os.path.join(ROOT, ".claude", "skills", "*", "SKILL.md"))):
        fm, t, src = mod.front(p)
        name = fm.get("name") or os.path.basename(os.path.dirname(p))
        items.append(dict(kind="skill", name=name, desc=mod.plain(fm.get("description", "")), repo=mod.repo_of(src),
                          model="", path=os.path.relpath(p, ROOT).replace("\\", "/")))
    for p in sorted(glob.glob(os.path.join(ROOT, ".claude", "agents", "*.md"))):
        if os.path.basename(p).lower() == "readme.md":
            continue
        fm, t, src = mod.front(p)
        name = fm.get("name") or os.path.splitext(os.path.basename(p))[0]
        items.append(dict(kind="agent", name=name, desc=mod.plain(fm.get("description", "")), repo=mod.repo_of(src),
                          model=fm.get("model", "inherits"), path=os.path.relpath(p, ROOT).replace("\\", "/")))
    try:
        hk = json.load(open(os.path.join(ROOT, ".claude", "settings.local.json"), encoding="utf-8")).get("hooks", {})
    except Exception:
        hk = {}
    for event, lst in hk.items():
        for h in lst:
            for c in h.get("hooks", []):
                found = re.findall(r"[\w.-]+\.(?:py|sh)", c.get("command", ""))
                script = os.path.basename(found[-1]) if found else c.get("command", "")
                items.append(dict(kind="hook", name=script, desc=mod.HOOKS.get(script, "A hook script."), repo="",
                                  model=f"fires on {event}", path=".claude/settings.local.json"))
    for p in sorted(glob.glob(os.path.join(ROOT, ".claude", "workflows", "*.js"))):
        t = open(p, encoding="utf-8", errors="replace").read()
        m = re.search(r"description:\s*'([^']*)'", t)
        items.append(dict(kind="workflow", name=os.path.splitext(os.path.basename(p))[0], desc=m.group(1) if m else "",
                          repo="", model="", path=os.path.relpath(p, ROOT).replace("\\", "/")))
    return items


# ---------- sops ----------
SKILL_OF = {"1.1": "sitrep", "1.3": "oscar-mike", "1.5": "rtb", "1.20": "launch", "1.22": "dope-sheet"}


def sops():
    t = open(os.path.join(ROOT, "SOP.md"), encoding="utf-8", errors="replace").read()
    out = []
    for m in re.finditer(r"^(#{2,3})\s*([\d.]+)\s*·\s*(.+)$", t, re.M):
        num, title = m.group(2).rstrip("."), m.group(3).strip()
        start = m.end()
        nxt = re.search(r"^#{2,3}\s", t[start:], re.M)
        body = t[start:start + (nxt.start() if nxt else len(t) - start)].strip()
        summary = re.sub(r"\s+", " ", re.sub(r"[*`>|_]", "", body.split("\n\n")[0]))[:400] if body else ""
        says = [s for s in re.findall(r'"([^"]{2,40})"', title)]
        out.append({"n": num, "title": title, "level": len(m.group(1)), "summary": summary,
                    "says": says, "skill": SKILL_OF.get(num, ""), "retired": "retired" in title.lower()})
    return out


# ---------- runs ----------
def runs(sop_rows, kit_items):
    skills = {i["name"] for i in kit_items if i["kind"] == "skill"}
    rx = {}
    for s in sop_rows:
        pats = [re.escape(x.lower()) for x in s["says"] if len(x) > 3]
        if pats:
            rx[s["n"]] = re.compile(r"(?<!\w)(" + "|".join(pats) + r")(?!\w)")
    ev = defaultdict(list)            # key -> [(datetime, session)]
    user_times = defaultdict(list)    # session -> sorted times of Chief's real messages
    files = glob.glob(os.path.join(TRANSCRIPTS, "*.jsonl"))
    for fp in files:
        sess = os.path.splitext(os.path.basename(fp))[0]
        with io.open(fp, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if '"timestamp"' not in line:
                    continue
                try:
                    o = json.loads(line)
                except Exception:
                    continue
                ts = o.get("timestamp")
                if not ts:
                    continue
                t = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                msg = o.get("message") or {}
                c = msg.get("content")
                if o.get("type") == "user":
                    text = c if isinstance(c, str) else " ".join(x.get("text", "") for x in (c or []) if isinstance(x, dict) and x.get("type") == "text")
                    if not text or text.startswith(("<system-reminder", "<task-notification", "[Request interrupted", "Base directory for this skill", "Caveat:")) or o.get("isMeta"):
                        continue
                    if "tool_result" in json.dumps(c)[:200] and not isinstance(c, str):
                        continue
                    user_times[sess].append(t)
                    low = text.lower()[:600]
                    m = re.search(r"<command-name>/?([\w:-]+)</command-name>", text)
                    if m and m.group(1) in skills:
                        ev["skill:" + m.group(1)].append((t, sess))
                    for n, r in rx.items():
                        if r.search(low):
                            ev["sop:" + n].append((t, sess))
                elif o.get("type") == "assistant" and isinstance(c, list):
                    for x in c:
                        if x.get("type") != "tool_use":
                            continue
                        inp = x.get("input") or {}
                        if x.get("name") == "Skill":
                            ev["skill:" + str(inp.get("skill", "")).split(":")[-1]].append((t, sess))
                        elif x.get("name") in ("Agent", "Task"):
                            ev["agent:" + str(inp.get("subagent_type") or "general-purpose")].append((t, sess))
    for s in user_times:
        user_times[s].sort()
    now = datetime.now(timezone.utc)
    out = {}
    for k, lst in ev.items():
        lst.sort()
        mins = []
        for t, s in lst:
            later = [u for u in user_times[s] if u > t + timedelta(seconds=5)]
            if later:
                d = (later[0] - t).total_seconds() / 60
                if d < 240:   # a gap over 4 h is Chief away, not the procedure
                    mins.append(d)
        out[k] = {"runs": len(lst), "first": lst[0][0].astimezone().strftime("%Y-%m-%d"),
                  "last": lst[-1][0].astimezone().strftime("%Y-%m-%d %H:%M"),
                  "last7": sum(1 for t, _ in lst if now - t < timedelta(days=7)),
                  "sessions": len({s for _, s in lst}),
                  "median_min": round(statistics.median(mins), 1) if mins else None}
    return out, len(files)


def main():
    t0 = time.time()
    os.makedirs(DATA, exist_ok=True)
    mod = load_kit_module()
    r, k, s = repos(), kit(mod), sops()
    rn, nfiles = runs(s, k)
    for name, obj in (("repos", r), ("kit", k), ("sops", s), ("runs", rn)):
        json.dump(obj, open(os.path.join(DATA, f"{name}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # the index the matcher reads: names and one line each, never the full files
    idx = ["# Kit index (for the matcher)", ""] + [f"- {i['kind']} · {i['name']} · {i['desc'][:220]}" for i in k]
    open(os.path.join(DATA, "kit.index.md"), "w", encoding="utf-8").write("\n".join(idx) + "\n")
    print(f"BEARINGS collect · repos {len(r)} · kit {len(k)} · sops {len(s)} · run keys {len(rn)} from {nfiles} transcripts · "
          f"{time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
