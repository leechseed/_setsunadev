@echo off
rem build.cmd: rebuild the command binary into %USERPROFILE%\go\bin, which is on PATH. BOLO 153, 10/18.
cd /d "%~dp0"
go build -o "%USERPROFILE%\go\bin\command.exe" . && echo built command.exe
