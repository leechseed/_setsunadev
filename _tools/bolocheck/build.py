"""BOLO check: every open BOLO on one glass, a check or an X each (10/13).

Chief, 10/13: "glass a page with every single open BOLO on it ... a description enough to give me context
to make a decision ... a checkmark or an X ... the X means ... in storage for now ... a live BOLO, which is
what we're going to pull from, versus ... think Marine." Check = LIVE BOLO (what "what next" pulls from).
X = COSMOLINE (provisional): packed in storage grease, out of the rotation, ready to unpack whole.

Inputs : rows.json   open BOLOs (n · group · trunk · when · title · t), cut from the sit rep's Block IV
         recs.txt    the CDR's rec per BOLO: n | live · cosmo · - | why
         _tools/sitrep/glossary.json   hover text for [[key|label]] links
Output : out/bolo-check.html  (publish with capabilities {db: {}}; picks land in collection "picks")
Usage  : python _tools/bolocheck/build.py
"""
from __future__ import annotations

import html
import json
import re
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / "out" / "bolo-check.html"
GROUPS = {"hot": ("HOT", "Moving now, or one step from moving."),
          "held": ("HELD", "Waiting on one ruling from Chief."),
          "gated": ("GATED", "Fires on Chief's go word, or when another BOLO lands."),
          "open": ("SLOW", "Open but slow: parked, waiting on a thing, or idle.")}


def esc(s) -> str:
    return html.escape(str(s or ""), quote=True)


def main() -> int:
    rows = json.loads((HERE / "rows.json").read_text(encoding="utf-8"))
    recs = {}
    for ln in (HERE / "recs.txt").read_text(encoding="utf-8").splitlines():
        if ln[:1].isdigit():
            n, r, why = ln.split("|", 2)
            recs[int(n)] = (r.strip(), why.strip())
    glossary = json.loads((ROOT / "_tools/sitrep/glossary.json").read_text(encoding="utf-8"))
    ctx = {}                        # 10/13 (Chief: "one bullet ... the mission ... how far we are ... what the next step would do")
    for f in sorted((HERE / "work").glob("out*.json")):
        ctx.update({int(k): v for k, v in json.loads(f.read_text(encoding="utf-8")).items()})
    missing = [r["n"] for r in rows if r["n"] not in recs]
    assert not missing, f"no rec for BOLO {missing}"

    def linkify(t: str) -> str:
        out, last = [], 0
        for m in re.finditer(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", t):
            out.append(esc(t[last:m.start()]))
            k, label = m.group(1), m.group(2) or m.group(1)
            g = glossary.get(k)
            if g:
                d = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda x: x.group(2) or x.group(1), g["d"])
                out.append(f'<button type="button" class="t">{esc(label)}<span class="tip" role="tooltip"><b>{esc(g["t"])}</b>{esc(d)}</span></button>')
            else:
                out.append(esc(label))
            last = m.end()
        out.append(esc(t[last:]))
        return re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", "".join(out))

    def three(n: int) -> str:
        c = ctx.get(n)
        if not c:
            return ""
        li = "".join(f'<li><span class="lb">{lab}</span>{esc(c.get(key, ""))}</li>' for key, lab in (("mission", "Mission"), ("progress", "Where it stands"), ("next", "Next step")))
        return f'<ul class="three">{li}</ul>'

    items = []
    for r in sorted(rows, key=lambda r: r["n"]):
        title = r["title"] if r["title"] not in ("?", "") and not r["title"].startswith("🟢") else r["t"].split(":")[0]
        title = re.sub(r"\[\[[^\]|]+\|([^\]]+)\]\]", r"\1", title).strip(" .")
        body = r["t"]
        if body.lower().startswith(title.lower()):
            body = body[len(title):].lstrip(": ,.")
        rec, why = recs[r["n"]]
        g, gtip = GROUPS[r["g"]]
        mark = {"live": '<span class="rec live">✓ rec</span>', "cosmo": '<span class="rec cosmo">✗ rec</span>', "-": '<span class="rec none">no rec</span>'}[rec]
        items.append(f"""
    <article class="b" data-n="{r['n']}" data-g="{r['g']}" data-rec="{rec}">
      <div class="num">{r['n']}</div>
      <div class="main">
        <h3>{esc(title)}</h3>
        <div class="meta"><button type="button" class="t pill g-{r['g']}">{g}<span class="tip" role="tooltip">{esc(gtip)}</span></button><span>{esc(r['trunk'])}</span><span>{esc(r.get('when') or r.get('issued') or '')}</span></div>
        {three(r['n']) or f'<p>{linkify(body)}</p>'}
        <div class="why">{mark}<span>{esc(why)}</span></div>
        <label class="bnote"><span>Note</span><textarea id="note-{r['n']}" rows="1" placeholder="type, or click here and hold JUDY's talk key"></textarea></label>
      </div>
      <div class="yn" role="group" aria-label="BOLO {r['n']}">
        <button type="button" class="y" data-p="live" aria-pressed="false" title="LIVE BOLO">✓</button>
        <button type="button" class="x" data-p="cosmo" aria-pressed="false" title="COSMOLINE">✗</button>
      </div>
    </article>""")

    n_live = sum(1 for v in recs.values() if v[0] == "live")
    built = time.strftime("%b %d, %I:%M %p").replace(" 0", " ")
    page = f"""<title>BOLO Check</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
  /* the Command look, DARK only (ruled 9/11): one strip, a filter row, then every open BOLO as a row with ✓ and ✗ */
  :root {{ color-scheme: dark;
    --bg:#121110; --panel:#1B1A18; --panel-2:#24221F; --line:#34312C; --ink:#ECE7DF; --ink-2:#B7B0A5; --ink-3:#7F786E;
    --accent:#FF5A1F; --accent-soft:#3A1D10; --accent-ink:#FFB08F; --good:#5FBF8A; --good-soft:#16301F; --cosmo:#C9A35A; --cosmo-soft:#2E2614; --warn:#E3B341;
    --display:"Barlow Condensed","Arial Narrow",Arial,sans-serif; --body:"Atkinson Hyperlegible","Segoe UI",Verdana,sans-serif; --mono:"IBM Plex Mono",Consolas,monospace; }}
  *{{box-sizing:border-box}} html,body{{background:var(--bg);color:var(--ink)}}
  body{{font:15px/1.5 var(--body);padding-inline:16px;padding-block:0 64px}}
  :focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
  .strip{{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;display:flex;align-items:center;gap:12px;flex-wrap:wrap;min-height:44px;margin-inline:-16px;padding:6px 16px;background:var(--panel);border-bottom:1px solid var(--line)}}
  .strip h1{{margin:0;font:800 20px/1 var(--display);letter-spacing:.06em;text-transform:uppercase}} .strip h1 b{{color:var(--accent)}}
  .spacer{{flex:1}}
  .tot{{font:700 18px var(--display);font-variant-numeric:tabular-nums;white-space:nowrap;letter-spacing:.03em}} .tot .l{{color:var(--good)}} .tot .c{{color:var(--cosmo)}} .tot .o{{color:var(--ink-2)}}
  #saveState{{font:500 11px var(--mono);color:var(--ink-3)}}
  .act{{font:700 13px var(--display);letter-spacing:.08em;text-transform:uppercase;padding:6px 12px;border:1px solid var(--accent);background:var(--accent-soft);color:var(--accent-ink);border-radius:3px;cursor:pointer}}
  .act:hover{{background:var(--accent);color:#1B0A03}}
  details.about summary{{cursor:pointer;font:500 11px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);list-style:none;padding:4px 7px;border:1px solid var(--line);border-radius:3px}}
  details.about[open] div{{position:absolute;right:16px;top:48px;width:min(460px,calc(100vw - 32px));background:var(--panel-2);border:1px solid var(--line);border-radius:4px;padding:10px 12px;font-size:14px;color:var(--ink-2);z-index:30}}
  details.about div p{{margin:0 0 8px}} details.about div p:last-child{{margin:0}}
  .bar{{height:4px;background:var(--panel-2);margin-inline:-16px;display:flex}} .bar i{{display:block;height:100%}} .bar .l{{background:var(--good)}} .bar .c{{background:var(--cosmo)}}
  .wrap{{max-width:960px;margin:0 auto;display:grid;gap:12px;padding-block:16px}}
  .lede{{margin:0;color:var(--ink-2);max-width:68ch}}
  .filters{{display:flex;flex-wrap:wrap;gap:6px}}
  .filters button{{font:500 12px var(--mono);padding:5px 9px;border:1px solid var(--line);border-radius:3px;background:var(--panel);color:var(--ink-2);cursor:pointer}}
  .filters button[aria-pressed="true"]{{border-color:var(--accent);color:var(--ink);background:var(--accent-soft)}}
  .list{{display:grid;gap:6px}}
  .b{{display:grid;grid-template-columns:44px minmax(0,1fr) auto;gap:12px;align-items:start;padding:10px 12px;background:var(--panel);border:1px solid var(--line);border-left:3px solid var(--line);border-radius:4px}}
  .b.live{{border-left-color:var(--good);background:linear-gradient(90deg,var(--good-soft),var(--panel) 40%)}}
  .b.cosmo{{border-left-color:var(--cosmo);opacity:.72}}
  .b .num{{font:800 24px/1 var(--display);color:var(--accent);font-variant-numeric:tabular-nums;padding-top:2px}}
  .b .main{{min-width:0}}
  .b h3{{margin:0;font:700 19px/1.15 var(--display);letter-spacing:.02em;text-wrap:balance}}
  .meta{{display:flex;flex-wrap:wrap;gap:4px 10px;align-items:center;margin:4px 0 6px;font:12px var(--mono);color:var(--ink-3)}}
  .pill{{font:500 10.5px/1 var(--mono);letter-spacing:.1em;padding:3px 6px;border-radius:3px;border:0}}
  .g-hot{{background:var(--accent-soft);color:var(--accent-ink)}} .g-held{{background:#2E2A10;color:var(--warn)}} .g-gated{{background:#14262E;color:#7FC4D8}} .g-open{{background:var(--panel-2);color:var(--ink-2)}}
  .b p{{margin:0 0 6px;max-width:72ch;overflow-wrap:anywhere}}
  .three{{list-style:none;margin:0 0 8px;padding:0;display:grid;gap:4px;max-width:74ch}}
  .three li{{display:grid;grid-template-columns:120px minmax(0,1fr);gap:10px;padding-left:10px;border-left:2px solid var(--line)}}
  .three li:first-child{{border-left-color:var(--accent)}}
  .three .lb{{font:500 10.5px/1.9 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3)}}
  @media (max-width:620px){{.three li{{grid-template-columns:minmax(0,1fr);gap:0}}}}
  .why{{display:flex;gap:8px;align-items:baseline;flex-wrap:wrap;font-size:14px;color:var(--ink-2)}}
  .rec{{font:500 11px var(--mono);letter-spacing:.06em;padding:1px 6px;border-radius:3px;white-space:nowrap}}
  .rec.live{{color:var(--good);border:1px solid var(--good)}} .rec.cosmo{{color:var(--cosmo);border:1px solid var(--cosmo)}} .rec.none{{color:var(--ink-3);border:1px dashed var(--line)}}
  .bnote{{display:grid;grid-template-columns:auto minmax(0,1fr);gap:8px;align-items:start;margin-top:8px;max-width:74ch}}
  .bnote span{{font:500 10.5px/2.2 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3)}}
  .bnote textarea{{width:100%;min-height:30px;resize:vertical;font:14px/1.45 var(--body);color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:3px;padding:5px 8px}}
  .bnote textarea:focus{{border-color:var(--accent);outline:none}}
  .bnote textarea.has{{border-color:var(--accent-ink)}}
  .yn{{display:flex;gap:4px}}
  .yn button{{width:44px;height:40px;font:700 20px/1 var(--body);border:1px solid var(--line);border-radius:4px;background:var(--panel-2);color:var(--ink-3);cursor:pointer}}
  .yn .y:hover{{border-color:var(--good);color:var(--good)}} .yn .x:hover{{border-color:var(--cosmo);color:var(--cosmo)}}
  .yn .y[aria-pressed="true"]{{background:var(--good);border-color:var(--good);color:#0B1F14}}
  .yn .x[aria-pressed="true"]{{background:var(--cosmo);border-color:var(--cosmo);color:#221A06}}
  .t{{position:relative;font:inherit;color:inherit;letter-spacing:inherit;background:none;border:0;padding:0;border-bottom:1px dotted var(--accent);cursor:help}}
  .pill.t{{border-bottom:0}}
  .tip{{display:none;position:absolute;left:0;top:calc(100% + 6px);z-index:20;width:min(320px,78vw);padding:8px 10px;background:var(--panel-2);border:1px solid var(--accent);border-radius:4px;font:400 13px/1.45 var(--body);color:var(--ink);text-transform:none;letter-spacing:0;text-align:left;box-shadow:0 8px 24px rgba(0,0,0,.5)}}
  .tip b{{display:block;font:700 15px var(--display);text-transform:uppercase;letter-spacing:.04em;margin-bottom:2px}}
  .t:hover .tip,.t:focus-visible .tip,.t.pin .tip{{display:block}}
  #noDb{{margin:0;padding:8px 12px;border:1px solid var(--warn);border-radius:4px;color:var(--warn);font-size:14px}}
  .empty{{padding:14px;border:1px dashed var(--line);color:var(--ink-3);border-radius:4px}}
  @media (max-width:620px){{.b{{grid-template-columns:34px minmax(0,1fr)}} .yn{{grid-column:2}}}}
</style>
<header class="strip">
  <h1><b>BOLO</b> Check</h1>
  <span class="tot"><span class="l" id="nLive">0</span> live · <span class="c" id="nCosmo">0</span> cosmoline · <span class="o" id="nOpen">{len(items)}</span> to call</span>
  <span class="spacer"></span>
  <span id="saveState">connecting…</span>
  <button type="button" class="act" id="takeRecs">Take all recs</button>
  <details class="about"><summary>About</summary><div>
    <p><b>✓ LIVE BOLO.</b> In the rotation. "What next" pulls only from these.</p>
    <p><b>✗ COSMOLINE</b> (provisional). Packed for storage the way Marines pack a rifle in cosmoline grease: out of the rotation, kept whole, ready to unpack. It stays on BOLO.md; it just stops coming up.</p>
    <p>Bench for the X word: COSMOLINE (rec) · MOTHBALL · FOOTLOCKER · DEADLINE. Say the one you want.</p>
    <p>Built {built} from the 10/13 sit rep's BOLO board. {n_live} of {len(items)} recs say live.</p>
  </div></details>
</header>
<div class="bar"><i class="l" id="barL" style="width:0%"></i><i class="c" id="barC" style="width:0%"></i></div>
<main class="wrap">
  <p class="lede">Every open BOLO, {len(items)} of them. Each row gives the mission, where it stands and the next step, then my rec. Press ✓ to keep it {"<button type='button' class='t'>live<span class='tip' role='tooltip'><b>Live BOLO</b>In the rotation. When we pick what to work on next, we pick from the live list only.</span></button>"} or ✗ to {"<button type='button' class='t'>cosmoline<span class='tip' role='tooltip'><b>Cosmoline</b>Out of the rotation and in storage. Still on BOLO.md, still whole, back on your word.</span></button>"} it. Press it again to undo. Add a note to any row: type it, or click the box and hold JUDY's talk key, and your words land there. <b>Take all recs</b> fills every row you have not called; BOLO 83 has no rec and stays yours.</p>
  <p id="noDb" hidden>Calls are not saving: the page could not reach its store. Your clicks show here but will not reach the CDR.</p>
  <div class="filters" role="group" aria-label="Show">
    <button type="button" data-f="all" aria-pressed="true">All {len(items)}</button>
    <button type="button" data-f="todo" aria-pressed="false">To call</button>
    <button type="button" data-f="live" aria-pressed="false">✓ Live</button>
    <button type="button" data-f="cosmo" aria-pressed="false">✗ Cosmoline</button>
    <button type="button" data-f="hot" aria-pressed="false">Hot</button>
    <button type="button" data-f="slow" aria-pressed="false">Held · gated · slow</button>
  </div>
  <div class="list" id="list">{''.join(items)}
  </div>
  <div class="empty" id="none" hidden>Nothing matches this filter.</div>
</main>
<script>
  let db = null, filter = "all"; const picks = {{}};
  const rows = Array.from(document.querySelectorAll(".b"));
  function render() {{
    let l = 0, c = 0, shown = 0;
    for (const el of rows) {{
      const p = (picks["b" + el.dataset.n] || {{}}).pick || "";
      el.classList.toggle("live", p === "live"); el.classList.toggle("cosmo", p === "cosmo");
      el.querySelector(".y").setAttribute("aria-pressed", p === "live"); el.querySelector(".x").setAttribute("aria-pressed", p === "cosmo");
      const ta = el.querySelector(".bnote textarea"), nt = (picks["b" + el.dataset.n] || {{}}).note || "";
      if (ta && document.activeElement !== ta && ta.value !== nt) {{ ta.value = nt; ta.classList.toggle("has", !!nt.trim()); ta.style.height = "auto"; ta.style.height = (ta.scrollHeight || 30) + "px"; }}
      if (p === "live") l++; else if (p === "cosmo") c++;
      const g = el.dataset.g;
      const vis = filter === "all" || (filter === "todo" && !p) || filter === p || (filter === "hot" && g === "hot") || (filter === "slow" && g !== "hot");
      el.hidden = !vis; if (vis) shown++;
    }}
    document.getElementById("nLive").textContent = l; document.getElementById("nCosmo").textContent = c; document.getElementById("nOpen").textContent = rows.length - l - c;
    document.getElementById("barL").style.width = (100 * l / rows.length) + "%"; document.getElementById("barC").style.width = (100 * c / rows.length) + "%";
    document.getElementById("none").hidden = shown > 0;
  }}
  async function put(n, patch) {{
    const id = "b" + n;
    picks[id] = Object.assign({{ n: +n, pick: "", note: "" }}, picks[id] || {{}}, patch);
    render();
    if (!db) return;
    const st = document.getElementById("saveState"); st.textContent = "saving…";
    try {{ await db.collection("picks").doc(id).set(picks[id]); st.textContent = "saved"; }}
    catch (e) {{ st.textContent = "not saved: " + (e && e.code || "error"); }}
  }}
  async function save(n, pick) {{ const cur = (picks["b" + n] || {{}}).pick; return put(n, {{ pick: cur === pick ? "" : pick }}); }}
  /* notes (10/13, Chief: "be able to add notes to it ... my voice notes"): typed, or JUDY's dictation pasted into the
     focused box; saved a moment after the typing or the paste stops */
  const timers = {{}};
  document.addEventListener("input", (ev) => {{
    const ta = ev.target.closest(".bnote textarea"); if (!ta) return;
    const n = ta.closest(".b").dataset.n;
    ta.classList.toggle("has", !!ta.value.trim());
    ta.style.height = "auto"; ta.style.height = ta.scrollHeight + "px";
    clearTimeout(timers[n]); timers[n] = setTimeout(() => put(n, {{ note: ta.value }}), 700);
  }});
  document.addEventListener("click", async (ev) => {{
    const t = ev.target.closest(".t");
    document.querySelectorAll(".t.pin").forEach((x) => {{ if (x !== t) x.classList.remove("pin"); }});
    if (t) t.classList.toggle("pin");
    const b = ev.target.closest(".yn button");
    if (b) save(b.closest(".b").dataset.n, b.dataset.p);
    const f = ev.target.closest(".filters button");
    if (f) {{ filter = f.dataset.f; document.querySelectorAll(".filters button").forEach((x) => x.setAttribute("aria-pressed", x === f)); render(); }}
    if (ev.target.id === "takeRecs") {{
      const st = document.getElementById("saveState");
      for (const el of rows) {{ const r = el.dataset.rec, id = "b" + el.dataset.n;
        if ((r === "live" || r === "cosmo") && !(picks[id] && picks[id].pick)) await save(el.dataset.n, r); }}
      st.textContent = "recs taken";
    }}
  }});
  document.addEventListener("keydown", (ev) => {{ if (ev.key === "Escape") document.querySelectorAll(".t.pin").forEach((x) => x.classList.remove("pin")); }});
  render();
  (async () => {{
    db = window.claude && window.claude.use ? await window.claude.use("db") : null;
    const st = document.getElementById("saveState");
    if (!db) {{ document.getElementById("noDb").hidden = false; st.textContent = "view only"; return; }}
    db.collection("picks").onSnapshot((snap) => {{
      for (const d of snap.docs) picks[d.id] = d.data();
      st.textContent = "calls loaded"; render();
    }}, () => {{ st.textContent = "calls unavailable"; }});
  }})();
</script>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT} · {len(items)} BOLOs · {n_live} recs live · {sum(1 for v in recs.values() if v[0]=='cosmo')} cosmo · {sum(1 for v in recs.values() if v[0]=='-')} no rec")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
