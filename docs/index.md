# cookiecutter-eo-llm

**A production-minded EO/SAR Python package template with TDD workflows and
LLM-ready context for Claude Code and Codex.**

One command gives you a typed, tested, LLM-aware Python package: a concrete
workflow class, a plain YAML config model, a living knowledge base, and
token-efficient context files that keep AI assistants grounded in
your project's rules — all from a single `.llm/` source of truth.

---

## Why this template?

EO/SAR work follows a predictable trajectory:

```mermaid
flowchart LR
    A([Notebook\nanalysis]) -->|"copy-paste\ngrows"| B([Ad-hoc\nscripts])
    B -->|"no tests\nno types"| C([Fragile\npipeline])
    C -->|"LLM sessions\nrediscover structure"| D([Wasted\ncontext budget])

    style A fill:#1e1e2e,stroke:#6c7086,color:#cdd6f4
    style B fill:#1e1e2e,stroke:#f38ba8,color:#cdd6f4
    style C fill:#1e1e2e,stroke:#f38ba8,color:#cdd6f4
    style D fill:#1e1e2e,stroke:#f38ba8,color:#cdd6f4
```

This template interrupts that trajectory at step one.

| Problem | How the template solves it |
|---------|---------------------------|
| CLAUDE.md and AGENTS.md drift apart | Both rendered from the same `.llm/` source of truth |
| Boilerplate for every new package | One command scaffolds a fully wired project |
| LLM context files bloat quickly | Hard 200-line limit enforced by tests |
| Inconsistent tooling across projects | uv + ruff + mypy strict + pytest everywhere |
| Notebook-to-package migration is messy | One workflow class + one config file + tests from day 1 |
| Heavy geospatial dependencies added too early | Runtime deps stay small; EO libraries added only when needed |
| New LLM sessions spend tokens rediscovering structure | `code_map.md` and `current_state.md` give agents a cheap first read |

---

## How it works

```mermaid
flowchart TD
    CC["uvx cookiecutter gh:pmuguda/cookiecutter-eo-llm"]
    CC --> P[Answer 8 prompts]
    P --> R{Render templates}

    R --> SRC["src/ — typed workflow\n+ config models"]
    R --> LLM[".llm/ — source of truth\nfor all LLM context"]
    R --> KB["knowledge_base/\nliving architecture docs"]
    R --> CI["CI/CD for selected\nplatform"]

    LLM --> CL["CLAUDE.md ≤200 lines\n(Claude Code)"]
    LLM --> AG["AGENTS.md ≤200 lines\n(Codex / other agents)"]

    SRC & CL & AG & KB & CI --> H["post_gen_project.py\nhook"]
    H --> RM["Remove unused\nplatform files"]
    H --> TS["Configure\ntest scheme"]
    H --> GI["git init +\ninitial commit"]
    GI --> DONE(["✅ your-package/ ready\njust setup && just test"])
```

The post-gen hook runs once and leaves the project in a clean, committed state
with only the files you asked for.

---

## What you get

```
my-eo-package/
├── src/my_eo_package/       ← importable package (snake_case)
│   ├── logger.py            ← get_logger(name) for consistent logging
│   ├── workflow/            ← abstract base + concrete implementation
│   ├── config/              ← SourceModel / ComputeParamsModel / DestinationModel
│   └── main.py              ← typer CLI + run_<project_slug>() entry point
├── .llm/                    ← single source of truth for LLM context
├── knowledge_base/          ← living architecture docs
├── tests/                   ← unit / integration / approval suites
├── CLAUDE.md                ← rendered from .llm/ (≤200 lines)
├── AGENTS.md                ← rendered from .llm/ (≤200 lines)
├── Justfile                 ← all dev commands in one place
└── pyproject.toml           ← hatchling + uv, fully wired
```

---

## Quick install

```bash
uvx cookiecutter gh:pmuguda/cookiecutter-eo-llm
```

→ [Full quickstart guide](quickstart.md)

---

## What you configure at scaffold time

Eight prompts control the entire project shape. Six of them are **feature
flags** — the post-gen hook removes any files that don't apply.

```mermaid
flowchart LR
    subgraph llm ["primary_llm"]
        LB([both]) --> CLMD[CLAUDE.md\n+ AGENTS.md]
        LC([claude]) --> CLMD2[CLAUDE.md only]
        LD([codex]) --> AGMD[AGENTS.md only]
    end

    subgraph ci ["ci_platform"]
        CG([github]) --> GHA[.github/workflows/]
        CGL([gitlab]) --> GLC[.gitlab-ci.yml]
    end

    subgraph ts ["test_scheme"]
        TF([full]) --> TALL[unit + approval\n+ hypothesis]
        TU([unit_and_approval]) --> TUA[unit + approval]
        TUN([unit]) --> TUO[unit only]
    end

    subgraph mk ["include_mkdocs"]
        MY([y]) --> MKYES[docs/ included]
        MN([n]) --> MKNO[docs/ removed]
    end
```

→ [Full variable reference](variables.md)

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
