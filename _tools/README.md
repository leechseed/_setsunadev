# _tools

Scripts the Command runs. Each folder has its own entry script; the SOP and the skills name which one to call.

## New scripts: write the failing check first

When a new prep script is written, write its check first and watch it fail for the right reason. The check can be small: a few lines that run the script on a tiny sample input and compare the output to a file or a count you wrote by hand. Run it before the script exists; it must fail because the output is missing, not because the check is broken. Then write the least code that makes it pass, run it again, and keep the check next to the script. If a check passes on the first run, it tests nothing; fix the check. This is a habit for new prep scripts, not a rule for old ones, and it does not replace RANGE, which still reviews outputs at the fan-in.

<!-- adapted from obra/superpowers test-driven-development (MIT); ideas only, the iron-law and delete-the-code rules not taken · BOLO 140 · 2026-10-13 -->
