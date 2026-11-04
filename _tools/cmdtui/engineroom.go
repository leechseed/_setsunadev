package main

// engineroom.go: `command engineroom` (BOLO 180, ruled 11/4: "the Engine Room"). The whole Venture Engine, the ten SSOT
// systems; phase 1 slice one is the gate meter (BOLO 100, systems first). The engine stays Python
// (_tools/engineroom/engineroom.py); this verb passes --json / --print through and opens the page.
//   command engineroom              start the local server if it is down (127.0.0.1:8796), then open /gate in the browser
//   command engineroom --json       the gate as JSON (add --rows for every counted and dropped line)
//   command engineroom --print      the gate table, once
//   command engineroom --dry-run    say what it would start and open

import (
	"fmt"
	"net"
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"time"
)

const engineRoomURL = "http://127.0.0.1:8796/gate"

func engineroomCmd(args []string) {
	script := filepath.Join(root, "_tools", "engineroom", "engineroom.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("engineroom") + sDim.Render("  engineroom.py is missing from _tools/engineroom"))
		os.Exit(1)
	}
	if hasFlag(args, "--json") || hasFlag(args, "--print") {
		py := append([]string{"-X", "utf8", script}, args...)
		c := exec.Command("python", py...)
		c.Dir = root
		c.Stdout, c.Stderr = os.Stdout, os.Stderr
		if err := c.Run(); err != nil {
			os.Exit(1)
		}
		return
	}
	if len(args) > 0 && !hasFlag(args, "--dry-run") {
		fmt.Println(sOK.Render("engineroom") + sDim.Render("  unknown flag "+args[0]+" · --json [--rows] · --print · --dry-run"))
		os.Exit(2)
	}
	up := engineRoomUp()
	if hasFlag(args, "--dry-run") {
		if up {
			fmt.Println(sDim.Render("  the Engine Room is up · would open " + engineRoomURL))
		} else {
			fmt.Println(sDim.Render("  the Engine Room is down · would start python engineroom.py serve, then open " + engineRoomURL))
		}
		return
	}
	if !up {
		c := exec.Command("cmd", "/c", "start", "Engine Room", "/min", "python", "-X", "utf8", script, "serve")
		c.Dir = root
		if err := c.Start(); err != nil {
			fmt.Println(sDim.Render("  could not start the Engine Room: " + err.Error()))
			os.Exit(1)
		}
		for i := 0; i < 30 && !engineRoomUp(); i++ {
			time.Sleep(200 * time.Millisecond)
		}
		if !engineRoomUp() {
			fmt.Println(sDim.Render("  the Engine Room did not answer on :8796 within 6 seconds"))
			os.Exit(1)
		}
	}
	// its own app window, the way the Console opens (msedge --app); a plain browser tab if Edge will not start
	if err := exec.Command("cmd", "/c", "start", "", "msedge", "--app="+engineRoomURL, "--window-size=1400,950").Start(); err != nil {
		if err2 := exec.Command("cmd", "/c", "start", "", engineRoomURL).Start(); err2 != nil {
			fmt.Println(sDim.Render("  the Engine Room is up but no window opened: " + err2.Error()))
			os.Exit(1)
		}
	}
	fmt.Println(sDim.Render("  the Engine Room · its own window · " + engineRoomURL))
}

func engineRoomUp() bool {
	conn, err := net.DialTimeout("tcp", "127.0.0.1:8796", 300*time.Millisecond)
	if err != nil {
		return false
	}
	conn.Close()
	hc := &http.Client{Timeout: 2 * time.Second}
	r, err := hc.Get("http://127.0.0.1:8796/health")
	if err != nil {
		return false
	}
	r.Body.Close()
	return r.StatusCode == http.StatusOK
}
