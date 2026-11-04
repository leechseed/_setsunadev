package main

// file.go: `command file <filing.json>` applies an approved scan filing (BOLO 149/170, 11/4: Chief "take every rec"):
// each scan folder moves from _PRIVATE/intake/paper/scans/ into its intake bin, a filing.md lands beside it, and the
// files that cite the old path are rewritten. The engine stays Python (_tools/intake/file_apply.py). A plain run is a
// dry run; --apply moves; --json prints the plan or the result; --dry-run is accepted and changes nothing.

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func fileCmd(args []string) {
	script := filepath.Join(root, "_tools", "intake", "file_apply.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("file") + sDim.Render("  file_apply.py is missing from _tools/intake"))
		os.Exit(1)
	}
	py := []string{"-X", "utf8", script}
	for _, a := range args {
		if a == "--dry-run" || a == "--print" {
			continue
		}
		py = append(py, a)
	}
	if hasFlag(args, "--dry-run") && hasFlag(args, "--apply") {
		fmt.Println(sDim.Render("--dry-run wins: nothing moves"))
		var keep []string
		for _, a := range py {
			if a != "--apply" {
				keep = append(keep, a)
			}
		}
		py = keep
	}
	c := exec.Command("python", py...)
	c.Dir = root
	c.Stdin, c.Stdout, c.Stderr = os.Stdin, os.Stdout, os.Stderr
	if err := c.Run(); err != nil {
		os.Exit(1)
	}
}
