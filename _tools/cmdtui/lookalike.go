package main

// lookalike.go: `command lookalike <url-or-file>` is the site-layout reader, stage 1 (BOLO 161 call 4, Chief 10/31
// "take all recs"). One fetch of the page, no browser, no installs: it prints the layout skeleton (landmarks, the
// heading tree, grid/flex hints, color tokens, fonts, component counts). The engine stays Python
// (_tools/lookalike/lookalike.py); this verb passes the arguments through. --json prints the data; --print prints the
// text view once (the default); --out F also writes the JSON to F; --dry-run says what it would run.

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func lookalikeCmd(args []string) {
	script := filepath.Join(root, "_tools", "lookalike", "lookalike.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("lookalike") + sDim.Render("  lookalike.py is missing from _tools/lookalike"))
		os.Exit(1)
	}
	py := []string{"-X", "utf8", script}
	for _, a := range args {
		if a == "--dry-run" {
			continue
		}
		py = append(py, a)
	}
	if hasFlag(args, "--dry-run") {
		fmt.Println("would run: python " + fmt.Sprint(py))
		return
	}
	c := exec.Command("python", py...)
	c.Dir = root
	c.Stdin, c.Stdout, c.Stderr = os.Stdin, os.Stdout, os.Stderr
	if err := c.Run(); err != nil {
		os.Exit(1)
	}
}
