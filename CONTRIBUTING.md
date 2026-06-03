# Contributing to cookiecutter-eo-llm

## Development setup

```bash
uv sync --dev
```

## TDD workflow

Write a failing test first. Implement the minimum code to pass it. Refactor.

## Testing

```bash
uv run pytest
```

## Rendering the template

```bash
uvx cookiecutter . --no-input -o /tmp/eo-llm-test
```

## Commit convention

Conventional Commits 1.0.0. No LLM co-author footers.
