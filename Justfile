default:
    @just --list

test:
    uv run python -m pytest

test-cov:
    uv run python -m pytest --cov=hooks --cov=tests/helpers --cov-report=xml --cov-report=term-missing

docs:
    uv run --extra docs mkdocs serve

docs-build:
    uv run --extra docs mkdocs build --strict

render:
    uvx cookiecutter . --no-input -o /tmp/eo-llm-test

lint:
    uv run ruff check hooks/ tests/

typecheck:
    uv run mypy hooks/ tests/

check: lint typecheck
