package main

// command glass: the recent glasses (every page Claude published, from the list glasses.py writes), newest first,
// on the shared pager with a cursor. Enter hands the row to the Console, which opens it in its frame; with the
// Console down, the default browser opens it. r reruns glasses.py. --json prints glasses.json as it is;
// command glass <id|N> --json prints what the pick did.

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"net/url"
	"os"
	"os/exec"
	"path/filepath"
	"sort"
	"strconv"
	"strings"
	"syscall"
	"time"

	"github.com/charmbracelet/x/ansi"
)

const consoleURL = "http://127.0.0.1:8795/" // the Console (console.py); the only server this verb talks to

var glassRefresh = []string{"python", "-X", "utf8", "_tools/console/glasses.py"} // run from the repo root

type glass struct {
	ID    string `json:"id"`
	Title string `json:"title"`
	URL   string `json:"url"`
	File  string `json:"file"`
	When  string `json:"when"`
	Local bool   `json:"local"`
}

type glassPick struct {
	ID       string `json:"id"`
	OpenedIn string `json:"opened_in"` // console · browser · none
	Target   string `json:"target"`
	Note     string `json:"note"`
}

func loadGlasses() (raw []byte, gs []glass, at string, err error) {
	raw, err = os.ReadFile(filepath.Join(root, "_tools", "console", "glasses.json"))
	if err != nil {
		return nil, nil, "", err
	}
	var doc struct {
		At      string  `json:"at"`
		Glasses []glass `json:"glasses"`
	}
	if err = json.Unmarshal(raw, &doc); err != nil {
		return nil, nil, "", err
	}
	gs = doc.Glasses
	sort.SliceStable(gs, func(i, j int) bool { return gs[i].When > gs[j].When })
	return raw, gs, doc.At, nil
}

func runGlassesPy() error {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Minute)
	defer cancel()
	c := exec.CommandContext(ctx, glassRefresh[0], glassRefresh[1:]...)
	c.Dir = root
	out, err := c.CombinedOutput()
	if err != nil {
		return fmt.Errorf("%v: %s", err, strings.TrimSpace(string(out)))
	}
	return nil
}

func glassSummary(gs []glass, at string) string {
	n := 0
	for _, g := range gs {
		if g.Local {
			n++
		}
	}
	s := fmt.Sprintf("%d glasses · %d local", len(gs), n)
	if t, err := time.ParseInLocation("2006-01-02 15:04:05", at, time.Local); err == nil {
		s += " · listed " + t.Format("Jan 2, 3:04 PM")
	}
	return s
}

func glassDay(t time.Time) string {
	now := time.Now()
	switch t.Format("2006-01-02") {
	case now.Format("2006-01-02"):
		return "TODAY"
	case now.AddDate(0, 0, -1).Format("2006-01-02"):
		return "YESTERDAY"
	}
	return strings.ToUpper(t.Format("Jan 2"))
}

// glassBody: one line per glass under a line per day; the pager's cursor steps over the glass lines
func glassBody(gs []glass, width int) string {
	if len(gs) == 0 {
		return sDim.Render("  no glasses yet · r runs glasses.py")
	}
	tw := max(width-35, 12) // the title's room: number, time, chip and id take the rest
	var out []string
	last := ""
	for i, g := range gs {
		day, hm := "UNDATED", "--:--"
		if t, err := time.Parse(time.RFC3339Nano, g.When); err == nil {
			day, hm = glassDay(t.Local()), t.Local().Format("3:04 PM")
		}
		if day != last {
			if last != "" {
				out = append(out, "")
			}
			out = append(out, sAcc.Render("── "+day))
			last = day
		}
		chip := sOK.Render("[local]")
		if !g.Local {
			chip = sAmber.Render("[ web ]")
		}
		title := ansi.Truncate(ansi.Strip(g.Title), tw, "…")
		title += strings.Repeat(" ", max(tw-ansi.StringWidth(title), 0))
		out = append(out, fmt.Sprintf("%s %s %s %s  %s", sDim.Render(fmt.Sprintf("%3d", i+1)), sFg.Render(fmt.Sprintf("%8s", hm)),
			chip, sWhite.Render(title), sDim.Render(g.ID)))
	}
	return strings.Join(out, "\n")
}

// findGlass: an id first, then a row number as --print shows it
func findGlass(gs []glass, arg string) (glass, bool) {
	for _, g := range gs {
		if g.ID == arg {
			return g, true
		}
	}
	if n, err := strconv.Atoi(arg); err == nil && n >= 1 && n <= len(gs) {
		return gs[n-1], true
	}
	return glass{}, false
}

// pickGlass: the Console when it answers, else the default browser. Only the id crosses the wire.
func pickGlass(g glass) glassPick {
	res := glassPick{ID: g.ID}
	why, tail := "Console is down", " · `command up` brings it back"
	hc := &http.Client{Timeout: 500 * time.Millisecond}
	if r, err := hc.Get(consoleURL + "glasses.json"); err == nil {
		r.Body.Close()
		body, _ := json.Marshal(map[string]string{"glass": g.ID})
		hc.Timeout = 3 * time.Second
		r, err := hc.Post(consoleURL+"show", "application/json", bytes.NewReader(body))
		if err == nil {
			defer r.Body.Close()
			if r.StatusCode == http.StatusOK {
				var j struct {
					URL string `json:"url"`
				}
				json.NewDecoder(r.Body).Decode(&j)
				res.OpenedIn, res.Target, res.Note = "console", j.URL, "opened in the Console"
				if res.Target == "" {
					res.Target = glassTarget(g)
				}
				return res
			}
			why, tail = "the Console turned the pick down", ""
			if r.StatusCode == http.StatusNotFound {
				why, tail = "the Console runs old code (no /show)", " · python _tools/console/console.py --restart"
			}
		} else {
			why, tail = "the Console did not answer", ""
		}
	}
	target := g.URL
	if _, err := os.Stat(g.File); g.Local && err == nil {
		target = g.File
	}
	res.Target = target
	if err := openDefault(target); err != nil {
		res.OpenedIn, res.Note = "none", why+" · the browser did not open: "+err.Error()
		return res
	}
	res.OpenedIn, res.Note = "browser", why+" · opened in the browser"+tail
	return res
}

// glassTarget: the path the Console frame opens, the same one its rail builds
func glassTarget(g glass) string {
	if g.Local {
		return "/glass/" + g.ID + "/" + url.PathEscape(filepath.Base(g.File))
	}
	return g.URL
}

// openDefault: cmd /c start "" "<target>", the target always quoted so cmd reads it as one word
func openDefault(target string) error {
	if target == "" || strings.ContainsAny(target, "\"\r\n") {
		return fmt.Errorf("no target to open")
	}
	if !strings.HasPrefix(target, "https://") {
		if _, err := os.Stat(target); err != nil {
			return err
		}
	}
	c := exec.Command("cmd")
	c.SysProcAttr = &syscall.SysProcAttr{CmdLine: `cmd /c start "" "` + target + `"`}
	return c.Run()
}

func glassCmd(args []string) {
	asJSON := hasFlag(args, "--json")
	if hasFlag(args, "--refresh") {
		if hasFlag(args, "--dry-run") { // the command it would run, and nothing else
			if asJSON {
				b, _ := json.MarshalIndent(map[string]string{"would_run": strings.Join(glassRefresh, " "), "cwd": root}, "", " ")
				fmt.Println(string(b))
			} else {
				fmt.Println(strings.Join(glassRefresh, " "))
			}
			return
		}
		if err := runGlassesPy(); err != nil {
			fmt.Fprintln(os.Stderr, "command glass: refresh:", err)
			os.Exit(1)
		}
	}
	raw, gs, at, err := loadGlasses()
	if err != nil {
		fmt.Fprintln(os.Stderr, "command glass:", err, "(command glass --refresh writes the list)")
		os.Exit(1)
	}
	for _, a := range args {
		if strings.HasPrefix(a, "--") {
			continue
		}
		res := glassPick{ID: a, OpenedIn: "none", Note: "no glass with that id or number · command glass --print lists them"}
		if g, ok := findGlass(gs, a); ok {
			res = pickGlass(g)
		}
		if asJSON {
			b, _ := json.MarshalIndent(res, "", " ")
			fmt.Println(string(b))
		} else {
			fmt.Println(sAccB.Render("glass "+res.ID) + sDim.Render(" · ") + res.Note)
		}
		if res.OpenedIn == "none" {
			os.Exit(1)
		}
		return
	}
	if asJSON { // glasses.json as glasses.py wrote it
		fmt.Println(string(raw))
		return
	}
	if hasFlag(args, "--print") { // the list once, no pager
		fmt.Println(sAccB.Render("◆ GLASSES") + "  " + sDim.Render(glassSummary(gs, at)))
		fmt.Println(glassBody(gs, 100))
		return
	}
	p := &pager{title: "glasses", note: glassSummary(gs, at)}
	p.render = func(_ int, width int) string { return glassBody(gs, width) }
	p.pick = func(i int) {
		if i < len(gs) {
			p.note = pickGlass(gs[i]).Note
		}
	}
	p.reload = func() {
		if err := runGlassesPy(); err != nil {
			p.note = "refresh failed: " + err.Error()
			return
		}
		if _, ng, nat, err := loadGlasses(); err == nil {
			gs, at = ng, nat
			p.note = "refreshed · " + glassSummary(gs, at)
		}
	}
	if err := runPager(p); err != nil { // no terminal: print the list
		fmt.Println(glassBody(gs, 100))
	}
}
