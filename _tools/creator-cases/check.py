# -*- coding: utf-8 -*-
"""CREATOR CASE check — the reviewer at the fan-in (script, zero tokens).

Usage:  python _tools/creator-cases/check.py <slug>   (or a path to any creator-case-*.md)
Checks the ten sections in order · the TTP header and its four parts · frontmatter keys · every §9 URL is used somewhere above ·
no private-info tripwires (street-address pattern, "real name", "legal name") · thin-record honesty (§8 non-empty).
"""
import io, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SECTIONS = ["Identity", "Timeline", "How", "Monetization", "Growth", "Quotes", "Interviews", "Not known", "Sources", "TTP"]

def main():
    a = sys.argv[1]
    p = a if a.endswith(".md") else os.path.join(ROOT, "_CANON_NODES", f"creator-case-{a}.md")
    t = io.open(p, encoding="utf-8").read()
    F, W = [], []
    fm = t.split("---")[1] if t.startswith("---") else ""
    for k in ("entity", "trunk", "status", "captured", "updated"):
        if not re.search(rf"^{k}:", fm, re.M): F.append(f"frontmatter: {k} missing")
    if "trunk: ORANGE" not in fm: W.append("trunk is not ORANGE")
    heads = re.findall(r"^## (\d+) · (.+)$", t, re.M)
    nums = [int(n) for n, _ in heads]
    if nums != list(range(1, 11)): F.append(f"sections are {nums}, must be 1..10")
    for (n, h), want in zip(heads, SECTIONS):
        if want.lower() not in h.lower(): W.append(f"§{n} header '{h[:40]}' does not read as {want}")
    if not re.search(r"^## 10 · TTP$", t, re.M): F.append("§10 header must be exactly '## 10 · TTP'")
    ttp = t.split("## 10 · TTP")[-1] if "## 10 · TTP" in t else ""
    for part in ("The one mechanic", "Transferable tips", "Does not transfer", "Feeds"):
        if part.lower() not in ttp.lower(): W.append(f"TTP lacks '{part}'")
    for part in ("Bottom line", "Papi's context", "Confidence"):
        if part not in t: W.append(f"opening lacks **{part}.**")
    src = t.split("## 9 ·")[-1].split("## 10 ·")[0] if "## 9 ·" in t else ""
    urls9 = set(re.findall(r"https?://\S+", src))
    above = t.split("## 9 ·")[0]
    unused = [u for u in urls9 if u.rstrip(").,") not in above]
    if len(unused) > max(2, len(urls9) // 3): W.append(f"{len(unused)} of {len(urls9)} §9 URLs never cited above")
    if not urls9: F.append("§9 has no URLs")
    nk = t.split("## 8 ·")[-1].split("## 9 ·")[0] if "## 8 ·" in t else ""
    if len(nk.strip()) < 80: W.append("§8 Not known is thin; the thin-record rule wants the gaps named")
    for pat, why in ((r"\b\d{2,5} [A-Z][a-z]+ (Street|St\.|Ave|Avenue|Road|Rd\.|Blvd)\b", "street address"), (r"\b(legal|real) name\b", "legal/real name mention")):
        if re.search(pat, t): F.append(f"privacy tripwire: {why}")
    print(f"CHECK · {os.path.basename(p)} · {len(F)} blocking · {len(W)} advisory · {len(urls9)} sources")
    for f in F: print("  BLOCK " + f)
    for w in W: print("  note  " + w)
    sys.exit(1 if F else 0)

if __name__ == "__main__":
    main()
