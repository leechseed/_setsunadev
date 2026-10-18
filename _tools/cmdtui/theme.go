package main

// The BoldVenture styleguide (Chief 10/18, lipgloss): every color the TUI draws lives here, once.
// The same palette the Console page and the boot screen wear.

import "github.com/charmbracelet/lipgloss"

var (
	cFg    = lipgloss.Color("#c6cbc8")
	cDim   = lipgloss.Color("#5f6160")
	cAcc   = lipgloss.Color("#FF5A1F") // BoldVenture orange
	cAccD  = lipgloss.Color("#6e280e")
	cAccM  = lipgloss.Color("#be4216")
	cAccH  = lipgloss.Color("#FFB08F")
	cOK    = lipgloss.Color("#4ec96f")
	cBad   = lipgloss.Color("#e5604d")
	cAmber = lipgloss.Color("#e3b341")
	cCyan  = lipgloss.Color("#79dfff")
	cWhite = lipgloss.Color("#ffffff")

	sFg    = lipgloss.NewStyle().Foreground(cFg)
	sDim   = lipgloss.NewStyle().Foreground(cDim)
	sAcc   = lipgloss.NewStyle().Foreground(cAcc)
	sAccB  = lipgloss.NewStyle().Foreground(cAcc).Bold(true)
	sOK    = lipgloss.NewStyle().Foreground(cOK).Bold(true)
	sBad   = lipgloss.NewStyle().Foreground(cBad).Bold(true)
	sAmber = lipgloss.NewStyle().Foreground(cAmber).Bold(true)
	sWhite = lipgloss.NewStyle().Foreground(cWhite).Bold(true)

	// the mark's four densities, dark to hot, plus the decode noise and the glitch tear
	shade = map[byte]lipgloss.Style{
		'.': lipgloss.NewStyle().Foreground(cAccD),
		'-': lipgloss.NewStyle().Foreground(cAccM),
		'+': lipgloss.NewStyle().Foreground(cAcc),
		'#': lipgloss.NewStyle().Foreground(cAccH).Bold(true),
		'z': lipgloss.NewStyle().Foreground(cCyan),
		'g': lipgloss.NewStyle().Foreground(cWhite).Bold(true),
		'p': lipgloss.NewStyle().Foreground(cAccM),
	}

	// the neofetch swatches: the palette, dark row then light row
	swatchA = []string{"#050608", "#6e280e", "#be4216", "#FF5A1F", "#FFB08F", "#4ec96f", "#e3b341", "#79dfff"}
	swatchB = []string{"#5f6160", "#e5604d", "#ff2a6d", "#ff8f62", "#ffd2bd", "#72c79b", "#ffcf73", "#c6cbc8"}
)
