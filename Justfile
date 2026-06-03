default:
    @just --list

test:
    uv run pytest

render:
    uvx cookiecutter . --no-input -o /tmp/eo-llm-test

lint:
    uv run ruff check hooks/ tests/

typecheck:
    uv run mypy hooks/ tests/

check: lint typecheck
