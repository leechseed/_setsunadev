@echo off
rem view.cmd — open a house page in a lightweight Edge app window (no Firefox, no tab bar).
rem
rem   view sitrep        the sit rep front page
rem   view soi           the SOI
rem   view 51            DOPE SHEET 51
rem   view https://...   any URL
rem
rem Names resolve through pages.json beside this file. Edge is already resident in Windows
rem (WebView2), so an --app window costs one process, not a browser session. Coded 2026-09-12, BOLO 51.
setlocal
set "HERE=%~dp0"
set "TARGET=%~1"
if "%TARGET%"=="" ( echo usage: view sitrep ^| soi ^| ^<bolo n^> ^| ^<url^> & exit /b 2 )
echo %TARGET% | findstr /b /i "http" >nul
if not errorlevel 1 goto open
for /f "usebackq delims=" %%U in (`powershell -NoProfile -Command "(Get-Content -Raw '%HERE%pages.json' | ConvertFrom-Json).'%TARGET%'"`) do set "URL=%%U"
if "%URL%"=="" ( echo no page named "%TARGET%" in pages.json & exit /b 1 )
set "TARGET=%URL%"
:open
set "EDGE=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"
if not exist "%EDGE%" set "EDGE=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
start "" "%EDGE%" --app=%TARGET% --window-size=1480,940
endlocal
