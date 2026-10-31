"""BOLO 77 wave 2 · build the trope graph (zero tokens).

Joins the book nodes (MS-N), the trope keys (8 PS batches, RANGE-checked), the
TV Tropes index definitions and the fetched trope links into one graph file:
  nodes   135 book nodes, each with its trope count
  tropes  every keyed trope (slug, name, index definition, node, alt, conf)
  edges   node -> node, weighted: how many trope links cross from a trope keyed
          to one node into a trope keyed to another; plus the books' own same_as
  unkeyed the tropes no node fits (count and slugs)

10/31 (BOLO 89 register v0.6.0, Chief: "run what you need"): the graph reads the full trope register
(data/domains/register.json, 8,700 tropes, the one key store, IF-01-04-22) for each trope's name, one-line
def and links, and carries the register's cross-domain keys on every trope it shares. The plot pull
(data/index.json + data/tropes.jsonl) is the fallback for plot tropes the register does not hold.

usage: python _tools/tropes/build_graph.py
out:   _tools/tropes/data/trope_graph.json
"""
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
WORK = HERE.parent / "bolostatus" / "work" / "77" / "tropes"


def main():
    nodes = json.loads((WORK / "nodes.json").read_text(encoding="utf-8"))
    index = json.loads((DATA / "index.json").read_text(encoding="utf-8"))
    keys = {}
    for b in range(1, 9):
        for k in json.loads((WORK / f"keys.batch{b}.json").read_text(encoding="utf-8")):
            keys[k["slug"]] = k
    reg = json.loads((DATA / "domains" / "register.json").read_text(encoding="utf-8"))
    links = {}
    tp = DATA / "tropes.jsonl"
    if tp.exists():
        for line in tp.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                links[r["slug"]] = r["links"]
    for slug, r in reg.items():  # the register's links win: the newer, wider fetch
        if r.get("links"):
            links[slug] = r["links"]

    tropes, unkeyed = [], []
    for slug, k in keys.items():
        e = index.get(slug, {})
        r = reg.get(slug)
        if not k.get("node"):
            unkeyed.append(slug)
            continue
        t = {"slug": slug, "name": (r or e).get("name", slug), "def": (r or {}).get("def") or e.get("def", ""),
             "indexes": e.get("indexes", []), "node": k["node"], "alt": k.get("alt"), "conf": k.get("conf")}
        if r:
            t["register"] = {"domains": r["domains"], "keys": r["keys"], "conf": r["conf"]}
        tropes.append(t)

    node_of = {t["slug"]: t["node"] for t in tropes}
    w = Counter()
    for t in tropes:
        for dst in links.get(t["slug"], []):
            b = node_of.get(dst)
            if b and b != t["node"]:
                w[tuple(sorted((t["node"], b)))] += 1
    edges = [{"a": a, "b": b, "type": "trope_link", "w": n} for (a, b), n in w.most_common()]
    seen = set()
    for n in nodes:
        for s in n.get("same_as") or []:
            pair = tuple(sorted((n["id"], s)))
            if pair not in seen:
                seen.add(pair)
                edges.append({"a": pair[0], "b": pair[1], "type": "same_as", "w": None})

    count = Counter(t["node"] for t in tropes)
    for n in nodes:
        n["tropes"] = count.get(n["id"], 0)
    out = {"built": "BOLO 77 wave 2 · on the full register (BOLO 89 v0.6.0, 2026-10-31)", "counts": {
               "nodes": len(nodes), "tropes_keyed": len(tropes), "tropes_unkeyed": len(unkeyed),
               "in_register": sum(1 for t in tropes if "register" in t), "register_size": len(reg),
               "links_fetched": len(links), "edges_trope_link": len(w), "edges_same_as": len(seen)},
           "nodes": nodes, "tropes": tropes, "edges": edges, "unkeyed": sorted(unkeyed)}
    (DATA / "trope_graph.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    c = out["counts"]
    print("trope graph · " + " · ".join(f"{k} {v}" for k, v in c.items()))
    top = sorted(nodes, key=lambda n: -n["tropes"])[:8]
    print("busiest nodes: " + " · ".join(f"{n['id']} {n['tropes']}" for n in top))
    print("empty nodes: %d" % sum(1 for n in nodes if not n["tropes"]))


if __name__ == "__main__":
    main()
