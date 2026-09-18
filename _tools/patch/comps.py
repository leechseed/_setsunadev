# -*- coding: utf-8 -*-
"""BOLO 72 v0.2 — the composition sheet: the Hand and the girl on the strings.

Chief's re-direction 9/18: v0.1 binned. The bunny, the horse and the ghost are gone. The patch is now
a giant white glove hand (the Super Smash Master Hand read) coming down from above with puppet strings
straight down to a thick, muscular woman who hangs from them and fights them. Who's controlling who.
Golden-ratio split (the hand takes the major share), the two set at an angle to each other.

This sheet is value-blocked thumbnails, not finished art: black silhouette for her, white for the hand,
gold for the strings, the field in BVX rose. Six poses; Chief picks; the pick goes to a posed 3D
reference (the Blender studio) and then a painted pass.

Usage:  python _tools/patch/comps.py     writes comps.html beside this script
"""
import io, os, math, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from patch import T, P, CX, CY, R   # threads + the patch circle helpers from v0.1

PHI = 0.618
GOLD_Y = 200 + 600 * (1 - PHI)     # the golden section across the field, from the top
GOLD_X = 200 + 600 * PHI


# ---------------------------------------------------------------- geometry helpers ----
def add(a, b): return (a[0] + b[0], a[1] + b[1])
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def mul(a, k): return (a[0] * k, a[1] * k)
def lerp(a, b, t): return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
def norm(a):
    L = math.hypot(*a) or 1.0
    return (a[0] / L, a[1] / L)
def f(p): return "%.1f %.1f" % p


def capsule(p1, p2, r1, r2):
    """A tapered limb: the hull of two circles."""
    d = norm(sub(p2, p1)); n = (-d[1], d[0])
    a, b = add(p1, mul(n, r1)), add(p2, mul(n, r2))
    c, e = sub(p2, mul(n, r2)), sub(p1, mul(n, r1))
    return "M %s L %s A %s %s 0 0 0 %s L %s A %s %s 0 0 0 %s Z" % (f(a), f(b), r2, r2, f(c), f(e), r1, r1, f(a))


def torso(sl, sr, hl, hr, waist=0.58):
    """Shoulders to hips with a waist pulled in; the glutes bulge below the hip line."""
    ms, mh = lerp(sl, sr, .5), lerp(hl, hr, .5)
    w = lerp(ms, mh, .55)
    wl = add(w, mul(sub(lerp(sl, hl, .55), w), waist * .55))
    wr = add(w, mul(sub(lerp(sr, hr, .55), w), waist * .55))
    down = norm(sub(mh, ms))
    return ("M %s Q %s %s Q %s %s Q %s %s Q %s %s Z"
            % (f(sl), f(wl), f(hl), f(add(mh, mul(down, 34))), f(hr), f(wr), f(sr), f(sub(ms, mul(down, 10))), f(sl)))


class Figure:
    """A thick, strong woman as a silhouette, posed by joints. All parts one thread (black)."""
    def __init__(self, J, hair=(0, 1), foot=(1, 0)):
        self.J, self.hair, self.foot = J, hair, foot

    def paths(self):
        J = self.J; out = []
        S = lambda d: out.append(d)
        # legs first (behind), thick thighs, real calves
        for h, k, a in (("hl", "kl", "al"), ("hr", "kr", "ar")):
            S(capsule(J[h], J[k], 30, 19)); S(capsule(J[k], J[a], 19, 10))
            fd = self.foot if isinstance(self.foot, tuple) else self.foot[h]
            S(capsule(J[a], add(J[a], mul(norm(fd), 26)), 9, 7))
        # torso, glutes, chest, delts
        S(torso(J["sl"], J["sr"], J["hl"], J["hr"]))
        mh = lerp(J["hl"], J["hr"], .5); ms = lerp(J["sl"], J["sr"], .5)
        S("M %s m -44 0 a 44 40 0 1 0 88 0 a 44 40 0 1 0 -88 0" % f(add(mh, mul(norm(sub(mh, ms)), 6))))
        c = lerp(ms, mh, .3)
        S("M %s m -34 0 a 34 30 0 1 0 68 0 a 34 30 0 1 0 -68 0" % f(c))
        for s in ("sl", "sr"):
            S("M %s m -20 0 a 20 20 0 1 0 40 0 a 20 20 0 1 0 -40 0" % f(J[s]))
        # arms
        for s, e, w in (("sl", "el", "wl"), ("sr", "er", "wr")):
            S(capsule(J[s], J[e], 17, 13)); S(capsule(J[e], J[w], 13, 9))
            S("M %s m -12 0 a 12 12 0 1 0 24 0 a 12 12 0 1 0 -24 0" % f(J[w]))
        # neck, head, hair
        S(capsule(J["nk"], J["hd"], 11, 9))
        S("M %s m -24 0 a 24 24 0 1 0 48 0 a 24 24 0 1 0 -48 0" % f(J["hd"]))
        hv = norm(self.hair); hc = add(J["hd"], mul(hv, 34)); ang = math.degrees(math.atan2(hv[1], hv[0]))
        out.append('<ellipse cx="%.1f" cy="%.1f" rx="42" ry="16" transform="rotate(%.1f %.1f %.1f)"/>' % (hc[0], hc[1], ang, hc[0], hc[1]))
        S("M %s m -28 0 a 28 28 0 1 0 56 0 a 28 28 0 1 0 -56 0" % f(sub(J["hd"], mul(hv, 6))))
        return out

    def svg(self, fill, stroke, sw=3):
        body = "".join('<path d="%s"/>' % p if p.startswith("M") else p for p in self.paths())
        return '<g fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round">%s</g>' % (fill, stroke, sw, body)


class Hand:
    """The glove. Local space: palm centre at 0,0, fingers pointing +y (down)."""
    FINGERS = {   # base → tip, radius base → tip
        "thumb":  ((-92, -30), (-190, 48), 30, 23),
        "index":  ((-68, 60), (-96, 206), 27, 22),
        "middle": ((-24, 64), (-30, 232), 28, 23),
        "ring":   ((22, 64), (34, 218), 27, 22),
        "pinky":  ((66, 56), (96, 172), 24, 19),
    }

    def __init__(self, cx, cy, rot=0, s=1.0, curl=None):
        self.cx, self.cy, self.rot, self.s = cx, cy, rot, s
        self.curl = curl or {}    # finger → tip override (local), for a strained/clenched read

    def world(self, p):
        t = math.radians(self.rot)
        x, y = p[0] * self.s, p[1] * self.s
        return (self.cx + x * math.cos(t) - y * math.sin(t), self.cy + x * math.sin(t) + y * math.cos(t))

    def place_by_tip(self, name, world_pt):
        """Move the hand so that fingertip `name` lands on world_pt (keeps rot and scale)."""
        self.cx, self.cy = 0.0, 0.0
        t = self.tip(name)
        self.cx, self.cy = world_pt[0] - t[0], world_pt[1] - t[1]
        return self

    def tip(self, name):
        b, t, r1, r2 = self.FINGERS[name]
        t = self.curl.get(name, t)
        d = norm(sub(t, b))
        return self.world(add(t, mul(d, r2 * .9)))

    def svg(self, fill, stroke, sw=6):
        parts = []
        parts.append('<path d="M -84 -78 L -70 -215 L 96 -215 L 82 -78 Z"/>')            # the wrist
        parts.append('<path d="M -76 -215 L -74 -258 L 104 -258 L 100 -215 Z"/>')        # the cuff band
        parts.append('<path d="M -95 -70 Q -108 40 -60 72 L 60 72 Q 108 40 95 -70 Q 0 -102 -95 -70 Z"/>')   # palm
        for name, (b, t, r1, r2) in self.FINGERS.items():
            t = self.curl.get(name, t)
            parts.append('<path d="%s"/>' % capsule(b, t, r1, r2))
        # the glove seams, three lines on the back of the hand
        seams = '<path d="M -40 -40 L -60 50 M 0 -44 L -8 58 M 40 -40 L 52 46" fill="none" stroke="%s" stroke-width="%s" opacity=".55"/>' % (stroke, sw * .5)
        return ('<g transform="translate(%.1f %.1f) rotate(%.1f) scale(%.3f)" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round">%s%s</g>'
                % (self.cx, self.cy, self.rot, self.s, fill, stroke, sw, "".join(parts), seams))


# ---------------------------------------------------------------- the patch frame ------
def frame_open():
    return ('<clipPath id="fld"><circle cx="%d" cy="%d" r="%d"/></clipPath>'
            '<circle cx="%d" cy="%d" r="%d" fill="%s"/><g clip-path="url(#fld)">' % (CX, CY, R, CX, CY, R, T["rose"]))


def ground(y=690):
    return ('<path d="M 180 %d C 320 %d 420 %d 520 %d C 640 %d 720 %d 820 %d L 820 820 L 180 820 Z" fill="%s"/>'
            % (y, y - 20, y + 12, y, y - 14, y + 10, y - 4, T["bruise"]))


def guides():
    return ('<g stroke="%s" stroke-width="2" stroke-dasharray="6 8" opacity=".45" fill="none">'
            '<line x1="200" y1="%.0f" x2="800" y2="%.0f"/><line x1="%.0f" y1="200" x2="%.0f" y2="800"/></g>'
            % (T["goldl"], GOLD_Y, GOLD_Y, GOLD_X, GOLD_X))


def frame_close(word="BOLO"):
    o = ['</g>']
    o.append('<circle cx="500" cy="500" r="310" fill="none" stroke="%s" stroke-width="22"/>' % T["black"])
    o.append('<circle cx="500" cy="500" r="310" fill="none" stroke="#2A2A2A" stroke-width="22" stroke-dasharray="3 4"/>')
    top = "M %s A 398 398 0 0 1 %s L %s A 318 318 0 0 0 %s Z" % (P(210, 398), P(330, 398), P(330, 318), P(210, 318))
    bot = "M %s A 398 398 0 0 1 %s L %s A 318 318 0 0 0 %s Z" % (P(30, 398), P(150, 398), P(150, 318), P(30, 318))
    for d in (top, bot):
        o.append('<path d="%s" fill="%s" stroke="%s" stroke-width="6" stroke-linejoin="round"/>' % (d, T["black"], T["black"]))
    o.append('<path d="M %s A 388 388 0 0 1 %s" fill="none" stroke="%s" stroke-width="2"/>' % (P(212, 388), P(328, 388), T["gold"]))
    o.append('<path d="M %s A 388 388 0 0 1 %s" fill="none" stroke="%s" stroke-width="2"/>' % (P(32, 388), P(148, 388), T["gold"]))
    font = "Impact, 'Arial Narrow', 'Arial Black', sans-serif"
    o.append('<path id="at" d="M %s A 343 343 0 0 1 %s" fill="none"/>' % (P(215, 343), P(325, 343)))
    o.append('<path id="ab" d="M %s A 376 376 0 0 0 %s" fill="none"/>' % (P(145, 376), P(35, 376)))
    o.append('<text font-family="%s" font-size="48" letter-spacing="5" fill="%s" stroke="%s" stroke-width="3" paint-order="stroke">'
             '<textPath href="#at" startOffset="50%%" text-anchor="middle">BOLD VENTURE</textPath></text>' % (font, T["goldl"], T["black"]))
    o.append('<text font-family="%s" font-size="44" letter-spacing="5" fill="%s" stroke="%s" stroke-width="3" paint-order="stroke">'
             '<textPath href="#ab" startOffset="50%%" text-anchor="middle">BE ON THE LOOKOUT</textPath></text>' % (font, T["goldl"], T["black"]))
    if word:
        o.append('<text x="500" y="772" text-anchor="middle" font-family="%s" font-size="84" letter-spacing="10" fill="%s" stroke="%s" '
                 'stroke-width="4" paint-order="stroke">%s</text>' % (font, T["goldl"], T["black"], word))
    return "".join(o)


def strings(pairs):
    """Gold strings, each from a fingertip straight down to its attachment."""
    return "".join('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="3"/>' % (a[0], a[1], b[0], b[1], T["goldl"])
                   for a, b in pairs)


def action(d):
    """The line of action, a faint gold curve for the reader's eye."""
    return '<path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="2 10" opacity=".6"/>' % (d, T["goldl"])


def comp(title, read, hand, figure, pairs, action_d, word="BOLO", ground_y=690, hand_first=True):
    inner = [frame_open(), ground(ground_y), guides()]
    hand_svg = hand.svg(T["white"], T["black"])
    fig_svg = figure.svg(T["black"], T["black"])
    if hand_first:
        inner += [hand_svg, strings(pairs), fig_svg]
    else:
        inner += [strings(pairs), fig_svg, hand_svg]
    inner.append(action(action_d))
    inner.append(frame_close(word))
    svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">%s</svg>' % "".join(inner)
    return dict(title=title, read=read, svg=svg)


# ---------------------------------------------------------------- the six --------------
def build():
    C = []

    # 1 · THE MARIONETTE — his pick: hands up on the strings, hanging, legs folded up behind, back arched
    H = Hand(0, 0, rot=40, s=1.05, curl={"thumb": (-176, 34)}).place_by_tip("index", (426, 356))   # in from the top-right corner
    ti, tm = H.tip("index"), H.tip("middle")
    wl, wr = (ti[0], 470), (tm[0], 466)
    m = lerp(wl, wr, .5)
    J = dict(wl=wl, wr=wr, el=(wl[0] - 26, 514), er=(wr[0] + 22, 508),
             sl=(wl[0] + 6, 560), sr=(wr[0] - 4, 556), nk=(m[0] - 18, 570), hd=(m[0] - 66, 596),
             hl=(m[0] - 18, 656), hr=(m[0] + 36, 652), kl=(m[0] + 96, 694), kr=(m[0] + 122, 678),
             al=(m[0] + 150, 616), ar=(m[0] + 172, 598))
    F = Figure(J, hair=(-1, 0.55), foot=(0.15, -1))
    C.append(comp("01 · THE MARIONETTE", "Chief's pick. Two strings straight down to her fists. Back arched, legs folded up behind, hair hanging. "
                  "She is not limp: the fists are closed on the strings and the fingers are bent back by her weight. Who's controlling who.",
                  H, F, [(ti, wl), (tm, wr)], "M %s C %s %s %s" % (f(ti), f((wl[0] + 10, 560)), f((wl[0] + 40, 700)), f((wl[0] + 180, 590))), ground_y=724))

    # 2 · THE YANK — tug of war. Feet planted wide, leaning back, both fists on the strings, the hand tipped toward her
    H = Hand(590, 235, rot=38, s=1.2, curl={"index": (-108, 176), "middle": (-52, 214)})
    ti, tm = H.tip("index"), H.tip("middle")
    wl, wr = (398, 352), (436, 340)
    J = dict(wl=wl, wr=wr, el=(372, 410), er=(420, 400), sl=(392, 468), sr=(446, 462), nk=(404, 474), hd=(378, 448),
             hl=(452, 566), hr=(500, 560), kl=(420, 640), kr=(552, 636), al=(372, 712), ar=(592, 712))
    F = Figure(J, hair=(-1, -0.2), foot={"hl": (-1, 0.2), "hr": (1, 0.2)})
    C.append(comp("02 · THE YANK", "Tug of war. Feet planted wide on the ground, whole body leaned back, both fists on the strings. "
                  "The strings run at an angle because she has pulled the hand down toward her. The index and middle fingers bend toward her. The hand is losing.",
                  H, F, [(ti, wl), (tm, wr)], "M 372 712 C 420 560 400 440 %s" % f(ti), ground_y=706))

    # 3 · THE MUSCLE-UP — she climbs the strings. Elbows out at the top of a pull-up, legs crossed. The hand is a giant, dead centre
    H = Hand(500, 180, rot=0, s=1.32, curl={"index": (-88, 196), "ring": (26, 208)})
    ti, tr = H.tip("index"), H.tip("ring")
    wl, wr = (ti[0], ti[1] + 20), (tr[0], tr[1] + 20)
    J = dict(wl=wl, wr=wr, el=(wl[0] - 62, wl[1] + 46), er=(wr[0] + 62, wr[1] + 46), sl=(wl[0] - 4, wl[1] + 92), sr=(wr[0] + 4, wr[1] + 92),
             nk=(500, wl[1] + 84), hd=(500, wl[1] + 54), hl=(468, wl[1] + 196), hr=(532, wl[1] + 196),
             kl=(456, wl[1] + 286), kr=(548, wl[1] + 282), al=(522, wl[1] + 352), ar=(478, wl[1] + 350))
    F = Figure(J, hair=(0.9, 0.5), foot=(0.2, 1))
    C.append(comp("03 · THE MUSCLE-UP", "She climbs. Top of a pull-up, elbows flared, lats out, ankles crossed under her. The hand is dead centre and giant, "
                  "and two of its fingers are being curled inward by her weight. Symmetric and heavy, the most patch-like of the six.",
                  H, F, [(ti, wl), (tr, wr)], "M 500 %d L 500 %d" % (wl[1] + 30, wl[1] + 350)))

    # 4 · THE SPLIT — strings at the ankles hold a full split across the width. Arms pressed down, face at the viewer
    H = Hand(500, 190, rot=0, s=1.2, curl={"thumb": (-200, 30), "pinky": (104, 160)})
    tt, tp = H.tip("thumb"), H.tip("pinky")
    al, ar = (tt[0], 578), (tp[0], 578)
    J = dict(al=al, ar=ar, kl=(al[0] + 110, 574), kr=(ar[0] - 110, 574), hl=(470, 576), hr=(530, 576),
             sl=(452, 452), sr=(548, 452), nk=(500, 440), hd=(500, 404), el=(430, 520), er=(570, 520), wl=(446, 578), wr=(554, 578))
    F = Figure(J, hair=(0, 1), foot={"hl": (-1, 0), "hr": (1, 0)})
    C.append(comp("04 · THE SPLIT", "Two strings, thumb and pinky, hold a full split across the whole width of the field. Her palms are pressed to the ground, "
                  "head up, straight at you. The hand spreads her; she holds the line. Widest silhouette, reads at any size.",
                  H, F, [(tt, al), (tp, ar)], "M %s Q 500 640 %s" % (f(al), f(ar)), ground_y=600))

    # 5 · THE CUFFS — wrists bound together over her head by a knot of strings, kneeling wide, chin up. Arms-up pose from the refs
    H = Hand(560, 200, rot=-12, s=1.15)
    ti, tm, tr = H.tip("index"), H.tip("middle"), H.tip("ring")
    knot = (tm[0] - 10, 372)
    J = dict(wl=(knot[0] - 8, knot[1] + 6), wr=(knot[0] + 8, knot[1] + 4), el=(knot[0] - 66, 428), er=(knot[0] + 60, 424),
             sl=(knot[0] - 40, 486), sr=(knot[0] + 40, 484), nk=(knot[0], 494), hd=(knot[0], 458),
             hl=(knot[0] - 34, 590), hr=(knot[0] + 34, 588), kl=(knot[0] - 128, 668), kr=(knot[0] + 126, 664),
             al=(knot[0] - 96, 738), ar=(knot[0] + 94, 736))
    F = Figure(J, hair=(-0.9, 0.3), foot=(0, 1))
    C.append(comp("05 · THE CUFFS", "Three strings meet in a knot above her head; her wrists are bound in it. Kneeling wide, chin up, hair thrown. "
                  "The one where she looks caught, except the knot is her own two fists and the hand is stretched taut to hold her. From the arms-up refs.",
                  H, F, [(ti, knot), (tm, knot), (tr, knot)], "M %s C %s %s %s" % (f(tm), f((knot[0] - 20, 520)), f((knot[0] + 30, 640)), f((knot[0], 760))), ground_y=720))

    # 6 · THE HOOK — hung by the ankles, inverted V, arms reaching for the ground. From the legs-up refs
    H = Hand(500, 170, rot=0, s=1.25, curl={"index": (-118, 190), "pinky": (120, 150)})
    ti, tp = H.tip("index"), H.tip("pinky")
    al, ar = (ti[0], 352), (tp[0], 352)
    J = dict(al=al, ar=ar, kl=(al[0] + 46, 432), kr=(ar[0] - 46, 432), hl=(474, 508), hr=(526, 508),
             sl=(456, 620), sr=(544, 620), nk=(500, 640), hd=(500, 676), el=(410, 660), er=(590, 660), wl=(390, 730), wr=(610, 730))
    F = Figure(J, hair=(0, 1), foot=(0, -1))
    C.append(comp("06 · THE HOOK", "Hung by the ankles from the index and the pinky, an inverted V, torso hanging, both arms reaching for the ground, hair down. "
                  "The one where the hand seems to win, until you see her palms are flat on the ground and she is pushing up. From the legs-up refs.",
                  H, F, [(ti, al), (tp, ar)], "M %s L 500 508 L %s" % (f(al), f(ar)), ground_y=740, word=""))
    return C


PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>BVX Patch Comps</title>
<meta name="description" content="BOLO 72 v0.2 — six composition studies for the Bold Venture patch: the Hand, the strings, and her.">
<style>
:root{--bg:#140A0E;--panel:#241018;--ink:#F5EDE9;--ink-2:#CBB6BE;--gold:#FDE68A;--line:#3F0D12}
*{box-sizing:border-box} html,body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 "Atkinson Hyperlegible",system-ui,sans-serif}
header{padding:28px 16px 8px;max-width:1500px;margin:0 auto}
h1{font:800 34px/1 "Barlow Condensed","Arial Narrow",sans-serif;letter-spacing:.04em;margin:0 0 6px;text-transform:uppercase}
h1 small{font:500 15px/1 "IBM Plex Mono",monospace;color:var(--gold);letter-spacing:.14em;display:block;margin-bottom:10px}
p.lede{margin:0 0 8px;color:var(--ink-2);max-width:80ch}
.row{display:grid;grid-template-columns:repeat(auto-fit,minmax(360px,1fr));gap:16px;padding:16px;max-width:1500px;margin:0 auto}
figure{margin:0;background:var(--panel);border:1px solid var(--line);padding:12px}
figure svg{width:100%%;height:auto;display:block}
figcaption{margin-top:10px}
figcaption b{font:700 13px/1.4 "IBM Plex Mono",monospace;letter-spacing:.12em;color:var(--gold);display:block;margin-bottom:4px}
figcaption span{color:var(--ink-2);font-size:14px}
.rules{padding:8px 16px 40px;max-width:1500px;margin:0 auto;color:var(--ink-2);font-size:14px}
.rules b{color:var(--ink)}
a{color:var(--gold)}
</style></head><body>
<header><h1><small>BOLO 72 · BOLD VENTURE · v0.2 · THE COMPOSITIONS · 2026-09-18</small>The Hand and the girl on the strings</h1>
<p class="lede">Six value-blocked thumbnails. Black is her, white is the Hand, gold is the strings. The dashed gold lines are the golden section of the field: the Hand owns the major share above the line, she owns the minor share, and the two are set at an angle so they read as at odds. The dotted gold curve is the line of action. These are studies to pick from, not finished art. The pick goes to a posed 3D reference and then a painted pass.</p></header>
<div class="row">%(figs)s</div>
<div class="rules">
<b>Held constant across all six.</b> Her build: thick thighs, real glutes, wide lats, delts, a small waist. The Hand: the white glove with the cuff, giant, always partly out of frame so it reads bigger than the patch. The strings: straight, taut, gold, always the only thing connecting them. The struggle: in every one, some finger is bent by her weight and some part of her is braced.
&nbsp;·&nbsp; <a href="index.html">v0.1 (superseded)</a>
</div>
</body></html>"""


def main():
    figs = "".join('<figure>%s<figcaption><b>%s</b><span>%s</span></figcaption></figure>' % (c["svg"], c["title"], c["read"]) for c in build())
    io.open(os.path.join(HERE, "comps.html"), "w", encoding="utf-8").write(PAGE % {"figs": figs})
    print("wrote comps.html")


if __name__ == "__main__":
    main()
