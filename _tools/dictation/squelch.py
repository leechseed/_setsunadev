# -*- coding: utf-8 -*-
"""squelch.py — the radio squelch around everything JUDY says (Chief, 9/17).

Key-up plays before her first sentence of a block (and before an acknowledgment);
key-down plays after her last sentence (and after an interrupt cuts her off).

Sounds live in _tools/dictation/sfx/:  key-up.wav · key-down.wav
Drop your own files there under those names and they are used as-is (16-bit PCM WAV,
any rate winsound accepts). If a file is missing, a stand-in burst is generated once
so the timing can be heard before the real sound lands.

judy.json → "session": {"squelch": {"enabled": true, "up": "<path>", "down": "<path>"}}
(paths optional; the sfx/ defaults apply when absent). Console knobs can follow.
"""
import io, os, json, math, wave, struct, random, time

HERE = os.path.dirname(os.path.abspath(__file__))
SFX = os.path.join(HERE, "sfx")
JUDY = os.path.join(HERE, "judy.json")
DEFAULT = {"enabled": True,
           "up": os.path.join(SFX, "key-up.wav"),
           "down": os.path.join(SFX, "key-down.wav")}


def cfg():
    try:
        j = json.load(io.open(JUDY, encoding="utf-8"))
        s = (j.get("session") or {}).get("squelch") or {}
        return {**DEFAULT, **{k: v for k, v in s.items() if v not in (None, "")}}
    except Exception:
        return dict(DEFAULT)


def _write(path, samples, rate=22050):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with wave.open(path, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate)
        w.writeframes(b"".join(struct.pack("<h", max(-32767, min(32767, int(v * 32767)))) for v in samples))


def _burst(ms, rate=22050, gain=0.35, tail=True):
    """A band-limited noise burst with a fast attack and a decaying tail: the classic squelch."""
    n = int(rate * ms / 1000)
    out, prev = [], 0.0
    for i in range(n):
        x = random.uniform(-1, 1)
        prev = 0.55 * prev + 0.45 * x                 # crude low-pass so it is a hiss, not a crackle
        env = 1.0 if i < n * 0.15 else math.exp(-4.0 * (i - n * 0.15) / n) if tail else 1.0
        out.append(prev * gain * env)
    return out


def _click(rate=22050, gain=0.5):
    n = int(rate * 0.012)
    return [gain * math.sin(2 * math.pi * 1800 * i / rate) * (1 - i / n) for i in range(n)]


def ensure_defaults():
    c = cfg()
    if not os.path.exists(c["up"]):
        # key-up: a click then a short hiss opening
        _write(c["up"], _click() + _burst(70, tail=False, gain=0.25) + [0.0] * 200)
    if not os.path.exists(c["down"]):
        # key-down: the hiss tail, then the click of the carrier dropping
        _write(c["down"], _burst(110, gain=0.3) + [0.0] * 120 + _click(gain=0.35))
    return c


def _play_sync(path):
    try:
        import winsound
        winsound.PlaySound(path, winsound.SND_FILENAME)   # synchronous: returns when the clip ends
    except Exception:
        pass


def key_up():
    c = ensure_defaults()
    if c.get("enabled", True) and os.path.exists(c["up"]):
        _play_sync(c["up"])


def key_down():
    c = ensure_defaults()
    if c.get("enabled", True) and os.path.exists(c["down"]):
        _play_sync(c["down"])


if __name__ == "__main__":
    c = ensure_defaults()
    print("key-up  ", c["up"]); key_up(); time.sleep(0.3)
    print("key-down", c["down"]); key_down()
