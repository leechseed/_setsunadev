"""JUDY's tab icon v3 (Chief, 10/17): an original silhouette of the over-the-shoulder action pose
(turned away, glancing back, pistol at the viewer, back arm flung out, one knee kicked up).
Drawn from scratch from primitives, nothing traced. Render with render_icon.py."""
import math, sys

OUT = sys.argv[1]
O = "#FF5A1F"
shapes = []

def circle(cx, cy, r):
    shapes.append('<circle cx="%.2f" cy="%.2f" r="%.2f"/>' % (cx, cy, r))

def poly(pts):
    shapes.append('<path d="M%s Z"/>' % " L".join("%.2f %.2f" % p for p in pts))

def limb(pts, w0, w1=None):
    """capsule chain through pts, width tapering w0 -> w1"""
    w1 = w0 if w1 is None else w1
    n = len(pts) - 1
    for i in range(n):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        a = w0 + (w1 - w0) * i / n
        b = w0 + (w1 - w0) * (i + 1) / n
        L = math.hypot(x1 - x0, y1 - y0) or 1
        nx, ny = -(y1 - y0) / L, (x1 - x0) / L
        poly([(x0 + nx * a / 2, y0 + ny * a / 2), (x1 + nx * b / 2, y1 + ny * b / 2),
              (x1 - nx * b / 2, y1 - ny * b / 2), (x0 - nx * a / 2, y0 - ny * a / 2)])
        circle(x0, y0, a / 2)
        circle(x1, y1, b / 2)

# ponytail streaming out behind the head
poly([(47.5, 10.5), (52, 10), (56.5, 13), (58, 19), (54.5, 15.5), (50.5, 15)])
# head, glancing back over the shoulder, headset nub
circle(45, 13.5, 4.6)
circle(47.6, 14.6, 1.9)
# torso, leaning: broad shoulders up-right, a cinched waist, then the hips toward the viewer
poly([(41.6, 16.6), (49.6, 19.2), (49, 23.4), (45, 27), (41.6, 29.6), (40.4, 33.4),
      (30.4, 33), (33.4, 28.6), (36, 25.4), (37, 21.6)])
circle(34.4, 34.0, 7.2)                 # the hips
circle(31.0, 36.4, 5.0)
# back arm flung out to the left, open hand
limb([(39, 19.6), (28.6, 18.2), (18.5, 17.2)], 3.0, 2.3)
limb([(18.5, 17.2), (14.6, 14.4)], 1.2)
limb([(18.5, 17.2), (13.8, 16.6)], 1.2)
limb([(18.5, 17.2), (14.4, 19.4)], 1.2)
# gun arm reaching at the viewer, pistol foreshortened with the muzzle facing out
limb([(47.4, 21.4), (49.6, 25.4)], 3.2, 2.8)
limb([(48.6, 25.4), (58.4, 29.6)], 3.8, 3.2)    # the pistol body, angled at the viewer
limb([(51.4, 25.2), (57.6, 27.8)], 1.6)          # the slide
limb([(50.4, 27.6), (49.4, 32.2)], 2.6, 2.2)    # the grip
shapes.append('<circle cx="58.40" cy="29.60" r="0.90" fill="#121110"/>')   # muzzle
# the kicked-up leg: thigh out to the left, shin folding back under the hips
limb([(30.4, 37), (19.6, 39.6), (9.4, 41.6)], 8.0, 5.0)
limb([(9.4, 41.6), (22, 46.2), (35.6, 50)], 5.0, 3.4)
poly([(33.6, 47.6), (42.6, 49.4), (43.4, 52.6), (34.6, 53.2)])   # boot
# the standing leg, down and out to the lower left
limb([(29.4, 38.4), (22.8, 49), (17.6, 58)], 7.0, 3.8)
poly([(15.8, 56.2), (21.2, 57.2), (19.8, 60.4), (13.2, 60.4)])  # boot

svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="JUDY">\n'
       '  <!-- JUDY tab icon v3, 10/17: original over-the-shoulder action silhouette; drawn from scratch, nothing traced; generator: gen_kick.py -->\n'
       '  <rect width="64" height="64" rx="14" fill="#121110"/>\n'
       '  <rect x="2" y="2" width="60" height="60" rx="12" fill="none" stroke="%s" stroke-width="3"/>\n'
       '  <g fill="%s">\n    %s\n  </g>\n</svg>\n') % (O, O, "\n    ".join(shapes))
open(OUT, "w", encoding="utf-8").write(svg)
print("wrote", OUT, len(shapes), "shapes")
