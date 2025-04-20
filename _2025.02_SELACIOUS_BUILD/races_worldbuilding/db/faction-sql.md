faction {
faction_id integer pk increments unique
name varchar // Short name (e.g., "Noxus")
display_name varchar // Formal or localized display (e.g., "The Noxian Empire")
acronym varchar // Optional shorthand (e.g., "NOX")
symbol_url varchar // Link or reference to insignia/sigil/emblem
color_primary varchar // Hex code or name for branding
color_secondary varchar
visual_style_tags varchar // e.g., "Gothic, Baroque, Brutalist"

origin_summary text // Where/when/how the faction was founded
founding_date varchar // Literal or narrative-friendly date
founder_name varchar // Mythic or real founder (e.g., "Mordekaiser")
core_myth text // Narrative myth that justifies their right to rule/exist
founding_principles text // Ideological doctrine or manifesto

geopolitical_scope varchar // "Empire", "City-State", "Spiritual Order", "Underground"
region_controlled varchar // e.g., "Eastern Valoran", "Void Pockets", etc.
capital_city varchar // Optional
known_bases text // Multiple cities, islands, or headquarters

economic_system varchar // e.g., "Warlord Plunder", "State Capitalism", "Guild Trade"
military_structure text // Rank system, enforcement units, elite forces
technological_level varchar // e.g., "Runic-Industrial", "Hexpunk", "Pre-Magitech"

religious_alignment varchar // Major faith or cosmic entity (if any)
cultural_rituals text // Rites, festivals, sacrifices, tattoos, etc.
fashion_style_tags varchar // e.g., "Iron + Leather", "Ceremonial Armor", "Tattooed Furs"
language_style varchar // Formal, brutalist, coded, poetic, dead language, etc.

faction_alignment varchar // Moral/ethical slot: "Lawful Evil", "Chaotic Neutral", etc.
primary_archetype varchar // "Imperialism", "Rebellion", "Faith", "Madness", etc.
opposing_faction_ids varchar // CSV or array of FK ids (for known rivals)

notable_figures text // Champion_ID + Role (e.g., "Darius - General")
known_events text // e.g., "Rune Wars", "The Fall of Boram Darkwill"
thematic_keywords text // e.g., "Dominance, Strength, Indoctrination"
summary_lore text // 3-5 sentence lore bio

crossmedia_presence text // Appearances in comics, show, cinematics
codex_notes text // Dev notes, fandom theories, out-of-universe context
}
