```markdown
# 📘 Dramatica Story Schema — **Specification Sheet**

**File**: `dramatica.schema.json` (Draft-07)  
**Purpose**: Canonical Dramatica storyform + plot progression + character web, suitable for agentic/NCP use.

---

## Table of Contents

1. [Schema Overview](#schema-overview)
2. [Top-Level Structure](#top-level-structure)
3. [Section Specs](#section-specs)
   - [metadata](#metadata)
   - [storyform](#storyform)
   - [throughlines](#throughlines)
   - [plot_progression](#plot_progression)
   - [characters](#characters)
4. [Definitions ($defs)](#definitions-defs)
   - [Throughline](#throughline)
   - [PlotTrack](#plottrack)
   - [Character](#character)
   - [Enums: TypeName, VariationName, ElementName](#enums-typename-variationname-elementname)
5. [Cross-Field Consistency (Recommended)](#cross-field-consistency-recommended)
6. [Validation Notes](#validation-notes)
7. [Minimal Valid Instance](#minimal-valid-instance)
8. [Scaffold Template (Fill-In-The-Blanks)](#scaffold-template-fill-in-the-blanks)
9. [Quick JSONPath/Pointer Reference](#quick-jsonpathpointer-reference)
10. [FAQ / Notes](#faq--notes)

---

## Schema Overview

- **$schema**: `http://json-schema.org/draft-07/schema#`
- **$id**: `https://example.org/schemas/dramatica.schema.json`
- **Title**: _Dramatica Story Schema_
- **Description**: Canonical Dramatica storyform + plot progression + character web, for agentic/NCP workflows.
- **Root Type**: `object`
- **Required at top level**:  
  `["version", "storyform", "throughlines", "plot_progression", "characters"]`

> You may also include `$schema` and `$id` inside instance files for discoverability, but they are not required by this schema for instances.

---

## Top-Level Structure

| Property           | Type   | Required | Description                                                                   |
| ------------------ | ------ | -------- | ----------------------------------------------------------------------------- |
| `version`          | string | ✅       | Schema/instance version (recommend **semver**: `1.0.0`).                      |
| `metadata`         | object | ❌       | Optional descriptive info. `additionalProperties: true`.                      |
| `storyform`        | object | ✅       | Dramatica Dynamics + Appreciations. `additionalProperties: false`.            |
| `throughlines`     | object | ✅       | OS/MC/IC/RS throughlines, each a `$defs.Throughline`.                         |
| `plot_progression` | object | ✅       | OS/MC/IC/RS plot tracks, each a `$defs.PlotTrack`.                            |
| `characters`       | object | ✅       | Player list and inter-character relationships. `additionalProperties: false`. |

---

## Section Specs

### `metadata`

- **Type**: object, `additionalProperties: true`
- **Fields**:
  | Field | Type | Description |
  |---------------|-----------------|-------------|
  | `title` | string | Story title. |
  | `logline` | string | One-sentence premise. |
  | `author` | string | Author/owner. |
  | `created_at` | string (date-time) | ISO 8601. |
  | `updated_at` | string (date-time) | ISO 8601. |
  | `tags` | string[] | Arbitrary labels. |

---

### `storyform`

- **Type**: object, `required: ["dynamics","appreciations"]`, `additionalProperties: false`

#### `storyform.dynamics`

- **Type**: object, `required: ["driver","limit","outcome","judgment"]`, `additionalProperties: false`
- **Fields & Enums**:
  | Field | Enum |
  |------------|------------------------|
  | `driver` | `Action` \| `Decision` |
  | `limit` | `Optionlock` \| `Timelock` |
  | `outcome` | `Success` \| `Failure` |
  | `judgment` | `Good` \| `Bad` |

#### `storyform.appreciations`

- **Type**: object, `additionalProperties: true` _(extensible)_
- **Common Dramatica keys (all strings)**:
  `goal`, `consequence`, `requirements`, `prerequisites`, `forewarnings`,
  `cost`, `dividend`, `focus`, `direction`, `problem`, `solution`,
  `unique_ability`, `critical_flaw`, `benchmark`.

> **Note**: This schema keeps **`dividend`** (aka “Collateral Benefit” in some materials) for compatibility.

---

### `throughlines`

- **Type**: object, `required: ["overall_story","main_character","impact_character","relationship_story"]`, `additionalProperties: false`
- **Each**: `$ref: "#/$defs/Throughline"`

| Key                  | Meaning                              |
| -------------------- | ------------------------------------ |
| `overall_story`      | Overall Story (OS) throughline.      |
| `main_character`     | Main Character (MC) throughline.     |
| `impact_character`   | Impact Character (IC) throughline.   |
| `relationship_story` | Relationship Story (RS) throughline. |

---

### `plot_progression`

- **Type**: object, `required: ["overall_story","main_character","impact_character","relationship_story"]`, `additionalProperties: false`
- **Each**: `$ref: "#/$defs/PlotTrack"`

| Key                  | Meaning                             |
| -------------------- | ----------------------------------- |
| `overall_story`      | OS plot track (signposts/journeys). |
| `main_character`     | MC plot track.                      |
| `impact_character`   | IC plot track.                      |
| `relationship_story` | RS plot track.                      |

---

### `characters`

- **Type**: object, `required: ["players"]`, `additionalProperties: false`
- **Fields**:

#### `characters.players`

- **Type**: array of `$defs.Character`, `minItems: 1`

#### `characters.relationships`

- **Type**: array of objects (`additionalProperties: false`)
- **Each relationship**:
  | Field | Type | Required | Notes |
  |---------|----------|----------|-------|
  | `ids` | string[] | ✅ | 2–3 character IDs (must match `players[].id`). |
  | `type` | enum | ✅ | One of: `Main_vs_Impact`, `Protagonist_vs_Antagonist`, `Mentor_Student`, `Rivals`, `Allies`, `Family`, `Romance`, `Other`. |
  | `label` | string | ❌ | Optional human-readable name. |
  | `notes` | string | ❌ | Freeform annotation. |

---

## Definitions ($defs)

### Throughline

`$defs.Throughline` (`additionalProperties: false`)

| Field          | Type / Enum                                         | Required |
| -------------- | --------------------------------------------------- | -------- |
| `domain`       | enum: `Activity`, `Situation`, `Psychology`, `Mind` | ✅       |
| `concern`      | string, `$defs.TypeName`                            | ✅       |
| `issue`        | string, `$defs.VariationName`                       | ✅       |
| `counterpoint` | string, `$defs.VariationName`                       | ❌       |
| `problem`      | string, `$defs.ElementName`                         | ✅       |
| `solution`     | string, `$defs.ElementName`                         | ✅       |
| `symptom`      | string, `$defs.ElementName`                         | ✅       |
| `response`     | string, `$defs.ElementName`                         | ✅       |
| `benchmark`    | string, `$defs.TypeName`                            | ❌       |
| `notes`        | string                                              | ❌       |

---

### PlotTrack

`$defs.PlotTrack` (`additionalProperties: false`)

- **signposts** (array, **exactly 4**):

  - Each signpost (`additionalProperties: false`):
    | Field | Type | Required |
    |----------|------------------------------|----------|
    | `type` | string, `$defs.TypeName` | ✅ |
    | `title` | string | ❌ |
    | `summary`| string | ❌ |
    | `beats` | array of `{id,label,text}` | ❌ |
    - Beat (`additionalProperties: false`): `id?: string`, `label?: string`, `text?: string`

- **journeys** (array, 0–3 items):
  - Each journey (`additionalProperties: false`):
    | Field | Type | Required | Constraints |
    |--------------|----------|----------|------------------|
    | `from_index` | integer | ✅ | min 0, max 2 |
    | `to_index` | integer | ✅ | min 1, max 3 |
    | `summary` | string | ❌ | |

> Indexing is **0-based** for signposts: `0..3`.

---

### Character

`$defs.Character` (`additionalProperties: false`)

| Field                 | Type / Enum                                                                                                         | Required | Notes                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------- | -------- | ---------------------------------------- |
| `id`                  | string                                                                                                              | ✅       | Must be unique across players.           |
| `name`                | string                                                                                                              | ✅       | Display name.                            |
| `archetype`           | enum: `Protagonist`,`Antagonist`,`Contagonist`,`Guardian`,`Reason`,`Emotion`,`Sidekick`,`Skeptic`,`Complex`,`Other` | ❌       |                                          |
| `is_main_character`   | boolean (default `false`)                                                                                           | ❌       |                                          |
| `is_impact_character` | boolean (default `false`)                                                                                           | ❌       |                                          |
| `dramatic_functions`  | string[]                                                                                                            | ❌       | Freeform tags (e.g., “Hacker”, “Fixer”). |
| `element_assignments` | array of objects (`additionalProperties: false`)                                                                    | ❌       | Map Dramatica Elements to character.     |
| └ `slot`              | enum: `Motivation`,`Methodology`,`Evaluation`,`Purpose`                                                             | ✅       | Dramatica quads mapping.                 |
| └ `element`           | string, `$defs.ElementName`                                                                                         | ✅       |                                          |
| └ `weight`            | number (0..1)                                                                                                       | ❌       | Strength/coverage.                       |
| └ `notes`             | string                                                                                                              | ❌       |                                          |
| `notes`               | string                                                                                                              | ❌       |                                          |

---

### Enums: `TypeName`, `VariationName`, `ElementName`

#### `TypeName`
```

Understanding, Doing, Obtaining, Learning,
Past, Progress, Future, Present,
Conceiving, Conceptualizing, Being, Becoming,
Memory, Conscious, Subconscious, Preconscious

```

#### `VariationName`
```

Knowledge, Thought, Ability, Desire,
Skill, Experience, Worry, Worth,
Fact, Security, Threat, Fantasy,
Truth, Evidence, Suspicion, Falsehood,
Senses, Interpretation, Conditioning, Instinct,
Wisdom, Enlightenment, Morality, Self-Interest,
Approach, Attitude, Self-Aware, Aware,
Permission, Need, Expediency, Deficiency,
Strategy, Analysis, Inaction, Reaction,
State of Being, Sense of Self, Situation, Circumstances,
Openness, Preconception, Delay, Choice,
Rationalization, Obligation, Commitment, Responsibility

```

#### `ElementName`
```

Logic, Feeling, Control, Uncontrolled,
Help, Hinder, Conscience, Temptation,
Pursuit, Avoid, Support, Oppose,
Trust, Test, Consider, Reconsider,
Faith, Disbelief, Acceptance, Non-acceptance,
Accurate, Non-Accurate, Cause, Effect,
Unproven, Proven, Theory, Hunch,
Result, Process, Expectation, Determination,
Prerequisite, Preconditions, Forethought, Afterthought,
Self-Aware, Aware, State of Being, Sense of Self,
Knowledge, Thought, Ability, Desire,
Skill, Experience, Worry, Worth,
Chance, Design, Attraction, Repulsion,
Order, Chaos, Self-Interest, Morality

````

---

## Cross-Field Consistency (Recommended)

> These are **best-practice rules** not enforced by the schema (unless you add custom validators):

1. **Concern matches Domain family**
   - `Activity` → Concern ∈ `{Understanding, Doing, Obtaining, Learning}`
   - `Situation` → Concern ∈ `{Past, Progress, Future, Present}`
   - `Psychology` → Concern ∈ `{Conceiving, Conceptualizing, Being, Becoming}`
   - `Mind` → Concern ∈ `{Memory, Conscious, Subconscious, Preconscious}`
2. **Issue / Counterpoint** should be siblings in the Variation set under the selected Concern (per Dramatica theory).
3. **Problem/Solution** and **Symptom/Response** should form valid Dramatica dynamic pairs.
4. **Benchmark** should also belong to the same Type family as the throughline’s Domain (see #1).
5. **Relationships.ids** must reference existing `players[].id` and avoid duplicates within the same relationship entry.
6. **Unique IDs**
   - `characters.players[].id` must be globally unique.
   - `plot_progression.*.signposts[i].beats[].id` should be unique per signpost for tooling.

---

## Validation Notes

- **Strictness**:
  - `storyform`, `throughlines.*`, `plot_progression.*`, `characters.players[]`, `characters.relationships[]` all have `additionalProperties: false` (no extra keys).
  - `metadata` and `storyform.appreciations` are **extensible** (`additionalProperties: true`) to allow custom fields/NCP hooks.
- **Indexing**: `journeys[].from_index`/`to_index` are **0-based** signpost indices with bounds checking.
- **Cardinality**: Each PlotTrack must have **exactly 4** signposts.

---

## Minimal Valid Instance

```json
{
  "version": "1.0.0",
  "metadata": {
    "title": "ASTRO7EX",
    "author": "Hubertimus Magillicutty",
    "created_at": "2025-08-24T21:00:00Z",
    "tags": ["dramatica", "ncp"]
  },
  "storyform": {
    "dynamics": {
      "driver": "Action",
      "limit": "Optionlock",
      "outcome": "Success",
      "judgment": "Good"
    },
    "appreciations": {
      "goal": "Understanding",
      "consequence": "Memory",
      "benchmark": "Learning",
      "problem": "Non-Accurate",
      "solution": "Accurate",
      "focus": "Consider",
      "direction": "Reconsider"
    }
  },
  "throughlines": {
    "overall_story": {
      "domain": "Activity",
      "concern": "Understanding",
      "issue": "Knowledge",
      "counterpoint": "Thought",
      "problem": "Non-Accurate",
      "solution": "Accurate",
      "symptom": "Consider",
      "response": "Reconsider",
      "benchmark": "Learning",
      "notes": "OS notes."
    },
    "main_character": {
      "domain": "Mind",
      "concern": "Past",
      "issue": "Truth",
      "problem": "Non-Accurate",
      "solution": "Accurate",
      "symptom": "Consider",
      "response": "Reconsider"
    },
    "impact_character": {
      "domain": "Fixed Attitude" ? "Mind",
      "concern": "Memory",
      "issue": "Evidence",
      "problem": "Non-Accurate",
      "solution": "Accurate",
      "symptom": "Consider",
      "response": "Reconsider"
    },
    "relationship_story": {
      "domain": "Psychology",
      "concern": "Becoming",
      "issue": "Commitment",
      "problem": "Non-Accurate",
      "solution": "Accurate",
      "symptom": "Consider",
      "response": "Reconsider"
    }
  },
  "plot_progression": {
    "overall_story": {
      "signposts": [
        { "type": "Understanding" },
        { "type": "Doing" },
        { "type": "Obtaining" },
        { "type": "Learning" }
      ]
    },
    "main_character": {
      "signposts": [
        { "type": "Past" },
        { "type": "Progress" },
        { "type": "Future" },
        { "type": "Present" }
      ]
    },
    "impact_character": {
      "signposts": [
        { "type": "Memory" },
        { "type": "Conscious" },
        { "type": "Preconscious" },
        { "type": "Subconscious" }
      ]
    },
    "relationship_story": {
      "signposts": [
        { "type": "Conceiving" },
        { "type": "Being" },
        { "type": "Becoming" },
        { "type": "Conceptualizing" }
      ]
    }
  },
  "characters": {
    "players": [
      { "id": "VIVIAN", "name": "Vivian", "archetype": "Complex", "is_main_character": true },
      { "id": "MODS", "name": "MODS", "archetype": "Other", "is_impact_character": true }
    ],
    "relationships": [
      { "ids": ["VIVIAN", "MODS"], "type": "Main_vs_Impact", "label": "Clerks of the Apocalypse" }
    ]
  }
}
````

> Note: Replace the placeholder `"Fixed Attitude" ? "Mind"` with `"Mind"`; “Fixed Attitude” is the _conceptual label_ for the **Mind** domain.

---

## Scaffold Template (Fill-In-The-Blanks)

```json
{
  "version": "1.0.0",
  "metadata": {
    "title": "",
    "logline": "",
    "author": "",
    "created_at": "YYYY-MM-DDTHH:MM:SSZ",
    "updated_at": "YYYY-MM-DDTHH:MM:SSZ",
    "tags": []
  },
  "storyform": {
    "dynamics": {
      "driver": "Action",
      "limit": "Optionlock",
      "outcome": "Success",
      "judgment": "Good"
    },
    "appreciations": {
      "goal": "",
      "consequence": "",
      "requirements": "",
      "prerequisites": "",
      "forewarnings": "",
      "cost": "",
      "dividend": "",
      "focus": "",
      "direction": "",
      "problem": "",
      "solution": "",
      "unique_ability": "",
      "critical_flaw": "",
      "benchmark": ""
    }
  },
  "throughlines": {
    "overall_story": {
      "domain": "Activity",
      "concern": "",
      "issue": "",
      "counterpoint": "",
      "problem": "",
      "solution": "",
      "symptom": "",
      "response": "",
      "benchmark": "",
      "notes": ""
    },
    "main_character": {
      "domain": "Mind",
      "concern": "",
      "issue": "",
      "counterpoint": "",
      "problem": "",
      "solution": "",
      "symptom": "",
      "response": "",
      "benchmark": "",
      "notes": ""
    },
    "impact_character": {
      "domain": "Mind",
      "concern": "",
      "issue": "",
      "counterpoint": "",
      "problem": "",
      "solution": "",
      "symptom": "",
      "response": "",
      "benchmark": "",
      "notes": ""
    },
    "relationship_story": {
      "domain": "Psychology",
      "concern": "",
      "issue": "",
      "counterpoint": "",
      "problem": "",
      "solution": "",
      "symptom": "",
      "response": "",
      "benchmark": "",
      "notes": ""
    }
  },
  "plot_progression": {
    "overall_story": {
      "signposts": [
        { "type": "" },
        { "type": "" },
        { "type": "" },
        { "type": "" }
      ],
      "journeys": []
    },
    "main_character": {
      "signposts": [
        { "type": "" },
        { "type": "" },
        { "type": "" },
        { "type": "" }
      ],
      "journeys": []
    },
    "impact_character": {
      "signposts": [
        { "type": "" },
        { "type": "" },
        { "type": "" },
        { "type": "" }
      ],
      "journeys": []
    },
    "relationship_story": {
      "signposts": [
        { "type": "" },
        { "type": "" },
        { "type": "" },
        { "type": "" }
      ],
      "journeys": []
    }
  },
  "characters": {
    "players": [
      {
        "id": "",
        "name": "",
        "archetype": "Complex",
        "is_main_character": false,
        "is_impact_character": false,
        "dramatic_functions": [],
        "element_assignments": [
          { "slot": "Motivation", "element": "", "weight": 1.0, "notes": "" }
        ],
        "notes": ""
      }
    ],
    "relationships": [
      { "ids": ["", ""], "type": "Other", "label": "", "notes": "" }
    ]
  }
}
```

---

## Quick JSONPath/Pointer Reference

- OS Problem: `$..throughlines.overall_story.problem` → `/throughlines/overall_story/problem`
- MC Concern: `$..throughlines.main_character.concern` → `/throughlines/main_character/concern`
- RS Signpost 3 Type: `$.plot_progression.relationship_story.signposts[2].type`
- Character by ID `"VIVIAN"`: `$..characters.players[?(@.id=="VIVIAN")]`
- All beat texts: `$..signposts[*].beats[*].text`

---

## FAQ / Notes

- **Why are some sections extensible?**
  `metadata` and `storyform.appreciations` allow extra keys for **NCP** integration or custom analytics.
- **Where’s “Dividend” vs “Collateral Benefit”?**
  This schema uses `dividend` to align with classic Dramatica terminology; feel free to mirror an alias in your tooling.
- **Domain labels vs theory nicknames**
  Use enum values (`Activity`, `Situation`, `Psychology`, `Mind`) in data; keep nicknames (e.g., “Fixed Attitude”) for UI.

---

```

```
