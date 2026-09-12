# -*- coding: utf-8 -*-
"""Token usage over the last N days from local Claude Code transcripts.
Groups: per day · per session (main vs subagents) · per tool name · per model.
Weighted usage approximates how limits count: output x5, cache-write x1.25, cache-read x0.1, input x1.
"""
import io, json, os, sys, glob, collections, datetime as dt

ROOT = r"C:\Users\U01_LEECHSEED\.claude\projects\c--Users-U01-LEECHSEED-Desktop--setsunadev"
DAYS = int(sys.argv[1]) if len(sys.argv) > 1 else 8
since = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=DAYS)

def weight(u):
    return (u["in"] + 1.25*u["cw"] + 0.1*u["cr"] + 5*u["out"])

Z = lambda: {"in":0,"cw":0,"cr":0,"out":0,"msgs":0}
def add(d, u):
    for k in ("in","cw","cr","out"): d[k]+=u[k]
    d["msgs"]+=1

by_day = collections.defaultdict(Z)
by_sess = collections.defaultdict(Z)          # (session, kind) kind=main|sub
by_model = collections.defaultdict(Z)
tool_calls = collections.Counter()
tool_result_bytes = collections.Counter()
sub_count = collections.Counter()             # session -> number of subagent files
first_prompt = {}
sess_dates = {}
seen_ids = set()

files = glob.glob(os.path.join(ROOT, "*.jsonl")) + glob.glob(os.path.join(ROOT, "*", "subagents", "**", "*.jsonl"), recursive=True)
for fp in files:
    rel = os.path.relpath(fp, ROOT)
    parts = rel.split(os.sep)
    sess = parts[0].replace(".jsonl","")
    kind = "sub" if len(parts) > 1 else "main"
    if kind == "sub": sub_count[sess] += 1
    try:
        fh = io.open(fp, encoding="utf-8", errors="replace")
    except OSError:
        continue
    with fh:
        for line in fh:
            try: o = json.loads(line)
            except Exception: continue
            ts = o.get("timestamp")
            if not ts: continue
            try: t = dt.datetime.fromisoformat(ts.replace("Z","+00:00"))
            except Exception: continue
            if t < since: continue
            day = t.astimezone().strftime("%m-%d")
            typ = o.get("type")
            msg = o.get("message") or {}
            if typ == "user" and kind == "main" and sess not in first_prompt:
                c = msg.get("content")
                if isinstance(c, str) and not c.startswith("<"):
                    first_prompt[sess] = c[:70].replace("\n"," ")
                elif isinstance(c, list):
                    for b in c:
                        if isinstance(b, dict) and b.get("type")=="text" and not b["text"].startswith("<"):
                            first_prompt[sess] = b["text"][:70].replace("\n"," "); break
            if typ == "user":
                c = msg.get("content")
                if isinstance(c, list):
                    for b in c:
                        if isinstance(b, dict) and b.get("type")=="tool_result":
                            cc = b.get("content")
                            n = len(cc) if isinstance(cc,str) else len(json.dumps(cc)) if cc else 0
                            tool_result_bytes[o.get("toolUseResult",{}).get("_tool","?") if isinstance(o.get("toolUseResult"),dict) else "?"] += n
            if typ != "assistant": continue
            u = msg.get("usage")
            mid = msg.get("id")
            if not u: continue
            # dedupe streamed duplicates of the same message id
            key = (mid, u.get("output_tokens"))
            if mid and key in seen_ids: continue
            seen_ids.add(key)
            uu = {"in":u.get("input_tokens",0),"cw":u.get("cache_creation_input_tokens",0),
                  "cr":u.get("cache_read_input_tokens",0),"out":u.get("output_tokens",0)}
            add(by_day[day], uu); add(by_sess[(sess,kind)], uu); add(by_model[msg.get("model","?")], uu)
            sess_dates.setdefault(sess, day)
            for b in msg.get("content") or []:
                if isinstance(b, dict) and b.get("type")=="tool_use":
                    nm = b.get("name","?")
                    if nm == "Agent":
                        nm = "Agent:" + str((b.get("input") or {}).get("model") or "inherit")
                    tool_calls[nm] += 1

def row(lbl, u):
    return f"{lbl:<58} {u['in']:>9,} {u['cw']:>11,} {u['cr']:>13,} {u['out']:>9,} {int(weight(u)):>12,} {u['msgs']:>6}"
hdr = f"{'':<58} {'input':>9} {'cache-write':>11} {'cache-read':>13} {'output':>9} {'WEIGHTED':>12} {'msgs':>6}"

print("== BY DAY (local) =="); print(hdr)
tot = Z()
for d in sorted(by_day):
    print(row(d, by_day[d]));
    for k in ("in","cw","cr","out"): tot[k]+=by_day[d][k]
    tot["msgs"]+=by_day[d]["msgs"]
print(row("TOTAL", tot))

print("\n== BY MODEL =="); print(hdr)
for m,u in sorted(by_model.items(), key=lambda kv:-weight(kv[1])): print(row(m,u))

print("\n== TOP SESSIONS (main + its subagents), by weighted ==")
agg = collections.defaultdict(lambda: {"main":Z(),"sub":Z()})
for (s,k),u in by_sess.items():
    for kk in ("in","cw","cr","out"): agg[s][k][kk]+=u[kk]
    agg[s][k]["msgs"]+=u["msgs"]
def tw(a): return weight(a["main"])+weight(a["sub"])
print(f"{'day':<6}{'session':<10}{'subs':>5} {'main-W':>12} {'sub-W':>12} {'out-main':>9} {'out-sub':>9}  first prompt")
for s,a in sorted(agg.items(), key=lambda kv:-tw(kv[1]))[:18]:
    print(f"{sess_dates.get(s,'?'):<6}{s[:8]:<10}{sub_count[s]:>5} {int(weight(a['main'])):>12,} {int(weight(a['sub'])):>12,} {a['main']['out']:>9,} {a['sub']['out']:>9,}  {first_prompt.get(s,'')}")

print("\n== TOOL CALLS (count) ==")
for nm,c in tool_calls.most_common(25): print(f"{c:>6}  {nm}")
