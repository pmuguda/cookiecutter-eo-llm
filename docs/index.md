# cookiecutter-eo-llm

**A Cookiecutter template for Earth Observation and SAR Python packages** — with token-efficient, LLM-agnostic context files generated from a single source of truth at scaffold time.

---

## Why this template?

EO/SAR packages share a common set of requirements: spatial-aware testing, strict type annotations, YAML-driven workflow configs, and increasingly — context files that keep AI coding assistants grounded in your architecture. This template bakes all of that in from day one.

| Problem | Solution |
|---------|----------|
| CLAUDE.md and AGENTS.md drift apart | Both rendered from the same `.llm/` source of truth |
| Boilerplate for every new package | One command scaffolds a fully wired project |
| LLM context files bloat quickly | Hard 200-line limit enforced by tests |
| Inconsistent tooling across projects | uv + ruff + mypy strict + pytest everywhere |
| Adding a workflow requires scattered edits | One subclass + one YAML tag — nothing else |

---

## What you get

```
my-eo-package/
├── src/my_eo_package/       ← importable package (snake_case)
│   ├── workflows/           ← abstract base + concrete implementations
│   ├── config/              ← Pydantic v2 models + YAML tag loaders
│   └── main.py              ← typer CLI + run() entry point
├── .llm/                    ← single source of truth for LLM context
├── knowledge_base/          ← living architecture docs (update as you code)
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
- **Single source of truth** — `.llm/` drives both CLAUDE.md and AGENTS.md
- **Conventional Commits** — feat/fix/chore with SemVer mapping
