package main

// repos.go: `command repos` is REPOS ARE UP (BOLO 165, Chief 10/19): it reads a copy of Firefox's session file, keeps
// every github.com/<owner>/<repo> tab, and prints the list plus the intake hand-off line. The engine stays Python
// (_tools/intake/repos_up.py); this verb passes the arguments through. --json prints the data; --print prints it once;
// --file F reads another session file (the test fixture); --dry-run says what it would run.

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func reposCmd(args []string) {
	script := filepath.Join(root, "_tools", "intake", "repos_up.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("repos") + sDim.Render("  repos_up.py is missing from _tools/intake"))
		os.Exit(1)
	}
	py := []string{"-X", "utf8", script}
	for _, a := range args {
		if a == "--dry-run" || a == "--print" {
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
