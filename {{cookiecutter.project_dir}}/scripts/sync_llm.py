"""Generate CLAUDE.md and AGENTS.md from the .llm/ source of truth.

.llm/ holds the project content (identity, stack, commands, boundaries, skills).
This script holds the fixed document structure and the cross-project framing
(development rules, code style, git workflow). Together they make .llm/ the
single source of truth for everything project-specific: edit .llm/, run
`just sync-llm`, and both context files are rebuilt identically every time.

Modes:
    (default)   rebuild whichever of CLAUDE.md / AGENTS.md already exist
    --init      create both files (used by the scaffold hook)
    --check     exit non-zero if either existing file is out of sync
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LLM = ROOT / ".llm"
FOOTER = "---\nSource of truth: .llm/  |  Keep this file under 200 lines"

REQUIRED_KNOWLEDGE = """## Required knowledge

To contribute effectively, understand:
- Current state and code map: knowledge_base/current_state.md, knowledge_base/code_map.md
- SAR/EO concepts relevant to this package (see knowledge_base/)
- Pydantic v2: BaseModel, model_validate, ConfigDict, extra="allow"
- Python ABC and abstractmethod patterns
- Geospatial: CRS, EPSG codes, coordinate transforms
- uv for dependency management — no pip"""

DEVELOPMENT_RULES = """## Development rules

- TDD: failing test → minimum code → refactor. Small steps always.
- SOLID: one responsibility per function and class.
- No comments — rename and simplify instead.
- Type-annotate every argument and return value. mypy strict must pass.
- One package = one workflow. Rename ExampleWorkflow; update the import in main.py.
- Update knowledge_base/ whenever architecture changes.
- Conventional Commits on every commit — see .llm/boundaries.md.
- Never add LLM co-author footers to commits."""

ROLE = """## Role

You are assisting with an EO/SAR Python package.
Write clean, typed, tested geospatial code.
Follow TDD and SOLID principles at all times.
Never add LLM attribution to commit messages or file headers."""

CODE_STYLE = """## Code style

- ruff, line-length 100
- mypy strict — every argument and return value typed
- NumPy docstrings
- No comments — readable names over explanatory text
- kebab-case for folders and PyPI name
- snake_case for Python imports and module names"""

GIT_WORKFLOW = """## Git workflow

### Branch naming
```
feat/<short-slug>
fix/<short-slug>
chore/<short-slug>
docs/<short-slug>
refactor/<short-slug>
```

### Commit format (Conventional Commits 1.0.0)
```
<type>[optional scope]: <description>
```

Types: `feat` `fix` `docs` `style` `refactor` `perf` `test` `build` `ci` `chore` `revert`

Breaking change: append `!` or add `BREAKING CHANGE:` footer.

SemVer: `fix` → PATCH · `feat` → MINOR · `BREAKING CHANGE` → MAJOR

- Description lowercase, no trailing period
- One logical change per commit
- Never add co-author footers from LLMs
- Version bumps via: `just bump <patch|minor|major>`"""


def read(name: str) -> str:
    return (LLM / f"{name}.md").read_text().strip()


def demote_headings(text: str) -> str:
    rows = [("#" + line if line.startswith("#") else line) for line in text.splitlines()]
    return "\n".join(rows)


def body_after_heading(text: str) -> str:
    rows = text.splitlines()
    if rows and rows[0].lstrip().startswith("#"):
        rows = rows[1:]
    return "\n".join(rows).strip()


def context_parts() -> tuple[str, str, str]:
    rows = read("context").splitlines()
    title = rows[0].strip()
    description = ""
    meta: list[str] = []
    for row in rows[1:]:
        stripped = row.strip()
        if not stripped:
            continue
        if stripped.startswith("-"):
            meta.append(stripped)
        elif not description:
            description = stripped
    return title, description, "\n".join(meta)


def fenced(body: str) -> str:
    return "```\n" + body + "\n```"


def join(parts: list[str]) -> str:
    return "\n\n".join(part.strip() for part in parts if part.strip()) + "\n"


def build_claude() -> str:
    title, description, _ = context_parts()
    return join(
        [
            f"{title}\n\n{description}",
            REQUIRED_KNOWLEDGE,
            DEVELOPMENT_RULES,
            "## Stack\n\n" + demote_headings(read("stack")),
            demote_headings(read("skills")),
            "## Commands\n\n" + fenced(body_after_heading(read("commands"))),
            "## Boundaries\n\n" + demote_headings(read("boundaries")),
            FOOTER,
        ]
    )


def build_agents() -> str:
    title, _, meta = context_parts()
    name = title.lstrip("# ").strip()
    return join(
        [
            f"# AGENTS.md — {name}",
            ROLE,
            "## Project knowledge\n\n" + meta,
            demote_headings(read("stack")),
            demote_headings(read("skills")),
            "## Commands\n\n" + fenced(body_after_heading(read("commands"))),
            CODE_STYLE,
            "## Boundaries\n\n" + demote_headings(read("boundaries")),
            GIT_WORKFLOW,
            FOOTER,
        ]
    )


def targets() -> dict[str, str]:
    return {"CLAUDE.md": build_claude(), "AGENTS.md": build_agents()}


def check() -> int:
    drifted = [
        name
        for name, content in targets().items()
        if (ROOT / name).exists() and (ROOT / name).read_text() != content
    ]
    if drifted:
        joined = ", ".join(drifted)
        print(f"Out of sync with .llm/: {joined} — run `just sync-llm`", file=sys.stderr)
        return 1
    return 0


def write(init: bool) -> int:
    for name, content in targets().items():
        path = ROOT / name
        if init or path.exists():
            path.write_text(content)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync CLAUDE.md and AGENTS.md from .llm/")
    parser.add_argument("--check", action="store_true", help="fail if files are out of sync")
    parser.add_argument("--init", action="store_true", help="create both files")
    args = parser.parse_args()
    return check() if args.check else write(args.init)


if __name__ == "__main__":
    raise SystemExit(main())
