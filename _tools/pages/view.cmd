@echo off
rem view.cmd — open a Command page as a normal tab in the default browser (Chief, 9/20: no more Edge --app windows; they read as a desktop app).
rem
rem   view sitrep        the sit rep front page
rem   view soi           the SOI
rem   view 51            DOPE SHEET 51
rem   view https://...   any URL
rem
rem Names resolve through pages.json beside this file. Coded 2026-09-12, BOLO 51; browser tab since 2026-09-20.
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
rem the default browser, a normal tab. The Edge --app window (9/12–9/19) is retired by Chief's word 9/20.
start "" "%TARGET%"
endlocal
