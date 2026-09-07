# modmigrate

Port a Modrinth mod list to another loader / Minecraft version using only the public
Modrinth API (no key, works with any launcher — drop the jars into the instance folder).

## Files

- `modmigrate.py` — the tool
- `slugs.txt` — the project list, one `<type> <slug>` per line (`mod` / `resourcepack` / `shader`)
- `matrix.md` — last coverage table output

## Usage

```
python modmigrate.py matrix
```
Pulls every project's full version list (cached under `%LOCALAPPDATA%\Temp\modmigrate-cache`)
and prints ✅/❌ per candidate target. Edit `TARGETS` at the top of the script to change the columns.
Add `--refresh` to re-pull.

```
python modmigrate.py download --loader neoforge --mc 1.21.11 --out "C:\path\to\instance" [--dry]
```
Picks the newest build per project for that loader + version, resolves required dependencies
(Kotlin for Forge etc.), skips Fabric plumbing (Fabric API, FLK, Mod Menu) when the target is not
Fabric, downloads into `<out>\mods|resourcepacks|shaderpacks`, sha512-checks every file, and
writes `modmigrate-<loader>-<mc>.json` as a manifest. Re-running is idempotent. `--dry` resolves
and reports without downloading.

Version choice: newest by publish date; if the newest is a beta/alpha and a full release for the
same target exists within 30 days of it, the release wins.

## 2026-09-07 run

Source: Modrinth App profile "Fabric 1.21.11" (113 projects).
Coverage: Forge 1.21.11 = 34, **NeoForge 1.21.11 = 83**, NeoForge 26.1.2 = 77, NeoForge 26.2 = 69.
Target chosen: NeoForge 1.21.11. Staging folder: `Desktop\MC-NeoForge-1.21.11-staging`.
