package main

// goon.go: `command goon` runs the Goon program (BOLO 111 / Chief 10/30): a standard hour on the clock, the hit timer,
// the bust and vape cues, VLC held on top, and a start and end record. The engine stays Python (_PRIVATE/goon/goon.py);
// this verb passes the arguments through. --json prints the last session record; --dry-run says what it would run.

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func goonCmd(args []string) {
	dir := filepath.Join(root, "_PRIVATE", "goon")
	script := filepath.Join(dir, "goon.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("goon") + sDim.Render("  goon.py is missing from _PRIVATE/goon"))
		os.Exit(1)
	}
	py := []string{"-X", "utf8", script}
	for _, a := range args {
		if a != "--dry-run" {
			py = append(py, a)
		}
	}
	if hasFlag(args, "--dry-run") {
		fmt.Println("would run: python " + fmt.Sprint(py))
		return
	}
	c := exec.Command("python", py...)
	c.Dir = dir
	c.Stdin, c.Stdout, c.Stderr = os.Stdin, os.Stdout, os.Stderr
	if err := c.Run(); err != nil {
		os.Exit(1)
	}
}
