# cookiecutter-eo-llm

**A production-minded EO/SAR Python package template with TDD workflows and
LLM-ready context for Claude Code and Codex.**

It scaffolds typed YAML config, strict Python tooling, living project docs, and
token-efficient LLM context generated from a single source of truth.

---

## Why this template?

EO/SAR work often begins as an analysis notebook, then slowly turns into a
workflow that other people need to run, test, review, and maintain. This template
sets up that package boundary early: one workflow class, one plain YAML config,
typed source/compute/destination models, tests, docs, and LLM guidance that all
point to the same architecture.

| Problem | Solution |
|---------|----------|
| CLAUDE.md and AGENTS.md drift apart | Both rendered from the same `.llm/` source of truth |
| Boilerplate for every new package | One command scaffolds a fully wired project |
| LLM context files bloat quickly | Hard 200-line limit enforced by tests |
| Inconsistent tooling across projects | uv + ruff + mypy strict + pytest everywhere |
| Notebook-to-package migration is messy | One workflow class + one config file + tests from the start |
| Heavy geospatial dependencies get added too early | Runtime deps stay small; EO/SAR libraries are added only when needed |
| New LLM sessions spend tokens rediscovering structure | `code_map.md` and `current_state.md` give agents a cheap first read |

---

## What you get

```
my-eo-package/
├── src/my_eo_package/       ← importable package (snake_case)
│   ├── logger.py            ← get_logger(name) for workflow/runtime logging
│   ├── workflow/            ← abstract base + concrete implementation
│   ├── config/              ← SourceModel / ComputeParamsModel / DestinationModel
│   └── main.py              ← typer CLI + run_<project_slug>() entry point
├── .llm/                    ← single source of truth for LLM context and skills
├── knowledge_base/          ← living architecture docs
├── tests/                   ← unit / integration / approval suites
├── CLAUDE.md                ← rendered from .llm/
├── AGENTS.md                ← rendered from .llm/
├── Justfile                 ← all dev commands
└── pyproject.toml           ← hatchling + uv, fully wired
```

---

## Quick install

```bash
uvx cookiecutter gh:pmuguda/cookiecutter-eo-llm
```

→ [Full quickstart guide](quickstart.md)

---

## Core principles

- **TDD everywhere** — every feature built test-first
- **SOLID** — one responsibility per function and class
- **No comments** — rename and simplify instead
- **uv only** — no pip, no Poetry
- **Tokens are gold** — LLM context files stay lean and human-curated
- **Context economy** — `just update-context` refreshes a local code map without extra tooling
- **Single source of truth** — `.llm/` drives both CLAUDE.md and AGENTS.md
- **Docs move with code** — architecture, workflow, and API changes update docs too
- **Conventional Commits** — feat/fix/chore with SemVer mapping

## Credits

This template stands on Cookiecutter, uv, hatchling, ruff, mypy, pytest,
Pydantic, Typer, PyYAML, MkDocs, GitHub Actions, and GitLab CI.
