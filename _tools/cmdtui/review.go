package main

// review.go: `command review` (BOLO 125, Chief 11/4 "Go."): the review desk's reviews. Chief highlights a Command doc in
// the Console's Review desk pane, comments, suggests changes, records voice notes and sends it; each review lands in
// _PRIVATE/reviews/<doc-slug>-<timestamp>/ (review.json + audio). The engine stays Python (_tools/reviewdesk/reviewdesk.py).
//   command review                     the open reviews, newest first (--all adds the done ones · --json · --print)
//   command review show <id|N|latest>  one review: every note with its quote, change and voice file (--json)
//   command review done <id|N>         mark it read once a session has acted on it (--dry-run · --json)
//   command review open                open the Review desk pane in the Console (--dry-run says what it would open)

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

func reviewCmd(args []string) {
	script := filepath.Join(root, "_tools", "reviewdesk", "reviewdesk.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("review") + sDim.Render("  reviewdesk.py is missing from _tools/reviewdesk"))
		os.Exit(1)
	}
	verb := "list"
	if len(args) > 0 && args[0] != "" && args[0][0] != '-' {
		verb, args = args[0], args[1:]
	}
	switch verb {
	case "open":
		if hasFlag(args, "--dry-run") || hasFlag(args, "--json") {
			b, _ := json.Marshal(map[string]string{"would_open": consoleURL + "local/review", "pane": "review"})
			fmt.Println(string(b))
			return
		}
		fmt.Println(sDim.Render("  " + openReview()))
		return
	case "list", "show", "done", "docs":
	default:
		fmt.Println(sOK.Render("review") + sDim.Render("  unknown verb "+verb+" · show <id|N|latest> · done <id> · open · docs"))
		os.Exit(2)
	}
	py := append([]string{"-X", "utf8", script, verb}, args...)
	c := exec.Command("python", py...)
	c.Dir = root
	c.Stdin, c.Stdout, c.Stderr = os.Stdin, os.Stdout, os.Stderr
	if err := c.Run(); err != nil {
		if ee, ok := err.(*exec.ExitError); ok {
			os.Exit(ee.ExitCode())
		}
		os.Exit(1)
	}
	if verb == "list" && !hasFlag(args, "--json") && !hasFlag(args, "--print") {
		fmt.Println(sDim.Render("  command review show <N> · command review open (the desk in the Console)"))
	}
}

// openReview: the Console's Review desk pane when the Console answers, else the page's URL to open by hand
func openReview() string {
	hc := &http.Client{Timeout: 3 * time.Second}
	body, _ := json.Marshal(map[string]string{"pane": "review"})
	if r, err := hc.Post(consoleURL+"show", "application/json", bytes.NewReader(body)); err == nil {
		r.Body.Close()
		if r.StatusCode == http.StatusOK {
			return "opened in the Console (Review desk)"
		}
		if err := openDefault(consoleURL + "local/review"); err == nil {
			return "the Console runs old code (python _tools/console/console.py --restart) · opened " + consoleURL + "local/review in the browser"
		}
	}
	return "the Console is down: start it (command up, or python _tools/console/console.py), then command review open"
}
