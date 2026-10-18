"""Render judy-pinup.svg's shapes with PIL (no cairosvg on the box). Mini SVG path parser: M L H V C Z (+ lowercase h l)."""
import re, sys
from PIL import Image, ImageDraw

SRC, OUT = sys.argv[1], sys.argv[2:]
svg = open(SRC, encoding="utf-8").read()
S = 16  # supersample: 64-unit viewBox -> 1024 px

def bez(p0, p1, p2, p3, n=24):
    return [tuple((1-t)**3*a + 3*(1-t)**2*t*b + 3*(1-t)*t**2*c + t**3*d for a, b, c, d in zip(p0, p1, p2, p3))
            for t in (i / n for i in range(1, n + 1))]

def path_pts(d):
    toks = re.findall(r"[MLHVCZmlhvcz]|-?\d*\.?\d+", d)
    pts, cur, cmd, i = [], (0.0, 0.0), None, 0
    def num():
        nonlocal i
        v = float(toks[i]); i += 1; return v
    while i < len(toks):
        if toks[i].isalpha():
            cmd = toks[i]; i += 1
            if cmd in "Zz":
                continue
        if cmd == "M": cur = (num(), num()); pts.append(cur); cmd = "L"
        elif cmd == "L": cur = (num(), num()); pts.append(cur)
        elif cmd == "l": cur = (cur[0] + num(), cur[1] + num()); pts.append(cur)
        elif cmd == "H": cur = (num(), cur[1]); pts.append(cur)
        elif cmd == "h": cur = (cur[0] + num(), cur[1]); pts.append(cur)
        elif cmd == "V": cur = (cur[0], num()); pts.append(cur)
        elif cmd == "C":
            p1 = (num(), num()); p2 = (num(), num()); p3 = (num(), num())
            pts += bez(cur, p1, p2, p3); cur = p3
        else:
            raise ValueError("unsupported command %r" % cmd)
    return pts

img = Image.new("RGBA", (64 * S, 64 * S), (0, 0, 0, 0))
dr = ImageDraw.Draw(img)
dr.rounded_rectangle([0, 0, 64 * S - 1, 64 * S - 1], radius=14 * S, fill="#121110")
dr.rounded_rectangle([0.5 * S, 0.5 * S, 63.5 * S, 63.5 * S], radius=13.5 * S, outline="#FF5A1F", width=3 * S)
fig = svg.split('<g fill="#FF5A1F">', 1)[1]
for cx, cy, r in re.findall(r'<circle cx="([\d.]+)" cy="([\d.]+)" r="([\d.]+)"', fig):
    cx, cy, r = float(cx) * S, float(cy) * S, float(r) * S
    dr.ellipse([cx - r, cy - r, cx + r, cy + r], fill="#FF5A1F")
for d in re.findall(r'<path d="([^"]+)"', fig, re.S):
    dr.polygon([(x * S, y * S) for x, y in path_pts(" ".join(d.split()))], fill="#FF5A1F")
for o in OUT:
    size = int(re.search(r"(\d+)\.png$", o).group(1)) if re.search(r"-(\d+)\.png$", o) else 512
    img.resize((size, size), Image.LANCZOS).save(o)
    print("wrote", o, size)
