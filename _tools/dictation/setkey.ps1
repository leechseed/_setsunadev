# setkey.ps1 — put the ElevenLabs key on the box without it touching the chat,
# the terminal scrollback, or PowerShell history.
#
#   pwsh -File _tools/dictation/setkey.ps1
#
# Reads the key as a masked prompt, checks its shape, writes it to the gitignored
# _PRIVATE/ tree, and verifies against the live API. Nothing is ever echoed.
#
# BOLO 56. This repo is PUBLIC — the key never goes in judy.json or any tracked file.

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$dir  = Join-Path $root '_PRIVATE'
$dest = Join-Path $dir 'elevenlabs.key'

Write-Host ''
Write-Host '  ElevenLabs key' -ForegroundColor White
Write-Host '  ──────────────' -ForegroundColor DarkGray
Write-Host '  Get it at elevenlabs.io → your avatar → API Keys.' -ForegroundColor Gray
Write-Host '  Copy the value that starts with ' -NoNewline -ForegroundColor Gray
Write-Host 'sk_' -NoNewline -ForegroundColor Green
Write-Host ' — NOT the key ID.' -ForegroundColor Gray
Write-Host '  It is shown only once, when the key is created or rotated.' -ForegroundColor DarkGray
Write-Host ''

$secure = Read-Host -AsSecureString '  Paste the key (input stays hidden)'
$key = [Runtime.InteropServices.Marshal]::PtrToStringBSTR(
         [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)).Trim()

if (-not $key) { Write-Host '  nothing entered — stopping.' -ForegroundColor Yellow; exit 1 }

if ($key -notlike 'sk_*') {
    Write-Host ''
    Write-Host '  ! That does not start with sk_.' -ForegroundColor Yellow
    Write-Host '    A 64-character hex string is the key ID, which the API rejects.' -ForegroundColor DarkGray
    $go = Read-Host '    Write it anyway? (y/N)'
    if ($go -ne 'y') { Write-Host '  stopped; nothing written.' -ForegroundColor Yellow; exit 1 }
}

New-Item -ItemType Directory -Force $dir | Out-Null
[IO.File]::WriteAllText($dest, $key + "`n", (New-Object Text.UTF8Encoding $false))
Write-Host ''
Write-Host "  wrote $dest ($($key.Length) chars)" -ForegroundColor Green

# Prove git cannot see it before anything else.
Push-Location $root
$ignored = (& git check-ignore _PRIVATE/elevenlabs.key) 2>$null
Pop-Location
if ($ignored) { Write-Host '  gitignored — confirmed' -ForegroundColor Green }
else { Write-Host '  ! NOT ignored by git — do not commit' -ForegroundColor Red }

Write-Host ''
Write-Host '  verifying against the API…' -ForegroundColor Gray
& python (Join-Path $PSScriptRoot 'speak.py') --list-eleven
Write-Host ''
Write-Host '  If voices listed, JUDY has a mouth. Set engine to elevenlabs in the console.' -ForegroundColor DarkGray
