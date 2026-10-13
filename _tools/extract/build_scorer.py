"""Build the langextract scoring page (BOLO 140 step 2, 10/13).

Reads the queue, every out/<stem>.jsonl the trial wrote, and the source notes for context,
then writes out/scorer.html: one section per note, one row per extracted event, a Right and a
Wrong button per row. Scores go to the artifact db (collection "scores") when the page is
published with capabilities {db: {}}; the CDR reads them back with ArtifactData.

Usage:  python _tools/extract/build_scorer.py [--queue _tools/extract/queue.txt]
"""
from __future__ import annotations

import argparse
import html
import json
import re
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "_tools/extract/out"
CTX = 140  # chars of source context on each side of the quote


def esc(s) -> str:
    return html.escape(str(s or ""), quote=True)


def rows_for(note: Path):
    stem = note.stem.replace(" ", "_")
    jl = OUT / f"{stem}.jsonl"
    if not jl.exists():
        return stem, "", None
    text = note.read_text(encoding="utf-8", errors="replace")
    rows = [json.loads(ln) for ln in jl.read_text(encoding="utf-8").splitlines() if ln.strip()]
    rev = OUT / f"{stem}.review.md"
    secs = ""
    if rev.exists():
        m = re.search(r"· (\d+) s ·", rev.read_text(encoding="utf-8"))
        secs = m.group(1) if m else ""
    for r in rows:
        a, b = int(r["start"]), int(r["end"])
        pre = text[max(0, a - CTX):a].lstrip()
        post = text[b:b + CTX].rstrip()
        r["pre"] = re.sub(r"\s+", " ", pre)
        r["post"] = re.sub(r"\s+", " ", post)
    return stem, secs, rows


def tip(term: str, body: str, gid: str) -> str:
    return (f'<button type="button" class="t" aria-describedby="{gid}">{esc(term)}'
            f'<span class="tip" role="tooltip" id="{gid}">{esc(body)}</span></button>')


def build(queue: Path) -> Path:
    notes = [ROOT / ln.strip() for ln in queue.read_text(encoding="utf-8").splitlines() if ln.strip()]
    sections, total, skipped = [], 0, []
    for n in notes:
        stem, secs, rows = rows_for(n)
        if rows is None:
            skipped.append(n.name)
            continue
        total += len(rows)
        body = []
        for i, r in enumerate(rows, 1):
            rid = f"{stem}__{i}"
            chips = "".join(f'<span class="chip"><b>{k}</b> {esc(r.get(k) or "·")}</span>' for k in ("who", "what", "when", "where", "era"))
            body.append(f"""
      <article class="row" data-id="{esc(rid)}" data-note="{esc(stem)}">
        <div class="n">{i}</div>
        <div class="body">
          <p class="q"><span class="pre">{esc(r['pre'])}</span><mark>{esc(r['text'])}</mark><span class="post">{esc(r['post'])}</span></p>
          <div class="chips">{chips}<span class="chip pos">{r['start']}–{r['end']}</span></div>
        </div>
        <div class="yn"><button type="button" class="y" data-s="right" aria-pressed="false">Right</button><button type="button" class="w" data-s="wrong" aria-pressed="false">Wrong</button></div>
      </article>""")
        if not rows:
            body.append('<p class="none">The model found no event in this note.</p>')
        rel = str(n.relative_to(ROOT)).replace("\\", "/")
        sections.append(f"""
    <section class="note" id="{esc(stem)}">
      <h2><span class="name">{esc(n.name)}</span><span class="s"><span class="cnt" data-cnt="{esc(stem)}">0 / {len(rows)} scored</span> · {len(rows)} row{'' if len(rows)==1 else 's'}{' · ' + secs + ' s' if secs else ''}</span></h2>
      <p class="path">{esc(rel)}</p>
      {''.join(body)}
    </section>""")

    built = time.strftime("%b %d, %I:%M %p").replace(" 0", " ")
    page = f"""<title>Event Scorer</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  /* the Command look, DARK only (ruled 9/11): one strip, then one section per note, one row per event, Right or Wrong */
  :root {{ color-scheme: dark;
    --bg:#121110; --panel:#1B1A18; --panel-2:#24221F; --line:#34312C; --ink:#ECE7DF; --ink-2:#B7B0A5; --ink-3:#7F786E;
    --accent:#FF5A1F; --accent-soft:#3A1D10; --accent-ink:#FFB08F; --good:#5FBF8A; --good-soft:#16301F; --bad:#E9788A; --bad-soft:#3A1B20;
    --display:"Barlow Condensed","Arial Narrow",Arial,sans-serif; --body:"Atkinson Hyperlegible","Segoe UI",Verdana,sans-serif; --mono:"IBM Plex Mono",Consolas,monospace; }}
  *{{box-sizing:border-box}} html,body{{background:var(--bg);color:var(--ink)}}
  body{{font:15px/1.5 var(--body);padding-inline:16px;padding-block:0 64px}}
  :focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
  .strip{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;display:flex;align-items:center;gap:12px;flex-wrap:wrap;min-height:44px;margin-inline:-16px;padding:6px 16px;background:var(--panel);border-bottom:1px solid var(--line)}}
  .strip h1{{margin:0;font:800 20px/1 var(--display);letter-spacing:.06em;text-transform:uppercase}} .strip h1 b{{color:var(--accent)}}
  .chipx{{font:500 11px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;padding:4px 7px;border:1px solid var(--line);border-radius:3px;color:var(--ink-2)}}
  .spacer{{flex:1}}
  .tot{{font:700 18px var(--display);font-variant-numeric:tabular-nums;white-space:nowrap}} .tot span{{color:var(--accent)}} .tot .g{{color:var(--good)}} .tot .b{{color:var(--bad)}}
  #saveState{{font:500 11px var(--mono);color:var(--ink-3)}}
  .bar{{height:4px;background:var(--panel-2);margin-inline:-16px;display:flex}} .bar i{{display:block;height:100%}} .bar .g{{background:var(--good)}} .bar .b{{background:var(--bad)}}
  .wrap{{max-width:900px;margin:0 auto;display:grid;gap:18px;padding-block:18px}}
  .lede{{margin:0;color:var(--ink-2);max-width:66ch}}
  section.note{{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:0 0 10px;min-width:0}}
  section.note h2{{margin:0;padding:10px 14px;font:700 18px var(--display);letter-spacing:.04em;display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;border-bottom:1px solid var(--line)}}
  section.note h2 .s{{margin-left:auto;font:400 12px var(--mono);color:var(--ink-2);letter-spacing:0}} section.note h2 .cnt{{color:var(--ink)}}
  .path{{margin:6px 14px 4px;font:12px var(--mono);color:var(--ink-3);overflow-wrap:anywhere}}
  .row{{display:grid;grid-template-columns:28px minmax(0,1fr) auto;gap:10px;align-items:start;padding:10px 14px;border-top:1px solid var(--line)}}
  .row.right{{background:var(--good-soft)}} .row.wrong{{background:var(--bad-soft)}}
  .row .n{{font:700 16px var(--display);color:var(--ink-3);font-variant-numeric:tabular-nums;padding-top:2px}}
  .row .body{{min-width:0}}
  .q{{margin:0 0 6px;font-size:14px;line-height:1.5;max-width:70ch}} .q .pre,.q .post{{color:var(--ink-3)}}
  .q mark{{background:var(--accent-soft);color:var(--ink);padding:1px 3px;border-radius:2px;font-weight:700}}
  .chips{{display:flex;flex-wrap:wrap;gap:4px}}
  .chip{{font:12px var(--mono);padding:2px 6px;border:1px solid var(--line);border-radius:3px;color:var(--ink-2);max-width:100%;overflow-wrap:anywhere}} .chip b{{color:var(--ink-3);font-weight:500;margin-right:4px}}
  .chip.pos{{color:var(--ink-3)}}
  .yn{{display:flex;gap:4px}}
  .yn button{{font:700 13px var(--display);letter-spacing:.06em;text-transform:uppercase;padding:6px 10px;border:1px solid var(--line);border-radius:3px;background:var(--panel-2);color:var(--ink-2);cursor:pointer}}
  .yn button:hover{{border-color:var(--ink-3);color:var(--ink)}}
  .yn .y[aria-pressed="true"]{{background:var(--good);border-color:var(--good);color:#0B1F14}}
  .yn .w[aria-pressed="true"]{{background:var(--bad);border-color:var(--bad);color:#2A0A10}}
  .none{{margin:10px 14px 0;color:var(--ink-3);font-size:14px}}
  .t{{position:relative;font:inherit;color:inherit;letter-spacing:inherit;text-transform:inherit;background:none;border:0;padding:0;border-bottom:1px dotted var(--accent);cursor:help}}
  .tip{{display:none;position:absolute;left:0;top:calc(100% + 6px);z-index:20;width:min(300px,80vw);padding:8px 10px;background:var(--panel-2);border:1px solid var(--accent);border-radius:4px;font:400 13px/1.45 var(--body);color:var(--ink);text-transform:none;letter-spacing:0;text-align:left;box-shadow:0 8px 24px rgba(0,0,0,.5)}}
  .t:hover .tip,.t:focus-visible .tip,.t.pin .tip{{display:block}}
  #noDb{{margin:0;padding:8px 12px;border:1px solid var(--bad);border-radius:4px;color:var(--bad);font-size:14px}}
  @media (max-width:640px){{.row{{grid-template-columns:24px minmax(0,1fr)}} .yn{{grid-column:2}}}}
</style>
<header class="strip">
  <h1><b>Event</b> Scorer</h1><span class="chipx">BOLO 140 · langextract step 2</span>
  <span class="spacer"></span>
  <span class="tot"><span class="g" id="nRight">0</span> right · <span class="b" id="nWrong">0</span> wrong · <span id="nOpen">{total}</span> open</span>
  <span class="tot"><span id="pct">—</span></span>
  <span id="saveState">connecting…</span>
</header>
<div class="bar"><i class="g" id="barG" style="width:0%"></i><i class="b" id="barB" style="width:0%"></i></div>
<main class="wrap">
  <p class="lede">qwen2.5:14b read {len(notes) - len(skipped)} lineage notes and pulled {total} {tip("events", "A thing that happens in the story world: a founding, a crash, a rename, a rise. The model was told to skip ideas, theory and notes about writing.", "g-ev")}.
  Every row is {tip("grounded", "The quote sits at a known offset in the source text (the small number on each row). Rows the model could not place were dropped before this page was built.", "g-gr")}: the highlighted words are the model's quote, the grey words around it are the note.
  Score each row Right or Wrong. The {tip("70% line", "The intake verdict (lx-01): if at least 70% of rows are right, the trial becomes a tool at _tools/extract/, feeding a review file, never canon.", "g-70")} decides whether this becomes a tool. Built {built}.</p>
  <p id="noDb" hidden>Scores are not saving: the page could not reach its store. Your clicks show here but will not reach the CDR.</p>
  {''.join(sections)}
</main>
<script>
  let db = null; const scores = {{}};
  const rows = Array.from(document.querySelectorAll(".row"));
  function render() {{
    let r = 0, w = 0; const per = {{}};
    for (const el of rows) {{
      const s = (scores[el.dataset.id] || {{}}).score || "";
      el.classList.toggle("right", s === "right"); el.classList.toggle("wrong", s === "wrong");
      el.querySelector(".y").setAttribute("aria-pressed", s === "right"); el.querySelector(".w").setAttribute("aria-pressed", s === "wrong");
      if (s === "right") r++; else if (s === "wrong") w++;
      const n = el.dataset.note; per[n] = per[n] || [0, 0]; per[n][1]++; if (s) per[n][0]++;
    }}
    const open = rows.length - r - w;
    document.getElementById("nRight").textContent = r; document.getElementById("nWrong").textContent = w; document.getElementById("nOpen").textContent = open;
    document.getElementById("pct").textContent = (r + w) ? Math.round(100 * r / (r + w)) + "% right" : "—";
    document.getElementById("barG").style.width = (rows.length ? 100 * r / rows.length : 0) + "%";
    document.getElementById("barB").style.width = (rows.length ? 100 * w / rows.length : 0) + "%";
    for (const [n, [a, b]] of Object.entries(per)) {{ const c = document.querySelector(`[data-cnt="${{CSS.escape(n)}}"]`); if (c) c.textContent = a + " / " + b + " scored"; }}
  }}
  async function save(id, score) {{
    const el = rows.find((x) => x.dataset.id === id);
    const cur = (scores[id] || {{}}).score;
    scores[id] = {{ note: el.dataset.note, quote: el.querySelector("mark").textContent, score: cur === score ? "" : score }};
    render();
    if (!db) return;
    const st = document.getElementById("saveState"); st.textContent = "saving…";
    try {{ await db.collection("scores").doc(id).set(scores[id]); st.textContent = "saved"; }}
    catch (e) {{ st.textContent = "not saved: " + (e && e.code || "error"); }}
  }}
  document.addEventListener("click", (ev) => {{
    const t = ev.target.closest(".t");
    document.querySelectorAll(".t.pin").forEach((x) => {{ if (x !== t) x.classList.remove("pin"); }});
    if (t) t.classList.toggle("pin");
    const k = ev.target.closest(".yn button");
    if (k) save(k.closest(".row").dataset.id, k.dataset.s);
  }});
  document.addEventListener("keydown", (ev) => {{ if (ev.key === "Escape") document.querySelectorAll(".t.pin").forEach((x) => x.classList.remove("pin")); }});
  render();
  (async () => {{
    db = window.claude && window.claude.use ? await window.claude.use("db") : null;
    const st = document.getElementById("saveState");
    if (!db) {{ document.getElementById("noDb").hidden = false; st.textContent = "view only"; return; }}
    db.collection("scores").onSnapshot((snap) => {{
      for (const d of snap.docs) scores[d.id] = d.data();
      st.textContent = "scores loaded"; render();
    }}, () => {{ st.textContent = "scores unavailable"; }});
  }})();
</script>
"""
    out = OUT / "scorer.html"
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out} · {len(notes) - len(skipped)} notes · {total} rows · skipped (no jsonl): {skipped or 'none'}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--queue", default=str(ROOT / "_tools/extract/queue.txt"))
    a = ap.parse_args()
    build(Path(a.queue))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
