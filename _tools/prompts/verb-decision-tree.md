# Is this verb transitive? — the head version

Three questions. Stop at the first answer.

```
                 THE VERB IN YOUR SENTENCE
                           |
   Q1  Swap the verb for "is/was" or "seems".
       Same meaning?   ("She felt tired" -> "She was tired")
           |
      YES -+-> LINKING VERB. Not transitive, not intransitive. Done.
           |
       NO -+
           |
   Q2  Ask "[verb] WHAT?" or "[verb] WHOM?"
       Is there an answer sitting right after the verb,
       with NO little word (to / at / on / under / with) in front of it?
           |
       NO -+-> INTRANSITIVE. Whatever follows is scenery:
           |   where, when, how.  ("walked to school", "rested under the tree",
           |   "sang beautifully")  Done.
           |
      YES -+
           |
   Q3  Flip it. Can that thing become the subject of "was ___ed"?
       ("sang a hymn" -> "a hymn was sung"   YES)
       ("weighs ten pounds" -> "ten pounds was weighed"   NO)
           |
       NO -+-> INTRANSITIVE. It is a measurement or scenery wearing
           |   an object costume. ("ran three miles", "cost five dollars")
           |
      YES -+-> TRANSITIVE. Done.
```

## The one trap worth carrying

A little word sits between the verb and the thing: "looked UP the word" vs "ran UP the hill".
Try moving the little word to after the thing.

- "looked the word up" works -> it is part of the verb -> go to Q3 -> transitive.
- "ran the hill up" does not work -> it is a preposition -> intransitive.

## Two things after the verb

"gave her a book", "elected him president". Still transitive. Q3 still works ("a book was given", "he was elected"). The second thing does not change the answer.

## When you are writing, not reading

Decide whether the action needs something to land on.

- It lands on something -> give the verb a bare object. Transitive.
- It just happens -> no object, add scenery if you want. Intransitive.
- It describes the subject -> use a linking verb (is, seems, feels, becomes).

## Mermaid

```mermaid
flowchart TD
    V(["The verb in your sentence"]) --> Q1{"Q1 · Swap the verb for is / was / seems.<br/>Same meaning?<br/><i>She felt tired → She was tired</i>"}
    Q1 -->|YES| L["LINKING VERB<br/>not transitive, not intransitive"]
    Q1 -->|NO| Q2{"Q2 · Ask: [verb] WHAT? / [verb] WHOM?<br/>Is there an answer right after the verb<br/>with NO little word in front of it?<br/>(to · at · on · under · with)"}
    Q2 -->|NO| I1["INTRANSITIVE<br/>what follows is scenery: where, when, how<br/><i>walked to school · rested under the tree · sang beautifully</i>"]
    Q2 -->|"a little word is in the way<br/>(looked UP the word)"| T{"THE TRAP · move the little word<br/>to after the thing. Does it work?<br/><i>looked the word up ✓ · ran the hill up ✗</i>"}
    T -->|NO| I1
    T -->|YES| Q3
    Q2 -->|YES| Q3{"Q3 · Flip it. Can that thing be<br/>the subject of 'was ___ed'?<br/><i>a hymn was sung ✓ · ten pounds was weighed ✗</i>"}
    Q3 -->|NO| I2["INTRANSITIVE<br/>a measurement or scenery in an object costume<br/><i>ran three miles · cost five dollars</i>"]
    Q3 -->|YES| TR["TRANSITIVE"]
    TR -.-> N["Two things after the verb?<br/><i>gave her a book · elected him president</i><br/>Still transitive. Q3 still works."]

    classDef q fill:#1f2937,color:#f9fafb,stroke:#9ca3af
    classDef yes fill:#14532d,color:#f0fdf4,stroke:#22c55e
    classDef no fill:#3f3f46,color:#fafafa,stroke:#a1a1aa
    classDef link fill:#1e3a8a,color:#eff6ff,stroke:#60a5fa
    classDef note fill:#292524,color:#fafaf9,stroke:#78716c,stroke-dasharray: 4 3
    class Q1,Q2,Q3,T q
    class TR yes
    class I1,I2 no
    class L link
    class N note
```
