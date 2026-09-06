# VERB ARGUMENT STRUCTURE — CLASSIFICATION KNOWLEDGE BASE (v2)

PURPOSE: Classify the lexical verb of an English clause by valency. Emit exactly one label from the closed set in section 1, the argument spans that justify it, and the tests that were applied. Every label must be reached through the procedure in section 4 and backed by the tests in section 3. Determinism over intuition.

## 0. Scope rules

- Classify the LEXICAL verb only. Never classify auxiliaries or modals (be, have, do, will, can, must, get in passives). In "has been eating", classify "eat".
- One classification per CLAUSE. Coordinated verbs and embedded clauses are separate inputs.
- Classify the USE in this sentence, not the lemma. Most lemmas allow several frames (section 1.2).
- Normalize voice before anything else (section 4, step 1). Passives are labeled on their reconstructed active frame.

## 1. Label set (closed)

| Label | Name | Frame | One-line diagnostic |
|---|---|---|---|
| Vl | Linking (copular) | S V PredComp | complement describes or renames S; "be/seem" substitution preserves meaning |
| Vi | Intransitive | S V (adjuncts) | no object; nothing after V can become a passive subject |
| Vt | Monotransitive | S V DO | one direct object; passivizes |
| Vd | Ditransitive | S V IO DO | two bare NPs; dative shift works (V DO to/for IO) |
| Vc | Complex-transitive | S V DO ObjComp | DO plus a phrase predicated of DO ("elected him president", "painted it red", "saw him leave") |

### 1.1 Subtypes (optional field, one value)

- Vi: unergative (S is an agent: run, laugh, work) | unaccusative (S undergoes the event: fall, arrive, melt, break-as-Vi; these are the Vi uses that have a causative Vt twin) | object-drop (a Vt lemma used without its object: "She ate") | prepositional (V selects a PP: rely on, look at) | particle (V + particle, no object: show up, give up) | existential ("There is a problem") | weather ("It rained") | measure (post-verbal measure phrase: weigh, last, cost)
- Vt: clausal (DO is a clause: know that, want to, ask whether) | reflexive/reciprocal (DO is -self / each other) | cognate (DO restates V: sing a song) | particle (look up the word) | light-verb (take a walk, make a decision) | stative (have, resemble, lack: no passive, still Vt)
- Vd: recipient (give, send, tell) | benefactive (bake her a cake)
- Vc: nominal (name him captain) | adjectival (paint it red) | bare-infinitive (make him cry, see him leave) | participial (hear it ringing)

### 1.2 Ambitransitive lemmas (property of the lemma, not the label)

- Object-drop type: eat, read, sing, drive, write. S stays the agent in both uses.
- Causative-inchoative type: break, open, melt, sink, close, grow. In the Vt use S causes the event; in the Vi use the former object is now S. "He broke the glass" (Vt) / "The glass broke" (Vi.unaccusative).

## 2. Definitions

- Direct object (DO): a bare NP or clause (not governed by a preposition) that is an argument of V, answers "V what/whom?", and can become the subject of a passive.
- Indirect object (IO): a bare NP recipient or beneficiary that precedes DO and can be paraphrased as a to/for-PP after DO.
- Object complement (ObjComp): AP, NP, bare infinitive, or participle predicated of DO. Test: "DO is/becomes ObjComp" holds.
- Predicative complement (PredComp): AP, NP, or PP after a linking verb, predicated of S.
- Adjunct: optional modifier of time, place, manner, reason, degree, or duration. Adverb, PP, or bare NP of time/place/measure ("yesterday", "home", "three miles", "two hours"). Never an object.
- Oblique: an NP governed by a preposition that V selects ("rely on X", "listen to X"). Not a DO. The verb stays Vi (prepositional).
- Particle: an adverbial element of a phrasal verb (up, off, out, away) that is not a preposition governing the following NP. Section 3, T7 decides.

## 3. Tests (apply in the order the procedure calls them)

- T1 PASSIVE: the candidate NP can be the subject of a passive with the same verb and meaning. "The hymn was sung" PASS. "*Ten pounds was weighed by the box" FAIL. "*The tree was rested under" FAIL.
- T2 WH-PROBE: "S V what/whom?" is well-formed and the candidate answers it. "The choir sang what? A hymn" PASS. "He walked what?" FAIL.
- T3 BARE-NP: the candidate is not inside a PP. "the ball" PASS. "to school" FAIL.
- T4 PRONOUN SWAP: the candidate can be replaced by it/them/him with no preposition. "sang it" PASS. "*walked it" (for "walked to school") FAIL.
- T5 BE-SUBSTITUTION (linking): replacing V with "be" or "seem" keeps grammaticality and meaning, and the complement still describes S. "He felt tired -> He was tired" PASS, Vl. "He felt the wall -> *He was the wall" FAIL, not Vl.
- T6 DATIVE SHIFT (ditransitive): "V NP1 NP2" alternates with "V NP2 to/for NP1". "gave her a book -> gave a book to her" PASS, Vd. "*named Rex to the dog" FAIL, not Vd.
- T7 PARTICLE MOVEMENT (phrasal vs prepositional): with a pronoun object the particle must follow it. "look up the word -> look it up" PASS, particle, V is Vt. "run up the hill -> *run it up" FAIL, preposition, V is Vi + PP.
- T8 OBJECT PREDICATION (complex-transitive): "DO is/becomes X" holds for the post-DO phrase. "elected him president -> he is president" PASS, Vc.

Decision weights:
- T1 PASS is sufficient for DO.
- T1 FAIL is decisive only when the candidate is a measure, duration, distance, or price phrase (section 5.12): label Vi.measure.
- Otherwise (stative verbs such as have, resemble, lack, fit, suit, or marginal passives) T2 + T3 + T4 all PASS => DO.
- T5 PASS overrides everything: the verb is Vl and no object search runs.

## 4. Procedure (deterministic)

1. SEGMENT. Isolate the clause. Identify the lexical verb; strip auxiliaries and modals. Imperatives: S = "you" (implicit).
2. VOICE. If the clause is passive (be/get + past participle, agent optional), reconstruct the active: the passive subject becomes DO (or IO for recipient passives, "He was given a book"). Label on the active frame. A passive clause always yields Vt, Vd, or Vc, never Vi or Vl.
3. RECOVER DISPLACED OBJECTS. Wh-questions ("What did she eat?" -> DO = what), relative clauses ("the book she read __" -> DO gap), topicalization ("That I never said" -> DO = that). A recovered object counts as present.
4. LINKING CHECK. Run T5. PASS -> emit Vl, stop.
5. COLLECT post-verbal constituents. Discard adjuncts (section 2). For each PP, run T7: particle -> the following NP is a candidate object; preposition -> the NP is an oblique or adjunct, not a candidate.
6. COUNT candidate objects (bare NPs or clauses that pass T1, or T2+T3+T4 under the section 3 weights):
   - 0 -> Vi. Assign subtype (existential, weather, prepositional, particle, object-drop if the lemma is object-drop type, unaccusative if the lemma has a causative twin, else unergative).
   - 1 -> run T8. PASS -> Vc. FAIL -> Vt with subtype.
   - 2 -> run T6. PASS -> Vd. FAIL -> Vc (second NP is ObjComp).
7. EMIT the JSON in section 6, citing every test run with its result.

## 5. Traps (each must resolve as stated)

- 5.1 Adjunct read as object: "walked to school", "rested under the tree", "arrived yesterday", "went home", "ran three miles" -> Vi. Bare NPs of time, place, and measure are adjuncts.
- 5.2 Prepositional verbs: "rely on", "look at", "listen to", "wait for", "look after" -> Vi.prepositional + oblique. Pseudo-passives exist ("was looked after"); the label stays Vi, the oblique is recorded.
- 5.3 Particle verbs with objects: "look up the word", "turn off the light", "give up smoking" -> Vt.particle (T7). Without objects: "show up", "break down", "give up" -> Vi.particle.
- 5.4 Minimal pairs on the same string: "ran up the hill" Vi (preposition) vs "ran up the bill" Vt (particle). Only T7 separates them.
- 5.5 Same lemma, linking vs action: "felt tired" Vl / "felt the wall" Vt. "grew old" Vl / "grew tomatoes" Vt. "looked sad" Vl / "looked at him" Vi / "looked up the word" Vt. "tastes sweet" Vl / "tasted the soup" Vt. "turned red" Vl / "turned the page" Vt.
- 5.6 Causative-inchoative: "The glass broke" Vi.unaccusative / "He broke the glass" Vt. "The ship sank" Vi / "They sank the ship" Vt.
- 5.7 Object drop: "She ate" Vi.object-drop / "She ate lunch" Vt. "She dressed" Vi / "She dressed the child" Vt. "He walked to school" Vi / "He walked the dog" Vt.
- 5.8 Clausal objects vs adjunct clauses: "I think [that it works]" Vt.clausal. "She wants [to leave]" Vt.clausal. "He wondered [whether to go]" Vt.clausal. "She left [because it rained]" Vi (adjunct clause; "*Because it rained was left" fails T1).
- 5.9 Raising vs control: "He seems [to be tired]" Vl (raising; T5 trivially passes). "He tried [to leave]" Vt.clausal (control).
- 5.10 Perception and causative with bare infinitive or participle: "saw him leave", "made him cry", "let it go", "heard it ringing" -> Vc.
- 5.11 Reflexives: "She hurt herself" Vt.reflexive. "They met each other" Vt.reciprocal. "They met" Vi.
- 5.12 Measure and cognate: "weighs ten pounds", "lasted two hours", "cost five dollars", "measures six feet" -> Vi.measure (fails T1; policy fixed here, apply it consistently even where dictionaries list the lemma as transitive). "She weighed the box" -> Vt. "sang a song", "slept a deep sleep" -> Vt.cognate (passivizes: "a song was sung").
- 5.13 Expletives: "There is a problem" -> Vi.existential. "It rained" -> Vi.weather. "It is cold" -> Vl.
- 5.14 have / get: "She has a car" Vt.stative (no passive; T2+T3+T4 pass). "She got tired" Vl. "She got a letter" Vt. "She got him to leave" Vc. "She got fired" -> passive of "fire": Vt.
- 5.15 Passives: "The hymn was sung by the choir" -> Vt. "He was given a book" -> Vd. "He was elected president" -> Vc.
- 5.16 Light verbs: "take a walk", "have a look", "make a decision" -> Vt.light-verb. The noun is the DO; the event meaning lives in the noun.
- 5.17 Ditransitive with one object dropped: "She told him the truth" Vd. "She told him" Vt (him passes T1: "He was told"). "She gave generously" Vi.object-drop.
- 5.18 Two NPs that are not IO + DO: "named the dog Rex", "consider him a friend", "called it a day" -> Vc (T6 fails).

## 6. Output schema (JSON, one object per clause)

{
  "clause": "string",
  "verb_lemma": "string",
  "verb_form": "string",
  "voice": "active | passive",
  "label": "Vl | Vi | Vt | Vd | Vc",
  "subtype": "string | null",
  "ambitransitive_lemma": "object-drop | causative-inchoative | null",
  "subject": "string",
  "direct_object": "string | null",
  "indirect_object": "string | null",
  "complement": "string | null",
  "obliques": ["string"],
  "adjuncts": ["string"],
  "tests": ["T1:PASS", "T5:FAIL"],
  "confidence": 0.0
}

Confidence: 1.0 when T1 or T5 passes cleanly. 0.8 when the label rests on T2+T3+T4 without T1. 0.6 for section 5.12 measure/cognate and 5.14 stative cases. Below 0.6, return the label and set "review": true.

## 7. Ground truth (sentence -> label; decisive evidence)

| Sentence | Label | Evidence |
|---|---|---|
| The choir sang beautifully. | Vi.unergative | "beautifully" is an adverb; no candidate NP |
| The choir sang a hymn. | Vt | T1: "A hymn was sung" |
| The travelers rested under the tree. | Vi.unergative | "under the tree" is a PP adjunct; T7 not applicable (rest is not phrasal) |
| She gave her brother the keys. | Vd.recipient | T6: "gave the keys to her brother" |
| They elected her captain. | Vc.nominal | T8: "she is captain"; T6 fails |
| The soup tastes sweet. | Vl | T5: "The soup is sweet" |
| She tasted the soup. | Vt | T1: "The soup was tasted" |
| The glass broke. | Vi.unaccusative | no candidate NP; lemma has a causative twin |
| He broke the glass. | Vt | T1 |
| She ate. | Vi.object-drop | no candidate NP; lemma is object-drop type |
| He looked up the word. | Vt.particle | T7: "looked it up" |
| He ran up the hill. | Vi.prepositional | T7: "*ran it up" |
| He ran up the bill. | Vt.particle | T7: "ran it up" |
| She relies on her sister. | Vi.prepositional | oblique = "her sister"; T3 fails |
| The box weighs ten pounds. | Vi.measure | T1 fails; measure phrase policy |
| She weighed the box. | Vt | T1 |
| I know that she left. | Vt.clausal | T4: "I know it" |
| She left because it rained. | Vi | adjunct clause; T1 and T4 fail |
| He seems to be tired. | Vl | T5 |
| We saw him leave. | Vc.bare-infinitive | T8: "he leaves/left" predicated of him |
| The hymn was sung by the choir. | Vt | passive; active reconstruction |
| He was given a book. | Vd.recipient | recipient passive |
| There is a problem. | Vi.existential | expletive subject |
| What did she eat? | Vt | recovered DO = what |
| The book that she read was long. | Vt (embedded clause: read) | DO gap in the relative clause |
| Close the door. | Vt | imperative, S = you; T1: "The door was closed" |
| She hurt herself. | Vt.reflexive | T4 with reflexive; "herself" is DO |
| They met. | Vi | no candidate NP |
| She has a car. | Vt.stative | T2, T3, T4 pass; T1 inapplicable |
| It rained all night. | Vi.weather | "all night" is a duration adjunct |
| Take a walk. | Vt.light-verb | "a walk" is DO |
| She got him to leave. | Vc.bare-infinitive-like (to-infinitive) | T8: "he leaves" predicated of him |

END OF KNOWLEDGE BASE.
