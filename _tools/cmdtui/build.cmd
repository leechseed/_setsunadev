@echo off
rem build.cmd: rebuild the command binary into %USERPROFILE%\go\bin, which is on PATH. BOLO 153, 10/18.
rem wake.exe is the same program under the go code "Wake Up, Neo." (Chief 10/19): it boots like command up.
rem kenshi.exe is the same program under the go code "Kenshi Watanabi" (Chief 10/19): it starts Kenshi + RE_Kenshi.
rem engineroom.exe is the same program, opening the Engine Room in its own window (Chief 11/4).
rem fresh.exe is the same program under the go code "Fresh hour" (Chief 10/30): it builds and opens a fresh hour of BBC.
cd /d "%~dp0"
go build -o "%USERPROFILE%\go\bin\command.exe" . && copy /y "%USERPROFILE%\go\bin\command.exe" "%USERPROFILE%\go\bin\wake.exe" >nul && copy /y "%USERPROFILE%\go\bin\command.exe" "%USERPROFILE%\go\bin\kenshi.exe" >nul && copy /y "%USERPROFILE%\go\bin\command.exe" "%USERPROFILE%\go\bin\fresh.exe" >nul && copy /y "%USERPROFILE%\go\bin\command.exe" "%USERPROFILE%\go\bin\engineroom.exe" >nul && echo built command.exe + wake.exe + kenshi.exe + fresh.exe + engineroom.exe
