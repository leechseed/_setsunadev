YAML How-TO

---
title: "How to Use the YAML Frontmatter Template"
project: "Beltline Salvation"
author: "Hubertimus Magillicutty"
date_created: "2025-07-24"
last_updated: "2025-07-24"
version: "v1.0"
phase: "Global"
document_type: "Manual"
status: "Final"
related_blueprints: []
related_phases:
  - "All"
tags:
  - "PMP"
  - "Documentation"
  - "Binder"
  - "Metadata"
  - "YAML"
table_of_contents: true
---

# 📘 How to Use the YAML Frontmatter Template

This document explains how to apply and manage the YAML frontmatter block at the beginning of each markdown file in your **Beltline Salvation** project binder. This metadata enables organization, indexing, searchability, and version tracking across your documentation system.

---

## 📚 Table of Contents

1. [🎯 Purpose](#-purpose)  
2. [🧠 What Is YAML Frontmatter?](#-what-is-yaml-frontmatter)  
3. [🔧 When to Use It](#-when-to-use-it)  
4. [📋 Field Descriptions](#-field-descriptions)  
5. [📦 Example Use Case](#-example-use-case)  
6. [✅ Best Practices](#-best-practices)  
7. [🧪 Validation and Consistency Tips](#-validation-and-consistency-tips)

---

## 🎯 Purpose

The YAML frontmatter block standardizes the structure of every binder document so that:

- Files are searchable and sortable by **phase**, **status**, or **type**.
- Project artifacts remain traceable and versioned.
- Third-party tools (like GitBook, Obsidian, or static site builders) can render metadata consistently.

---

## 🧠 What Is YAML Frontmatter?

YAML frontmatter is a block of structured metadata at the top of a markdown file. It’s wrapped in triple dashes (`---`) and contains key-value pairs used to tag, track, and organize the document.

It **does not display** in rendered markdown but is **used by systems** to index or manipulate your content.

---

## 🔧 When to Use It

Include the YAML block in **every document** in the binder, including:

- Phase Playbooks  
- Transition Checklists  
- Blueprint Registers  
- Risk Logs  
- Daily Logs or Reports  
- Resource Maps  
- Final Launch Summary  

---

## 📋 Field Descriptions

| Field             | Description |
|------------------|-------------|
| `title`           | Human-readable name of the document. |
| `project`         | Always `"Beltline Salvation"` (for global searchability). |
| `author`          | Who created or owns the document. |
| `date_created`    | When this doc was first made. Format: `YYYY-MM-DD`. |
| `last_updated`    | Last revision date. |
| `version`         | Track using `vX.X`. Increment with meaningful changes. |
| `phase`           | The related project phase (`Phase 1`, `Global`, etc). |
| `document_type`   | Helps sort the doc: `Playbook`, `Checklist`, `Log`, etc. |
| `status`          | Track doc readiness: `Draft`, `In Progress`, or `Final`. |
| `related_blueprints` | List of blueprint names or URLs. Optional. |
| `related_phases`  | Phases affected by or referenced in the document. |
| `tags`            | Freeform keywords for searching and filtering. |
| `table_of_contents` | `true` if this doc includes a ToC. Most should. |

---

## 📦 Example Use Case

A `Phase 3: Rail Logistics` Playbook might begin with:

```yaml
---
title: "Phase 3 Playbook: Rail Logistics"
project: "Beltline Salvation"
author: "Hubertimus Magillicutty"
date_created: "2025-07-25"
last_updated: "2025-07-26"
version: "v1.1"
phase: "Phase 3"
document_type: "Playbook"
status: "In Progress"
related_blueprints: 
  - "Train Unloader v2.0"
  - "T-Junction Blueprint v1.3"
related_phases:
  - "Phase 2"
  - "Phase 4"
tags:
  - "Rail"
  - "Factorio"
  - "Logistics"
  - "Belt Only"
table_of_contents: true
---


id: 19fdfd1068df4eff92e59bfa9db478ff
parent_id: e48e624aea1b47bc8431a60d412f3f4e
created_time: 2025-07-24T21:00:52.430Z
updated_time: 2025-07-24T21:01:06.100Z
is_conflict: 0
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
author: 
source_url: 
is_todo: 0
todo_due: 0
todo_completed: 0
source: joplin-desktop
source_application: net.cozic.joplin-desktop
application_data: 
order: 0
user_created_time: 2025-07-24T21:00:52.430Z
user_updated_time: 2025-07-24T21:01:06.100Z
encryption_cipher_text: 
encryption_applied: 0
markup_language: 1
is_shared: 0
share_id: 
conflict_original_id: 
master_key_id: 
user_data: 
deleted_time: 0
type_: 1