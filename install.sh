#!/bin/bash
#
# GHOST-CRAB-V1 - Installation Script
# Author: Ian Carter Kulani
# Version: 1.0.0
#

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
RESET='\033[0m'

# Variables
APP_NAME="GHOST-CRAB-V1"
VERSION="1.0.0"
INSTALL_DIR="/opt/ghost-crab"
CONFIG_DIR="$HOME/.ghost_crab_v1"
PYTHON_VERSION="3.11"

# Banner
print_banner() {
    echo -e "${RED}"
    cat << "EOF"
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║   ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗                ║
    ║  ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝                ║
    ║  ██║  ███╗███████║██║   ██║███████╗   ██║                   ║
    ║  ██║   ██║██╔══██║██║   ██║╚════██║   ██║                   ║
    ║  ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║                   ║
    ║   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝                   ║
    ║                                                              ║
    ║              GHOST-CRAB-V1 INSTALLER v1.0.0                  ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
EOF
    echo -e "${RESET}"
}

# Print functions
print_info() { echo -e "${CYAN}[INFO]${RESET} $1"; }
print_success() { echo -e "${GREEN}[✓]${RESET} $1"; }
print_warning() { echo -e "${YELLOW}[!]${RESET} $1"; }
print_error() { echo -e "${RED}[✗]${RESET} $1"; }

# Check if running as root
check_root() {
    if [[ $EUID -ne 0 ]]; then
        print_warning "Not running as root. Some features may not work."
        print_info "Run with: sudo $0"
    fi
}

# Detect OS
detect_os() {
    if [[ -f /etc/os-release ]]; then
        . /etc/os-release
        OS=$ID
        VERSION=$VERSION_ID
    elif [[ -f /etc/debian_version ]]; then
        OS="debian"
    elif [[ -f /etc/redhat-release ]]; then
        OS="rhel"
    elif [[ "$(uname)" == "Darwin" ]]; then
        OS="macos"
    else
        OS="unknown"
    fi
    
    print_info "Detected OS: $OS"
}

# Install system dependencies
install_system_deps() {
    print_info "Installing system dependencies..."
    
    case $OS in
        ubuntu|debian)
            apt-get update
            apt-get install -y \
                python3 python3-pip python3-venv python3-dev \
                build-essential gcc g++ make cmake \
                nmap curl wget netcat-openbsd dnsutils \
                traceroute whois tcpdump net-tools \
                iputils-ping iproute2 telnet ftp \
                openssh-client git vim htop tree jq \
                libssl-dev libffi-dev libxml2-dev \
                libxslt1-dev libjpeg-dev libpng-dev \
                libfreetype6-dev libpq-dev libmagic-dev \
                libpcap-dev ca-certificates
            ;;
        fedora|rhel|centos)
            dnf install -y \
                python3 python3-pip python3-devel \
                gcc gcc-c++ make cmake \
                nmap curl wget nmap-ncat bind-utils \
                traceroute whois tcpdump net-tools \
                openssh-clients git vim htop tree jq \
                openssl-devel libffi-devel libxml2-devel \
                libxslt-devel libjpeg-turbo-devel \
                freetype-devel postgresql-devel \
                file-devel libpcap-devel ca-certificates
            ;;
        arch)
            pacman -Syu --noconfirm \
                python python-pip python-virtualenv \
                base-devel gcc make cmake \
                nmap curl wget gnu-netcat bind \
                traceroute whois tcpdump net-tools \
                openssh git vim htop tree jq \
                openssl libffi libxml2 libxslt \
                libjpeg-turbo libpng freetype2 \
                postgresql-libs file libpcap
            ;;
        alpine)
            apk add --no-cache \
                python3 py3-pip py3-virtualenv \
                build-base gcc g++ make cmake \
                nmap curl wget netcat-openbsd bind-tools \
                traceroute whois tcpdump net-tools \
                iputils iproute2 openssh-client git \
                vim htop tree jq openssl-dev libffi-dev \
                libxml2-dev libxslt-dev jpeg-dev \
                libpng-dev freetype-dev postgresql-dev \
                file-dev libpcap-dev ca-certificates
            ;;
        macos)
            if ! command -v brew &> /dev/null; then
                print_info "Installing Homebrew..."
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            fi
            brew install python3 nmap curl wget netcat \
                bind traceroute whois tcpdump git vim \
                htop tree jq openssl libffi libxml2 \
                libxslt jpeg libpng freetype postgresql \
                libmagic libpcap
            ;;
        *)
            print_error "Unsupported OS: $OS"
            exit 1
            ;;
    esac
    
    print_success "System dependencies installed"
}

# Install Python dependencies
install_python_deps() {
    print_info "Installing Python dependencies..."
    
    # Create virtual environment
    python3 -m venv "$INSTALL_DIR/venv"
    source "$INSTALL_DIR/venv/bin/activate"
    
    # Upgrade pip
    pip install --upgrade pip setuptools wheel
    
    # Install requirements
    if [[ -f requirements.txt ]]; then
        pip install -r requirements.txt
    else
        print_warning "requirements.txt not found, installing core packages..."
        pip install requests urllib3 paramiko scapy dnspython whois \
            cryptography flask flask-socketio flask-cors \
            discord.py telethon slack-sdk selenium \
            numpy pandas matplotlib seaborn \
            sqlalchemy redis pymongo \
            reportlab python-docx openpyxl \
            Pillow opencv-python \
            pynput pyperclip pyautogui mss \
            qrcode psutil colorama rich tqdm \
            beautifulsoup4 lxml pyyaml
    fi
    
    print_success "Python dependencies installed"
}

# Create directories
create_directories() {
    print_info "Creating directories..."
    
    # Install directory
    mkdir -p "$INSTALL_DIR"
    
    # Config directories
    mkdir -p "$CONFIG_DIR"
    mkdir -p "$CONFIG_DIR/payloads"
    mkdir -p "$CONFIG_DIR/workspaces"
    mkdir -p "$CONFIG_DIR/scans"
    mkdir -p "$CONFIG_DIR/phishing_pages"
    mkdir -p "$CONFIG_DIR/phishing_templates"
    mkdir -p "$CONFIG_DIR/captured_credentials"
    mkdir -p "$CONFIG_DIR/ssh_keys"
    mkdir -p "$CONFIG_DIR/traffic_logs"
    mkdir -p "$CONFIG_DIR/reports"
    mkdir -p "$CONFIG_DIR/keylogs"
    mkdir -p "$CONFIG_DIR/keylog_screenshots"
    mkdir -p "$CONFIG_DIR/dos_logs"
    mkdir -p "$CONFIG_DIR/agents"
    mkdir -p "$CONFIG_DIR/c2_logs"
    mkdir -p "$CONFIG_DIR/modules"
    mkdir -p "$CONFIG_DIR/network_monitor"
    mkdir -p "$CONFIG_DIR/keylog_exfil"
    mkdir -p "$CONFIG_DIR/deployments"
    mkdir -p "$CONFIG_DIR/domain_hosting"
    mkdir -p "$CONFIG_DIR/reverse_engineering"
    mkdir -p "$CONFIG_DIR/cracking"
    mkdir -p "$CONFIG_DIR/docker_scans"
    mkdir -p "$CONFIG_DIR/saas"
    mkdir -p "$CONFIG_DIR/malware"
    mkdir -p "$CONFIG_DIR/images"
    
    print_success "Directories created"
}

# Install application files
install_files() {
    print_info "Installing application files..."
    
    # Copy main script
    if [[ -f ghost_crab_v1.py ]]; then
        cp ghost_crab_v1.py "$INSTALL_DIR/"
    else
        print_error "ghost_crab_v1.py not found!"
        exit 1
    fi
    
    # Copy other files
    for file in requirements.txt test-commands.py health-check.py \
                Dockerfile Dockerfile.alpine docker-compose.yml \
                .env.example; do
        if [[ -f "$file" ]]; then
            cp "$file" "$INSTALL_DIR/"
        fi
    done
    
    # Create symlink
    ln -sf "$INSTALL_DIR/ghost_crab_v1.py" /usr/local/bin/ghost-crab 2>/dev/null || true
    
    print_success "Application files installed"
}

# Create launcher script
create_launcher() {
    print_info "Creating launcher script..."
    
    cat > /usr/local/bin/ghost-crab << 'EOF'
#!/bin/bash
INSTALL_DIR="/opt/ghost-crab"
source "$INSTALL_DIR/venv/bin/activate"
cd "$INSTALL_DIR"
exec python3 ghost_crab_v1.py "$@"
EOF
    
    chmod +x /usr/local/bin/ghost-crab
    
    print_success "Launcher script created"
}

# Create systemd service
create_systemd_service() {
    if [[ "$OS" == "macos" ]]; then
        return
    fi
    
    print_info "Creating systemd service..."
    
    cat > /etc/systemd/system/ghost-crab.service << EOF
[Unit]
Description=GHOST-CRAB-V1 Cyber Command Platform
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=$INSTALL_DIR
Environment="PATH=$INSTALL_DIR/venv/bin:/usr/local/bin:/usr/bin:/bin"
ExecStart=$INSTALL_DIR/venv/bin/python3 $INSTALL_DIR/ghost_crab_v1.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF
    
    systemctl daemon-reload
    print_success "Systemd service created"
    print_info "Enable with: sudo systemctl enable ghost-crab"
    print_info "Start with: sudo systemctl start ghost-crab"
}

# Verify installation
verify_installation() {
    print_info "Verifying installation..."
    
    source "$INSTALL_DIR/venv/bin/activate"
    
    if python3 -c "import requests, urllib3, paramiko" 2>/dev/null; then
        print_success "Core modules verified"
    else
        print_error "Core modules verification failed"
        exit 1
    fi
    
    if [[ -f "$INSTALL_DIR/health-check.py" ]]; then
        cd "$INSTALL_DIR"
        python3 health-check.py || true
    fi
    
    print_success "Installation verified"
}

# Print completion message
print_completion() {
    echo ""
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════════╗${RESET}"
    echo -e "${GREEN}║                                                              ║${RESET}"
    echo -e "${GREEN}║           ✅ INSTALLATION COMPLETE!                          ║${RESET}"
    echo -e "${GREEN}║                                                              ║${RESET}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════════╝${RESET}"
    echo ""
    echo -e "${WHITE}📁 Install Directory: ${CYAN}$INSTALL_DIR${RESET}"
    echo -e "${WHITE}📁 Config Directory: ${CYAN}$CONFIG_DIR${RESET}"
    echo ""
    echo -e "${WHITE}🚀 To run:${RESET}"
    echo -e "   ${CYAN}ghost-crab${RESET}"
    echo -e "   or"
    echo -e "   ${CYAN}cd $INSTALL_DIR && source venv/bin/activate && python3 ghost_crab_v1.py${RESET}"
    echo ""
    echo -e "${WHITE}📊 Web Dashboard: ${CYAN}http://localhost:5000${RESET}"
    echo ""
    echo -e "${YELLOW}⚠️  For authorized security testing only${RESET}"
    echo ""
}

# Main installation
main() {
    print_banner
    check_root
    detect_os
    create_directories
    install_system_deps
    install_files
    install_python_deps
    create_launcher
    create_systemd_service
    verify_installation
    print_completion
}

# Run main
main "$@"
