package main

// hour.go: `command hour` (go code: `fresh hour`, Chief 10/30) builds a fresh hour of BBC (gay lists + straight from Stash,
// no PMVs, nothing played today) and opens it in a new VLC window without touching any other player. The engine stays
// Python (_tools/stashplay/hour.py); this verb passes the arguments through. --json prints the clip list; --dry-run
// builds and prints without writing or launching.

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func hourCmd(args []string) {
	script := filepath.Join(root, "_tools", "stashplay", "hour.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("hour") + sDim.Render("  hour.py is missing from _tools/stashplay"))
		os.Exit(1)
	}
	py := []string{"-X", "utf8", script}
	for _, a := range args {
		if a != "hour" { // "fresh hour": the word is the go code, not an argument
			py = append(py, a)
		}
	}
	c := exec.Command("python", py...)
	c.Dir = root
	c.Stdin, c.Stdout, c.Stderr = os.Stdin, os.Stdout, os.Stderr
	if err := c.Run(); err != nil {
		os.Exit(1)
	}
}
