package main

// intro.go: the opening of The Matrix, before wake boots (Chief 10/31: "have that enter in the console just like it
// did in the matrix before it does the whole start up sequence"). A black screen, green text typed one key at a
// time under a blinking block cursor, the screen cleared between lines; "Knock, knock, Neo." lands all at once.
// Any key skips to the boot; Ctrl+C quits without booting.

import (
	"math/rand"
	"time"

	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
)

var (
	cMatrix     = lipgloss.Color("#3BFF5B")
	cBlack      = lipgloss.Color("#000000")
	sMatrix     = lipgloss.NewStyle().Foreground(cMatrix).Background(cBlack).Bold(true)
	mxLines     = []string{"Wake up, Neo...", "The Matrix has you...", "Follow the white rabbit.", "Knock, knock, Neo."}
	mxAllAtOnce = 3 // the last line is not typed: it is just there, as in the film
)

const (
	mxTyping = iota
	mxHold
	mxBlank
)

type mxStep struct{}

func mxAfter(ms int) tea.Cmd {
	return tea.Tick(time.Duration(ms)*time.Millisecond, func(time.Time) tea.Msg { return mxStep{} })
}

type matrixModel struct {
	w, h          int
	line, shown   int
	phase, left   int
	cursor        bool
	quit, aborted bool
}

func (m *matrixModel) Init() tea.Cmd { return mxAfter(900) } // a beat of black and the cursor first

func (m *matrixModel) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.WindowSizeMsg:
		m.w, m.h = msg.Width, msg.Height
	case tea.KeyMsg:
		m.aborted = msg.String() == "ctrl+c"
		m.quit = true
		return m, tea.Quit
	case mxStep:
		switch m.phase {
		case mxTyping:
			text := []rune(mxLines[m.line])
			if m.line == mxAllAtOnce {
				m.shown, m.phase, m.left, m.cursor = len(text), mxHold, 6, true
				return m, mxAfter(500)
			}
			if m.shown < len(text) {
				m.shown++
				m.cursor = true
				ms := 70 + rand.Intn(110) // a person at a keyboard, not a printer
				if r := text[m.shown-1]; r == ',' || r == '.' {
					ms += 140
				}
				return m, mxAfter(ms)
			}
			m.phase, m.left = mxHold, 5
			return m, mxAfter(450)
		case mxHold:
			m.cursor = !m.cursor
			if m.left--; m.left <= 0 {
				m.phase, m.cursor = mxBlank, true
				return m, mxAfter(500)
			}
			return m, mxAfter(450)
		case mxBlank:
			m.line++
			m.shown = 0
			if m.line == len(mxLines) {
				m.quit = true
				return m, tea.Quit
			}
			m.phase = mxTyping
			return m, mxAfter(250)
		}
	}
	return m, nil
}

func (m *matrixModel) View() string {
	if m.quit {
		return ""
	}
	text := ""
	if m.phase != mxBlank && m.line < len(mxLines) {
		text = string([]rune(mxLines[m.line])[:m.shown])
	}
	cur := " "
	if m.cursor {
		cur = "█"
	}
	body := "\n" + sMatrix.Render("  "+text+cur)
	if m.w == 0 {
		return body
	}
	return lipgloss.Place(m.w, m.h, lipgloss.Left, lipgloss.Top, body, lipgloss.WithWhitespaceBackground(cBlack))
}

// matrixIntro plays the opening; false means Chief pressed Ctrl+C and the boot should not run.
func matrixIntro() bool {
	m := &matrixModel{}
	if _, err := tea.NewProgram(m, tea.WithAltScreen()).Run(); err != nil {
		return true // no terminal (a pipe): skip straight to the boot
	}
	return !m.aborted
}
