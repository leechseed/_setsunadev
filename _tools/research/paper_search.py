"""Search OpenAlex for papers by title or DOI. Metadata only; never downloads a PDF.

Usage:
    python _tools/research/paper_search.py "<title or DOI>" [--n 5]

Prints one line per hit: year | first author | title | DOI | open-access URL (if any).
No API key. Optional env var OPENALEX_MAILTO adds a polite mailto to the
User-Agent; if unset, it is omitted. Stdlib only.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.openalex.org/works"
FIELDS = "display_name,publication_year,authorships,doi,open_access,best_oa_location"


def fetch(url):
    ua = "command-paper-search/1.0"
    mail = os.environ.get("OPENALEX_MAILTO")
    if mail:
        ua += f" (mailto:{mail})"
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("query", help="title words or a DOI")
    ap.add_argument("--n", type=int, default=5, help="max hits (default 5)")
    a = ap.parse_args()

    q = a.query.strip()
    doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", q, flags=re.I)
    try:
        if re.match(r"^10\.\d{4,}/\S+$", doi):
            w = fetch(f"{API}/doi:{urllib.parse.quote(doi, safe='/')}?select={FIELDS}")
            results = [w]
        else:
            qs = urllib.parse.urlencode(
                {"search": q, "per-page": max(1, min(a.n, 50)), "select": FIELDS}
            )
            results = fetch(f"{API}?{qs}").get("results", [])
    except urllib.error.HTTPError as e:
        print(f"error: OpenAlex returned HTTP {e.code} for {q!r}", file=sys.stderr)
        return 1
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"error: could not reach OpenAlex: {e}", file=sys.stderr)
        return 1

    if not results:
        print(f"no hits for {q!r}", file=sys.stderr)
        return 1
    for w in results[: a.n]:
        auths = w.get("authorships") or []
        first = ((auths[0].get("author") or {}).get("display_name") if auths else None) or "?"
        oa = (w.get("best_oa_location") or {}).get("landing_page_url") or (
            w.get("open_access") or {}
        ).get("oa_url") or ""
        print(
            f"{w.get('publication_year') or '?'} | {first} | "
            f"{w.get('display_name') or '?'} | {w.get('doi') or '-'} | {oa or '-'}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())

# adapted from ykdojo/paper-search (MIT) · BOLO 140 · 2026-10-12
