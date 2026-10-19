# -*- coding: utf-8 -*-
"""BOLO 159: the working mode. `mode.py <research|design|build>` switches it; `mode.py show [--json]` reads it.
One file, modes.json, holds the active mode and the three definitions. An unknown name exits 2 and writes nothing.
--dry-run says what the switch would write and writes nothing."""
import io, os, sys, json, time

FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "modes.json")


def load():
    with io.open(FILE, encoding="utf-8") as f:
        return json.load(f)


def main(argv):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = [a for a in argv if not a.startswith("--")]
    as_json, dry = "--json" in argv, "--dry-run" in argv
    d = load()
    cmd = args[0] if args else "show"
    if cmd == "show":
        m = d["modes"][d["active"]]
        if as_json:
            print(json.dumps({"active": d["active"], "since": d["since"], **m}, ensure_ascii=False, indent=1))
        else:
            print("MODE · %s since %s · may: %s · may not: %s · model: %s" % (d["active"].upper(), d["since"], m["may"], m["may_not"], m["model"]))
        return 0
    if cmd not in d["modes"]:
        print("unknown mode %r; one of: %s" % (cmd, ", ".join(d["modes"])), file=sys.stderr)
        return 2
    since = time.strftime("%Y-%m-%d %H:%M")
    if dry:
        print("would set active=%s since=%s (nothing written)" % (cmd, since))
        return 0
    d["active"], d["since"], d["set_by"] = cmd, since, "proword"
    with io.open(FILE, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("MODE · %s since %s · model: %s" % (cmd.upper(), since, d["modes"][cmd]["model"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
