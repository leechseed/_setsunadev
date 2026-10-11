"""The footage drop: phone clips in, Resolve-ready copies out (Chief 10/11: "go ingest").

Usage:
  python _tools/ingest/ingest.py            # process everything in the drop folder once
  python _tools/ingest/ingest.py --watch    # keep watching the drop folder (checks every 30 s)
  python _tools/ingest/ingest.py --small    # H.264 edit copies instead of DNxHR (smaller, 8-bit)

Zero tokens. Works for iPhone or Android: drag the clips (cable, LocalSend, anything) into Q:/_FOOTAGE/_DROP.
For each video the script reads the shoot date, moves the ORIGINAL to Q:/_FOOTAGE/originals/<date>/ (never altered),
and writes an edit copy to Q:/_FOOTAGE/edit/<date>/ that Resolve free opens cleanly:
  - constant frame rate (phone video drifts; that is what slides the audio out of sync in Resolve)
  - DNxHR HQ (8-bit source) or HQX (10-bit source) in .mov, PCM audio at 48 kHz
Photos (jpg · heic · png · dng) go to originals/<date>/ as they are. A file whose copy already exists is skipped.
"""
import json, os, shutil, subprocess, sys, time
from datetime import datetime

BASE = "Q:/_FOOTAGE"
DROP, ORIG, EDIT = BASE + "/_DROP", BASE + "/originals", BASE + "/edit"
VIDEO = {".mov", ".mp4", ".m4v", ".3gp", ".mkv"}
PHOTO = {".jpg", ".jpeg", ".heic", ".png", ".dng"}
RATES = [23.976, 24, 25, 29.97, 30, 48, 50, 59.94, 60, 119.88, 120]
LOG = BASE + "/ingest.log"


def log(msg):
    line = "%s  %s" % (datetime.now().strftime("%m/%d %H:%M:%S"), msg)
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", path],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    return json.loads(out.stdout or "{}")


def shoot_date(path, info):
    tags = (info.get("format") or {}).get("tags") or {}
    for k in ("com.apple.quicktime.creationdate", "creation_time"):
        if tags.get(k):
            try:
                return datetime.fromisoformat(tags[k].replace("Z", "+00:00")[:25]).strftime("%Y-%m-%d")
            except ValueError:
                pass
    return datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d")


def frame_rate(v):
    num, _, den = (v.get("avg_frame_rate") or "30/1").partition("/")
    fps = float(num) / float(den or 1) if float(den or 1) else 30.0
    return min(RATES, key=lambda r: abs(r - fps))


def edit_copy(src, dst, info, small):
    v = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), {})
    has_audio = any(s.get("codec_type") == "audio" for s in info.get("streams", []))
    fps = frame_rate(v)
    ten_bit = "10" in (v.get("pix_fmt") or "")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-map", "0:v:0"] + (["-map", "0:a:0"] if has_audio else [])
    cmd += ["-fps_mode", "cfr", "-r", str(fps)]
    if small:
        cmd += ["-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p"]
    elif ten_bit:
        cmd += ["-c:v", "dnxhd", "-profile:v", "dnxhr_hqx", "-pix_fmt", "yuv422p10le"]
    else:
        cmd += ["-c:v", "dnxhd", "-profile:v", "dnxhr_hq", "-pix_fmt", "yuv422p"]
    if has_audio:
        cmd += ["-c:a", "pcm_s16le", "-ar", "48000"]
    cmd += [dst]
    t = time.time()
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode == 0, "%s fps · %s · %.0f s" % (fps, "10-bit HQX" if ten_bit and not small else ("H.264" if small else "HQ"), time.time() - t), r.stderr.strip()[-300:]


def run_once(small):
    for d in (DROP, ORIG, EDIT):
        os.makedirs(d, exist_ok=True)
    files = sorted(f for f in os.listdir(DROP) if os.path.isfile(os.path.join(DROP, f)))
    done = 0
    for name in files:
        src = os.path.join(DROP, name)
        ext = os.path.splitext(name)[1].lower()
        if ext not in VIDEO | PHOTO:
            continue
        try:                                   # still copying in? wait for the size to settle
            s1 = os.path.getsize(src); time.sleep(2)
            if os.path.getsize(src) != s1:
                continue
        except OSError:
            continue
        info = probe(src) if ext in VIDEO else {}
        day = shoot_date(src, info)
        os.makedirs(os.path.join(ORIG, day), exist_ok=True)
        if ext in VIDEO:
            os.makedirs(os.path.join(EDIT, day), exist_ok=True)
            dst = os.path.join(EDIT, day, os.path.splitext(name)[0] + (".mp4" if small else ".mov"))
            if not os.path.exists(dst):
                ok, how, err = edit_copy(src, dst, info, small)
                if not ok:
                    log("FAIL  %s · %s" % (name, err))
                    continue
                log("EDIT  %s -> edit/%s · %s" % (name, day, how))
        target = os.path.join(ORIG, day, name)
        if os.path.exists(target):
            target = os.path.join(ORIG, day, "%s_%d%s" % (os.path.splitext(name)[0], int(time.time()), ext))
        shutil.move(src, target)
        log("KEEP  %s -> originals/%s" % (name, day))
        done += 1
    return done


if __name__ == "__main__":
    small = "--small" in sys.argv
    if "--watch" in sys.argv:
        log("WATCH %s (every 30 s; Ctrl+C stops)" % DROP)
        while True:
            run_once(small)
            time.sleep(30)
    else:
        n = run_once(small)
        print("INGEST: %d file(s) done · originals in %s · edit copies in %s" % (n, ORIG, EDIT))
