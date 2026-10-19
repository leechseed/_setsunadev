# The verb standard

Ruled by Chief on 10/19 (BOLO 153): "CLI everything". Every new tool ships as a `command` verb. This page says what a verb must do before it counts as done.

## The five rules

1. **One verb, one job.** The verb is `command <verb>`, written in `_tools/cmdtui/`, and listed in the help screen (`command` alone).
2. **`--json` prints the data.** Every verb can print its data as JSON, so Claude and the scripts read the same thing Chief sees.
3. **`--print` draws it once.** Every verb with a full-screen view can also print that view once and exit, for pipes and for the done check.
4. **`--dry-run` before writes.** A verb that changes files, moves data or pushes anything says what it would do under `--dry-run` and changes nothing.
5. **The engine stays Python.** The verb reads the JSON the Python scripts write, or runs those scripts. It never reimplements a station.

## The done check

A verb is done when:
- `go vet ./...` passes;
- `build.cmd` builds `command.exe`;
- `command <verb> --json` parses as JSON;
- `command <verb> --print` runs without an error;
- the help screen lists it.

## The look

Every color comes from `theme.go` (the BoldVenture palette). Full-screen views use the shared pager in `pager.go`: the strip with tabs on top, the body, the key line at the bottom.

## Where the pattern came from

The JSON output, the dry run and the test gate come from the harness method in HKUDS/CLI-Anything (`cli-anything-plugin/HARNESS.md`, Apache-2.0). We took the pattern only; the generator, the hub and the harnesses were not installed. The intake is logged on BOLO 140.
