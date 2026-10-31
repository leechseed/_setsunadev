@echo off
rem downloads.cmd: the DOWNLOADS station's tab (BOLO 166). launch.py hands this file to Windows Terminal as its
rem whole command: wt.exe folds any command with arguments into one program name and fails 0x80070002 (10/24,
rem 10/30, 10/31), while one bare file path runs. Chief's setup (10/31): PowerShell 7 (x86) in Downloads,
rem running ytdlp_go.py; -NoExit keeps the tab up if the script ends.
cd /d "%USERPROFILE%\Downloads"
set "PWSH=C:\Program Files (x86)\PowerShell\7\pwsh.exe"
if not exist "%PWSH%" set "PWSH=pwsh"
"%PWSH%" -NoExit -Command "python ytdlp_go.py"
