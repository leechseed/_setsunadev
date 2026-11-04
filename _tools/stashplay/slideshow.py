"""slideshow.py — `command slideshow` (Chief 10/30): a photo slideshow from the DARKROOM corpus, built as a video and opened in VLC.

  python slideshow.py                         # 10 minutes, 5 seconds per image = 120 photos, new VLC window on the left screen
  python slideshow.py --minutes 20 --seconds 4 --side right
  python slideshow.py --dry-run --json        # pick the photos and print them; render and launch nothing
  python slideshow.py --minutes 120 --want framing=full,threeq --want part=legs,thighs,full       --want styling=gym,swim,skimpy,lingerie --want register=studio,editorial --boost styling=gym --fps 2
                                              # filter by the top auto-tag (tags_auto.json); boosted photos play first (11/4)

Source: the DARKROOM corpus manifest (Q:\\fun\\.2026picstach8252026\\_pipeline\\manifest.json), the normalized JPEGs, not
animated, not quarantined (a quarantined file has left _normalized, so it is skipped). No photo repeats across slideshows:
the used ids go in _PRIVATE/slideshows/ledger.json. The video is 1920x1080, each photo fitted on black. It is written to
_PRIVATE/slideshows/ (private, gitignored). The new window never closes another player.
"""
import argparse
import json
import os
import random
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "_tools", "dictation"))

CORPUS = r"Q:\fun\.2026picstach8252026"
MANIFEST = os.path.join(CORPUS, "_pipeline", "manifest.json")
NORM = os.path.join(CORPUS, "_normalized")
OUT = os.path.join(ROOT, "_PRIVATE", "slideshows")
LEDGER = os.path.join(OUT, "ledger.json")


def load_ledger():
    try:
        return set(json.load(open(LEDGER, encoding="utf-8")))
    except (OSError, ValueError):
        return set()


TAGS = os.path.join(CORPUS, "_pipeline", "tags_auto.json")


def parse_rules(specs):
    out = []
    for s in specs or []:
        k, _, vals = s.partition("=")
        out.append((k.strip(), {v.strip() for v in vals.split(",") if v.strip()}))
    return out


def pick(n, used, want=None, avoid=None, boost=None):
    images = json.load(open(MANIFEST, encoding="utf-8"))["images"]
    ids = [c for c, v in images.items() if not v.get("animated") and not v.get("excluded") and c not in used]
    if want or avoid or boost:
        tags = json.load(open(TAGS, encoding="utf-8"))
        top = lambda c, k: ((tags.get(c) or {}).get(k) or [""])[0]
        ids = [c for c in ids if c in tags
               and all(top(c, k) in vs for k, vs in want or [])
               and not any(top(c, k) in vs for k, vs in avoid or [])]
    random.shuffle(ids)
    if boost:
        ids.sort(key=lambda c: not any(top(c, k) in vs for k, vs in boost))   # stable: boosted first, each group still shuffled
    out = []
    for c in ids:
        p = os.path.join(NORM, c + ".jpg")
        if os.path.exists(p):
            out.append((c, p))
        if len(out) >= n:
            break
    return out, len(ids)


def render(photos, seconds, path, fps=10):
    ff = shutil.which("ffmpeg")
    if not ff:
        sys.exit("ffmpeg is not on PATH.")
    with tempfile.TemporaryDirectory() as tmp:
        lst = os.path.join(tmp, "list.txt")
        with open(lst, "w", encoding="utf-8") as f:
            for _, p in photos:
                f.write("file '%s'\nduration %s\n" % (p.replace("\\", "/").replace("'", "'\\''"), seconds))
            f.write("file '%s'\n" % photos[-1][1].replace("\\", "/").replace("'", "'\\''"))   # concat needs the last file repeated
        vf = "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,format=yuv420p"
        r = subprocess.run([ff, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-vf", vf,
                            "-r", str(fps), "-c:v", "libx264", "-preset", "veryfast", "-crf", "23", "-movflags", "+faststart", path],
                           capture_output=True, text=True)
        if r.returncode:
            sys.exit("ffmpeg failed: " + r.stderr.strip()[-400:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--minutes", type=float, default=10)
    ap.add_argument("--seconds", type=float, default=5)
    ap.add_argument("--side", default="left")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--want", action="append", help="KEY=v1,v2: the photo's top auto-tag for KEY must be one of these (repeatable)")
    ap.add_argument("--avoid", action="append", help="KEY=v1,v2: drop photos whose top tag for KEY is one of these")
    ap.add_argument("--boost", action="append", help="KEY=v1,v2: these play first")
    ap.add_argument("--fps", type=float, default=10, help="video frame rate; 2 renders long shows fast")
    a = ap.parse_args()
    n = max(1, int(a.minutes * 60 / a.seconds))
    used = load_ledger()
    photos, pool = pick(n, used, parse_rules(a.want), parse_rules(a.avoid), parse_rules(a.boost))
    if len(photos) < n:
        sys.exit("Only %d fresh photos left (wanted %d); clear _PRIVATE/slideshows/ledger.json to start over." % (len(photos), n))
    line = "%d photos x %g s = %g min (%d fresh photos were left in the pool)" % (n, a.seconds, n * a.seconds / 60, pool)
    if a.json:
        print(json.dumps({"summary": line, "dry_run": a.dry_run, "photos": [c for c, _ in photos]}, indent=1))
    if a.dry_run:
        if not a.json:
            print("dry run: " + line)
        return
    os.makedirs(OUT, exist_ok=True)
    day = time.strftime("%Y-%m-%d")
    k = 1 + sum(1 for f in os.listdir(OUT) if f.startswith("darkroom-" + day))
    path = os.path.join(OUT, "darkroom-%s-%d.mp4" % (day, k))
    t0 = time.time()
    render(photos, a.seconds, path, a.fps)
    json.dump(sorted(used | {c for c, _ in photos}), open(LEDGER, "w", encoding="utf-8"))
    import stashplay as sp
    ok = sp.launch(path, side=a.side)
    if not a.json:
        print(("Slideshow is up: " if ok else "Rendered, but the window did not report in: ") + line + "  [%s, rendered in %ds]" % (os.path.basename(path), time.time() - t0))


main()
