import os
import re
from pathlib import Path
import json

# Base directory
base_dir = Path("C:/Users/U01_LEECHSEED/Desktop/_setsunadev/_0.1_BVX_LEARN/KNOWLEDGE_AREAS")

# List of untagged IDs from LIBRARY-GAP.md
untagged_ids = [
    "BVX.0236", "BVX.0343", "BVX.0479", "BVX.0480", "BVX.0580", "BVX.0581",
    "BVX.0598", "BVX.0599", "BVX.1128", "BIZ.01", "CRE.01", "CRE.02", "CRE.03",
    "CRE.04", "MIL.01", "MIL.02", "MIL.03", "MIL.04", "MIL.05", "MIL.06",
    "MIL.07", "MIL.08", "MIL.09", "MIL.10", "MIL.11", "MSX.01", "MSX.02",
    "MSX.03", "MSX.04", "MSX.05", "MSX.06", "MSX.07", "MSX.08", "MSX.09",
    "MSX.10", "MSX.11", "MSX.12", "MSX.13", "MSX.14", "MSX.15", "MSX.16",
    "PHI.01", "PHI.02", "PSY.02", "PSY.03", "PSY.05", "PSY.06", "PSY.07",
    "PSY.43", "PSY.44", "PSY.45", "PSY.46", "PSY.47", "PSY.48", "TEC.01",
    "TEC.02", "TEC.03", "TEC.04", "TEC.05"
]

results = []

for file_id in untagged_ids:
    # Find file matching this ID
    matching_files = list(base_dir.glob(f"*{file_id}*.md"))
    if not matching_files:
        print(f"NOT FOUND: {file_id}", flush=True)
        continue
    
    file_path = matching_files[0]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter (between --- markers)
        fm_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
        frontmatter = fm_match.group(1) if fm_match else ""
        
        # Extract CORE THESIS section
        thesis_match = re.search(r'## CORE THESIS\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
        thesis = thesis_match.group(1).strip() if thesis_match else ""
        
        # Get title from frontmatter
        title_match = re.search(r'title: ["\']?([^"\'\n]+)', frontmatter)
        title = title_match.group(1) if title_match else file_id
        
        results.append({
            'id': file_id,
            'title': title,
            'frontmatter': frontmatter,
            'thesis': thesis[:500] if thesis else "(no CORE THESIS found)"
        })
    except Exception as e:
        print(f"ERROR reading {file_id}: {e}", flush=True)

# Write to JSON for analysis
with open("C:/Users/U01_LEECHSEED/Desktop/_setsunadev/_tools/bolostatus/work/100/untagged_extracted.json", 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Processed {len(results)} files. Output written to untagged_extracted.json", flush=True)
