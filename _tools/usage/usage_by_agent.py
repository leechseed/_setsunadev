# -*- coding: utf-8 -*-
"""Second pass: what the subagents were, and which tools' results filled the contexts."""
import io, json, os, glob, collections, datetime as dt
ROOT = r"C:\Users\U01_LEECHSEED\.claude\projects\c--Users-U01-LEECHSEED-Desktop--setsunadev"
since = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=8)
W = lambda u: u["in"]+1.25*u["cw"]+0.1*u["cr"]+5*u["out"]

def lines(fp):
    with io.open(fp, encoding="utf-8", errors="replace") as fh:
        for l in fh:
            try: yield json.loads(l)
            except Exception: pass

# --- per subagent: model, weighted, first user prompt (the tasking) ---
subs = []
for fp in glob.glob(os.path.join(ROOT, "*", "subagents", "**", "*.jsonl"), recursive=True):
    sess = os.path.relpath(fp, ROOT).split(os.sep)[0]
    u = {"in":0,"cw":0,"cr":0,"out":0}; seen=set(); prompt=None; model="?"; day="?"
    for o in lines(fp):
        ts=o.get("timestamp")
        if not ts: continue
        t=dt.datetime.fromisoformat(ts.replace("Z","+00:00"))
        if t<since: continue
        day=t.astimezone().strftime("%m-%d")
        m=o.get("message") or {}
        if o.get("type")=="user" and prompt is None:
            c=m.get("content")
            if isinstance(c,str): prompt=c
            elif isinstance(c,list):
                for b in c:
                    if isinstance(b,dict) and b.get("type")=="text": prompt=b["text"]; break
        if o.get("type")=="assistant" and m.get("usage"):
            k=(m.get("id"),m["usage"].get("output_tokens"))
            if k in seen: continue
            seen.add(k); model=m.get("model",model)
            uu=m["usage"]; u["in"]+=uu.get("input_tokens",0); u["cw"]+=uu.get("cache_creation_input_tokens",0)
            u["cr"]+=uu.get("cache_read_input_tokens",0); u["out"]+=uu.get("output_tokens",0)
    if u["out"]==0 and u["cw"]==0: continue
    subs.append((W(u), day, sess[:8], model.replace("claude-",""), u["out"], (prompt or "")[:90].replace("\n"," ")))
subs.sort(reverse=True)
print("== SUBAGENTS, top 30 by weighted ==")
print(f"{'W':>11} {'day':<6}{'sess':<9}{'model':<12}{'out':>7}  tasking")
for w,day,s,mdl,out,p in subs[:30]:
    print(f"{int(w):>11,} {day:<6}{s:<9}{mdl:<12}{out:>7,}  {p}")
print(f"subagents in window: {len(subs)} · total sub-W {int(sum(x[0] for x in subs)):,}")

# --- tool-result bytes by tool, main sessions only + subagents ---
tb = collections.Counter(); tc = collections.Counter()
for fp in glob.glob(os.path.join(ROOT, "*.jsonl")) + glob.glob(os.path.join(ROOT, "*", "subagents", "**", "*.jsonl"), recursive=True):
    idmap={}
    for o in lines(fp):
        ts=o.get("timestamp")
        if not ts: continue
        t=dt.datetime.fromisoformat(ts.replace("Z","+00:00"))
        if t<since: continue
        m=o.get("message") or {}
        c=m.get("content")
        if not isinstance(c,list): continue
        for b in c:
            if not isinstance(b,dict): continue
            if b.get("type")=="tool_use":
                nm=b.get("name","?")
                if nm=="Bash": nm="Bash"
                idmap[b.get("id")]=nm; tc[nm]+=1
            elif b.get("type")=="tool_result":
                nm=idmap.get(b.get("tool_use_id"),"?")
                cc=b.get("content"); n=len(cc) if isinstance(cc,str) else len(json.dumps(cc)) if cc else 0
                tb[nm]+=n
print("\n== TOOL RESULTS: bytes that entered a context, by tool (main + subs) ==")
tot=sum(tb.values())
for nm,n in tb.most_common(15): print(f"{n/1e6:>8.1f} MB {100*n/tot:>5.1f}%  {tc[nm]:>5} calls  {nm}")
print(f"{tot/1e6:>8.1f} MB total ≈ {tot/4/1e6:.1f}M tokens")
