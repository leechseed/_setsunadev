# -*- coding: utf-8 -*-
"""BOLO close: move finished rows from the active table to the Done table, stamped (11/04, the docket).

Usage:  python _tools/bolo/close.py <n> [<n> ...] --why "<who said what>" [--dry] [--json]

Does:   each named row leaves "## Active BOLOs" and lands in "## Done" as `| ✅ n | ... | status · ✅ CLOSED <date> (why) |`.
        The ✅ before the number keeps Done rows out of every active-row parser (digest, add.py, the boards).
        Active rows found below "## Done" (add.py's old append spot) move back into the active table, in order.
        The header `updated:` is stamped today. Refuses an unknown number; never deletes a row.
"""
import datetime, io, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
ROW = re.compile(r"^\| (\d+) \| .+\|$")


def main():
    a = sys.argv[1:]
    dry, as_json = ("--dry" in a or "--dry-run" in a), "--json" in a
    why = a[a.index("--why") + 1] if "--why" in a else "closed"
    nums = [int(x) for x in a if x.isdigit()]
    if not nums:
        print(__doc__); return 2
    today = datetime.date.today()
    bp = os.path.join(ROOT, "BOLO.md")
    lines = io.open(bp, encoding="utf-8").read().split("\n")
    i_act = lines.index("## Active BOLOs")
    i_pmcs = next(i for i, l in enumerate(lines) if l.startswith("## PMCS"))
    i_done = lines.index("## Done")

    active, stray, done_rows = [], [], []
    for i, l in enumerate(lines):
        m = ROW.match(l)
        if not m:
            continue
        (active if i < i_pmcs else stray).append((int(m.group(1)), i, l))
    have = {n for n, _, _ in active + stray}
    unknown = [n for n in nums if n not in have]
    if unknown:
        print("unknown or already closed: %s" % unknown); return 1

    stamp = " · ✅ **CLOSED %d/%d** (%s)" % (today.month, today.day, why)
    for n, i, l in active + stray:
        if n in nums:
            body = l[len("| %d " % n):]
            done_rows.append("| ✅ %d %s" % (n, body[:-1].rstrip() + stamp + " |"))
    keep_active = [l for n, i, l in active if n not in nums]
    keep_stray = [l for n, i, l in sorted(stray) if n not in nums]

    # rebuild: everything before the first active row, the active rows (+ strays), the gap to Done, Done
    first = min(i for _, i, _ in active)
    last = max(i for _, i, _ in active)
    head = lines[:first]
    mid = lines[last + 1:i_done + 1]
    tail = [l for l in lines[i_done + 1:] if not ROW.match(l)]
    tail = [l for l in tail if not l.startswith("*(empty")]
    old_done = [l for l in tail if l.startswith("| ✅ ")]
    rest = [l for l in tail if not l.startswith("| ✅ ") and l not in ("| # | Order | Issued | Status |", "|---|---|---|---|")]
    while rest and rest[0] == "":
        rest.pop(0)
    done_block = ["", "| # | Order | Issued | Status |", "|---|---|---|---|"] + old_done + done_rows
    out = head + keep_active + keep_stray + mid + done_block + ([""] + rest if rest else [""])
    text = "\n".join(out)
    text = re.sub(r"^updated: .*$", "updated: %s" % today.isoformat(), text, count=1, flags=re.M)

    res = {"closed": [n for n in nums], "moved_back": [n for n, _, _ in stray if n not in nums],
           "active_left": len(keep_active) + len(keep_stray), "done_total": len(old_done) + len(done_rows)}
    if not dry:
        io.open(bp, "w", encoding="utf-8", newline="\r\n").write(text)   # BOLO.md is CRLF
    print(json.dumps(res) if as_json else "BOLO close%s · %d closed · %d active left · %d moved back above Done" % (
        " (dry)" if dry else "", len(nums), res["active_left"], len(res["moved_back"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
