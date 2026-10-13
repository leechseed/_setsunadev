# Tasks: <job name>

Order: <the one-line order this job serves>
Ticked by: <the loop or RANGE script that checks each done line>

Format: `- [ ] N. task`, then its done line (a command and the output that proves it), `_Boundary:_` (files it may touch), `_Depends:_` (task numbers). `(P)` marks a task that can run in parallel. A script ticks a box only after the done line passes. Notes carried forward go at the bottom so a run resumes after a crash.

- [ ] 1. <task>
  - Done when: `<command>` prints `<expected>`
  - _Boundary:_ <paths>
  - _Depends:_ none
- [ ] 2. (P) <task>
  - Done when: `<command>` prints `<expected>`
  - _Boundary:_ <paths>
  - _Depends:_ 1

## Notes carried forward
- <date>: <what the next run must know>
