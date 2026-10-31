package main

// bookmarks.go: `command bookmarks` runs the bookmark dig (BOLO 167, Chief 10/19 and 10/31): it reads a copy of
// Firefox's bookmark store, checks for dead links, ranks the keepers, saves offline text and builds the judging page
// at _PRIVATE/reference/bookmarks/bookmarks.html. The engine stays Python (_tools/bookmarks/dig.py); this verb passes
// the arguments through. With no dig verb it prints the summary. --json prints the data; --print prints it once;
// --dry-run says what it would run.

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func bookmarksCmd(args []string) {
	script := filepath.Join(root, "_tools", "bookmarks", "dig.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("bookmarks") + sDim.Render("  dig.py is missing from _tools/bookmarks"))
		os.Exit(1)
	}
	py := []string{"-X", "utf8", script}
	verb := false
	for _, a := range args {
		if a == "--dry-run" || a == "--print" {
			continue
		}
		if len(a) > 0 && a[0] != '-' && !verb {
			verb = true
		}
		py = append(py, a)
	}
	if !verb {
		py = append(py[:3], append([]string{"summary"}, py[3:]...)...)
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
