#!/usr/bin/env python3
"""
GHOST-CRAB-V1 - Command Test Suite
Tests all major command categories
"""

import sys
import os
import time
import unittest
import subprocess
from typing import Dict, List

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# ANSI Colors
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


class CommandTester:
    """Test command execution"""
    
    def __init__(self):
        self.results = {
            'passed': 0,
            'failed': 0,
            'skipped': 0,
            'tests': []
        }
    
    def run_command(self, command: str, timeout: int = 30) -> Dict:
        """Run a command and capture result"""
        start = time.time()
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            elapsed = time.time() - start
            return {
                'success': result.returncode == 0,
                'output': result.stdout + result.stderr,
                'elapsed': elapsed,
                'returncode': result.returncode
            }
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'output': 'Command timed out',
                'elapsed': time.time() - start,
                'returncode': -1
            }
        except Exception as e:
            return {
                'success': False,
                'output': str(e),
                'elapsed': time.time() - start,
                'returncode': -1
            }
    
    def test_command(self, name: str, command: str, expected_in_output: str = None,
                    timeout: int = 30, skip: bool = False) -> bool:
        """Test a single command"""
        if skip:
            self.results['skipped'] += 1
            self.results['tests'].append({
                'name': name,
                'status': 'SKIPPED',
                'command': command
            })
            print(f"{Colors.YELLOW}⊘ SKIPPED: {name}{Colors.RESET}")
            return False
        
        print(f"{Colors.CYAN}▶ Testing: {name}...{Colors.RESET}", end=' ')
        
        result = self.run_command(command, timeout)
        
        # Check success
        passed = result['success']
        
        # Check expected output
        if passed and expected_in_output:
            passed = expected_in_output.lower() in result['output'].lower()
        
        if passed:
            self.results['passed'] += 1
            print(f"{Colors.GREEN}✅ PASSED ({result['elapsed']:.2f}s){Colors.RESET}")
        else:
            self.results['failed'] += 1
            print(f"{Colors.RED}❌ FAILED{Colors.RESET}")
            if result['output']:
                print(f"   Output: {result['output'][:200]}")
        
        self.results['tests'].append({
            'name': name,
            'status': 'PASSED' if passed else 'FAILED',
            'command': command,
            'elapsed': result['elapsed'],
            'output': result['output'][:500]
        })
        
        return passed
    
    def print_summary(self):
        """Print test summary"""
        total = self.results['passed'] + self.results['failed'] + self.results['skipped']
        
        print(f"\n{Colors.BOLD}{'='*60}{Colors.RESET}")
        print(f"{Colors.BOLD}📊 TEST SUMMARY{Colors.RESET}")
        print(f"{Colors.BOLD}{'='*60}{Colors.RESET}")
        
        print(f"  Total Tests: {total}")
        print(f"  {Colors.GREEN}Passed: {self.results['passed']}{Colors.RESET}")
        print(f"  {Colors.RED}Failed: {self.results['failed']}{Colors.RESET}")
        print(f"  {Colors.YELLOW}Skipped: {self.results['skipped']}{Colors.RESET}")
        
        if self.results['failed'] == 0:
            print(f"\n{Colors.GREEN}✅ All tests passed!{Colors.RESET}")
        else:
            print(f"\n{Colors.RED}❌ {self.results['failed']} test(s) failed{Colors.RESET}")
        
        print(f"{Colors.BOLD}{'='*60}{Colors.RESET}")


def run_system_tests(tester: CommandTester):
    """Test system commands"""
    print(f"\n{Colors.BOLD}🖥️  System Tests{Colors.RESET}")
    print("-" * 40)
    
    tester.test_command("Python Version", "python3 --version", "Python")
    tester.test_command("Pip Version", "pip3 --version", "pip")
    tester.test_command("System Info", "uname -a")
    tester.test_command("Disk Space", "df -h")
    tester.test_command("Memory Info", "free -h")
    tester.test_command("CPU Info", "nproc")


def run_network_tests(tester: CommandTester):
    """Test network commands"""
    print(f"\n{Colors.BOLD}🌐 Network Tests{Colors.RESET}")
    print("-" * 40)
    
    tester.test_command("Ping Localhost", "ping -c 1 127.0.0.1", "1 received")
    tester.test_command("DNS Lookup", "nslookup google.com", "Address")
    tester.test_command("Curl Test", "curl -s -o /dev/null -w '%{http_code}' https://www.google.com", "200")
    tester.test_command("Wget Test", "wget -q --spider https://www.google.com")
    tester.test_command("Traceroute", "traceroute -m 3 8.8.8.8", skip=True)
    tester.test_command("Netcat Check", "which nc")


def run_security_tests(tester: CommandTester):
    """Test security tools"""
    print(f"\n{Colors.BOLD}🔒 Security Tool Tests{Colors.RESET}")
    print("-" * 40)
    
    tester.test_command("Nmap Version", "nmap --version", "Nmap")
    tester.test_command("Nmap Localhost", "nmap -F 127.0.0.1", timeout=60)
    tester.test_command("OpenSSL Version", "openssl version", "OpenSSL")
    tester.test_command("SSH Client", "ssh -V", "OpenSSH")
    tester.test_command("Whois Tool", "which whois")


def run_python_tests(tester: CommandTester):
    """Test Python modules"""
    print(f"\n{Colors.BOLD}🐍 Python Module Tests{Colors.RESET}")
    print("-" * 40)
    
    modules = [
        ('requests', 'import requests; print(requests.__version__)'),
        ('urllib3', 'import urllib3; print(urllib3.__version__)'),
        ('paramiko', 'import paramiko; print(paramiko.__version__)'),
        ('scapy', 'from scapy.all import *; print("scapy OK")'),
        ('flask', 'import flask; print(flask.__version__)'),
        ('numpy', 'import numpy; print(numpy.__version__)'),
        ('pandas', 'import pandas; print(pandas.__version__)'),
        ('matplotlib', 'import matplotlib; print(matplotlib.__version__)'),
        ('cryptography', 'import cryptography; print(cryptography.__version__)'),
        ('PIL', 'from PIL import Image; print("Pillow OK")'),
        ('psutil', 'import psutil; print(psutil.__version__)'),
        ('qrcode', 'import qrcode; print("qrcode OK")'),
        ('reportlab', 'import reportlab; print(reportlab.Version)'),
        ('bs4', 'import bs4; print(bs4.__version__)'),
        ('yaml', 'import yaml; print(yaml.__version__)'),
    ]
    
    for name, cmd in modules:
        tester.test_command(f"Module: {name}", f"python3 -c '{cmd}'")


def run_ghost_crab_tests(tester: CommandTester):
    """Test Ghost Crab specific functionality"""
    print(f"\n{Colors.BOLD}👻 Ghost Crab Tests{Colors.RESET}")
    print("-" * 40)
    
    # Check if main script exists
    tester.test_command("Main Script", "test -f ghost_crab_v1.py")
    tester.test_command("Config File", "test -f requirements.txt")
    tester.test_command("Health Check", "test -f health-check.py")
    
    # Test directory creation
    tester.test_command("Config Dir", "mkdir -p .ghost_crab_v1 && test -d .ghost_crab_v1")
    
    # Test Python syntax
    tester.test_command("Python Syntax", "python3 -m py_compile ghost_crab_v1.py", skip=not os.path.exists('ghost_crab_v1.py'))


def main():
    """Main test runner"""
    print(f"""
{Colors.GREEN}╔══════════════════════════════════════════════════════════════════╗
║{Colors.WHITE}          👻 GHOST-CRAB-V1 - Command Test Suite                  {Colors.GREEN}║
╠══════════════════════════════════════════════════════════════════╣
║{Colors.CYAN}  Testing all command categories and dependencies                {Colors.GREEN}║
╚══════════════════════════════════════════════════════════════════╝{Colors.RESET}
""")
    
    tester = CommandTester()
    
    # Run all test categories
    run_system_tests(tester)
    run_network_tests(tester)
    run_security_tests(tester)
    run_python_tests(tester)
    run_ghost_crab_tests(tester)
    
    # Print summary
    tester.print_summary()
    
    # Return exit code
    return 0 if tester.results['failed'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
