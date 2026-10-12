# ============================================
# GHOST-CRAB-V1 - PowerShell Installation Script
# Author: Ian Carter Kulani
# Version: 1.0.0
# ============================================

#Requires -RunAsAdministrator

# Set error action
$ErrorActionPreference = "Stop"

# Variables
$AppName = "GHOST-CRAB-V1"
$Version = "1.0.0"
$InstallDir = "$env:ProgramFiles\GhostCrab"
$ConfigDir = "$env:USERPROFILE\.ghost_crab_v1"

# Colors
$Red = "Red"
$Green = "Green"
$Yellow = "Yellow"
$Cyan = "Cyan"
$White = "White"

# Functions
function Write-Banner {
    Write-Host ""
    Write-Host "    ╔══════════════════════════════════════════════════════════════╗" -ForegroundColor $Red
    Write-Host "    ║                                                              ║" -ForegroundColor $Red
    Write-Host "    ║   ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗                ║" -ForegroundColor $Red
    Write-Host "    ║  ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝                ║" -ForegroundColor $Red
    Write-Host "    ║  ██║  ███╗███████║██║   ██║███████╗   ██║                   ║" -ForegroundColor $Red
    Write-Host "    ║  ██║   ██║██╔══██║██║   ██║╚════██║   ██║                   ║" -ForegroundColor $Red
    Write-Host "    ║  ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║                   ║" -ForegroundColor $Red
    Write-Host "    ║   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝                   ║" -ForegroundColor $Red
    Write-Host "    ║                                                              ║" -ForegroundColor $Red
    Write-Host "    ║              GHOST-CRAB-V1 INSTALLER v1.0.0                  ║" -ForegroundColor $Red
    Write-Host "    ║                                                              ║" -ForegroundColor $Red
    Write-Host "    ╚══════════════════════════════════════════════════════════════╝" -ForegroundColor $Red
    Write-Host ""
}

function Write-Info { param($Message) Write-Host "[INFO] " -ForegroundColor $Cyan -NoNewline; Write-Host $Message }
function Write-Success { param($Message) Write-Host "[✓] " -ForegroundColor $Green -NoNewline; Write-Host $Message }
function Write-Warning { param($Message) Write-Host "[!] " -ForegroundColor $Yellow -NoNewline; Write-Host $Message }
function Write-Error { param($Message) Write-Host "[✗] " -ForegroundColor $Red -NoNewline; Write-Host $Message }

function Test-Administrator {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Test-Python {
    Write-Info "Checking Python installation..."
    try {
        $pythonVersion = python --version 2>&1
        if ($pythonVersion -match "Python (\d+\.\d+\.\d+)") {
            $version = $matches[1]
            Write-Success "Python $version found"
            return $true
        }
    }
    catch {
        Write-Error "Python not found!"
        Write-Warning "Please install Python 3.7+ from https://python.org"
        Write-Warning "Make sure to check 'Add Python to PATH' during installation"
        return $false
    }
    return $false
}

function Test-Pip {
    Write-Info "Checking pip..."
    try {
        $pipVersion = pip --version 2>&1
        if ($pipVersion -match "pip") {
            Write-Success "pip found"
            return $true
        }
    }
    catch {
        Write-Warning "pip not found, installing..."
        python -m ensurepip --upgrade
        return $true
    }
    return $false
}

function New-Directories {
    Write-Info "Creating directories..."
    
    $dirs = @(
        $InstallDir,
        $ConfigDir,
        "$ConfigDir\payloads",
        "$ConfigDir\workspaces",
        "$ConfigDir\scans",
        "$ConfigDir\phishing_pages",
        "$ConfigDir\phishing_templates",
        "$ConfigDir\captured_credentials",
        "$ConfigDir\ssh_keys",
        "$ConfigDir\traffic_logs",
        "$ConfigDir\reports",
        "$ConfigDir\keylogs",
        "$ConfigDir\keylog_screenshots",
        "$ConfigDir\dos_logs",
        "$ConfigDir\agents",
        "$ConfigDir\c2_logs",
        "$ConfigDir\modules",
        "$ConfigDir\network_monitor",
        "$ConfigDir\keylog_exfil",
        "$ConfigDir\deployments",
        "$ConfigDir\domain_hosting",
        "$ConfigDir\reverse_engineering",
        "$ConfigDir\cracking",
        "$ConfigDir\docker_scans",
        "$ConfigDir\saas",
        "$ConfigDir\malware",
        "$ConfigDir\images"
    )
    
    foreach ($dir in $dirs) {
        if (-not (Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
    }
    
    Write-Success "Directories created"
}

function Copy-ApplicationFiles {
    Write-Info "Copying application files..."
    
    $files = @(
        "ghost_crab_v1.py",
        "requirements.txt",
        "test-commands.py",
        "health-check.py",
        ".env.example"
    )
    
    foreach ($file in $files) {
        if (Test-Path $file) {
            Copy-Item -Path $file -Destination $InstallDir -Force
        }
    }
    
    if (-not (Test-Path "$InstallDir\ghost_crab_v1.py")) {
        Write-Error "ghost_crab_v1.py not found!"
        exit 1
    }
    
    Write-Success "Application files copied"
}

function Install-PythonDependencies {
    Write-Info "Installing Python dependencies..."
    
    python -m pip install --upgrade pip setuptools wheel
    
    if (Test-Path "$InstallDir\requirements.txt") {
        python -m pip install -r "$InstallDir\requirements.txt"
    }
    else {
        Write-Warning "requirements.txt not found, installing core packages..."
        python -m pip install requests urllib3 paramiko scapy dnspython whois `
            cryptography flask flask-socketio flask-cors `
            discord.py telethon slack-sdk selenium `
            numpy pandas matplotlib seaborn `
            sqlalchemy redis pymongo `
            reportlab python-docx openpyxl `
            Pillow opencv-python `
            pynput pyperclip pyautogui mss `
            qrcode psutil colorama rich tqdm `
            beautifulsoup4 lxml pyyaml
    }
    
    Write-Success "Python dependencies installed"
}

function New-Launcher {
    Write-Info "Creating launcher..."
    
    $launcherContent = @"
@echo off
cd /d "$InstallDir"
python ghost_crab_v1.py %*
"@
    
    Set-Content -Path "$InstallDir\ghost-crab.bat" -Value $launcherContent
    
    # Add to PATH
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    if ($currentPath -notlike "*$InstallDir*") {
        [Environment]::SetEnvironmentVariable("Path", "$currentPath;$InstallDir", "Machine")
    }
    
    Write-Success "Launcher created"
}

function New-DesktopShortcut {
    Write-Info "Creating desktop shortcut..."
    
    $WScriptShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WScriptShell.CreateShortcut("$env:USERPROFILE\Desktop\GHOST-CRAB-V1.lnk")
    $Shortcut.TargetPath = "$InstallDir\ghost-crab.bat"
    $Shortcut.WorkingDirectory = $InstallDir
    $Shortcut.Description = "GHOST-CRAB-V1 Cyber Command Platform"
    $Shortcut.Save()
    
    Write-Success "Desktop shortcut created"
}

function New-StartMenuShortcut {
    Write-Info "Creating Start Menu shortcut..."
    
    $StartMenuDir = "$env:ProgramData\Microsoft\Windows\Start Menu\Programs\GhostCrab"
    if (-not (Test-Path $StartMenuDir)) {
        New-Item -ItemType Directory -Path $StartMenuDir -Force | Out-Null
    }
    
    $WScriptShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WScriptShell.CreateShortcut("$StartMenuDir\GHOST-CRAB-V1.lnk")
    $Shortcut.TargetPath = "$InstallDir\ghost-crab.bat"
    $Shortcut.WorkingDirectory = $InstallDir
    $Shortcut.Description = "GHOST-CRAB-V1 Cyber Command Platform"
    $Shortcut.Save()
    
    Write-Success "Start Menu shortcut created"
}

function Test-Installation {
    Write-Info "Verifying installation..."
    
    try {
        $result = python -c "import requests, urllib3, paramiko; print('OK')" 2>&1
        if ($result -eq "OK") {
            Write-Success "Core modules verified"
        }
    }
    catch {
        Write-Error "Core modules verification failed"
    }
    
    if (Test-Path "$InstallDir\health-check.py") {
        Push-Location $InstallDir
        python health-check.py
        Pop-Location
    }
}

function Write-Completion {
    Write-Host ""
    Write-Host "    ╔══════════════════════════════════════════════════════════════╗" -ForegroundColor $Green
    Write-Host "    ║                                                              ║" -ForegroundColor $Green
    Write-Host "    ║           ✅ INSTALLATION COMPLETE!                          ║" -ForegroundColor $Green
    Write-Host "    ║                                                              ║" -ForegroundColor $Green
    Write-Host "    ╚══════════════════════════════════════════════════════════════╝" -ForegroundColor $Green
    Write-Host ""
    Write-Host "    📁 Install Directory: " -ForegroundColor $White -NoNewline
    Write-Host $InstallDir -ForegroundColor $Cyan
    Write-Host "    📁 Config Directory: " -ForegroundColor $White -NoNewline
    Write-Host $ConfigDir -ForegroundColor $Cyan
    Write-Host ""
    Write-Host "    🚀 To run:" -ForegroundColor $White
    Write-Host "       ghost-crab.bat" -ForegroundColor $Cyan
    Write-Host "       or" -ForegroundColor $White
    Write-Host "       cd `"$InstallDir`" && python ghost_crab_v1.py" -ForegroundColor $Cyan
    Write-Host ""
    Write-Host "    📊 Web Dashboard: " -ForegroundColor $White -NoNewline
    Write-Host "http://localhost:5000" -ForegroundColor $Cyan
    Write-Host ""
    Write-Host "    ⚠️  For authorized security testing only" -ForegroundColor $Yellow
    Write-Host ""
}

# Main installation
function Main {
    Write-Banner
    
    # Check admin
    if (-not (Test-Administrator)) {
        Write-Error "This script requires administrator privileges."
        Write-Warning "Right-click and select 'Run as administrator'"
        Read-Host "Press Enter to exit"
        exit 1
    }
    
    # Check Python
    if (-not (Test-Python)) {
        Read-Host "Press Enter to exit"
        exit 1
    }
    
    # Check pip
    if (-not (Test-Pip)) {
        Read-Host "Press Enter to exit"
        exit 1
    }
    
    # Install
    New-Directories
    Copy-ApplicationFiles
    Install-PythonDependencies
    New-Launcher
    New-DesktopShortcut
    New-StartMenuShortcut
    Test-Installation
    Write-Completion
    
    Read-Host "Press Enter to exit"
}

# Run main
Main
