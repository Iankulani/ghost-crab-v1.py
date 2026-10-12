#!/usr/bin/env python3
"""
GHOST-CRAB-V1 - Requirements Checker
Validates all dependencies are installed correctly
"""

import sys
import subprocess
import importlib
import pkg_resources
from typing import List, Tuple, Dict

# ANSI Colors
class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


REQUIRED_PACKAGES = {
    # Core
    'requests': 'requests',
    'urllib3': 'urllib3',
    'paramiko': 'paramiko',
    'scapy': 'scapy',
    'dns': 'dnspython',
    'whois': 'whois',
    'cryptography': 'cryptography',
    
    # Web
    'flask': 'Flask',
    'flask_socketio': 'Flask-SocketIO',
    'flask_cors': 'Flask-CORS',
    'socketio': 'python-socketio',
    
    # Bots
    'discord': 'discord.py',
    'telethon': 'telethon',
    'slack_sdk': 'slack-sdk',
    'selenium': 'selenium',
    
    # Data
    'numpy': 'numpy',
    'pandas': 'pandas',
    'matplotlib': 'matplotlib',
    'seaborn': 'seaborn',
    
    # Database
    'sqlalchemy': 'SQLAlchemy',
    'redis': 'redis',
    'pymongo': 'pymongo',
    
    # PDF & Documents
    'reportlab': 'reportlab',
    'docx': 'python-docx',
    'openpyxl': 'openpyxl',
    
    # Images
    'PIL': 'Pillow',
    'cv2': 'opencv-python',
    
    # Keylogger
    'pynput': 'pynput',
    'pyperclip': 'pyperclip',
    'pyautogui': 'pyautogui',
    'mss': 'mss',
    
    # QR
    'qrcode': 'qrcode',
    
    # System
    'psutil': 'psutil',
    
    # Terminal
    'colorama': 'colorama',
    'rich': 'rich',
    'tqdm': 'tqdm',
    
    # Parsing
    'bs4': 'beautifulsoup4',
    'lxml': 'lxml',
    'yaml': 'PyYAML',
    
    # Testing
    'pytest': 'pytest',
    'coverage': 'coverage',
}

OPTIONAL_PACKAGES = {
    'pyinstaller': 'PyInstaller',
    'docker': 'docker',
    'boto3': 'boto3',
    'stripe': 'stripe',
    'twilio': 'twilio',
    'playwright': 'playwright',
}


def print_banner():
    """Print banner"""
    banner = f"""
{Colors.BRIGHT_RED}╔══════════════════════════════════════════════════════════════════╗
║{Colors.WHITE}          👻 GHOST-CRAB-V1 - Requirements Checker              {Colors.BRIGHT_RED}║
╠══════════════════════════════════════════════════════════════════╣
║{Colors.BRIGHT_CYAN}  Validating all dependencies for optimal functionality         {Colors.BRIGHT_RED}║
╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)


def check_package(module_name: str, package_name: str) -> Tuple[bool, str]:
    """Check if a package is installed"""
    try:
        mod = importlib.import_module(module_name)
        version = getattr(mod, '__version__', 'unknown')
        return True, version
    except ImportError:
        try:
            dist = pkg_resources.get_distribution(package_name)
            return True, dist.version
        except pkg_resources.DistributionNotFound:
            return False, "Not installed"
        except Exception as e:
            return False, str(e)


def check_python_version() -> bool:
    """Check Python version"""
    required = (3, 7)
    current = sys.version_info[:2]
    
    if current >= required:
        print(f"{Colors.BRIGHT_GREEN}✅ Python {current[0]}.{current[1]} (Required: {required[0]}.{required[1]}+){Colors.RESET}")
        return True
    else:
        print(f"{Colors.BRIGHT_RED}❌ Python {current[0]}.{current[1]} (Required: {required[0]}.{required[1]}+){Colors.RESET}")
        return False


def check_system_tools() -> Dict[str, bool]:
    """Check system tools"""
    import shutil
    
    tools = {
        'ping': 'Network diagnostics',
        'nmap': 'Port scanning',
        'curl': 'HTTP requests',
        'wget': 'File downloads',
        'nc': 'Netcat networking',
        'dig': 'DNS lookups',
        'traceroute': 'Network tracing',
        'ssh': 'SSH client',
        'whois': 'WHOIS lookups',
        'docker': 'Container management',
        'git': 'Version control',
    }
    
    results = {}
    print(f"\n{Colors.BRIGHT_CYAN}🔧 System Tools:{Colors.RESET}")
    
    for tool, description in tools.items():
        if shutil.which(tool):
            print(f"{Colors.BRIGHT_GREEN}✅ {tool:<15} - {description}{Colors.RESET}")
            results[tool] = True
        else:
            print(f"{Colors.BRIGHT_YELLOW}⚠️  {tool:<15} - {description} (not found){Colors.RESET}")
            results[tool] = False
    
    return results


def check_all_requirements() -> Tuple[int, int]:
    """Check all requirements"""
    print(f"\n{Colors.BRIGHT_CYAN}📦 Python Packages:{Colors.RESET}")
    
    installed = 0
    missing = 0
    
    for module, package in REQUIRED_PACKAGES.items():
        success, version = check_package(module, package)
        if success:
            print(f"{Colors.BRIGHT_GREEN}✅ {package:<25} v{version}{Colors.RESET}")
            installed += 1
        else:
            print(f"{Colors.BRIGHT_RED}❌ {package:<25} - {version}{Colors.RESET}")
            missing += 1
    
    return installed, missing


def check_optional_requirements():
    """Check optional requirements"""
    print(f"\n{Colors.BRIGHT_CYAN}📦 Optional Packages:{Colors.RESET}")
    
    for module, package in OPTIONAL_PACKAGES.items():
        success, version = check_package(module, package)
        if success:
            print(f"{Colors.BRIGHT_GREEN}✅ {package:<25} v{version}{Colors.RESET}")
        else:
            print(f"{Colors.BRIGHT_YELLOW}⚠️  {package:<25} - Not installed (optional){Colors.RESET}")


def generate_report(installed: int, missing: int):
    """Generate summary report"""
    total = installed + missing
    
    print(f"\n{Colors.BRIGHT_RED}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}📊 SUMMARY{Colors.RESET}")
    print(f"{Colors.BRIGHT_RED}{'='*60}{Colors.RESET}")
    
    print(f"  Total required packages: {total}")
    print(f"  {Colors.BRIGHT_GREEN}Installed: {installed}{Colors.RESET}")
    print(f"  {Colors.BRIGHT_RED}Missing: {missing}{Colors.RESET}")
    
    if missing == 0:
        print(f"\n{Colors.BRIGHT_GREEN}✅ All required packages are installed!{Colors.RESET}")
        print(f"{Colors.BRIGHT_GREEN}   GHOST-CRAB-V1 is ready to run!{Colors.RESET}")
    else:
        print(f"\n{Colors.BRIGHT_YELLOW}⚠️  {missing} package(s) missing.{Colors.RESET}")
        print(f"{Colors.WHITE}   Run: pip install -r requirements.txt{Colors.RESET}")
    
    print(f"{Colors.BRIGHT_RED}{'='*60}{Colors.RESET}")


def main():
    """Main function"""
    print_banner()
    
    print(f"{Colors.BRIGHT_CYAN}🐍 Python Environment:{Colors.RESET}")
    python_ok = check_python_version()
    print(f"  Executable: {sys.executable}")
    print(f"  Platform: {sys.platform}")
    
    system_tools = check_system_tools()
    installed, missing = check_all_requirements()
    check_optional_requirements()
    generate_report(installed, missing)
    
    # Exit code
    sys.exit(0 if missing == 0 else 1)


if __name__ == '__main__':
    main()
