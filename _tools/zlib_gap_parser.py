# zlib_gap_parser.py — fuzzy-diff the z-lib favorites export against the BVX catalog
# Companion to zlib_favorites_walker.js (which produces the export).
# INPUT:  Desktop\_BVX_INBOX\zlib\zlib-favorites.txt  (one "Author — Title" per line)
#         _0.1_BVX_LEARN/_meta/catalog.json           (the 1,106-source catalog)
# OUTPUT: _0.1_BVX_LEARN/_meta/ZLIB-GAP-REPORT.md     (three lists: catalogued / THE GAP / maybes)
#         _0.1_BVX_LEARN/_meta/zlib_gap.json          (machine-readable, feeds acquisition tooling)
# Read-only against its inputs; safe to rerun after any new export.

import json
import re
import sys
import unicodedata
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FAVORITES = Path(r"C:\Users\U01_LEECHSEED\Desktop\_BVX_INBOX\zlib\zlib-favorites.txt")
CATALOG = REPO / "_0.1_BVX_LEARN" / "_meta" / "catalog.json"
REPORT_MD = REPO / "_0.1_BVX_LEARN" / "_meta" / "ZLIB-GAP-REPORT.md"
REPORT_JSON = REPO / "_0.1_BVX_LEARN" / "_meta" / "zlib_gap.json"

MATCH_T = 0.90        # score at/above → already catalogued
MATCH_T_AUTHOR = 0.88 # slightly lowered bar when author tokens also overlap
MAYBE_T = 0.76        # between this and match → review-queue maybe

STOP = {"the", "a", "an", "of", "and", "in", "on", "to", "for", "with", "at",
        "by", "from", "how", "why", "what", "its", "is", "are", "vol", "volume",
        "edition", "ed", "revised", "new", "series", "guide", "book", "handbook"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower().replace("&", " and ")
    s = re.sub(r"\b(97[89])?\d{9}[\dx]\b", " ", s)          # ISBNs
    s = re.sub(r"\b(\d+(st|nd|rd|th)|first|second|third|fourth|fifth|sixth)\s+(edition|ed)\b\.?", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def title_core(s: str) -> str:
    # cut subtitle at first colon / " - ", strip trailing parentheticals
    s = re.sub(r"\([^)]*\)\s*$", "", s)
    s = re.split(r":|\s-\s|\u2014|\u2013", s, maxsplit=1)[0]
    return norm(s)


def tokens(s: str) -> set:
    return {t for t in s.split() if t not in STOP and len(t) > 2}


def subtitle(s: str) -> str:
    parts = re.split(r":|\s-\s|—|–", s, maxsplit=1)
    return norm(parts[1]) if len(parts) == 2 else ""


def score(a: str, b: str) -> float:
    seq = SequenceMatcher(None, a, b).ratio()
    ta, tb = tokens(a), tokens(b)
    jac = len(ta & tb) / len(ta | tb) if ta | tb else 0.0
    return max(seq, (seq + jac) / 2 + 0.1 * (jac == 1.0))


def main() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    cat = []
    tok_index = defaultdict(set)
    full_index = defaultdict(list)
    core_index = defaultdict(list)
    for i, e in enumerate(catalog):
        nt, ct = norm(e["t"]), title_core(e["t"])
        na = norm(e.get("a", ""))
        cat.append({"nt": nt, "ct": ct, "na_tok": tokens(na) | set(na.split()), "e": e})
        full_index[nt].append(i)
        if ct:
            core_index[ct].append(i)
        for t in tokens(nt):
            tok_index[t].add(i)

    lines = [ln.strip() for ln in FAVORITES.read_text(encoding="utf-8").splitlines() if ln.strip()]
    catalogued, gap, maybes = [], [], []

    for ln in lines:
        parts = ln.split(" \u2014 ", 1)
        author, title = (parts[0], parts[1]) if len(parts) == 2 else ("", parts[0])
        nt, ct = norm(title), title_core(title)
        na_tok = tokens(norm(author)) | set(norm(author).split())
        rec = {"line": ln, "author": author, "title": title}

        hit = None
        if nt in full_index:
            hit = (cat[full_index[nt][0]], 1.0)
        elif ct and ct in core_index and len(ct) >= 12:
            ci = core_index[ct][0]
            # same core, but two non-empty subtitles sharing zero tokens reads as
            # two volumes of one series, not one book — human rules it
            s1, s2 = subtitle(title), subtitle(cat[ci]["e"]["t"])
            if s1 and s2 and not (tokens(s1) & tokens(s2)):
                maybes.append({**rec, "candidate": cat[ci]["e"]["id"],
                               "candidate_title": cat[ci]["e"]["t"],
                               "score": round(score(nt, cat[ci]["nt"]), 3)})
                continue
            hit = (cat[ci], max(0.90, score(nt, cat[ci]["nt"])))
        else:
            cand = set()
            for t in sorted(tokens(nt), key=lambda t: len(tok_index[t]))[:8]:
                cand |= tok_index[t]
            best, best_s = None, 0.0
            for ci in cand:
                s = score(nt, cat[ci]["nt"])
                if s > best_s:
                    best, best_s = cat[ci], s
            if best is not None:
                thresh = MATCH_T_AUTHOR if (na_tok & best["na_tok"]) else MATCH_T
                if best_s >= thresh:
                    hit = (best, best_s)
                elif best_s >= MAYBE_T:
                    maybes.append({**rec, "candidate": best["e"]["id"],
                                   "candidate_title": best["e"]["t"],
                                   "score": round(best_s, 3)})
                    continue
        if hit:
            catalogued.append({**rec, "id": hit[0]["e"]["id"],
                               "catalog_title": hit[0]["e"]["t"],
                               "score": round(hit[1], 3)})
        else:
            gap.append(rec)

    REPORT_JSON.write_text(json.dumps(
        {"source": str(FAVORITES), "favorites": len(lines),
         "catalogued": catalogued, "gap": gap, "maybes": maybes},
        indent=1, ensure_ascii=False), encoding="utf-8")

    md = []
    md.append("---\ntitle: ZLIB GAP REPORT — favorites vs catalog\ntype: report\n"
              f"source: zlib-favorites.txt ({len(lines)} books) vs catalog.json ({len(catalog)} sources)\n"
              "regenerate: python _tools/zlib_gap_parser.py\n---\n")
    md.append("# ZLIB GAP REPORT\n")
    md.append(f"**{len(lines)} favorites** diffed against **{len(catalog)} catalogued sources**: "
              f"**{len(catalogued)} already catalogued** · **{len(gap)} in THE GAP** (acquisition queue) · "
              f"**{len(maybes)} review-queue maybes**.\n")
    md.append("## Already catalogued\n")
    md.append("| Favorite | BVX | Score |\n|---|---|---|")
    for r in sorted(catalogued, key=lambda r: r["id"]):
        md.append(f"| {r['line']} | {r['id']} | {r['score']} |")
    md.append("\n## THE GAP — acquisition queue\n")
    md.append("One per line, walker order (z-lib favorites order, newest-faved first).\n")
    for r in gap:
        md.append(f"- {r['line']}")
    md.append("\n## Review-queue maybes\n")
    md.append("Close-but-not-confident matches — rule each row: same book → catalogued, different → GAP.\n")
    md.append("| Favorite | Candidate | BVX | Score |\n|---|---|---|---|")
    for r in sorted(maybes, key=lambda r: -r["score"]):
        md.append(f"| {r['line']} | {r['candidate_title']} | {r['candidate']} | {r['score']} |")
    md.append("")
    REPORT_MD.write_text("\n".join(md), encoding="utf-8")

    print(f"favorites={len(lines)} catalogued={len(catalogued)} gap={len(gap)} maybes={len(maybes)}")
    print(f"report: {REPORT_MD}")


if __name__ == "__main__":
    sys.exit(main())
