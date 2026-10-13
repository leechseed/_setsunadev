"""Claude Code docs mirror (BOLO 140). Runs on Chief's word only, never from a hook.
  python -X utf8 _tools/docs/mirror.py          fetch, keep previous as .prev.md, print diff summary
  python -X utf8 _tools/docs/mirror.py --check  diff against stored copies, write nothing
Pages come from mirror_pages.txt. Asks for the markdown form (<url>.md); falls back to HTML->text."""
import urllib.error, sys, re, ssl, subprocess, difflib, pathlib, urllib.request, html
from html.parser import HTMLParser
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parents[1] / "_PRIVATE" / "reference" / "claude-code-docs"

class T(HTMLParser):
    SKIP = {"script", "style", "nav", "footer", "svg"}
    def __init__(s): super().__init__(); s.o = []; s.skip = 0
    def handle_starttag(s, t, a):
        if t in s.SKIP: s.skip += 1
        elif t in ("h1","h2","h3","h4"): s.o.append("\n\n" + "#" * int(t[1]) + " ")
        elif t in ("p","div","li","br","tr","pre"): s.o.append("\n")
    def handle_endtag(s, t):
        if t in s.SKIP and s.skip: s.skip -= 1
    def handle_data(s, d):
        if not s.skip: s.o.append(d)

def to_text(body):
    if not re.search(r"<html|<!doctype", body[:500], re.I): return body
    p = T(); p.feed(body)
    return re.sub(r"\n{3,}", "\n\n", html.unescape("".join(p.o))).strip() + "\n"

def fetch(url):
    req = urllib.request.Request(url + ".md", headers={"User-Agent": "command-mirror/1"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return to_text(r.read().decode("utf-8", "replace"))
    except (ssl.SSLError, urllib.error.URLError) as e:  # this box's Python trust store has an expired root; the system curl is fine
        r = subprocess.run(["curl", "-sfL", "-m", "30", url + ".md"], capture_output=True)
        if r.returncode: raise RuntimeError(f"{e}; curl exit {r.returncode}")
        return to_text(r.stdout.decode("utf-8", "replace"))

def heads(t): return {l.strip() for l in t.splitlines() if l.startswith("#")}

def main():
    check = "--check" in sys.argv
    urls = [l.strip() for l in (HERE/"mirror_pages.txt").read_text(encoding="utf-8").splitlines() if l.strip().startswith("http")]
    OUT.mkdir(parents=True, exist_ok=True)
    n = tot = 0; changed_heads = []
    for u in urls:
        slug = u.rstrip("/").rsplit("/", 1)[-1]
        try: new = fetch(u)
        except Exception as e: print(f"{slug}: FAIL {e}"); continue
        n += 1; tot += len(new.encode("utf-8"))
        f = OUT / f"{slug}.md"
        if f.exists():
            old = f.read_text(encoding="utf-8")
            d = list(difflib.unified_diff(old.splitlines(), new.splitlines(), lineterm="", n=0))
            add = sum(1 for x in d if x.startswith("+") and not x.startswith("+++"))
            rem = sum(1 for x in d if x.startswith("-") and not x.startswith("---"))
            ch = sorted(heads(old) ^ heads(new))
            print(f"{slug}: +{add} -{rem}" + (f" headings changed: {ch[:6]}" if ch else ""))
            if ch: changed_heads.append(slug)
            if not check and old != new: f.with_suffix(".prev.md").write_text(old, encoding="utf-8")
        else:
            print(f"{slug}: new ({len(new.splitlines())} lines)")
        if not check: f.write_text(new, encoding="utf-8")
    print(f"SUMMARY {n}/{len(urls)} pages, {tot} bytes" + (" (check, nothing written)" if check else ""))
    if changed_heads: print("CALL FOR CHIEF before any skill or hook edit: headings changed in " + ", ".join(changed_heads))
if __name__ == "__main__": main()
