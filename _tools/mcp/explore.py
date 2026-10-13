"""explore.py - one SQL query on a COPY -> one DARK chart page (BOLO 140, Superset idea).

python _tools/mcp/explore.py <db> "<sql>" --chart bar|line|heatmap|treemap|table
       [--x col --y col --v col --title "..."] --out page.html
Reads _PRIVATE/dbcopies/<db>.sqlite read-only (mode=ro, query_only, SELECT-only guard, 5,000 rows max).
Inline SVG, no chart library. Rules: _tools/pages/TASTE.md section 6. heatmap: x, y, then --v (default 3rd col).
"""
import argparse
import datetime
import html
import os
import re
import sqlite3
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
COPIES = os.path.join(ROOT, "_PRIVATE", "dbcopies")
MAXROWS = 5000
FORBIDDEN = re.compile(r"\b(PRAGMA|ATTACH|DETACH|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|VACUUM|REPLACE)\b", re.I)
AC, GR, TX, MU = "#FF5A1F", "#5b5750", "#E9E6E1", "#8C877F"
e = html.escape


def run(db, sql):
    s = sql.strip().rstrip(";")
    if not re.match(r"(select|with)\b", s, re.I) or ";" in s or FORBIDDEN.search(s):
        sys.exit("refused: one SELECT / WITH...SELECT only")
    path = os.path.join(COPIES, db + ".sqlite")
    c = sqlite3.connect("file:" + path.replace("\\", "/") + "?mode=ro", uri=True)
    c.execute("PRAGMA query_only=1")
    cur = c.execute(s)
    cols = [d[0] for d in cur.description]
    rows = cur.fetchmany(MAXROWS)
    c.close()
    return cols, rows


def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def fmt(v):
    return "{:,.0f}".format(v) if abs(v - round(v)) < 1e-9 else "{:,.2f}".format(v)


def trunc(s, n):
    s = str(s)
    return s if len(s) <= n else s[:n - 1] + "…"


def bar(rows, xi, yi):
    data = sorted(((str(r[xi]), num(r[yi])) for r in rows), key=lambda t: -t[1])[:40]
    mx = max([v for _, v in data] + [1])
    rh, lw, W = 26, 230, 900
    h = rh * len(data) + 10
    out = ['<svg viewBox="0 0 %d %d" width="100%%" role="img">' % (W, h)]
    for i, (k, v) in enumerate(data):
        y = 5 + i * rh
        w = max(1, (W - lw - 90) * v / mx)
        col = AC if i == 0 else GR
        out.append('<text x="%d" y="%d" text-anchor="end" fill="%s" font-size="13">%s</text>' % (lw - 10, y + 17, TX, e(trunc(k, 32))))
        out.append('<rect class="m" x="%d" y="%d" width="%.1f" height="%d" fill="%s" rx="2"><title>%s: %s</title></rect>' % (lw, y + 3, w, rh - 8, col, e(k), fmt(v)))
        out.append('<text x="%.1f" y="%d" fill="%s" font-size="12">%s</text>' % (lw + w + 6, y + 17, AC if i == 0 else MU, fmt(v)))
    return "".join(out) + "</svg>"


def line(rows, xi, yi):
    pts = sorted(((str(r[xi]), num(r[yi])) for r in rows), key=lambda t: t[0])
    W, H, L, B, T = 900, 380, 60, 36, 20
    mx = max([v for _, v in pts] + [1])
    n = max(len(pts) - 1, 1)

    def X(i):
        return L + (W - L - 80) * i / n

    def Y(v):
        return H - B - (H - B - T) * v / (mx * 1.05)
    out = ['<svg viewBox="0 0 %d %d" width="100%%" role="img">' % (W, H)]
    for t in range(5):
        v = mx * t / 4
        out.append('<line x1="%d" x2="%d" y1="%.1f" y2="%.1f" stroke="#2C2A27"/><text x="%d" y="%.1f" text-anchor="end" fill="%s" font-size="11">%s</text>' % (L, W - 80, Y(v), Y(v), L - 6, Y(v) + 4, MU, fmt(v)))
    step = max(1, len(pts) // 10)
    for i, (k, _) in enumerate(pts):
        if i % step == 0 or i == len(pts) - 1:
            out.append('<text x="%.1f" y="%d" text-anchor="middle" fill="%s" font-size="11">%s</text>' % (X(i), H - 12, MU, e(trunc(k, 10))))
    d = " ".join("%s%.1f %.1f" % ("M" if i == 0 else "L", X(i), Y(v)) for i, (_, v) in enumerate(pts))
    out.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.2"/>' % (d, AC))
    pk = max(range(len(pts)), key=lambda i: pts[i][1])
    for i, (k, v) in enumerate(pts):
        out.append('<circle class="m" cx="%.1f" cy="%.1f" r="%d" fill="%s"><title>%s: %s</title></circle>' % (X(i), Y(v), 5 if i == pk else 3, AC if i == pk else GR, e(k), fmt(v)))
    out.append('<text x="%.1f" y="%.1f" text-anchor="middle" fill="%s" font-size="12">peak %s (%s)</text>' % (X(pk), Y(pts[pk][1]) - 10, AC, fmt(pts[pk][1]), e(pts[pk][0])))
    return "".join(out) + "</svg>"


def heat(rows, xi, yi, vi):
    xs = sorted({str(r[xi]) for r in rows})[:40]
    ys = sorted({str(r[yi]) for r in rows})[:30]
    val = {(str(r[xi]), str(r[yi])): num(r[vi]) for r in rows}
    mx = max(list(val.values()) + [1])
    cw, ch, L, T = 34, 24, 170, 70
    W, H = L + cw * len(xs) + 20, T + ch * len(ys) + 10
    out = ['<svg viewBox="0 0 %d %d" width="100%%" style="max-width:%dpx" role="img">' % (W, H, W)]
    for i, x in enumerate(xs):
        out.append('<text transform="translate(%d,%d) rotate(-50)" fill="%s" font-size="11">%s</text>' % (L + i * cw + cw / 2, T - 6, MU, e(trunc(x, 12))))
    for j, y in enumerate(ys):
        out.append('<text x="%d" y="%d" text-anchor="end" fill="%s" font-size="12">%s</text>' % (L - 8, T + j * ch + 16, TX, e(trunc(y, 24))))
        for i, x in enumerate(xs):
            v = val.get((x, y), 0)
            out.append('<rect class="m" x="%d" y="%d" width="%d" height="%d" fill="%s" fill-opacity="%.2f"><title>%s / %s: %s</title></rect>' % (L + i * cw + 1, T + j * ch + 1, cw - 2, ch - 2, AC, 0.06 + 0.94 * v / mx, e(x), e(y), fmt(v)))
    return "".join(out) + "</svg>"


def treemap(rows, xi, yi):
    data = sorted(((str(r[xi]), num(r[yi])) for r in rows if num(r[yi]) > 0), key=lambda t: -t[1])[:60]
    W, H = 900, 520
    out = ['<svg viewBox="0 0 %d %d" width="100%%" role="img">' % (W, H)]

    def lay(items, x, y, w, h):  # slice and dice, split at the half-weight point
        if not items:
            return
        if len(items) == 1:
            k, v = items[0]
            first = k == data[0][0]
            out.append('<g class="m"><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="#121110" stroke-width="2"><title>%s: %s</title></rect>' % (x, y, w, h, AC if first else GR, e(k), fmt(v)))
            if w > 70 and h > 30:
                out.append('<text x="%.1f" y="%.1f" fill="%s" font-size="12">%s</text><text x="%.1f" y="%.1f" fill="%s" font-size="11">%s</text>' % (x + 6, y + 16, "#121110" if first else TX, e(trunc(k, int(w / 7))), x + 6, y + 30, "#121110" if first else MU, fmt(v)))
            out.append("</g>")
            return
        t = sum(v for _, v in items)
        acc, cut = 0, 1
        for i, (_, v) in enumerate(items):
            acc += v
            if acc >= t / 2:
                cut = max(1, min(i + 1, len(items) - 1))
                break
        a, b = items[:cut], items[cut:]
        fa = sum(v for _, v in a) / t
        if w >= h:
            lay(a, x, y, w * fa, h)
            lay(b, x + w * fa, y, w * (1 - fa), h)
        else:
            lay(a, x, y, w, h * fa)
            lay(b, x, y + h * fa, w, h * (1 - fa))
    lay(data, 0, 0, W, H)
    return "".join(out) + "</svg>"


def table(cols, rows):
    nums = [all(isinstance(r[i], (int, float)) or r[i] is None for r in rows) for i in range(len(cols))]
    h = "".join("<th%s>%s</th>" % (' class="n"' if nums[i] else "", e(c)) for i, c in enumerate(cols))
    b = "".join("<tr>" + "".join("<td%s>%s</td>" % (' class="n"' if nums[i] else "", e(trunc("" if v is None else (fmt(v) if isinstance(v, (int, float)) else v), 80))) for i, v in enumerate(r)) + "</tr>" for r in rows[:500])
    return '<div class="tb"><table><tr>%s</tr>%s</table></div>' % (h, b)


PAGE = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>@T@</title>
<style>:root{--bg:#121110;--pan:#1B1A18;--ac:#FF5A1F;--tx:#E9E6E1;--mu:#8C877F;--ln:#2C2A27}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:14px 'Atkinson Hyperlegible',system-ui,sans-serif}
header{height:44px;display:flex;align-items:center;padding:0 16px;background:var(--pan);border-bottom:1px solid var(--ln);font:700 18px 'Barlow Condensed',system-ui;color:var(--ac);letter-spacing:.04em}
main{max-width:960px;margin:0 auto;padding:16px}h1{font:700 28px 'Barlow Condensed',system-ui;margin:8px 0 16px}
td.n,th.n{font-family:'IBM Plex Mono',monospace;font-variant-numeric:tabular-nums;text-align:right}
.m:hover{opacity:.7}.tb{overflow:auto;max-height:70vh}table{border-collapse:collapse;width:100%}th,td{padding:4px 10px;border-bottom:1px solid var(--ln);font-size:13px;text-align:left}th{color:var(--mu);position:sticky;top:0;background:var(--bg)}
footer{margin-top:16px;color:var(--mu);font:12px 'IBM Plex Mono',monospace}svg text{font-family:'IBM Plex Mono',monospace}</style></head>
<body><header>EXPLORE</header><main><h1>@T@</h1>@C@<footer>Source: @D@.sqlite copy &middot; @N@ rows &middot; as of @A@<br>@Q@</footer></main></body></html>"""


def main():
    p = argparse.ArgumentParser()
    p.add_argument("db")
    p.add_argument("sql")
    p.add_argument("--chart", default="table", choices=["bar", "line", "heatmap", "treemap", "table"])
    p.add_argument("--x")
    p.add_argument("--y")
    p.add_argument("--v")
    p.add_argument("--title")
    p.add_argument("--out", required=True)
    a = p.parse_args()
    cols, rows = run(a.db, a.sql)
    if not rows:
        sys.exit("query returned no rows")

    def ix(n, d):
        if n is None:
            return d
        if n not in cols:
            sys.exit("no column " + n)
        return cols.index(n)
    xi, yi = ix(a.x, 0), ix(a.y, 1 if len(cols) > 1 else 0)
    vi = ix(a.v, 2 if len(cols) > 2 else yi)
    body = {"bar": lambda: bar(rows, xi, yi), "line": lambda: line(rows, xi, yi),
            "heatmap": lambda: heat(rows, xi, yi, vi), "treemap": lambda: treemap(rows, xi, yi),
            "table": lambda: table(cols, rows)}[a.chart]()
    now = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p").replace(" 0", " ")
    rep = {"@T@": e(a.title or a.db + " query"), "@C@": body, "@D@": e(a.db), "@N@": str(len(rows)), "@A@": now, "@Q@": e(trunc(a.sql, 300))}
    page = PAGE
    for k, v in rep.items():
        page = page.replace(k, v)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(page)
    print("%s: %d rows -> %s" % (a.chart, len(rows), a.out))


if __name__ == "__main__":
    main()
