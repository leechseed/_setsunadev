"""test_repos_up.py - the done check for repos_up.py (BOLO 165). Builds a FAKE Firefox session file (made-up owners,
never Chief's tabs) with a small LZ4 block encoder, runs repos_up.py --file on it, and checks the repos that come out.

Usage: python -X utf8 _tools/intake/test_repos_up.py      (exit 0 = pass)
"""
from __future__ import annotations

import json
import os
import struct
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import repos_up  # noqa: E402


def _len_bytes(n: int) -> bytes:
    out = bytearray()
    while n >= 255:
        out.append(255)
        n -= 255
    out.append(n)
    return bytes(out)


def lz4_block_encode(src: bytes) -> bytes:
    """Greedy LZ4 block encoder (enough to make real matches, so the decoder's match path is tested)."""
    out, table, i, anchor, n = bytearray(), {}, 0, 0, len(src)
    limit = n - 12  # the last match must start 12+ bytes before the end; the last 5 bytes stay literals
    while i < limit:
        key = src[i:i + 4]
        cand = table.get(key)
        table[key] = i
        if cand is None or i - cand > 0xFFFF:
            i += 1
            continue
        m = 4
        while i + m < n - 5 and src[cand + m] == src[i + m]:
            m += 1
        lit = i - anchor
        ml = m - 4
        out.append((min(lit, 15) << 4) | min(ml, 15))
        if lit >= 15:
            out += _len_bytes(lit - 15)
        out += src[anchor:i]
        out += struct.pack("<H", i - cand)
        if ml >= 15:
            out += _len_bytes(ml - 15)
        i += m
        anchor = i
    lit = n - anchor
    out.append(min(lit, 15) << 4)
    if lit >= 15:
        out += _len_bytes(lit - 15)
    out += src[anchor:]
    return bytes(out)


def tab(*urls: str, index: int | None = None) -> dict:
    return {"entries": [{"url": u, "title": "t"} for u in urls], "index": index or len(urls)}


FAKE = {
    "version": ["sessionrestore", 1],
    "windows": [
        {"tabs": [
            tab("https://github.com/fake-owner-one/widget-kit"),
            tab("https://github.com/fake-owner-one/widget-kit/tree/main/src?x=1#readme"),   # dupe after normalizing
            tab("https://example.com/not-github"),
            tab("https://github.com/fake-owner-two"),                                         # owner alone: skip
            tab("https://gist.github.com/fake-owner-two/abc123"),                             # gist: skip
            tab("https://github.com/settings/profile"),                                       # settings: skip
            tab("https://github.com/notifications"),                                          # skip
            tab("https://github.com/Fake-Owner-Two/Tiny.Lib/blob/dev/README.md"),
        ]},
        {"tabs": [
            tab("https://github.com/fake-owner-three/old-page", "https://example.org/now-here"),  # back history: skip
            tab("https://example.org/a", "https://github.com/fake-owner-three/sea-chart.git", index=2),
            tab("https://www.github.com/fake-owner-one/WIDGET-KIT/issues/4"),                  # case-blind dupe
            tab("about:newtab"),
        ]},
    ],
    "_closedWindows": [{"tabs": [tab("https://github.com/fake-closed/never-counted")]}],
}
WANT = ["fake-owner-one/widget-kit", "Fake-Owner-Two/Tiny.Lib", "fake-owner-three/sea-chart"]


def main() -> int:
    raw = json.dumps(FAKE).encode("utf-8") * 1  # one session, compressed for real below
    block = lz4_block_encode(raw)
    assert repos_up.lz4_block_decode(block, len(raw)) == raw, "LZ4 round trip failed"
    rep = (b"abcabcabc" * 400) + b"tail-bytes-here"  # overlapping matches + long lengths
    assert repos_up.lz4_block_decode(lz4_block_encode(rep), len(rep)) == rep, "LZ4 long/overlap round trip failed"

    with tempfile.TemporaryDirectory(prefix="repos_up_test_") as tmp:
        f = os.path.join(tmp, "recovery.jsonlz4")
        with open(f, "wb") as fh:
            fh.write(repos_up.MAGIC + struct.pack("<I", len(raw)) + block)
        p = subprocess.run([sys.executable, "-X", "utf8", os.path.join(HERE, "repos_up.py"), "--file", f, "--json"],
                           capture_output=True, text=True, encoding="utf-8")
        assert p.returncode == 0, p.stdout + p.stderr
        data = json.loads(p.stdout)
        got = [r["owner"] + "/" + r["repo"] for r in data["repos"]]
        assert got == WANT, f"repos: {got}"
        assert data["windows"] == 2 and data["tabs"] == 12, data
        assert data["handoff"] == "intake " + " ".join("https://github.com/" + w for w in WANT), data["handoff"]
        assert data["scan"].startswith("python _tools/intake/repo_scan.py https://github.com/"), data["scan"]
        print(f"PASS · LZ4 block {len(raw)} -> {len(block)} bytes · {data['tabs']} fake tabs in "
              f"{data['windows']} windows -> {len(got)} repos: {', '.join(got)} · "
              f"{data['github_not_repo']} other GitHub tabs skipped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
