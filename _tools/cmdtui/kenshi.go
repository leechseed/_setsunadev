package main

// kenshi.go: the go code "Kenshi Watanabi" (Chief 10/19) starts Kenshi with RE_Kenshi and the Sentient Sands mod.
// RE_Kenshi 0.3.5 is patched into kenshi_x64.exe (there is no RE_Kenshi.exe to run), so Steam's own launch loads it.
// The shell runs kenshi.exe (a copy of this program); `command kenshi` does the same. Python-free: the launch is one Steam URI.

import (
	"encoding/json"
	"fmt"
	"os"
	"os/exec"
	"strings"
)

const kenshiDir = `H:\SteamLibrary\steamapps\common\Kenshi`
const kenshiURI = "steam://rungameid/233860"

// kenshiWords: "Watanabi" (Chief's spelling) or "Watanabe", in any case and punctuation, is the go code.
func kenshiWords(args []string) bool {
	for _, a := range args {
		if strings.HasPrefix(strings.Map(func(r rune) rune {
			if r >= 'a' && r <= 'z' {
				return r
			}
			return -1
		}, strings.ToLower(a)), "watanab") {
			return true
		}
	}
	return false
}

// kenshiCmd: --json prints what it checked, --dry-run starts nothing. words=false means no go code was spoken.
func kenshiCmd(args []string, words bool) {
	_, exeErr := os.Stat(kenshiDir + `\kenshi_x64.exe`)
	_, dllErr := os.Stat(kenshiDir + `\RE_Kenshi.dll`)
	_, modErr := os.Stat(`H:\SteamLibrary\steamapps\workshop\content\233860\3675880187\SentientSands.mod`)
	ready := exeErr == nil && dllErr == nil
	dry := hasFlag(args, "--dry-run")
	if hasFlag(args, "--json") {
		b, _ := json.MarshalIndent(map[string]any{
			"game": exeErr == nil, "re_kenshi": dllErr == nil, "sentient_sands": modErr == nil,
			"uri": kenshiURI, "would_launch": ready && words, "dry_run": dry,
		}, "", " ")
		fmt.Println(string(b))
		return
	}
	if !ready {
		fmt.Println(sBad.Render("Kenshi or RE_Kenshi.dll not found in " + kenshiDir))
		os.Exit(1)
	}
	if !words {
		fmt.Println(sAccB.Render("kenshi") + sDim.Render("  say the go code: kenshi watanabi  (--dry-run checks, --json prints the check)"))
		return
	}
	fmt.Println(sOK.Render("Kenshi + RE_Kenshi") + sDim.Render(map[bool]string{true: "  · Sentient Sands present", false: "  · Sentient Sands NOT found"}[modErr == nil]))
	if dry {
		fmt.Println(sDim.Render("dry run: would open " + kenshiURI))
		return
	}
	if err := exec.Command("cmd", "/c", "start", "", kenshiURI).Start(); err != nil {
		fmt.Println(sBad.Render("launch failed: " + err.Error()))
		os.Exit(1)
	}
	fmt.Println(sDim.Render("started through Steam; tick Sentient Sands and KenshiLib in the launcher, then play"))
}
