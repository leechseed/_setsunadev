package main

// The pager every reading view shares (BOLO 153, 10/19): a framed strip on top with the tabs, a scrolling body
// (bubbles' viewport), a key line at the bottom. command md and command board both ride on it.

import (
	"fmt"
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
}

var (
	sTabOn  = lipgloss.NewStyle().Foreground(lipgloss.Color("#050608")).Background(cAcc).Bold(true).Padding(0, 1)
	sTabOff = lipgloss.NewStyle().Foreground(cDim).Padding(0, 1)
)

func (p *pager) Init() tea.Cmd { return nil }

func (p *pager) load() {
	body := p.render(p.tab, p.w-2)
	p.vp.SetContent(body)
	p.vp.GotoTop()
	p.marks = p.marks[:0]
	for i, l := range strings.Split(body, "\n") {
		t := strings.TrimSpace(ansi.Strip(l))
		if strings.HasPrefix(t, "#") || strings.HasPrefix(t, "──") {
			p.marks = append(p.marks, i)
		}
	}
}

func (p *pager) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
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
	if len(p.tabs) > 1 {
		keys = "←/→ or 1-" + fmt.Sprint(len(p.tabs)) + " tab · " + keys
	}
	foot := sDim.Render(keys) + "  " + sAcc.Render(fmt.Sprintf("%3.0f%%", p.vp.ScrollPercent()*100))
	return ansi.Truncate(head, p.w, "") + "\n" + rule + "\n" + p.vp.View() + "\n" + ansi.Truncate(foot, p.w, "")
}

func runPager(p *pager) error {
	_, err := tea.NewProgram(p, tea.WithAltScreen(), tea.WithMouseCellMotion()).Run()
	return err
}
