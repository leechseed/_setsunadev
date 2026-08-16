#!/usr/bin/env bash
# Session autosave. Wired as a Stop hook — runs when Claude Code finishes a turn,
# on /clear, on resume, and on compact.
#
# Commits locally. Does NOT push: this repo is public, and publishing should stay
# a deliberate act. Local commits protect against overwrites and bad edits;
# `git push` is yours to run when you mean it.
#
# Always exits 0 so a git problem can never block the session.

REPO="c:/Users/U01_LEECHSEED/Desktop/_setsunadev"
cd "$REPO" 2>/dev/null || exit 0

git rev-parse --git-dir >/dev/null 2>&1 || exit 0

DIRTY="$(git status --porcelain 2>/dev/null)"
[ -z "$DIRTY" ] && exit 0

N="$(printf '%s\n' "$DIRTY" | grep -c '^')"

git add -A >/dev/null 2>&1 || exit 0
git commit -q -m "autosave $(date '+%Y-%m-%d %H:%M') · ${N} file(s)" >/dev/null 2>&1 || exit 0

SHA="$(git rev-parse --short HEAD 2>/dev/null)"
AHEAD="$(git rev-list --count @{u}..HEAD 2>/dev/null || echo '?')"

printf '{"systemMessage":"⌁ autosaved %s file(s) → %s · %s commit(s) unpushed"}\n' \
  "$N" "$SHA" "$AHEAD"
exit 0
