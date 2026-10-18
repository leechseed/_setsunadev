// command: the Command's terminal front end (BOLO 153, Chief 10/18 "go": Go + the Charm kit).
//
//	command up      boot the whole architecture from a shell: VS Code on the repo, then the launch sequence
//	                (stations, JUDY, the Console as the viewer), drawn live as the boot screen with the
//	                spinning mark and the fetch panel; it holds on "press SPACE to continue"
//	command fetch   the mark and the fetch panel, printed once (neofetch for the Command)
//
// Python stays the engine: launch.py runs the stations and writes boot.jsonl; this program only draws it.
// Build: see build.cmd beside this file.
package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"io"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"time"

	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
	"github.com/charmbracelet/x/ansi"
)

var root = `C:\Users\U01_LEECHSEED\Desktop\_setsunadev` // set at build time with -ldflags "-X main.root=..."

func init() {
	if r := os.Getenv("COMMAND_ROOT"); r != "" {
		root = r
	}
}

type event struct {
	T       float64  `json:"t"`
	State   string   `json:"state"`
	Station string   `json:"station"`
	Go      bool     `json:"go"`
	Note    string   `json:"note"`
	Waves   []string `json:"waves"`
	Sub     []string `json:"sub"`
}

var early = [][2]string{
	{":: running early hook", "[udev]"}, {":: running hook", "[keymap]"}, {":: mounting", "'/dev/q' on real root"},
	{":: loading", "the Command · SOP · BOLO · STATE"}, {":: starting", "systemd-launch (BOLO 58)"},
}

type tickMsg time.Time
type launchDone struct{ err error }

type model struct {
	w, h       int
	start      time.Time
	startEpoch float64
	spin       *spinner
	fetch      [][2]string
	lines      []string // finished lines: the early hooks, then one per station (plus its sub lines)
	earlyShown int
	running    string
	runSince   time.Time
	frame      int
	ok, bad    int
	ended      bool
	launchErr  error
	events     string // path to boot.jsonl
	offset     int64
	partial    string
	logPath    string
}

func stamp(sec float64) string { return sDim.Render(fmt.Sprintf("[%8.3f]", sec)) }

func pad(s string, n int) string {
	if len(s) >= n {
		return s
	}
	return s + strings.Repeat(" ", n-len(s))
}

func stationLine(e event, sec float64) []string {
	tag, verdict := sOK.Render("[  OK  ]"), sOK.Render("GO    ")
	if !e.Go {
		tag, verdict = sBad.Render("[FAILED]"), sBad.Render("NO-GO ")
	}
	note := e.Note
	if len(e.Waves) > 0 {
		note = fmt.Sprintf("%d waves open", len(e.Waves))
	}
	if len(note) > 52 {
		note = note[:52]
	}
	out := []string{fmt.Sprintf("%s %s %s %s %s %s", stamp(sec), tag, sWhite.Render(pad(e.Station, 10)),
		sDim.Render(strings.Repeat(".", 30)), verdict, sDim.Render(note))}
	for _, s := range e.Sub {
		out = append(out, "           "+sDim.Render("└─ "+trunc(s, 92)))
	}
	for _, wv := range e.Waves {
		st := sOK
		if strings.Contains(wv, "STALLED") {
			st = sBad
		}
		out = append(out, "           "+sDim.Render("└─ ")+st.Render(trunc(wv, 90)))
	}
	return out
}

func trunc(s string, n int) string {
	r := []rune(s)
	if len(r) > n {
		return string(r[:n])
	}
	return s
}

func tick() tea.Cmd {
	return tea.Tick(50*time.Millisecond, func(t time.Time) tea.Msg { return tickMsg(t) })
}

func (m *model) Init() tea.Cmd { return tick() }

// readEvents takes the new whole lines of boot.jsonl; events older than this run are the last launch's, skipped
func (m *model) readEvents() {
	f, err := os.Open(m.events)
	if err != nil {
		return
	}
	defer f.Close()
	if st, err := f.Stat(); err == nil && st.Size() < m.offset {
		m.offset, m.partial = 0, "" // the launch truncated the file: start over
	}
	f.Seek(m.offset, io.SeekStart)
	b, _ := io.ReadAll(f)
	m.offset += int64(len(b))
	chunk := m.partial + string(b)
	parts := strings.Split(chunk, "\n")
	m.partial = parts[len(parts)-1]
	for _, l := range parts[:len(parts)-1] {
		var e event
		if json.Unmarshal([]byte(strings.TrimSpace(l)), &e) != nil || e.T < m.startEpoch-2 {
			continue
		}
		switch e.State {
		case "start":
			m.running, m.runSince = e.Station, time.Now()
		case "done":
			if e.Go {
				m.ok++
			} else {
				m.bad++
			}
			m.lines = append(m.lines, stationLine(e, e.T-m.startEpoch)...)
			m.running = ""
		case "end":
			m.ended = true
		}
	}
}

func (m *model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.WindowSizeMsg:
		m.w, m.h = msg.Width, msg.Height
	case tea.KeyMsg:
		switch msg.String() {
		case "ctrl+c":
			return m, tea.Quit
		case " ", "enter":
			if m.ended || m.launchErr != nil {
				return m, tea.Quit
			}
		}
	case launchDone:
		m.readEvents()
		if !m.ended {
			m.launchErr = msg.err
			if m.launchErr == nil {
				m.launchErr = fmt.Errorf("the launch ended without its last event")
			}
		}
	case tickMsg:
		m.frame++
		if m.earlyShown < len(early) && m.frame%2 == 0 {
			e := early[m.earlyShown]
			m.lines = append(m.lines, fmt.Sprintf("%s %s %s", stamp(0.12*float64(m.earlyShown+1)), sAcc.Render(e[0]), sFg.Render(e[1])))
			m.earlyShown++
			if m.earlyShown == len(early) {
				m.lines = append(m.lines, "")
			}
		} else if m.earlyShown == len(early) {
			m.readEvents()
		}
		return m, tick()
	}
	return m, nil
}

func (m *model) hero(still bool) string {
	shown := -1
	if !still {
		shown = 2 + m.frame/2 // the panel types in, two ticks a line
	}
	logo := m.spin.frame(time.Now(), still)
	return lipgloss.JoinHorizontal(lipgloss.Center, logo, "    ", fetchBlock(m.fetch, shown))
}

func banner() string {
	return sAccB.Render("        B  O  L  D  V  E  N  T  U  R  E") + "\n" +
		sDim.Render("   ── the Command · launch sequence "+strings.Repeat("─", 22))
}

func (m *model) tail() []string {
	out := append([]string{}, m.lines...)
	if m.running != "" {
		n := int(time.Since(m.runSince).Milliseconds()/80) % 30
		spin := string("|/-\\"[m.frame%4])
		out = append(out, fmt.Sprintf("%s %s %s %s", stamp(float64(time.Now().UnixNano())/1e9-m.startEpoch),
			sAmber.Render("[  "+spin+"   ]"), sWhite.Render(pad(m.running, 10)), sDim.Render(strings.Repeat(".", n+1))))
	}
	switch {
	case m.launchErr != nil:
		out = append(out, "", sBad.Render("  launch stopped: "+m.launchErr.Error()), sDim.Render("  its output: "+m.logPath), "", sAccB.Render("  press SPACE to continue"))
	case m.ended:
		if m.bad > 0 {
			out = append(out, "", sBad.Render(fmt.Sprintf("  %d NO-GO", m.bad))+sDim.Render(" · ")+sOK.Render(fmt.Sprintf("%d GO", m.ok))+sDim.Render(" · the sit rep carries the details"))
		} else {
			out = append(out, "", sOK.Render("  Reached target ")+sAccB.Render("The Command")+sOK.Render(fmt.Sprintf(".  ALL GO (%d)", m.ok)))
		}
		if (m.frame/10)%2 == 0 { // the blink
			out = append(out, "", sAccB.Render("  press SPACE to continue"))
		} else {
			out = append(out, "", "")
		}
	}
	return out
}

func (m *model) View() string {
	top := m.hero(false) + "\n\n" + banner() + "\n"
	room := m.h - lipgloss.Height(top) - 1
	body := m.tail()
	if room > 0 && len(body) > room {
		body = body[len(body)-room:]
	}
	var b strings.Builder
	b.WriteString(top)
	for _, l := range body {
		b.WriteString("\n" + ansi.Truncate(l, max(m.w, 20), ""))
	}
	return b.String()
}

// pickScale fits the mark into about 45% of the terminal height
func pickScale(art []string, h int) int {
	if h <= 0 {
		h = 40
	}
	for s := 2; s < 8; s++ {
		if (len(art)+s-1)/s <= int(float64(h)*0.45) {
			return s
		}
	}
	return 8
}

func termHeight() int {
	if _, h, err := termSize(); err == nil {
		return h
	}
	return 40
}

func up() {
	art := loadArt(filepath.Join(root, "_tools", "brand", "boldventure-ascii.txt"))
	m := &model{start: time.Now(), events: filepath.Join(root, "_tools", "launch", "boot.jsonl"), fetch: fetchRows()}
	m.startEpoch = float64(m.start.UnixNano()) / 1e9
	m.spin = newSpinner(shrink(art, pickScale(art, termHeight())))

	// VS Code on the repo (an open window just gets focus), then the launch sequence
	exec.Command("cmd", "/c", "code", root).Start()
	m.logPath = filepath.Join(root, "_tools", "cmdtui", "last_up.log")
	logf, _ := os.Create(m.logPath)
	launch := exec.Command("python", "-X", "utf8", filepath.Join(root, "_tools", "launch", "launch.py"))
	launch.Dir = root
	launch.Stdout, launch.Stderr = logf, logf

	p := tea.NewProgram(m, tea.WithAltScreen())
	if err := launch.Start(); err != nil {
		m.launchErr = err
	} else {
		go func() { err := launch.Wait(); logf.Close(); p.Send(launchDone{err}) }()
	}
	if _, err := p.Run(); err != nil {
		fmt.Fprintln(os.Stderr, "command up:", err)
		os.Exit(1)
	}
	// leave the board in the scrollback, the way neofetch does
	fmt.Println(m.hero(true))
	fmt.Println()
	for _, l := range m.lines {
		fmt.Println(l)
	}
	if m.ended {
		fmt.Println(sDim.Render("\n  the poll and the NEXT lines: " + m.logPath))
	}
}

func fetchOnce() {
	art := loadArt(filepath.Join(root, "_tools", "brand", "boldventure-ascii.txt"))
	s := newSpinner(shrink(art, pickScale(art, termHeight())))
	fmt.Println(lipgloss.JoinHorizontal(lipgloss.Center, s.frame(time.Now(), true), "    ", fetchBlock(fetchRows(), -1)))
}

func main() {
	cmd := ""
	if len(os.Args) > 1 {
		cmd = os.Args[1]
	}
	switch cmd {
	case "up":
		up()
	case "fetch":
		fetchOnce()
	default:
		w := bufio.NewWriter(os.Stdout)
		fmt.Fprintln(w, sAccB.Render("command")+sDim.Render(" · the Command's terminal front end (BOLO 153)"))
		fmt.Fprintln(w, "  "+sAcc.Render("up   ")+"  boot the whole architecture: VS Code, the stations, JUDY, the Console")
		fmt.Fprintln(w, "  "+sAcc.Render("fetch")+"  the mark and the numbers, neofetch style")
		w.Flush()
	}
}
