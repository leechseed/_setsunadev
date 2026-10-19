package main

import "os"

func init() {
	if os.Getenv("CMD_TRY") == "push" {
		pushCmd(os.Args[1:])
		os.Exit(0)
	}
}
