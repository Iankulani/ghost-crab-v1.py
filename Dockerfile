# ============================================
# GHOST-CRAB-V1 - Dockerfile (Ubuntu-based)
# ============================================

FROM ubuntu:22.04

LABEL maintainer="Ian Carter Kulani"
LABEL description="GHOST-CRAB-V1 - Cyber Command Platform"
LABEL version="1.0.0"

# Prevent interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Core utilities
    python3 \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    gcc \
    g++ \
    make \
    cmake \
    pkg-config \
    # Network tools
    nmap \
    curl \
    wget \
    netcat-openbsd \
    dnsutils \
    traceroute \
    whois \
    tcpdump \
    tshark \
    net-tools \
    iputils-ping \
    iproute2 \
    telnet \
    ftp \
    ssh \
    openssh-client \
    # Security tools
    hashcat \
    john \
    hydra \
    sqlmap \
    nikto \
    gobuster \
    dirb \
    wfuzz \
    # Development tools
    git \
    vim \
    nano \
    htop \
    tree \
    jq \
    # Libraries
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    libjpeg-dev \
    libpng-dev \
    libfreetype6-dev \
    libpq-dev \
    libmagic-dev \
    libpcap-dev \
    # Browser for Selenium
    chromium-browser \
    chromium-chromedriver \
    firefox \
    # Misc
    ca-certificates \
    gnupg \
    lsb-release \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Install Docker CLI
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && apt-get update \
    && apt-get install -y docker-ce-cli \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN python3 -m pip install --upgrade pip setuptools wheel

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create necessary directories
RUN mkdir -p /app/.ghost_crab_v1/{payloads,workspaces,scans,phishing_pages,phishing_templates,captured_credentials,ssh_keys,traffic_logs,nikto_results,reports,keylogs,keylog_screenshots,dos_logs,agents,c2_logs,modules,network_monitor,keylog_exfil,deployments,domain_hosting,reverse_engineering,cracking,docker_scans,saas,malware,images}

# Create non-root user
RUN useradd -m -s /bin/bash ghostcrab && \
    chown -R ghostcrab:ghostcrab /app

# Switch to non-root user
USER ghostcrab

# Expose ports
EXPOSE 5000 8080 4444 5555 9001

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 health-check.py || exit 1

# Default command
CMD ["python3", "ghost_crab_v1.py"]
