# -*- coding: utf-8 -*-
"""LOCI collect — the script half of a link-harvest research run (BOLO 51 phase 7, the formation).

Usage:  python _tools/loci/collect.py <locus.md or links.txt> [--limit N] [--batch N] [--gear N] [--resume] [--check] [--wide] [--narrow 3,7,12] [--lead]
        Effort table (mar-02): 12 links or fewer = 1 PS; 13-36 = up to 3 PS; more = "gear call needed: N links" and stop unless --gear N.
        --batch N overrides the batch size. --resume reuses the fetch and writes briefs only for batches whose extract is missing or empty.
        --resume gate (aas-06): if any batch extract is missing or empty, print the pending batches and exit 2 before writing the register brief.
        --check (aas-07): validate the file, count links, print the effort row and a cost floor from the COST dict, exit without fetching.
        --wide (mar-08): PS extract only title, one-line abstract and source quality per link -> wide.k.json. Rerun --wide after they land to print the numbered list and stop.
        --narrow 3,7,12 (mar-08): reuse the fetch, rerun the full extract on only those link numbers (extract.nK.json), then write the register brief.
        --lead (BOLO 54 depth 2): also write brief.LEAD.md (work folder, batch list, budget, register brief path) for collect-lead and print it.
        Every real run appends one JSON line per step to work/<name>/trace.jsonl and writes run.json (check.py stamps the locus frontmatter from it, mar-07).

Reads   every http(s) URL in the file (order kept)
Writes  _tools/loci/work/<name>/<nnn>.txt      the page as text (tags stripped, scripts dropped), capped 120 KB
        _tools/loci/work/<name>/manifest.json  url · status · bytes · title per link
        _tools/loci/work/<name>/plan.md        question · batch split · stop rule · time (a rerun prints "resuming plan from <time>")
        _tools/loci/work/<name>/brief.EXTRACT.<k>.md   one haiku brief per batch of links: text → extract.<k>.json
        _tools/loci/work/<name>/brief.WRITE.md          the sonnet brief: every extract.*.json → the register file
        Each brief has four parts: OBJECTIVE · OUTPUT · SOURCES AND TOOLS · BOUNDARY, plus a turn cap and a hand-back cap.
Then:   python _tools/loci/check.py <name> <register.md>  proves every fetched link is covered and every claim line is sourced.
"""
import io, os, re, sys, json, html, subprocess, math, datetime, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) loci-collect/1.0"
# aas-07: per-unit cost constants for the --check floor and the frontmatter token estimate
COST = {"fetch_bytes_per_link": 60_000, "ps_tokens_per_batch": 12_000, "ms_tokens_per_register": 30_000}

def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")
def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, "w", encoding="utf-8", newline="\n") as f: f.write(s)

def trace(wd, step, batches, links, files, seconds):
    """aas-07: one JSON line per step."""
    os.makedirs(wd, exist_ok=True)
    rec = {"time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "step": step, "batches": batches,
           "links": links, "files": files, "seconds": round(seconds, 2)}
    with io.open(os.path.join(wd, "trace.jsonl"), "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")

def to_text(h):
    h = re.sub(r"(?is)<(script|style|noscript|svg|nav|footer|header)[^>]*>.*?</\1>", " ", h)
    title = re.search(r"(?is)<title[^>]*>(.*?)</title>", h)
    h = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</h\d>|</tr>", "\n", h)
    h = re.sub(r"(?s)<[^>]+>", " ", h)
    t = html.unescape(h)
    t = re.sub(r"[ \t\r\f\v]+", " ", t); t = re.sub(r"\n\s*\n+", "\n", t)
    return (html.unescape(title.group(1)).strip() if title else ""), t.strip()

def effort(n, gear):
    """mar-02 effort table -> (label, max PS), or None when a gear call is needed."""
    if n <= 12: return "1 PS, no fan-out (12 links or fewer)", 1
    if n <= 36: return "up to 3 PS (13 to 36 links)", 3
    if gear: return f"up to {gear} PS (gear {gear} passed, {n} links)", gear
    return None

def extract_ok(path):
    """mar-06: an extract counts as good only if it exists and holds a non-empty JSON list."""
    try:
        if os.path.getsize(path) < 3: return False
        return bool(json.load(io.open(path, encoding="utf-8")))
    except Exception:
        return False

def parts(who, objective, output, sources, boundary, turns, reply):
    """mar-01: the four-part brief plus the turn cap and the hand-back cap."""
    return f"""{who}
OBJECTIVE: {objective}
OUTPUT: {output}
SOURCES AND TOOLS: {sources}
BOUNDARY: {boundary}
TURN CAP: {turns}
HAND-BACK CAP: reply under 150 words; the file is the deliverable. {reply}
"""

def main():
    try: sys.stdout.reconfigure(encoding="utf-8")
    except Exception: pass
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"): print(__doc__); sys.exit(0 if a else 2)
    opt = lambda f: int(a[a.index(f) + 1]) if f in a else 0
    src = a[0]; limit = opt("--limit"); batch_arg = opt("--batch"); gear = opt("--gear"); resume = "--resume" in a
    check = "--check" in a; wide = "--wide" in a; lead = "--lead" in a
    narrow = []
    if "--narrow" in a:
        try: narrow = sorted({int(x) for x in a[a.index("--narrow") + 1].split(",") if x.strip()})
        except Exception: narrow = []
        if not narrow: print("--narrow needs link numbers, e.g. --narrow 3,7,12"); sys.exit(2)
        resume = True
    t0 = time.time()
    try: text = io.open(src, encoding="utf-8").read()
    except Exception as e: print(f"CHECK FAILED: cannot read {src}: {e}"); sys.exit(2)
    urls = []
    for u in re.findall(r"https?://[^\s)>\]]+", text):
        u = u.rstrip(".,;")
        if u not in urls: urls.append(u)
    if limit: urls = urls[:limit]
    name = os.path.splitext(os.path.basename(src))[0].replace(".locus", "")
    wd = os.path.join(HERE, "work", name)
    eff = effort(len(urls), gear)
    if check:
        n = len(urls)
        if not n: print(f"CHECK FAILED: no http(s) links in {src}"); sys.exit(2)
        row, ps = eff if eff else (f"gear call needed: {n} links (pass --gear N)", 3)
        nb = max(1, min(ps, n))
        floor_b = n * COST["fetch_bytes_per_link"]
        floor_t = nb * COST["ps_tokens_per_batch"] + COST["ms_tokens_per_register"]
        print(f"CHECK OK · {name} · {n} links · effort row: {row}")
        print(f"cost floor · fetch ~{floor_b // 1024} KB · ~{floor_t} tokens ({nb} PS batch(es) x {COST['ps_tokens_per_batch']} + 1 register x {COST['ms_tokens_per_register']}) · nothing fetched")
        sys.exit(0 if eff else 3)
    if eff is None:
        print(f"gear call needed: {len(urls)} links")
        print("stopped before any fetch. Rerun with --gear N (N = how many PS to launch) once Chief rules the gear.")
        sys.exit(3)
    plan_p = os.path.join(wd, "plan.md"); plan_time = None; plan_batch = 0
    if os.path.exists(plan_p):
        pt = io.open(plan_p, encoding="utf-8").read()
        m = re.search(r"^time: (.+)$", pt, re.M); plan_time = m.group(1).strip() if m else None
        m = re.search(r"^batch size: (\d+)", pt, re.M); plan_batch = int(m.group(1)) if m else 0
        print(f"resuming plan from {plan_time or 'unknown time'}")
    man_p = os.path.join(wd, "manifest.json")
    man = []
    if resume and os.path.exists(man_p):
        man = json.load(io.open(man_p, encoding="utf-8"))
        print(f"resume: reusing the fetch ({len(man)} links in manifest.json); nothing refetched")
    elif narrow:
        print("narrow needs a prior fetch (manifest.json); run the plain collect or --wide first"); sys.exit(2)
    else:
        for i, u in enumerate(urls, 1):
            # curl, not urllib: this box's python cert store is stale (CERTIFICATE_VERIFY_FAILED on every host, 9/12)
            try:
                r = subprocess.run(["curl", "-sL", "--compressed", "-A", UA, "--max-time", "30", "-w", "\n__STATUS__%{http_code}", u],
                                   capture_output=True, text=True, encoding="utf-8", errors="replace")
                body, _, code = r.stdout.rpartition("\n__STATUS__")
                status = int(code) if code.strip().isdigit() else 0
                body = body[:1_500_000] if code else (r.stdout or r.stderr)
            except Exception as e:
                status, body = 0, str(e)
            title, t = to_text(body) if status == 200 else ("", body)
            t = t[:120_000]
            write(os.path.join(wd, f"{i:03d}.txt"), f"URL: {u}\nTITLE: {title}\nSTATUS: {status}\n\n{t}")
            man.append({"n": i, "url": u, "status": status, "bytes": len(t.encode("utf-8")), "title": title[:120]})
            print(f"{i:03d} {status:>3} {len(t)//1024:>4} KB  {title[:60] or u[:60]}")
        write(man_p, json.dumps(man, ensure_ascii=False, indent=1))
        trace(wd, "fetch", 0, len(man), len(man) + 1, time.time() - t0)
    t1 = time.time()
    ok = [m for m in man if m["status"] == 200]
    if narrow:
        ok = [m for m in ok if m["n"] in narrow]
        if not ok: print(f"narrow: none of {narrow} is a fetched link"); sys.exit(2)
        np_ = os.path.join(wd, "narrow.json")
        try: prev = json.load(io.open(np_, encoding="utf-8"))
        except Exception: prev = None
        if prev != narrow:  # a different selection: old narrow extracts are stale
            for f in os.listdir(wd):
                if re.match(r"extract\.n\d+\.json$", f): os.remove(os.path.join(wd, f))
        write(np_, json.dumps(narrow))
    batch = batch_arg or plan_batch or (max(1, math.ceil(len(ok) / eff[1])) if ok else 12)
    if narrow and not batch_arg: batch = max(1, math.ceil(len(ok) / eff[1]))
    batches = [ok[s:s + batch] for s in range(0, len(ok), batch)]
    k = len(batches)
    dead = len([m for m in man if m["status"] != 200])
    # mar-03: the plan file, written before the fan-out (not rewritten by a narrow pass, which splits a subset)
    now = plan_time or datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    split = "\n".join(f"- batch {j}: " + ", ".join(f"{m['n']:03d}" for m in c) + f" ({len(c)} links)" for j, c in enumerate(batches, 1))
    if not narrow:
        write(plan_p, f"""# Plan · {name}
question: {name} (the locus title; the register answers it)
time: {now}
effort: {eff[0]}
batch size: {batch}
## Batch split
{split or '- (no fetched links)'}
## Stop rule
Stop when every batch has a non-empty extract.k.json, WRITE has produced the register, and check.py reports 0 MISSING and 0 errors. If most links are dead behind a bot wall, stop and say so. Rerun with --resume to redo only missing batches.
""")
    if wide:
        wp = [os.path.join(wd, f"wide.{j}.json") for j in range(1, k + 1)]
        if wp and all(extract_ok(x) for x in wp):
            rows = []
            for x in wp:
                try: rows += json.load(io.open(x, encoding="utf-8"))
                except Exception: pass
            rows.sort(key=lambda r: r.get("n", 0))
            print(f"WIDE · {name} · {len(rows)} link(s) · mark the ones worth a full read, then rerun with --narrow N,N,N")
            for r in rows:
                print(f"{r.get('n', 0):>3}. [{r.get('quality', '?')}] {str(r.get('title', ''))[:70]} - {str(r.get('abstract', ''))[:110]}")
            trace(wd, "wide-list", k, len(rows), 0, time.time() - t1)
            sys.exit(0)
        for j, chunk in enumerate(batches, 1):
            files = " · ".join(rel(os.path.join(wd, f"{m['n']:03d}.txt")) for m in chunk)
            nums = ", ".join(str(m["n"]) for m in chunk)
            write(os.path.join(wd, f"brief.WIDE.{j}.md"), parts(
                f'You are WIDE-{j}, a collect specialist for the "{name}" locus. Model: haiku. Read {rel(plan_p)}; stay inside your batch.',
                "Skim each page in your batch: title, a one-line abstract (under 25 words), and source quality. Do not list items.",
                f'{rel(os.path.join(wd, f"wide.{j}.json"))} — a JSON list, one object per file: {{"n": <link number>, "url": "…", "title": "…", "abstract": "one line", "quality": "high|low"}}. Link numbers in your batch: {nums}.',
                f'READ: {files}. Nothing else. SOURCE QUALITY: primary source = high; SEO farms, listicles, reposts = low.',
                f"every file outside your list and every batch other than {j}; no fetching.",
                "6 turns.", "Reply with the path and the link count, nothing else."))
        trace(wd, "wide-briefs", k, len(ok), k, time.time() - t1)
        print(f"WIDE · {name} · {len(ok)} fetched · {k} wide batch(es) · launch WIDE-1..{k} (haiku, one message), then rerun with --wide to print the numbered list")
        sys.exit(0)
    xp = "extract.n" if narrow else "extract."
    todo = []; skipped = []
    for j, chunk in enumerate(batches, 1):
        ex = os.path.join(wd, f"{xp}{j}.json")
        if resume and extract_ok(ex):
            skipped.append(j); continue
        todo.append(j)
        files = " · ".join(rel(os.path.join(wd, f"{m['n']:03d}.txt")) for m in chunk)
        write(os.path.join(wd, f"brief.EXTRACT.{j}.md"), parts(
            f'JOB: extracting-link-batch\nYou are EXTRACT-{j}, a collect specialist for the "{name}" locus. Model: haiku. Read {rel(plan_p)}; stay inside your batch.',
            f'Extract what each page in your batch actually lists, for the "{name}" locus. A page that is a list of standards yields many items, a single standard yields one; never invent an id; keep notes under 20 words.',
            f'{rel(os.path.join(wd, f"{xp}{j}.json"))} — a JSON list, one object per file: {{"url": "…", "body": "<the standards body or publisher>", "quality": "high|low", "items": [{{"id": "<standard number or title>", "title": "…", "domain": "<quality|software|systems|AI|risk|PM|HF|design|print|other>", "tier": "<policy|standard|handbook|procedure|list>", "free": true|false, "note": "one line"}}], "gaps": "what the page promised but did not carry"}}.',
            f'READ: {files}. Nothing else. SOURCE QUALITY: prefer the primary source (paper, author, official doc). Mark SEO farms, listicles and reposts "quality": "low"; if you cannot fit the field, start the note with "quality: low".',
            f"every file outside your list and every batch other than {j}; no fetching; no judging the register.",
            "10 turns.", "Reply with the path and the item count, nothing else."))
    if todo and resume and not narrow:
        # aas-06: never write a register brief from partial extracts
        trace(wd, "resume-gate", k, len(ok), len(todo), time.time() - t1)
        print(f"resume: batch(es) {todo} pending (extract missing or empty); briefs rewritten for them. Launch those, then rerun --resume. Register brief NOT written.")
        sys.exit(2)
    if todo and narrow:
        trace(wd, "narrow-briefs", k, len(ok), len(todo), time.time() - t1)
        print(f"narrow {narrow}: launch EXTRACT-{', '.join(map(str, todo))} (haiku), then rerun the same --narrow command to write the register brief.")
        sys.exit(0)
    wsrc = f"every {rel(wd)}/extract.n*.json (the narrow set only)" if narrow else f"every {rel(wd)}/extract.*.json"
    write(os.path.join(wd, "brief.WRITE.md"), parts(
        f'JOB: writing-harvest-register\nYou are WRITE, the register specialist for the "{name}" locus. Model: sonnet.',
        "Write the register: one table by domain (id · title · body · tier · free · maps to house area · note), then a gaps section (what no link carried), then a free-sources section. Every fetched URL appears at least once. Outline first (the domains, then the rows). Cite each claim. Keep one source per paragraph or row.",
        f"the register file the locus names (or {rel(os.path.join(wd, name + '.register.draft.md'))} if it does not). Under 900 lines. Every claim line (bullet or table row) carries one URL from manifest.json.",
        f"READ: {wsrc} and the locus file {rel(src)} (for the Command's areas it names). Nothing else. Carry each extract's quality field into the note; never rank a quality: low source above a high one.",
        "nothing not in the extracts; ids verbatim; no fetching; no new sources.",
        "20 turns.", "Reply with the path and nothing else."))
    write(os.path.join(wd, "run.json"), json.dumps({"src": os.path.abspath(src), "agents": k + 1, "batches": k, "links": len(ok), "dead": dead}))
    trace(wd, "narrow-register" if narrow else "briefs", k, len(ok), len(todo) + 2, time.time() - t1)
    print(f"COLLECT · {name} · {len(ok)}/{len(urls)} fetched · effort: {eff[0]} · {k} extract batch(es) of {batch} · {rel(wd)}")
    if resume:
        print(f"resume: skipped batch(es) {skipped or 'none'} (extract present and non-empty); briefs rewritten for {todo or 'none'}")
    if lead and not narrow and not (todo and resume):
        NL = chr(10)
        lp = os.path.join(wd, "brief.LEAD.md")
        blist = NL.join(f"- batch {j}: {rel(os.path.join(wd, f'brief.EXTRACT.{j}.md'))} -> {rel(os.path.join(wd, f'extract.{j}.json'))}" for j in todo)
        lead_txt = parts(
            f'You are collect-lead for the "{name}" locus. Model: sonnet. Depth 2 (SOP 1.17).',
            "Launch one PS per batch below as the agent extracting-link-batch (haiku; by name, never general-purpose), all in one message, each with its brief verbatim; wait; check each extract.k.json exists and parses to a non-empty JSON list (script check, no judging); then write the register from the WRITE brief yourself.",
            f"the register file named in {rel(os.path.join(wd, 'brief.WRITE.md'))}; hand back one line per batch plus the register path.",
            f"READ: {rel(plan_p)} and the briefs below. Work folder: {rel(wd)}. Batches:{NL}{blist}{NL}Register brief: {rel(os.path.join(wd, 'brief.WRITE.md'))}",
            "budget: at most 3 PS, one launch round, no relaunch, no reviewer, no depth 3; write only the register.",
            "25 turns.", "One line per batch, then the register path.")
        write(lp, lead_txt)
        print(f"LEAD brief written: {rel(lp)}"); print(lead_txt)
        sys.exit(0)
    print(f"next: launch EXTRACT-{', '.join(map(str, todo)) if todo else '(none needed)'} (haiku, one message, gear permitting) → WRITE (sonnet) → python _tools/loci/check.py {name} <register.md>")

if __name__ == "__main__":
    main()
