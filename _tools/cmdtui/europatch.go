package main

// europatch.go: `command europatch` (BOLO 173, Chief 10/31: "lock it and run what you need"). The patch bay: LEECHSEED's
// 12 layers as patch modules, dials + patch cables, a seed rolls one character instance as JSON. The engine stays
// Python (_tools/europatch/europatch.py); this verb passes its verbs through and opens the page.
//   command europatch                         open the Patch bay pane in the Console (else the page in the browser)
//   command europatch roll <patch|default|preset:NAME> [--seed N] [--json] [--out F]
//   command europatch modules|presets|default [--json] · check <patch> [--json] · build [--json]
// Every verb takes --json (the engine's own JSON). With no verb: --json prints the status, --print the module table
// once, --dry-run what it would open; only the bare word opens anything. build --dry-run writes nothing.

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

func europatchCmd(args []string) {
	script := filepath.Join(root, "_tools", "europatch", "europatch.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("europatch") + sDim.Render("  europatch.py is missing from _tools/europatch"))
		os.Exit(1)
	}
	verbs := map[string]bool{"roll": true, "modules": true, "presets": true, "check": true, "default": true, "build": true, "help": true}
	if len(args) > 0 && verbs[args[0]] {
		py := append([]string{"-X", "utf8", script}, args...)
		c := exec.Command("python", py...)
		c.Dir = root
		c.Stdin, c.Stdout, c.Stderr = os.Stdin, os.Stdout, os.Stderr
		if err := c.Run(); err != nil {
			if ee, ok := err.(*exec.ExitError); ok {
				os.Exit(ee.ExitCode())
			}
			os.Exit(1)
		}
		return
	}
	if len(args) > 0 && !hasFlag(args[:1], "--json") && !hasFlag(args[:1], "--print") && !hasFlag(args[:1], "--dry-run") {
		fmt.Println(sOK.Render("europatch") + sDim.Render("  unknown verb "+args[0]+" · roll · modules · presets · check · default · build"))
		os.Exit(2)
	}
	if hasFlag(args, "--json") { // the status, no side effects (the done check)
		page := filepath.Join(root, "_tools", "europatch", "patchbay.html")
		_, perr := os.Stat(page)
		b, _ := json.Marshal(map[string]interface{}{"page": page, "page_ok": perr == nil, "pane": "/local/europatch",
			"engine": script, "verbs": []string{"roll", "modules", "presets", "check", "default", "build"}})
		fmt.Println(string(b))
		return
	}
	if hasFlag(args, "--print") { // the module table, once
		c := exec.Command("python", "-X", "utf8", script, "modules")
		c.Dir = root
		c.Stdout, c.Stderr = os.Stdout, os.Stderr
		if err := c.Run(); err != nil {
			os.Exit(1)
		}
		return
	}
	if hasFlag(args, "--dry-run") {
		fmt.Println(sDim.Render("  would open the Patch bay pane in the Console (/local/europatch), else _tools/europatch/patchbay.html in the browser"))
		return
	}
	fmt.Println(sDim.Render("  " + openEuropatch()))
}

// openEuropatch: the Console's Patch bay pane when the Console answers, else the page in the default browser
// (a file copy rolls with the page's JS mirror and saves by download)
func openEuropatch() string {
	hc := &http.Client{Timeout: 3 * time.Second}
	body, _ := json.Marshal(map[string]string{"pane": "europatch"})
	if r, err := hc.Post(consoleURL+"show", "application/json", bytes.NewReader(body)); err == nil {
		r.Body.Close()
		if r.StatusCode == http.StatusOK {
			return "opened in the Console (Patch bay)"
		}
	}
	page := filepath.Join(root, "_tools", "europatch", "patchbay.html")
	if err := openDefault(page); err != nil {
		return "the Console did not take it and the browser did not open: " + err.Error()
	}
	return "the Console did not take it (down, or old code: python _tools/console/console.py --restart) · opened in the browser (JS mirror)"
}
