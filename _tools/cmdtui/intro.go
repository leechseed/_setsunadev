package main

// intro.go: the opening of The Matrix, before wake boots (Chief 10/31: "have that enter in the console just like it
// did in the matrix before it does the whole start up sequence"). A black screen, green text typed one key at a
// time under a blinking block cursor, the screen cleared between lines; "Knock, knock, Neo." lands all at once.
// Any key skips to the boot screen; Ctrl+C skips it too (the launch started before the intro keeps loading).

import (
	"math/rand"
	"os"
	"path/filepath"
	"syscall"
	"time"
	"unsafe"

	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
)

var (
	cMatrix = lipgloss.Color("#3BFF5B")
	cBlack  = lipgloss.Color("#000000")
	sMatrix = lipgloss.NewStyle().Foreground(cMatrix).Background(cBlack).Bold(true)
	// "Wake up, Neo." is what Chief types to start it, so the screen picks up after it (10/31)
	mxLines = []string{"The Matrix has you...", "Follow the white rabbit.", "Knock, knock, Neo."}
)

// the film's own audio under the typing (Chief 10/31): neorabbit.mp4's track, leading silence cut, as a WAV for PlaySound
func introSoundPath() string { return filepath.Join(root, "_PRIVATE", "audio", "neorabbit.wav") }

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
	skipped       bool
}

func (m *matrixModel) Init() tea.Cmd { return mxAfter(250) } // a beat of black and the cursor first

func (m *matrixModel) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.WindowSizeMsg:
		m.w, m.h = msg.Width, msg.Height
	case tea.KeyMsg:
		m.aborted = msg.String() == "ctrl+c"
		m.quit, m.skipped = true, true
		return m, tea.Quit
	case mxStep:
		switch m.phase {
		case mxTyping:
			text := []rune(mxLines[m.line])
			if m.line == len(mxLines)-1 { // the last line is not typed: it is just there, as in the film
				m.shown, m.phase, m.left, m.cursor = len(text), mxHold, 5, true
				return m, mxAfter(300)
			}
			if m.shown < len(text) {
				m.shown++
				m.cursor = true
				ms := 30 + rand.Intn(35) // a person at a keyboard, not a printer (10/31: "can it be faster?")
				if r := text[m.shown-1]; r == ',' || r == '.' {
					ms += 70
				}
				return m, mxAfter(ms)
			}
			m.phase, m.left = mxHold, 3
			return m, mxAfter(280)
		case mxHold:
			m.cursor = !m.cursor
			if m.left--; m.left <= 0 {
				m.phase, m.cursor = mxBlank, true
				return m, mxAfter(150)
			}
			return m, mxAfter(280)
		case mxBlank:
			m.line++
			m.shown = 0
			if m.line == len(mxLines) {
				m.quit = true
				return m, tea.Quit
			}
			m.phase = mxTyping
			return m, mxAfter(120)
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
	if _, err := os.Stat(introSoundPath()); err == nil {
		if s, err := syscall.UTF16PtrFromString(introSoundPath()); err == nil {
			playSound.Call(uintptr(unsafe.Pointer(s)), 0, sndFilename|sndAsync) // once, no loop
		}
	}
	started := time.Now()
	m := &matrixModel{}
	if _, err := tea.NewProgram(m, tea.WithAltScreen()).Run(); err != nil {
		musicStop()
		return true // no terminal (a pipe): skip straight to the boot
	}
	introPlayed = true
	if m.skipped {
		musicStop()
	} else if st, err := os.Stat(introSoundPath()); err == nil { // let the clip finish; the boot music waits for it
		bootMusicAt = started.Add(time.Duration(float64(st.Size()-44) / (44100 * 4) * float64(time.Second)))
	}
	return !m.aborted
}

// bootMusicAt: when the boot's music may start (after the intro's clip has played out); zero means at once.
// introPlayed: only wake's intro leads into the music; a bare `command up` boots silent.
var (
	bootMusicAt time.Time
	introPlayed bool
)
