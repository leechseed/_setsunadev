"""slideshow.py — `command slideshow` (Chief 10/30): a photo slideshow from the DARKROOM corpus, built as a video and opened in VLC.

  python slideshow.py                         # 10 minutes, 5 seconds per image = 120 photos, new VLC window on the left screen
  python slideshow.py --minutes 20 --seconds 4 --side right
  python slideshow.py --dry-run --json        # pick the photos and print them; render and launch nothing

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


def pick(n, used):
    images = json.load(open(MANIFEST, encoding="utf-8"))["images"]
    ids = [c for c, v in images.items() if not v.get("animated") and c not in used]
    random.shuffle(ids)
    out = []
    for c in ids:
        p = os.path.join(NORM, c + ".jpg")
        if os.path.exists(p):
            out.append((c, p))
        if len(out) >= n:
            break
    return out, len(ids)


def render(photos, seconds, path):
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
                            "-r", "10", "-c:v", "libx264", "-preset", "veryfast", "-crf", "23", "-movflags", "+faststart", path],
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
    a = ap.parse_args()
    n = max(1, int(a.minutes * 60 / a.seconds))
    used = load_ledger()
    photos, pool = pick(n, used)
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
    render(photos, a.seconds, path)
    json.dump(sorted(used | {c for c, _ in photos}), open(LEDGER, "w", encoding="utf-8"))
    import stashplay as sp
    ok = sp.launch(path, side=a.side)
    if not a.json:
        print(("Slideshow is up: " if ok else "Rendered, but the window did not report in: ") + line + "  [%s, rendered in %ds]" % (os.path.basename(path), time.time() - t0))


main()
