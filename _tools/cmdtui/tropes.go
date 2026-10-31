package main

// tropes.go: `command tropes` builds the trope system glass (BOLO 89, Chief 10/31: "i want to be able to browse the
// system itself") and opens it in the Console's Tropes pane. The engine stays Python (_tools/tropes/build_glass.py):
// it writes _tools/tropes/glass/tropes.html. --json prints the build summary; --print prints the summary line once
// (no open); --dry-run says what it would write. When the Console is down the page opens in the default browser.

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"time"
)

func tropesCmd(args []string) {
	script := filepath.Join(root, "_tools", "tropes", "build_glass.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("tropes") + sDim.Render("  build_glass.py is missing from _tools/tropes"))
		os.Exit(1)
	}
	py := []string{"-X", "utf8", script}
	if hasFlag(args, "--json") {
		py = append(py, "--json")
	}
	if hasFlag(args, "--dry-run") {
		py = append(py, "--dry-run")
	}
	c := exec.Command("python", py...)
	c.Dir = root
	c.Stdin, c.Stdout, c.Stderr = os.Stdin, os.Stdout, os.Stderr
	if err := c.Run(); err != nil {
		os.Exit(1)
	}
	if hasFlag(args, "--json") || hasFlag(args, "--dry-run") || hasFlag(args, "--print") {
		return
	}
	fmt.Println(sDim.Render("  " + openTropes()))
}

// openTropes: the Console's Tropes pane when the Console answers, else the page in the default browser
func openTropes() string {
	hc := &http.Client{Timeout: 3 * time.Second}
	body, _ := json.Marshal(map[string]string{"pane": "tropes"})
	if r, err := hc.Post(consoleURL+"show", "application/json", bytes.NewReader(body)); err == nil {
		r.Body.Close()
		if r.StatusCode == http.StatusOK {
			return "opened in the Console (Tropes)"
		}
	}
	page := filepath.Join(root, "_tools", "tropes", "glass", "tropes.html")
	if err := openDefault(page); err != nil {
		return "the Console did not take it and the browser did not open: " + err.Error()
	}
	return "the Console did not take it (down, or old code: python _tools/console/console.py --restart) · opened in the browser"
}
