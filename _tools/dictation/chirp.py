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


def _send(vol):
    """Dry relay click (8 ms band-passed noise) + soft two-partial sine tail, ~180 ms, no reverb."""
    import random
    rnd = random.Random(114)
    nc = int(RATE * 0.008)
    lp1 = lp2 = 0.0
    a_hi, a_lo = 0.12, 0.55   # crude band-pass: ~0.4k..3k one-pole difference
    click = []
    for i in range(nc):
        x = rnd.uniform(-1, 1)
        lp1 += a_hi * (x - lp1)
        lp2 += a_lo * (x - lp2)
        click.append((lp2 - lp1) * math.exp(-5.0 * i / nc) * 1.6 * vol)
    n = int(RATE * 0.172)
    fade = int(RATE * 0.003)
    tail = []
    for i in range(n):
        t = i / RATE
        v = 0.6 * math.sin(2 * math.pi * 520 * t) + 0.4 * math.sin(2 * math.pi * 783 * t)
        env = math.exp(-t / 0.045) * min(1.0, i / fade)
        tail.append(v * env * 0.8 * vol)
    out = [0.0] * len(tail)
    for i, c in enumerate(click):
        out[i] += c
    for i in range(len(tail)):
        out[i] += tail[i]
    return out


def _bell(f, ms, vol):
    """One struck chime: a sine with two soft overtones and a long exponential ring."""
    n = int(RATE * ms / 1000.0)
    att = int(RATE * 0.004)
    out = []
    for i in range(n):
        t = i / RATE
        v = math.sin(2 * math.pi * f * t) + 0.35 * math.sin(2 * math.pi * 2 * f * t) + 0.12 * math.sin(2 * math.pi * 3 * f * t)
        out.append(v / 1.47 * math.exp(-t / 0.32) * min(1.0, i / att) * vol)
    return out


def _chime(f1, f2, vol):
    """The cockpit two-tone (BOLO 122, Chief 10/6: "a bing bong ... like a cockpit thing"); the second note
    strikes while the first still rings. Original, synthesized here, nothing sampled."""
    a, b = _bell(f1, 900, vol), _bell(f2, 1100, vol)
    off = int(RATE * 0.42)
    out = a + [0.0] * (off + len(b) - len(a))
    for i, x in enumerate(b):
        out[off + i] += x
    return out


def _buzz(f0, f1, ms, gate_hz, vol):
    """A gated buzz: a bright saw/square carrier gliding f0->f1, chopped at gate_hz (the "BRRRT")."""
    n = int(RATE * ms / 1000.0)
    out, ph = [], 0.0
    for i in range(n):
        f = f0 + (f1 - f0) * i / max(1, n - 1)
        ph += f / RATE
        frac = ph % 1.0
        saw = 2.0 * frac - 1.0
        sq = 1.0 if frac < 0.5 else -1.0
        gate = 1.0 if ((i / RATE) * gate_hz) % 1.0 < 0.62 else 0.08
        env = min(1.0, i / (RATE * 0.003), (n - 1 - i) / (RATE * 0.004))
        out.append((0.55 * saw + 0.45 * sq) * gate * env * vol * 0.75)
    return out


def _critical(up, vol):
    """The critical model call (BOLO 122, Chief 10/6: "more urgent ... a critical, like a Bram-B-B-B-B-Ht"):
    two HUD bursts, each a chopped buzz that ends in a hard high tick. Up = the buzz climbs; down = it falls."""
    f0, f1, tick = (480, 760, 1900) if up else (760, 480, 1250)
    burst = _buzz(f0, f1, 380, 30, vol) + _gap(28) + _tone(tick, tick, 42, vol * 0.9, square=0.7)
    return burst + _gap(140) + burst


def _build(vol):
    return {
        "send": _send(vol),
        "open": _tone(1300, 1300, 45, vol) + _tone(1900, 1900, 45, vol),
        "sent": _tone(1800, 1150, 70, vol),
        "busy": _tone(420, 420, 60, vol, square=0.5) + _gap(40) + _tone(420, 420, 60, vol, square=0.5),
        # focus pad (Chief 10/6): a soft lock-on, an upward glide then one high tick; original, no sample
        "focus": _tone(700, 1400, 35, vol * 0.8, square=0.1) + _gap(15) + _tone(2200, 2200, 15, vol * 0.6, square=0.0),
        # the model call (BOLO 122): the critical burst; the buzz climbs going up to a stronger model, falls coming back down (the bell chime retired same night)
        "escalate": _critical(True, vol),
        "deescalate": _critical(False, vol),
        # the reconfirm (BOLO 122, Chief 10/6: "a reconfirm ... to make sure that I did switch"): a clean two-step lock
        "confirm": _tone(880, 880, 60, vol, square=0.1) + _gap(30) + _tone(1320, 1320, 110, vol, square=0.1),
        # the relay (Chief 10/13: "instead of the word relay ... a fucking UI sound"): an agent or the harness reported in.
        # A data-packet blip: three soft rising ticks, quieter than the pad chirps, ~120 ms; original, no sample.
        "relay": _tone(1400, 1400, 18, vol * 0.55, square=0.0) + _gap(22) + _tone(1750, 1750, 18, vol * 0.55, square=0.0)
                 + _gap(22) + _tone(2100, 2350, 30, vol * 0.5, square=0.0),
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
            if fn.endswith(".wav") and fn.split("_")[0] in ("open", "sent", "busy", "send", "focus", "escalate", "deescalate", "confirm", "relay") and not fn.endswith(tag):
                try:
                    os.remove(os.path.join(SOUNDS, fn))
                except Exception:
                    pass
        built = None
        for name in ("open", "sent", "busy", "send", "focus", "escalate", "deescalate", "confirm", "relay"):
            p = path_for(name, vol)
            if not os.path.exists(p):
                built = built or _build(vol)
                _write(p, built[name])
        return {n: path_for(n, vol) for n in ("open", "sent", "busy", "send", "focus", "escalate", "deescalate", "confirm", "relay")}
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
