"""
knobs.py — the MPK rotary knobs as the scroll wheel and the zoom (BOLO 62).

Chief, 9/17: "bind one of the rotary dials … to scroll down, because my finger hurts
using this scroll wheel on the Razer" — scroll up and down, scroll X, and zoom in and
out, three knobs. Each knob turn becomes a real mouse-wheel event (Win32 SendInput), so
it lands in whatever window is under the pointer: a browser, VS Code, a PDF, the board.

    python knobs.py --list               # ports + what is bound
    python knobs.py --watch              # every knob message, to see what a knob sends
    python knobs.py --learn scroll_y     # turn the knob you want for up/down; saved
    python knobs.py --learn scroll_x     # … for left/right
    python knobs.py --learn zoom         # … for zoom in/out (ctrl + wheel)
    python knobs.py --selftest           # one wheel notch down, one back up — proves SendInput
    python knobs.py --run                # the daemon; the launch sequence starts it (KNOBS station)

The port is shareable on this box (proved 9/17: a second open beside JUDY's succeeds),
so this runs beside judy.py --session and needs no restart of her.

Knob modes. Chief's program shipped the knobs ABSOLUTE (0–127), so a knob had end stops:
at 0 or 127 it went silent until turned back. 9/17: mpkprog.py switched K1–K3 to RELATIVE
over SysEx (RAM + stored program 2) and config.json → knobs.mode is "relative"; the knobs
are endless now. Both modes are handled here, and both relative encodings are read.
"""

import argparse
import ctypes
import io
import json
import os
import sys
import time
from ctypes import wintypes

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(HERE, "config.json")

ROLES = ("scroll_y", "scroll_x", "zoom")
# Chief's MPK mini 3 program (watched 9/17): the first three knobs send CC 1 2 3 on channel 0, absolute
DEFAULT = {
    "mode": "absolute",
    "scroll_y": {"cc": 1, "notch": 2, "invert": False},   # 2 ticks per notch = half speed (Chief 9/17)
    "scroll_x": {"cc": 2, "notch": 1, "invert": False},
    "zoom":     {"cc": 3, "notch": 4, "invert": False},
}


def load():
    try:
        return json.load(io.open(CONFIG, encoding="utf-8"))
    except Exception:
        return {}


def save(patch):
    cfg = load()
    cfg.update(patch)
    io.open(CONFIG, "w", encoding="utf-8", newline="\n").write(
        json.dumps(cfg, ensure_ascii=False, indent=1) + "\n")
    return cfg


def knob_cfg():
    k = dict(DEFAULT)
    k.update(load().get("knobs") or {})
    for r in ROLES:
        base = dict(DEFAULT[r])
        base.update(k.get(r) or {})
        k[r] = base
    return k


# ---- Win32 SendInput ------------------------------------------------------------
INPUT_MOUSE, INPUT_KEYBOARD = 0, 1
MOUSEEVENTF_WHEEL, MOUSEEVENTF_HWHEEL = 0x0800, 0x1000
KEYEVENTF_KEYUP = 0x0002
VK_CONTROL = 0x11
WHEEL_DELTA = 120
ULONG_PTR = ctypes.c_size_t


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [("dx", wintypes.LONG), ("dy", wintypes.LONG), ("mouseData", wintypes.DWORD),
                ("dwFlags", wintypes.DWORD), ("time", wintypes.DWORD), ("dwExtraInfo", ULONG_PTR)]


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [("wVk", wintypes.WORD), ("wScan", wintypes.WORD), ("dwFlags", wintypes.DWORD),
                ("time", wintypes.DWORD), ("dwExtraInfo", ULONG_PTR)]


class _U(ctypes.Union):
    _fields_ = [("mi", MOUSEINPUT), ("ki", KEYBDINPUT)]


class INPUT(ctypes.Structure):
    _anonymous_ = ("u",)
    _fields_ = [("type", wintypes.DWORD), ("u", _U)]


def _wheel(delta, horizontal=False):
    i = INPUT(type=INPUT_MOUSE)
    i.mi = MOUSEINPUT(0, 0, ctypes.c_ulong(delta & 0xFFFFFFFF).value,
                      MOUSEEVENTF_HWHEEL if horizontal else MOUSEEVENTF_WHEEL, 0, 0)
    return i


def _key(vk, up=False):
    i = INPUT(type=INPUT_KEYBOARD)
    i.ki = KEYBDINPUT(vk, 0, KEYEVENTF_KEYUP if up else 0, 0, 0)
    return i


def send(*inputs):
    arr = (INPUT * len(inputs))(*inputs)
    n = ctypes.windll.user32.SendInput(len(inputs), arr, ctypes.sizeof(INPUT))
    if n != len(inputs):
        raise OSError("SendInput sent %d of %d" % (n, len(inputs)))


def scroll_y(notches):
    """+ = up (wheel away from you), - = down."""
    send(_wheel(notches * WHEEL_DELTA))


def scroll_x(notches):
    """+ = right, - = left."""
    send(_wheel(notches * WHEEL_DELTA, horizontal=True))


def zoom(notches):
    """+ = in, - = out: ctrl held around a wheel notch, the way browsers and VS Code zoom."""
    send(_key(VK_CONTROL), _wheel(notches * WHEEL_DELTA), _key(VK_CONTROL, up=True))


ACT = {"scroll_y": scroll_y, "scroll_x": scroll_x, "zoom": zoom}
# clockwise on the knob = scroll DOWN, scroll RIGHT, zoom IN (the sign of one knob tick per role)
SIGN = {"scroll_y": -1, "scroll_x": +1, "zoom": +1}


# ---- the knob reader -------------------------------------------------------------
class Knobs:
    """control_change in, wheel events out. handle(control, value, channel) is the whole API."""

    def __init__(self, cfg=None, dry=False):
        self.cfg = cfg or knob_cfg()
        self.dry = dry
        self.relative = str(self.cfg.get("mode", "absolute")).lower().startswith("rel")
        self.by_cc = {}
        for r in ROLES:
            c = self.cfg[r]
            if c.get("cc") is not None:
                self.by_cc[int(c["cc"])] = r
        self.last = {}   # cc -> last absolute value
        self.acc = {}    # role -> accumulated ticks toward the next notch
        self.count = 0

    def delta(self, cc, value):
        if self.relative:
            if 60 <= value <= 68:            # offset-64 encoders: 65 = +1, 63 = -1
                return value - 64
            return value if value < 64 else value - 128   # two's complement: 1 = +1, 127 = -1
        prev = self.last.get(cc)
        self.last[cc] = value
        if prev is None:
            return 0
        d = value - prev
        if abs(d) > 32:      # a pickup jump, not a turn
            return 0
        return d

    def handle(self, control, value, channel=None):
        role = self.by_cc.get(control)
        if role is None:
            return
        c = self.cfg[role]
        if c.get("channel") is not None and channel is not None and channel != c["channel"]:
            return
        d = self.delta(control, value)
        if not d:
            return
        step = SIGN[role] * (-1 if c.get("invert") else 1)
        notch = max(1, int(c.get("notch") or 1))
        self.acc[role] = self.acc.get(role, 0) + d
        n = int(self.acc[role] / notch)
        if n == 0:
            return
        self.acc[role] -= n * notch
        self.count += 1
        if self.dry:
            print("  %-8s %+d" % (role, n * step))
            return
        try:
            ACT[role](n * step)
        except Exception as e:
            print("  ! %s: %s" % (role, e))


def find_port(want=None):
    import midipad
    return midipad.find_port(want)


def run(port=None, dry=False, quiet=False):
    import mido
    name = find_port(port)
    if not name:
        print("  no MIDI input ports found")
        return 2
    k = Knobs(dry=dry)
    if not quiet:
        print("  knobs · %s · mode %s" % (name, "relative" if k.relative else "absolute"))
        for r in ROLES:
            print("    %-8s cc %s · %d tick(s) per notch%s" % (
                r, k.cfg[r].get("cc"), int(k.cfg[r].get("notch") or 1),
                " · inverted" if k.cfg[r].get("invert") else ""))
        print("  turning · ctrl-c to stop\n")
    try:
        with mido.open_input(name) as inp:
            while True:
                for msg in inp.iter_pending():
                    if msg.type == "control_change":
                        k.handle(msg.control, msg.value, msg.channel)
                time.sleep(0.003)
    except KeyboardInterrupt:
        return 0
    except Exception as e:
        print("  !", e)
        return 1


def watch(seconds=20, port=None):
    import mido
    name = find_port(port)
    if not name:
        print("  no MIDI input ports found")
        return
    print("  watching %s for %ds — turn knobs, ctrl-c to stop\n" % (name, seconds))
    try:
        with mido.open_input(name) as inp:
            t0 = time.time()
            while time.time() - t0 < seconds:
                for msg in inp.iter_pending():
                    if msg.type == "control_change":
                        print("  cc %3d  ch %2d  val %3d" % (msg.control, msg.channel, msg.value))
                time.sleep(0.004)
    except KeyboardInterrupt:
        pass


def learn(role, port=None, timeout=30):
    import mido
    name = find_port(port)
    if not name:
        print("  no MIDI input ports found")
        return None
    print("  port: %s" % name)
    print("  TURN THE KNOB you want for %s…  (ctrl-c to cancel)" % role.replace("_", " "))
    try:
        with mido.open_input(name) as inp:
            t0 = time.time()
            while time.time() - t0 < timeout:
                for msg in inp.iter_pending():
                    if msg.type == "control_change":
                        k = load().get("knobs") or {}
                        entry = dict(DEFAULT[role])
                        entry.update(k.get(role) or {})
                        entry["cc"] = msg.control
                        entry["channel"] = msg.channel
                        k[role] = entry
                        k.setdefault("mode", DEFAULT["mode"])
                        save({"knobs": k, "midi_port": name})
                        print("\n  learned: %s = cc %d on channel %d" % (role, msg.control, msg.channel))
                        print("  saved to %s" % CONFIG)
                        return msg.control
                time.sleep(0.004)
    except KeyboardInterrupt:
        print("\n  cancelled")
        return None
    print("  timed out — nothing turned")
    return None


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="MPK knobs as scroll and zoom (BOLO 62)")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--watch", action="store_true")
    ap.add_argument("--learn", choices=ROLES, help="turn the knob for this role")
    ap.add_argument("--run", action="store_true", help="the daemon")
    ap.add_argument("--dry", action="store_true", help="with --run: print, don't scroll")
    ap.add_argument("--selftest", action="store_true", help="one notch down, one notch up, under the pointer")
    ap.add_argument("--port")
    ap.add_argument("--seconds", type=int, default=20)
    ap.add_argument("--timeout", type=int, default=30)
    a = ap.parse_args()

    if a.list:
        import midipad
        ns = midipad.ports()
        print("MIDI input ports (%d):" % len(ns))
        for i, n in enumerate(ns):
            print("  [%d] %s" % (i, n))
        k = knob_cfg()
        learned = load().get("knobs") or {}
        print("\n  mode %s" % k.get("mode"))
        for r in ROLES:
            print("  %-8s cc %s%s" % (r, k[r].get("cc"),
                                      "" if learned.get(r) else "  (built-in default, not learned)"))
        return
    if a.watch:
        watch(a.seconds, a.port)
        return
    if a.learn:
        learn(a.learn, a.port, a.timeout)
        return
    if a.selftest:
        scroll_y(-1)
        time.sleep(0.25)
        scroll_y(+1)
        print("  sent one wheel notch down and one up under the pointer — SendInput works")
        return
    if a.run:
        sys.exit(run(a.port, a.dry))
    ap.print_help()


if __name__ == "__main__":
    main()
