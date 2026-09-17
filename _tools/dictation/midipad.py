"""
midipad.py — a MIDI pad as JUDY's talk button.

BOLO 56. Papi already owns an Akai MPK mini 3, so the push-to-talk hardware question
answers itself: a pad is a button, it costs nothing, and there are eight of them.

A pad sends note_on when struck and note_off when released, which maps exactly onto
hold-to-talk. Which note a given pad sends depends on the program loaded on the
device, so nothing here is hardcoded — `--learn` captures the actual note.

    python midipad.py --list          # MIDI ports
    python midipad.py --watch         # every message, to see what a pad sends
    python midipad.py --learn         # hit a pad, it is saved as the talk button
    python midipad.py --test          # prove press/release fire

Aftertouch is ignored on purpose: the MPK pads stream polyphonic pressure while held,
and treating that as a re-press would retrigger the loop dozens of times a second.
"""

import argparse
import io
import json
import os
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(HERE, "config.json")


def load():
    try:
        return json.load(io.open(CONFIG, encoding="utf-8"))
    except Exception:
        return {}


def save(patch):
    cfg = load()
    cfg.update(patch)
    io.open(CONFIG, "w", encoding="utf-8", newline="\n").write(
        json.dumps(cfg, ensure_ascii=False, indent=2) + "\n")
    return cfg


def ports():
    import mido
    return mido.get_input_names()


def find_port(want=None):
    """The configured port, else the first thing that looks like a controller."""
    names = ports()
    if not names:
        return None
    if want:
        for n in names:
            if want.lower() in n.lower():
                return n
    cfg = load().get("midi_port")
    if cfg:
        for n in names:
            if cfg.lower() in n.lower():
                return n
    for hint in ("mpk", "akai", "launch", "pad", "keystation"):
        for n in names:
            if hint in n.lower():
                return n
    return names[0]


class PadListener:
    """
    Watches one port for one note. Calls on_press when the pad goes down and
    on_release when it comes up. Runs in a daemon thread; never blocks the caller.
    """

    def __init__(self, on_press, on_release, port=None, note=None, channel=None):
        cfg = load()
        self.port_name = port or find_port()
        self.note = note if note is not None else cfg.get("midi_note")
        self.channel = channel if channel is not None else cfg.get("midi_channel")
        self.on_press = on_press
        self.on_release = on_release
        self.down = False
        self._stop = threading.Event()
        self.thread = None
        self.error = None

    def start(self):
        if self.port_name is None:
            self.error = "no MIDI input ports"
            return False
        if self.note is None:
            self.error = "no pad learned yet — run: python midipad.py --learn"
            return False
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()
        return True

    def stop(self):
        self._stop.set()

    def _match(self, msg):
        if self.channel is not None and getattr(msg, "channel", None) != self.channel:
            return False
        return getattr(msg, "note", None) == self.note

    def _run(self):
        import mido
        try:
            with mido.open_input(self.port_name) as inp:
                while not self._stop.is_set():
                    for msg in inp.iter_pending():
                        # polytouch is continuous pressure while the pad is held;
                        # it is not a press, and treating it as one retriggers madly
                        if msg.type == "polytouch":
                            continue
                        if not self._match(msg):
                            continue
                        if msg.type == "note_on" and msg.velocity > 0:
                            if not self.down:
                                self.down = True
                                self.on_press()
                        elif msg.type == "note_off" or (
                                msg.type == "note_on" and msg.velocity == 0):
                            if self.down:
                                self.down = False
                                self.on_release()
                    time.sleep(0.004)
        except Exception as e:
            self.error = str(e)


def watch(seconds=30, port=None):
    import mido
    name = find_port(port)
    if not name:
        print("  no MIDI input ports found")
        return
    print(f"  watching {name} for {seconds}s — hit pads and keys, ctrl-c to stop\n")
    seen = {}
    try:
        with mido.open_input(name) as inp:
            t0 = time.time()
            while time.time() - t0 < seconds:
                for msg in inp.iter_pending():
                    if msg.type == "polytouch":
                        continue
                    if msg.type in ("note_on", "note_off"):
                        key = (msg.channel, msg.note)
                        if msg.type == "note_on" and msg.velocity > 0:
                            seen[key] = seen.get(key, 0) + 1
                            print(f"  note {msg.note:3d}  ch {msg.channel:2d}  "
                                  f"vel {msg.velocity:3d}  DOWN")
                        else:
                            print(f"  note {msg.note:3d}  ch {msg.channel:2d}"
                                  f"{'':11s}up")
                    elif msg.type == "control_change":
                        print(f"  cc   {msg.control:3d}  ch {msg.channel:2d}  "
                              f"val {msg.value:3d}")
                time.sleep(0.004)
    except KeyboardInterrupt:
        pass
    if seen:
        print("\n  distinct pads/keys struck:")
        for (ch, note), n in sorted(seen.items()):
            print(f"    note {note:3d} on channel {ch:2d}  ({n} hit{'s' if n > 1 else ''})")


def learn(port=None, timeout=45):
    """Hit the pad you want. First note wins."""
    import mido
    name = find_port(port)
    if not name:
        print("  no MIDI input ports found")
        return None
    print(f"  port: {name}")
    print("  HIT THE PAD you want as the talk button…  (ctrl-c to cancel)")
    try:
        with mido.open_input(name) as inp:
            t0 = time.time()
            while time.time() - t0 < timeout:
                for msg in inp.iter_pending():
                    if msg.type == "note_on" and msg.velocity > 0:
                        save({"midi_port": name, "midi_note": msg.note,
                              "midi_channel": msg.channel})
                        print(f"\n  learned: note {msg.note} on channel {msg.channel}")
                        print(f"  saved to {CONFIG}")
                        return msg.note
                time.sleep(0.004)
    except KeyboardInterrupt:
        print("\n  cancelled")
        return None
    print("  timed out — nothing struck")
    return None


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="MIDI pad as the talk button (BOLO 56)")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--watch", action="store_true")
    ap.add_argument("--learn", action="store_true")
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--port")
    ap.add_argument("--seconds", type=int, default=30)
    a = ap.parse_args()

    if a.list:
        ns = ports()
        print(f"MIDI input ports ({len(ns)}):")
        for i, n in enumerate(ns):
            print(f"  [{i}] {n}")
        cfg = load()
        if cfg.get("midi_note") is not None:
            print(f"\n  talk pad: note {cfg['midi_note']} "
                  f"ch {cfg.get('midi_channel')} on {cfg.get('midi_port')}")
        else:
            print("\n  no pad learned — run: python midipad.py --learn")
        return

    if a.watch:
        watch(a.seconds, a.port)
        return

    if a.learn:
        learn(a.port)
        return

    if a.test:
        cfg = load()
        if cfg.get("midi_note") is None:
            print("  no pad learned — run --learn first")
            return
        print(f"  pad: note {cfg['midi_note']} ch {cfg.get('midi_channel')}")
        print("  press and release it; ctrl-c to stop\n")
        pl = PadListener(lambda: print("  ● DOWN — would start listening"),
                         lambda: print("  ○ UP   — would transcribe\n"))
        if not pl.start():
            print("  !", pl.error)
            return
        try:
            while True:
                time.sleep(0.2)
                if pl.error:
                    print("  !", pl.error)
                    return
        except KeyboardInterrupt:
            pl.stop()
        return

    ap.print_help()


if __name__ == "__main__":
    main()
