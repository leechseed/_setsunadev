## Updated Plan

Based on all 12 answers, the revised build sequence:

### Phase 1: Dramatica Integration

**1A. SSOT: Dramatica Integration Protocol** — What Dramatica is in the system, how storyforms relate to characters, the `storyform_id` keying system, Pattern 1 nested storyform support.

**1B. L12 Architecture Decision** — Implement Option C (core L12 + `L12_DRAMATICA_EXTENDED` sub-table). Define which variables live where.

**1C. Tier 2 Character System** — Implement Approach 3 (element signature + relational roles). Define the L12 block format for Tier 2 characters.

**1D. Dramatica Ingest Template (.md)** — The canonical intake form for Tier 3 characters. Covers full storyform position, throughline variables, element quads. Includes the `storyform_id` field.

### Phase 2: Character Astrology Integration

**2A. SSOT: Character Astrology** — Renamed, relocated to 02_CHARACTER. Defines the system's role as a deterministic character rendering engine. Separates the 15 categories into character-level (natal chart, dignities, personal stack, structural stack, aspects, houses, interface layer) and story-level (progressions, transits, synastry, movements, reset protocol).

**2B. DAI Expansion (Dramatica-Astrology Interface)** — The full translation table from Dramatica variables to astrological configurations. This is the API spec. Narrative-first derivation rules for each planet from Dramatica inputs.

**2C. Character Astrology Ingest Template (.md)** — The canonical intake form for astrological character data. Captures natal chart, planetary positions, aspects, dignities, house placements — all derived from the locked Dramatica ingest via the DAI.

### Phase 3: Integration Architecture

**3A. Character Astrology ↔ 12-Layer Mapping** — Which astrological variables feed which layers. Where they are independent. The formal interface between the parallel datasets.

**3B. Character State Architecture** — The static core + state diff system. Defines how progressions, transits, and narrative-moment snapshots overlay on the static character record without modifying it.

**3C. Step 1 Source Verification Protocol (revised)** — Formal definition of "canonical documentation exists and is locked." Requires: Dramatica Ingest Template [LOCKED] + Character Astrology Ingest Template [LOCKED] + both validated against interface spec.

### Phase 4: Validation

Run Victoria Midnight through the new pipeline. Produce both ingest templates from her authoritative document. Confirm the existing vertical slice is reproducible from those templates. Identify any gaps where the authoritative document does not contain enough data to complete a template field.