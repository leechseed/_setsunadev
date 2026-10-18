package main

// The fetch panel (Chief 10/18, neofetch for the Command): the same numbers the Console's boot screen shows.

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"
	"time"

	"github.com/charmbracelet/lipgloss"
)

func git(args ...string) string {
	cmd := exec.Command("git", args...)
	cmd.Dir = root
	b, err := cmd.Output()
	if err != nil {
		return ""
	}
	return strings.TrimSpace(string(b))
}

func fetchRows() [][2]string {
	up := "?"
	if first := strings.SplitN(git("log", "--reverse", "--format=%cs"), "\n", 2)[0]; first != "" {
		if d, err := time.Parse("2006-01-02", first); err == nil {
			up = fmt.Sprintf("%d days (since %s)", int(time.Since(d).Hours()/24), first)
		}
	}
	commits := git("rev-list", "--count", "HEAD")
	if n, err := strconv.Atoi(commits); err == nil {
		commits = comma(n)
	}
	bolos := 0
	if f, err := os.Open(filepath.Join(root, "BOLO.md")); err == nil {
		sc := bufio.NewScanner(f)
		sc.Buffer(make([]byte, 1<<20), 1<<24)
		for sc.Scan() {
			if l := sc.Text(); len(l) > 2 && l[:2] == "| " && l[2] >= '0' && l[2] <= '9' {
				bolos++
			}
		}
		f.Close()
	}
	stations := "?"
	var poll struct {
		Stations []struct {
			Go bool `json:"go"`
		} `json:"stations"`
	}
	if b, err := os.ReadFile(filepath.Join(root, "_tools", "launch", "last_poll.json")); err == nil && json.Unmarshal(b, &poll) == nil {
		ok := 0
		for _, s := range poll.Stations {
			if s.Go {
				ok++
			}
		}
		stations = fmt.Sprintf("%d/%d GO", ok, len(poll.Stations))
	}
	agents, _ := filepath.Glob(filepath.Join(root, ".claude", "agents", "*.md"))
	skills, _ := filepath.Glob(filepath.Join(root, ".claude", "skills", "*", "SKILL.md"))
	glasses := 0
	var gl struct {
		Glasses []json.RawMessage `json:"glasses"`
	}
	if b, err := os.ReadFile(filepath.Join(root, "_tools", "console", "glasses.json")); err == nil && json.Unmarshal(b, &gl) == nil {
		glasses = len(gl.Glasses)
	}
	return [][2]string{
		{"OS", "The Command · BoldVenture"},
		{"Kernel", "Claude Code · Opus 5.5 (CDR)"},
		{"Uptime", up},
		{"Commits", commits},
		{"Stations", stations},
		{"BOLOs", fmt.Sprintf("%d on the board", bolos)},
		{"Agents", fmt.Sprintf("%d on call", len(agents))},
		{"Skills", strconv.Itoa(len(skills))},
		{"Glasses", fmt.Sprintf("%d published", glasses)},
		{"Shell", "bash 5 · PowerShell 7"},
		{"Terminal", "Windows Terminal · command up"},
		{"Voice", "JUDY"},
		{"Theme", "BoldVenture orange #FF5A1F"},
		{"Font", "IBM Plex Mono"},
	}
}

func comma(n int) string {
	s := strconv.Itoa(n)
	for i := len(s) - 3; i > 0; i -= 3 {
		s = s[:i] + "," + s[i:]
	}
	return s
}

// fetchBlock renders the first `shown` lines of the panel (the boot types it in)
func fetchBlock(rows [][2]string, shown int) string {
	lines := []string{sAccB.Render("chief") + sFg.Render("@") + sAccB.Render("the-command"), sDim.Render(strings.Repeat("-", 17))}
	for _, r := range rows {
		lines = append(lines, sAccB.Render(r[0])+sFg.Render(": "+r[1]))
	}
	sw := func(cs []string) string {
		var b strings.Builder
		for _, c := range cs {
			b.WriteString(lipgloss.NewStyle().Background(lipgloss.Color(c)).Render("   "))
		}
		return b.String()
	}
	lines = append(lines, "", sw(swatchA), sw(swatchB))
	if shown >= 0 && shown < len(lines) {
		lines = lines[:shown]
	}
	return strings.Join(lines, "\n")
}
