# -*- coding: utf-8 -*-
"""LOCI collect — the script half of a link-harvest research run (BOLO 51 phase 7, the formation).

Usage:  python _tools/loci/collect.py <locus.md or links.txt> [--limit N] [--batch N] [--gear N] [--resume]
        Effort table (mar-02): 12 links or fewer = 1 PS; 13-36 = up to 3 PS; more = "gear call needed: N links" and stop unless --gear N.
        --batch N overrides the batch size. --resume reuses the fetch and writes briefs only for batches whose extract is missing or empty.

Reads   every http(s) URL in the file (order kept)
Writes  _tools/loci/work/<name>/<nnn>.txt      the page as text (tags stripped, scripts dropped), capped 120 KB
        _tools/loci/work/<name>/manifest.json  url · status · bytes · title per link
        _tools/loci/work/<name>/plan.md        question · batch split · stop rule · time (a rerun prints "resuming plan from <time>")
        _tools/loci/work/<name>/brief.EXTRACT.<k>.md   one haiku brief per batch of links: text → extract.<k>.json
        _tools/loci/work/<name>/brief.WRITE.md          the sonnet brief: every extract.*.json → the register file
        Each brief has four parts: OBJECTIVE · OUTPUT · SOURCES AND TOOLS · BOUNDARY, plus a turn cap and a hand-back cap.
Then:   python _tools/loci/check.py <name> <register.md>  proves every fetched link is covered and every claim line is sourced.
"""
import io, os, re, sys, json, html, subprocess, math, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) loci-collect/1.0"

def rel(p): return os.path.relpath(p, ROOT).replace("\\", "/")
def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, "w", encoding="utf-8", newline="\n") as f: f.write(s)

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
    text = io.open(src, encoding="utf-8").read()
    urls = []
    for u in re.findall(r"https?://[^\s)>\]]+", text):
        u = u.rstrip(".,;")
        if u not in urls: urls.append(u)
    if limit: urls = urls[:limit]
    name = os.path.splitext(os.path.basename(src))[0].replace(".locus", "")
    wd = os.path.join(HERE, "work", name)
    eff = effort(len(urls), gear)
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
    ok = [m for m in man if m["status"] == 200]
    batch = batch_arg or plan_batch or (max(1, math.ceil(len(ok) / eff[1])) if ok else 12)
    batches = [ok[s:s + batch] for s in range(0, len(ok), batch)]
    k = len(batches)
    # mar-03: the plan file, written before the fan-out
    now = plan_time or datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    split = "\n".join(f"- batch {j}: " + ", ".join(f"{m['n']:03d}" for m in c) + f" ({len(c)} links)" for j, c in enumerate(batches, 1))
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
    todo = []; skipped = []
    for j, chunk in enumerate(batches, 1):
        ex = os.path.join(wd, f"extract.{j}.json")
        if resume and extract_ok(ex):
            skipped.append(j); continue
        todo.append(j)
        files = " · ".join(rel(os.path.join(wd, f"{m['n']:03d}.txt")) for m in chunk)
        write(os.path.join(wd, f"brief.EXTRACT.{j}.md"), parts(
            f'You are EXTRACT-{j}, a collect specialist for the "{name}" locus. Model: haiku. Read {rel(plan_p)}; stay inside your batch.',
            f'Extract what each page in your batch actually lists, for the "{name}" locus. A page that is a list of standards yields many items, a single standard yields one; never invent an id; keep notes under 20 words.',
            f'{rel(os.path.join(wd, f"extract.{j}.json"))} — a JSON list, one object per file: {{"url": "…", "body": "<the standards body or publisher>", "quality": "high|low", "items": [{{"id": "<standard number or title>", "title": "…", "domain": "<quality|software|systems|AI|risk|PM|HF|design|print|other>", "tier": "<policy|standard|handbook|procedure|list>", "free": true|false, "note": "one line"}}], "gaps": "what the page promised but did not carry"}}.',
            f'READ: {files}. Nothing else. SOURCE QUALITY: prefer the primary source (paper, author, official doc). Mark SEO farms, listicles and reposts "quality": "low"; if you cannot fit the field, start the note with "quality: low".',
            f"every file outside your list and every batch other than {j}; no fetching; no judging the register.",
            "10 turns.", "Reply with the path and the item count, nothing else."))
    write(os.path.join(wd, "brief.WRITE.md"), parts(
        f'You are WRITE, the register specialist for the "{name}" locus. Model: sonnet.',
        "Write the register: one table by domain (id · title · body · tier · free · maps to house area · note), then a gaps section (what no link carried), then a free-sources section. Every fetched URL appears at least once.",
        f"the register file the locus names (or {rel(os.path.join(wd, name + '.register.draft.md'))} if it does not). Under 900 lines. Every claim line (bullet or table row) carries one URL from manifest.json.",
        f"READ: every {rel(wd)}/extract.*.json and the locus file {rel(src)} (for the Command's areas it names). Nothing else. Carry each extract's quality field into the note; never rank a quality: low source above a high one.",
        "nothing not in the extracts; ids verbatim; no fetching; no new sources.",
        "20 turns.", "Reply with the path and nothing else."))
    print(f"COLLECT · {name} · {len(ok)}/{len(urls)} fetched · effort: {eff[0]} · {k} extract batch(es) of {batch} · {rel(wd)}")
    if resume:
        print(f"resume: skipped batch(es) {skipped or 'none'} (extract present and non-empty); briefs rewritten for {todo or 'none'}")
    print(f"next: launch EXTRACT-{', '.join(map(str, todo)) if todo else '(none needed)'} (haiku, one message, gear permitting) → WRITE (sonnet) → python _tools/loci/check.py {name} <register.md>")

if __name__ == "__main__":
    main()
