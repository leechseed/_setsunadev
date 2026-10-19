package main

// command board: the newest sit rep board (the JSON the sit rep skill writes) in the terminal, one tab per block:
// Last session · Fresh Ten · Ancients · BOLO board · Blocked on you · the leverage line. --json prints the board.

import (
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"sort"
	"strings"

	"github.com/charmbracelet/lipgloss"
)

type bItem struct {
	T       string `json:"t"`
	Trunk   string `json:"trunk"`
	S       string `json:"s"`
	When    string `json:"when"`
	N       any    `json:"n"`
	Title   string `json:"title"`
	What    string `json:"what"`
	Unblock string `json:"unblocks"`
}

type bBlock struct {
	ID     string `json:"id"`
	Name   string `json:"name"`
	Plain  string `json:"plain"`
	Items  []bItem
	Groups []struct {
		Label string  `json:"label"`
		Items []bItem `json:"items"`
	} `json:"groups"`
	Line string `json:"line"`
	Why  string `json:"why"`
	Pmcs []struct {
		Item   string `json:"item"`
		S      string `json:"s"`
		Status string `json:"status"`
		Next   string `json:"next"`
	} `json:"pmcs"`
	Strand struct {
		Next string `json:"next"`
	} `json:"strand"`
}

type board struct {
	Meta struct {
		When    string   `json:"when"`
		Trigger string   `json:"trigger"`
		Stats   []string `json:"stats"`
	} `json:"meta"`
	Blocks []bBlock `json:"blocks"`
}

func (b *bBlock) UnmarshalJSON(data []byte) error { // items carry a mixed shape (Block V uses n/title/what)
	type alias bBlock
	var a alias
	if err := json.Unmarshal(data, &a); err != nil {
		return err
	}
	var raw struct {
		Items []bItem `json:"items"`
	}
	json.Unmarshal(data, &raw)
	a.Items = raw.Items
	*b = bBlock(a)
	return nil
}

var (
	reBold  = regexp.MustCompile(`\*\*(.+?)\*\*`)
	reLink  = regexp.MustCompile(`\[\[[^\]|]+\|([^\]]+)\]\]|\[\[([^\]]+)\]\]`)
	reTick  = regexp.MustCompile("`([^`]+)`")
	chipSty = map[string]lipgloss.Style{
		"hot": sAccB, "open": sAmber, "held": sAmber, "gated": sDim, "parked": sDim,
		"done": sOK, "ruled": sOK, "good": sOK, "bad": sBad, "missing": sBad,
	}
)

// inline: the board's light markdown (**bold**, `code`, [[key|label]]) as terminal styles
func inline(s string) string {
	s = reLink.ReplaceAllStringFunc(s, func(m string) string {
		p := reLink.FindStringSubmatch(m)
		if p[1] != "" {
			return p[1]
		}
		return p[2]
	})
	s = reTick.ReplaceAllStringFunc(s, func(m string) string { return sAmber.Render(reTick.FindStringSubmatch(m)[1]) })
	return reBold.ReplaceAllStringFunc(s, func(m string) string { return sAccB.Render(reBold.FindStringSubmatch(m)[1]) })
}

func chip(s string) string {
	if s == "" {
		return ""
	}
	st, ok := chipSty[s]
	if !ok {
		st = sDim
	}
	return st.Render("[" + s + "]")
}

func itemLines(it bItem, width int) string {
	text := it.T
	if text == "" && it.Title != "" {
		text = fmt.Sprintf("**%v · %s**: %s", it.N, it.Title, it.What)
		if it.Unblock != "" {
			text += " → unblocks " + it.Unblock
		}
	}
	meta := strings.TrimSpace(chip(it.S) + " " + sDim.Render(strings.TrimSpace(it.Trunk+" "+it.When)))
	body := lipgloss.NewStyle().Width(max(width-4, 30)).Render(inline(text))
	return "  " + meta + "\n" + indent(body, "    ")
}

func indent(s, pre string) string {
	ls := strings.Split(s, "\n")
	for i := range ls {
		ls[i] = pre + ls[i]
	}
	return strings.Join(ls, "\n")
}

func boardCmd(args []string) {
	files, _ := filepath.Glob(filepath.Join(root, "_tools", "sitrep", "boards", "*.json"))
	if len(files) == 0 {
		fmt.Fprintln(os.Stderr, "command board: no board yet (say sit rep)")
		os.Exit(1)
	}
	sort.Slice(files, func(i, j int) bool {
		a, _ := os.Stat(files[i])
		b, _ := os.Stat(files[j])
		return a.ModTime().Before(b.ModTime())
	})
	raw, err := os.ReadFile(files[len(files)-1])
	if err != nil {
		fmt.Fprintln(os.Stderr, "command board:", err)
		os.Exit(1)
	}
	if hasFlag(args, "--json") {
		fmt.Println(string(raw))
		return
	}
	var bd board
	if err := json.Unmarshal(raw, &bd); err != nil {
		fmt.Fprintln(os.Stderr, "command board:", err)
		os.Exit(1)
	}
	want := []string{"0", "I", "II", "IV", "V", "VI"}
	names := map[string]string{"0": "Last session", "I": "Fresh Ten", "II": "Ancients", "IV": "BOLO board", "V": "Blocked", "VI": "Leverage"}
	var blocks []bBlock
	var tabs []string
	for _, id := range want {
		for _, b := range bd.Blocks {
			if b.ID == id {
				blocks = append(blocks, b)
				tabs = append(tabs, names[id])
			}
		}
	}
	render := func(tab, width int) string {
		b := blocks[tab]
		var out []string
		out = append(out, sAccB.Render("BLOCK "+b.ID+" · "+strings.ToUpper(b.Name))+sDim.Render("   board "+bd.Meta.When+" · "+bd.Meta.Trigger), "")
		out = append(out, lipgloss.NewStyle().Width(max(width-2, 30)).Foreground(cFg).Render(inline(b.Plain)), "")
		if b.Line != "" {
			out = append(out, sAccB.Render("▶ ")+lipgloss.NewStyle().Width(max(width-4, 30)).Render(inline(b.Line)), "", sDim.Render("why  ")+inline(b.Why), "")
		}
		for _, it := range b.Items {
			out = append(out, itemLines(it, width), "")
		}
		for _, g := range b.Groups {
			out = append(out, sAcc.Render(fmt.Sprintf("── %s (%d)", g.Label, len(g.Items))), "")
			for _, it := range g.Items {
				out = append(out, itemLines(it, width), "")
			}
		}
		if len(b.Pmcs) > 0 {
			out = append(out, sAcc.Render("── PMCS"), "")
			for _, p := range b.Pmcs {
				out = append(out, "  "+chip(p.S)+" "+sWhite.Render(p.Item)+sDim.Render(" · ")+inline(p.Status), "")
			}
		}
		if len(b.Items) == 0 && len(b.Groups) == 0 && b.Line == "" {
			out = append(out, sDim.Render("  nothing on this block"))
		}
		if b.Strand.Next != "" {
			out = append(out, sDim.Render("next  ")+inline(b.Strand.Next))
		}
		return strings.Join(out, "\n")
	}
	if hasFlag(args, "--print") { // every tab printed once, no pager (pipes, scripts, the done check)
		for i := range blocks {
			fmt.Println(render(i, 100) + "\n")
		}
		return
	}
	if err := runPager(&pager{title: "the board", tabs: tabs, render: render}); err != nil {
		for i := range blocks { // no terminal: print every tab
			fmt.Println(render(i, 100))
		}
	}
}
