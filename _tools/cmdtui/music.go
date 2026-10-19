package main

// The boot screen's idle music (Chief 10/19): looped from the moment the boot opens until Space.
// winmm's PlaySound, async and looping, the same call the Console's server makes.

import (
	"os"
	"path/filepath"
	"syscall"
	"unsafe"
)

var playSound = syscall.NewLazyDLL("winmm.dll").NewProc("PlaySoundW")

const (
	sndAsync    = 0x0001
	sndLoop     = 0x0008
	sndFilename = 0x00020000
)

func musicPath() string { return filepath.Join(root, "_PRIVATE", "audio", "boot-music.wav") }

func musicStart() {
	p := musicPath()
	if _, err := os.Stat(p); err != nil {
		return
	}
	s, err := syscall.UTF16PtrFromString(p)
	if err != nil {
		return
	}
	playSound.Call(uintptr(unsafe.Pointer(s)), 0, sndFilename|sndAsync|sndLoop)
}

func musicStop() { playSound.Call(0, 0, 0) }
