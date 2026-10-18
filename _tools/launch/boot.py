# -*- coding: utf-8 -*-
"""The boot screen (BOLO 58 · BOLO 153's first screen, Chief 10/17: "really cruncy arc linux boot sequence looking
with an ascii logo of bold venture"). launch.py opens this in its own console window and writes one JSON line per
event to boot.jsonl; this screen tails that file and draws each station as it runs:

  [  4.218] [  OK  ] AUDIT .......................... GO     1 finding · the rack

Dots fill while a station works; GO / NO-GO lands with the detail column. ALL GO closes the window after 10 s;
any NO-GO keeps it open until Enter. Zero tokens. Run by hand to replay the last launch:  python boot.py --replay
"""
import json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
EVENTS = os.path.join(HERE, "boot.jsonl")
W_NAME, W_DOTS = 10, 30

O = "\x1b[38;2;255;90;31m"      # BoldVenture orange
OB = "\x1b[1;38;2;255;90;31m"
G = "\x1b[1;32m"
R = "\x1b[1;31m"
Y = "\x1b[1;33m"
D = "\x1b[2;37m"
B = "\x1b[1;37m"
X = "\x1b[0m"

MASK = r"""
           /\               /\
          /  \             /  \
         | /\ |           | /\ |
         | || |           | || |
          \||/             \||/
     ______||_______________||______
    /                               \
   |    ________         ________    |
   |   /########\       /########\   |
    \  \########/  /^\  \########/  /
     \___________/     \___________/
"""

FONT = {
    "B": ["████ ", "█   █", "████ ", "█   █", "████ "], "O": [" ███ ", "█   █", "█   █", "█   █", " ███ "],
    "L": ["█    ", "█    ", "█    ", "█    ", "█████"], "D": ["████ ", "█   █", "█   █", "█   █", "████ "],
    "V": ["█   █", "█   █", "█   █", " █ █ ", "  █  "], "E": ["█████", "█    ", "████ ", "█    ", "█████"],
    "N": ["█   █", "██  █", "█ █ █", "█  ██", "█   █"], "T": ["█████", "  █  ", "  █  ", "  █  ", "  █  "],
    "U": ["█   █", "█   █", "█   █", "█   █", " ███ "], "R": ["████ ", "█   █", "████ ", "█  █ ", "█   █"],
}

EARLY = [   # the crunchy part: an initramfs-style preamble, ~1 s, before the real stations
    (":: running early hook", "[udev]"), (":: running hook", "[keymap]"), (":: mounting", "'/dev/q' on real root"),
    (":: loading", "the Command · SOP · BOLO · STATE"), (":: starting", "systemd-launch (BOLO 58)"),
]


def banner():
    out = [O + line + X for line in MASK.strip("\n").splitlines()]
    word = "BOLDVENTURE"
    for row in range(5):
        out.append(OB + "  " + " ".join(FONT[c][row] for c in word) + X)
    out.append(D + "  ── the Command · launch sequence ──────────────────────────────────" + X)
    return "\n".join(out)


def stamp(t0):
    return D + "[%8.3f]" % (time.time() - t0) + X


def line(name, dots, tag, verdict, note):
    return "%s %s %s %s %s" % (tag, B + name.ljust(W_NAME) + X, D + "." * dots + " " * (W_DOTS - dots) + X, verdict, note)


def read_from(pos):
    try:
        with open(EVENTS, encoding="utf-8") as f:
            f.seek(pos)
            chunk = f.read()
            return [json.loads(l) for l in chunk.splitlines() if l.strip()], f.tell()
    except (OSError, ValueError):
        return [], pos


def main():
    os.system("")                       # turns on ANSI colors in the Windows console
    if os.name == "nt":
        os.system("mode con: cols=104 lines=46 >nul 2>&1")
        os.system("title THE COMMAND · launch sequence")
    replay = "--replay" in sys.argv
    t0 = time.time()
    print(banner())
    print()
    for verb, what in EARLY:
        print("%s %s %s" % (stamp(t0), O + verb + X, what))
        time.sleep(0.12 if not replay else 0.02)
    print()
    pos, running, frame, ok, bad, done = 0, None, 0, 0, 0, False
    deadline = time.time() + 600
    while not done and time.time() < deadline:
        evs, pos = read_from(pos)
        for ev in evs:
            if ev.get("state") == "start":
                running, frame = ev["station"], 0
            elif ev.get("state") == "done":
                go = ev.get("go")
                ok += 1 if go else 0
                bad += 0 if go else 1
                tag = G + "[  OK  ]" + X if go else R + "[FAILED]" + X
                verdict = G + "GO    " + X if go else R + "NO-GO " + X
                note = (ev.get("note") or "")[:52]
                sys.stdout.write("\r\x1b[2K" + stamp(t0) + " " + line(ev["station"], W_DOTS, tag, verdict, D + note + X) + "\n")
                running = None
            elif ev.get("state") == "end":
                done = True
        if running:
            frame = min(frame + 1, W_DOTS - 1)
            spin = "|/-\\"[frame % 4]
            sys.stdout.write("\r\x1b[2K" + stamp(t0) + " " + line(running, frame, Y + "[  " + spin + "   ]" + X, Y + "....  " + X, ""))
            sys.stdout.flush()
        time.sleep(0.08 if not replay else 0.01)
    print()
    if bad:
        print(R + "  %d NO-GO" % bad + X + " · " + G + "%d GO" % ok + X + " · the sit rep carries the details")
        print(D + "  press Enter to close" + X)
        try:
            input()
        except EOFError:
            pass
    else:
        print(G + "  Reached target " + OB + "The Command" + X + G + ".  ALL GO (%d)" % ok + X)
        for n in range(10, 0, -1):
            sys.stdout.write("\r" + D + "  closing in %2d s" % n + X)
            sys.stdout.flush()
            time.sleep(1)


if __name__ == "__main__":
    main()
