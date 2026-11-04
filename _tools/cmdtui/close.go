package main

// close.go: `command close <n> [<n> ...] --why "<who said what>"` moves finished BOLO rows from the active table to
// the Done table, stamped (the Docket, Chief 11/4: "ship the BOLO close script as a command verb", the verb rule).
// The engine stays Python (_tools/bolo/close.py; keeps BOLO.md CRLF, refuses an unknown number, never deletes a row);
// this verb passes the arguments through. --dry-run says what would move without writing; --json prints the data.

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func closeCmd(args []string) {
	script := filepath.Join(root, "_tools", "bolo", "close.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("close") + sDim.Render("  close.py is missing from _tools/bolo"))
		os.Exit(1)
	}
	py := append([]string{"-X", "utf8", script}, args...)
	c := exec.Command("python", py...)
	c.Dir = root
	c.Stdin, c.Stdout, c.Stderr = os.Stdin, os.Stdout, os.Stderr
	if err := c.Run(); err != nil {
		os.Exit(1)
	}
}
