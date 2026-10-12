"""deconstruct.py — THE CUT (BOLO 136): take a set of reference videos apart into numbers, so Chief can
format his own edits from what the references actually do (10/12: "come up with a deconstruction of each …
then format my own videos to increase speed").

For every video:
  picture   ffprobe duration · fps · size · aspect; ffmpeg scene detection -> cut times; shot lengths
            (mean · median · shortest · longest); the pace curve (cuts per 5 s window)
  sound     librosa tempo (BPM) and beat grid; RMS energy per second; the structure read off the energy
            (intro · build · drop · outro as % of duration, by energy quantiles); cuts on the beat (within
            ±70 ms of a beat) as a share of all cuts; cuts per bar
  look      one frame a second through OpenCV: brightness · saturation · motion (frame-to-frame change),
            as means and as curves
Writes one JSON per video, a summary table, and TEMPLATE.md: the format the set agrees on (median of the
medians, with the spread), which is the starting sheet for a new edit.

Inputs (one of): --stash-tag NAME (scenes carrying that Stash tag, via the local API) · --m3u FILE · --dir DIR · paths.
Usage: .venv/Scripts/python.exe _tools/thecut/deconstruct.py --stash-tag pmv:ref --out _PRIVATE/thecut/deconstruct
"""

import argparse
import glob
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request

import numpy as np

STASH = "http://127.0.0.1:9999/graphql"
SCENE_T = 0.30          # ffmpeg scene-change score; PMVs flash, so 0.30 reads as a cut and a hard flash alike (provisional)
BEAT_WIN = 0.070        # a cut within 70 ms of a beat counts as on the beat
WIN = 5.0               # the pace-curve window, seconds


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", **kw)


def stash_paths(tag):
    q = {"query": '{ findTags(tag_filter:{name:{value:"%s",modifier:EQUALS}}){ tags{ id } } }' % tag}
    r = json.loads(urllib.request.urlopen(urllib.request.Request(STASH, json.dumps(q).encode(), {"Content-Type": "application/json"})).read())
    tags = r["data"]["findTags"]["tags"]
    if not tags:
        sys.exit(f"no Stash tag named {tag}")
    q = {"query": '{ findScenes(scene_filter:{tags:{value:["%s"],modifier:INCLUDES}}, filter:{per_page:500}){ scenes{ id title files{ path } } } }' % tags[0]["id"]}
    r = json.loads(urllib.request.urlopen(urllib.request.Request(STASH, json.dumps(q).encode(), {"Content-Type": "application/json"})).read())
    out = []
    for s in r["data"]["findScenes"]["scenes"]:
        for f in s["files"]:
            if os.path.exists(f["path"]):
                out.append((f"stash{s['id']}", f["path"]))
                break
    return out


def probe(path):
    r = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height,r_frame_rate:format=duration", "-of", "json", path])
    d = json.loads(r.stdout)
    st = d["streams"][0]
    num, den = st["r_frame_rate"].split("/")
    return float(d["format"]["duration"]), int(st["width"]), int(st["height"]), float(num) / float(den or 1)


def cuts(path):
    r = run(["ffmpeg", "-hide_banner", "-i", path, "-an", "-vf", f"select='gt(scene,{SCENE_T})',showinfo", "-f", "null", "-"])
    return sorted(float(m) for m in re.findall(r"pts_time:\s*([0-9.]+)", r.stderr))


def audio(path, dur):
    import librosa
    tmp = os.path.join(tempfile.gettempdir(), "thecut_%d.wav" % os.getpid())
    run(["ffmpeg", "-hide_banner", "-y", "-i", path, "-vn", "-ac", "1", "-ar", "22050", tmp])
    y, sr = librosa.load(tmp, sr=22050, mono=True)
    os.remove(tmp)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    beat_t = librosa.frames_to_time(beats, sr=sr)
    rms = librosa.feature.rms(y=y, frame_length=2048, hop_length=512)[0]
    t = librosa.frames_to_time(np.arange(len(rms)), sr=sr, hop_length=512)
    secs = np.arange(0, int(np.ceil(dur)) + 1)
    energy = np.array([rms[(t >= s) & (t < s + 1)].mean() if ((t >= s) & (t < s + 1)).any() else 0.0 for s in secs[:-1]])
    e = energy / (energy.max() or 1)
    # structure by energy: the first stretch under the 40% line is the intro, the first stretch over 80% is the drop
    hi, lo = e >= 0.8, e < 0.4
    intro_end = int(np.argmax(~lo)) if (~lo).any() else 0
    drop_start = int(np.argmax(hi)) if hi.any() else len(e)
    tail = np.where(lo[drop_start:])[0]
    outro_start = int(drop_start + tail[0]) if len(tail) and drop_start < len(e) else len(e)
    n = len(e) or 1
    structure = {"intro_pct": round(100 * intro_end / n), "build_pct": round(100 * max(drop_start - intro_end, 0) / n),
                 "drop_pct": round(100 * max(outro_start - drop_start, 0) / n), "outro_pct": round(100 * (n - outro_start) / n),
                 "drop_at_s": drop_start}
    return float(np.atleast_1d(tempo)[0]), beat_t, e.round(3).tolist(), structure


def look(path, dur):
    import cv2
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    bright, sat, motion, prev = [], [], [], None
    for s in range(int(dur)):
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(s * fps))
        ok, fr = cap.read()
        if not ok:
            break
        small = cv2.resize(fr, (160, 90))
        hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
        bright.append(float(hsv[..., 2].mean() / 255))
        sat.append(float(hsv[..., 1].mean() / 255))
        g = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY).astype(np.float32)
        motion.append(float(np.abs(g - prev).mean() / 255) if prev is not None else 0.0)
        prev = g
    cap.release()
    return {"brightness": round(float(np.mean(bright)), 3) if bright else None, "saturation": round(float(np.mean(sat)), 3) if sat else None,
            "motion": round(float(np.mean(motion)), 4) if motion else None,
            "brightness_curve": [round(b, 2) for b in bright], "motion_curve": [round(m, 3) for m in motion]}


def deconstruct(vid, path):
    dur, w, h, fps = probe(path)
    c = cuts(path)
    shots = np.diff([0.0] + c + [dur]) if c else np.array([dur])
    tempo, beat_t, energy, structure = audio(path, dur)
    on_beat = int(sum(1 for x in c if len(beat_t) and np.min(np.abs(beat_t - x)) <= BEAT_WIN))
    bars = (dur * tempo / 60) / 4 if tempo else 0
    pace = [int(sum(1 for x in c if s <= x < s + WIN)) for s in np.arange(0, dur, WIN)]
    aspect = "9:16" if h > w * 1.3 else "1:1" if abs(w - h) < 0.05 * w else "16:9" if w > h * 1.3 else f"{w}x{h}"
    return {
        "id": vid, "path": path, "title": os.path.splitext(os.path.basename(path))[0],
        "duration_s": round(dur, 1), "fps": round(fps, 2), "width": w, "height": h, "aspect": aspect,
        "cuts": len(c), "cuts_per_min": round(60 * len(c) / dur, 1) if dur else 0,
        "shot_s": {"mean": round(float(shots.mean()), 2), "median": round(float(np.median(shots)), 2),
                   "shortest": round(float(shots.min()), 2), "longest": round(float(shots.max()), 2)},
        "bpm": round(tempo, 1), "cuts_on_beat_pct": round(100 * on_beat / len(c)) if c else None,
        "cuts_per_bar": round(len(c) / bars, 2) if bars else None,
        "structure": structure, "pace_curve": pace, "energy_curve": energy, "cut_times": [round(x, 2) for x in c],
        "look": look(path, dur),
    }


def template(rows):
    def med(vals):
        v = [x for x in vals if x is not None]
        return (round(float(np.median(v)), 2), round(float(np.percentile(v, 25)), 2), round(float(np.percentile(v, 75)), 2)) if v else (None, None, None)
    L = []
    L.append("# THE CUT · the reference format\n")
    L.append(f"Built {time.strftime('%Y-%m-%d %H:%M')} from {len(rows)} reference videos. Each line is the middle value, then the middle half of the set (25th to 75th percentile). Start a new edit from the middle; stay inside the half.\n")
    for label, key, unit in [("Duration", lambda r: r["duration_s"], "s"), ("Cuts per minute", lambda r: r["cuts_per_min"], ""), ("Median shot length", lambda r: r["shot_s"]["median"], "s"),
                             ("Shortest shot", lambda r: r["shot_s"]["shortest"], "s"), ("Longest shot", lambda r: r["shot_s"]["longest"], "s"), ("Tempo", lambda r: r["bpm"], "BPM"),
                             ("Cuts on the beat", lambda r: r["cuts_on_beat_pct"], "%"), ("Cuts per bar", lambda r: r["cuts_per_bar"], ""),
                             ("Intro", lambda r: r["structure"]["intro_pct"], "% of length"), ("Build", lambda r: r["structure"]["build_pct"], "% of length"),
                             ("Drop", lambda r: r["structure"]["drop_pct"], "% of length"), ("Outro", lambda r: r["structure"]["outro_pct"], "% of length"),
                             ("Brightness", lambda r: r["look"]["brightness"], "0-1"), ("Saturation", lambda r: r["look"]["saturation"], "0-1"), ("Motion", lambda r: r["look"]["motion"], "0-1")]:
        m, lo, hi = med([key(r) for r in rows])
        if m is not None:
            L.append(f"- **{label}:** {m} {unit} · middle half {lo} to {hi}")
    from collections import Counter
    asp = Counter(r["aspect"] for r in rows).most_common()
    L.append(f"- **Aspect:** " + " · ".join(f"{a} ×{n}" for a, n in asp))
    L.append("\n## How to use it\n")
    L.append("1. Pick the track. Its BPM should sit in the tempo band above, or the cut rate will fight the music.")
    L.append("2. Map the track: intro, build, drop, outro, at the percentages above. Put the first drop where the set puts it.")
    L.append("3. Cut to the median shot length through the build. Go to the shortest shots in the drop. Hold the longest shots in the intro and outro.")
    L.append("4. Land the share of cuts on the beat that the set lands. More than that reads mechanical; less reads sloppy.")
    L.append("5. Grade toward the set's brightness and saturation, then push one of them for the look.")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--stash-tag")
    ap.add_argument("--m3u")
    ap.add_argument("--dir")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    items = []
    if args.stash_tag:
        items += stash_paths(args.stash_tag)
    if args.m3u:
        items += [(f"m3u{i}", l.strip()) for i, l in enumerate(open(args.m3u, encoding="utf-8", errors="replace")) if l.strip() and not l.startswith("#")]
    if args.dir:
        items += [(f"dir{i}", p) for i, p in enumerate(sorted(glob.glob(os.path.join(args.dir, "*.*")))) if p.lower().endswith((".mp4", ".mov", ".mkv", ".webm", ".m4v"))]
    items += [(f"arg{i}", p) for i, p in enumerate(args.paths)]
    os.makedirs(args.out, exist_ok=True)
    rows, t0 = [], time.time()
    for vid, path in items:
        outp = os.path.join(args.out, vid + ".json")
        if os.path.exists(outp):
            rows.append(json.load(open(outp, encoding="utf-8")))
            continue
        try:
            r = deconstruct(vid, path)
        except Exception as e:
            print(f"SKIP {vid} · {os.path.basename(path)[:60]} · {e}", flush=True)
            continue
        json.dump(r, open(outp, "w", encoding="utf-8"), ensure_ascii=False)
        rows.append(r)
        print(f"{vid:>9} · {r['duration_s']:>6}s · {r['cuts']:>3} cuts · median shot {r['shot_s']['median']}s · {r['bpm']} BPM · {r['cuts_on_beat_pct']}% on beat · drop at {r['structure']['drop_at_s']}s · {r['aspect']} · {os.path.basename(path)[:50]}", flush=True)
    with open(os.path.join(args.out, "SUMMARY.md"), "w", encoding="utf-8") as f:
        f.write("| id | title | length | aspect | cuts/min | median shot | BPM | on beat | cuts/bar | intro/build/drop/outro % | bright | sat | motion |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
        for r in sorted(rows, key=lambda r: r["cuts_per_min"], reverse=True):
            s = r["structure"]
            f.write(f"| {r['id']} | {r['title'][:50]} | {r['duration_s']}s | {r['aspect']} | {r['cuts_per_min']} | {r['shot_s']['median']}s | {r['bpm']} | {r['cuts_on_beat_pct']}% | {r['cuts_per_bar']} | {s['intro_pct']}/{s['build_pct']}/{s['drop_pct']}/{s['outro_pct']} | {r['look']['brightness']} | {r['look']['saturation']} | {r['look']['motion']} |\n")
    with open(os.path.join(args.out, "TEMPLATE.md"), "w", encoding="utf-8") as f:
        f.write(template(rows))
    json.dump(rows, open(os.path.join(args.out, "all.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(f"done · {len(rows)} videos · {time.time()-t0:.0f}s · {args.out}/SUMMARY.md · TEMPLATE.md")


if __name__ == "__main__":
    main()
