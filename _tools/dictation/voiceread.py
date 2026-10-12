"""
voiceread.py - BOLO 124, the voice read. First working version (10/12).

JUDY measures how Chief speaks: pitch, pace, loudness, breath. She compares each dictation
against his running baseline (the last 40 dictations) and returns a short tag, so Claude can
answer to the delivery as well as the words. numpy only; no model.

    import voiceread
    tag = voiceread.read(audio, text)        # "" when nothing stands out
    # audio = 16 kHz mono float32 (what ptt.Recorder returns); text = the transcript

Off by default. judy.json: "session": {"voice_read": true} turns it on (next JUDY launch).
The tag rides after the typed words as "[voice: faster, louder]". Test with a wav:
    python voiceread.py take.wav "the words that were said"
"""
import io
import json
import os
import sys

import numpy as np

SR = 16000
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, "_voiceread_baseline.json")
KEEP = 40          # dictations in the running baseline
MIN_BASE = 5       # no tags until the baseline has this many
FRAME = 400        # 25 ms
HOP = 160          # 10 ms


def _frames(x):
    n = 1 + max(0, (len(x) - FRAME) // HOP)
    idx = np.arange(FRAME)[None, :] + HOP * np.arange(n)[:, None]
    return x[idx]


def _pitch(fr):
    """Median F0 over voiced frames by autocorrelation, 70-400 Hz. None if too few voiced frames."""
    lo, hi = SR // 400, SR // 70
    f0 = []
    for f in fr:
        f = f - f.mean()
        e = float(np.dot(f, f))
        if e <= 1e-8:
            continue
        ac = np.correlate(f, f, "full")[len(f) - 1:]
        seg = ac[lo:hi]
        k = int(np.argmax(seg))
        if seg[k] / ac[0] > 0.45:
            f0.append(SR / (lo + k))
    return float(np.median(f0)) if len(f0) >= 8 else None


def measure(audio, text=""):
    """Raw numbers for one take: pitch_hz, loud_db, pace_wps, breath."""
    x = np.asarray(audio, dtype="float32")
    if len(x) < SR * 0.6:
        return None
    fr = _frames(x)
    rms = np.sqrt((fr ** 2).mean(axis=1) + 1e-12)
    db = 20 * np.log10(rms)
    floor = np.percentile(db, 10)
    top = np.percentile(db, 95)
    speech = db > max(floor + 10, top - 25)
    if speech.sum() < 20:
        return None
    zcr = (np.abs(np.diff(np.sign(fr), axis=1)) > 0).mean(axis=1)
    # breath: quiet but above the floor, noisy (high zero-crossing), not speech
    breathy = (~speech) & (db > floor + 4) & (zcr > 0.25)
    secs = len(x) / SR
    voiced_s = float(speech.sum()) * HOP / SR
    words = len(text.split()) if text else 0
    return {
        "pitch_hz": _pitch(fr[speech]),
        "loud_db": float(np.median(db[speech])),
        "pace_wps": (words / voiced_s) if words and voiced_s > 0.5 else None,
        "breath": float(breathy.sum()) * HOP / SR / secs,
        "secs": round(secs, 2),
    }


def _load():
    try:
        return json.load(io.open(BASE, encoding="utf-8"))
    except Exception:
        return []


def _med(rows, k):
    v = [r[k] for r in rows if r.get(k) is not None]
    return (float(np.median(v)), float(np.std(v)) if len(v) > 2 else 0.0, len(v)) if v else (None, 0.0, 0)


def tag_for(m, rows):
    """Words for what stands out against the baseline rows; empty when it is a plain take."""
    out = []
    spec = (("pitch_hz", 0.10, 12.0, "higher pitch", "lower pitch"),
            ("pace_wps", 0.18, 0.4, "faster", "slower"),
            ("loud_db", 0.0, 4.0, "louder", "quieter"),
            ("breath", 0.0, 0.06, "breathy", None))
    for k, rel, ab, up, down in spec:
        base, sd, n = _med(rows, k)
        if base is None or m.get(k) is None or n < MIN_BASE:
            continue
        d = m[k] - base
        gate = max(ab, rel * abs(base), 1.5 * sd)
        if d > gate:
            out.append(up)
        elif d < -gate and down:
            out.append(down)
    return ", ".join(out)


def read(audio, text=""):
    """Measure, tag against the baseline, then fold this take into the baseline. Never raises."""
    try:
        m = measure(audio, text)
        if not m:
            return ""
        rows = _load()
        tag = tag_for(m, rows)
        rows.append(m)
        io.open(BASE, "w", encoding="utf-8").write(json.dumps(rows[-KEEP:]))
        return "[voice: %s]" % tag if tag else ""
    except Exception as e:
        print("  ! voiceread: %s" % e)
        return ""


if __name__ == "__main__":
    import wave
    w = wave.open(sys.argv[1])
    a = np.frombuffer(w.readframes(w.getnframes()), dtype="int16").astype("float32") / 32768
    if w.getnchannels() > 1:
        a = a.reshape(-1, w.getnchannels()).mean(axis=1)
    txt = sys.argv[2] if len(sys.argv) > 2 else ""
    print(json.dumps(measure(a, txt), indent=1))
