# -*- coding: utf-8 -*-
"""BOLO 72 — the Bold Venture patch: the bunny with the bolas.

One geometry, three renders:
  patch-line.svg   the line-art pass (cream, black strokes, no fills)
  patch-color.svg  the six-thread color pass (BVX design system v2.0.0 tokens)
  index.html       the page: line · color · on fabric (satin-stitch texture, merrow, shadow)

Usage:  python _tools/patch/patch.py          writes the three files beside this script
Threads (ruled 9/18, provisional): ROSE 700 field · ROSE 900 ground/dust · BLACK · GOLD deep + light
· FLESH 500 · WHITE (the ghost only).
"""
import io, os, math

HERE = os.path.dirname(os.path.abspath(__file__))

# --- threads (BVX design system v2.0.0) -------------------------------------------------
T = {
    "rose":   "#8A1F44",   # ROSE 700, the field
    "bruise": "#55112B",   # ROSE 900, ground + dust
    "black":  "#0B0B0B",
    "gold":   "#D97706",   # gold deep, the bolas + cuffs
    "goldl":  "#FDE68A",   # gold light, lettering + highlights
    "flesh":  "#FFC8B5",   # FLESH 500
    "white":  "#FFFFFF",   # the ghost, and only the ghost
    "none":   "none",
}
CREAM = "#F4EFE6"
CX, CY, R = 500, 500, 300


def P(a, r):
    """Point on the patch circle at angle a (degrees, SVG orientation) and radius r."""
    t = math.radians(a)
    return "%.1f %.1f" % (CX + r * math.cos(t), CY + r * math.sin(t))


class Render:
    def __init__(self, mode):
        self.mode = mode          # "line" | "color"
        self.out = []

    def fill(self, thread):
        if self.mode == "line":
            return "none"
        return T[thread]

    def stroke(self, thread, default="black"):
        if self.mode == "line":
            return T["black"]
        return T[thread] if thread else T[default]

    def shape(self, d, fill="black", stroke="black", sw=5, extra=""):
        """A filled shape with the patch's black outline. `detail` strokes ride on top."""
        self.out.append('<path d="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round" %s/>'
                        % (d, self.fill(fill), self.stroke(stroke), sw, extra))

    def line(self, d, thread="gold", sw=4, extra=""):
        """A detail line: gold on the color pass, black on the line pass."""
        self.out.append('<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" %s/>'
                        % (d, self.stroke(thread), sw, extra))

    def circle(self, cx, cy, r, fill="black", stroke="black", sw=5, extra=""):
        self.out.append('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="%s" %s/>'
                        % (cx, cy, r, self.fill(fill), self.stroke(stroke), sw, extra))

    def ellipse(self, cx, cy, rx, ry, rot=0, fill="black", stroke="black", sw=5):
        self.out.append('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" transform="rotate(%s %s %s)" fill="%s" stroke="%s" stroke-width="%s"/>'
                        % (cx, cy, rx, ry, rot, cx, cy, self.fill(fill), self.stroke(stroke), sw))

    def text_on_arc(self, pid, d, text, size, fill="goldl"):
        self.out.append('<path id="%s" d="%s" fill="none"/>' % (pid, d))
        self.out.append('<text font-family="Impact, \'Arial Narrow\', \'Arial Black\', sans-serif" font-size="%s" font-weight="700" '
                        'letter-spacing="5" fill="%s" stroke="%s" stroke-width="%s" paint-order="stroke">'
                        '<textPath href="#%s" startOffset="50%%" text-anchor="middle">%s</textPath></text>'
                        % (size, self.fill(fill) if self.mode == "color" else "none", T["black"],
                           2 if self.mode == "line" else 3, pid, text))


def scene(r: Render):
    o = r.out
    # ---- the field ------------------------------------------------------------------
    o.append('<clipPath id="field"><circle cx="%d" cy="%d" r="%d"/></clipPath>' % (CX, CY, R))
    r.circle(CX, CY, R, fill="rose", stroke="black", sw=0)
    o.append('<g clip-path="url(#field)">')

    # ground + dust (bruise)
    r.shape("M 180 700 C 300 665 420 700 520 690 C 620 680 720 705 820 700 L 820 820 L 180 820 Z", fill="bruise", sw=5)
    r.shape("M 232 690 C 218 650 262 625 292 652 C 300 612 362 615 366 655 C 396 640 428 668 406 692 Z", fill="bruise", sw=5)  # hoof dust
    r.shape("M 640 705 C 632 672 668 660 688 680 C 700 655 745 665 740 695 C 760 690 772 712 752 720 Z", fill="bruise", sw=5)  # ghost dust
    r.line("M 236 705 h 42 M 250 722 h 60 M 300 740 h 36", thread="goldl", sw=4)       # speed lines on the ground

    # ---- the horse (black), galloping right, mean --------------------------------------
    r.shape("M 330 480 C 290 470 240 480 200 520 C 230 505 260 500 290 505 C 270 520 250 545 245 570 C 280 540 320 520 340 500 Z")  # tail
    r.shape("M 360 570 L 300 620 L 240 660 L 250 672 L 320 632 L 380 590 Z")   # hind leg near
    r.shape("M 345 555 L 270 580 L 210 610 L 218 624 L 285 600 L 365 578 Z")   # hind leg far
    r.shape("M 520 555 L 600 560 L 660 600 L 672 588 L 610 540 L 530 535 Z")   # fore leg far
    r.shape("M 500 560 L 560 590 L 620 640 L 640 632 L 585 570 L 525 545 Z")   # fore leg near
    r.shape("M 330 480 C 300 520 310 580 360 580 L 500 570 C 540 565 560 520 540 480 C 520 455 470 460 470 470 C 430 450 360 455 330 480 Z")  # body
    r.shape("M 500 480 C 530 440 570 400 610 395 L 640 420 C 620 450 600 490 560 520 Z")  # neck
    r.shape("M 600 392 C 580 380 550 385 530 400 C 545 400 560 405 580 415 Z")            # mane
    r.shape("M 600 390 C 640 380 690 410 705 445 L 700 465 C 680 470 650 470 630 455 C 615 440 600 420 600 390 Z")  # head
    r.shape("M 605 392 L 568 400 L 598 412 Z")   # ear pinned
    r.shape("M 620 386 L 588 370 L 612 402 Z")   # ear pinned
    r.line("M 545 400 C 560 396 575 400 590 412 M 535 408 C 555 412 570 420 585 430", thread="gold", sw=3)  # mane threads
    r.shape("M 682 460 L 688 451 L 694 460 L 700 451 L 706 460 L 706 467 L 682 467 Z", fill="goldl", sw=3)  # teeth
    r.shape("M 652 413 L 672 418 L 668 428 L 650 424 Z", fill="goldl", sw=3)   # eye, a slit
    r.line("M 646 408 L 676 412", thread="gold", sw=4)                          # brow
    r.circle(694, 440, 4, fill="goldl", sw=2)                                   # nostril
    r.line("M 556 444 Q 620 440 690 455", thread="black", sw=4)                 # rein

    # ---- the rider (the bunny) ---------------------------------------------------------
    r.shape("M 435 475 C 460 480 500 500 505 520 C 505 545 500 570 498 590 L 490 602 C 485 570 485 545 480 525 C 470 505 445 495 430 490 Z", fill="flesh")  # leg
    r.shape("M 486 588 L 522 590 L 526 604 L 486 604 Z", fill="black")           # the heel
    r.shape("M 445 392 C 455 360 480 325 512 300 L 524 310 C 498 335 478 365 462 398 Z", fill="flesh")   # arm up (bolas)
    r.shape("M 470 392 C 500 400 530 420 555 438 L 550 450 C 525 435 495 420 468 410 Z", fill="flesh")   # arm forward (rein)
    r.shape("M 430 480 C 425 450 430 425 445 412 Q 458 422 470 408 C 480 425 485 455 478 485 Z", fill="black")   # the suit
    r.shape("M 440 412 C 438 395 445 380 455 372 L 465 372 C 475 380 478 395 472 410 Q 458 420 440 412 Z", fill="flesh")   # neck + shoulders
    r.shape("M 446 366 L 470 366 L 470 376 L 446 376 Z", fill="goldl", sw=3)    # collar
    r.shape("M 458 371 L 448 365 L 448 377 Z M 458 371 L 468 365 L 468 377 Z", fill="black", sw=2)  # bow tie
    r.shape("M 508 296 L 522 288 L 530 302 L 516 310 Z", fill="goldl", sw=3)    # cuff up
    r.shape("M 540 432 L 554 428 L 558 442 L 544 446 Z", fill="goldl", sw=3)    # cuff forward
    r.circle(519, 301, 9, fill="flesh")                                          # fist on the cord
    r.circle(556, 445, 8, fill="flesh")                                          # fist on the rein
    # ears (black, flesh inside)
    r.shape("M 445 322 C 435 290 430 260 440 245 C 455 258 458 290 458 320 Z", fill="black")
    r.shape("M 447 316 C 441 292 439 268 444 256 C 452 266 454 292 455 316 Z", fill="flesh", sw=2)
    r.shape("M 468 320 C 470 290 478 260 492 250 C 496 268 488 300 478 322 Z", fill="black")
    r.shape("M 471 316 C 473 292 478 270 488 260 C 490 274 484 298 477 316 Z", fill="flesh", sw=2)
    # head, hair, face
    r.circle(458, 345, 26, fill="flesh")
    r.shape("M 432 340 C 430 315 445 305 462 306 C 480 306 490 320 486 338 C 478 322 460 318 445 326 C 440 330 436 336 432 340 Z", fill="black")  # hair cap
    r.shape("M 434 338 C 410 340 385 350 365 370 C 385 360 405 356 425 356 Z", fill="black")   # ponytail
    r.line("M 462 341 q 8 -6 16 0", thread="black", sw=3)      # the eye, lid down, smug
    r.line("M 476 340 l 4 -3", thread="black", sw=3)           # lash
    r.line("M 460 329 q 10 -9 20 -3", thread="black", sw=3)    # one brow up
    r.line("M 466 357 q 7 3 12 -4", thread="black", sw=3)      # the smirk

    # ---- the bolas -----------------------------------------------------------------------
    r.line("M 481 221 A 100 100 0 0 1 609 349", thread="goldl", sw=6, extra='stroke-dasharray="14 12"')   # the whirl
    for bx, by in ((549, 221), (597, 258), (615, 315)):
        r.line("M 519 301 L %d %d" % (bx, by), thread="black", sw=4)
    for bx, by in ((549, 221), (597, 258), (615, 315)):
        r.circle(bx, by, 16, fill="gold")
        r.line("M %d %d a 9 9 0 0 1 9 -9" % (bx - 8, by - 2), thread="goldl", sw=3)

    # ---- the ghost (white, the only white on the patch) -----------------------------------
    r.line("M 616 566 h 22 M 608 586 h 20 M 616 606 h 22", thread="goldl", sw=4)   # motion lines behind it
    r.shape("M 668 626 C 645 640 630 636 618 652 C 640 652 655 646 672 640 Z", fill="white")   # the tail wisp
    r.circle(712, 588, 58, fill="white")
    r.shape("M 704 600 C 714 642 752 638 762 598 Z", fill="black")                 # the mouth, wide open
    r.shape("M 720 612 C 724 630 742 630 746 612 Z", fill="rose", sw=3)            # the tongue, in rose
    r.shape("M 712 604 l 5 11 l 5 -11 Z M 746 602 l 5 11 l 5 -11 Z", fill="white", sw=2)   # fangs
    r.ellipse(680, 566, 20, 12, rot=-35, fill="white")   # a hand over the face
    r.ellipse(682, 596, 20, 12, rot=25, fill="white")    # the other hand
    r.ellipse(692, 581, 6, 9, fill="black", sw=2)        # one eye peeking between them
    r.circle(694, 578, 2, fill="white", sw=0)

    o.append('</g>')

    # ---- the field word --------------------------------------------------------------------
    o.append('<text x="500" y="778" text-anchor="middle" font-family="Impact, \'Arial Narrow\', \'Arial Black\', sans-serif" '
             'font-size="92" letter-spacing="10" fill="%s" stroke="%s" stroke-width="4" paint-order="stroke">BOLO</text>'
             % (r.fill("goldl") if r.mode == "color" else "none", T["black"]))

    # ---- merrow border ---------------------------------------------------------------------
    r.circle(CX, CY, 310, fill="none", stroke="black", sw=22)
    if r.mode == "color":
        o.append('<circle cx="500" cy="500" r="310" fill="none" stroke="#2A2A2A" stroke-width="22" stroke-dasharray="3 4"/>')
    else:
        r.circle(CX, CY, 300, fill="none", sw=4)
        r.circle(CX, CY, 320, fill="none", sw=4)

    # ---- rockers -----------------------------------------------------------------------------
    top = "M %s A 398 398 0 0 1 %s L %s A 318 318 0 0 0 %s Z" % (P(210, 398), P(330, 398), P(330, 318), P(210, 318))
    bot = "M %s A 398 398 0 0 1 %s L %s A 318 318 0 0 0 %s Z" % (P(30, 398), P(150, 398), P(150, 318), P(30, 318))
    r.shape(top, fill="black", sw=6)
    r.shape(bot, fill="black", sw=6)
    if r.mode == "color":   # a gold hairline inside each rocker, the way the patches do it
        o.append('<path d="M %s A 388 388 0 0 1 %s" fill="none" stroke="%s" stroke-width="2"/>' % (P(212, 388), P(328, 388), T["gold"]))
        o.append('<path d="M %s A 388 388 0 0 1 %s" fill="none" stroke="%s" stroke-width="2"/>' % (P(32, 388), P(148, 388), T["gold"]))
    r.text_on_arc("arc-top", "M %s A 343 343 0 0 1 %s" % (P(215, 343), P(325, 343)), "BOLD VENTURE", 48)
    r.text_on_arc("arc-bot", "M %s A 376 376 0 0 0 %s" % (P(145, 376), P(35, 376)), "BE ON THE LOOKOUT", 44)


def svg(mode, fabric=False):
    r = Render(mode)
    scene(r)
    bg = CREAM if mode == "line" else "none"
    body = "\n".join(r.out)
    defs = ""
    if fabric:
        defs = ('<defs><pattern id="satin" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
                '<line x1="0" y1="0" x2="0" y2="6" stroke="#000" stroke-width="1.2" stroke-opacity=".22"/></pattern>'
                '<pattern id="satin2" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(-30)">'
                '<line x1="0" y1="0" x2="0" y2="5" stroke="#fff" stroke-width=".8" stroke-opacity=".10"/></pattern>'
                '<clipPath id="whole"><circle cx="500" cy="500" r="321"/>'
                '<path d="M %s A 398 398 0 0 1 %s L %s A 318 318 0 0 0 %s Z"/>'
                '<path d="M %s A 398 398 0 0 1 %s L %s A 318 318 0 0 0 %s Z"/></clipPath></defs>'
                % (P(210, 401), P(330, 401), P(330, 318), P(210, 318), P(30, 401), P(150, 401), P(150, 318), P(30, 318)))
        body += ('\n<g clip-path="url(#whole)" style="pointer-events:none">'
                 '<rect width="1000" height="1000" fill="url(#satin)"/><rect width="1000" height="1000" fill="url(#satin2)"/></g>')
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" height="1000">'
            '<title>BOLD VENTURE · BOLO · the bunny with the bolas (BOLO 72)</title>%s'
            '<rect width="1000" height="1000" fill="%s"/>\n%s\n</svg>' % (defs, bg, body))


PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>BVX Patch</title>
<meta name="description" content="BOLO 72 — the Bold Venture patch: line-art, the six-thread color pass, and the fabric mockup.">
<style>
:root{--bg:#140A0E;--panel:#241018;--ink:#F5EDE9;--ink-2:#CBB6BE;--rose:#8A1F44;--gold:#FDE68A;--line:#3F0D12;--cream:#F4EFE6}
*{box-sizing:border-box} html,body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 "Atkinson Hyperlegible",system-ui,sans-serif}
header{padding:28px 16px 8px;max-width:1500px;margin:0 auto}
h1{font:800 34px/1 "Barlow Condensed","Arial Narrow",sans-serif;letter-spacing:.04em;margin:0 0 6px;text-transform:uppercase}
h1 small{font:500 15px/1 "IBM Plex Mono",monospace;color:var(--gold);letter-spacing:.14em;display:block;margin-bottom:10px}
p.lede{margin:0;color:var(--ink-2);max-width:70ch}
.row{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px;padding:16px;max-width:1500px;margin:0 auto}
figure{margin:0;background:var(--panel);border:1px solid var(--line);padding:12px}
figure.fabric{background:
 radial-gradient(1200px 600px at 30% 0%,rgba(255,255,255,.05),transparent 60%),
 repeating-linear-gradient(0deg,rgba(255,255,255,.028) 0 1px,transparent 1px 3px),
 repeating-linear-gradient(90deg,rgba(0,0,0,.20) 0 1px,transparent 1px 3px),#1B0B10}
figure.line{background:var(--cream)}
figure svg{width:100%;height:auto;display:block}
figure.fabric svg{filter:drop-shadow(0 14px 18px rgba(0,0,0,.55)) drop-shadow(0 2px 2px rgba(0,0,0,.6))}
figcaption{font:500 12px/1.4 "IBM Plex Mono",monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--ink-2);margin-top:10px}
figure.line figcaption{color:#5A4A4E}
.threads{display:flex;flex-wrap:wrap;gap:8px;padding:0 16px 40px;max-width:1500px;margin:0 auto}
.sw{display:flex;align-items:center;gap:8px;border:1px solid var(--line);padding:6px 10px 6px 6px;font:500 12px "IBM Plex Mono",monospace;letter-spacing:.06em;background:var(--panel)}
.sw i{width:22px;height:22px;display:inline-block;border:1px solid #000}
</style></head><body>
<header><h1><small>BOLO 72 · BOLD VENTURE · v0.1 · 2026-09-18</small>The bunny with the bolas</h1>
<p class="lede">One geometry, three passes. Read left to right: the line-art the embroiderer digitizes from, the six-thread color pass, and the patch as it would sit on a jacket. The pun does the work: BOLO the list, bolo the weapon, Boo the thing that only moves when you look away.</p></header>
<div class="row">
<figure class="line">%(line)s<figcaption>01 · line-art · the digitizer's sheet</figcaption></figure>
<figure>%(color)s<figcaption>02 · six threads · flat color</figcaption></figure>
<figure class="fabric">%(fabric)s<figcaption>03 · on fabric · satin stitch, merrowed edge</figcaption></figure>
</div>
<div class="threads">
<div class="sw"><i style="background:#8A1F44"></i>ROSE 700 · field</div>
<div class="sw"><i style="background:#55112B"></i>ROSE 900 · ground, dust</div>
<div class="sw"><i style="background:#0B0B0B"></i>BLACK · border, horse, suit</div>
<div class="sw"><i style="background:#D97706"></i>GOLD deep · bolas, cuffs</div>
<div class="sw"><i style="background:#FDE68A"></i>GOLD light · lettering, teeth</div>
<div class="sw"><i style="background:#FFC8B5"></i>FLESH 500 · her</div>
<div class="sw"><i style="background:#FFFFFF"></i>WHITE · the ghost only</div>
</div>
</body></html>"""


def main():
    line, color, fabric = svg("line"), svg("color"), svg("color", fabric=True)
    io.open(os.path.join(HERE, "patch-line.svg"), "w", encoding="utf-8").write(line)
    io.open(os.path.join(HERE, "patch-color.svg"), "w", encoding="utf-8").write(color)
    io.open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(PAGE.replace("%(line)s", line).replace("%(color)s", color).replace("%(fabric)s", fabric))
    print("wrote patch-line.svg · patch-color.svg · index.html")


if __name__ == "__main__":
    main()
