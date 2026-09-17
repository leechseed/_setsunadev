"""
mpkprog.py — read and write the MPK mini 3's program over SysEx (BOLO 62).

Why: the knobs are endless encoders, but the program sends them ABSOLUTE (0–127), so a
knob goes silent at the top of its count and the page stops scrolling. RELATIVE mode
sends "one click" instead of "I am at 127". The Akai editor is not installed; the
device takes its program straight over the wire, so this does the one edit itself.

    python mpkprog.py --dump             # the live (RAM) program, decoded — read only
    python mpkprog.py --dump 1           # stored program 1 (1–8)
    python mpkprog.py --rel 1 2 3        # knobs 1 2 3 → relative, written to RAM (live now)
    python mpkprog.py --rel 1 2 3 --persist   # also into the stored slot the RAM matches
    python mpkprog.py --abs 1 2 3        # back to absolute

Layout (community-documented for the mk3; every byte is 7-bit):
    request  F0 47 7F 49 66 00 01 <prog> F7          prog 0 = RAM, 1–8 = stored
    answer   F0 47 7F 49 67 <len hi> <len lo> <prog> <data ×245> F7
    write    F0 47 7F 49 64 <len hi> <len lo> <prog> <data ×245> F7
    data     0–15 program name ("PGM:…") · 16 pad ch · 17 aftertouch · 18 key ch · 19 octave · 20–29 arp+tempo
             30–35 joystick · 36–83 pads (16 × note cc pc) · 84–243 knobs (8 × mode cc min max name[16]) · 244 transpose
    (verified against Chief's device 9/17: pad ch 9, pad notes 36–51, knobs cc 1–8, all read back where written)
    knob mode byte: 0 = absolute, 1 = relative

The dump is verified before any write: the knob CCs must read as the wire showed them
(1 2 3 …) and the pad channel must match config.json's talk pad; otherwise nothing is sent.
"""

import argparse
import io
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(HERE, "config.json")

AKAI, DEV, MPK3 = 0x47, 0x7F, 0x49
CMD_DUMP, CMD_REQUEST, CMD_REPLY = 0x64, 0x66, 0x67   # 64 = program in, 66 = ask, 67 = the device's answer
KNOBS_AT, KNOB_LEN, NKNOBS = 84, 20, 8
NAME_AT, PADCH_AT, PADS_AT, PAD_LEN = 0, 16, 36, 3
DATA_LEN = 245


def ports():
    import mido
    ins = [n for n in mido.get_input_names() if "mpk" in n.lower()]
    outs = [n for n in mido.get_output_names() if "mpk" in n.lower()]
    if not ins or not outs:
        raise SystemExit("  MPK mini 3 not found on the MIDI ports")
    return ins[0], outs[0]


def request(prog=0, timeout=3.0):
    """Ask the device for a program; return (prog, data bytes) or None."""
    import mido
    inp_name, out_name = ports()
    with mido.open_input(inp_name) as inp, mido.open_output(out_name) as out:
        for _ in inp.iter_pending():
            pass
        out.send(mido.Message("sysex", data=[AKAI, DEV, MPK3, CMD_REQUEST, 0x00, 0x01, prog]))
        t0 = time.time()
        while time.time() - t0 < timeout:
            for msg in inp.iter_pending():
                # the device answers with device id 00 where we sent 7F; match maker + product + command only
                if msg.type == "sysex" and msg.data[0] == AKAI and msg.data[2] == MPK3 and msg.data[3] in (CMD_REPLY, CMD_DUMP):
                    d = list(msg.data)
                    length = (d[4] << 7) | d[5]
                    body = d[6:]
                    return {"prog": body[0], "len": length, "data": body[1:]}
            time.sleep(0.01)
    return None


def write(prog, data):
    import mido
    _, out_name = ports()
    length = len(data) + 1
    payload = [AKAI, DEV, MPK3, CMD_DUMP, (length >> 7) & 0x7F, length & 0x7F, prog] + list(data)
    with mido.open_output(out_name) as out:
        out.send(mido.Message("sysex", data=payload))


def knob(data, k):
    o = KNOBS_AT + KNOB_LEN * (k - 1)
    blk = data[o:o + KNOB_LEN]
    name = "".join(chr(b) for b in blk[4:20] if 32 <= b < 127).strip()
    return {"k": k, "mode": blk[0], "cc": blk[1], "min": blk[2], "max": blk[3], "name": name, "at": o}


def decode(d):
    data = d["data"]
    out = ["  program %s · %d bytes (%d expected)" % ("RAM (live)" if d["prog"] == 0 else d["prog"], len(data), DATA_LEN),
           "  name %s" % "".join(chr(b) for b in data[NAME_AT:NAME_AT + 16] if 32 <= b < 127),
           "  pad channel %d · aftertouch %d · key channel %d · octave %d" % (data[PADCH_AT], data[PADCH_AT + 1], data[PADCH_AT + 2], data[PADCH_AT + 3]),
           "  pads A: notes %s" % " ".join(str(data[PADS_AT + PAD_LEN * i]) for i in range(8)),
           "  knobs:"]
    for k in range(1, NKNOBS + 1):
        kn = knob(data, k)
        out.append("    K%d  %-8s cc %3d  range %3d–%3d  %s" % (
            k, "RELATIVE" if kn["mode"] == 1 else "absolute", kn["cc"], kn["min"], kn["max"], kn["name"]))
    return "\n".join(out)


def verify(d):
    """The layout guard: the knob CCs and the pad channel must match what the wire already showed."""
    data = d["data"]
    problems = []
    if len(data) != DATA_LEN:
        problems.append("length %d, expected %d" % (len(data), DATA_LEN))
    try:
        cfg = json.load(io.open(CONFIG, encoding="utf-8"))
    except Exception:
        cfg = {}
    kn = cfg.get("knobs") or {}
    want = {1: (kn.get("scroll_y") or {}).get("cc"), 2: (kn.get("scroll_x") or {}).get("cc"), 3: (kn.get("zoom") or {}).get("cc")}
    for k, cc in want.items():
        if cc is not None and knob(data, k)["cc"] != cc:
            problems.append("K%d reads cc %d, the wire showed cc %d" % (k, knob(data, k)["cc"], cc))
    if cfg.get("midi_channel") is not None and data[PADCH_AT] != cfg["midi_channel"]:
        problems.append("pad channel reads %d, the talk pad is on %d" % (data[PADCH_AT], cfg["midi_channel"]))
    if cfg.get("midi_note") is not None and cfg["midi_note"] not in [data[PADS_AT + PAD_LEN * i] for i in range(16)]:
        problems.append("the talk pad's note %d is not among the pad notes" % cfg["midi_note"])
    for k in range(1, NKNOBS + 1):
        if knob(data, k)["mode"] not in (0, 1):
            problems.append("K%d mode byte %d is neither 0 nor 1" % (k, knob(data, k)["mode"]))
    return problems


def set_mode(data, knobs, mode):
    data = list(data)
    for k in knobs:
        data[KNOBS_AT + KNOB_LEN * (k - 1)] = mode
    return data


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="MPK mini 3 program over SysEx (BOLO 62)")
    ap.add_argument("--dump", nargs="?", const=0, type=int, metavar="PROG", help="decode a program (0 = live RAM)")
    ap.add_argument("--rel", nargs="+", type=int, metavar="K", help="set these knobs (1–8) to relative")
    ap.add_argument("--abs", nargs="+", type=int, metavar="K", help="set these knobs (1–8) to absolute")
    ap.add_argument("--persist", action="store_true", help="also write the stored slot whose contents match RAM")
    a = ap.parse_args()

    if a.dump is not None:
        d = request(a.dump)
        if not d:
            print("  no dump came back (is the device on program %d?)" % a.dump)
            sys.exit(1)
        print(decode(d))
        p = verify(d)
        print("\n  layout check: " + ("OK — matches the wire" if not p else "FAILED\n    " + "\n    ".join(p)))
        return

    if a.rel or a.abs:
        knobs = a.rel or a.abs
        mode = 1 if a.rel else 0
        d = request(0)
        if not d:
            print("  no RAM dump came back; nothing written")
            sys.exit(1)
        p = verify(d)
        if p:
            print("  layout check FAILED; nothing written:\n    " + "\n    ".join(p))
            sys.exit(1)
        new = set_mode(d["data"], knobs, mode)
        write(0, new)
        time.sleep(0.3)
        back = request(0)
        ok = back and all(knob(back["data"], k)["mode"] == mode for k in knobs)
        word = "relative" if mode else "absolute"
        print("  RAM: K%s → %s · %s" % ("/K".join(str(k) for k in knobs), word, "read back OK" if ok else "READ-BACK MISMATCH"))
        if not ok:
            sys.exit(1)
        if a.persist:
            slot = None
            for s in range(1, 9):
                sd = request(s)
                if sd and sd["data"] == d["data"]:
                    slot = s
                    break
            if slot is None:
                print("  persist: no stored slot matches the live program; RAM only (lost on power-off)")
                return
            write(slot, new)
            time.sleep(0.3)
            sb = request(slot)
            ok = sb and all(knob(sb["data"], k)["mode"] == mode for k in knobs)
            print("  stored program %d: %s" % (slot, "written, read back OK" if ok else "READ-BACK MISMATCH"))
        return

    ap.print_help()


if __name__ == "__main__":
    main()
