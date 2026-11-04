package main

// leechseed.go: the character console (LEECHSEED), BOLO 176, Chief 11/4. The Console's character pane: each character's
// card, fill list, raw record and derived stats, read from _tools/leechseed/characters/<id>.json (extract.py writes them).
// The verb is the spoken code name (leechseedVerb); it also answers to `command leechseed`.
//   command <verb>              open the character pane in the Console (else the page in the browser)
//   command <verb> --json       the character list with counts and gates
//   command <verb> --print      the same list as a table, once
//   command <verb> --dry-run    what it would open
//   command <verb> extract      re-run extract.py (--json · --dry-run pass through)
// The engine stays Python (_tools/leechseed/extract.py); this verb only reads its JSON and opens the page.

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"sort"
	"time"
)

const leechseedVerb = "siswet" // the spoken code name; the repo says leechseed everywhere else

type lsChar struct {
	ID     string            `json:"id"`
	Name   string            `json:"name"`
	Node   string            `json:"node"`
	Counts map[string]int    `json:"counts"`
	Gates  map[string]string `json:"gates"`
}

func lsList() ([]lsChar, error) {
	dir := filepath.Join(root, "_tools", "leechseed", "characters")
	files, err := filepath.Glob(filepath.Join(dir, "*.json"))
	if err != nil {
		return nil, err
	}
	out := []lsChar{}
	for _, f := range files {
		b, err := os.ReadFile(f)
		if err != nil {
			continue
		}
		var c lsChar
		if json.Unmarshal(b, &c) == nil && c.ID != "" {
			out = append(out, c)
		}
	}
	order := map[string]int{"victoria_midnight": 0, "anna_colson_conway": 1}
	rank := func(id string) int {
		if r, ok := order[id]; ok {
			return r
		}
		return 9
	}
	sort.SliceStable(out, func(i, j int) bool {
		if rank(out[i].ID) != rank(out[j].ID) {
			return rank(out[i].ID) < rank(out[j].ID)
		}
		return out[i].Name < out[j].Name
	})
	return out, nil
}

func leechseedCmd(args []string) {
	script := filepath.Join(root, "_tools", "leechseed", "extract.py")
	page := filepath.Join(root, "_tools", "leechseed", "console.html")
	if len(args) > 0 && args[0] == "extract" {
		c := exec.Command("python", append([]string{"-X", "utf8", script}, args[1:]...)...)
		c.Dir = root
		c.Stdout, c.Stderr = os.Stdout, os.Stderr
		if err := c.Run(); err != nil {
			os.Exit(1)
		}
		return
	}
	if len(args) > 0 && !hasFlag(args[:1], "--json") && !hasFlag(args[:1], "--print") && !hasFlag(args[:1], "--dry-run") {
		fmt.Println(sOK.Render("leechseed") + sDim.Render("  unknown verb "+args[0]+" · extract · --json · --print · --dry-run"))
		os.Exit(2)
	}
	chars, err := lsList()
	if hasFlag(args, "--json") {
		_, perr := os.Stat(page)
		m := map[string]interface{}{"characters": chars, "pane": "/local/leechseed", "page": page, "page_ok": perr == nil,
			"engine": script}
		if err != nil {
			m["error"] = err.Error()
		}
		b, _ := json.Marshal(m)
		fmt.Println(string(b))
		return
	}
	if hasFlag(args, "--print") {
		fmt.Println(sAccB.Render("LEECHSEED") + sDim.Render(" · the character console"))
		if len(chars) == 0 {
			fmt.Println(sDim.Render("  no characters yet: python -X utf8 _tools/leechseed/extract.py"))
			return
		}
		for _, c := range chars {
			fmt.Printf("  %-22s filled %3d  parked %3d  step1 %-4s  step3 %-4s\n", c.Name, c.Counts["filled"], c.Counts["parked"],
				c.Gates["step1"], c.Gates["step3"])
		}
		return
	}
	if hasFlag(args, "--dry-run") {
		fmt.Println(sDim.Render("  would open the character pane in the Console (/local/leechseed), else _tools/leechseed/console.html in the browser"))
		return
	}
	fmt.Println(sDim.Render("  " + openLeechseed()))
}

// openLeechseed: the Console's character pane when the Console answers, else the page file in the browser (no data there)
func openLeechseed() string {
	hc := &http.Client{Timeout: 3 * time.Second}
	body, _ := json.Marshal(map[string]string{"pane": "leechseed"})
	if r, err := hc.Post(consoleURL+"show", "application/json", bytes.NewReader(body)); err == nil {
		r.Body.Close()
		if r.StatusCode == http.StatusOK {
			return "opened in the Console (the character pane)"
		}
	}
	page := filepath.Join(root, "_tools", "leechseed", "console.html")
	if err := openDefault(page); err != nil {
		return "the Console did not take it and the browser did not open: " + err.Error()
	}
	return "the Console did not take it (down, or old code: python _tools/console/console.py --restart) · opened the page file (no data without the Console)"
}
