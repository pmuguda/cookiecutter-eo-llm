# LLM Context Files

The template generates token-efficient context files for Claude Code and OpenAI Codex.
Both are rendered from the same `.llm/` source of truth at scaffold time.

---

## The .llm/ directory

Five small files that define everything an LLM assistant needs to know:

| File | Content | Hard limit |
|------|---------|-----------|
| `context.md` | Project identity: name, author, repo, Python version, license | — |
| `stack.md` | Toolchain, EO/SAR libraries, architecture summary, conventions | — |
| `commands.md` | Every `just` command with a one-line description | — |
| `boundaries.md` | Three sections: Always / Ask first / Never | — |
| `skills.md` | Useful assistant capabilities for the package: tests, typing, EO/SAR workflow design, docs, CI/CD | — |

## How this helps development

The generated package is designed for repeated collaboration with LLM coding
assistants. The context files keep the assistant grounded in project-specific
rules before it writes code:

- `AGENTS.md` and `CLAUDE.md` tell the assistant to read `knowledge_base/` first.
- `.llm/boundaries.md` makes project rules explicit: TDD, typing, CRS checks,
  docs updates, no direct pushes to main, and no LLM attribution in commits.
- `.llm/stack.md` separates required runtime dependencies from optional EO/SAR
  libraries so assistants do not add raster/geospatial packages casually.
- `.llm/skills.md` names the kind of expertise useful for the project, which helps
  assistants focus on workflow design, geospatial review, CI/CD, and documentation.
- The 200-line limit prevents context files from becoming a second documentation
  site. Deep detail belongs in `knowledge_base/` and `docs/`.

The result is a tighter loop: tests guide behavior, `.llm/` guides assistant
behavior, and `knowledge_base/` preserves the architectural decisions behind the
code.

## Context economy without extra supply-chain risk

Generated projects include two lightweight context files:

| File | Purpose |
|------|---------|
| `knowledge_base/code_map.md` | Cheap structural map of modules, configs, tests, docs, and key commands |
| `knowledge_base/current_state.md` | Current stage, first-read order, and open implementation work |

Refresh them with:

```bash
just update-context
```

The updater is a stdlib-only Python script in `scripts/update_code_map.py`.
It avoids third-party code-indexing executables while still giving Claude Code,
Codex, and other agents a low-token starting point for new sessions.

---

## CLAUDE.md

Used by [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview).
Loaded automatically when you open a project in Claude Code.

**Structure:**

```markdown
# Project name
Short description.

## Development rules   ← project-specific TDD/SOLID rules
## Stack               ← from .llm/stack.md
## Commands            ← from .llm/commands.md
## Boundaries          ← from .llm/boundaries.md

---
Source of truth: .llm/  |  Keep this file under 200 lines
```

Hard limit: **200 lines**. Enforced by `test_claude_md_under_200_lines` in `tests/test_structure.py`.

---

## AGENTS.md

Follows the [AAIF AGENTS.md specification](https://github.com/agentprotocol/aaif).
Used by OpenAI Codex and other AGENTS.md-aware tools.

**Structure:**

```markdown
# AGENTS.md — Project name

## Role          ← brief instruction to the agent
## Project knowledge   ← from .llm/context.md + .llm/stack.md
## Commands      ← from .llm/commands.md
## Code style    ← ruff/mypy/naming conventions
## Boundaries    ← from .llm/boundaries.md
## Git workflow  ← branch naming + Conventional Commits rules
```

Hard limit: **200 lines**. Enforced by `test_agents_md_under_200_lines`.

---

## primary_llm flag

| Value | Result |
|-------|--------|
| `both` (default) | CLAUDE.md + AGENTS.md generated |
| `claude` | AGENTS.md removed by post-gen hook |
| `codex` | CLAUDE.md removed by post-gen hook |

The `.llm/` directory is **always** present — it is the source of truth.

---

## Keeping context lean

Context files have a token cost on every request. Keep them under 200 lines by:

- Describing patterns, not implementations
- Linking to `knowledge_base/` for deep detail
- Deleting stale information immediately
- Never auto-generating content — write every line by hand

---

## Updating after scaffold

As the codebase evolves, update `.llm/` and then sync CLAUDE.md and AGENTS.md manually.
A future release will add a `just sync-llm` command to automate this.

For now: when you update `.llm/stack.md` or `.llm/boundaries.md`, copy the relevant
sections into CLAUDE.md and AGENTS.md. The test suite will catch any files that exceed
200 lines.
