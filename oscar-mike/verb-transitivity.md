---
parked: 2026-09-06
title: The Transitive-Verb Kit
handle: verb quiz
tags: grammar, writing-craft, learning-tool, BLACK, artifact
status: parked on "Oscar Mike" ×3 — three deliverables on disk, last one live; whether v3 of the quiz satisfied is unknown
open-decision: none named; resumes if Papi calls the quiz or the tree again
---

# THE TRANSITIVE-VERB KIT

A stacked break-break on 9/6 that ran four turns. Papi pasted a machine-facing "verb argument structure" prompt and asked for it better; what he actually wanted was a head model and then a drill.

## What exists

| Piece | Where | State |
|---|---|---|
| Knowledge base v2 (machine-facing: 5 labels, 8 tests, 18 traps, JSON schema, 32 ground-truth rows) | `_tools/prompts/verb-argument-structure-v2.md` | done; Papi's reaction: "what the fuck is all this" — not what he needed |
| The head version: three-question tree + the one trap + the writing-side rule | `_tools/prompts/verb-decision-tree.md` | done, with the Mermaid appended |
| The quiz, **Transitive or Not** — 24 sentences, TRANSITIVE / INTRANSITIVE buttons, keys T/I, shuffle, flash, score + missed list | `_tools/prompts/verb-quiz.html` · live: https://claude.ai/code/artifact/187a273e-ceef-4c69-b802-7177a4da27f4 | v3 published; v1 had explanations (struck: "nothing else"), v2 was true/false, v3 is the two-label form with the three linking sentences swapped for clean intransitives |

## The tree (so this card stands alone)

1. Swap the verb for *is/was/seems*. Same meaning? → linking, neither.
2. Ask "[verb] what/whom?" Answer right after the verb, no little word in front? No → intransitive.
3. Flip it: can that thing be the subject of "was ___ed"? No → intransitive (measurement). Yes → transitive.
Trap: a little word between verb and thing ("looked UP the word") — move it after the thing; works → part of the verb, go to 3.

## The lesson (feedback, saved to memory)

Papi-facing learning tools are the sentence and the buttons. The complete version reads as noise and burns patience. Head version first; the machine version only if he says it is for a machine and means it.

## Resume

Nothing owed. If called: the quiz bank is a 24-row array in the HTML, easy to grow; the tree file is the teaching doc.
