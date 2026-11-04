"""test_gate.py: the script reviewer for the Engine Room gate meter (BOLO 180). Builds a small fake canon in a temp folder,
checks each scrub rule, then checks the live repo run parses and adds up. Prints ok/FAIL per check and PASS or FAIL last."""
import io
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sources  # noqa: E402

P = sources.PARK
fails = []


def check(name, cond):
    print(("  ok    " if cond else "  FAIL  ") + name)
    if not cond:
        fails.append(name)


def write(base, relpath, text):
    p = os.path.join(base, relpath)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    io.open(p, "w", encoding="utf-8").write(text)


with tempfile.TemporaryDirectory() as tmp:
    canon = os.path.join(tmp, "_CANON")
    write(canon, "_SSOT/01_TEST/doc.md", "\n".join([
        "# Doc",
        "real_field: null  # " + P + " fill pass (phase 2)",                # 1 parked
        "| **P1** | `" + P + " row 9 fill pass (phase 2)` |",                # 1 parked (a marker written in code is still real)
        "Use the marker `" + P + "` for a blank field.",                    # inline code: dropped
        P + " means the field is parked until its pass.",                   # legend: dropped
        "```yaml",
        "yaml_field: null   # " + P + " fill",                              # 1 parked (yaml fence counts)
        "```",
        "```mermaid",
        "A[" + P + " step] --> B",                                          # mermaid: dropped
        "```",
        "The status is OPEN until Chief rules.",                            # unmarked
        "**OPEN:** which name wins.",                                       # 1 open
        "## Version history",
        "- **1.0.0 — 2026-10-01.** parked " + P + " rows added; OPEN item closed.",   # history: dropped x2? one line, parked kind
        "| 1.1.0 | " + P + " row |",                                        # history: dropped
        "## Next section",
        "after: null  # " + P + " later",                                   # 1 parked (history ended)
    ]))
    write(canon, "_SSOT/01_TEST/ssot_01_template_ingest.md", "x: null  # " + P + " fill\n**OPEN:** template\n")  # template: dropped x2
    write(canon, "_SSOT/02_OTHER/doc.md", "# Empty\nnothing here\n")
    write(canon, "_DOCS/01_TEST/doc/2-reference.md", "> **OPEN:** the page asks this.\nplain line\n")  # 1 open
    write(canon, "_DOCS/01_TEST/doc/1-concept.md", "OPEN as a word on a page does not count\n")
    g = sources.gate(canon=canon, waivers={})
    s1 = next(s for s in g["systems"] if s["id"] == "01")
    s2 = next(s for s in g["systems"] if s["id"] == "02")
    check("parked counts the real field, the code-span marker, the yaml-fence field and the field after history (4)", s1["parked"] == 4)
    check("open counts the SSOT marker and the page marker (2)", s1["open"] == 2)
    check("unmarked holds the loose OPEN word, apart from the gate (1)", s1["unmarked"] == 1)
    check("gate = open + parked (6)", s1["gate"] == 6)
    dropped = [r for r in s1["rows"] if r["dropped"]]
    reasons = sorted(set(r["dropped"] for r in dropped))
    check("template file dropped", "template file" in reasons)
    check("version history dropped", "version history" in reasons)
    check("mermaid dropped", "mermaid diagram" in reasons)
    check("inline-code marker dropped (the bare symbol only)", any(r.startswith("inline code") for r in reasons))
    check("legend line dropped", "legend line" in reasons)
    check("an empty system reads zero", s2["gate"] == 0 and s2["unmarked"] == 0)
    rid = next(r["row_id"] for r in s1["rows"] if r["kind"] == "parked" and not r["dropped"])
    g2 = sources.gate(canon=canon, waivers={rid: {"row_id": rid}})
    s1w = next(s for s in g2["systems"] if s["id"] == "01")
    check("a waived row leaves the gate and shows as waived", s1w["parked"] == 3 and s1w["waived"] == 1)
    check("totals add up across systems", g["totals"]["gate"] == sum(s["gate"] for s in g["systems"]))

r = subprocess.run([sys.executable, "-X", "utf8", os.path.join(HERE, "engineroom.py"), "--json"], capture_output=True, text=True,
                   encoding="utf-8")
try:
    live = json.loads(r.stdout)
    ok = len(live["systems"]) == 10 and live["totals"]["gate"] == sum(s["gate"] for s in live["systems"])
except (ValueError, KeyError):
    ok = False
check("the live run: --json parses, ten systems, the sums match", ok)

# phase 2: the answer store never writes canon, and an answer / a skip land where they should
import answers  # noqa: E402
import gatepage  # noqa: E402
for bad in ("ShroomsQ/_CANON/_SSOT/x.md", "ShroomsQ/_CANON/_DOCS/x.md", "_CANON_NODES/x.md", "ShroomsQ/_CANON/_TRACKING/oxo.yaml"):
    try:
        answers.safe_write(os.path.join(answers.ROOT, bad), "x")
        refused = False
    except PermissionError:
        refused = True
    check("the answer store refuses " + bad, refused)
with tempfile.TemporaryDirectory() as tmp:
    answers.ANS_DIR = os.path.join(tmp, "answers")
    answers.ANS_FILE = os.path.join(answers.ANS_DIR, "answers.jsonl")
    answers.WAIVERS = os.path.join(tmp, "waivers.json")
    answers.ALLOWED = (os.path.realpath(answers.ANS_DIR), os.path.realpath(answers.WAIVERS))
    answers.save({"row_id": "a#1", "mode": "answer", "answer": "belt-born"})
    answers.save({"row_id": "b#2", "mode": "rec", "rec": "wait", "answer": "wait"})
    answers.save({"row_id": "c#3", "mode": "skip"})
    got = answers.load_answers()
    w = json.load(io.open(answers.WAIVERS, encoding="utf-8"))
    check("an answer and a taken rec queue; a skip does not", len(answers.queue()) == 2 and got["c#3"]["status"] == "skipped")
    check("a skip writes a waiver (row id, no content)", [x["row_id"] for x in w] == ["c#3"] and "text" not in w[0])
    try:
        answers.save({"row_id": "d#4", "mode": "answer", "answer": "  "})
        empty_ok = False
    except ValueError:
        empty_ok = True
    check("an empty answer is refused", empty_ok)
html_page = gatepage.page(sources.gate(), {}, {})
check("the page renders with its answer window and data", "id=\"modal\"" in html_page and "er-data" in html_page)
print("FAIL" if fails else "PASS")
sys.exit(1 if fails else 0)
