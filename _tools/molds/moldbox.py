"""Mold boxes for casting off a real object (BOLO 133, Chief 10/12: "use some sort of thing to conform around a real bottle").

Usage:
  python _tools/molds/moldbox.py slimcan            # a preset (slimcan · can12 · tallcan · bottle)
  python _tools/molds/moldbox.py custom 53 134      # any round object: diameter mm, height mm
  options: --wall 10 (silicone thickness around the object, mm) · --out <folder>

Zero tokens. Writes two STL files to print on the Kobra S1 (PETG or PLA, 0.2 mm layers, no supports):
  <name>_base.stl    a base plate with a locating ring; the object stands upside down inside the ring
  <name>_sleeve.stl  a tube that sits on the base around the object, 1.5 degrees of draft so the cured block slides out
Pour mold silicone in until it covers the object by `wall` mm. Cure, lift the sleeve, pull the object out of the block.
Prints the volume of mold silicone the pour needs. The shapes are solids of revolution, so every round object works.
"""
import math, os, struct, sys

PRESETS = {                     # diameter mm, height mm (measure yours: real containers vary by brand)
    "slimcan": (53, 134),       # 250 ml slim energy can
    "can12": (66, 122),         # 12 oz standard can
    "tallcan": (66, 168),       # 16 oz tall can
    "bottle": (61, 230),        # 12 oz long-neck beer bottle (body diameter)
}
SEG = 96                        # facets around the circle
SLEEVE_T, BASE_T, RING_H, RING_W, FIT, DRAFT = 3.0, 4.0, 4.0, 2.4, 0.4, 1.5


def revolve(profile):
    """Turn a closed (r, z) outline into STL triangles around the z axis."""
    tris = []
    ring = [(math.cos(2 * math.pi * k / SEG), math.sin(2 * math.pi * k / SEG)) for k in range(SEG)]
    for i in range(len(profile)):
        (r1, z1), (r2, z2) = profile[i], profile[(i + 1) % len(profile)]
        for k in range(SEG):
            (c1, s1), (c2, s2) = ring[k], ring[(k + 1) % SEG]
            a, b = (r1 * c1, r1 * s1, z1), (r2 * c1, r2 * s1, z2)
            c, d = (r2 * c2, r2 * s2, z2), (r1 * c2, r1 * s2, z1)
            if r1 or r2:
                tris += [(a, b, c), (a, c, d)]
    return [t for t in tris if len({t[0], t[1], t[2]}) == 3]


def write_stl(path, tris):
    with open(path, "wb") as f:
        f.write(b"moldbox".ljust(80, b" ") + struct.pack("<I", len(tris)))
        for a, b, c in tris:
            u = [b[i] - a[i] for i in range(3)]
            v = [c[i] - a[i] for i in range(3)]
            n = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
            L = math.sqrt(sum(x * x for x in n)) or 1.0
            f.write(struct.pack("<12fH", *(x / L for x in n), *a, *b, *c, 0))


def build(name, dia, height, wall, out):
    r_obj = dia / 2.0
    r_in = r_obj + wall                               # inner radius of the sleeve at the bottom
    h = height + wall + 6                             # sleeve height: object + cover + a little freeboard
    r_in_top = r_in + h * math.tan(math.radians(DRAFT))
    r_base = r_in_top + SLEEVE_T + 8
    # base plate with a locating ring for the object, and a shallow seat for the sleeve
    ring_in, ring_out = r_obj + FIT, r_obj + FIT + RING_W
    base = [(0, 0), (r_base, 0), (r_base, BASE_T), (r_in + SLEEVE_T + FIT, BASE_T), (r_in + SLEEVE_T + FIT, BASE_T - 1.5),
            (r_in - FIT, BASE_T - 1.5), (r_in - FIT, BASE_T), (ring_out, BASE_T), (ring_out, BASE_T + RING_H),
            (ring_in, BASE_T + RING_H), (ring_in, BASE_T), (0, BASE_T)]
    sleeve = [(r_in, 0), (r_in + SLEEVE_T, 0), (r_in_top + SLEEVE_T, h), (r_in_top, h)]
    os.makedirs(out, exist_ok=True)
    write_stl(os.path.join(out, name + "_base.stl"), revolve(base[::-1]))
    write_stl(os.path.join(out, name + "_sleeve.stl"), revolve(sleeve[::-1]))
    fill = height + wall                              # silicone depth inside the sleeve
    r_mid = r_in + fill / 2 * math.tan(math.radians(DRAFT))
    vol_ml = (math.pi * r_mid ** 2 * fill - math.pi * r_obj ** 2 * height) / 1000.0
    print("MOLDBOX %s: object %g x %g mm · wall %g mm · sleeve %.0f mm tall, %.0f mm wide · base %.0f mm wide" % (
        name, dia, height, wall, h, 2 * (r_in_top + SLEEVE_T), 2 * r_base))
    print("  mold silicone: about %.0f ml (~%.0f g at 1.1 g/ml) -> %s" % (vol_ml, vol_ml * 1.1, out))


if __name__ == "__main__":
    a = sys.argv[1:]
    wall = float(a[a.index("--wall") + 1]) if "--wall" in a else 10.0
    out = a[a.index("--out") + 1] if "--out" in a else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "..", "_PRIVATE", "orange", "molds")
    if a and a[0] == "custom":
        build("custom_%sx%s" % (a[1], a[2]), float(a[1]), float(a[2]), wall, out)
    else:
        for name in ([a[0]] if a and a[0] in PRESETS else PRESETS):
            build(name, *PRESETS[name], wall, out)
