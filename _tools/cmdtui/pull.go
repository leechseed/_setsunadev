package main

// command pull: the pull waves (BOLO 137) on the shared pager. pull_queue.py json is the engine: it reads the queue
// and the wave logs and writes nothing; this only draws its counts. Tab 1 Live: a card per live wave. Tab 2 All
// waves: a thin bar per wave. r reruns the read. --json prints the engine's JSON as it is; --print draws both tabs.

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"math"
	"os"
	"os/exec"
	"path/filepath"
	"strconv"
	"strings"
	"time"

	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
)

type pullWave struct {
	N       int     `json:"n"`
	State   string  `json:"state"` // pulling · stalled · landed
	Size    int     `json:"size"`
	Done    int     `json:"done"`
	Empty   int     `json:"empty"`
	Dropped int     `json:"dropped"`
	Left    int     `json:"left"`
	Images  int     `json:"images"`
	Pace    float64 `json:"pace"` // minutes a board
	ETA     string  `json:"eta"`  // 12-hour, from the engine; empty once landed
	E429    int     `json:"e429"`
	Quiet   float64 `json:"quiet"` // minutes since the log last moved
}

type pullMapRow struct {
	N      int    `json:"n"`
	Size   int    `json:"size"`
	Got    int    `json:"got"`
	Images int    `json:"images"`
	State  string `json:"state"` // landed · part · todo · pulling · stalled
}

type pullSnap struct {
	When      string       `json:"when"`
	Pulled    int          `json:"pulled"`
	Total     int          `json:"total"`
	Images    int          `json:"images"`
	HeldVideo int          `json:"held_video"`
	QFreeGB   float64      `json:"q_free_gb"`
	Low       bool         `json:"low"`
	Waves     []pullWave   `json:"waves"`
	Map       []pullMapRow `json:"map"`
}

var pullTabs = []string{"Live", "All waves"}

var pullStateSty = map[string]lipgloss.Style{
	"pulling": sAccB, "stalled": sBad, "landed": sOK, "part": sAmber, "todo": sDim,
}

// runPullJSON: python -X utf8 pull_queue.py json in the engine's folder, 30 s at most
func runPullJSON() ([]byte, error) {
	py, err := exec.LookPath("python")
	if err != nil {
		return nil, errors.New("python is not on PATH")
	}
	dir := filepath.Join(root, "_PRIVATE", "taxonomy_engine")
	if _, err := os.Stat(filepath.Join(dir, "pull_queue.py")); err != nil {
		return nil, errors.New("no pull_queue.py in " + dir)
	}
	if _, err := os.Stat(filepath.Join(root, "_PRIVATE", "reference", "pullqueue", "queue.json")); err != nil {
		return nil, errors.New("no queue yet (pull_queue.py build writes queue.json)")
	}
	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	defer cancel()
	c := exec.CommandContext(ctx, py, "-X", "utf8", "pull_queue.py", "json")
	c.Dir = dir
	out, err := c.Output()
	if ctx.Err() == context.DeadlineExceeded {
		return nil, errors.New("pull_queue.py json ran past 30 s")
	}
	if err != nil {
		msg := err.Error()
		var ee *exec.ExitError
		if errors.As(err, &ee) {
			if ls := strings.Split(strings.TrimSpace(string(ee.Stderr)), "\n"); ls[len(ls)-1] != "" {
				msg = strings.TrimSpace(ls[len(ls)-1])
			}
		}
		return nil, errors.New("pull_queue.py json: " + msg)
	}
	return out, nil
}

func readPull() (*pullSnap, error) {
	raw, err := runPullJSON()
	if err != nil {
		return nil, err
	}
	var s pullSnap
	if err := json.Unmarshal(raw, &s); err != nil {
		return nil, fmt.Errorf("the engine's JSON did not parse: %v", err)
	}
	return &s, nil
}

// pullNum: 449789 as 449,789
func pullNum(n int) string {
	s := strconv.Itoa(n)
	for i := len(s) - 3; i > 0 && s[i-1] != '-'; i -= 3 {
		s = s[:i] + "," + s[i:]
	}
	return s
}

// pullCells: how many of w cells a share of size fills
func pullCells(part, size, w int) int {
	if size <= 0 {
		return 0
	}
	return min(max(int(math.Round(float64(part)*float64(w)/float64(size))), 0), w)
}

// pullSeg: the card's bar, █ done (green) · ▒ empty or dropped (dim) · ░ left
func pullSeg(wv pullWave, w int) string {
	d := pullCells(wv.Done, wv.Size, w)
	e := pullCells(wv.Done+wv.Empty+wv.Dropped, wv.Size, w) - d
	return sOK.Render(strings.Repeat("█", d)) + sDim.Render(strings.Repeat("▒", e)) + sDim.Render(strings.Repeat("░", w-d-e))
}

func pullChip(state string) string {
	st, ok := pullStateSty[state]
	if !ok {
		st = sDim
	}
	t := strings.ToUpper(state)
	if state == "stalled" {
		t += "?"
	}
	return st.Render("[" + t + "]")
}

// pullHead: the line on top of both tabs
func pullHead(s *pullSnap, width int) string {
	pct := 0.0
	if s.Total > 0 {
		pct = 100 * float64(s.Pulled) / float64(s.Total)
	}
	line := "  " + sWhite.Render(pullNum(s.Pulled)+"/"+pullNum(s.Total)) + sDim.Render(fmt.Sprintf(" boards pulled (%.0f%%) · ", pct)) +
		sFg.Render(pullNum(s.Images)) + sDim.Render(" images · Q free ") + sFg.Render(pullNum(int(math.Round(s.QFreeGB)))+" GB")
	if s.Low {
		line += " " + sBad.Render("[LOW]") + sDim.Render(" under 200 GB, the waves crash when Q fills")
	}
	sub := sDim.Render(fmt.Sprintf("  as of %s · %s video-heavy boards held for the video step", s.When, pullNum(s.HeldVideo)))
	return lipgloss.NewStyle().Width(max(width, 30)).Render(line) + "\n" + sub
}

func pullCard(wv pullWave, width int) []string {
	barW := max(min(width-24, 60), 10)
	got := wv.Done + wv.Empty + wv.Dropped
	eta := wv.ETA
	if eta == "" {
		eta = "-"
	}
	out := []string{
		sAcc.Render(fmt.Sprintf("── WAVE %d", wv.N)) + "  " + pullChip(wv.State),
		"  " + pullSeg(wv, barW) + "  " + sWhite.Render(fmt.Sprintf("%d/%d", got, wv.Size)) + sDim.Render(" boards"),
		"  " + sFg.Render(pullNum(wv.Images)) + sDim.Render(" images · pace ") + sFg.Render(fmt.Sprintf("%.0f", wv.Pace)) +
			sDim.Render(" min/board · ETA ") + sFg.Render(eta) + sDim.Render(" · 429s ") + sFg.Render(strconv.Itoa(wv.E429)) +
			sDim.Render(" · quiet ") + sFg.Render(fmt.Sprintf("%.0f", wv.Quiet)) + sDim.Render(" min"),
	}
	tail := fmt.Sprintf("  %d done · %d empty", wv.Done, wv.Empty)
	if wv.Dropped > 0 {
		tail += fmt.Sprintf(" · %d dropped", wv.Dropped)
	}
	out = append(out, sDim.Render(tail+fmt.Sprintf(" · %d left", wv.Left)))
	if wv.State == "stalled" {
		out = append(out, sBad.Render("  the log is quiet past its pace")+
			sDim.Render(fmt.Sprintf(" · if the runner died: delete wave%d.lock, then pull_queue.py wave %d", wv.N, wv.N)))
	}
	return out
}

func pullMapLine(m pullMapRow, width int) string {
	barW := max(min(width-44, 40), 10)
	f := pullCells(m.Got, m.Size, barW)
	st, ok := pullStateSty[m.State]
	if !ok {
		st = sDim
	}
	return fmt.Sprintf("  %s %s%s  %s  %s  %s", sDim.Render(fmt.Sprintf("wave %3d", m.N)), st.Render(strings.Repeat("━", f)),
		sDim.Render(strings.Repeat("─", barW-f)), sWhite.Render(fmt.Sprintf("%3d/%-3d", m.Got, m.Size)),
		sFg.Render(fmt.Sprintf("%9s", pullNum(m.Images)))+sDim.Render(" images"), st.Render(m.State))
}

func pullRender(s *pullSnap, tab, width int) string {
	out := []string{pullHead(s, width), ""}
	if tab == 0 {
		if len(s.Waves) == 0 {
			return strings.Join(append(out, sDim.Render("  no wave is live · the All waves tab has the whole queue")), "\n")
		}
		for _, wv := range s.Waves {
			out = append(out, pullCard(wv, width)...)
			out = append(out, "")
		}
		return strings.Join(out, "\n")
	}
	out = append(out, sAcc.Render(fmt.Sprintf("── ALL WAVES (%d)", len(s.Map))))
	for _, m := range s.Map {
		out = append(out, pullMapLine(m, width))
	}
	var key []string
	for _, k := range []string{"pulling", "stalled", "landed", "part", "todo"} {
		key = append(key, pullStateSty[k].Render("━ "+k))
	}
	return strings.Join(append(out, "", "  "+strings.Join(key, sDim.Render(" · "))), "\n")
}

// pullView: the pager plus r, which reruns the engine without stopping the screen
type pullView struct {
	*pager
	snap *pullSnap
}

type pullRead struct {
	s   *pullSnap
	err error
}

func (v *pullView) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.KeyMsg:
		if msg.String() == "r" {
			v.note = "rereading…"
			return v, func() tea.Msg { s, err := readPull(); return pullRead{s, err} }
		}
	case pullRead:
		if msg.err != nil {
			v.note = "reread failed: " + msg.err.Error()
			return v, nil
		}
		v.snap, v.note = msg.s, "r reread · read "+time.Now().Format("3:04 PM")
		if v.ready {
			y := v.vp.YOffset
			v.load()
			v.vp.SetYOffset(y)
		}
		return v, nil
	}
	_, cmd := v.pager.Update(msg)
	return v, cmd
}

func pullCmd(args []string) {
	if hasFlag(args, "--json") { // the engine's JSON as it is
		raw, err := runPullJSON()
		if err != nil {
			fmt.Fprintln(os.Stderr, "command pull:", err)
			os.Exit(1)
		}
		os.Stdout.Write(raw)
		return
	}
	s, err := readPull()
	if err != nil {
		fmt.Fprintln(os.Stderr, "command pull:", err)
		os.Exit(1)
	}
	if _, _, err := termSize(); hasFlag(args, "--print") || err != nil { // both tabs once, no pager (and no terminal)
		for i, t := range pullTabs {
			fmt.Println(sAccB.Render("◆ PULL · "+strings.ToUpper(t)) + "\n" + pullRender(s, i, 100) + "\n")
		}
		return
	}
	v := &pullView{snap: s}
	v.pager = &pager{title: "pull", tabs: pullTabs, note: "r reread · as of " + s.When}
	v.render = func(tab, width int) string { return pullRender(v.snap, tab, width) }
	if _, err := tea.NewProgram(v, tea.WithAltScreen(), tea.WithMouseCellMotion()).Run(); err != nil {
		fmt.Fprintln(os.Stderr, "command pull:", err)
		os.Exit(1)
	}
}
