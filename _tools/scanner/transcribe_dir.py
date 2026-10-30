# -*- coding: utf-8 -*-
"""transcribe_dir.py - 10/30: transcribe every video/audio file under a folder with faster-whisper, resumable.

Reads   a folder of .MOV/.mp4/.wav/.mp3 (any depth)
Writes  <out>/<subfolder>/<file>.txt (timestamped lines) + <out>/_log.txt ; skips files already done
Model   Systran/faster-distil-whisper-large-v3 (already in the HF cache); cuda if it loads, else cpu int8
Run with the .venv python: .venv/Scripts/python -X utf8 _tools/scanner/transcribe_dir.py <in> <out>
"""
import os, subprocess, sys, tempfile, time

EXT = {".mov", ".mp4", ".wav", ".mp3", ".m4a", ".wmv"}


def load():
    from faster_whisper import WhisperModel
    try:
        return WhisperModel("distil-large-v3", device="cuda", compute_type="float16"), "cuda"
    except Exception as e:
        print("cuda failed, cpu:", str(e)[:120], flush=True)
        return WhisperModel("distil-large-v3", device="cpu", compute_type="int8"), "cpu"


def main():
    src, out = sys.argv[1], sys.argv[2]
    files = []
    for dp, _, fn in os.walk(src):
        for f in sorted(fn):
            if os.path.splitext(f)[1].lower() in EXT:
                files.append(os.path.join(dp, f))
    files.sort()
    os.makedirs(out, exist_ok=True)
    log = open(os.path.join(out, "_log.txt"), "a", encoding="utf-8")
    model, dev = load()
    print(f"{len(files)} files on {dev}", flush=True)
    tmp = tempfile.mkdtemp()
    for i, p in enumerate(files, 1):
        rel = os.path.relpath(p, src)
        dest = os.path.join(out, os.path.splitext(rel)[0] + ".txt")
        if os.path.exists(dest):
            continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        wav = os.path.join(tmp, "a.wav")
        t0 = time.time()
        r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", p, "-vn", "-ac", "1", "-ar", "16000", wav], capture_output=True)
        if r.returncode:
            log.write(f"FAIL audio {rel}\n"); log.flush(); continue
        segs, info = model.transcribe(wav, language="en", vad_filter=True)
        lines = [f"[{int(s.start)//60}:{int(s.start)%60:02d}] {s.text.strip()}" for s in segs]
        with open(dest, "w", encoding="utf-8") as f:
            f.write(f"# {rel}  ({info.duration:.0f}s)\n" + "\n".join(lines) + "\n")
        msg = f"{i}/{len(files)} {rel} {info.duration:.0f}s audio in {time.time()-t0:.0f}s, {len(lines)} lines"
        print(msg, flush=True); log.write(msg + "\n"); log.flush()
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
