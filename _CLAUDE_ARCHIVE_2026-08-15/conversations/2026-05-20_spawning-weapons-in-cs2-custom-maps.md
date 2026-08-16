---
title: "Spawning weapons in CS2 custom maps"
uuid: 6e36ba5c-4ea3-4e4e-bf56-d574edc0a42e
created: 2026-05-20
updated: 2026-05-20
trunk: BLACK
messages: 2
chars: 2590
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# Spawning weapons in CS2 custom maps

> **Conversation Overview**

The person asked for help with CS2 (Counter-Strike 2) console commands to spawn weapons on a custom map. This was a straightforward technical gaming question focused on map testing and development workflows. Claude provided a comprehensive response covering the prerequisite steps (enabling the developer console and activating `sv_cheats 1`), the `give weapon_<name>` command syntax, and an extensive list of weapon identifiers spanning rifles, pistols, snipers, SMGs, shotguns, grenades, and equipment like armor and defuse kits. Claude also included useful companion commands for map testing such as `mp_buy_anywhere`, `mp_buytime`, money-related variables, `noclip`, and `bot_kick`, and provided a ready-to-paste multi-command string for quickly configuring a clean testing session. A troubleshooting note was included about verifying `sv_cheats` status if the `give` command produces no output.

---
## 🧑 Papi  <sub>2026-05-20 00:17:10</sub>

how do i spawn in weapons in cs2 in a custom map using the console code

---

## 🤖 Claude  <sub>2026-05-20 00:17:32</sub>

The user is asking about CS2 console commands for spawning weapons in custom maps, which is a straightforward gaming question about built-in cheats functionality. I'm recalling that the give commands in CS2 have remained fairly consistent, so I should be able to provide accurate syntax for this.

I know the core setup involves enabling cheats with `sv_cheats 1`, then using `give weapon_<name>` format for weapons, grenades, and equipment like armor. I'm also thinking through some useful companion commands for testing maps like disabling freeze time and adjusting buy settings. Since the user has map design experience, I can answer this directly without needing to verify the current syntax.To spawn weapons in CS2 on a custom map, you need cheats enabled first. Here's the workflow:

**Enable the console and cheats:**
1. Settings → Game → Enable Developer Console (Yes), then bind a key (default `~`)
2. In your custom/offline map, open console and run: `sv_cheats 1`

**Give weapon syntax:** `give weapon_<name>`

Common weapons:
- `give weapon_ak47`
- `give weapon_m4a1` (M4A4) / `give weapon_m4a1_silencer` (M4A1-S)
- `give weapon_awp`
- `give weapon_deagle`
- `give weapon_glock` / `give weapon_usp_silencer` / `give weapon_hkp2000`
- `give weapon_ssg08` (scout) / `give weapon_scar20` / `give weapon_g3sg1`
- `give weapon_p90` / `give weapon_mp9` / `give weapon_mac10`
- `give weapon_nova` / `give weapon_xm1014` / `give weapon_negev`

Grenades:
- `give weapon_hegrenade`
- `give weapon_flashbang`
- `give weapon_smokegrenade`
- `give weapon_molotov` (T) / `give weapon_incgrenade` (CT)
- `give weapon_decoy`

Other useful stuff:
- `give item_assaultsuit` — kevlar + helmet
- `give item_defuser`
- `impulse 101` — max money
- `mp_warmup_end` — skip warmup
- `mp_buy_anywhere 1` — buy anywhere on the map
- `mp_buytime 9999` — extend buy time
- `mp_maxmoney 65535` + `mp_startmoney 65535` — set high money
- `bot_kick` — clear bots if it's a comp map
- `noclip` — fly through walls (handy for map testing)

**Quick all-in-one warmup setup** (paste into console for a clean testing session):
```
sv_cheats 1; mp_warmup_end; mp_freezetime 0; mp_buy_anywhere 1; mp_buytime 9999; mp_maxmoney 65535; mp_startmoney 65535; mp_restartgame 1
```

If `give` returns nothing, double-check `sv_cheats` is actually 1 — most custom workshop maps will let you flip it, but some competitive map setups override it on round start.