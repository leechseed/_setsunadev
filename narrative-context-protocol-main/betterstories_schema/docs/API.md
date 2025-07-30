# 📘 API Integration Report: Storypoint Ontology Layer for BetterStories

**Section**: Narrative Schema Architecture
**Project**: BetterStories Schema
**Studio**: \[Your Studio or Handle Here]
**Date**: \[Insert Date]
**Prepared by**: Schema Systems Architect

---

## 🎯 Objective

To design a modular, extensible, and schema-compliant API interface for managing, extending, and integrating Dramatica-style storypoints into the `betterstories` JSON Schema system.

---

## 🧭 Context

The original `betterstories` schema references a large enum (\~144+ values) embedded in multiple places. While functional, this approach is:

- ❌ Redundant
- ❌ Hard to maintain
- ❌ Opaque for external systems or non-technical users

This report outlines a **new approach**: creating a centralized, versioned, API-driven **Storypoint Ontology Layer**, integrated cleanly into the `betterstories` JSON Schema structure.

---

## 📐 Core Design Goals

### ✅ Modular

Storypoints should be defined once and imported cleanly into the schema.

### ✅ Declarative

All attributes (e.g., `squad`, `platoon`, `company`, etc.) should be exposed in a normalized, extensible format.

### ✅ Schema-Aware

Storypoints should include `method_enum` references and `schema_path` bindings to support automation.

### ✅ Human + Machine Friendly

Must support:

- Agent systems
- Schema generators
- Human readers (e.g., Joplin-linked notes)

---

## 🧱 Data Model

### Table Structure (Recommended Fields)

| Field                | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| `id`                 | Stable internal ID (e.g., SP001)                            |
| `name`               | Human-readable name (e.g., "Problem")                       |
| `squad`              | Functional micro-layer (e.g., Appreciation, Tone)           |
| `platoon`            | Structural group (e.g., Throughline, Act Dynamic)           |
| `company`            | Thematic macro-layer (e.g., OverallStory, Signpost)         |
| `occurrences`        | Number of times this appears in a Dramatica-style storyform |
| `canonical_function` | Narrative purpose (e.g., "Root conflict in domain")         |
| `method_enum`        | Token string used in MethodEnum for schema compatibility    |
| `schema_path`        | Reference to JSON Schema (e.g., `$defs.StoryPoint.method`)  |
| `joplin_link`        | Deep link to note in research vault (optional)              |

### Example Entry (YAML Format)

```yaml
- id: SP001
  name: Problem
  squad: Appreciation
  platoon: Throughline
  company: OverallStory
  occurrences: 4
  canonical_function: Root conflict in domain
  method_enum: problem
  schema_path: $defs.StoryPoint.method
  joplin_link: joplin://problem-note-uuid
```

---

## 🔌 API Design (REST Example)

### Endpoint

```http
GET /api/storypoints
```

### Response

```json
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

## 🧩 Integration with Schema

### Enum Linking

```json
"$defs": {
  "MethodEnum": {
    "type": "string",
    "enum": [ /* values dynamically loaded from API or YAML */ ]
  }
}
```

### Automation Pipeline

```ts
// Load and map storypoints
const storypoints = loadYAML("storypoints.yml");
const methodEnum = storypoints.map((sp) => sp.method_enum);
```

---

## ✅ Benefits

- 🔁 **DRY**: Define once, reuse everywhere
- 🧠 **Ontology Mapping**: Clean logical groupings by squad/platoon/company
- 🧩 **Schema Composability**: Path-based references allow partial validation and component growth
- 🧠 **Knowledge Linkage**: Joplin deep links and research sync
- 🔮 **Agent Ready**: Designed for integration into LLM logic or game engines

---

## 🏁 Next Steps

1. Build YAML storypoint catalog (starting with canonical 16)
2. Script enum extraction for `$defs.MethodEnum`
3. Implement API endpoint
4. Link Joplin note UUIDs into table
5. Version and publish to `/schema/storypoints.yml`

---

## 🧪 Internal Tags

`#betterstories` `#schema` `#storypoint-api` `#dramatic-ontology` `#linked-schema`

---

> “It’s not just a schema anymore. It’s a story OS.”
