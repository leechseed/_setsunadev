# MemPalace intake

Source: [github.com/MemPalace/mempalace](https://github.com/MemPalace/mempalace). Read 2026-10-17.

## What it is
- A local-first memory system for AI chats. The MemPalace org makes it. License is MIT ([repo](https://github.com/MemPalace/mempalace)).
- It stores text verbatim, with no summaries. Content sits in wings (people or projects), rooms (topics) and drawers (the original text) ([repo](https://github.com/MemPalace/mempalace)).
- Retrieval is semantic search scoped by wing and room. ChromaDB is the default. Qdrant, pgvector, Milvus and SQLite are opt-in ([repo](https://github.com/MemPalace/mempalace)).
- Embeddings run locally by default. It can also call any OpenAI-compatible endpoint ([repo](https://github.com/MemPalace/mempalace)).
- It adds a temporal knowledge graph in SQLite ([repo](https://github.com/MemPalace/mempalace)).
- It ships a CLI, a Python API, an MCP server with 47 tools, and auto-save hooks for Claude Code ([repo](https://github.com/MemPalace/mempalace)).

## What it would add
- Today the Command recalls by reading MEMORY.md, STATE.md and BOLO.md. Recall is by index and file name, not by meaning.
- MemPalace would search old session text directly. Example: "what did Chief rule about the school name" would hit the original turn, not a one-line summary.
- Auto-save hooks would capture sessions without the Oscar Mike step ([repo](https://github.com/MemPalace/mempalace)).
- For the canon, wings could map to story, Zotero and BOLO. The graph could track who knew what, and when. The SSOT and fabula graph already do this on purpose, so it would be a search layer, not a source of truth.
- It adds nothing for rulings. Those must stay in hand-kept files.

## Risks
- Maturity: 59.6k stars, but 375 open issues and 445 open PRs. Almost all commits come from one author ([commits](https://github.com/MemPalace/mempalace/commits/main)).
- Trust: the authors retracted several launch claims in April. These included "30x lossless" compression, a "+34% boost" and unsourced competitor figures ([HISTORY](https://github.com/MemPalace/mempalace/blob/develop/docs/HISTORY.md)). The remaining 96.6% LongMemEval recall is self-reported.
- Impostors: fake sites spread malware. Only the GitHub repo, PyPI and mempalaceofficial.com are official ([HISTORY](https://github.com/MemPalace/mempalace/blob/develop/docs/HISTORY.md)).
- Data: local by default, and "nothing leaves your machine unless you opt in" ([repo](https://github.com/MemPalace/mempalace)). Private notes would sit in a store the public-repo rules must keep out.
- Lock-in: low. Text is stored verbatim, so export is easy.
- Fit: it recalls text. It does not know the Command's rulings, so stale chat can outrank a newer ruling.

## Verdict: WATCH
**RULED 10/17 ~7:58 PM** (Chief: "go" on the rec): WATCH, no install. Re-check on or after 11/17.

Trial it later on one job: search past session transcripts for "what did we rule on X", on the 3090 with local embeddings, in a scratch folder with no private wing. Not yet, because the project is churning and retracted its claims. Re-check in two months.

## Unverified
- Release date of 3.11.0, and the real quality of retrieval on our data.
- The MCP and hook docs on mempalaceofficial.com were not read.
