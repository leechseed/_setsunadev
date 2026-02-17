# 📘 Knowledgebase Plan: Structuring `sexual_presence` Into a Modular Erotic Engine (v2)

**Goal:** Convert your current monolithic `sexual_presence` concept into a **modular, database-ready** v2 system that supports:

- Projection-only entities (seductive aura without kink logic)
    
- Kink-only entities (fetish logic without “charisma/aura” dominance)
    
- Anti-erotic / nullification entities (MODS/Committee-style)
    
- Consent/boundary governance (to prevent incoherence and tonal accidents)
    
- Compression into 4 master axes for sanity and long-term scalability
    

---

## 0. Outputs You Will Produce (Concrete Deliverables)

You will end this process with:

1. **DB schema v2**
    
    - `sexual_projection`
        
    - `kink_logic`
        
    - `consent_model`
        
    - (optional) `sexual_profile` as the join + summary
        
2. **Canonical tag registries**
    
    - `fetish_taxonomy`
        
    - `aesthetic_coding_registry`
        
    - (optional) `archetype_registry`
        
3. **Migration + normalization rules**
    
    - mapping from current `sexual_presence` fields → v2 tables
        
    - required fields vs optional fields
        
    - null-handling rules
        
4. **Character YAML templates**
    
    - projection-only template
        
    - kink-only template
        
    - full erotic profile template
        
    - anti-erotic template
        
5. **Validation rules**
    
    - “Firewall” rules for non-erotic archetypes
        
    - axis coverage rules (Projection/Desire/Control/Identity)
        
    - narrative weight governance
        

---

## 1. Split the Module Into Two Layers (Execution Plan)

### 1.1 Create Two New Tables (Do This First)

#### Table A — `sexual_projection`

Contains “what they _do_ to others” (social/erotic presence).

**Fields (v2 core):**

- `character_id` (PK/FK)
    
- `erotic_archetype`
    
- `sexual_energy_type`
    
- `presentation_mode`
    
- `arousal_effect` (rename from `arousal_reaction`)
    
- `performance_confidence`
    
- `projection_notes` (optional narrative glue)
    
- `erotic_plot_weight` (see section 2)
    

#### Table B — `kink_logic`

Contains “what they _want/do_ in private mechanics.”

**Fields (v2 core):**

- `character_id` (PK/FK)
    
- `personal_kink`
    
- `dominant_fetishes`
    
- `submissive_fetishes`
    
- `kink_triggers`
    
- `kink_expression_style`
    
- `kink_notes` (optional narrative glue)
    

---

### 1.2 Decide Join Strategy (Pick One and Lock It)

**Option A (cleanest):**  
`character_id` is PK in each table. Presence in a table = that layer exists.

- Projection-only: row exists in `sexual_projection`, no row in `kink_logic`
    
- Kink-only: row exists in `kink_logic`, no row in `sexual_projection`
    
- Full profile: both rows exist
    
- Anti-erotic: projection exists but with nullification + weight low/structural depending (see 2 + 4)
    

**Option B (more flexible but heavier):**  
Use `sexual_profile` as the master row, with nullable links to layers.

I recommend **Option A** because it’s simpler and your system already loves modularity.

---

### 1.3 Migration Mapping (From Your Current Schema)

Map your current fields like this:

**Move into `sexual_projection`:**

- `charisma_score` (optional: keep here or in a separate `social_presence` table)
    
- `sexual_energy_type`
    
- `presentation_mode`
    
- `erotic_archetype`
    
- `performance_confidence`
    
- `arousal_reaction` → rename to `arousal_effect`
    
- `trauma_or_origin_note` → becomes `projection_notes` (or split: origin goes elsewhere)
    

**Move into `kink_logic`:**

- `personal_kink`
    
- `dominant_fetishes`
    
- `submissive_fetishes`
    
- `kink_expression_style`
    
- `kink_triggers`
    

**Keep separate (do NOT keep inside either layer):**

- `fetishized_features`
    
- `aesthetic_coding`
    
- `gaze_style`
    
- `vocal_cues`
    
- `touch_behavior`
    
- `scent_profile`
    

These are better treated as **presentation signals** (see optional 1.4).

---

### 1.4 (Optional but Recommended) Create a Third Table: `erotic_signals`

This keeps projection clean and prevents kink logic from getting polluted by aesthetics.

**Fields:**

- `character_id`
    
- `fetishized_features`
    
- `aesthetic_coding`
    
- `gaze_style`
    
- `vocal_cues`
    
- `touch_behavior`
    
- `scent_profile`
    

If you don’t do this now, you’ll do it later anyway when the schema balloons again.

---

## 2. Add the “Narrative Weight” Field (Execution Plan)

### 2.1 Add `erotic_plot_weight` to `sexual_projection`

**Enum:**

- `low`
    
- `medium`
    
- `high`
    
- `structural`
    

### 2.2 Define Canon Rules for Each Weight

You need a “what does this _do_ in scenes?” rule so it’s not just a label.

- **low**: flavor + texture; no scene steering
    
- **medium**: can tilt social outcomes; affects tension/chemistry beats
    
- **high**: can drive conflict, deals, betrayals, obsessions
    
- **structural**: sexuality is an _operating principle_ of their role (Fiona-tier, cult leaders, paradigms, etc.)
    

### 2.3 Hard Constraint (Prevents Story Gravity Collapse)

Rule:

- Only **X% of major cast** can be `high` or `structural`.
    
- Everyone else must be `medium` or `low`.
    

Pick a cap. Example:

- Main cast: max 2 structural, max 3 high.
    
- Minor cast: default low.
    

Write this into your system doctrine so you don’t sabotage yourself later.

---

## 3. Formalize a Consent & Boundary Model (Execution Plan)

### 3.1 Create `consent_model` Table

**Fields:**

- `character_id`
    
- `negotiation_style`
    
- `boundary_flexibility`
    
- `public_vs_private_alignment`
    
- `taboo_threshold`
    
- `aftercare_need_level` (optional but extremely useful)
    
- `consent_notes`
    

### 3.2 Define Allowed Values (Don’t Leave This As Freeform)

You need canonical enums or controlled vocab or you’ll get mush-data.

**negotiation_style** (examples):

- explicit-verbal
    
- ritualized
    
- implicit-trust-based
    
- transactional
    
- power-ceremonial
    
- avoidant / non-engaging
    

**boundary_flexibility**:

- rigid
    
- contextual
    
- fluid
    

**public_vs_private_alignment**:

- aligned (same persona)
    
- split (public mask / private reality)
    
- inverted (public purity / private intensity)
    

**taboo_threshold**:

- low
    
- medium
    
- high
    
- sanctified-taboo (taboo is the point)
    
- sterile (taboo-avoidant)
    

### 3.3 Add Firewall Rules (Non-Negotiables)

This is the safety rail that also improves coherence.

- If `sexual_energy_type = none | non-erotic | anti-erotic`  
    then:
    
    - `kink_logic` row must be absent OR explicitly marked `disabled`
        
    - `taboo_threshold` must not imply pursuit
        
    - negotiation style becomes procedural / none
        
- If archetype is “innocent/childlike/aesthetic-of-innocence”  
    then:
    
    - hard lock: **no kink logic**
        
    - only “projection” is allowed if it’s protective/nostalgic and explicitly non-erotic
        
    - signals must avoid eroticized descriptors
        

This prevents tonal contamination.

---

## 4. Define 4 Core Erotic Axes (Compression Plan)

### 4.1 Create an Axis Scoring Block (Lightweight and Useful)

Add this to either:

- `sexual_projection` (if you want it tied to outward effect), or
    
- `sexual_profile` (if you create a summary table)
    

**Fields:**

- `axis_projection` (0–5)
    
- `axis_desire` (0–5)
    
- `axis_control` (0–5)
    
- `axis_identity` (0–5)
    

### 4.2 Create the Mapping Rule: Every Field Must Feed an Axis

Before adding any new field, you must answer:

- Does this primarily describe Projection, Desire, Control, or Identity?
    
- If it doesn’t, it’s either:
    
    - a registry tag, or
        
    - narrative prose, or
        
    - junk
        

### 4.3 Pruning Rule (How You Cut Fields Without Regret)

Once you have 20+ characters encoded, run a “field usefulness audit”:

- If a field is:
    
    - often empty, and
        
    - doesn’t predict scenes, and
        
    - doesn’t differentiate archetypes,  
        then cut it or move it to notes.
        

---

## 5. Step-by-Step Implementation Sequence (Do It In This Order)

### Phase 1 — Schema Lock (1–2 sessions)

1. Create v2 table definitions for:
    
    - `sexual_projection`
        
    - `kink_logic`
        
    - `consent_model`
        
    - (optional) `erotic_signals`
        
2. Decide enums and controlled vocab (minimum viable, not perfect).
    
3. Write the firewall rules as doctrine.
    

### Phase 2 — Migration Pass (2–4 sessions)

4. Select 6 characters as calibration set:
    
    - Fiona (full, structural)
        
    - Vivian (full, medium/high)
        
    - Nacho (projection-heavy)
        
    - MODS (anti-erotic)
        
    - Myrtle (non-erotic)
        
    - John Smith (ascetic authoritarian)
        
5. Convert them into v2 rows.
    
6. Fix schema pain immediately (don’t “later” it).
    

### Phase 3 — Registries + Tag Hygiene (ongoing)

7. Build `fetish_taxonomy` (even if rough).
    
8. Build `aesthetic_coding_registry`.
    
9. Enforce: fields use registries, not freehand strings.
    

### Phase 4 — Templates + Automation (once stable)

10. Create YAML templates for 4 profile types.
    
11. Build a generator (script or snippet) that emits YAML skeletons.
    
12. Add validation checks (simple: required fields + enum checking).
    

---

## 6. Minimal YAML Templates (Drop-In Starters)

### 6.1 Projection-Only

```yaml
sexual_projection:
  erotic_plot_weight: medium
  erotic_archetype: ""
  sexual_energy_type: ""
  presentation_mode: ""
  arousal_effect: ""
  performance_confidence: ""
  axis:
    projection: 0
    desire: 0
    control: 0
    identity: 0
```

### 6.2 Kink-Only

```yaml
kink_logic:
  personal_kink: ""
  dominant_fetishes: []
  submissive_fetishes: []
  kink_expression_style: ""
  kink_triggers: []
```

### 6.3 Consent Model

```yaml
consent_model:
  negotiation_style: ""
  boundary_flexibility: ""
  public_vs_private_alignment: ""
  taboo_threshold: ""
  aftercare_need_level: ""
```

### 6.4 Anti-Erotic (Firewall Example)

```yaml
sexual_projection:
  erotic_plot_weight: structural
  erotic_archetype: "N/A"
  sexual_energy_type: "anti-erotic"
  presentation_mode: "judicial"
  arousal_effect: "nullification / suppression"
  performance_confidence: "detached"
  axis:
    projection: 4
    desire: 0
    control: 5
    identity: 4

kink_logic: null

consent_model:
  negotiation_style: "non-engaging"
  boundary_flexibility: "rigid"
  public_vs_private_alignment: "aligned"
  taboo_threshold: "sterile"
```

---

## 7. Your Key Design Decision (Lock This Now)

You asked whether this is a narrative enhancement layer or metaphysical substrate.

To structure data correctly, you must choose one of these operating modes:

### Mode A — Enhancement Layer

- Most characters: low/medium weight
    
- Only 1–2 structural entities
    
- Sex affects scenes occasionally
    

### Mode B — Substrate Layer

- Sex governs status, factions, rituals, virtue, taboo
    
- `sexual_paradigms` becomes a world law
    
- Weight field becomes a story-gravity dial, not just caution tape
    

Given your existing faction/ritual/paradigm work, you’re already in **Mode B**.  
So structure it like a substrate and stop pretending it’s optional.

---

If you want, I can produce **the actual SQL v2 schema** for the 3–4 tables plus enums + constraints as a clean drop-in next.