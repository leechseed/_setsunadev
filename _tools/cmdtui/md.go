package main

// command md <file>: any markdown file rendered in the terminal (Glamour, the engine behind Glow), in the
// BoldVenture colors, inside the shared pager. Shortcuts: sop · bolo · state · projects. --json lists the headings.

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"strings"

	"github.com/charmbracelet/glamour"
	gansi "github.com/charmbracelet/glamour/ansi"
	"github.com/charmbracelet/glamour/styles"
)

var mdShort = map[string]string{"sop": "SOP.md", "bolo": "BOLO.md", "state": "STATE.md", "projects": "PROJECTS.md"}

func mdPath(arg string) string {
	if f, ok := mdShort[strings.ToLower(arg)]; ok {
		return filepath.Join(root, f)
	}
	if filepath.IsAbs(arg) {
		return arg
	}
	if _, err := os.Stat(arg); err == nil {
		return arg
	}
	return filepath.Join(root, arg)
}

func sp(s string) *string { return &s }
func bp(b bool) *bool     { return &b }

// mdStyle: Glamour's dark style with the headings, links and bold in BoldVenture orange
func mdStyle() gansi.StyleConfig {
	s := styles.DarkStyleConfig
	s.Document.Color = sp("#c6cbc8")
	s.Heading.Color = sp("#FF5A1F")
	s.Heading.Bold = bp(true)
	s.H1.Color = sp("#050608")
	s.H1.BackgroundColor = sp("#FF5A1F")
	s.H2.Color = sp("#FF5A1F")
	s.H3.Color = sp("#FFB08F")
	s.Link.Color = sp("#79dfff")
	s.LinkText.Color = sp("#FFB08F")
	s.Strong.Color = sp("#FFB08F")
	s.Code.Color = sp("#e3b341")
	s.HorizontalRule.Color = sp("#5f6160")
	return s
}

func mdCmd(args []string) {
	if len(args) == 0 {
		fmt.Println(sAccB.Render("command md") + sDim.Render(" <file | sop | bolo | state | projects> [--json]"))
		return
	}
	path := mdPath(args[0])
	src, err := os.ReadFile(path)
	if err != nil {
		fmt.Fprintln(os.Stderr, "command md:", err)
		os.Exit(1)
	}
	if hasFlag(args, "--json") { // the rule (Chief 10/19): every verb can print JSON
		var heads []string
		for _, l := range strings.Split(string(src), "\n") {
			if strings.HasPrefix(l, "#") {
				heads = append(heads, strings.TrimSpace(l))
			}
		}
		b, _ := json.MarshalIndent(map[string]any{"file": path, "bytes": len(src), "headings": heads}, "", " ")
		fmt.Println(string(b))
		return
	}
	if s := strings.ReplaceAll(string(src), "\r\n", "\n"); strings.HasPrefix(s, "---\n") { // the YAML front matter is for scripts, not the reader
		if end := strings.Index(s[4:], "\n---\n"); end >= 0 {
			src = []byte(s[4+end+5:])
		}
	}
	cache := map[int]string{}
	render := func(_ int, width int) string {
		if out, ok := cache[width]; ok {
			return out
		}
		r, err := glamour.NewTermRenderer(glamour.WithStyles(mdStyle()), glamour.WithWordWrap(max(width-2, 40)))
		if err != nil {
			return string(src)
		}
		out, err := r.Render(string(src))
		if err != nil {
			return string(src)
		}
		cache[width] = out
		return out
	}
	if hasFlag(args, "--print") { // rendered once, no pager
		fmt.Print(render(0, 100))
		return
	}
	if err := runPager(&pager{title: filepath.Base(path), render: render}); err != nil {
		fmt.Print(render(0, 100)) // no terminal: print it
	}
}

func hasFlag(args []string, f string) bool {
	for _, a := range args {
		if a == f {
			return true
		}
	}
	return false
}
