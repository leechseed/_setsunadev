import json
import re

# Load the extracted data
with open("C:/Users/U01_LEECHSEED/Desktop/_setsunadev/_tools/bolostatus/work/100/untagged_extracted.json", 'r', encoding='utf-8') as f:
    distills = json.load(f)

# Define storytelling systems and analysis rules
systems = {
    'character': [],
    'plot': [],
    'setting': [],
    'genre': [],
    'texture': [],
    'theme': [],
    'tracking': [],
    'worldbuilding': [],
    'style': [],
    'NONE': []
}

results = []

for distill in distills:
    dist_id = distill['id']
    title = distill['title'].lower()
    thesis = distill['thesis'].lower()
    frontmatter = distill['frontmatter'].lower()
    
    # Determine system and layer
    system = None
    layer = None
    reason = ""
    
    # NONE: operational/technical/business docs
    if any(word in title for word in ['warfighting', 'strategy', 'logistics', 'planning', 'intelligence', 'command', 'tactics', 'learning', 'underground economy', 'seduction', 'bottoming', 'topping', 'cocksucking', 'faggot', 'pickup', 'nice guy', 'models', 'rational male', 'shogun', 'art of', 'docs', 'manual', 'engineering', 'handbook', 'minimalism', 'minto pyramid']):
        system = 'NONE'
        reason = "operational/military/business/technical doctrine, not story method"
    
    # STYLE: prose craft and writing mechanics
    elif any(word in title for word in ['clarity', 'style', 'writing', 'rhetoric', 'prose', 'point of view']):
        system = 'style'
        layer = '?'
        reason = "prose craft, writing voice, sentence mechanics"
    
    # TEXTURE/STYLE: fantasy rhetorics, narrative mediation
    elif 'rhetorics of fantasy' in title:
        system = 'texture'
        layer = '?'
        reason = "tone and atmosphere in fantasy narrative"
    
    # GENRE: film/literature genre theory
    elif any(word in title for word in ['genre', 'hollywood']):
        system = 'genre'
        layer = '?'
        reason = "genre conventions and film/literary types"
    
    # SETTING: worldbuilding guides and campaign settings
    elif any(word in title for word in ['world', 'setting', 'campaign', 'travel', 'gamemaster', 'game master', 'pathfinder']):
        system = 'setting'
        layer = 'S?'
        reason = "place construction, campaign/world rules"
    
    # THEME: sexuality in literature, philosophical texts
    elif any(word in title for word in ['sexuality', 'human sexuality', 'sexual ecstasy', 'phallicism', 'sexual', 'sex', 'intimacy', 'threesomes', 'desire', 'pleasure', 'bdsm', 'sadomasochism', 'desire', 'ecstasy', 'hedonism', 'tantra']):
        system = 'theme'
        layer = 'T?'
        reason = "sexual desire and eros as thematic force in character"
    
    # THEME: learning, cognition
    elif any(word in title for word in ['learning', 'efficiency', 'multimedia', 'instruction', 'learning works', 'yourself how to learn']):
        system = 'NONE'
        reason = "cognitive science and pedagogy, not story method"
    
    # THEME: domination, power structures
    elif any(word in title for word in ['domination', 'phallic', 'power', 'lucifer effect']):
        system = 'theme'
        layer = 'T?'
        reason = "power dynamics and moral transgression as theme"
    
    # CHARACTER: queer theory, identity, sexuality studies
    elif any(word in title for word in ['queer', 'homosexuality', 'lesbian', 'gay', 'male', 'manhood', 'masculinity', 'female', 'gender', 'trouble', 'body', 'culture of queers', 'drag', 'leather', 'counterpublic']):
        system = 'character'
        layer = 'C?'
        reason = "identity, desire, and subculture identity construction"
    
    # CHARACTER: biography/cultural history of male identity
    elif any(word in title for word in ['rent boys', 'sex work', 'public sex', 'gay new york', 'pornography', 'macho', 'homos', 'homosexual desire']):
        system = 'character'
        layer = 'C?'
        reason = "sexual identity, male subculture, erotic expression"
    
    # TRACKING: narrative technical analysis
    elif any(word in title for word in ['dramatica', 'narrative', 'semantics', 'narratology', 'structural']):
        system = 'tracking'
        layer = '?'
        reason = "story structure and narrative mechanics"
    
    # NONE: business/economics
    elif any(word in title for word in ['business', 'economy', 'sales']):
        system = 'NONE'
        reason = "business and economics, not story method"
    
    # Default: unclassified but story-adjacent
    else:
        system = 'NONE'
        reason = f"unclear; title='{distill['title'][:60]}'"
    
    results.append({
        'id': dist_id,
        'title': distill['title'],
        'system': system,
        'layer': layer,
        'reason': reason
    })

# Count by system
counts = {}
for system in systems.keys():
    count = len([r for r in results if r['system'] == system])
    counts[system] = count

# Sort results by ID
results.sort(key=lambda x: x['id'])

# Write markdown table
output = []
output.append("# LIBRARY-UNTAGGED Analysis")
output.append("")
output.append(f"**Summary:** {sum(1 for r in results if r['system'] != 'NONE')} distills assigned to story systems · {counts['NONE']} NONE")
output.append("")
output.append("## Counts by system")
for system in sorted(counts.keys()):
    if system != 'NONE':
        output.append(f"- **{system}**: {counts[system]}")
output.append(f"- **NONE**: {counts['NONE']}")
output.append("")
output.append("## Full table")
output.append("")
output.append("| id | title | system | layer | reason |")
output.append("|---|---|---|---|---|")
for r in results:
    title_short = r['title'][:45].replace('|', '·')
    reason_short = r['reason'][:60].replace('|', '·')
    layer_str = r['layer'] if r['layer'] else '—'
    output.append(f"| {r['id']} | {title_short} | {r['system']} | {layer_str} | {reason_short} |")

# Write to file
with open("C:/Users/U01_LEECHSEED/Desktop/_setsunadev/_tools/bolostatus/work/100/LIBRARY-UNTAGGED.md", 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

# Print summary to stdout
print("Analysis complete. Counts:")
for system in sorted(counts.keys()):
    print(f"  {system}: {counts[system]}")
