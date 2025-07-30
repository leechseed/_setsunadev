---

## 🧠 Objective

Design a **schema-compatible, API-extensible, declarative interface** for all storypoints—based on Dramatica but abstracted to be:

* ✅ Extensible (custom or experimental storypoints allowed)
* ✅ Structured (squad → platoon → company hierarchy)
* ✅ Machine-parseable (for APIs or agents)
* ✅ Joplin-linkable (for your knowledge system)
* ✅ Compatible with the `betterstories` schema via `$ref` or import

---

## ✅ Recommended Data Model

### Format: **YAML / JSON / DB Table (Normalized)**

```yaml
storypoints:
  - id: SP001
    name: Problem
    squad: Appreciation
    platoon: Throughline
    company: OverallStory
    occurrences: 4
    canonical_function: Root conflict in domain
    method_enum: problem
    schema_path: $defs.StoryPoint.method
    joplin_link: joplin://uuid-of-problem-note

  - id: SP002
    name: Catalyst
    squad: Appreciation
    platoon: Act Dynamic
    company: OS/RS/MC/IC (varies)
    occurrences: 4
    canonical_function: Drives progression
    method_enum: catalyst
    schema_path: $defs.StoryPoint.method
    joplin_link: joplin://catalyst-uuid
```

---

## 🧩 Integrates With `betterstories` via:

### 1. **Enum Linking**

In your schema:

```json
"$defs": {
  "MethodEnum": {
    "type": "string",
    "enum": [ /* pull from storypoint_table.method_enum */ ]
  }
}
```

You can write a small script that **auto-generates MethodEnum** from your table.

---

### 2. **Dynamic StoryPoint Loader**

For future extensibility:

```ts
// Load from external config or database
const storypointTable = loadYAML("storypoint-table.yml");

// Generate valid MethodEnum
const methodEnum = storypointTable.map((sp) => sp.method_enum);
```

---

## 🧱 Suggested Table Fields

| Field                | Description                                     |
| -------------------- | ----------------------------------------------- |
| `id`                 | Stable internal ID (SP001–SP144 or UUID)        |
| `name`               | Human-readable storypoint name                  |
| `squad`              | Micro-layer (Appreciation, Tone, Structural)    |
| `platoon`            | Mid-layer group (e.g. Throughline, Act Dynamic) |
| `company`            | Macro-group (e.g. OverallStory, Signpost, etc.) |
| `occurrences`        | How often it appears (e.g., 1–4)                |
| `canonical_function` | Purpose / thematic logic                        |
| `method_enum`        | What it maps to in `MethodEnum` (if any)        |
| `schema_path`        | Where it appears in `betterstories`             |
| `joplin_link`        | Deep link to your research note                 |

---

## 🔌 Clean API Example

```http
GET /api/storypoints

[
  {
    "id": "SP001",
    "name": "Problem",
    "method_enum": "problem",
    "schema_path": "$defs.StoryPoint.method",
    "linked_throughlines": ["OverallStory", "MainCharacter"],
    "canonical_function": "Core conflict driver"
  }
]
```

---
