#!/usr/bin/env python3
import json
import re
from pathlib import Path

# Read nodes file - parse with proper delimiters
nodes = {}
nodes_list = []
line_num = 0
with open(r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\nodes.compact.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        line_num += 1
        # Format: structured_id | title | definition
        parts = line.split(" | ", 2)
        if len(parts) >= 2:
            structured_id = parts[0]
            node_title = parts[1]
            node_def = parts[2] if len(parts) > 2 else ""

            node_id = str(line_num)  # Use line number as node_id

            nodes[node_id] = {
                "structured_id": structured_id,
                "title": node_title,
                "definition": node_def,
            }
            nodes_list.append((node_id, structured_id, node_title, node_def))

print(f"Loaded {len(nodes)} nodes")

# Read batch7 file
tropes = []
with open(r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\batch7.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        # Format: slug | name | definition | [indexes]
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

print(f"Loaded {len(tropes)} tropes")

def find_best_match(trope_slug, trope_name, trope_def):
    """
    Find the best matching node for a trope.
    Returns (node_id, alt_node_id, confidence)
    """

    trope_text = f"{trope_slug} {trope_name} {trope_def}".lower()

    # Manual keyword-to-node mapping using line numbers (1-135)
    # Keywords map to node line numbers
    exact_keywords = {
        "quest": ["1"],
        "adventure": ["2"],
        "pursuit": ["3", "30", "96"],
        "chase": ["3", "96"],
        "rescue": ["4", "23", "97"],
        "escape": ["5", "29", "95"],
        "revenge": ["6", "25", "26"],
        "vengeance": ["6", "25", "26"],
        "riddle": ["7", "41"],
        "mystery": ["7", "21", "41"],
        "enigma": ["41"],
        "rivalry": ["8", "27"],
        "rival": ["8", "27"],
        "underdog": ["9"],
        "temptation": ["10", "126"],
        "tempt": ["10", "126"],
        "metamorphosis": ["11"],
        "transformation": ["12"],
        "transform": ["12"],
        "maturation": ["13"],
        "mature": ["13"],
        "coming of age": ["13"],
        "love": ["14", "64", "125"],
        "romance": ["14"],
        "forbidden": ["15"],
        "taboo": ["15"],
        "adultery": ["29", "49"],
        "infidelity": ["29", "49"],
        "sacrifice": ["16", "48", "56", "59"],
        "discovery": ["17", "41", "42", "61", "62"],
        "excess": ["18"],
        "ascension": ["19"],
        "descension": ["20"],
        "fall": ["20"],
        "descend": ["20"],
        "supplication": ["21"],
        "benefaction": ["22"],
        "deliverance": ["23"],
        "sojourn": ["24", "4"],
        "abduction": ["39"],
        "kidnap": ["39"],
        "reunion": ["40"],
        "invention": ["42"],
        "obtaining": ["43"],
        "enmity": ["45"],
        "enemy": ["45"],
        "hatred": ["45"],
        "madness": ["51"],
        "insane": ["51"],
        "genius": ["52"],
        "loss": ["71"],
        "griev": ["71"],
        "odd couple": ["73"],
        "opposite": ["73"],
        "misfit": ["74"],
        "displace": ["74"],
        "villain": ["83", "93"],
        "evil": ["83"],
        "call": ["108"],
        "challenge": ["108"],
        "refusal": ["109"],
        "mentor": ["110"],
        "guide": ["110"],
        "threshold": ["111"],
        "crossing": ["111"],
        "test": ["112", "87", "88"],
        "ordeal": ["114"],
        "reward": ["115"],
        "return": ["116"],
        "resurrection": ["117"],
        "rebirth": ["117"],
        "elixir": ["118"],
    }

    best_matches = []

    # Check for keyword matches in order of priority
    for keyword in sorted(exact_keywords.keys(), key=len, reverse=True):  # Longer keywords first
        if keyword in trope_text:
            for node_id_str in exact_keywords[keyword]:
                if node_id_str in nodes:
                    best_matches.append((node_id_str, "high"))

    # Remove duplicates, keep first occurrence
    seen = set()
    unique_matches = []
    for match in best_matches:
        if match[0] not in seen:
            unique_matches.append(match)
            seen.add(match[0])
    best_matches = unique_matches

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
errors = 0
for r in results:
    if r["node"] and r["node"] not in valid_node_ids:
        print(f"ERROR: Invalid node id '{r['node']}' for trope {r['slug']}")
        errors += 1
    if r["alt"] and r["alt"] not in valid_node_ids:
        print(f"ERROR: Invalid alt node id '{r['alt']}' for trope {r['slug']}")
        errors += 1

if errors == 0:
    print("All node IDs validated successfully!")
else:
    print(f"Found {errors} validation errors")
