@echo off
rem build.cmd: rebuild the command binary into %USERPROFILE%\go\bin, which is on PATH. BOLO 153, 10/18.
rem wake.exe is the same program under the go code "Wake Up, Neo." (Chief 10/19): it boots like command up.
cd /d "%~dp0"
go build -o "%USERPROFILE%\go\bin\command.exe" . && copy /y "%USERPROFILE%\go\bin\command.exe" "%USERPROFILE%\go\bin\wake.exe" >nul && echo built command.exe + wake.exe
