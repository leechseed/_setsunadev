# Plan template

Use for any plan the planner writes. Skip commit steps and test-first steps (our scripts have no suite); every step carries a command we can run.

## Global Constraints
What holds for every task: stdlib only, forward-slash Windows paths, UTF-8, no scanning the box, private detail stays in `_PRIVATE/`, write only the files named. List the ones that apply.

## Phase N: <name>
Goal in one sentence. Then per task:

### Task N.M: <name>
- **File:** exact path
- **Action / Why / Depends on / Risk (low, medium, high)**
- **Interfaces:** every name another task or specialist must match: function signatures, JSON keys, file paths, CLI flags, column names. Write each once, here, so two specialists never name the same thing differently.
- **Verify:** the command and its expected output

## Proportion check (last, before handing back)
A plan longer than the code it describes is a transcript. Count plan lines against the expected change; if the plan is longer, cut it down to Interfaces, Verify and the risks.
