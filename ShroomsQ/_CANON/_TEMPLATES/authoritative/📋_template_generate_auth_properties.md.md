---
{{#template}}
Read the content below and generate YAML properties:

Required fields:
- type: authoritative
- story: [OVEREXITOUT, ASTRO7EX, or LAKAD]
- category: [character, plot, theme, or world]
- entity: [specific character name or plot element]
- ssot_dependencies: [list SSOT docs used, use [[wikilinks]]]
- version: 1.0.0
- last_updated: {{date:YYYY-MM-DD}}
- status: canonical

Output only the YAML block. No explanation.

---
{{/template}}

{{content}}
```

---

## USAGE WORKFLOW

### Scenario: Staged SSOT Candidate Ready for Canon

1. Open file in `_STAGED/ssot_candidates/`
2. Command palette: "Text Generator: Generate from template"
3. Select `📋_template_generate_ssot_properties`
4. AI reads content, generates frontmatter
5. Review generated properties
6. Insert at top of file
7. Move to `_CANON/_SSOT/[category]/`

### Scenario: Quick Property Fill

1. Cursor at top of document
2. Command palette: "Text Generator: Generate"
3. Type prompt:
```
Generate YAML frontmatter for this SSOT document. 
Use the standard template format.
Identify dependencies from content.
```
4. Review output
5. Insert

---

## HOTKEY SETUP (OPTIONAL)

Settings → Hotkeys → Text Generator:
```
Generate from template: Alt+Shift+G
Generate (inline): Alt+Shift+I