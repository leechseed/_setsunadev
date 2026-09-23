@echo off
rem The second concurrent session runs in its own git worktree (BOLO 64 fix, 9/23; docs: claude --worktree).
rem Usage: second.cmd [name]   default name = side-<yyyymmdd>. Merge its branch back before Oscar Mike on the main session.
cd /d c:\Users\U01_LEECHSEED\Desktop\_setsunadev
set NAME=%1
if "%NAME%"=="" set NAME=side-%date:~-4%%date:~4,2%%date:~7,2%
claude --worktree %NAME%
