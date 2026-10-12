"""SITREP assemble — the fan-in (BOLO 54, the formation).

Usage:  python _tools/sitrep/assemble.py <date> [--build] [--flush]

Reads   work/<date>/frag/{0,I,II,IV,V}.json   from the three specialists
        work/<date>/frag/{III,VII}.json        carried by prep.py
        work/<date>/frag/VI.json               written by the main line after the digest (optional on a dry run)
        work/<date>/meta.json                  from prep.py (+ work/<date>/meta.patch.json, the main line's overrides)
Checks  the reviewer's list — deterministic, no agent:
        all eight blocks in order · every item has t + trunk · trunk values legal ·
        every [[key]] resolves in glossary.json · every BOLO number named in Block IV exists in BOLO.md ·
        Block V row count equals the Blocked table's numbered rows · no empty plain/strand · no fragment older than prep
Writes  boards/<date>.json, prints the digest (what changed vs the previous board, counts, findings)
--build runs build.py on it; --flush moves _CACHE/*.session.md → _LOG/ (only after a clean write)
"""
import io, json, os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
BOARDS = os.path.join(HERE, "boards")
WORK = os.path.join(HERE, "work")
ORDER = ["0", "I", "II", "III", "IV", "V", "VI", "VII"]
TRUNKS = {"BLACK", "ORANGE", "OPERATOR"}

def load(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()

def jload(p):
    return json.loads(load(p))

def items_of(block):
    out = list(block.get("items", []))
    for g in block.get("groups", []):
        out += g.get("items", [])
    return out

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    date = sys.argv[1]
    flags = set(sys.argv[2:])
    wd = os.path.join(WORK, date)
    fd = os.path.join(wd, "frag")
    findings, blocks = [], []
    iii_src = "carried"

    meta = jload(os.path.join(wd, "meta.json"))
    pp = os.path.join(wd, "meta.patch.json")
    if os.path.exists(pp):
        meta.update(jload(pp))
    # the page maps stats as a list of "label: value" strings; a dict here blanks the whole board (10/4, twice)
    if isinstance(meta.get("stats"), dict):
        meta["stats"] = [f"{k.replace('_', ' ')}: {v}" for k, v in meta["stats"].items()]
        findings.append("meta.stats was a dict — coerced to a list of 'label: value' strings (write a list next time)")
    for k in ("prev_board", "sizes_kb", "commits_since_prev"):
        meta.pop(k, None)

    prep_time = os.path.getmtime(os.path.join(wd, "meta.json"))
    for bid in ORDER:
        p = os.path.join(fd, f"{bid}.json")
        if not os.path.exists(p):
            if bid == "VI":
                findings.append("VI missing — the main line writes frag/VI.json (line + why + strand) after reading this digest")
                blocks.append({"id": "VI", "name": "The leverage line", "kind": "line", "plain": "", "strand": {}, "line": "", "why": ""})
            else:
                findings.append(f"{bid} MISSING — no fragment at {os.path.relpath(p, ROOT)}")
            continue
        if os.path.getmtime(p) < prep_time and bid not in ("III", "VII"):
            findings.append(f"{bid} is older than prep — a stale fragment?")
        b = jload(p)
        if bid == "III" and "_carried" not in b and os.path.getmtime(p) >= prep_time:
            iii_src = "INDEX"   # BOLO 86: INDEX rebuilt III from PROJECTS.md; prep's carried copy always has _carried
        b.pop("_carried", None)
        if b.get("id") != bid:
            findings.append(f"{bid}: fragment id says {b.get('id')!r}")
            b["id"] = bid
        blocks.append(b)

    # the reviewer's list
    glossary = jload(os.path.join(HERE, "glossary.json"))
    text = json.dumps(blocks, ensure_ascii=False)
    missing = sorted({k for k in re.findall(r"\[\[([^\]|]+)", text) if k not in glossary})
    if missing:
        findings.append("unknown glossary keys: " + ", ".join(missing))
    for b in blocks:
        if b["id"] == "VI" and not b.get("line"):
            continue
        if not b.get("plain") or not all(b.get("strand", {}).get(k) for k in ("last", "plan", "you", "next")):
            findings.append(f"{b['id']}: plain or strand incomplete")
        for i, it in enumerate(items_of(b)):
            if not (it.get("t") or it.get("title") or it.get("what") or it.get("item")):
                findings.append(f"{b['id']} item {i}: no text (t · title/what · item)")
            tr = it.get("trunk", "")
            if b["id"] not in ("VI", "VII") and not tr:
                findings.append(f"{b['id']} item {i}: no trunk (trunk discipline, SOP §2)")
            elif tr and not set(re.split(r"[/+ ]+", tr)) <= TRUNKS:
                findings.append(f"{b['id']} item {i}: trunk {tr!r} not in BLACK · ORANGE · OPERATOR")

    bolo = load(os.path.join(ROOT, "BOLO.md"))
    real = {int(n) for n in re.findall(r"^\| (\d+) \|", bolo, re.M)}
    iv = next((b for b in blocks if b["id"] == "IV"), None)
    if iv:
        named = {int(n) for n in re.findall(r"\*\*(\d+)\*\*|\bBOLO (\d+)\b|(?<![\w/])(\d{1,2})(?= ·|\.$|$)", json.dumps([i["t"] for i in items_of(iv)], ensure_ascii=False)) for n in n if n}
        ghost = sorted(named - real)
        if ghost:
            findings.append(f"IV names numbers that are not BOLOs (advisory): {ghost}")
        unplaced = sorted(real - named)
        if unplaced:
            findings.append(f"IV: BOLOs not placed in any group: {unplaced}")
        if "pmcs" in iv:
            rows = len(re.findall(r"^\| \*\*", bolo.split("## PMCS")[-1].split("## Done")[0], re.M))
            if rows != len(iv["pmcs"]):
                findings.append(f"IV pmcs has {len(iv['pmcs'])} entries; the PMCS table has {rows}")
    v = next((b for b in blocks if b["id"] == "V"), None)
    if v:
        state = load(os.path.join(ROOT, "STATE.md"))
        blocked = state.split("## 🔴 Blocked on you")[-1].split("\n## ")[0]
        rows = len(re.findall(r"^\| \*\*\d+\*\* \|", blocked, re.M))
        if rows != len(v.get("items", [])):
            findings.append(f"V has {len(v.get('items', []))} items; the Blocked table has {rows} numbered rows")

    # DOC-SOP 3.2 (BOLO 95): long sentences, advisory only; quoted speech is Chief's and does not count
    def _long(s):
        s = re.sub(r"\[\[[^\]|]+\|([^\]]+)\]\]", r"", re.sub(r'"[^"]*"', "", s))
        return [x for x in re.split(r"(?<=[.!?;])\s+|\s+·\s+", s) if len(x.split()) > 20]  # a · list item is its own idea
    longs = {}
    for b in blocks:
        txt = [b.get("plain", ""), b.get("line", ""), b.get("why", "")] + list((b.get("strand") or {}).values()) + [i.get("t", "") for i in items_of(b) if isinstance(i, dict)]
        n = sum(len(_long(t)) for t in txt if isinstance(t, str))
        if n: longs[b["id"]] = n
    if longs:
        findings.append("sentences over 20 words (advisory, SOP 3.2): " + " · ".join(f"{k} {v}" for k, v in longs.items()))
        # the auto-rerun (BOLO 95, ruled 10/4 "recommend"): one rerun per role, the finding pasted; written once, never looped
        ROLES = {"0": ("RACK", "haiku"), "I": ("INDEX", "sonnet"), "II": ("INDEX", "sonnet"), "V": ("INDEX", "sonnet"), "IV": ("WATCH", "haiku")}
        byrole = {}
        for bid, n in longs.items():
            if bid in ROLES: byrole.setdefault(ROLES[bid], []).append((bid, n))
        for (role, model), hits in byrole.items():
            rp = os.path.join(wd, f"rerun.{role}.md")
            if os.path.exists(rp): continue  # already rerun once this board; the rest rides as advisory
            files = " · ".join(os.path.relpath(os.path.join(wd, "frag", f"{b}.json"), ROOT).replace("\\", "/") for b, _ in hits)
            io.open(rp, "w", encoding="utf-8").write(
                f"Repo root {ROOT}. You are {role}, rerun with one finding. Model: {model}. Write files as UTF-8.\n"
                f"READ and REWRITE only: {files}.\n"
                f"FINDING (RANGE, DOC-SOP 3.2): sentences over 20 words: " + ", ".join(f"{b} has {n}" for b, n in hits) + ". "
                "Rule: one idea per sentence, 20 words at most; every sentence names who does what. A ' · ' list item counts as its own sentence.\n"
                "Do: split or trim every sentence and list item over 20 words, in plain, strand, line, why and every item's text. Strand values stay strings. "
                "Keep all facts, numbers, keys, [[key|label]] links, trunks, s, when and the JSON shape exactly. Text inside quotation marks is Chief's and stays verbatim. "
                "Count the words yourself before you finish.\nReply in one line.\n")
            print(f"RERUN {role} ({model}) · brief {os.path.relpath(rp, ROOT)}")

    # BOLO 122: one ledger line per board; append-only, never read here, never allowed to break the board
    try:
        reruns = sorted(f[len('rerun.'):-3] for f in os.listdir(wd) if f.startswith('rerun.') and f.endswith('.md'))
        import datetime
        with io.open(os.path.join(HERE, 'judge_ledger.jsonl'), 'a', encoding='utf-8', newline='\n') as lf:
            lf.write(json.dumps({'ts': datetime.datetime.now().isoformat(timespec='seconds'), 'date': date, 'src': 'assemble', 'reruns': reruns,
                                 'findings': len(findings), 'long_sentence_blocks': longs, 'iii': iii_src}, ensure_ascii=False) + '\n')
    except Exception:
        pass

    # the digest: what changed vs the previous board
    prev_dir = os.path.join(wd, "prev")
    print(f"SITREP assemble · {date}")
    for b in blocks:
        n = len(items_of(b))
        pv = os.path.join(prev_dir, f"{b['id']}.json")
        pn = len(items_of(jload(pv))) if os.path.exists(pv) else "-"
        head = (b.get("line") or b.get("plain") or "")[:110].replace("\n", " ")
        print(f"  {b['id']:>3} {b.get('name','?'):<20} {n:>3} items (was {pn})  {head}")
    if findings:
        print("FINDINGS (" + str(len(findings)) + "):")
        for f in findings: print("  - " + f)
    blocking = [f for f in findings if "MISSING" in f or "unknown glossary" in f]
    if blocking:
        print("NOT WRITTEN — fix the blocking findings above."); sys.exit(1)

    board = {"meta": meta, "blocks": [next(b for b in blocks if b["id"] == bid) for bid in ORDER if any(x["id"] == bid for x in blocks)]}
    out = os.path.join(BOARDS, date + ".json")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(board, f, ensure_ascii=False, indent=1)
    print("wrote", os.path.relpath(out, ROOT), f"({os.path.getsize(out)//1024} KB)")

    if "--build" in flags:
        r = subprocess.run([sys.executable, os.path.join(HERE, "build.py"), date], cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
        print(r.stdout.strip()); print(r.stderr.strip())
        if r.returncode: sys.exit(r.returncode)
    if "--flush" in flags:
        cache, logd = os.path.join(ROOT, "_CACHE"), os.path.join(ROOT, "_LOG")
        moved = []
        import re as _re
        def _nk(f):   # BOLO 86: natural order, so -2 follows the plain note
            m = _re.match(r"(\d{4}-\d{2}-\d{2})(?:-(\d+))?\.session\.md$", f)
            return (m.group(1), int(m.group(2) or 1)) if m else ("", 0)
        notes = sorted([f for f in os.listdir(cache) if f.endswith(".session.md")], key=_nk)
        for f in notes[:-1]:   # keep only the newest note (BOLO 86 rec 3)
            shutil.move(os.path.join(cache, f), os.path.join(logd, f)); moved.append(f)
        print("flushed → _LOG/: " + (", ".join(moved) or "nothing (the newest note stays staged)"))

if __name__ == "__main__":
    try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception: pass
    main()
