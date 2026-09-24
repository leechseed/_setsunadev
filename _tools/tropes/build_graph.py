"""BOLO 77 wave 2 · build the trope graph (zero tokens).

Joins the book nodes (MS-N), the trope keys (8 PS batches, RANGE-checked), the
TV Tropes index definitions and the fetched trope links into one graph file:
  nodes   135 book nodes, each with its trope count
  tropes  every keyed trope (slug, name, index definition, node, alt, conf)
  edges   node -> node, weighted: how many trope links cross from a trope keyed
          to one node into a trope keyed to another; plus the books' own same_as
  unkeyed the tropes no node fits (count and slugs)

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
    links = {}
    tp = DATA / "tropes.jsonl"
    if tp.exists():
        for line in tp.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                links[r["slug"]] = r["links"]

    tropes, unkeyed = [], []
    for slug, k in keys.items():
        e = index.get(slug, {})
        if not k.get("node"):
            unkeyed.append(slug)
            continue
        tropes.append({"slug": slug, "name": e.get("name", slug), "def": e.get("def", ""),
                       "indexes": e.get("indexes", []), "node": k["node"],
                       "alt": k.get("alt"), "conf": k.get("conf")})

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
    out = {"built": "BOLO 77 wave 2", "counts": {
               "nodes": len(nodes), "tropes_keyed": len(tropes), "tropes_unkeyed": len(unkeyed),
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
