---
title: "💬 best desktop companion app. i'…"
uuid: 48f983e6-cb00-46e6-843a-90b4079664a4
created: 2026-08-08
updated: 2026-08-08
trunk: BLACK
messages: 10
chars: 4545
artifacts: 0
generated_files: 0
tools: [ask_user_input_v0, web_search]
source: claude.ai-export-2026-08-15
---

# 💬 best desktop companion app. i'…

> **Conversation Overview**

The person is building out a desktop companion app setup and already has an established adult content library workflow in place, including Stash for library management. The conversation focused on identifying the best desktop companion application given their interest in both a visual desktop mascot and an AI chat companion simultaneously.

Claude walked through several options including Desktop Mate (with mod support via MelonLoader and custom VRM models), VPet-Simulator, and SillyTavern before narrowing the recommendation based on the person's stated needs. The person confirmed they already use Stash, which resolved the library management question and kept the focus on the companion layer specifically.

For the "both" use case — visual mascot plus AI chat — Claude recommended Project AIRI as the primary option due to its VRM support, real-time voice chat, local inference compatibility, and screen awareness, with a note to use the GitHub desktop build rather than the Steam version to allow custom API backends. Open-LLM-VTuber was presented as the desktop-pet specialist alternative, supporting transparent background, always-on-top display, click-through, and drag interaction, but limited to Live2D models only. Claude noted that uncensored behavior depends entirely on the model backend (e.g., Ollama with an abliterated finetune) rather than the companion app itself. The conversation ended with the person asking for clarification on the term "VRM," which Claude explained as an open 3D avatar file format built on glTF, noting that VRoid Studio enables character creation without modeling expertise and that custom VRM characters could be imported directly into AIRI.

---
## 🧑 Papi  <sub>2026-08-08 04:28:23</sub>

best desktop companion app. i'm a gooner go with that

---

## 🤖 Claude  <sub>2026-08-08 04:29:31</sub>

Depends what flavor of "companion" you mean — here are the top picks per lane:

- **Desktop Mate + mods** — the polished desktop mascot on Steam. Vanilla is SFW, but the modding scene (MelonLoader + custom VRM/MMD models) is where gooners take it. Best animation and interaction quality in the genre.
- **VPet-Simulator** — open-source alternative with Steam Workshop support. Jankier, but way more permissive about NSFW mods without third-party loaders.
- **SillyTavern** — if "companion" means one you talk to. Self-hosted frontend, character cards, hooks into whatever model backend you want, plus TTS and image-gen extensions. The standard in that scene.

And honestly, given GOON+PASTE is already feeding you a download queue — **Stash** might be the real answer. Self-hosted library manager built specifically for adult content: auto-scrapes metadata, tags performers, fingerprints scenes, makes the whole archive searchable. It'd bolt right onto your ytdlp pipeline as the storage/organization layer.

If you tell me which lane you're actually in, I can go deeper on setup.

---

## 🧑 Papi  <sub>2026-08-08 04:31:55</sub>

goon paste? yah i actually already use stash for my library

---

## 🤖 Claude  <sub>2026-08-08 04:32:19</sub>

GOON+PASTE is your clipboard watcher — the ytdlp_go.py script that auto-queues links you copy. That plus Stash means your capture-and-library stack is already handled, so "companion" is the only open slot left.

That narrows it to two real options: Desktop Mate modded with custom VRM models (visual mascot living on your screen — and VRM means you could eventually run your own LEECHSEED character designs), or SillyTavern (conversational, character cards, TTS, hooks into local or API models).
```
This block is not supported on your current device yet.
```

---

## 🧑 Papi  <sub>2026-08-08 04:33:15</sub>

Q: Which lane are you after?
A: Both, honestly

---

## 🤖 Claude  <sub>2026-08-08 04:34:12</sub>

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The "both" answer is two open-source projects that bolted a brain onto a body, and which one wins depends on which half matters more to you:

- **Project AIRI** — the most popular open-source AI companion project as of mid-2026 (40k+ GitHub stars), with VRM and Live2D avatars, real-time voice chat, and local inference. The companion can see your screen, and you can import your own VRM model and configure personality and voice. One catch: the Steam version requires their cloud account and doesn't permit third-party API keys — so skip Steam and grab the desktop build from GitHub, where you can point it at whatever backend you want.
- **Open-LLM-VTuber** — the desktop-pet specialist. Transparent background, always-on-top, mouse click-through, drag the character anywhere on screen, plus touch feedback when you click or drag the avatar, and screen/camera vision. Fully offline with Ollama for the brain. Live2D only — no VRM.

The part that actually matters for your use case: neither is uncensored by itself — the model behind it is. Run Ollama with an uncensored/abliterated finetune as the backend and either one will go wherever you steer it. Cloud APIs will refuse.

My pick for you specifically: **AIRI**, because VRM support means the companion can eventually *be* a LEECHSEED character — your own TCVM archetype as the model, which makes your desktop gooner setup double as a live prototype for a BVX product line. Want the Ollama + uncensored model setup steps to go with it?

---

## 🧑 Papi  <sub>2026-08-08 04:40:03</sub>

what do you mean by arm

---

## 🧑 Papi  <sub>2026-08-08 04:40:07</sub>

vrm

---

## 🤖 Claude  <sub>2026-08-08 04:40:17</sub>

VRM is a file format — an open standard for 3D humanoid avatars, built on glTF. One .vrm file packs the model, rig, facial expressions, hair/clothing physics, and even licensing metadata, so the same character works in any app that supports the standard: AIRI, VRChat-style platforms, VTuber software, all of it.

The reason it's the key detail here: you can make one free in VRoid Studio (anime-style character creator, no modeling skills needed) or build fully custom in Blender with the VRM add-on. So the pipeline is: design a LEECHSEED character → export as .vrm → drop it into AIRI → that's now the thing living on your desktop talking to you.