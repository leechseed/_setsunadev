---
title: "Spawning scout weapon in CS2"
uuid: cd8a7008-e581-46ba-bb7b-85b39f4c11e2
created: 2026-05-28
updated: 2026-05-28
trunk: OTHER
messages: 2
chars: 1219
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# Spawning scout weapon in CS2

> **Conversation Overview**

The person asked how to spawn the Scout sniper rifle (SSG 08) in Counter-Strike 2. Claude explained that weapon spawning requires a private or local server environment with cheats enabled, as it is not available in official matchmaking. Claude provided the relevant console commands: enabling cheats with `sv_cheats 1`, then spawning the weapon using `give weapon_ssg08`. Claude also suggested pairing this with `sv_infinite_ammo 1` for practice purposes and noted that `sv_cheats 1` only functions when the person is hosting or on a local/offline server. Claude offered to provide a full practice server configuration if needed, but the conversation ended there.

---
## 🧑 Papi  <sub>2026-05-28 02:40:21</sub>

spawn scout weapon on cs2

---

## 🤖 Claude  <sub>2026-05-28 02:40:28</sub>

Counter-Strike 2 doesn't have a "spawn weapon" command that works in normal matchmaking or competitive play. But if you're in a private server, a practice config, or a workshop map with cheats enabled, you can give yourself the Scout (the SSG 08) easily.

Here's how:

First, enable cheats. Open the console (the `~` key, which you may need to turn on in Settings → Game) and type:

```
sv_cheats 1
```

Then give yourself the Scout with:

```
give weapon_ssg08
```

The SSG 08 is the official name for the gun players call the "Scout." Note that `sv_cheats 1` only works if you're the host of the server or on a local/offline server — you can't run it in official matchmaking.

If you want a full practice setup, a couple of other handy commands once cheats are on:

```
sv_infinite_ammo 1
give weapon_ssg08
```

That gives you unlimited ammo so you can grind your no-scopes or flick shots without reloading constantly.

If you're trying to set up a dedicated practice server with bots, sliding spawn positions, and saved configs, let me know and I can walk you through a full practice config file.