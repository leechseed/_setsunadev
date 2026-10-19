package main

// command push: the one road up to origin (BOLO 153, 10/19). A checklist in order: Hold · Branch · Fetch · Status ·
// Ahead/behind · Commits · Diffstat · Diff · Audit · Hold gate · Verdict; then Chief types push at his terminal.
// The hold file fails closed and only Chief clears it; the push never forces. --dry-run, --print and --json never
// fetch, never prompt, never push. Exit: 0 pushed or nothing to push · 1 error · 2 held · 3 audit finding ·
// 4 off main, behind origin, no terminal, or not confirmed.

import (
	"bufio"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"os/exec"
	"path"
	"path/filepath"
	"regexp"
	"strconv"
	"strings"
	"time"

	"github.com/charmbracelet/lipgloss"
	"github.com/charmbracelet/x/ansi"
	"github.com/charmbracelet/x/term"
)

const (
	pushRange   = "origin/main..HEAD"
	pushCommand = "git push origin HEAD:main"  // the only push this verb runs; never --force
	hunkLook    = "hunk diff origin/main HEAD" // hunk 0.23: "hunk diff <from> <to>" compares two revisions
	pushDiffCap = 3000                         // lines one file tab shows
	pushTabCap  = 40                           // file tabs; the files tab lists the rest
)

type pushHold struct {
	Held   bool   `json:"held"`
	Since  string `json:"since"`
	Reason string `json:"reason"`
	FileOK bool   `json:"file_ok"`
}

type pushCommit struct {
	SHA     string `json:"sha"`
	When    string `json:"when"`
	Subject string `json:"subject"`
}

type pushItem struct {
	File string `json:"file"`
	Line int    `json:"line"`
	Kind string `json:"kind"` // P: private detail on an added line · _PRIVATE: a path under _PRIVATE/
}

type pushAudit struct {
	Ran          bool       `json:"ran"`
	Findings     int        `json:"findings"`
	PrivatePaths int        `json:"private_paths"`
	Items        []pushItem `json:"items"`
	Error        string     `json:"error,omitempty"`
}

type pushReport struct {
	Hold     pushHold     `json:"hold"`
	Branch   string       `json:"branch"`
	Upstream string       `json:"upstream"`
	Fetched  bool         `json:"fetched"`
	Ahead    int          `json:"ahead"`
	Behind   int          `json:"behind"`
	Commits  []pushCommit `json:"commits"`
	Dirty    []string     `json:"dirty"`
	Diffstat struct {
		Files      int `json:"files"`
		Insertions int `json:"insertions"`
		Deletions  int `json:"deletions"`
	} `json:"diffstat"`
	Audit pushAudit `json:"audit"`
	Hunk  struct {
		Found bool   `json:"found"`
		Path  string `json:"path"`
	} `json:"hunk"`
	Verdict  string `json:"verdict"` // held · blocked · behind · nothing · ready · unconfirmed · pushed · error
	Why      string `json:"why"`
	Exit     int    `json:"exit"`
	WouldRun string `json:"would_run"`
}

type pushFlow struct {
	r     pushReport
	quiet bool // --json: no checklist, the report at the end
	dry   bool // --dry-run, --print, --json: no fetch, no confirm, no push
	look  bool // open the diff look: a terminal, and no --print, --json or --no-diff
	width int
}

var (
	pushOK   = sOK.Render("✓")
	pushNo   = sBad.Render("✗")
	pushNote = sAmber.Render("!")
	pushSkip = sDim.Render("·")

	sDiffAdd  = lipgloss.NewStyle().Foreground(cOK)
	sDiffDel  = lipgloss.NewStyle().Foreground(cBad)
	sDiffHunk = lipgloss.NewStyle().Foreground(cCyan)

	reShortstat = regexp.MustCompile(`(\d+) (file|insertion|deletion)`)
)

// pushGit: one git call in the repo; the error carries git's first stderr line
func pushGit(args ...string) (string, error) {
	c := exec.Command("git", append([]string{"-c", "core.quotepath=off"}, args...)...)
	c.Dir = root
	out, err := c.Output()
	if err != nil {
		var ee *exec.ExitError
		if errors.As(err, &ee) {
			if l := strings.TrimSpace(strings.SplitN(strings.TrimSpace(string(ee.Stderr)), "\n", 2)[0]); l != "" {
				return "", errors.New(l)
			}
		}
		return "", err
	}
	return strings.TrimRight(string(out), "\r\n"), nil
}

// readHold: _tools/release/hold.json; a missing file, bad JSON, or anything but "held": false counts as held
func readHold() pushHold {
	raw, err := os.ReadFile(filepath.Join(root, "_tools", "release", "hold.json"))
	var f struct {
		Held   *bool  `json:"held"`
		Since  string `json:"since"`
		Reason string `json:"reason"`
	}
	if err != nil || json.Unmarshal(raw, &f) != nil || f.Held == nil {
		return pushHold{Held: true, Reason: "the hold file is missing or does not parse, so it counts as held"}
	}
	h := pushHold{Held: *f.Held, Since: f.Since, Reason: f.Reason, FileOK: true}
	if h.Held && h.Reason == "" {
		h.Reason = "held; the file gives no reason"
	}
	return h
}

func pushTTY() bool { return term.IsTerminal(os.Stdin.Fd()) && term.IsTerminal(os.Stdout.Fd()) }

// pushAuditRun: sop_audit.py --diff over the outgoing range (the engine; that mode writes nothing)
func pushAuditRun() (pushAudit, error) {
	a := pushAudit{Items: []pushItem{}}
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Minute)
	defer cancel()
	c := exec.CommandContext(ctx, "python", "-X", "utf8", filepath.Join(root, "_tools", "audit", "sop_audit.py"), "--diff", pushRange, "--json")
	c.Dir = root
	out, err := c.Output()
	if ctx.Err() == context.DeadlineExceeded {
		return a, errors.New("sop_audit.py ran past 2 min")
	}
	if jerr := json.Unmarshal(out, &a); jerr != nil {
		if err != nil {
			return a, fmt.Errorf("sop_audit.py: %v", err)
		}
		return a, fmt.Errorf("sop_audit.py's JSON did not parse: %v", jerr)
	}
	if !a.Ran {
		if a.Error == "" {
			a.Error = "sop_audit.py did not run"
		}
		return a, errors.New(a.Error)
	}
	if a.Items == nil {
		a.Items = []pushItem{}
	}
	return a, nil
}

// row: one checklist line; a long detail wraps under itself
func (f *pushFlow) row(mark, label, detail string) {
	if !f.quiet {
		ls := strings.Split(ansi.Wordwrap(detail, max(f.width-18, 30), ""), "\n")
		fmt.Println("  " + mark + " " + sWhite.Render(pad(label, 13)) + ls[0])
		for _, l := range ls[1:] {
			f.sub(l)
		}
	}
}

func (f *pushFlow) sub(s string) {
	if !f.quiet {
		fmt.Println(strings.Repeat(" ", 18) + s)
	}
}

func (f *pushFlow) stop(code int, verdict, why string) {
	f.r.Exit, f.r.Verdict, f.r.Why = code, verdict, why
}

// run: push_flow steps 1-11, in order; every refusal stops the flow with its exit code
func (f *pushFlow) run() {
	r := &f.r

	// 1 Hold: read first and shown on top; the flow keeps going so the look still works
	r.Hold = readHold()
	if !f.quiet {
		fmt.Println(sAccB.Render("◆ PUSH") + sDim.Render(" · "+pushCommand+" · every check runs in order"))
		if r.Hold.Held {
			fmt.Println(indent(ansi.Wordwrap(sBad.Render("[HELD]")+" "+sFg.Render(r.Hold.Reason), f.width-2, ""), "  "))
		}
		fmt.Println()
	}
	switch {
	case !r.Hold.FileOK:
		f.row(pushNo, "Hold", sFg.Render("held: the file is missing or does not parse")+sDim.Render(" · fails closed"))
	case r.Hold.Held:
		f.row(pushNo, "Hold", sFg.Render("held since "+r.Hold.Since)+sDim.Render(" · only Chief clears _tools/release/hold.json"))
	default:
		f.row(pushOK, "Hold", sFg.Render("clear"))
	}

	// 2 Branch: main, tracking origin/main
	br, err := pushGit("symbolic-ref", "--short", "-q", "HEAD")
	if err != nil || br == "" {
		f.row(pushNo, "Branch", sFg.Render("HEAD is detached"))
		f.stop(4, "blocked", "HEAD is detached; check out main first")
		return
	}
	up, _ := pushGit("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
	r.Branch, r.Upstream = br, up
	if br != "main" || up != "origin/main" {
		why := "on " + br + ", not main"
		if br == "main" && up == "" {
			why = "main has no upstream; it must track origin/main"
		} else if br == "main" {
			why = "main tracks " + up + ", not origin/main"
		}
		f.row(pushNo, "Branch", sFg.Render(why))
		f.stop(4, "blocked", why)
		return
	}
	f.row(pushOK, "Branch", sFg.Render("main → origin/main"))

	// 3 Fetch: a real run brings origin/main up to date; the dry run reads the last-known one
	if f.dry {
		f.row(pushSkip, "Fetch", sDim.Render("skipped (dry run): uses the last-known origin/main"))
	} else {
		if _, err := pushGit("fetch", "origin", "main"); err != nil {
			f.row(pushNo, "Fetch", sFg.Render(err.Error()))
			f.stop(1, "error", "git fetch origin main: "+err.Error())
			return
		}
		r.Fetched = true
		f.row(pushOK, "Fetch", sFg.Render("origin/main is current"))
	}

	// 4 Status: a push sends commits only, so uncommitted files are a note
	st, err := pushGit("status", "--porcelain=v1", "--branch")
	if err != nil {
		f.row(pushNo, "Status", sFg.Render(err.Error()))
		f.stop(1, "error", "git status: "+err.Error())
		return
	}
	for _, l := range strings.Split(st, "\n") {
		if len(l) > 3 && !strings.HasPrefix(l, "##") {
			r.Dirty = append(r.Dirty, l[3:])
		}
	}
	if len(r.Dirty) == 0 {
		f.row(pushOK, "Status", sFg.Render("clean"))
	} else {
		f.row(pushNote, "Status", sFg.Render(fmt.Sprintf("%d uncommitted", len(r.Dirty)))+sDim.Render(" · a push sends commits only; these stay here"))
		for i, d := range r.Dirty {
			if i == 5 {
				f.sub(sDim.Render(fmt.Sprintf("+%d more", len(r.Dirty)-5)))
				break
			}
			f.sub(sDim.Render(d))
		}
	}

	// 5 Ahead/behind: nothing ahead is nothing to push; anything behind is a refusal, never a force
	if _, err := pushGit("rev-parse", "--verify", "-q", "origin/main"); err != nil {
		f.row(pushNo, "Ahead/behind", sFg.Render("no origin/main ref in this clone"))
		f.stop(1, "error", "no origin/main ref; a real run fetches it")
		return
	}
	ab, err := pushGit("rev-list", "--left-right", "--count", "origin/main...HEAD")
	n := strings.Fields(ab)
	if err != nil || len(n) != 2 {
		f.row(pushNo, "Ahead/behind", sFg.Render("git rev-list gave no count"))
		f.stop(1, "error", "git rev-list --left-right --count gave no count")
		return
	}
	r.Behind, _ = strconv.Atoi(n[0])
	r.Ahead, _ = strconv.Atoi(n[1])
	count := sFg.Render(fmt.Sprintf("%d ahead · %d behind", r.Ahead, r.Behind))
	switch {
	case r.Ahead == 0:
		f.row(pushOK, "Ahead/behind", count+sDim.Render(" · nothing to push"))
		f.stop(0, "nothing", "origin/main already holds every commit")
		return
	case r.Behind > 0:
		f.row(pushNo, "Ahead/behind", count+sDim.Render(" · origin has commits this clone lacks"))
		f.stop(4, "behind", fmt.Sprintf("origin/main has %d commits this clone lacks; pull them first (the verb never forces)", r.Behind))
		return
	}
	f.row(pushOK, "Ahead/behind", count)

	// 6 Commits, then the totals
	lg, err := pushGit("log", "--format=%H%x09%ct%x09%s", pushRange)
	if err != nil {
		f.row(pushNo, "Commits", sFg.Render(err.Error()))
		f.stop(1, "error", "git log: "+err.Error())
		return
	}
	for _, l := range strings.Split(lg, "\n") {
		if p := strings.SplitN(l, "\t", 3); len(p) == 3 {
			ct, _ := strconv.ParseInt(p[1], 10, 64)
			r.Commits = append(r.Commits, pushCommit{SHA: p[0], When: time.Unix(ct, 0).Format("Jan 2, 3:04 PM"), Subject: p[2]})
		}
	}
	f.row(pushSkip, "Commits", sFg.Render(fmt.Sprintf("%d outgoing", len(r.Commits)))+sDim.Render(", newest first"))
	for i, c := range r.Commits {
		if i == 12 {
			f.sub(sDim.Render(fmt.Sprintf("+%d more · git log %s", len(r.Commits)-12, pushRange)))
			break
		}
		f.sub(sAcc.Render(c.SHA[:min(8, len(c.SHA))]) + "  " + sDim.Render(pad(c.When, 16)) + "  " + sFg.Render(trunc(c.Subject, max(f.width-46, 20))))
	}
	ss, err := pushGit("diff", "--shortstat", pushRange)
	if err != nil {
		f.row(pushNo, "Diffstat", sFg.Render(err.Error()))
		f.stop(1, "error", "git diff --shortstat: "+err.Error())
		return
	}
	for _, m := range reShortstat.FindAllStringSubmatch(ss, -1) {
		v, _ := strconv.Atoi(m[1])
		switch m[2] {
		case "file":
			r.Diffstat.Files = v
		case "insertion":
			r.Diffstat.Insertions = v
		case "deletion":
			r.Diffstat.Deletions = v
		}
	}
	f.row(pushSkip, "Diffstat", sFg.Render(comma(r.Diffstat.Files)+" files · ")+sDiffAdd.Render("+"+comma(r.Diffstat.Insertions))+" "+
		sDiffDel.Render("−"+comma(r.Diffstat.Deletions)))

	// 7 Diff look: hunk when it is on PATH, else the shared pager over git diff
	if hp, err := exec.LookPath(strings.Fields(hunkLook)[0]); err == nil {
		r.Hunk.Found, r.Hunk.Path = true, hp
	}
	how := hunkLook
	if !r.Hunk.Found {
		how = "the pager over git diff " + pushRange
	}
	switch {
	case !f.look:
		f.row(pushSkip, "Diff", sFg.Render(how))
		f.sub(sDim.Render("not opened: no terminal, or --print, --json, --no-diff"))
	case r.Hunk.Found:
		f.row(pushSkip, "Diff", sFg.Render(hunkLook)+sDim.Render(" · quitting hunk comes back here"))
		c := exec.Command(r.Hunk.Path, strings.Fields(hunkLook)[1:]...)
		c.Dir, c.Stdin, c.Stdout, c.Stderr = root, os.Stdin, os.Stdout, os.Stderr
		var ee *exec.ExitError
		if err := c.Run(); errors.As(err, &ee) {
			f.row(pushNote, "Diff", sFg.Render(fmt.Sprintf("hunk exited with code %d", ee.ExitCode())))
		} else if err != nil { // hunk did not start: the pager instead
			f.row(pushNote, "Diff", sFg.Render("hunk did not start: "+err.Error())+sDim.Render(" · the pager instead"))
			if err := pushPager(); err != nil {
				f.row(pushNote, "Diff", sFg.Render("the pager did not open: "+err.Error()))
			}
		}
	default:
		f.row(pushSkip, "Diff", sFg.Render(how)+sDim.Render(" · hunk is not on PATH"))
		if err := pushPager(); err != nil {
			f.row(pushNote, "Diff", sFg.Render("the pager did not open: "+err.Error()))
		}
	}

	// 8 Audit: the outgoing diff against the private patterns; a finding or a _PRIVATE/ path stops the push
	a, err := pushAuditRun()
	r.Audit = a
	if err != nil {
		r.Audit.Ran, r.Audit.Error = false, err.Error()
		f.row(pushNo, "Audit", sFg.Render("did not run: "+err.Error()))
		f.stop(1, "error", "the audit did not run, so nothing goes up")
		return
	}
	if a.Findings > 0 || a.PrivatePaths > 0 {
		f.row(pushNo, "Audit", sBad.Render(fmt.Sprintf("%d findings · %d _PRIVATE paths", a.Findings, a.PrivatePaths))+
			sDim.Render(" · file:line only; the words stay out of the terminal"))
		for i, it := range a.Items {
			if i == 12 {
				f.sub(sDim.Render(fmt.Sprintf("+%d more · sop_audit.py --diff %s", len(a.Items)-12, pushRange)))
				break
			}
			f.sub(sFg.Render(fmt.Sprintf("%s:%d", it.File, it.Line)) + sDim.Render(" "+it.Kind))
		}
		f.stop(3, "blocked", "the audit found private detail in the outgoing diff")
		return
	}
	f.row(pushOK, "Audit", sFg.Render("clean")+sDim.Render(" · 0 findings · 0 _PRIVATE paths · a regex minimum, not the sanitizer"))

	// 9 Hold gate
	if r.Hold.Held {
		f.row(pushNo, "Hold gate", sFg.Render(r.Hold.Reason))
		f.stop(2, "held", "the hold is on; only Chief clears _tools/release/hold.json")
		return
	}
	f.row(pushOK, "Hold gate", sFg.Render("clear"))

	// 10 Confirm: a terminal, and Chief types push
	if f.dry {
		f.stop(0, "ready", "every check passed; the dry run stops before the confirm")
		return
	}
	if !pushTTY() {
		f.row(pushNo, "Confirm", sFg.Render("no terminal"))
		f.stop(4, "unconfirmed", "the confirm needs a terminal and Chief at the keys")
		return
	}
	fmt.Print("  " + sAccB.Render("?") + " " + sWhite.Render(pad("Confirm", 13)) + sFg.Render(fmt.Sprintf("type push to send %d commits to origin/main: ", r.Ahead)))
	line, _ := bufio.NewReader(os.Stdin).ReadString('\n')
	if strings.TrimSpace(line) != "push" {
		f.stop(4, "unconfirmed", "not confirmed; nothing went up")
		return
	}
	if readHold().Held { // one last read: the file can change while the diff is open
		f.stop(2, "held", "the hold came back on before the push")
		return
	}

	// 11 Push: no --force, then one line in the push log
	from, _ := pushGit("rev-parse", "origin/main")
	to, _ := pushGit("rev-parse", "HEAD")
	p := strings.Fields(pushCommand)
	c := exec.Command(p[0], p[1:]...)
	c.Dir, c.Stdout, c.Stderr = root, os.Stdout, os.Stderr
	if err := c.Run(); err != nil {
		f.stop(1, "error", "git push failed: "+err.Error())
		return
	}
	if err := pushLog(from, to, len(r.Commits)); err != nil {
		f.row(pushNote, "Log", sFg.Render("pushed, but pushes.jsonl did not take the line: "+err.Error()))
	}
	f.stop(0, "pushed", fmt.Sprintf("%d commits up to origin/main", len(r.Commits)))
}

// pushLog: one line in _tools/release/pushes.jsonl, after a real push only (24-hour, like every log)
func pushLog(from, to string, n int) error {
	b, _ := json.Marshal(struct {
		When    string `json:"when"`
		From    string `json:"from"`
		To      string `json:"to"`
		Commits int    `json:"commits"`
		Audit   string `json:"audit"`
	}{time.Now().Format("2006-01-02 15:04"), from, to, n, "clean"})
	fl, err := os.OpenFile(filepath.Join(root, "_tools", "release", "pushes.jsonl"), os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0o644)
	if err != nil {
		return err
	}
	defer fl.Close()
	_, err = fl.Write(append(b, '\n'))
	return err
}

// pushPager: the outgoing diff on the shared pager when hunk is not here
func pushPager() error {
	p, err := pushDiffPager()
	if err != nil {
		return err
	}
	return runPager(p)
}

// pushDiffPager: a files tab, then one tab per file (pushTabCap at most), each drawn the first time it shows
func pushDiffPager() (*pager, error) {
	ns, err := pushGit("diff", "--numstat", "--no-renames", pushRange)
	if err != nil {
		return nil, err
	}
	type nfile struct{ add, del, path string }
	var files []nfile
	for _, l := range strings.Split(ns, "\n") {
		if p := strings.SplitN(l, "\t", 3); len(p) == 3 {
			files = append(files, nfile{p[0], p[1], p[2]})
		}
	}
	tabs := []string{"files"}
	for i, fl := range files {
		if i == pushTabCap {
			break
		}
		tabs = append(tabs, trunc(path.Base(fl.path), 18))
	}
	raw := map[int]string{}
	render := func(tab, width int) string {
		if tab == 0 {
			out := []string{sAccB.Render(fmt.Sprintf("── %d FILES · %s", len(files), pushRange)), ""}
			for i, fl := range files {
				num := sDim.Render(fmt.Sprintf("%3d ", i+2))
				if i >= pushTabCap {
					num = "    "
				}
				out = append(out, "  "+num+sDiffAdd.Render(fmt.Sprintf("%7s", "+"+fl.add))+" "+sDiffDel.Render(fmt.Sprintf("%7s", "−"+fl.del))+"  "+
					sFg.Render(ansi.Truncate(fl.path, max(width-24, 20), "…")))
			}
			if len(files) > pushTabCap {
				out = append(out, "", sDim.Render(fmt.Sprintf("  past the first %d files there is no tab: git diff %s -- <path>", pushTabCap, pushRange)))
			}
			return strings.Join(out, "\n")
		}
		fl := files[tab-1]
		d, ok := raw[tab]
		if !ok {
			var err error
			if d, err = pushGit("diff", "--no-color", "--no-ext-diff", "--no-renames", pushRange, "--", fl.path); err != nil {
				d = "git diff: " + err.Error()
			}
			raw[tab] = d
		}
		return pushDiffBody(fl.path, d, width)
	}
	return &pager{title: "push · outgoing", tabs: tabs, render: render}, nil
}

// pushDiffBody: one file's diff in git's colors, taken from theme.go; each @@ opens a section, so n/N step the hunks
func pushDiffBody(file, d string, width int) string {
	out := []string{sAccB.Render(file)}
	ls := strings.Split(d, "\n")
	cut := len(ls) - pushDiffCap
	if cut > 0 {
		ls = ls[:pushDiffCap]
	}
	head := true
	for _, l := range ls {
		l = strings.ReplaceAll(strings.TrimRight(l, "\r"), "\t", "    ")
		st := sFg
		switch {
		case strings.HasPrefix(l, "diff --git "):
			head = true
			continue
		case strings.HasPrefix(l, "@@"):
			head = false
			out = append(out, "", sDiffHunk.Render(ansi.Truncate("── "+l, width, "…")))
			continue
		case head:
			st = sDim
		case strings.HasPrefix(l, "+"):
			st = sDiffAdd
		case strings.HasPrefix(l, "-"):
			st = sDiffDel
		case strings.HasPrefix(l, `\`):
			st = sDim
		}
		out = append(out, st.Render(ansi.Truncate(l, width, "…")))
	}
	if cut > 0 {
		out = append(out, "", sDim.Render(fmt.Sprintf("  %s more lines cut here · git diff %s -- %s shows the rest", comma(cut), pushRange, file)))
	}
	return strings.Join(out, "\n")
}

func pushCmd(args []string) {
	for _, a := range args {
		switch a {
		case "--json", "--print", "--dry-run", "--no-diff":
		case "-h", "--help":
			fmt.Println(sAccB.Render("command push") + sDim.Render(" [--dry-run] [--print] [--json] [--no-diff]"))
			fmt.Println(sDim.Render("  the checks in order, the diff look, the audit and the hold; then Chief types push. It never forces."))
			return
		default:
			fmt.Fprintln(os.Stderr, "command push: unknown flag "+a+" (it takes --dry-run, --print, --json, --no-diff; it never forces)")
			os.Exit(1)
		}
	}
	asJSON, asPrint := hasFlag(args, "--json"), hasFlag(args, "--print")
	f := &pushFlow{quiet: asJSON, dry: asJSON || asPrint || hasFlag(args, "--dry-run"), width: 100}
	f.look = !asJSON && !asPrint && !hasFlag(args, "--no-diff") && pushTTY()
	if w, _, err := termSize(); err == nil && w > 40 {
		f.width = min(w, 100)
	}
	f.r.Commits, f.r.Dirty, f.r.Audit.Items, f.r.WouldRun = []pushCommit{}, []string{}, []pushItem{}, pushCommand
	f.run()
	if f.quiet {
		b, _ := json.MarshalIndent(f.r, "", " ")
		fmt.Println(string(b))
	} else {
		mark := pushNo
		if f.r.Exit == 0 {
			mark = pushOK
		}
		f.row(mark, "Verdict", sAccB.Render(strings.ToUpper(f.r.Verdict))+sDim.Render(fmt.Sprintf(" · exit %d · ", f.r.Exit))+sFg.Render(f.r.Why))
		if f.dry {
			f.sub(sDim.Render("would run ") + sAmber.Render(pushCommand) + sDim.Render(" · nothing was fetched, pushed or logged"))
		}
	}
	if asPrint && f.r.Exit != 1 { // --print only draws the look; the run, --dry-run and --json carry the gate's code
		return
	}
	os.Exit(f.r.Exit)
}
