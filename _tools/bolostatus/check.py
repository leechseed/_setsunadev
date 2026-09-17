# -*- coding: utf-8 -*-
"""DOPE SHEET check — the reviewer at the fan-in (script, zero tokens).

Usage:  python _tools/bolostatus/check.py <N> [--promote]
Reads boards/<N>.draft.json if present, else boards/<N>.json. Findings printed; blocking ones exit 1.
--promote renames the draft to boards/<N>.json when clean.
"""
import io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PARAS = ["S", "M", "E", "A", "C", "L"]

def main():
    n = sys.argv[1]
    dp, fp = os.path.join(HERE, "boards", f"{n}.draft.json"), os.path.join(HERE, "boards", f"{n}.json")
    p = dp if os.path.exists(dp) else fp
    try:
        b = json.load(io.open(p, encoding="utf-8"))
    except Exception as e:
        print(f"BLOCKING: {os.path.basename(p)} is not valid JSON: {e}"); sys.exit(1)
    F, W = [], []
    bolo = b.get("bolo", {})
    for k in ("n", "title", "trunk", "issued", "asof", "s", "status", "decider", "feeds", "home", "version"):
        if not bolo.get(k) and bolo.get(k) != 0: F.append(f"bolo.{k} missing")
    # a "<n>.boresight" board carries bolo.n = <n>: a BORESIGHT page on the same template (Chief 9/17)
    if str(bolo.get("n")) != str(n) and not str(n).startswith(str(bolo.get("n")) + "."):
        F.append(f"bolo.n is {bolo.get('n')!r}, file says {n}")
    ids = [x.get("id") for x in b.get("paragraphs", [])]
    if ids != PARAS: F.append(f"paragraphs are {ids}, must be {PARAS}")
    if len(b.get("mantra", [])) != 3: W.append("mantra is not three lines")
    fr = b.get("frago", {})
    for k in ("mission", "order", "default"):
        if not fr.get(k): W.append(f"frago.{k} empty (the main line's write)")
    for x in b.get("paragraphs", []):
        if not x.get("plain"): W.append(f"{x.get('id')}: plain empty")
        st = x.get("strand", {})
        if not all(st.get(k) for k in ("last", "plan", "you", "next")): W.append(f"{x.get('id')}: strand incomplete")
        if x.get("id") == "E":
            ns = [ph.get("n") for ph in x.get("phases", [])]
            if ns != sorted(ns): W.append("E: phases out of order")
            for ph in x.get("phases", []):
                if ph.get("s") not in ("done", "open", "gated", "held", "hot", "parked", "tabled"): W.append(f"E phase {ph.get('n')}: s={ph.get('s')!r}")
        if x.get("id") == "L" and not x.get("entries"): W.append("L: no entries")
        if x.get("id") == "M" and not x.get("task"): W.append("M: task empty (the main line's write)")
    text = json.dumps(b, ensure_ascii=False)
    gl = json.load(io.open(os.path.join(ROOT, "_tools", "sitrep", "glossary.json"), encoding="utf-8"))
    missing = sorted({k for k in re.findall(r"\[\[([^\]|]+)", text) if k not in gl})
    if missing: F.append("unknown glossary keys: " + ", ".join(missing))
    if f"bolo{str(n).split('.')[0]}" not in gl: W.append(f"glossary has no bolo{n} key (add it; the standing order)")
    print(f"CHECK · DOPE SHEET {n} · {os.path.basename(p)} · {len(F)} blocking · {len(W)} advisory")
    for f in F: print("  BLOCK " + f)
    for w in W: print("  note  " + w)
    if F: sys.exit(1)
    if "--promote" in sys.argv and p == dp:
        os.replace(dp, fp); print(f"promoted → boards/{n}.json")

if __name__ == "__main__":
    main()
