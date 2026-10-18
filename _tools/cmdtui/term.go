package main

import (
	"os"

	"github.com/charmbracelet/x/term"
)

func termSize() (int, int, error) { return term.GetSize(os.Stdout.Fd()) }
