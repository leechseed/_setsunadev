# -*- coding: utf-8 -*-
"""chirp.py — the PTT chirp (BOLO 114): early-2000s walkie-talkie beeps, synthesized here.

All sounds are original generic two-tone beeps made with the stdlib; nothing sampled or copied.
  open.wav   pad down, channel clear: two quick rising tones
  sent.wav   pad up: the roger beep, one falling tone
  busy.wav   pad down while JUDY is speaking: two low blips
Files land in sounds/ and carry the volume in their name (open_35.wav), so a changed
volume in judy.json["ptt_chirp"] regenerates on the next use.
"""
import io
import json
import math
import os
import struct
import wave

HERE = os.path.dirname(os.path.abspath(__file__))
SOUNDS = os.path.join(HERE, "sounds")
RATE = 22050
LEAD_S = 0.10   # recording starts this long after the open chirp so the mic never hears it


def cfg():
    try:
        with io.open(os.path.join(HERE, "judy.json"), encoding="utf-8") as f:
            c = json.load(f).get("ptt_chirp") or {}
    except Exception:
        c = {}
    try:
        vol = max(0.0, min(1.0, float(c.get("volume", 0.35))))
    except Exception:
        vol = 0.35
    return {"on": bool(c.get("on", True)), "volume": vol}


def _tone(f0, f1, ms, vol, square=0.35):
    """One tone gliding f0->f1; a little square edge mixed in; 5 ms fades."""
    n = int(RATE * ms / 1000.0)
    fade = int(RATE * 0.005)
    out, ph = [], 0.0
    for i in range(n):
        f = f0 + (f1 - f0) * i / max(1, n - 1)
        ph += 2 * math.pi * f / RATE
        s = math.sin(ph)
        sq = 1.0 if s >= 0 else -1.0
        v = (1 - square) * s + square * sq
        env = min(1.0, i / fade, (n - 1 - i) / fade) if fade else 1.0
        out.append(v * env * vol)
    return out


def _gap(ms):
    return [0.0] * int(RATE * ms / 1000.0)


def _write(path, samples):
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        w.writeframes(b"".join(struct.pack("<h", int(max(-1.0, min(1.0, s)) * 32767)) for s in samples))


def _build(vol):
    return {
        "open": _tone(1300, 1300, 45, vol) + _tone(1900, 1900, 45, vol),
        "sent": _tone(1800, 1150, 70, vol),
        "busy": _tone(420, 420, 60, vol, square=0.5) + _gap(40) + _tone(420, 420, 60, vol, square=0.5),
    }


def path_for(name, vol=None):
    vol = cfg()["volume"] if vol is None else vol
    return os.path.join(SOUNDS, f"{name}_{int(round(vol * 100))}.wav")


def ensure():
    """Generate any missing WAV for the current volume (and drop stale-volume files). Never raises."""
    try:
        vol = cfg()["volume"]
        os.makedirs(SOUNDS, exist_ok=True)
        tag = f"_{int(round(vol * 100))}.wav"
        for fn in os.listdir(SOUNDS):
            if fn.endswith(".wav") and fn.split("_")[0] in ("open", "sent", "busy") and not fn.endswith(tag):
                try:
                    os.remove(os.path.join(SOUNDS, fn))
                except Exception:
                    pass
        built = None
        for name in ("open", "sent", "busy"):
            p = path_for(name, vol)
            if not os.path.exists(p):
                built = built or _build(vol)
                _write(p, built[name])
        return {n: path_for(n, vol) for n in ("open", "sent", "busy")}
    except Exception:
        return {}


def play(name):
    """Async, never blocks, never raises. Returns True if a chirp was started."""
    try:
        if not cfg()["on"]:
            return False
        p = ensure().get(name)
        if not p:
            return False
        import winsound
        winsound.PlaySound(p, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NODEFAULT)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    for n, p in ensure().items():
        with wave.open(p) as w:
            print(n, p, f"{w.getnframes() / w.getframerate() * 1000:.0f} ms")
