#!/usr/bin/env python3
import json
import re
from pathlib import Path

# Read nodes file
nodes = {}
with open(r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\nodes.compact.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split("\t", 3)
        if len(parts) >= 3:
            node_id = parts[0]
            node_name = parts[1]
            node_def = parts[2] if len(parts) > 2 else ""
            # Parse the name to extract structured id (e.g., "tob.01_quest" from "tob.01_quest | Quest")
            name_parts = node_name.split(" | ")
            if len(name_parts) >= 2:
                structured_id = name_parts[0]
                node_title = name_parts[1]
            else:
                structured_id = node_id
                node_title = node_name
            nodes[node_id] = {
                "structured_id": structured_id,
                "title": node_title,
                "definition": node_def
            }

# Read batch7 file
tropes = []
with open(r"C:\Users\U01_LEECHSEED\Desktop\_setsunadev\_tools\bolostatus\work\77\tropes\batch7.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(" | ", 3)
        if len(parts) >= 3:
            slug = parts[0]
            name = parts[1]
            definition = parts[2] if len(parts) > 2 else ""
            tropes.append({
                "slug": slug,
                "name": name,
                "definition": definition
            })

# Key matching function
def find_best_match(trope_slug, trope_name, trope_def):
    """
    Find the best matching node for a trope.
    Returns (node_id, alt_node_id, confidence)
    """

    # Normalize search terms
    slug_lower = trope_slug.lower()
    name_lower = trope_name.lower()
    def_lower = trope_def.lower()

    best_match = (None, None, "low")
    best_score = 0
    alt_match = (None, "low")
    alt_score = 0

    # Direct keyword matching
    keyword_map = {
        # Quest/Search patterns
        "quest": ("1", "high"),  # tob.01_quest
        "seeking": ("1", "high"),
        "search": ("1", "high"),

        # Adventure
        "adventure": ("2", "high"),

        # Pursuit/Chase
        "pursuit": ("3", "high"),
        "chase": ("3", "high"),
        "pursuing": ("3", "high"),

        # Rescue
        "rescue": ("4", "high"),

        # Escape
        "escape": ("5", "high"),

        # Revenge
        "revenge": ("6", "high"),
        "vengeance": ("6", "high"),
        "retaliati": ("6", "high"),

        # Riddle/Mystery
        "riddle": ("7", "high"),
        "enigma": ("41", "high"),
        "mystery": ("7", "medium"),

        # Rivalry
        "rivalry": ("8", "high"),
        "rival": ("8", "high"),
        "competition": ("27", "high"),
        "compete": ("27", "high"),

        # Underdog
        "underdog": ("9", "high"),

        # Temptation
        "temptation": ("10", "high"),
        "tempt": ("10", "high"),

        # Transformation/Metamorphosis
        "metamorphosis": ("11", "high"),
        "transformation": ("12", "high"),
        "transform": ("12", "high"),
        "shape": ("11", "medium"),

        # Maturation
        "maturation": ("13", "high"),
        "mature": ("13", "high"),
        "coming of age": ("13", "high"),
        "innocence": ("13", "medium"),

        # Love
        "love": ("14", "high"),
        "romance": ("14", "high"),
        "fall in love": ("14", "high"),

        # Forbidden Love
        "forbidden": ("15", "high"),
        "taboo": ("15", "high"),
        "adultery": ("29", "high"),
        "infidelity": ("29", "medium"),

        # Sacrifice
        "sacrifice": ("16", "high"),

        # Discovery/Self-knowledge
        "discovery": ("17", "high"),
        "who am i": ("17", "high"),

        # Excess
        "excess": ("18", "high"),
        "wretched": ("18", "high"),

        # Ascension
        "ascension": ("19", "high"),

        # Descension/Fall
        "descension": ("20", "high"),
        "fall": ("20", "high"),
        "descend": ("20", "high"),

        # Supplication
        "supplication": ("21", "high"),
        "petition": ("21", "high"),

        # Benefaction
        "benefaction": ("22", "high"),
        "charity": ("22", "high"),
        "aid": ("22", "high"),

        # Deliverance
        "deliverance": ("23", "high"),

        # Sojourn
        "sojourn": ("24", "high"),
        "stranger": ("24", "medium"),
        "visit": ("24", "medium"),

        # Abduction
        "abduction": ("39", "high"),
        "kidnap": ("39", "high"),

        # Reunion
        "reunion": ("40", "high"),
        "reunite": ("40", "high"),

        # Invention
        "invention": ("42", "high"),
        "invent": ("42", "high"),

        # Obtaining
        "obtaining": ("43", "high"),
        "acquire": ("43", "high"),

        # Enmity
        "enmity": ("45", "high"),
        "enemy": ("45", "high"),
        "hatred": ("45", "high"),

        # Competition
        "competition": ("47", "high"),
        "compete": ("47", "high"),

        # Madness
        "madness": ("51", "high"),
        "mad": ("51", "high"),
        "insane": ("51", "high"),

        # Genius
        "genius": ("52", "high"),

        # Self-Sacrifice
        "self-sacrifice": ("59", "high"),

        # Loss of loved one
        "loss": ("71", "high"),
        "death": ("71", "high"),
        "griev": ("71", "high"),

        # Odd Couple
        "odd couple": ("73", "high"),
        "opposite": ("73", "medium"),
        "mismat": ("73", "medium"),

        # Fish out of water
        "fish out of water": ("74", "high"),
        "misfit": ("74", "medium"),
        "displace": ("74", "medium"),

        # Villainy (Propp)
        "villain": ("83", "medium"),
        "evil": ("83", "medium"),

        # Call to Adventure (Vogler)
        "call": ("108", "high"),
        "challenge": ("108", "high"),

        # Refusal of Call
        "refusal": ("109", "high"),
        "hesitate": ("109", "high"),
        "refuse": ("109", "high"),

        # Meeting with mentor
        "mentor": ("110", "high"),
        "guide": ("110", "high"),

        # Crossing threshold
        "threshold": ("111", "high"),
        "crossing": ("111", "high"),

        # Tests/Allies/Enemies
        "test": ("112", "high"),
        "allies": ("112", "high"),
        "ally": ("112", "high"),
        "enemy": ("112", "high"),

        # Ordeal
        "ordeal": ("114", "high"),

        # Reward
        "reward": ("115", "high"),

        # Return
        "return": ("116", "high"),
        "road back": ("116", "high"),

        # Resurrection
        "resurrection": ("117", "high"),
        "rebirth": ("117", "high"),

        # Elixir
        "elixir": ("118", "high"),

        # Campbell stages
        "supernatural aid": ("121", "high"),
        "belly of the whale": ("123", "high"),
        "road of trials": ("124", "high"),
        "meeting with goddess": ("125", "high"),
        "temptress": ("126", "high"),
        "atonement": ("127", "high"),
        "apotheosis": ("128", "high"),
        "ultimate boon": ("129", "high"),
        "magic flight": ("131", "high"),
        "rescue from without": ("132", "high"),
        "master of two worlds": ("134", "high"),
        "freedom to live": ("135", "high"),
    }

    # Check for keyword matches in trope name and definition
    for keyword, (node_num, conf) in keyword_map.items():
        score = 0
        word_score = 0

        if keyword in slug_lower:
            word_score += 4
        if keyword in name_lower:
            word_score += 3
        if keyword in def_lower:
            word_score += 1

        if word_score > 0:
            # Adjust score based on confidence level
            if conf == "high":
                score = word_score * 3
            elif conf == "medium":
                score = word_score * 2
            else:
                score = word_score

            if score > best_score:
                alt_match = best_match[:2]
                alt_score = best_score
                best_match = (node_num, None, conf)
                best_score = score
            elif score > alt_score and node_num != best_match[0]:
                alt_match = (node_num, conf)
                alt_score = score

    # Format node ids properly
    if best_match[0]:
        best_match = (str(best_match[0]), alt_match[0] if alt_match[0] else None, best_match[2])

    # Default null if no match found
    if not best_match[0]:
        return None, None, "low"

    return best_match[0], best_match[1], best_match[2]

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
for r in results:
    if r["node"] and r["node"] not in valid_node_ids:
        print(f"WARNING: Invalid node id {r['node']} for trope {r['slug']}")
    if r["alt"] and r["alt"] not in valid_node_ids:
        print(f"WARNING: Invalid alt node id {r['alt']} for trope {r['slug']}")
