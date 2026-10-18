---
name: verifying-before-done
description: Use before telling Chief a build is done, and when Chief says "done check", "verify it" or "is it clean". Runs the zero-token done check over what changed.
---

# The done check (BOLO 155 move 3)

Borrowed from superpowers' verification-before-completion, adapted to the Command's doctrine: the check is a **script** (RANGE's kind), never a checker agent.

## Run it

```
python _tools/done/verify.py
```

It checks every file changed since the last commit: Python compiles, JSON parses, agent and skill frontmatter is whole, skill descriptions stay at 500 characters or fewer and keep every quoted trigger, and no BOLO number sits on two rows. `--all` checks every file it knows.

## Then

- **PASS:** say the build is done, with the line `DONE CHECK · N file(s) · PASS` in the reply.
- **FAIL:** fix each finding once, rerun once. What still fails goes in the reply's caveat line. Never loop.
- A FAIL is never hidden: the reply names it even when the rest of the build landed.
