#!/usr/bin/env python3
"""
modmigrate.py - port a Modrinth mod list to another loader / Minecraft version.

  python modmigrate.py matrix                       coverage table for the candidate targets -> matrix.md
  python modmigrate.py matrix --refresh             same, but re-pull every project's version list
  python modmigrate.py download --loader neoforge --mc 1.21.11 --out "C:\\path\\to\\instance" [--dry]

Reads slugs.txt next to this file (lines: "<type> <slug>", types: mod | resourcepack | shader).
Public Modrinth v2 API only, no key.  Downloads land in <out>/mods, <out>/resourcepacks,
<out>/shaderpacks.  Required dependencies are pulled in automatically (Kotlin for Forge etc).
Every file is sha512-checked.  Version JSON is cached under %LOCALAPPDATA%\\Temp\\modmigrate-cache.
"""
import argparse, hashlib, json, os, sys, time, urllib.error, urllib.parse, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
for _s in (sys.stdout, sys.stderr):
    try: _s.reconfigure(encoding="utf-8")
    except Exception: pass

HERE  = os.path.dirname(os.path.abspath(__file__))
CACHE = os.environ.get("MODMIGRATE_CACHE") or os.path.join(os.environ.get("LOCALAPPDATA", HERE), "Temp", "modmigrate-cache")
API   = "https://api.modrinth.com/v2"
UA    = "setsunadev-modmigrate/0.1 (cllankers@gmail.com)"

# Windows' system trust store rejected cdn.modrinth.com's chain as expired; certifi's bundle accepts it.
import ssl, subprocess
try:
    import certifi
    CTX = ssl.create_default_context(cafile=certifi.where())
except Exception:
    CTX = None


def fetch_bytes(url, timeout=180):
    """GET url -> bytes.  urllib with certifi first; on TLS failure fall back to curl (its own CA bundle)."""
    try:
        return urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=timeout, context=CTX).read()
    except (urllib.error.URLError, ssl.SSLError) as e:
        if "CERTIFICATE" not in str(e).upper():
            raise

        r = subprocess.run(["curl", "-sSL", "--max-time", str(timeout), "-A", UA, url], capture_output=True)
        if r.returncode != 0:
            raise RuntimeError(f"curl failed: {r.stderr.decode(errors='replace').strip()}")
        return r.stdout

# candidate targets shown by `matrix`  (loader, minecraft version)
TARGETS = [("fabric", "1.21.11"), ("forge", "1.21.11"), ("neoforge", "1.21.11"),
           ("forge", "26.2"), ("neoforge", "26.2"), ("neoforge", "26.1.2")]
LOADERLESS = {"resourcepack", "shader"}      # only the game version matters
# fabric plumbing the other loaders replace natively
PLUMBING = {"fabric-api", "fabric-language-kotlin", "modmenu"}


def get(url, tries=5):
    for i in range(tries):
        try:
            return json.loads(fetch_bytes(url, timeout=30))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(5 * (i + 1)); continue
            if e.code == 404:
                return None
            raise
        except Exception:
            time.sleep(2 * (i + 1))
    raise RuntimeError("gave up on " + url)


def load_slugs():
    out = []
    for line in open(os.path.join(HERE, "slugs.txt"), encoding="utf-8"):
        line = line.split("#")[0].strip()
        if line:
            t, s = line.split()
            out.append((t, s))
    return out


def project_meta(slugs):
    meta = {}
    for i in range(0, len(slugs), 60):
        chunk = json.dumps(slugs[i:i + 60])
        for p in get(f"{API}/projects?ids={urllib.parse.quote(chunk)}") or []:
            meta[p["slug"]] = p
            meta[p["id"]] = p
    return meta


def versions_for(slug, refresh=False):
    os.makedirs(CACHE, exist_ok=True)
    f = os.path.join(CACHE, f"{slug}.json")
    if not refresh and os.path.exists(f):
        return json.load(open(f, encoding="utf-8"))
    v = get(f"{API}/project/{slug}/version") or []
    json.dump(v, open(f, "w", encoding="utf-8"))
    return v


def pick(versions, loader, mc, loaderless):
    """Newest version for (loader, mc).  If the newest is a beta/alpha but a full
    release for the same target was published within 30 days of it, take the release."""
    c = [v for v in versions if mc in v["game_versions"] and (loaderless or loader in v["loaders"])]
    if not c:
        return None
    c.sort(key=lambda v: v["date_published"], reverse=True)
    newest = c[0]
    if newest["version_type"] == "release":
        return newest
    rel = next((v for v in c if v["version_type"] == "release"), None)
    if rel:
        gap = (date.fromisoformat(newest["date_published"][:10]) - date.fromisoformat(rel["date_published"][:10])).days
        if gap <= 30:
            return rel
    return newest


def cmd_matrix(args):
    slugs = load_slugs()
    names = [s for _, s in slugs]
    meta = project_meta(names)
    with ThreadPoolExecutor(6) as ex:
        allv = dict(zip(names, ex.map(lambda s: versions_for(s, args.refresh), names)))
    hdr = "| project | type | " + " | ".join(f"{l} {m}" for l, m in TARGETS) + " |"
    rows = [hdr, "|" + "---|" * (2 + len(TARGETS))]
    totals = {t: 0 for t in TARGETS}
    for t, s in slugs:
        m = meta.get(s)
        title = m["title"] if m else s + " (404)"
        cells = []
        for l, mc in TARGETS:
            v = pick(allv[s], l, mc, t in LOADERLESS)
            if v:
                cells.append("✅ " + v["version_number"][:24]); totals[(l, mc)] += 1
            else:
                cells.append("❌")
        rows.append(f"| {title} | {t} | " + " | ".join(cells) + " |")
    rows.append("|" + "---|" * (2 + len(TARGETS)))
    rows.append("| **TOTAL** | | " + " | ".join(f"**{totals[t]}** / {len(slugs)}" for t in TARGETS) + " |")
    out = "\n".join(rows)
    open(os.path.join(HERE, "matrix.md"), "w", encoding="utf-8").write(out + "\n")
    print(out)
    print(f"\nwritten to {os.path.join(HERE, 'matrix.md')}")


def cmd_download(args):
    loader, mc = args.loader, args.mc
    want = {s: t for t, s in load_slugs()}
    meta = project_meta(list(want))
    chosen, missing, queue, seen = {}, [], list(want), set()
    while queue:
        s = queue.pop(0)
        if s in seen:
            continue
        seen.add(s)
        t = want[s]
        if loader != "fabric" and s in PLUMBING:
            print(f"  skip {s:32}  fabric plumbing, {loader} has its own")
            continue
        v = pick(versions_for(s), loader, mc, t in LOADERLESS)
        if not v:
            missing.append((s, t)); continue
        chosen[s] = (t, v)
        dep_ids = [d["project_id"] for d in v.get("dependencies", [])
                   if d.get("dependency_type") == "required" and d.get("project_id")]
        new_ids = [d for d in dep_ids if d not in meta]
        if new_ids:
            meta.update(project_meta(new_ids))
        for d in dep_ids:
            p = meta.get(d)
            if p and p["slug"] not in want:
                want[p["slug"]] = "mod"
                queue.append(p["slug"])
                print(f"  + dep  {p['title']:32}  needed by {meta[s]['title']}")
    sub = {"mod": "mods", "resourcepack": "resourcepacks", "shader": "shaderpacks"}
    for d in sub.values():
        os.makedirs(os.path.join(args.out, d), exist_ok=True)
    manifest = []
    for s, (t, v) in chosen.items():
        f = next((x for x in v["files"] if x.get("primary")), v["files"][0])
        dest = os.path.join(args.out, sub[t], f["filename"])
        manifest.append({"slug": s, "type": t, "version": v["version_number"], "file": f["filename"], "url": f["url"]})
        if os.path.exists(dest) and hashlib.sha512(open(dest, "rb").read()).hexdigest() == f["hashes"]["sha512"]:
            print(f"  ok   {f['filename']}"); continue
        if args.dry:
            print(f"  GET  {f['filename']}"); continue
        data = fetch_bytes(f["url"])
        if hashlib.sha512(data).hexdigest() != f["hashes"]["sha512"]:
            print(f"  !!   hash mismatch, not saved: {f['filename']}"); continue
        open(dest, "wb").write(data)
        print(f"  got  {f['filename']}")
    mpath = os.path.join(args.out, f"modmigrate-{loader}-{mc}.json")
    json.dump(manifest, open(mpath, "w", encoding="utf-8"), indent=1)
    print(f"\n{len(manifest)} files for {loader} {mc}  ->  {args.out}")
    if missing:
        print(f"\nNO BUILD for {loader} {mc}  ({len(missing)}):")
        for s, t in missing:
            kind = "mod" if t == "mod" else t
            print(f"  - {meta.get(s, {}).get('title', s):40}  https://modrinth.com/{kind}/{s}")


ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
sp = ap.add_subparsers(dest="cmd", required=True)
m = sp.add_parser("matrix"); m.add_argument("--refresh", action="store_true")
d = sp.add_parser("download")
d.add_argument("--loader", required=True, choices=["fabric", "forge", "neoforge", "quilt"])
d.add_argument("--mc", required=True)
d.add_argument("--out", required=True)
d.add_argument("--dry", action="store_true", help="resolve and report, download nothing")
a = ap.parse_args()
cmd_matrix(a) if a.cmd == "matrix" else cmd_download(a)
