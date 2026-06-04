# Code map

Regenerate with:

```bash
just update-context
```

This file gives humans and LLM assistants a cheap structural map before they
scan the repository.

## Entry points

- CLI: `src/{{cookiecutter.project_slug}}/main.py`
- Workflow base: `src/{{cookiecutter.project_slug}}/workflow/base.py`
- Example workflow: `src/{{cookiecutter.project_slug}}/workflow/example.py`
- Config models: `src/{{cookiecutter.project_slug}}/config/models.py`

## Package modules

- `{{cookiecutter.project_slug}}.main` — Typer CLI and `run(config)` entry point
- `{{cookiecutter.project_slug}}.config.models` — Pydantic config contracts
- `{{cookiecutter.project_slug}}.workflow.base` — abstract workflow interface
- `{{cookiecutter.project_slug}}.workflow.example` — scaffold workflow example
- `{{cookiecutter.project_slug}}.logger` — logging helper

## Config and tests

- Runtime config: `config/config_{{cookiecutter.project_slug}}.yml`
- Unit tests: `tests/unit/`
- Integration tests: `tests/integration/`
- Approval tests: `tests/approval/`

## Context files

- `.llm/` — source of truth for LLM-facing guidance
- `AGENTS.md` — Codex-oriented guidance
- `CLAUDE.md` — Claude Code-oriented guidance
- `knowledge_base/current_state.md` — current project status and open work
