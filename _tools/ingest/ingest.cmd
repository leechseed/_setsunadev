@echo off
rem Double-click: watch Q:\_FOOTAGE\_DROP and turn phone clips into Resolve-ready copies (Chief 10/11, "go ingest").
start "" explorer "Q:\_FOOTAGE\_DROP"
python "%~dp0ingest.py" --watch
