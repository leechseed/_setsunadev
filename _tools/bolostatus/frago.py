# -*- coding: utf-8 -*-
"""FRAGO — push a fragmentary order onto a DOPE SHEET without rewriting it (BOLO 51 phase 3; pure script).

Usage:  python _tools/bolostatus/frago.py <N> <patch.json> [--build]

The patch is small JSON; everything not mentioned stands as ordered. Keys (all optional):
  "status": "…"            bolo.status (the header line)        "s": "hot|open|held|gated|done"   bolo.s
  "order": "…"             frago.order                          "default": "…"                    frago.default
  "mission": "…"           frago.mission
  "calls":  [{"q": "…", "s": "ruled", "ruling": "…"}]           matched by q (prefix ok); missing q = new call
  "phases": [{"n": 4, "s": "done", "when": "9/12", "t": "…"}]    matched by n; new n = appended
  "files":  [{"path": "…", "what": "…", "s": "done"}]           matched by path; new path = appended
  "items":  [{"p": "S", "label": "…", "t": "…", "s": "done"}]   appended to paragraph p's group (by label prefix; new label = new group)
  "strand": {"S": {"next": "…"}, "E": {"you": "…"}}             per-paragraph strand fields
  "log":    [{"who": "Papi|Claude", "t": "…"}]                  appended to the Log paragraph, dated today
  "related":[{"n": 54, "why": "…"}]                             appended if n is new
Always: bolo.asof = today · bolo.version bumped (v0.2 → v0.3) · the change list printed.
--build runs build.py N and prints the fragment path to publish.
"""
import io, json, os, re, sys, datetime, subprocess
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    n, pp = sys.argv[1], sys.argv[2]
    bp = os.path.join(HERE, "boards", f"{n}.json")
    board = json.load(io.open(bp, encoding="utf-8"))
    patch = json.load(io.open(pp, encoding="utf-8"))
    today = datetime.date.today()
    md = f"{today.month}/{today.day}"
    changes = []
    b, fr = board["bolo"], board.setdefault("frago", {})
    P = {p["id"]: p for p in board["paragraphs"]}

    for k in ("status", "s"):
        if k in patch: b[k] = patch[k]; changes.append(f"bolo.{k}")
    for k in ("order", "default", "mission"):
        if k in patch: fr[k] = patch[k]; changes.append(f"frago.{k}")
    for c in patch.get("calls", []):
        hit = next((x for x in fr.setdefault("calls", []) if x["q"].lower().startswith(c["q"].lower()[:24])), None)
        if hit: hit.update({k: v for k, v in c.items() if k != "q"}); changes.append(f"call '{hit['q'][:30]}'")
        else: fr["calls"].append(c); changes.append(f"new call '{c['q'][:30]}'")
    E = P.get("E")
    for ph in patch.get("phases", []):
        hit = next((x for x in E.get("phases", []) if x.get("n") == ph["n"]), None) if E else None
        if hit: hit.update(ph); changes.append(f"phase {ph['n']}")
        elif E: E.setdefault("phases", []).append(ph); changes.append(f"new phase {ph['n']}")
    A = P.get("A")
    for f_ in patch.get("files", []):
        hit = next((x for x in A.get("files", []) if x["path"] == f_["path"]), None) if A else None
        if hit: hit.update(f_); changes.append(f"file {f_['path']}")
        elif A: A.setdefault("files", []).append(f_); changes.append(f"new file {f_['path']}")
    for it in patch.get("items", []):
        p = P.get(it.pop("p", "S"))
        if not p: continue
        label = it.pop("label", None)
        g = next((x for x in p.setdefault("groups", []) if label and x["label"].lower().startswith(label.lower()[:20])), None)
        if not g:
            g = {"label": label or f"FRAGO · {md}", "items": []}; p["groups"].append(g)
        g["items"].append(it); changes.append(f"item → {p['id']} / {g['label'][:24]}")
    for pid, fields in patch.get("strand", {}).items():
        if pid in P: P[pid].setdefault("strand", {}).update(fields); changes.append(f"strand {pid}")
    L = P.get("L")
    for e in patch.get("log", []):
        if L: L.setdefault("entries", []).append({"when": md, "who": e.get("who", "Claude"), "t": e["t"]}); changes.append("log entry")
    for r in patch.get("related", []):
        if not any(x.get("n") == r["n"] for x in b.setdefault("related", [])):
            b["related"].append(r); changes.append(f"related {r['n']}")

    b["asof"] = today.isoformat()
    m = re.match(r"v(\d+)\.(\d+)", b.get("version", "v0.1"))
    b["version"] = f"v{m.group(1)}.{int(m.group(2)) + 1} · DOPE SHEET" if m else "v0.2 · DOPE SHEET"
    io.open(bp, "w", encoding="utf-8", newline="\n").write(json.dumps(board, ensure_ascii=False, indent=1))
    print(f"FRAGO {n} · {b['version']} · {len(changes)} change(s): " + " · ".join(changes))
    if "--build" in sys.argv:
        r = subprocess.run([sys.executable, os.path.join(HERE, "build.py"), n], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
        print(r.stdout.strip() or r.stderr.strip())
        if r.returncode: sys.exit(r.returncode)

if __name__ == "__main__":
    main()
