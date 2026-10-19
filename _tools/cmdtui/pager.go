package main

// The pager every reading view shares (BOLO 153, 10/19): a framed strip on top with the tabs, a scrolling body
// (bubbles' viewport), a key line at the bottom. command md and command board both ride on it.
// The cursor is optional (command glass, 10/19): with pick set, j/k step a lit row over the body lines that are
// not blank and not a section mark, Enter hands the row's number to pick, r runs reload. board and md leave it nil.

import (
	"fmt"
	"slices"
	"strings"

	"github.com/charmbracelet/bubbles/viewport"
	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
	"github.com/charmbracelet/x/ansi"
)

type pager struct {
	title  string
	tabs   []string
	tab    int
	render func(tab, width int) string // the body for a tab at a width
	vp     viewport.Model
	ready  bool
	w, h   int
	marks  []int // body lines that start a section, for n / N

	pick   func(i int) // optional: Enter hands it the cursor row; nil keeps the plain scroll
	reload func()      // optional, with pick: r runs it, then the body is drawn again
	note   string      // optional: one line beside the keys (pick and reload may set it)
	cur    int         // the cursor row
	rows   []int       // the body line of each cursor row
	lines  []string    // the body, split, so the cursor row can be lit
}

type pagerReload struct{}

var (
	sTabOn  = lipgloss.NewStyle().Foreground(lipgloss.Color("#050608")).Background(cAcc).Bold(true).Padding(0, 1)
	sTabOff = lipgloss.NewStyle().Foreground(cDim).Padding(0, 1)
	sCur    = sTabOn.Padding(0, 0) // the cursor row: dark on BoldVenture orange, like the tab that is on
)

func (p *pager) Init() tea.Cmd { return nil }

func (p *pager) load() {
	body := p.render(p.tab, p.w-2)
	p.vp.SetContent(body)
	p.vp.GotoTop()
	p.marks = p.marks[:0]
	p.rows = p.rows[:0]
	p.lines = strings.Split(body, "\n")
	for i, l := range p.lines {
		t := strings.TrimSpace(ansi.Strip(l))
		if strings.HasPrefix(t, "#") || strings.HasPrefix(t, "──") {
			p.marks = append(p.marks, i)
		} else if t != "" && p.pick != nil {
			p.rows = append(p.rows, i)
		}
	}
	if p.pick != nil {
		p.cur = min(p.cur, max(len(p.rows)-1, 0))
		p.paint()
		p.show()
	}
}

// paint: the body again with the cursor row lit
func (p *pager) paint() {
	if len(p.rows) == 0 {
		return
	}
	ls := append([]string(nil), p.lines...)
	l := ansi.Strip(ls[p.rows[p.cur]])
	ls[p.rows[p.cur]] = sCur.Render(l + strings.Repeat(" ", max(p.w-2-ansi.StringWidth(l), 0)))
	p.vp.SetContent(strings.Join(ls, "\n"))
}

// show: scroll so the cursor row is in view
func (p *pager) show() {
	if len(p.rows) == 0 {
		return
	}
	l := p.rows[p.cur]
	switch {
	case p.cur == 0:
		p.vp.GotoTop()
	case l < p.vp.YOffset:
		if slices.Contains(p.marks, l-1) { // keep the section line above the row in view
			l--
		}
		p.vp.SetYOffset(l)
	case l >= p.vp.YOffset+p.vp.Height:
		p.vp.SetYOffset(l - p.vp.Height + 1)
	}
}

// follow: after the view scrolls on its own (mouse, page keys, n/N), the cursor comes along into it
func (p *pager) follow() {
	if len(p.rows) == 0 {
		return
	}
	top, bot := p.vp.YOffset, p.vp.YOffset+p.vp.Height-1
	for p.cur > 0 && p.rows[p.cur] > bot {
		p.cur--
	}
	for p.cur < len(p.rows)-1 && p.rows[p.cur] < top {
		p.cur++
	}
	p.paint()
}

func (p *pager) move(d int) {
	if len(p.rows) == 0 {
		return
	}
	p.cur = min(max(p.cur+d, 0), len(p.rows)-1)
	p.paint()
	p.show()
}

func (p *pager) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	if p.pick != nil {
		switch msg := msg.(type) {
		case pagerReload:
			p.reload()
			p.load()
			return p, nil
		case tea.KeyMsg:
			switch msg.String() {
			case "down", "j":
				p.move(1)
				return p, nil
			case "up", "k":
				p.move(-1)
				return p, nil
			case "g", "home":
				p.move(-len(p.rows))
				return p, nil
			case "G", "end":
				p.move(len(p.rows))
				return p, nil
			case "enter":
				if len(p.rows) > 0 {
					p.pick(p.cur)
				}
				return p, nil
			case "r":
				if p.reload != nil {
					p.note = "refreshing…"
					return p, func() tea.Msg { return pagerReload{} }
				}
			}
		}
		y := p.vp.YOffset
		m, cmd := p.update(msg)
		if p.ready && p.vp.YOffset != y {
			p.follow()
		}
		return m, cmd
	}
	return p.update(msg)
}

func (p *pager) update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.WindowSizeMsg:
		p.w, p.h = msg.Width, msg.Height
		bodyH := max(p.h-4, 3)
		if !p.ready {
			p.vp = viewport.New(p.w, bodyH)
			p.ready = true
		} else {
			p.vp.Width, p.vp.Height = p.w, bodyH
		}
		p.load()
		return p, nil
	case tea.KeyMsg:
		switch msg.String() {
		case "q", "esc", "ctrl+c":
			return p, tea.Quit
		case "right", "l", "tab":
			if len(p.tabs) > 1 {
				p.tab = (p.tab + 1) % len(p.tabs)
				p.load()
			}
			return p, nil
		case "left", "h", "shift+tab":
			if len(p.tabs) > 1 {
				p.tab = (p.tab + len(p.tabs) - 1) % len(p.tabs)
				p.load()
			}
			return p, nil
		case "g", "home":
			p.vp.GotoTop()
			return p, nil
		case "G", "end":
			p.vp.GotoBottom()
			return p, nil
		case "n":
			for _, m := range p.marks {
				if m > p.vp.YOffset {
					p.vp.SetYOffset(m)
					break
				}
			}
			return p, nil
		case "N":
			for i := len(p.marks) - 1; i >= 0; i-- {
				if p.marks[i] < p.vp.YOffset {
					p.vp.SetYOffset(p.marks[i])
					break
				}
			}
			return p, nil
		}
		if len(p.tabs) > 1 && len(msg.String()) == 1 && msg.String() >= "1" && msg.String() <= "9" {
			if i := int(msg.String()[0] - '1'); i < len(p.tabs) {
				p.tab = i
				p.load()
			}
			return p, nil
		}
	}
	var cmd tea.Cmd
	p.vp, cmd = p.vp.Update(msg)
	return p, cmd
}

func (p *pager) View() string {
	if !p.ready {
		return ""
	}
	head := sAccB.Render("◆ "+strings.ToUpper(p.title)) + "  "
	for i, t := range p.tabs {
		if i == p.tab {
			head += sTabOn.Render(t)
		} else {
			head += sTabOff.Render(fmt.Sprintf("%d %s", i+1, t))
		}
	}
	rule := sDim.Render(strings.Repeat("─", max(p.w, 10)))
	keys := "j/k scroll · space page · g/G ends · n/N section · q quit"
	if p.pick != nil {
		r := ""
		if p.reload != nil {
			r = "r refresh · "
		}
		keys = "j/k move · enter open · " + r + "g/G ends · n/N section · q quit"
	}
	if len(p.tabs) > 1 {
		keys = "←/→ or 1-" + fmt.Sprint(len(p.tabs)) + " tab · " + keys
	}
	foot := sDim.Render(keys) + "  " + sAcc.Render(fmt.Sprintf("%3.0f%%", p.vp.ScrollPercent()*100))
	if p.note != "" {
		foot += "  " + sFg.Render(p.note)
	}
	return ansi.Truncate(head, p.w, "") + "\n" + rule + "\n" + p.vp.View() + "\n" + ansi.Truncate(foot, p.w, "")
}

func runPager(p *pager) error {
	_, err := tea.NewProgram(p, tea.WithAltScreen(), tea.WithMouseCellMotion()).Run()
	return err
}
