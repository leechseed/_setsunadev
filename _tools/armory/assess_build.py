"""BOLO 155 · the Armory assessment glass. DVA (.claude/agents/dva.md) reads the Armory data and writes
assessment.json; this script builds the page from it, with a codec call in the corner (16-bit, green, scanlines).

  python _tools/armory/assess_build.py

Writes two pages from one template:
  _PRIVATE/reference/armory/assessment.html        the published glass: the codec shows DVA as a pixel silhouette
  _PRIVATE/reference/armory/assessment.local.html  Chief's local copy: the codec plays codec.gif from the same folder
"""
import base64, html, io, json, os
from datetime import datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DIR = os.path.join(ROOT, "_PRIVATE", "reference", "armory")


def e(s):
    return html.escape(str(s), quote=True)


def build(a, codec_src, out):
    sev = {"high": 0, "medium": 1, "low": 2}
    findings = "".join(
        f'<article class="find {e(f.get("severity", "low"))}"><header><span class="fid">{e(f["id"])}</span><b>{e(f["title"])}</b>'
        f'<span class="sev">{e(f.get("severity", ""))}</span></header><p class="big">{e(f.get("number", ""))}</p><p>{e(f["says"])}</p></article>'
        for f in sorted(a.get("findings", []), key=lambda f: sev.get(f.get("severity"), 3)))
    methods = "".join(
        f'<tr><td class="rk">{e(m.get("rank", ""))}</td><th scope="row">{e(m["title"])}<small>for {e(", ".join(m.get("for", [])))}</small></th>'
        f'<td>{e(m["change"])}<div class="paths">{"".join(f"<code>{e(t)}</code>" for t in m.get("touches", []))}</div></td>'
        f'<td><span class="eff e{e(m.get("effort", ""))}">{e(m.get("effort", ""))}</span></td><td><code class="proof">{e(m.get("proof", ""))}</code></td></tr>'
        for m in sorted(a.get("methods", []), key=lambda m: m.get("rank", 99)))
    agents = "".join(
        f'<tr><th scope="row">{e(g["name"])}</th><td class="num">{e(g.get("deployments", ""))}</td><td>{e(g.get("model", ""))}</td>'
        f'<td>{e(g.get("job", ""))}<small>{e("; ".join(g.get("from_briefs", [])))}</small></td></tr>' for g in a.get("agents_to_name", []))
    shelf = a.get("shelf", {})
    score = "".join(   # the rescore (10/18): before, now, target per metric
        f'<tr><th scope="row">{e(r.get("metric", ""))}</th><td>{e(r.get("before", ""))}</td><td class="now">{e(r.get("now", ""))}</td>'
        f'<td>{e(r.get("target", ""))}</td><td><small>{e(r.get("note", ""))}</small></td></tr>' for r in a.get("scoreboard", []))

    def chips(xs):
        return "".join(f'<li>{e(" + ".join(x) if isinstance(x, list) else x)}</li>' for x in xs) or "<li class=\"none\">none</li>"
    now = datetime.now()
    page = PAGE
    for k, v in {
        "HEADLINE": e(a.get("headline", "")), "WINDOW": e(a.get("window", "")), "FINDINGS": findings, "METHODS": methods,
        "AGENTS": agents or '<tr><td colspan="4">none</td></tr>', "KEEP": chips(shelf.get("keep", [])), "FIX": chips(shelf.get("fix", [])),
        "MERGE": chips(shelf.get("merge", [])), "CUT": chips(shelf.get("cut", [])), "SHELFWHY": e(shelf.get("why", "")),
        "DVA": e(a.get("dva_says", "")), "SCORE": score or '<tr><td colspan="5">no scoreboard yet</td></tr>', "CODEC_SRC": codec_src,
        "WHEN": f"{now.month}/{now.day} {now.strftime('%I:%M %p').lstrip('0')}",
        "NF": str(len(a.get("findings", []))), "NM": str(len(a.get("methods", []))),
    }.items():
        page = page.replace("{{" + k + "}}", v)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    return out


PAGE = """<title>DVA's Assessment</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&family=Press+Start+2P&display=swap">
<style>
  /* the Command look, DARK only (ruled 9/11) · the read first, findings as a grid, the methods ranked, the codec call pinned bottom-right */
  :root { color-scheme: dark;
    --bg:#121110; --panel:#1B1A18; --panel-2:#24221F; --line:#34312C; --ink:#ECE7DF; --ink-2:#B7B0A5; --ink-3:#7F786E;
    --accent:#FF5A1F; --accent-soft:#3A1D10; --accent-ink:#FFB08F; --good:#5FBF8A; --good-soft:#16301F; --warn:#E3B341; --warn-soft:#3A2E10; --bad:#E5604D; --bad-soft:#3A1612;
    --codec:#7CFF6B; --codec-dim:#1E4A1A; --codec-bg:#06140A;
    --display:"Barlow Condensed","Arial Narrow",Arial,sans-serif; --body:"Atkinson Hyperlegible","Segoe UI",Verdana,sans-serif; --mono:"IBM Plex Mono",Consolas,monospace; --pixel:"Press Start 2P","IBM Plex Mono",monospace; }
  *{box-sizing:border-box} html,body{background:var(--bg);color:var(--ink)}
  body{font:15px/1.5 var(--body);padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:0 280px}
  body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:10;background:var(--panel)}
  :focus-visible{outline:2px solid var(--accent);outline-offset:2px}
  .strip{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;display:flex;align-items:center;gap:12px;flex-wrap:wrap;min-height:44px;margin-inline:-16px;padding:6px 16px;background:var(--panel);border-bottom:1px solid var(--line)}
  .strip h1{margin:0;font:800 20px/1 var(--display);letter-spacing:.06em;text-transform:uppercase} .strip h1 b{color:var(--accent)}
  .chip{font:500 11px/1 var(--mono);letter-spacing:.08em;text-transform:uppercase;padding:4px 7px;border:1px solid var(--line);border-radius:3px;color:var(--ink-2)}
  .spacer{flex:1}
  .wrap{max-width:1080px;margin:0 auto;display:grid;gap:18px;padding-block:18px}
  .read{border-left:4px solid var(--accent);padding:6px 0 6px 14px} .read h2{margin:0;font:700 30px/1.15 var(--display);text-wrap:balance}
  .read p{margin:6px 0 0;font:13px var(--mono);color:var(--ink-3)}
  section{background:var(--panel);border:1px solid var(--line);border-radius:6px;padding:0 0 14px;min-width:0}
  section>h2{margin:0 0 12px;padding:10px 14px;font:700 18px var(--display);letter-spacing:.06em;text-transform:uppercase;border-bottom:1px solid var(--line);display:flex;gap:10px;align-items:center}
  section>h2 .s{margin-left:auto;font:400 13px var(--mono);color:var(--ink-2);text-transform:none;letter-spacing:0}
  .finds{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px;margin:0 14px}
  .find{background:var(--panel-2);border:1px solid var(--line);border-top:3px solid var(--ink-3);border-radius:4px;padding:10px 12px;min-width:0}
  .find.high{border-top-color:var(--bad)} .find.medium{border-top-color:var(--warn)} .find.low{border-top-color:var(--good)}
  .find header{display:flex;gap:8px;align-items:baseline} .find b{font:700 17px var(--display);letter-spacing:.02em}
  .fid{font:500 11px var(--mono);color:var(--ink-3)} .sev{margin-left:auto;font:500 10px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3)}
  .find.high .sev{color:var(--bad)} .find.medium .sev{color:var(--warn)} .find.low .sev{color:var(--good)}
  .find .big{margin:6px 0 4px;font:800 26px/1.1 var(--display);color:var(--accent-ink);font-variant-numeric:tabular-nums} .find p{margin:0;font-size:14px;color:var(--ink-2)}
  .tbl{overflow-x:auto;margin:0 14px}
  table{width:100%;border-collapse:collapse;font-size:14px;min-width:720px}
  thead th{font:500 11px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);text-align:left;padding:6px 8px;border-bottom:1px solid var(--line)}
  tbody th{text-align:left;padding:8px;font:700 16px/1.2 var(--display);vertical-align:top;min-width:170px} tbody th small,tbody td small{display:block;font:11px var(--mono);color:var(--ink-3);margin-top:3px;font-weight:400}
  tbody td{padding:8px;vertical-align:top;color:var(--ink-2)} tbody tr{border-bottom:1px solid var(--line)} tbody tr:last-child{border:0}
  .rk{font:800 24px var(--display);color:var(--accent);width:36px} .num{text-align:right;font-variant-numeric:tabular-nums}
  .paths{display:flex;flex-wrap:wrap;gap:4px;margin-top:6px} code{font:12px var(--mono);background:var(--bg);border:1px solid var(--line);border-radius:3px;padding:1px 5px;color:var(--ink-2);overflow-wrap:anywhere}
  .eff{font:700 12px var(--mono);padding:3px 7px;border-radius:3px} .eS{background:var(--good-soft);color:var(--good)} .eM{background:var(--warn-soft);color:var(--warn)} .eL{background:var(--bad-soft);color:var(--bad)}
  .shelf{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:0 14px}
  .shelf div{min-width:0} .shelf h3{margin:0 0 6px;font:700 15px var(--display);letter-spacing:.06em;text-transform:uppercase}
  .shelf ul{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:4px} .shelf li{font:12px var(--mono);padding:3px 7px;border-radius:3px;background:var(--panel-2)} .shelf li.none{color:var(--ink-3)}
  .k h3{color:var(--good)} .f h3{color:var(--warn)} .m h3{color:var(--accent-ink)} .c h3{color:var(--bad)}
  td.now{color:var(--accent-ink);font-weight:700}
  .why{margin:12px 14px 0;font-size:14px;color:var(--ink-2)}
  /* the codec call: 16-bit, phosphor green, scanlines; the subtitle box carries DVA's sign-off */
  .codec{position:fixed;right:max(12px,env(safe-area-inset-right,0px));bottom:max(12px,env(safe-area-inset-bottom,0px));z-index:30;width:200px;background:var(--codec-bg);border:2px solid var(--codec);border-radius:2px;box-shadow:0 0 0 2px #000,0 0 18px rgba(124,255,107,.35);font:8px/1.6 var(--pixel);color:var(--codec)}
  .codec .top{display:flex;justify-content:space-between;padding:4px 6px;border-bottom:2px solid var(--codec-dim)}
  .codec .scr{position:relative;height:256px;overflow:hidden;background:#000}
  .codec canvas{display:block;width:100%;height:100%;image-rendering:pixelated;filter:grayscale(1) sepia(1) hue-rotate(62deg) saturate(4) brightness(.95) contrast(1.25)}
  .codec .scr::after{content:"";position:absolute;inset:0;pointer-events:none;background:repeating-linear-gradient(0deg,rgba(0,0,0,.45) 0 1px,transparent 1px 3px);mix-blend-mode:multiply}
  .codec .scr::before{content:"";position:absolute;inset:0;pointer-events:none;z-index:1;background:radial-gradient(ellipse at center,transparent 55%,rgba(0,0,0,.7));}
  .codec .bars{display:flex;gap:2px;align-items:flex-end;height:14px;padding:0 6px 4px} .codec .bars i{flex:1;background:var(--codec);animation:bar 1.1s steps(4) infinite}
  .codec .bars i:nth-child(2){animation-delay:.2s} .codec .bars i:nth-child(3){animation-delay:.4s} .codec .bars i:nth-child(4){animation-delay:.1s} .codec .bars i:nth-child(5){animation-delay:.3s}
  @keyframes bar{0%{height:20%}50%{height:100%}100%{height:40%}}
  .codec .name{padding:4px 6px;border-top:2px solid var(--codec-dim);display:flex;justify-content:space-between}
  .sub{position:fixed;right:max(224px,calc(env(safe-area-inset-right,0px) + 224px));bottom:max(12px,env(safe-area-inset-bottom,0px));z-index:30;width:min(420px,calc(100vw - 260px));background:rgba(6,20,10,.94);border:2px solid var(--codec);padding:10px 12px;font:9px/1.9 var(--pixel);color:var(--codec);box-shadow:0 0 0 2px #000}
  .sub b{display:block;margin-bottom:4px;color:#fff}
  .codec .x{background:none;border:0;color:var(--codec);font:inherit;cursor:pointer;padding:0}
  .codec.min .scr,.codec.min .bars{display:none}
  @media (prefers-reduced-motion:reduce){.codec .bars i{animation:none;height:60%}}
  @media (max-width:720px){.shelf{grid-template-columns:repeat(2,minmax(0,1fr))}.sub{position:static;width:auto;margin:0 0 12px}.codec{width:150px}.codec .scr{height:190px}body{padding-block:0 240px}}
</style>
<header class="strip">
  <h1><b>DVA</b> · The Assessment</h1><span class="chip">BOLO 155</span><span class="chip">reads BOLO 154</span>
  <span class="spacer"></span>
  <span class="chip">{{NF}} findings · {{NM}} methods</span><span class="chip">as of {{WHEN}}</span>
</header>
<main class="wrap">
  <div class="read"><h2>{{HEADLINE}}</h2><p>{{WINDOW}}</p></div>
  <section><h2>The scoreboard<span class="s">before (DVA's first read, 10/17) · now · target</span></h2>
    <div class="tbl"><table><thead><tr><th scope="col">Metric</th><th scope="col">Before</th><th scope="col">Now</th><th scope="col">Target</th><th scope="col">Note</th></tr></thead><tbody>{{SCORE}}</tbody></table></div></section>
  <section><h2>What the data says<span class="s">red high · amber medium · green low</span></h2><div class="finds">{{FINDINGS}}</div></section>
  <section><h2>Methods to move forward<span class="s">ranked by payoff per effort</span></h2>
    <div class="tbl"><table><thead><tr><th scope="col">#</th><th scope="col">Move</th><th scope="col">The change</th><th scope="col">Effort</th><th scope="col">Proof</th></tr></thead><tbody>{{METHODS}}</tbody></table></div></section>
  <section><h2>Agents to name<span class="s">jobs the general-purpose type keeps doing</span></h2>
    <div class="tbl"><table><thead><tr><th scope="col">Name</th><th scope="col" class="num">Runs</th><th scope="col">Model</th><th scope="col">Job · briefs</th></tr></thead><tbody>{{AGENTS}}</tbody></table></div></section>
  <section><h2>The shelf<span class="s">never fired · DVA's sort</span></h2>
    <div class="shelf"><div class="k"><h3>Keep</h3><ul>{{KEEP}}</ul></div><div class="f"><h3>Fix</h3><ul>{{FIX}}</ul></div><div class="m"><h3>Merge</h3><ul>{{MERGE}}</ul></div><div class="c"><h3>Cut</h3><ul>{{CUT}}</ul></div></div>
    <p class="why">{{SHELFWHY}}</p></section>
</main>
<div class="sub" role="note"><b>DVA</b>{{DVA}}</div>
<aside class="codec" id="codec" aria-label="codec call from DVA">
  <div class="top"><span>PTT</span><span>140.85</span><button class="x" type="button" id="cx" aria-label="minimize the codec">_</button></div>
  <div class="scr"><canvas id="cv" width="64" height="112"></canvas></div>
  <div class="bars" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div>
  <div class="name"><span>DVA</span><span>MEMORY</span></div>
</aside>
{{CODEC_SRC}}
<script>
  // the codec: draw the source down to 64x112, the canvas upscales it pixelated; ~12 fps feels like the old codec
  (function () {
    const cv = document.getElementById("cv"), ctx = cv.getContext("2d"), src = document.getElementById("codec-src");
    ctx.imageSmoothingEnabled = false;
    let last = 0;
    function draw(t) {
      if (t - last > 80) {
        last = t;
        try {
          const iw = src.naturalWidth || 64, ih = src.naturalHeight || 112, s = Math.max(cv.width / iw, cv.height / ih);
          const w = iw * s, h = ih * s;
          ctx.fillStyle = "#000"; ctx.fillRect(0, 0, cv.width, cv.height);
          ctx.drawImage(src, (cv.width - w) / 2, (cv.height - h) / 2, w, h);
        } catch (err) { /* the source has not loaded yet */ }
      }
      requestAnimationFrame(draw);
    }
    requestAnimationFrame(draw);
    document.getElementById("cx").addEventListener("click", () => document.getElementById("codec").classList.toggle("min"));
  })();
</script>
"""


def main():
    a = json.load(io.open(os.path.join(DIR, "assessment.json"), encoding="utf-8"))
    svg = io.open(os.path.join(ROOT, "_tools", "brand", "judy-kick.svg"), "rb").read()
    published = f'<img id="codec-src" hidden alt="" src="data:image/svg+xml;base64,{base64.b64encode(svg).decode()}">'
    local = '<img id="codec-src" alt="" src="codec.gif" style="position:fixed;left:-9999px;top:0;width:320px">'   # kept in the DOM so the GIF animates
    print("wrote", build(a, published, os.path.join(DIR, "assessment.html")))
    print("wrote", build(a, local, os.path.join(DIR, "assessment.local.html")))


if __name__ == "__main__":
    main()
