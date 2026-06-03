# ----------------------------------------
# Project Commands
# ----------------------------------------

.PHONY: install dev format lint test clean help

help:
	@echo "Available commands:"
	@echo "  make install   - Install project in editable mode"
	@echo "  make dev       - Install dev dependencies"
	@echo "  make format    - Format code with black + ruff"
	@echo "  make lint      - Run linters (ruff + mypy)"
	@echo "  make test      - Run tests"
	@echo "  make clean     - Remove build artifacts and caches"
	@echo "  make help      - Display this help message"

# Install the project in editable mode
install:
	pip install -e .

# Install development dependencies
dev:
	pip install -e .[dev]

# Run formatting tools
format:
	black .
	ruff check --fix .

# Run linting without modifying files
lint:
	ruff check .
	mypy .

# Run tests
test:
	pytest -q

# Run test coverage
coverage:
	pytest --cov=. --cov-report=term-missing

coverage-html:
	pytest --cov=. --cove-report=term-missing --cov-report=html

# Remove caches, build artifacts, and temporary files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".pytest_cache" -exec rm -r {} +
	rm -rf build dist *.egg-info htmlcov
