# -*- coding: utf-8 -*-
"""UserPromptSubmit hook (steer-02): prints one ORDER HINT line when the prompt holds a proword hit scoring >= 0.8.
Uses _tools/soi/garble.py's matcher. Never rewrites the prompt, never blocks; exit 0 always."""
import io, json, os, sys
try:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    d = json.load(sys.stdin)
    prompt = d.get("prompt") or ""
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "soi"))
    import garble
    table = garble.load_table()
    for k, v in garble.SEEDS.items():
        table.setdefault(k, []).extend(v)
    hits = [h for h in garble.find_hits(prompt, table) if h[2] >= 0.8]
    if hits:
        pw, text, sc = max(hits, key=lambda h: h[2])
        print('ORDER HINT · %s (matched "%s", %.2f)' % (pw, text, sc))
        sys.stdout.flush()
except Exception:
    pass
sys.exit(0)
