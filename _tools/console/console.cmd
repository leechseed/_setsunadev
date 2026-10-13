@echo off
rem The Console (BOLO 142): start the server if :8795 is down, then open the app window.
powershell -NoProfile -Command "try{(Invoke-WebRequest -UseBasicParsing -TimeoutSec 1 http://127.0.0.1:8795/panes.json)|Out-Null;exit 0}catch{exit 1}"
if errorlevel 1 (
  start "" /min python -u "%~dp0console.py"
  timeout /t 2 /nobreak >nul
)
start msedge --app=http://127.0.0.1:8795/ --window-size=1500,950
