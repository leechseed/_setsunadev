---
title: "The tracking system: tutorial"
type: tutorial
for: "A writer new to the tracking system who learns by recording one setup and its payoff"
does: "Teaches the time code, story points, cables and the reader ledger with the source's own example"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/08_TRACKING_SYSTEMS/📐 ssot_08_tracking_system.md
source_version: 1.2.0
---

**Who it's for:** a writer new to tracking · **What it does:** walks one setup and payoff through the records · **Type:** tutorial

# The tracking system: tutorial

You will record a setup in Movement 1 and its payoff in Movement 3. The source's own example addresses supply the time codes. Keep the [reference](2-reference.md) open.

## Step 1: address the setup

1. Pick the setup scene: Movement 1, Sequence 1, Scene 2.
2. Write the movement, sequence and scene: `M1 · Q1 · S02`.
3. Add ` | `, then bar 4, beat 1, tick 1 as `004.1.1`.
4. Your code reads:

```
M1 · Q1 · S02 | 004.1.1
```

5. Check: the scene number has 2 digits, and the bar has 3.

## Step 2: address the payoff

1. Pick the payoff scene: Movement 3, Sequence 2, Scene 9.
2. Write bar 41, beat 2, tick 3.
3. Your code reads:

```
M3 · Q2 · S09 | 041.2.3
```

4. Sort the two codes. The movement differs, so `M1` comes before `M3`.

## Step 3: log a story point

1. At the setup, a trait ticks up on a character. Name the point with a slug.
2. Set `subject.kind` to `trait` and give the subject id.
3. Write the `field` and the new `value`.
4. Set `at` to the setup's time code.
5. Leave `ramp` false. The value holds until the next point.

## Step 4: lay the cable

1. Write a `cable_id` and `type: setup_payoff`.
2. Under `setup`, set the track and `at: "M1 · Q1 · S02 | 004.1.1"`. A track id looks like `character:victoria_midnight` or `trope:t114`.
3. Under `payoff`, set the track and `at: "M3 · Q2 · S09 | 041.2.3"`.
4. Set `edge: enable` and `orphan: none`.
5. Check: both ends exist, so the cable is no orphan.
6. Try the other case. Delete the payoff time code and set `orphan: provisional`. The cable is not an orphan, but a time code is now owed.

## Step 5: log what the reader believes

1. Add a reader entry at the setup scene. Set `belief` to what the reader believes now.
2. Set `trust` high, for example 8, and `disclosure: concealed`.
3. Set `shifted_at` to the setup's time code.
4. At the payoff scene, write a second entry. Set `disclosure: revealed` and drop `trust`.
5. Notice the gap between the first entry and the character's real state. That gap is dramatic irony.

## Step 6: zoom out

1. Zoom from R2 SCENE to R4 MOVEMENT.
2. Watch the story points and cables bundle into count badges.
3. Zoom back in. They fan out to the exact tick.

You now hold the core loop: address, record, cable, reader ledger. Next, use the [how-to](3-how-to.md) to add tempo and proportion lanes.
