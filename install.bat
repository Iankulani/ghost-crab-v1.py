@echo off
REM ============================================
REM GHOST-CRAB-V1 - Windows Installation Script
REM Author: Ian Carter Kulani
REM Version: 1.0.0
REM ============================================

setlocal EnableDelayedExpansion

REM Colors (using ANSI escape codes if supported)
set "RED=[91m"
set "GREEN=[92m"
set "YELLOW=[93m"
set "CYAN=[96m"
set "WHITE=[97m"
set "RESET=[0m"

REM Variables
set "APP_NAME=GHOST-CRAB-V1"
set "VERSION=1.0.0"
set "INSTALL_DIR=%ProgramFiles%\GhostCrab"
set "CONFIG_DIR=%USERPROFILE%\.ghost_crab_v1"

REM Check for admin
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo %RED%[!] This script requires administrator privileges.%RESET%
    echo %YELLOW%Right-click and select "Run as administrator"%RESET%
    pause
    exit /b 1
)

REM Print banner
:print_banner
echo.
echo %RED%    ╔══════════════════════════════════════════════════════════════╗
echo %RED%    ║                                                              ║
echo %RED%    ║   ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗                ║
echo %RED%    ║  ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝                ║
echo %RED%    ║  ██║  ███╗███████║██║   ██║███████╗   ██║                   ║
echo %RED%    ║  ██║   ██║██╔══██║██║   ██║╚════██║   ██║                   ║
echo %RED%    ║  ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║                   ║
echo %RED%    ║   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝                   ║
echo %RED%    ║                                                              ║
echo %RED%    ║              GHOST-CRAB-V1 INSTALLER v1.0.0                  ║
echo %RED%    ║                                                              ║
echo %RED%    ╚══════════════════════════════════════════════════════════════╝
echo %RESET%

REM Check Python
:check_python
echo %CYAN%[INFO]%RESET% Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo %RED%[✗]%RESET% Python not found!
    echo %YELLOW%[!]%RESET% Please install Python 3.7+ from https://python.org
    echo %YELLOW%[!]%RESET% Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo %GREEN%[✓]%RESET% Python %PYTHON_VERSION% found

REM Check pip
:check_pip
echo %CYAN%[INFO]%RESET% Checking pip...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo %YELLOW%[!]%RESET% pip not found, installing...
    python -m ensurepip --upgrade
)
echo %GREEN%[✓]%RESET% pip found

REM Create directories
:create_dirs
echo %CYAN%[INFO]%RESET% Creating directories...

if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
if not exist "%CONFIG_DIR%" mkdir "%CONFIG_DIR%"
if not exist "%CONFIG_DIR%\payloads" mkdir "%CONFIG_DIR%\payloads"
if not exist "%CONFIG_DIR%\workspaces" mkdir "%CONFIG_DIR%\workspaces"
if not exist "%CONFIG_DIR%\scans" mkdir "%CONFIG_DIR%\scans"
if not exist "%CONFIG_DIR%\phishing_pages" mkdir "%CONFIG_DIR%\phishing_pages"
if not exist "%CONFIG_DIR%\phishing_templates" mkdir "%CONFIG_DIR%\phishing_templates"
if not exist "%CONFIG_DIR%\captured_credentials" mkdir "%CONFIG_DIR%\captured_credentials"
if not exist "%CONFIG_DIR%\ssh_keys" mkdir "%CONFIG_DIR%\ssh_keys"
if not exist "%CONFIG_DIR%\traffic_logs" mkdir "%CONFIG_DIR%\traffic_logs"
if not exist "%CONFIG_DIR%\reports" mkdir "%CONFIG_DIR%\reports"
if not exist "%CONFIG_DIR%\keylogs" mkdir "%CONFIG_DIR%\keylogs"
if not exist "%CONFIG_DIR%\keylog_screenshots" mkdir "%CONFIG_DIR%\keylog_screenshots"
if not exist "%CONFIG_DIR%\dos_logs" mkdir "%CONFIG_DIR%\dos_logs"
if not exist "%CONFIG_DIR%\agents" mkdir "%CONFIG_DIR%\agents"
if not exist "%CONFIG_DIR%\c2_logs" mkdir "%CONFIG_DIR%\c2_logs"
if not exist "%CONFIG_DIR%\modules" mkdir "%CONFIG_DIR%\modules"
if not exist "%CONFIG_DIR%\network_monitor" mkdir "%CONFIG_DIR%\network_monitor"
if not exist "%CONFIG_DIR%\keylog_exfil" mkdir "%CONFIG_DIR%\keylog_exfil"
if not exist "%CONFIG_DIR%\deployments" mkdir "%CONFIG_DIR%\deployments"
if not exist "%CONFIG_DIR%\domain_hosting" mkdir "%CONFIG_DIR%\domain_hosting"
if not exist "%CONFIG_DIR%\reverse_engineering" mkdir "%CONFIG_DIR%\reverse_engineering"
if not exist "%CONFIG_DIR%\cracking" mkdir "%CONFIG_DIR%\cracking"
if not exist "%CONFIG_DIR%\docker_scans" mkdir "%CONFIG_DIR%\docker_scans"
if not exist "%CONFIG_DIR%\saas" mkdir "%CONFIG_DIR%\saas"
if not exist "%CONFIG_DIR%\malware" mkdir "%CONFIG_DIR%\malware"
if not exist "%CONFIG_DIR%\images" mkdir "%CONFIG_DIR%\images"

echo %GREEN%[✓]%RESET% Directories created

REM Copy application files
:copy_files
echo %CYAN%[INFO]%RESET% Copying application files...

if exist "ghost_crab_v1.py" (
    copy /Y "ghost_crab_v1.py" "%INSTALL_DIR%\" >nul
) else (
    echo %RED%[✗]%RESET% ghost_crab_v1.py not found!
    pause
    exit /b 1
)

for %%f in (requirements.txt test-commands.py health-check.py .env.example) do (
    if exist "%%f" copy /Y "%%f" "%INSTALL_DIR%\" >nul
)

echo %GREEN%[✓]%RESET% Application files copied

REM Install Python dependencies
:install_deps
echo %CYAN%[INFO]%RESET% Installing Python dependencies...

python -m pip install --upgrade pip setuptools wheel

if exist "%INSTALL_DIR%\requirements.txt" (
    python -m pip install -r "%INSTALL_DIR%\requirements.txt"
) else (
    echo %YELLOW%[!]%RESET% requirements.txt not found, installing core packages...
    python -m pip install requests urllib3 paramiko scapy dnspython whois ^
        cryptography flask flask-socketio flask-cors ^
        discord.py telethon slack-sdk selenium ^
        numpy pandas matplotlib seaborn ^
        sqlalchemy redis pymongo ^
        reportlab python-docx openpyxl ^
        Pillow opencv-python ^
        pynput pyperclip pyautogui mss ^
        qrcode psutil colorama rich tqdm ^
        beautifulsoup4 lxml pyyaml
)

echo %GREEN%[✓]%RESET% Python dependencies installed

REM Create launcher
:create_launcher
echo %CYAN%[INFO]%RESET% Creating launcher...

(
echo @echo off
echo cd /d "%INSTALL_DIR%"
echo python ghost_crab_v1.py %%*
) > "%INSTALL_DIR%\ghost-crab.bat"

REM Add to PATH
setx PATH "%PATH%;%INSTALL_DIR%" /M >nul 2>&1

echo %GREEN%[✓]%RESET% Launcher created

REM Create desktop shortcut
:create_shortcut
echo %CYAN%[INFO]%RESET% Creating desktop shortcut...

powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%USERPROFILE%\Desktop\GHOST-CRAB-V1.lnk'); $SC.TargetPath = '%INSTALL_DIR%\ghost-crab.bat'; $SC.WorkingDirectory = '%INSTALL_DIR%'; $SC.Description = 'GHOST-CRAB-V1 Cyber Command Platform'; $SC.Save()"

echo %GREEN%[✓]%RESET% Desktop shortcut created

REM Verify installation
:verify
echo %CYAN%[INFO]%RESET% Verifying installation...

python -c "import requests, urllib3, paramiko" >nul 2>&1
if %errorlevel% equ 0 (
    echo %GREEN%[✓]%RESET% Core modules verified
) else (
    echo %RED%[✗]%RESET% Core modules verification failed
)

REM Completion message
:complete
echo.
echo %GREEN%    ╔══════════════════════════════════════════════════════════════╗
echo %GREEN%    ║                                                              ║
echo %GREEN%    ║           ✅ INSTALLATION COMPLETE!                          ║
echo %GREEN%    ║                                                              ║
echo %GREEN%    ╚══════════════════════════════════════════════════════════════╝
echo %RESET%
echo %WHITE%    📁 Install Directory: %CYAN%%INSTALL_DIR%%RESET%
echo %WHITE%    📁 Config Directory: %CYAN%%CONFIG_DIR%%RESET%
echo.
echo %WHITE%    🚀 To run:%RESET%
echo %CYAN%       ghost-crab.bat
echo %CYAN%       or
echo %CYAN%       cd "%INSTALL_DIR%" ^&^& python ghost_crab_v1.py%RESET%
echo.
echo %WHITE%    📊 Web Dashboard: %CYAN%http://localhost:5000%RESET%
echo.
echo %YELLOW%    ⚠️  For authorized security testing only%RESET%
echo.

pause
exit /b 0
