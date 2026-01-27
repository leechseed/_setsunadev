---
tags:
  - oxo
---


```markdown
# 📘 AI Docs Agent — Operational README
**Canonical Knowledgebase Entry**

---

## Table of Contents

1. [What This System Is](#what-this-system-is)
2. [System Architecture (Mental Model)](#system-architecture-mental-model)
3. [Directory Layout](#directory-layout)
4. [Prerequisites](#prerequisites)
5. [Startup — From Zero to Query](#startup--from-zero-to-query)
6. [Tagging Rules (CRITICAL)](#tagging-rules-critical)
7. [Indexing Process](#indexing-process)
8. [Querying Documents](#querying-documents)
9. [Shutdown / Safe Stop](#shutdown--safe-stop)
10. [How to Verify It’s Working](#how-to-verify-its-working)
11. [Common Failure Modes (and What They Mean)](#common-failure-modes-and-what-they-mean)
12. [What NOT to Change](#what-not-to-change)
13. [Recovery Checklist (When Something Breaks)](#recovery-checklist-when-something-breaks)

---

## 1. What This System Is

This is a **local semantic document retrieval system** for Markdown knowledgebases.

It allows you to:

- Hard-filter documents by **canonical tags**
- Embed and index Markdown files into a vector database (FAISS)
- Ask natural-language questions against only the documents you authorize
- Treat your writing as **lawful reference material**, not loose notes

It is **not**:
- A live editor
- A file watcher
- A sync engine
- A knowledge graph

It is a **read-only retrieval engine**.

---

## 2. System Architecture (Mental Model)

Think of the system as **three irreversible phases**:

### Phase 1 — Documents (Authoritative Source)
- Markdown files live in **Obsidian**
- Tags are assigned using YAML front matter
- Obsidian is the *source of truth*

### Phase 2 — Index Build (Compilation)
- `index_docs.py`:
  - Scans files
  - Filters by required tags
  - Chunks text
  - Builds embeddings
  - Writes FAISS index + metadata

This phase is **destructive**:
> If a document is not indexed here, it does not exist to the system.

### Phase 3 — Query (Read-Only)
- `ask_docs.py`:
  - Loads the index
  - Embeds your query
  - Retrieves top matches
  - Shows excerpts + file paths

No writes. No mutation. No inference.

---

## 3. Directory Layout

### Vault (Authoring)


C:\Users\U01_LEECHSEED\Desktop_setsunadev  
└── OVER_EXIT_OUT_OBSIDIAN  
└── OVEREXITOUT  
├── 📘 documents.md  
├── folders/  
└── ...

```

### Agent (Execution)
```

C:\Users\U01_LEECHSEED\Desktop\ai-docs-agent  
├── index_docs.py  
├── ask_docs.py  
├── config.json  
├── docs.index  
├── docs.jsonl  
├── build_meta.json  
└── .venv\

````

## 4. Prerequisites

### Python
- Python **3.11.x**
- Virtual environment recommended

### Required packages
Installed **inside `.venv`**:
- `sentence-transformers`
- `faiss`
- `numpy`

---

## 5. Startup — From Zero to Query

### Step 1 — Activate environment
```powershell
.\.venv\Scripts\activate
````

You should see:

```
(.venv)
```

---

### Step 2 — Confirm config

Open `config.json` and verify:

```json
"source_dir": "C:/Users/U01_LEECHSEED/Desktop/_setsunadev/OVER_EXIT_OUT_OBSIDIAN/OVEREXITOUT"
```

This must point to the **Obsidian vault root**.

---

### Step 3 — Build the index

```powershell
python index_docs.py
```

Expected result:

- `DONE.`
    
- `chunks_indexed > 0`
    
- Files written:
    
    - `docs.index`
        
    - `docs.jsonl`
        
    - `build_meta.json`
        

---

### Step 4 — Query

```powershell
python ask_docs.py
```

You are now live.

---

## 6. Tagging Rules (CRITICAL)

### Canonical Tag Format (REQUIRED)

Use **Obsidian Properties / YAML front matter**:

```yaml
---
tags:
  - oxo
---
```

### Rules

- YAML **must be at the very top**
    
- Tags are **case-insensitive**
    
- Tags are **hard filters**
    
- If a document lacks the required tag → **it does not exist**
    

### Do NOT use

- Inline `#oxo`
    
- Joplin tag metadata
    
- Filename hacks
    

Only YAML front matter counts.

---

## 7. Indexing Process

What `index_docs.py` does:

1. Recursively scans `.md` files under `source_dir`
    
2. Reads YAML front matter
    
3. Normalizes tags
    
4. Applies **required_tags** filter
    
5. Strips junk metadata (lat/long/etc.)
    
6. Chunks text
    
7. Embeds with SentenceTransformers
    
8. Writes FAISS index
    

Re-run this script **every time** you:

- Add documents
    
- Change tags
    
- Edit important content
    

---

## 8. Querying Documents

Inside `ask_docs.py`:

- Type natural language questions
    
- Results show:
    
    - Score
        
    - File path
        
    - Chunk excerpt
        

Commands:

- `:file N` → dump full document for result `N`
    
- `:quit` → exit
    

---

## 9. Shutdown / Safe Stop

There is **no daemon**.

To shut down:

- Exit `ask_docs.py`
    
- Deactivate venv (optional)
    

```powershell
deactivate
```

No cleanup required.

---

## 10. How to Verify It’s Working

### Check index metadata

```powershell
python -c "import json; print(json.load(open('build_meta.json')))"
```

Confirm:

- `chunks_indexed > 0`
    
- `required_tags` is correct
    
- `source_dir` is correct
    

### Sanity query

Ask:

```
narrative invariants
```

You should get:

- Results from tagged OXO documents only
    
- Correct file paths into Obsidian vault
    

---

## 11. Common Failure Modes (and What They Mean)

### ❌ “No documents indexed”

Means:

- Tag missing
    
- YAML not at top
    
- Wrong vault path
    
- Tag mismatch (`oxo` vs `OXO` handled, spelling not)
    

---

### ❌ Old content showing

Means:

- Index not rebuilt
    
- You edited docs but didn’t re-run `index_docs.py`
    

---

### ❌ Garbage metadata in results

Means:

- Front matter stripping not applied
    
- You indexed before the fixed script
    

Rebuild index.

---

## 12. What NOT to Change

Do not casually modify:

- `index_docs.py` parsing logic
    
- Tag normalization rules
    
- FAISS index settings
    
- Chunk size unless you understand retrieval impact
    

This system is **intentionally conservative**.

---

## 13. Recovery Checklist (When Something Breaks)

1. Confirm Obsidian files exist
    
2. Confirm YAML tags exist at top
    
3. Confirm `source_dir`
    
4. Delete:
    
    - `docs.index`
        
    - `docs.jsonl`
        
    - `build_meta.json`
        
5. Re-run:
    
    ```powershell
    python index_docs.py
    ```
    
6. Query again
    

If step 5 fails → the problem is **documents or tags**, not the code.

---

## Final Note

This system is **not smart**.  
That is why it is **trustworthy**.

It does exactly what you authorize, nothing more.

End of document.

```

---

If you want later:
- multi-tag modes
- Obsidian backlink awareness
- section-level citations
- agent-driven synthesis

That’s **next phase**.  
For now: you have a **stable, lawful reference engine**.
```