"""make_icon.py: draws the Engine Room's V6 mark (Chief 11/4: "a V6 type logo") as PNG + ICO.

Two cylinder banks in a V, three bores each, on a crankcase; BoldVenture orange on black. Writes
_tools/engineroom/icon/engineroom.png (256) and engineroom.ico (16-256) for the favicon and the desktop shortcut.
  python -X utf8 _tools/engineroom/make_icon.py
"""
import math
import os

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "icon")
ORANGE = (255, 90, 31, 255)
INK = (18, 19, 21, 255)
S = 1024


def rotated_rect(cx, cy, w, h, deg):
    a = math.radians(deg)
    ca, sa = math.cos(a), math.sin(a)
    pts = []
    for dx, dy in ((-w / 2, -h / 2), (w / 2, -h / 2), (w / 2, h / 2), (-w / 2, h / 2)):
        pts.append((cx + dx * ca - dy * sa, cy + dx * sa + dy * ca))
    return pts


def draw():
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((24, 24, S - 24, S - 24), radius=190, fill=INK)
    # crankcase: a wide block at the base of the V
    d.rounded_rectangle((330, 650, 694, 830), radius=50, fill=ORANGE)
    # the two banks, 30 degrees off vertical each (a 60-degree V6)
    for side in (-1, 1):
        deg = 30 * side
        cx, cy = 512 + side * 165, 455
        d.polygon(rotated_rect(cx, cy, 200, 470, deg), fill=ORANGE)
        a = math.radians(deg)
        for k in (-1, 0, 1):   # three bores per bank, along the bank's long axis
            t = k * 140
            bx = cx - t * math.sin(a)   # along the bank's long axis: (-sin a, cos a)
            by = cy + t * math.cos(a)
            r = 54
            d.ellipse((bx - r, by - r, bx + r, by + r), fill=INK)
    # the valley between the banks: a dark wedge keeps the V readable at 16 px
    d.polygon([(512, 560), (420, 300), (604, 300)], fill=INK)
    return im


def main():
    os.makedirs(OUT, exist_ok=True)
    big = draw()
    big.resize((256, 256), Image.LANCZOS).save(os.path.join(OUT, "engineroom.png"))
    big.resize((256, 256), Image.LANCZOS).save(os.path.join(OUT, "engineroom.ico"),
                                               sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print("wrote", os.path.join(OUT, "engineroom.png"), "and engineroom.ico")


if __name__ == "__main__":
    main()
