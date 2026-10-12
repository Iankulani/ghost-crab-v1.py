#!/usr/bin/env python3
"""
GHOST-CRAB-V1 - Health Check Script
Validates system health and dependencies
"""

import sys
import os
import json
import socket
import subprocess
import platform
import time
import importlib
import shutil
from datetime import datetime
from pathlib import Path

# Version
VERSION = "1.0.0"

# ANSI Colors
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


class HealthCheck:
    """Health check system"""
    
    def __init__(self):
        self.checks = []
        self.results = {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'version': VERSION,
            'checks': [],
            'errors': [],
            'warnings': []
        }
    
    def add_check(self, name: str, status: str, message: str, details: dict = None):
        """Add a check result"""
        check = {
            'name': name,
            'status': status,  # 'pass', 'fail', 'warn'
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        if details:
            check['details'] = details
        
        self.results['checks'].append(check)
        
        if status == 'fail':
            self.results['errors'].append(f"{name}: {message}")
            self.results['status'] = 'unhealthy'
        elif status == 'warn':
            self.results['warnings'].append(f"{name}: {message}")
            if self.results['status'] == 'healthy':
                self.results['status'] = 'degraded'
        
        # Print result
        icon = {'pass': '✅', 'fail': '❌', 'warn': '⚠️'}[status]
        color = {'pass': Colors.GREEN, 'fail': Colors.RED, 'warn': Colors.YELLOW}[status]
        print(f"{color}{icon} {name}: {message}{Colors.RESET}")
    
    def check_python(self):
        """Check Python installation"""
        version = sys.version_info
        if version >= (3, 7):
            self.add_check(
                'Python Version',
                'pass',
                f'Python {version.major}.{version.minor}.{version.micro}',
                {'version': f"{version.major}.{version.minor}.{version.micro}"}
            )
        else:
            self.add_check(
                'Python Version',
                'fail',
                f'Python {version.major}.{version.minor} (requires 3.7+)'
            )
    
    def check_platform(self):
        """Check platform"""
        self.add_check(
            'Platform',
            'pass',
            f'{platform.system()} {platform.release()}',
            {'system': platform.system(), 'release': platform.release()}
        )
    
    def check_hostname(self):
        """Check hostname"""
        try:
            hostname = socket.gethostname()
            self.add_check('Hostname', 'pass', hostname, {'hostname': hostname})
        except Exception as e:
            self.add_check('Hostname', 'warn', str(e))
    
    def check_directories(self):
        """Check required directories"""
        required_dirs = [
            '.ghost_crab_v1',
            '.ghost_crab_v1/payloads',
            '.ghost_crab_v1/scans',
            '.ghost_crab_v1/reports',
            '.ghost_crab_v1/logs',
        ]
        
        for d in required_dirs:
            path = Path(d)
            if path.exists():
                self.add_check(f'Directory: {d}', 'pass', 'Exists')
            else:
                try:
                    path.mkdir(parents=True, exist_ok=True)
                    self.add_check(f'Directory: {d}', 'warn', 'Created')
                except Exception as e:
                    self.add_check(f'Directory: {d}', 'fail', str(e))
    
    def check_database(self):
        """Check database"""
        db_path = '.ghost_crab_v1/ghost_crab_v1.db'
        try:
            import sqlite3
            conn = sqlite3.connect(db_path)
            conn.execute('SELECT 1')
            conn.close()
            self.add_check('Database', 'pass', 'SQLite accessible')
        except Exception as e:
            self.add_check('Database', 'warn', str(e))
    
    def check_network(self):
        """Check network connectivity"""
        try:
            socket.create_connection(('8.8.8.8', 53), timeout=5)
            self.add_check('Network', 'pass', 'Internet accessible')
        except Exception as e:
            self.add_check('Network', 'warn', f'Limited connectivity: {e}')
    
    def check_ports(self):
        """Check if required ports are available"""
        ports = [5000, 8080, 4444]
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                sock.bind(('127.0.0.1', port))
                self.add_check(f'Port {port}', 'pass', 'Available')
            except OSError:
                self.add_check(f'Port {port}', 'warn', 'In use')
            finally:
                sock.close()
    
    def check_system_tools(self):
        """Check system tools"""
        tools = {
            'nmap': 'Port scanning',
            'curl': 'HTTP requests',
            'wget': 'File downloads',
            'nc': 'Netcat',
            'dig': 'DNS lookups',
            'ssh': 'SSH client',
        }
        
        for tool, desc in tools.items():
            if shutil.which(tool):
                self.add_check(f'Tool: {tool}', 'pass', desc)
            else:
                self.add_check(f'Tool: {tool}', 'warn', f'Not found - {desc}')
    
    def check_python_modules(self):
        """Check required Python modules"""
        modules = [
            ('requests', 'HTTP library'),
            ('urllib3', 'HTTP library'),
            ('paramiko', 'SSH library'),
            ('flask', 'Web framework'),
            ('psutil', 'System monitoring'),
            ('cryptography', 'Encryption'),
        ]
        
        for module, desc in modules:
            try:
                importlib.import_module(module)
                self.add_check(f'Module: {module}', 'pass', desc)
            except ImportError:
                self.add_check(f'Module: {module}', 'warn', f'Not installed - {desc}')
    
    def check_memory(self):
        """Check memory"""
        try:
            import psutil
            mem = psutil.virtual_memory()
            if mem.percent < 90:
                self.add_check('Memory', 'pass', f'{mem.percent}% used')
            else:
                self.add_check('Memory', 'warn', f'{mem.percent}% used (high)')
        except ImportError:
            self.add_check('Memory', 'warn', 'psutil not available')
    
    def check_disk(self):
        """Check disk space"""
        try:
            import psutil
            disk = psutil.disk_usage('/')
            if disk.percent < 90:
                self.add_check('Disk', 'pass', f'{disk.percent}% used')
            else:
                self.add_check('Disk', 'warn', f'{disk.percent}% used (high)')
        except ImportError:
            self.add_check('Disk', 'warn', 'psutil not available')
    
    def check_cpu(self):
        """Check CPU"""
        try:
            import psutil
            cpu = psutil.cpu_percent(interval=1)
            if cpu < 90:
                self.add_check('CPU', 'pass', f'{cpu}% used')
            else:
                self.add_check('CPU', 'warn', f'{cpu}% used (high)')
        except ImportError:
            self.add_check('CPU', 'warn', 'psutil not available')
    
    def check_main_script(self):
        """Check main script"""
        if os.path.exists('ghost_crab_v1.py'):
            self.add_check('Main Script', 'pass', 'ghost_crab_v1.py found')
        else:
            self.add_check('Main Script', 'warn', 'ghost_crab_v1.py not found')
    
    def run_all(self):
        """Run all health checks"""
        print(f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════════╗
║{Colors.WHITE}          👻 GHOST-CRAB-V1 - Health Check                         {Colors.CYAN}║
╠══════════════════════════════════════════════════════════════════╣
║{Colors.WHITE}  Version: {VERSION:<50} {Colors.CYAN}║
║{Colors.WHITE}  Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S'):<53} {Colors.CYAN}║
╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}
""")
        
        print(f"{Colors.BOLD}🔍 Running Health Checks...{Colors.RESET}\n")
        
        # Run checks
        self.check_python()
        self.check_platform()
        self.check_hostname()
        self.check_main_script()
        self.check_directories()
        self.check_database()
        self.check_network()
        self.check_ports()
        self.check_system_tools()
        self.check_python_modules()
        self.check_memory()
        self.check_disk()
        self.check_cpu()
        
        # Print summary
        self.print_summary()
        
        return self.results
    
    def print_summary(self):
        """Print health check summary"""
        passed = len([c for c in self.results['checks'] if c['status'] == 'pass'])
        failed = len([c for c in self.results['checks'] if c['status'] == 'fail'])
        warned = len([c for c in self.results['checks'] if c['status'] == 'warn'])
        
        print(f"\n{Colors.BOLD}{'='*60}{Colors.RESET}")
        print(f"{Colors.BOLD}📊 HEALTH SUMMARY{Colors.RESET}")
        print(f"{Colors.BOLD}{'='*60}{Colors.RESET}")
        
        print(f"  {Colors.GREEN}Passed: {passed}{Colors.RESET}")
        print(f"  {Colors.RED}Failed: {failed}{Colors.RESET}")
        print(f"  {Colors.YELLOW}Warnings: {warned}{Colors.RESET}")
        
        status_color = {
            'healthy': Colors.GREEN,
            'degraded': Colors.YELLOW,
            'unhealthy': Colors.RED
        }[self.results['status']]
        
        print(f"\n  {Colors.BOLD}Status: {status_color}{self.results['status'].upper()}{Colors.RESET}")
        
        if self.results['errors']:
            print(f"\n{Colors.RED}❌ Errors:{Colors.RESET}")
            for error in self.results['errors']:
                print(f"   • {error}")
        
        if self.results['warnings']:
            print(f"\n{Colors.YELLOW}⚠️  Warnings:{Colors.RESET}")
            for warning in self.results['warnings'][:5]:
                print(f"   • {warning}")
        
        print(f"{Colors.BOLD}{'='*60}{Colors.RESET}")
    
    def save_report(self, path: str = 'health_report.json'):
        """Save health check report"""
        try:
            with open(path, 'w') as f:
                json.dump(self.results, f, indent=2)
            print(f"\n📄 Report saved to: {path}")
        except Exception as e:
            print(f"\n❌ Failed to save report: {e}")


def main():
    """Main function"""
    check = HealthCheck()
    results = check.run_all()
    check.save_report()
    
    # Exit code
    if results['status'] == 'healthy':
        sys.exit(0)
    elif results['status'] == 'degraded':
        sys.exit(1)
    else:
        sys.exit(2)


if __name__ == '__main__':
    main()
