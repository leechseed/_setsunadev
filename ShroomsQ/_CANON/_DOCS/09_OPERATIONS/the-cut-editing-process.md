---
type: process_doc
bolo: 136
version: 0.1.0
date: 2026-10-12
status: DRAFT (for Chief's ruling)
trunk: ORANGE / BLACK
---

# THE CUT: the editing process

## 1. Purpose

This document gives Chief one repeatable process from idea to delivered file. Every edit runs the same eleven stations, in the same order. Nothing gets reinvented, so each job starts faster than the last.

Terms used throughout:
- **Timeline** is the strip where clips are arranged in order.
- **Select** is a take chosen for use.
- **Proxy** is a small, light copy of a clip that plays smoothly while editing.
- **LUFS** is a loudness unit for finished audio.
- **PowerGrade** is a saved color look in Resolve that works in any project.
- **AAR** is the after-action review, a short look back at the job.

## 2. The stations

Time budgets assume one 60-second finished clip. They are targets; Chief adjusts after five jobs.

### Station 0: Concept
- **Goal:** Chief states the idea in one line before touching any footage.
- **Steps:**
  1. Write the idea in one sentence.
  2. Name the audience: who watches, and where.
  3. Set the length in seconds.
  4. If the edit is music-led, name the track.
- **Resolve page:** none. Use a notes file.
- **Deliverable:** one line in the job note: idea, audience, length, track.
- **Time budget:** 5 minutes.
- **Costliest mistake:** starting to cut with no stated idea. The edit then drifts and gets redone.

### Station 1: Brief
- **Goal:** Chief and the client agree on what gets delivered, in writing.
- **Steps:**
  1. Fill in the one-page brief: deliverables, aspect ratios, duration, reference edits, due date.
  2. For client work, get the client's written confirmation that everyone shown is 18 or older.
  3. Get the records confirmation and the payment terms in writing.
  4. Take the deposit or full payment before station 2 starts.
  5. Save the brief in the job folder.
- **Resolve page:** none.
- **Deliverable:** a signed-off brief, confirmations on file, payment received.
- **Time budget:** 10 minutes, plus waiting on the client.
- **Costliest mistake:** starting work before the confirmations and payment arrive. Chief then carries the risk.

### Station 2: Ingest
- **Goal:** all footage sits in one named, backed-up place, ready to edit.
- **Steps:**
  1. Make the job folder from the template (see section 5).
  2. Copy iPhone files and client files into the `01_RAW` subfolder. Never edit the originals.
  3. Rename each file with the job code, date and a number.
  4. Strip metadata with ffmpeg from any file that will leave Chief's hands. Check the exact command in the ffmpeg docs.
  5. Copy the raw folder to a second drive. Two copies before the first cut.
  6. Create the Resolve project from the template and import the footage.
  7. Generate proxies if the footage is heavy. Check in Resolve for the proxy setting.
- **Resolve page:** Media.
- **Deliverable:** a project with all clips imported, a backup made, proxies built.
- **Time budget:** 10 minutes.
- **Costliest mistake:** skipping the backup, or editing the only copy.

### Station 3: Selects
- **Goal:** Chief knows which takes are good and where they are.
- **Steps:**
  1. Watch every clip once, with no cutting.
  2. Mark the in and out points of each good moment.
  3. Color-tag or rate selects so they filter fast. Check in Resolve for the flag and rating keys.
  4. Pull the selects into a "Selects" bin, or a selects timeline.
  5. Throw away nothing yet. Just do not mark it.
- **Resolve page:** Cut or Edit. The Cut page is quick for scrubbing.
- **Deliverable:** a Selects bin holding only marked moments.
- **Time budget:** 10 minutes.
- **Costliest mistake:** dragging whole clips to the timeline instead of marked selects. The timeline then fills with dead air.

### Station 4: Assembly
- **Goal:** a rough skeleton of the whole piece sits on the timeline.
- **Steps:**
  1. Create the timeline at the final aspect ratio and frame rate.
  2. Lay down the structure: opening, middle, ending.
  3. For music-led edits, drop the track first and place markers at its sections.
  4. Place selects in order. Do not trim finely yet.
  5. Play through once at full length.
- **Resolve page:** Edit (the Cut page also works).
- **Deliverable:** a full-length timeline in correct order, even if rough.
- **Time budget:** 10 minutes.
- **Costliest mistake:** polishing the first ten seconds before the whole piece exists.

### Station 5: Rough cut
- **Goal:** the story works; every shot earns its place.
- **Steps:**
  1. Ask of each shot: what does the viewer learn or feel here?
  2. Cut every shot that answers nothing.
  3. Trim each clip to its useful part.
  4. Fix the order. Move shots until the flow reads.
  5. Hit the target length, plus or minus two seconds.
- **Resolve page:** Edit.
- **Deliverable:** a timeline at target length with no dead shots.
- **Time budget:** 10 minutes.
- **Costliest mistake:** keeping a weak shot because it looks good. If it does no work, cut it.

### Station 6: Fine cut
- **Goal:** rhythm and cut points feel right.
- **Steps:**
  1. Tune each cut point. Use trim mode to nudge both sides of a cut at once.
  2. Match action across cuts: a motion that starts in one shot finishes in the next.
  3. Set the pace. Short shots build energy; long shots let the viewer rest.
  4. Cut to the beat if music-led (see section 3).
  5. Place captions, and check them against safe areas (see section 4).
  6. Add transitions only where a plain cut fails.
- **Resolve page:** Edit. Use Fusion only for effects that need it.
- **Deliverable:** a picture-locked timeline. Chief declares "locked" and stops touching the cuts.
- **Time budget:** 15 minutes.
- **Costliest mistake:** changing cuts after color and sound start. Every change then redoes work.

### Station 7: Color
- **Goal:** one consistent look across the whole timeline.
- **Steps:**
  1. Match exposure and white balance clip to clip first.
  2. Check the scopes (waveform, vectorscope), not just the eye. Check in Resolve for the Scopes menu.
  3. Apply one look to every clip. Pick a client's saved PowerGrade if one exists.
  4. Compare the first and last clips side by side.
  5. Save the final look as a PowerGrade named for the client.
- **Resolve page:** Color.
- **Deliverable:** a graded timeline and a saved PowerGrade or LUT.
- **Time budget:** 8 minutes.
- **Costliest mistake:** grading before the picture locks. Shots get cut and the grade is wasted.

### Station 8: Sound
- **Goal:** the mix is clear, even and loud enough for the platform.
- **Steps:**
  1. Set clip levels so dialogue or key sound sits near the same level throughout.
  2. Duck the music under any voice. Check in Resolve for the ducking tools.
  3. Place hits and effects on the beat or the cut.
  4. Add short fades at every edit and at the ends.
  5. Measure loudness and set the target for the platform (see section 8, call 4).
  6. Listen on phone speakers and on headphones.
- **Resolve page:** Fairlight.
- **Deliverable:** a mixed timeline at the target loudness with no clipping.
- **Time budget:** 8 minutes.
- **Costliest mistake:** judging the mix on studio headphones only. Most viewers use phone speakers.

### Station 9: Deliver
- **Goal:** the right file, in the right size, named correctly, checked.
- **Steps:**
  1. Do one full playback pass of the timeline. Fix anything wrong first.
  2. Pick the export preset for this aspect ratio and platform.
  3. Name the file: `JOBCODE_title_ratio_v01.mp4`.
  4. Export.
  5. Make a checksum of the file (a short fingerprint) and write it in the job note.
  6. Re-watch the first and last 10 seconds of the exported file, not the timeline.
  7. Send the file to the client and log the delivery date.
- **Resolve page:** Deliver.
- **Deliverable:** the exported file, its checksum, and a delivery log line.
- **Time budget:** 8 minutes, mostly export time.
- **Costliest mistake:** exporting without a playback pass. A single flash frame forces a full re-export.

### Station 10: Review and AAR
- **Goal:** Chief learns from the job and saves what he built.
- **Steps:**
  1. Note which station took longest.
  2. Write one thing to change next time.
  3. Save the reusable asset: preset, LUT, PowerGrade or title template.
  4. Archive the project and move the job folder to the finished area.
- **Resolve page:** Project Manager, then Media.
- **Deliverable:** a three-line AAR in the job note and one saved asset.
- **Time budget:** 5 minutes.
- **Costliest mistake:** skipping the AAR. The same slow step then repeats every job.

**Total for a 60-second clip: about 100 minutes**, not counting client waits or export time.

## 3. The music-led variant (PMV-style montages)

A montage cut to a track needs the track's structure before any footage.

1. **Map the track first.** Play it once. Mark intro, builds, drops and outro with timecodes in a note.
2. **Set markers.** Place a Resolve marker at each section. Press M while the track plays. Check in Resolve for marker colors.
3. **Find the beat grid.** Check in Resolve for any beat-detect tool. If none exists, tap a marker on every beat in one pass. Then zoom in and nudge the markers that drift.
4. **Cut on the grid.** Snap each cut to a beat marker. Check in Resolve for the snapping key.
5. **One idea per phrase.** A musical phrase is a short run of bars, often four or eight beats. Give each phrase one idea, one location or one motion.
6. **Land the hit on the downbeat.** The downbeat is the first beat of a bar. Put the strongest shot or effect there.
7. **Build with speed.** Cut faster in a build. Let a drop breathe with a longer shot, or hit it with a flash.
8. **Audition cuts fast.** Loop the playback over one phrase. Play it, adjust one cut, play it again. Never judge a cut from a single pass.

## 4. The vertical variant (9:16)

1. **Create the timeline at 9:16.** Start at 1080 by 1920 pixels. Check in Resolve for timeline resolution settings.
2. **Reframe wide footage.** Try Smart Reframe, an automatic tool. Check in Resolve whether the free version has it.
3. **Reframe by hand if needed.** Set keyframes on Position and Zoom, one at the start and one at the end of the move.
4. **Keep the subject in the center third.** The platform interface covers the edges.
5. **Respect safe areas.** Keep captions out of the top 10 percent and the bottom 20 percent of the frame. The interface sits there. Check each platform's current guide.
6. **Style captions to survive compression.** Use a bold sans-serif font, white fill, a dark outline or shadow, and large size. Avoid thin fonts and pale colors.
7. **Keep caption lines short.** Use two lines at most, and break at natural phrases.
8. **Test on a phone.** Export a preview and watch it on the real device before delivering.

## 5. The reusable kit

Every job saves the following. Each item is named so the next job starts at station 2.

| Item | Where it lives | Name pattern |
|---|---|---|
| Brief template | `_KIT/01_briefs/` | `brief_template_v01.md` |
| Job folder template | `_KIT/02_folders/` | `JOB_folder_template/` |
| Resolve project template | `_KIT/03_projects/` | `proj_template_9x16.drp`, `proj_template_16x9.drp` |
| Export presets | `_KIT/04_presets/` | `exp_9x16_social.xml`, `exp_16x9_master.xml` |
| PowerGrades and LUTs | `_KIT/05_color/` | `pg_clientname_v01`, `lut_looknamed_v01.cube` |
| Title and caption templates | `_KIT/06_titles/` | `title_clientname_v01` |
| Beat-marker checklist | `_KIT/07_music/` | `track_map_template.md` |
| AAR log | `_KIT/08_aar/` | `aar_log.md`, one line per job |

Chief keeps the whole `_KIT` folder backed up with the job archives.

## 6. Efficiency rules

1. **Use the keyboard first.** Learn the keys for play, mark in, mark out, split, ripple delete and marker.
2. **Use trim mode.** It edits both sides of a cut without dragging.
3. **Use proxies for heavy footage.** Proxies keep playback smooth.
4. **Never grade before the picture locks.** Color comes after fine cut.
5. **Rough first, fine later.** Never polish a shot that might be cut.
6. **Do one playback pass before any export.** It catches errors that a re-export would cost.
7. **Name everything on ingest.** A clear name saves a search later.
8. **Work from the timeline template.** Never start from a blank project.
9. **Save an asset after every job.** A preset or a PowerGrade is worth five minutes.
10. **Stop at "locked."** After lock, change only fixes, not ideas.

## 7. The shelf

Ten references the process leans on. Chief reads them in the order the stations need them.

| Book | Author | Year | Station | What it gives the process |
|---|---|---|---|---|
| In the Blink of an Eye | Walter Murch | 2001, 2nd ed. | 5, 6 | A short rule set for judging when and why to cut. |
| The Technique of Film and Video Editing | Ken Dancyger | 6th ed., 2018 | 4, 5, 6 | The history and theory behind story structure and pacing. |
| Grammar of the Edit | Christopher J. Bowen | 4th ed., 2017 | 6 | Plain rules for cut types, continuity and screen direction. |
| Cutting Rhythms: Intuitive Film Editing | Karen Pearlman | 2nd ed., 2015 | 6, music-led variant | How to feel and shape rhythm in a cut. |
| The Eye Is Quicker | Richard D. Pepperman | 2004 | 5, 6 | Worked examples of cutting choices, shot by shot. |
| On Film Editing | Edward Dmytryk | 1984 | 3, 5 | A working editor's method for selects and story flow. |
| The Conversations: Walter Murch and the Art of Editing Film | Michael Ondaatje | 2002 | 0, 5 | Murch on process and mindset, in interview form. |
| The Visual Story | Bruce Block | 3rd ed., 2020 | 6, 7 | Contrast, space and color as tools for guiding the eye. |
| Color Correction Handbook | Alexis Van Hurkman | 2nd ed., 2013 | 7 | Scopes, grading steps and look-building, in depth. |
| The Beginner's Guide to DaVinci Resolve 19 | Blackmagic Design | 2024 | All Resolve pages | Where each tool lives. **Free official PDF from Blackmagic's site.** |

## 8. Calls for Chief

1. **Folder root.** Rec: `Q:\EDITS\` with one subfolder per job code. Tip: a short fixed root keeps paths short and backups simple.
2. **Default aspect ratios.** Rec: 9:16 as the default, with 16:9 as the second master on request. Tip: vertical is where short clips are posted.
3. **Proxies for iPhone footage.** Rec: proxies on for any clip over 1080p or 60 fps. Tip: iPhone files are heavy to decode, and proxies keep playback smooth on most machines.
4. **Loudness target.** Rec: about -14 LUFS integrated with peaks under -1 dB. Tip: check each platform's current spec before delivery, because these numbers change.
5. **Client intake.** Rec: no work starts until the 18+ confirmation, the records confirmation and payment are on file. Tip: put these three lines at the top of the brief template so they cannot be missed.

## 9. Version history

- 0.1.0, 2026-10-12: draft.
