package main

// kenshi.go: the go code "Kenshi Watanabi" (Chief 10/19) sets up the AI and starts Kenshi.
// Steps: (1) Ollama server up, (2) the model is pulled, (3) the model is loaded into memory, (4) Sentient Sands points at it,
// (5) Kenshi starts through Steam. RE_Kenshi 0.3.5 is patched into kenshi_x64.exe (there is no RE_Kenshi.exe to run),
// so Steam's own launch loads it. The shell runs kenshi.exe (a copy of this program); `command kenshi` does the same.

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"regexp"
	"strings"
	"syscall"
	"time"
)

const (
	kenshiDir   = `H:\SteamLibrary\steamapps\common\Kenshi`
	modDir      = `H:\SteamLibrary\steamapps\workshop\content\233860\3675880187`
	kenshiURI   = "steam://rungameid/233860"
	ollamaURL   = "http://localhost:11434"
	ollamaModel = "qwen2.5:14b"        // what Ollama calls it
	modModel    = "ollama-qwen2.5-14b" // what Sentient Sands calls it (models.json key, ini currentmodel)
)

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

type step struct {
	Name string `json:"step"`
	OK   bool   `json:"ok"`
	Note string `json:"note"`
}

func ollamaTags() ([]string, bool) {
	c := http.Client{Timeout: 2 * time.Second}
	resp, err := c.Get(ollamaURL + "/api/tags")
	if err != nil {
		return nil, false
	}
	defer resp.Body.Close()
	var d struct {
		Models []struct{ Name string } `json:"models"`
	}
	if json.NewDecoder(resp.Body).Decode(&d) != nil {
		return nil, false
	}
	var names []string
	for _, m := range d.Models {
		names = append(names, m.Name)
	}
	return names, true
}

func ollamaExe() string {
	if p, err := exec.LookPath("ollama"); err == nil {
		return p
	}
	return filepath.Join(os.Getenv("LOCALAPPDATA"), "Programs", "Ollama", "ollama.exe")
}

// stepOllama: the server answers on :11434; if not, start `ollama serve` detached and wait up to 30 s.
func stepOllama(dry bool) step {
	if _, up := ollamaTags(); up {
		return step{"ollama server", true, "already up on :11434"}
	}
	exe := ollamaExe()
	if _, err := os.Stat(exe); err != nil {
		return step{"ollama server", false, "ollama.exe not found"}
	}
	if dry {
		return step{"ollama server", true, "down; would start " + exe}
	}
	cmd := exec.Command(exe, "serve")
	// 8192 tokens of context is plenty for the mod's prompts and keeps the 14B model near 10 GB of video memory,
	// which leaves room for Kenshi (3 GB) and JUDY (2 GB) on the 24 GB card. Ollama's own default can grow the cache to ~14 GB.
	cmd.Env = append(os.Environ(), "OLLAMA_CONTEXT_LENGTH=8192")
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true, CreationFlags: 0x00000008 | 0x00000200} // DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP: it outlives this window
	if err := cmd.Start(); err != nil {
		return step{"ollama server", false, "start failed: " + err.Error()}
	}
	t0 := time.Now()
	for time.Since(t0) < 30*time.Second {
		time.Sleep(500 * time.Millisecond)
		if _, up := ollamaTags(); up {
			return step{"ollama server", true, fmt.Sprintf("started · %.1f s", time.Since(t0).Seconds())}
		}
	}
	return step{"ollama server", false, "no answer after 30 s"}
}

// stepPulled: the model is in Ollama's list. A pull is gigabytes, so this only reports; it never downloads on its own.
func stepPulled() step {
	names, up := ollamaTags()
	if !up {
		return step{"model pulled", false, "ollama is not answering"}
	}
	for _, n := range names {
		if n == ollamaModel {
			return step{"model pulled", true, ollamaModel}
		}
	}
	return step{"model pulled", false, ollamaModel + " is not pulled; run: ollama pull " + ollamaModel}
}

// stepLoaded: ask Ollama to load the model and keep it for 4 hours, so the first NPC line is not a 30 s wait.
func stepLoaded() step {
	body, _ := json.Marshal(map[string]any{"model": ollamaModel, "keep_alive": "4h"})
	c := http.Client{Timeout: 180 * time.Second}
	t0 := time.Now()
	resp, err := c.Post(ollamaURL+"/api/generate", "application/json", bytes.NewReader(body))
	if err != nil {
		return step{"model loaded", false, err.Error()}
	}
	defer resp.Body.Close()
	io.Copy(io.Discard, resp.Body)
	if resp.StatusCode != 200 {
		return step{"model loaded", false, fmt.Sprintf("ollama answered %d", resp.StatusCode)}
	}
	return step{"model loaded", true, fmt.Sprintf("in memory for 4 h · %.1f s", time.Since(t0).Seconds())}
}

// stepMod: models.json holds the model and the ini selects it. A Steam workshop update can undo both, so the launch repairs them.
func stepMod(dry bool) step {
	mp := filepath.Join(modDir, "server", "config", "models.json")
	ip := filepath.Join(modDir, "SentientSands_Config.ini")
	var fixed []string
	raw, err := os.ReadFile(mp)
	if err != nil {
		return step{"sentient sands", false, "models.json not found"}
	}
	var models map[string]any
	if json.Unmarshal(raw, &models) != nil {
		return step{"sentient sands", false, "models.json does not parse"}
	}
	if _, ok := models[modModel]; !ok {
		fixed = append(fixed, "added "+modModel+" to models.json")
		if !dry {
			models[modModel] = map[string]string{"provider": "ollama", "model": ollamaModel}
			out, _ := json.MarshalIndent(models, "", "    ")
			if err := os.WriteFile(mp, append(out, '\n'), 0o644); err != nil {
				return step{"sentient sands", false, "could not write models.json: " + err.Error()}
			}
		}
	}
	ini, err := os.ReadFile(ip)
	if err != nil {
		return step{"sentient sands", false, "SentientSands_Config.ini not found"}
	}
	re := regexp.MustCompile(`(?m)^currentmodel\s*=\s*(.*?)\s*$`)
	if m := re.FindSubmatch(ini); m == nil || string(m[1]) != modModel {
		fixed = append(fixed, "set currentmodel = "+modModel)
		if !dry {
			var out []byte
			if m == nil {
				out = append(ini, []byte("\r\ncurrentmodel = "+modModel+"\r\n")...)
			} else {
				out = re.ReplaceAll(ini, []byte("currentmodel = "+modModel))
			}
			if err := os.WriteFile(ip, out, 0o644); err != nil {
				return step{"sentient sands", false, "could not write the ini: " + err.Error()}
			}
		}
	}
	if len(fixed) == 0 {
		return step{"sentient sands", true, "already set to " + modModel}
	}
	return step{"sentient sands", true, strings.Join(fixed, " · ")}
}

// kenshiCmd: --json prints the steps, --dry-run changes nothing, --no-game sets up the AI and stops short of Kenshi,
// --no-warm skips loading the model into memory (a 14B model shares video memory with the game). words=false means no go code.
func kenshiCmd(args []string, words bool) {
	_, exeErr := os.Stat(kenshiDir + `\kenshi_x64.exe`)
	_, dllErr := os.Stat(kenshiDir + `\RE_Kenshi.dll`)
	dry, asJSON := hasFlag(args, "--dry-run"), hasFlag(args, "--json")
	if exeErr != nil || dllErr != nil {
		fmt.Println(sBad.Render("Kenshi or RE_Kenshi.dll not found in " + kenshiDir))
		os.Exit(1)
	}
	if !words && !asJSON {
		fmt.Println(sAccB.Render("kenshi") + sDim.Render("  say the go code: kenshi watanabi  (--dry-run checks · --no-game sets up the AI only · --no-warm skips loading the model · --json)"))
		return
	}
	if !words {
		dry = true // --json without the go code only reports
	}
	var steps []step
	emit := func(s step) bool {
		steps = append(steps, s)
		if !asJSON {
			mark := sOK.Render("✓")
			if !s.OK {
				mark = sBad.Render("✗")
			}
			fmt.Printf("  %s %-15s %s\n", mark, s.Name, sDim.Render(s.Note))
		}
		return s.OK
	}
	if !asJSON {
		fmt.Println(sAccB.Render("Kenshi Watanabi") + sDim.Render("  · AI first, then the game"))
	}
	aiOK := emit(stepOllama(dry))
	if aiOK {
		aiOK = emit(stepPulled())
	}
	if aiOK && !dry && !hasFlag(args, "--no-warm") {
		emit(stepLoaded()) // a slow load does not stop the game; the mod retries the call
	}
	emit(stepMod(dry))
	launch := words && !dry && !hasFlag(args, "--no-game")
	if launch {
		if !aiOK && !asJSON {
			fmt.Println(sBad.Render("  the AI is not ready; starting Kenshi anyway (the mod will report it in debug.log)"))
		}
		if err := exec.Command("cmd", "/c", "start", "", kenshiURI).Start(); err != nil {
			emit(step{"kenshi", false, "launch failed: " + err.Error()})
		} else {
			emit(step{"kenshi", true, "started through Steam; tick Sentient Sands and KenshiLib in the launcher"})
		}
	} else {
		emit(step{"kenshi", true, "not started (" + map[bool]string{true: "dry run", false: "--no-game"}[dry] + ")"})
	}
	if asJSON {
		b, _ := json.MarshalIndent(map[string]any{"steps": steps, "uri": kenshiURI, "launched": launch, "dry_run": dry}, "", " ")
		fmt.Println(string(b))
	}
	for _, s := range steps {
		if !s.OK && s.Name == "kenshi" {
			os.Exit(1)
		}
	}
}
