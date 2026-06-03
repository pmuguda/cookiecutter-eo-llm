# cookiecutter-eo-llm

[![PyPI](https://img.shields.io/pypi/v/cookiecutter-eo-llm)](https://pypi.org/project/cookiecutter-eo-llm/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

Cookiecutter template for Earth Observation / SAR Python packages with
token-efficient, LLM-agnostic context files (CLAUDE.md, AGENTS.md).

## Usage

```bash
uvx cookiecutter gh:pmuguda/cookiecutter-eo-llm
```

Or locally:

```bash
uvx cookiecutter .
```

## What you get

- `src/` layout with abstract `Workflow` base class
- YAML-tag-driven workflow dispatch
- Pydantic v2 config validation
- Typer CLI entry point
- Full test suite (unit, integration, approval)
- CLAUDE.md + AGENTS.md rendered from a single `.llm/` source of truth
- `knowledge_base/` living architecture docs
- GitHub Actions CI + GitLab CI
- Justfile with all dev commands
- Conventional Commits + bump-my-version wired up

## Template development

```bash
uv sync --dev
uv run pytest
```

## License

MIT © Pavan Muguda Sanjeevamurthy
