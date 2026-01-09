---
title: readme.md
updated: 2025-09-06 21:50:37Z
created: 2025-09-06 21:50:24Z
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
---



# ☕ CoffeeBreak Screenwriter Digitization

This repo encodes the *CoffeeBreak Screenwriter* step-by-step workflow into **Markdown + YAML front-matter** so it can be referenced by AI agents, compiled into databases, or used manually as a structured writing process.

---

## 📂 Folder Structure

```
coffeebreak/
├─ steps/          # one file per step (with YAML + Markdown body)
│  ├─ 01-010.md
│  ├─ 01-020.md
│  └─ ...
├─ artifacts/      # generated outputs, versions, alternates
├─ refs/           # research notes, external references
├─ schema/         # JSON + SQL schema definitions
└─ README.md       # this file
```

---

## 🟨 YAML Template (Lean)

Every step file begins with this metadata:

```yaml
---
id: CB-01010
title: 
chapter_index: 1
step_rank: 10
status: draft   # draft | in_progress | review | approved
updated: 2025-09-06
---
```

* **id**: Stable reference (chapter + step, or ULID if preferred).
* **title**: Fill in later (e.g. "Refine Character Arcs").
* **chapter\_index**: Which chapter the step belongs to.
* **step\_rank**: Order inside the chapter (spaced: 10, 20, 30…).
* **status**: Track workflow progress.
* **updated**: Quick timestamp.

---

## 📝 Filename Convention

```
{chapter_index zero-padded}-{step_rank zero-padded}-{short_title}.md
```

Examples:

* `01-010.md`
* `01-020.md`
* `03-093-refine_character_arcs.md`

This ensures steps stay sorted in order by filename.

---

## 🔢 Ordering System

* **chapter\_index** = the “bucket” (Chapter 1, Chapter 2, …).
* **step\_rank** = the position inside the bucket.
* Use increments of **10** (10, 20, 30) so you can insert later steps (15, 25, etc.) without renumbering everything.

---

## 📖 Example — Chapter 1 (10 Steps)

Here’s a skeleton of 10 steps for Chapter 1. Titles left blank for you to fill in later.

```yaml
---
id: CB-01010
title: 
chapter_index: 1
step_rank: 10
status: draft
updated: 2025-09-06
---
```

```yaml
---
id: CB-01020
title: 
chapter_index: 1
step_rank: 20
status: draft
updated: 2025-09-06
---
```

```yaml
---
id: CB-01030
title: 
chapter_index: 1
step_rank: 30
status: draft
updated: 2025-09-06
---
```

```yaml
---
id: CB-01040
title: 
chapter_index: 1
step_rank: 40
status: draft
updated: 2025-09-06
---
```

```yaml
---
id: CB-01050
title: 
chapter_index: 1
step_rank: 50
status: draft
updated: 2025-09-06
---
```

```yaml
---
id: CB-01060
title: 
chapter_index: 1
step_rank: 60
status: draft
updated: 2025-09-06
---
```

```yaml
---
id: CB-01070
title: 
chapter_index: 1
step_rank: 70
status: draft
updated: 2025-09-06
---
```

```yaml
---
id: CB-01080
title: 
chapter_index: 1
step_rank: 80
status: draft
updated: 2025-09-06
---
```

```yaml
---
id: CB-01090
title: 
chapter_index: 1
step_rank: 90
status: draft
updated: 2025-09-06
---
```

```yaml
---
id: CB-01100
title: 
chapter_index: 1
step_rank: 100
status: draft
updated: 2025-09-06
---
```

---

## ✅ Usage

1. **Create a step file** using the filename convention.
2. **Fill the YAML front-matter** (title + status).
3. **Write your notes or outputs** in the Markdown body.
4. **Track progress** by updating the `status` field.
5. Optionally compile to **JSONL / SQLite** for AI queries.

---

## 🚀 Next Steps

* Scaffold all chapters with blank step YAMLs.
* Add optional `scripts/` folder with generators (Python/PowerShell).
* Hook into a SQLite/JSONL pipeline if you want AI agents to reference these steps.

---

Would you like me to expand this README with a **ready-to-run “Getting Started” section** (like copy-paste commands to scaffold steps, and how to query them later)?
