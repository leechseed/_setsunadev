package main

// recall.go: `command recall <words>` is ranked search over the Command's own notes (BOLO 162 call 3, Chief "take
// all recs" 10/31): _CACHE, the _LOG session notes, the memory folder, SOP and STATE, split by section and ranked BM25.
// The engine stays Python (_tools/recall/recall.py, SQLite FTS5; the index sits gitignored in _PRIVATE/recall/);
// this verb passes the arguments through. With no words it prints the index summary. --json prints the data;
// --print prints it once; -n N · --source cache|log|memory|sop|state · --rebuild; --dry-run says what it would run.

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func recallCmd(args []string) {
	script := filepath.Join(root, "_tools", "recall", "recall.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("recall") + sDim.Render("  recall.py is missing from _tools/recall"))
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
