"""engineroom.py: the Engine Room (BOLO 180, phase 1, first slice: the gate meter). Ruled 11/4.

The Engine Room holds the whole Venture Engine (the ten SSOT systems). This slice serves the gate meter: how much of each
system is still open or parked before plotting can start (BOLO 100, systems first). Read-only; it writes nothing.

  python -X utf8 engineroom.py --json [--rows]   the gate as JSON (rows: every counted and dropped line)
  python -X utf8 engineroom.py --print           the gate as a table, once
  python -X utf8 engineroom.py serve [--port 8796]   the local page: http://127.0.0.1:8796/gate ; /api/gate
Verb: `command engineroom` (_tools/cmdtui/engineroom.go).
"""
import html
import json
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources  # noqa: E402

PORT = 8796


def clock12(iso):
    t = time.strptime(iso, "%Y-%m-%dT%H:%M:%S")
    return time.strftime("%I:%M %p", t).lstrip("0") + time.strftime(", %b %d", t).replace(" 0", " ")


def table(g):
    head = "%-4s %-14s %6s %7s %6s %9s %7s %8s" % ("#", "system", "open", "parked", "gate", "unmarked", "waived", "dropped")
    lines = [head, "-" * len(head)]
    for s in g["systems"]:
        lines.append("%-4s %-14s %6d %7d %6d %9d %7d %8d" % (s["id"], s["name"], s["open"], s["parked"], s["gate"],
                                                               s["unmarked"], s["waived"], s["dropped"]))
    t = g["totals"]
    lines.append("-" * len(head))
    lines.append("%-4s %-14s %6d %7d %6d %9d %7d %8d" % ("", "all ten", t["open"], t["parked"], t["gate"], t["unmarked"],
                                                       t["waived"], t["dropped"]))
    lines.append("plotting: " + ("UNLOCKED" if g["plotting_unlocked"] else "locked (gate %d)" % t["gate"]))
    return "\n".join(lines)


CSS = """
:root{--bg:#121315;--plate:#1a1c1f;--line:#2c2f34;--ink:#e9e6e1;--dim:#9a9690;--faint:#5b5853;--accent:#FF5A1F;--ok:#7fbf8e;color-scheme:dark}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 "IBM Plex Sans","Segoe UI",system-ui,sans-serif}
.strip{display:flex;align-items:center;gap:14px;flex-wrap:wrap;min-height:44px;padding:8px 16px;border-bottom:1px solid var(--line)}
.strip h1{margin:0;font:700 16px "Segoe UI",system-ui,sans-serif;letter-spacing:.1em;text-transform:uppercase}.strip h1 b{color:var(--accent)}
.strip .m{color:var(--dim);font-size:13px}.strip .lock{margin-left:auto;font-weight:700;letter-spacing:.06em}
main{padding:18px 16px 40px;max-width:1180px;margin:0 auto;display:grid;gap:16px}
.big{display:flex;gap:28px;flex-wrap:wrap;align-items:baseline}.big div{display:grid}.big span{color:var(--dim);font-size:12px;text-transform:uppercase;letter-spacing:.08em}
.big strong{font-size:34px;font-weight:600;font-variant-numeric:tabular-nums}.big .g strong{color:var(--accent)}
table{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}th,td{padding:7px 10px;border-bottom:1px solid var(--line);text-align:right}
th{color:var(--dim);font-weight:500;font-size:12px;text-transform:uppercase;letter-spacing:.08em}th:nth-child(-n+2),td:nth-child(-n+2){text-align:left}
td.gate{color:var(--accent);font-weight:700}td.zero{color:var(--ok)}
.bar{height:6px;background:var(--line);border-radius:3px;min-width:80px}.bar i{display:block;height:6px;border-radius:3px;background:var(--accent)}
details{background:var(--plate);border:1px solid var(--line);border-radius:6px;padding:10px 14px}summary{cursor:pointer;font-weight:600}
summary span{color:var(--dim);font-weight:400}ul{margin:8px 0 0;padding-left:0;list-style:none;display:grid;gap:4px}
li{font-size:13px;display:grid;grid-template-columns:5.5rem minmax(0,1fr);gap:8px}li code{color:var(--dim);font-size:12px;word-break:break-all}
li .k{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--accent)}li.drop .k{color:var(--faint)}li.drop{opacity:.6}
li.unm .k{color:var(--dim)}.note{color:var(--dim);font-size:13px;margin:0}
[title]{text-decoration:underline dotted var(--faint);text-underline-offset:3px}
"""


def page(g):
    t = g["totals"]
    mx = max([s["gate"] for s in g["systems"]] + [1])
    rows = []
    for s in g["systems"]:
        w = int(100 * s["gate"] / mx)
        rows.append("<tr><td>%s</td><td><a href='#s%s' style='color:inherit'>%s</a></td><td>%d</td><td>%d</td><td class='%s'>%d</td>"
                    "<td><div class='bar'><i style='width:%d%%'></i></div></td><td>%d</td><td>%d</td><td>%d</td></tr>" % (
                        s["id"], s["id"], html.escape(s["name"]), s["open"], s["parked"], "zero" if s["gate"] == 0 else "gate",
                        s["gate"], w, s["unmarked"], s["waived"], s["dropped"]))
    blocks = []
    for s in g["systems"]:
        items = []
        for r in s.get("rows", []):
            cls = "drop" if r["dropped"] else ("unm" if r["kind"] == "unmarked" else "")
            label = r["kind"] + (" · " + r["dropped"] if r["dropped"] else "") + (" · waived" if r["waived"] else "")
            items.append("<li class='%s'><span class='k'>%s</span><span>%s<br><code>%s:%d</code></span></li>" % (
                cls, html.escape(r["kind"]), html.escape(r["text"]), html.escape(r["file"]), r["line"]) if not r["dropped"] else
                "<li class='%s'><span class='k'>dropped</span><span>%s<br><code>%s:%d · %s</code></span></li>" % (
                cls, html.escape(r["text"]), html.escape(r["file"]), r["line"], html.escape(label)))
        blocks.append("<details id='s%s'><summary>%s %s <span>· gate %d · %d open · %d parked · %d unmarked · %d dropped</span></summary>"
                      "<ul>%s</ul></details>" % (s["id"], s["id"], html.escape(s["name"]), s["gate"], s["open"], s["parked"],
                                                  s["unmarked"], s["dropped"], "".join(items) or "<li>Nothing open.</li>"))
    lock = "<span class='lock' style='color:var(--ok)'>PLOTTING UNLOCKED</span>" if g["plotting_unlocked"] else \
        "<span class='lock' style='color:var(--accent)'>PLOTTING LOCKED · gate %d</span>" % t["gate"]
    return """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>The Engine Room · Gate</title><style>%s</style></head><body>
<header class="strip"><h1>The <b>Engine Room</b></h1><span class="m">The gate meter · counted %s · BOLO 100 systems first</span>%s</header>
<main>
<section class="big"><div class="g"><span title="Open plus parked, scrubbed, waivers out. Plotting unlocks at zero.">Gate</span><strong>%d</strong></div>
<div><span title="Formal OPEN markers on doc pages and in the system docs.">Open</span><strong>%d</strong></div>
<div><span title="Fields and rows carrying the parked marker.">Parked</span><strong>%d</strong></div>
<div><span title="Loose upper-case OPEN words. Shown apart; they do not count (ruled 11/4).">Unmarked</span><strong>%d</strong></div>
<div><span title="Template text, version history, legends and diagram lines the scrub removed.">Dropped</span><strong>%d</strong></div>
<div><span title="Rows Chief waived (waivers.json).">Waived</span><strong>%d</strong></div></section>
<table><thead><tr><th>#</th><th>System</th><th>Open</th><th>Parked</th><th>Gate</th><th></th><th>Unmarked</th><th>Waived</th><th>Dropped</th></tr></thead>
<tbody>%s</tbody></table>
<p class="note">Raw before the scrub: %d open, %d parked. Every row below shows its file and line. The page reads the repo each time it loads; refresh to recount.</p>
%s
</main></body></html>""" % (CSS, clock12(g["counted_at"]), lock, t["gate"], t["open"], t["parked"], t["unmarked"], t["dropped"],
                             t["waived"], "".join(rows), t["raw_open"], t["raw_parked"], "".join(blocks))


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype):
        b = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(b)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path in ("/", "/gate"):
            return self._send(200, page(sources.gate()), "text/html; charset=utf-8")
        if path == "/api/gate":
            rows = "rows=1" in self.path
            return self._send(200, json.dumps(sources.gate(with_rows=rows)), "application/json")
        if path == "/health":
            return self._send(200, json.dumps({"ok": True, "app": "engineroom", "port": PORT}), "application/json")
        self._send(404, json.dumps({"error": "no route " + path}), "application/json")

    def log_message(self, *a):
        pass


def main(argv):
    if "--json" in argv:
        print(json.dumps(sources.gate(with_rows="--rows" in argv), ensure_ascii=False))
        return 0
    if "--print" in argv:
        print(table(sources.gate(with_rows=False)))
        return 0
    if argv and argv[0] == "serve":
        port = int(argv[argv.index("--port") + 1]) if "--port" in argv else PORT
        srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
        print("the Engine Room on http://127.0.0.1:%d/gate" % port)
        srv.serve_forever()
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
