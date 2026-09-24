#!/usr/bin/env python3
import json
import re
from pathlib import Path

# Read nodes file
nodes = {}
nodes_list = []
with open(r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\nodes.compact.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split("\t", 2)
        if len(parts) >= 2:
            node_id = parts[0]
            content = parts[1]
            # Parse: "structured_id | title | definition"
            subparts = content.split(" | ", 2)
            if len(subparts) >= 2:
                structured_id = subparts[0]
                node_title = subparts[1]
                node_def = subparts[2] if len(subparts) > 2 else ""
            else:
                structured_id = node_id
                node_title = content
                node_def = ""

            nodes[node_id] = {
                "structured_id": structured_id,
                "title": node_title,
                "definition": node_def,
                "id_index": node_id
            }
            nodes_list.append((node_id, structured_id, node_title, node_def))

# Read batch7 file
tropes = []
with open(r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\batch7.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(" | ", 3)
        if len(parts) >= 2:
            slug = parts[0]
            name = parts[1]
            definition = parts[2] if len(parts) > 2 else ""
            tropes.append({
                "slug": slug,
                "name": name,
                "definition": definition
            })

def similarity_score(text1, text2):
    """Simple word overlap similarity"""
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    if not words1 or not words2:
        return 0
    overlap = len(words1 & words2)
    return overlap / max(len(words1), len(words2))

def find_best_match(trope_slug, trope_name, trope_def):
    """
    Find the best matching node for a trope using semantic analysis.
    Returns (node_id, alt_node_id, confidence)
    """

    # Combine trope text for matching
    trope_text = f"{trope_slug} {trope_name} {trope_def}".lower()

    # Manual keyword-to-node mapping for high-confidence matches
    exact_keywords = {
        "secret": [],  # Too vague - multiple matches
        "quest": ["1"],
        "adventure": ["2"],
        "pursuit": ["3", "30"],
        "chase": ["3"],
        "rescue": ["4", "23"],
        "escape": ["5"],
        "revenge": ["6"],
        "vengeance": ["25"],
        "riddle": ["7", "41"],
        "mystery": ["7", "21", "41"],
        "rivalry": ["8"],
        "rival": ["8"],
        "underdog": ["9"],
        "temptation": ["10"],
        "metamorphosis": ["11"],
        "transformation": ["12"],
        "maturation": ["13"],
        "love": ["14"],
        "forbidden": ["15"],
        "sacrifice": ["16"],
        "discovery": ["17"],
        "excess": ["18"],
        "ascension": ["19"],
        "descension": ["20"],
        "fall from grace": ["20"],
        "supplication": ["21"],
        "benefaction": ["22"],
        "deliverance": ["23"],
        "sojourn": ["24"],
        "abduction": ["39"],
        "kidnap": ["39"],
        "reunion": ["40"],
        "invention": ["42"],
        "obtaining": ["43"],
        "enmity": ["45"],
        "enemy": ["45"],
        "hatred": ["45"],
        "madness": ["51"],
        "mad": ["51"],
        "insane": ["51"],
        "genius": ["52"],
        "loss": ["71"],
        "griev": ["71"],
        "odd couple": ["73"],
        "misfit": ["74"],
        "villain": ["83"],
        "evil": ["83"],
        "call to adventure": ["108"],
        "call": ["108"],
        "refusal": ["109"],
        "mentor": ["110"],
        "threshold": ["111"],
        "test": ["112"],
        "ordeal": ["114"],
        "reward": ["115"],
        "return": ["116"],
        "resurrection": ["117"],
        "rebirth": ["117"],
        "elixir": ["118"],
    }

    best_matches = []

    # Check for keyword matches
    for keyword, node_ids in exact_keywords.items():
        if keyword in trope_text:
            for nid in node_ids:
                if nid in nodes:
                    best_matches.append((nid, "high"))

    # If no high-confidence matches, try semantic similarity
    if not best_matches:
        scores = []
        for node_id, structured_id, node_title, node_def in nodes_list:
            node_text = f"{structured_id} {node_title} {node_def}".lower()
            score = similarity_score(trope_text, node_text)
            if score > 0.15:  # Threshold for reasonable match
                scores.append((node_id, score, "medium"))

        if scores:
            scores.sort(key=lambda x: x[1], reverse=True)
            best_matches = [(nid, conf) for nid, _, conf in scores[:2]]

    # Return results
    if best_matches:
        return best_matches[0][0], (best_matches[1][0] if len(best_matches) > 1 else None), best_matches[0][1]
    else:
        return None, None, "low"

# Process each trope
results = []
for trope in tropes:
    node_id, alt_id, conf = find_best_match(trope["slug"], trope["name"], trope["definition"])

    results.append({
        "slug": trope["slug"],
        "node": node_id,
        "alt": alt_id,
        "conf": conf
    })

# Write JSON output
output_path = r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\keys.batch7.json"
with open(output_path, "w") as f:
    json.dump(results, f, indent=2)

print(f"Wrote {len(results)} trope keys to {output_path}")

# Validation
keyed_count = sum(1 for r in results if r["node"] is not None)
null_count = sum(1 for r in results if r["node"] is None)

print(f"Total tropes: {len(results)}")
print(f"Keyed (non-null): {keyed_count}")
print(f"Null nodes: {null_count}")

# Validate node ids
valid_node_ids = set(nodes.keys())
print(f"Valid node IDs: {len(valid_node_ids)}")
errors = 0
for r in results:
    if r["node"] and r["node"] not in valid_node_ids:
        print(f"WARNING: Invalid node id '{r['node']}' for trope {r['slug']}")
        errors += 1
    if r["alt"] and r["alt"] not in valid_node_ids:
        print(f"WARNING: Invalid alt node id '{r['alt']}' for trope {r['slug']}")
        errors += 1

if errors == 0:
    print("All node IDs validated successfully!")
