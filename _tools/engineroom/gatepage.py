"""gatepage.py: the Engine Room's gate page, written for a person (Chief 11/4: "I don't even know what I'm looking at").
Plain words first, the picture second, the detail last. engineroom.py reloads this module on every request, so a change
here shows on the next refresh without restarting the server."""
import html
import math
import os
import re
import time

ABOUT = {
    "00": "The ground rules: how the engine decides what is true, the patch bay, the module registry.",
    "01": "Story shape: genre, the collision engine, the scale ladder, the story registry.",
    "02": "Characters: LEECHSEED, the twelve layers, Tori's and Anna's records.",
    "03": "Places: the setting system and how a place changes over time.",
    "04": "What happens: the fabula (the world clock), the plot system, the trope graph.",
    "05": "The world's parts: the worldbuilding system and its catalog.",
    "06": "What it means: the theme system.",
    "07": "How it reads: prose, document and page style.",
    "08": "Keeping track: the tracking files (OXO's lives here).",
    "09": "Running the work: project flow and the house standards.",
}
PARK = "⏸"


def esc(s):
    return html.escape(str(s))


def clock12(iso):
    t = time.strptime(iso, "%Y-%m-%dT%H:%M:%S")
    return time.strftime("%I:%M %p", t).lstrip("0")


def doc_name(path):
    base = os.path.basename(path)
    folder = os.path.basename(os.path.dirname(path))
    page = ""
    m = re.match(r"^\d-(\w[\w-]*)\.md$", base)
    if m:  # a doc page: _DOCS/<sys>/<doc>/2-reference.md
        page = " (" + m.group(1).replace("-", " ") + " page)"
        base = folder
    base = re.sub(r"\.md$", "", base)
    base = re.sub(r"^[^\w]+", "", base).strip()
    base = re.sub(r"^ssot[_ ]+\d\d[_ ]*", "", base, flags=re.I)
    base = base.replace("_", " ").strip()
    return (base[:1].upper() + base[1:] if base else os.path.basename(path)) + page


def plain(text, kind):
    """Turn one markdown / YAML line into a plain sentence: (title, note)."""
    t = text.strip()
    m = re.match(r"^[-*]?\s*([\w.\-\[\]]+):\s*(null|~|\"\"|''|\[\]|\{\})?\s*#\s*" + PARK + r"?\s*(.*)$", t)
    if m:  # a YAML field left empty
        note = m.group(3).strip()
        note = re.sub(r"\s*→\s*see\s+\S+", "", note)
        return m.group(1).replace("_", " "), "Empty, waiting on: " + (note or "a fill pass")
    m = re.match(r"^>\s*\*\*OPEN:\*\*\s*(.*)$", t)
    if m:
        return "Unanswered", clean(m.group(1))
    if t.startswith("|"):  # a table row
        cells = [clean(c) for c in t.strip("|").split("|")]
        cells = [c for c in cells if c and not set(c) <= set("-: ")]
        if cells:
            return cells[0][:80], " · ".join(cells[1:])[:240]
    return "", clean(t)[:280]


def clean(s):
    s = re.sub(r"\[\[[^\]]+\]\]", "", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = s.replace("**", "").replace("`", "").replace(PARK, "")
    s = re.sub(r"^#+\s*", "", s.strip())
    s = re.sub(r"^[-*]\s+", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip(" ·|")


def ring(systems):
    """The Ninestar ring as a small SVG: 00 in the middle, 01-09 around, each dot sized and lit by what is left."""
    S, C, R = 300, 150, 112
    mx = max([s["gate"] for s in systems] + [1])
    parts = ["<svg viewBox='0 0 300 300' role='img' aria-label='The ten systems, sized by how much is left'>",
             "<circle cx='150' cy='150' r='112' fill='none' stroke='var(--line)'/>"]
    pos = {}
    for s in systems:
        if s["id"] == "00":
            pos["00"] = (C, C)
        else:
            a = (-90 + (int(s["id"]) - 1) * 40) * math.pi / 180
            pos[s["id"]] = (C + R * math.cos(a), C + R * math.sin(a))
    for s in systems:
        if s["id"] != "00":
            x, y = pos[s["id"]]
            parts.append("<line x1='150' y1='150' x2='%.1f' y2='%.1f' stroke='var(--line)'/>" % (x, y))
    for s in systems:
        x, y = pos[s["id"]]
        r = 11 + 15 * math.sqrt(s["gate"] / mx)
        done = s["gate"] == 0
        parts.append("<a href='#s%s'><g class='dot'><title>%s %s: %d left</title>"
                     "<circle cx='%.1f' cy='%.1f' r='%.1f' fill='%s' stroke='%s' stroke-width='2'/>"
                     "<text x='%.1f' y='%.1f' text-anchor='middle' dominant-baseline='central' font-size='11' font-weight='700' fill='%s'>%s</text></g></a>" % (
                         s["id"], s["id"], esc(s["name"]), s["gate"], x, y, r,
                         "var(--okbg)" if done else "rgba(255,90,31,%.2f)" % (0.15 + 0.6 * s["gate"] / mx),
                         "var(--ok)" if done else "var(--accent)", x, y,
                         "var(--ink)", s["gate"] if not done else "✓"))
    parts.append("</svg>")
    return "".join(parts)


CSS = """
:root{--bg:#121315;--plate:#1a1c1f;--plate2:#202327;--line:#2c2f34;--ink:#ece9e4;--dim:#a29e98;--faint:#66625c;
--accent:#FF5A1F;--ok:#7fbf8e;--okbg:rgba(127,191,142,.18);color-scheme:dark}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 "Segoe UI",system-ui,sans-serif}
a{color:inherit}
.strip{display:flex;align-items:center;gap:12px;min-height:44px;padding:8px 20px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg);z-index:5}
.strip b{color:var(--accent)}.strip .t{font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:14px}
.strip .m{color:var(--dim);font-size:13px;margin-left:auto}
main{max-width:1100px;margin:0 auto;padding:22px 20px 60px;display:grid;gap:22px}
.hero{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(220px,300px);gap:24px;align-items:center}
@media(max-width:760px){.hero{grid-template-columns:1fr}}
.hero h1{font-size:30px;line-height:1.2;margin:0 0 10px;font-weight:600;text-wrap:balance}.hero h1 span{color:var(--accent)}
.hero p{margin:0 0 10px;color:var(--dim);max-width:60ch}.hero p strong{color:var(--ink)}
.lock{display:inline-flex;gap:8px;align-items:center;font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
padding:4px 12px;border-radius:999px;border:1px solid var(--accent);color:var(--accent)}.lock.open{border-color:var(--ok);color:var(--ok)}
.ring svg{width:100%;height:auto;display:block}.dot circle{transition:stroke-width .15s}.dot:hover circle{stroke-width:4}
.boxes{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:14px}
.box{background:var(--plate);border:1px solid var(--line);border-radius:8px;padding:14px 16px}
.box h2{margin:0 0 6px;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--dim);font-weight:600}
.box p{margin:0}.box.next{border-color:var(--accent)}.box.next h2{color:var(--accent)}
.legend{display:grid;gap:6px;margin:0;padding:0;list-style:none}.legend li{display:flex;gap:10px;align-items:baseline}
.chip{display:inline-block;font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:1px 8px;border-radius:999px;white-space:nowrap}
.chip.q{background:rgba(255,90,31,.15);color:var(--accent)}.chip.f{background:rgba(255,255,255,.07);color:var(--ink)}
h2.sec{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--dim);margin:6px 0 -8px;font-weight:600}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:12px}
details.card{background:var(--plate);border:1px solid var(--line);border-radius:8px}
details.card[open]{grid-column:1/-1;border-color:var(--faint)}
details.card>summary{list-style:none;cursor:pointer;padding:14px 16px;display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:4px 12px;align-items:center}
details.card>summary::-webkit-details-marker{display:none}
.num{font-size:12px;font-weight:700;color:var(--dim);font-family:Consolas,monospace}
.nm{font-weight:600;font-size:16px}.left{font-size:26px;font-weight:600;font-variant-numeric:tabular-nums;color:var(--accent);text-align:right;line-height:1}
.left small{display:block;font-size:11px;color:var(--dim);font-weight:500;letter-spacing:.06em;text-transform:uppercase}
.left.done{color:var(--ok)}.about{grid-column:2/4;color:var(--dim);font-size:13px}
.split{grid-column:2/4;display:flex;gap:8px;flex-wrap:wrap}
.bar{grid-column:1/-1;height:4px;background:var(--line);border-radius:2px;overflow:hidden}.bar i{display:block;height:4px;background:var(--accent)}
.inside{padding:0 16px 16px;display:grid;gap:12px}
.file{background:var(--plate2);border-radius:6px;padding:10px 12px}
.file h3{margin:0 0 6px;font-size:14px;font-weight:600;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.file h3 span{color:var(--dim);font-weight:400;font-size:12px}
.items{margin:0;padding:0;list-style:none;display:grid;gap:6px}
.items li{display:grid;grid-template-columns:auto minmax(0,1fr);gap:10px;align-items:baseline;font-size:14px}
.items .w{color:var(--faint);font-size:12px;font-family:Consolas,monospace}
.items .ti{font-weight:600}.more{color:var(--dim);font-size:13px}
details.behind{background:transparent;border:1px dashed var(--line);border-radius:8px;padding:10px 16px;color:var(--dim)}
details.behind summary{cursor:pointer}details.behind table{width:100%;border-collapse:collapse;margin-top:10px;font-size:13px;font-variant-numeric:tabular-nums}
details.behind td,details.behind th{padding:5px 8px;border-bottom:1px solid var(--line);text-align:right}
details.behind td:first-child,details.behind th:first-child{text-align:left}
"""


def card(s, maxgate):
    rows = [r for r in s.get("rows", []) if not r["dropped"] and not r["waived"] and r["kind"] in ("open", "parked")]
    by_file = {}
    for r in rows:
        by_file.setdefault(r["file"], []).append(r)
    files = sorted(by_file.items(), key=lambda kv: -len(kv[1]))
    inner = []
    for f, items in files:
        q = sum(1 for r in items if r["kind"] == "open")
        e = len(items) - q
        li = []
        for r in items[:25]:
            title, note = plain(r["text"], r["kind"])
            chip = "<span class='chip q'>question</span>" if r["kind"] == "open" else "<span class='chip f'>empty</span>"
            li.append("<li>%s<span>%s%s <span class='w'>line %d</span></span></li>" % (
                chip, ("<span class='ti'>%s</span> · " % esc(title)) if title else "", esc(note), r["line"]))
        more = "<p class='more'>…and %d more in this file.</p>" % (len(items) - 25) if len(items) > 25 else ""
        parts = []
        if q:
            parts.append("%d question%s" % (q, "" if q == 1 else "s"))
        if e:
            parts.append("%d empty field%s" % (e, "" if e == 1 else "s"))
        inner.append("<div class='file'><h3>%s <span>%s · %s</span></h3><ul class='items'>%s</ul>%s</div>" % (
            esc(doc_name(f)), " · ".join(parts), esc(f), "".join(li), more))
    w = int(100 * s["gate"] / maxgate) if maxgate else 0
    done = s["gate"] == 0
    return ("<details class='card' id='s%s'><summary><span class='num'>%s</span><span class='nm'>%s</span>"
            "<span class='left%s'>%s<small>%s</small></span><span class='about'>%s</span>"
            "<span class='split'><span class='chip q'>%d questions</span><span class='chip f'>%d empty fields</span></span>"
            "<span class='bar'><i style='width:%d%%'></i></span></summary><div class='inside'>%s</div></details>") % (
        s["id"], s["id"], esc(s["name"]), " done" if done else "", "✓" if done else s["gate"], "all clear" if done else "left",
        esc(ABOUT.get(s["id"], "")), s["open"], s["parked"], w,
        "".join(inner) or "<p class='more'>Nothing left here.</p>")


def page(g):
    t = g["totals"]
    systems = g["systems"]
    order = sorted(systems, key=lambda s: -s["gate"])
    top = order[0] if order and order[0]["gate"] else None
    maxgate = max([s["gate"] for s in systems] + [1])
    clear = sum(1 for s in systems if s["gate"] == 0)
    lock = "<span class='lock open'>Plotting unlocked</span>" if g["plotting_unlocked"] else "<span class='lock'>Plotting locked</span>"
    nxt = ("Start with <strong>%s</strong>: %d left. Open its card below; each line says what is missing and where it lives." % (
        esc(top["name"]), top["gate"])) if top else "Everything is answered. Plotting can start."
    behind = "".join("<tr><td>%s %s</td><td>%d</td><td>%d</td><td>%d</td><td>%d</td></tr>" % (
        s["id"], esc(s["name"]), s["unmarked"], s["dropped"], s["waived"], s["raw_open"] + s["raw_parked"]) for s in systems)
    return """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Engine Room</title><style>%s</style></head><body>
<header class="strip"><span class="t">The <b>Engine Room</b></span><span class="m">Counted at %s · refresh to recount</span></header>
<main>
<section class="hero">
  <div>
    %s
    <h1><span>%d</span> blanks left before you can plot OXO</h1>
    <p>The Venture Engine is your ten story systems. This page counts every blank still in them: a <strong>question</strong> nobody has answered yet, or an <strong>empty field</strong> left for later. You set the rule on 10/4: every system done before any plotting (BOLO 100).</p>
    <p><strong>%d of 10</strong> systems are clear. The biggest dot on the ring has the most left.</p>
  </div>
  <div class="ring">%s</div>
</section>

<section class="boxes">
  <div class="box next"><h2>What to do next</h2><p>%s</p></div>
  <div class="box"><h2>How to read a card</h2><ul class="legend">
    <li><span class="chip q">question</span><span>A decision only you can make. Usually one line.</span></li>
    <li><span class="chip f">empty</span><span>A field on a character, place or event that has no value yet.</span></li>
    <li><span style="color:var(--accent);font-weight:700">129</span><span>How many blanks that system still has.</span></li>
  </ul></div>
  <div class="box"><h2>How a blank goes away</h2><p>You answer it in chat (or skip it). An agent writes the answer into the doc, and this count drops on the next refresh. Answer cards right on this page come in phase 2.</p></div>
</section>

<h2 class="sec">The ten systems, most left first</h2>
<section class="cards">%s</section>

<details class="behind"><summary>Behind the scenes: what the count leaves out</summary>
<p>Loose mentions use the word OPEN without the formal marker; you ruled they don't count (11/4). Ignored lines are templates, version history, marker legends and diagrams. Skipped means you waived it. Raw is everything before that cleanup.</p>
<table><thead><tr><th>System</th><th>Loose mentions</th><th>Ignored</th><th>Skipped</th><th>Raw</th></tr></thead><tbody>%s</tbody></table>
</details>
</main></body></html>""" % (CSS, clock12(g["counted_at"]), lock, t["gate"], clear, ring(systems), nxt,
                             "".join(card(s, maxgate) for s in order), behind)
