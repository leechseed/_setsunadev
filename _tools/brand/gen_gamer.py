"""Generate JUDY's tab icon v2: an original gamer-girl action silhouette (headset, long hair, pistol arm out,
hand on hip, wide stance). Drawn from scratch from primitives; limbs are capsules (quad + round joints)."""
import math, sys

OUT = sys.argv[1]
O = "#FF5A1F"
shapes = []

def circle(cx, cy, r):
    shapes.append('<circle cx="%.2f" cy="%.2f" r="%.2f"/>' % (cx, cy, r))

def poly(pts):
    d = "M" + " L".join("%.2f %.2f" % p for p in pts) + " Z"
    shapes.append('<path d="%s"/>' % d)

def limb(pts, w0, w1=None):
    """capsule chain through pts, width tapering w0 -> w1"""
    w1 = w0 if w1 is None else w1
    n = len(pts) - 1
    for i in range(n):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        a = w0 + (w1 - w0) * i / n
        b = w0 + (w1 - w0) * (i + 1) / n
        dx, dy = x1 - x0, y1 - y0
        L = math.hypot(dx, dy) or 1
        nx, ny = -dy / L, dx / L
        poly([(x0 + nx * a / 2, y0 + ny * a / 2), (x1 + nx * b / 2, y1 + ny * b / 2),
              (x1 - nx * b / 2, y1 - ny * b / 2), (x0 - nx * a / 2, y0 - ny * a / 2)])
        circle(x0, y0, a / 2)
        circle(x1, y1, b / 2)

# long hair flowing back (drawn first, behind)
poly([(27, 9.4), (22, 9.8), (18.6, 13), (16, 19.5), (14, 27), (10.6, 35.5), (14.4, 33.6), (17.2, 29.5), (19.6, 24.5), (22.4, 20.5), (25, 17)])
# head
circle(26.5, 14.5, 5)
# headset: ear cup, two little antenna nubs, mic boom
circle(23.4, 15.2, 2.6)
limb([(22.2, 11.2), (20.6, 7.6)], 1.3, 1.0)
limb([(24.0, 10.4), (23.6, 6.6)], 1.3, 1.0)
limb([(24.2, 17.2), (29.0, 19.0)], 0.9)
# neck + torso (bust to the right, narrow waist, hips)
poly([(25, 18.5), (28.5, 18.5), (29, 21),
      (32.2, 22), (33.2, 25.2), (31.2, 27.5),
      (30, 31), (31.6, 35.5), (32.8, 40),
      (21.2, 40), (22.4, 35.5), (24, 31),
      (23, 26.5), (22.2, 22.5), (24.6, 21)])
# gun arm, straight out to the right, slightly raised
limb([(31, 22.8), (38.5, 21.6), (45, 20.2)], 3.0, 2.5)
# pistol: chunky body, barrel, grip
poly([(43.5, 16.8), (52.5, 16.8), (53.5, 18.2), (53.5, 20.2), (43.5, 20.2)])
poly([(53.5, 17.6), (57, 17.6), (57, 19.4), (53.5, 19.4)])
poly([(44.2, 20.2), (47.4, 20.2), (46.6, 24.8), (43.8, 24.8)])
# other arm: elbow out, hand on hip
limb([(23.2, 22.8), (17.6, 29.2), (22.6, 35)], 2.8, 2.3)
# legs: wide stance, front leg forward-right, back leg out-left
limb([(29.4, 38.5), (35.5, 47.5), (38.5, 56.5)], 6.0, 3.4)
limb([(24.6, 38.5), (20.4, 47.8), (16.6, 56.5)], 6.0, 3.4)
# boots
poly([(36.4, 55.2), (42.4, 56.4), (42.4, 58.4), (36.2, 58.4)])
poly([(18.6, 55.2), (12.6, 56.4), (12.6, 58.4), (18.8, 58.4)])

svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="JUDY">\n'
       '  <!-- JUDY tab icon v2, 10/17: an original gamer-girl action silhouette (headset, long hair, pistol out, hand on hip); drawn from scratch, nothing traced; generator: gen_gamer.py -->\n'
       '  <rect width="64" height="64" rx="14" fill="#121110"/>\n'
       '  <rect x="2" y="2" width="60" height="60" rx="12" fill="none" stroke="%s" stroke-width="3"/>\n'
       '  <g fill="%s">\n    %s\n  </g>\n</svg>\n') % (O, O, "\n    ".join(shapes))
open(OUT, "w", encoding="utf-8").write(svg)
print("wrote", OUT, len(shapes), "shapes")
