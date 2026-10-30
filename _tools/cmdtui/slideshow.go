package main

// slideshow.go: `command slideshow` (Chief 10/30) makes a photo slideshow from the DARKROOM corpus (default 10 minutes, 5 seconds
// a photo, no repeats across runs) as a video and opens it in a new VLC window. The engine stays Python
// (_tools/stashplay/slideshow.py); this verb passes the arguments through. --json lists the photos; --dry-run picks and prints.

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
)

func slideshowCmd(args []string) {
	script := filepath.Join(root, "_tools", "stashplay", "slideshow.py")
	if _, err := os.Stat(script); err != nil {
		fmt.Println(sOK.Render("slideshow") + sDim.Render("  slideshow.py is missing from _tools/stashplay"))
		os.Exit(1)
	}
	py := []string{"-X", "utf8", script}
	for _, a := range args {
		py = append(py, a)
	}
	c := exec.Command("python", py...)
	c.Dir = root
	c.Stdin, c.Stdout, c.Stderr = os.Stdin, os.Stdout, os.Stderr
	if err := c.Run(); err != nil {
		os.Exit(1)
	}
}
