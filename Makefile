# ============================================
# GHOST-CRAB-V1 - Makefile
# Author: Ian Carter Kulani
# Version: 1.0.0
# ============================================

# Variables
APP_NAME = ghost-crab-v1
VERSION = 1.0.0
PYTHON = python3
PIP = pip3
PYTEST = pytest
DOCKER = docker
DOCKER_COMPOSE = docker-compose
INSTALL_DIR = /opt/ghost-crab
CONFIG_DIR = $(HOME)/.ghost_crab_v1

# Directories
BUILD_DIR = build
DIST_DIR = dist
TEST_DIR = tests
DOCS_DIR = docs
REPORTS_DIR = reports

# Files
MAIN_SCRIPT = ghost_crab_v1.py
REQUIREMENTS = requirements.txt
DOCKERFILE = Dockerfile
DOCKERFILE_ALPINE = Dockerfile.alpine
COMPOSE_FILE = docker-compose.yml

# Colors
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
CYAN = \033[0;36m
WHITE = \033[1;37m
RESET = \033[0m

# Phony targets
.PHONY: all help clean install install-dev uninstall \
        test test-unit test-integration test-coverage test-commands \
        lint lint-fix format format-check \
        build build-exe build-wheel \
        docker docker-alpine docker-run docker-stop \
        docker-compose docker-compose-up docker-compose-down docker-compose-logs \
        security security-deps \
        docs docs-serve \
        package publish \
        run run-debug \
        deploy-staging deploy-prod \
        requirements check-requirements count-lines tree backup \
        health init

# Default target
all: install lint test health
	@echo -e "$(GREEN)✅ Build complete!$(RESET)"

# ==================== HELP ====================
help:
	@echo -e "$(CYAN)GHOST-CRAB-V1 v$(VERSION) - Makefile$(RESET)"
	@echo ""
	@echo -e "$(WHITE)Usage: make [target]$(RESET)"
	@echo ""
	@echo -e "$(YELLOW)Installation:$(RESET)"
	@echo "  install          Install dependencies"
	@echo "  install-dev      Install development dependencies"
	@echo "  uninstall        Remove installation"
	@echo ""
	@echo -e "$(YELLOW)Testing:$(RESET)"
	@echo "  test             Run all tests"
	@echo "  test-unit        Run unit tests"
	@echo "  test-integration Run integration tests"
	@echo "  test-coverage    Generate coverage report"
	@echo "  test-commands    Test all commands"
	@echo "  health           Run health check"
	@echo ""
	@echo -e "$(YELLOW)Code Quality:$(RESET)"
	@echo "  lint             Run linter"
	@echo "  lint-fix         Auto-fix lint issues"
	@echo "  format           Format code"
	@echo "  format-check     Check code format"
	@echo ""
	@echo -e "$(YELLOW)Build:$(RESET)"
	@echo "  build            Build Python package"
	@echo "  build-exe        Build executable"
	@echo "  build-wheel      Build wheel"
	@echo ""
	@echo -e "$(YELLOW)Docker:$(RESET)"
	@echo "  docker           Build Docker image"
	@echo "  docker-alpine    Build Alpine Docker image"
	@echo "  docker-run       Run Docker container"
	@echo "  docker-stop      Stop Docker container"
	@echo "  docker-compose   Start with Docker Compose"
	@echo ""
	@echo -e "$(YELLOW)Security:$(RESET)"
	@echo "  security         Run security scan"
	@echo "  security-deps    Audit dependencies"
	@echo ""
	@echo -e "$(YELLOW)Utilities:$(RESET)"
	@echo "  run              Run application"
	@echo "  clean            Clean build artifacts"
	@echo "  tree             Display project tree"
	@echo "  backup           Create backup"
	@echo "  count-lines      Count lines of code"

# ==================== INSTALLATION ====================
install:
	@echo -e "$(CYAN)📦 Installing dependencies...$(RESET)"
	$(PIP) install --upgrade pip setuptools wheel
	$(PIP) install -r $(REQUIREMENTS)
	@echo -e "$(GREEN)✅ Dependencies installed$(RESET)"

install-dev: install
	@echo -e "$(CYAN)📦 Installing development dependencies...$(RESET)"
	$(PIP) install pytest pytest-cov pytest-html flake8 black isort mypy pylint bandit safety
	@echo -e "$(GREEN)✅ Development dependencies installed$(RESET)"

uninstall:
	@echo -e "$(YELLOW)🗑️  Uninstalling...$(RESET)"
	$(PIP) uninstall -y -r $(REQUIREMENTS)
	rm -rf $(BUILD_DIR) $(DIST_DIR) *.egg-info
	@echo -e "$(GREEN)✅ Uninstalled$(RESET)"

# ==================== TESTING ====================
test:
	@echo -e "$(CYAN)🧪 Running all tests...$(RESET)"
	$(PYTEST) $(TEST_DIR) -v

test-unit:
	@echo -e "$(CYAN)🧪 Running unit tests...$(RESET)"
	$(PYTEST) $(TEST_DIR)/unit -v

test-integration:
	@echo -e "$(CYAN)🧪 Running integration tests...$(RESET)"
	$(PYTEST) $(TEST_DIR)/integration -v

test-coverage:
	@echo -e "$(CYAN)📊 Generating coverage report...$(RESET)"
	$(PYTEST) $(TEST_DIR) --cov=. --cov-report=html --cov-report=xml --cov-report=term

test-commands:
	@echo -e "$(CYAN)🧪 Testing commands...$(RESET)"
	$(PYTHON) test-commands.py

health:
	@echo -e "$(CYAN)🏥 Running health check...$(RESET)"
	$(PYTHON) health-check.py

# ==================== CODE QUALITY ====================
lint:
	@echo -e "$(CYAN)🔍 Running linter...$(RESET)"
	flake8 --max-line-length=120 --ignore=E501,W503,E203 $(MAIN_SCRIPT) test-commands.py health-check.py

lint-fix:
	@echo -e "$(CYAN)🔧 Auto-fixing lint issues...$(RESET)"
	autopep8 --in-place --aggressive --aggressive $(MAIN_SCRIPT)

format:
	@echo -e "$(CYAN)🎨 Formatting code...$(RESET)"
	black --line-length 120 $(MAIN_SCRIPT) test-commands.py health-check.py
	isort $(MAIN_SCRIPT) test-commands.py health-check.py

format-check:
	@echo -e "$(CYAN)🎨 Checking code format...$(RESET)"
	black --check --line-length 120 $(MAIN_SCRIPT)
	isort --check $(MAIN_SCRIPT)

# ==================== BUILD ====================
build: clean
	@echo -e "$(CYAN)📦 Building Python package...$(RESET)"
	$(PYTHON) -m build

build-exe:
	@echo -e "$(CYAN)📦 Building executable...$(RESET)"
	pyinstaller --onefile --name $(APP_NAME) $(MAIN_SCRIPT)

build-wheel:
	@echo -e "$(CYAN)📦 Building wheel...$(RESET)"
	$(PYTHON) setup.py bdist_wheel

# ==================== DOCKER ====================
docker:
	@echo -e "$(CYAN)🐳 Building Docker image...$(RESET)"
	$(DOCKER) build -t $(APP_NAME):$(VERSION) -f $(DOCKERFILE) .
	$(DOCKER) tag $(APP_NAME):$(VERSION) $(APP_NAME):latest

docker-alpine:
	@echo -e "$(CYAN)🐳 Building Alpine Docker image...$(RESET)"
	$(DOCKER) build -t $(APP_NAME):$(VERSION)-alpine -f $(DOCKERFILE_ALPINE) .
	$(DOCKER) tag $(APP_NAME):$(VERSION)-alpine $(APP_NAME):alpine

docker-run:
	@echo -e "$(CYAN)🚀 Running Docker container...$(RESET)"
	$(DOCKER) run -d --name $(APP_NAME) -p 5000:5000 -p 8080:8080 $(APP_NAME):$(VERSION)

docker-stop:
	@echo -e "$(YELLOW)🛑 Stopping Docker container...$(RESET)"
	$(DOCKER) stop $(APP_NAME) && $(DOCKER) rm $(APP_NAME)

docker-compose: docker-compose-up

docker-compose-up:
	@echo -e "$(CYAN)🚀 Starting with Docker Compose...$(RESET)"
	$(DOCKER_COMPOSE) up -d --build

docker-compose-down:
	@echo -e "$(YELLOW)🛑 Stopping Docker Compose...$(RESET)"
	$(DOCKER_COMPOSE) down

docker-compose-logs:
	$(DOCKER_COMPOSE) logs -f

docker-push:
	@echo -e "$(CYAN)📤 Pushing Docker image...$(RESET)"
	$(DOCKER) push $(APP_NAME):$(VERSION)

# ==================== SECURITY ====================
security:
	@echo -e "$(CYAN)🔒 Running security scan...$(RESET)"
	bandit -r . -f json -o bandit-report.json
	safety check --json > safety-report.json

security-deps:
	@echo -e "$(CYAN)🔒 Auditing dependencies...$(RESET)"
	pip-audit

# ==================== DOCUMENTATION ====================
docs:
	@echo -e "$(CYAN)📚 Building documentation...$(RESET)"
	mkdocs build

docs-serve:
	@echo -e "$(CYAN)📚 Serving documentation...$(RESET)"
	mkdocs serve

# ==================== PACKAGE ====================
package: build
	@echo -e "$(CYAN)📦 Creating distribution package...$(RESET)"

publish: package
	@echo -e "$(CYAN)📤 Publishing to PyPI...$(RESET)"
	twine upload dist/*

# ==================== RUN ====================
run:
	@echo -e "$(CYAN)🚀 Running application...$(RESET)"
	$(PYTHON) $(MAIN_SCRIPT)

run-debug:
	@echo -e "$(CYAN)🐛 Running in debug mode...$(RESET)"
	$(PYTHON) -m pdb $(MAIN_SCRIPT)

# ==================== DEPLOY ====================
deploy-staging:
	@echo -e "$(CYAN)🚀 Deploying to staging...$(RESET)"
	ssh $(STAGING_HOST) "cd /opt/ghost-crab && git pull && docker-compose up -d"

deploy-prod:
	@echo -e "$(CYAN)🚀 Deploying to production...$(RESET)"
	ssh $(PROD_HOST) "cd /opt/ghost-crab && git pull && docker-compose up -d"

# ==================== UTILITIES ====================
requirements:
	@echo -e "$(CYAN)📋 Freezing requirements...$(RESET)"
	$(PIP) freeze > $(REQUIREMENTS)

check-requirements:
	@echo -e "$(CYAN)📋 Checking requirements...$(RESET)"
	$(PYTHON) requirements-check.py

count-lines:
	@echo -e "$(CYAN)📊 Counting lines...$(RESET)"
	wc -l $(MAIN_SCRIPT) $(REQUIREMENTS) test-commands.py health-check.py

tree:
	@echo -e "$(CYAN)🌳 Project tree:$(RESET)"
	tree -I '__pycache__|*.pyc|.git|build|dist|venv'

backup:
	@echo -e "$(CYAN)💾 Creating backup...$(RESET)"
	tar -czf backup-$$(date +%Y%m%d-%H%M%S).tar.gz \
		$(MAIN_SCRIPT) $(REQUIREMENTS) $(DOCKERFILE) $(COMPOSE_FILE)

clean:
	@echo -e "$(YELLOW)🧹 Cleaning build artifacts...$(RESET)"
	rm -rf $(BUILD_DIR) $(DIST_DIR) .pytest_cache __pycache__ *.pyc *.pyo
	rm -rf *.egg-info .coverage htmlcov coverage.xml
	rm -rf bandit-report.json safety-report.json
	@echo -e "$(GREEN)✅ Cleaned$(RESET)"

init:
	@echo -e "$(CYAN)🚀 Initializing configuration...$(RESET)"
	$(PYTHON) $(MAIN_SCRIPT) --init
