from __future__ import annotations

import ast
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = ROOT / "src" / "{{cookiecutter.project_slug}}"
KNOWLEDGE_BASE = ROOT / "knowledge_base"


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def module_name(path: Path) -> str:
    rel = path.relative_to(PACKAGE_ROOT).with_suffix("")
    parts = [part for part in rel.parts if part != "__init__"]
    return ".".join(("{{cookiecutter.project_slug}}", *parts))


def public_symbols(path: Path) -> list[str]:
    tree = ast.parse(path.read_text())
    symbols: list[str] = []
    for node in tree.body:
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            if not node.name.startswith("_"):
                symbols.append(node.name)
    return symbols


def module_rows() -> list[str]:
    rows: list[str] = []
    for path in sorted(PACKAGE_ROOT.rglob("*.py")):
        symbols = public_symbols(path)
        summary = ", ".join(symbols) if symbols else "module constants or package marker"
        rows.append(f"- `{module_name(path)}` — `{relative(path)}` — {summary}")
    return rows


def existing_paths(paths: list[Path]) -> list[str]:
    return [f"- `{relative(path)}`" for path in paths if path.exists()]


def write_code_map() -> None:
    config_paths = sorted((ROOT / "config").glob("*.yml"))
    test_paths = [ROOT / "tests" / name for name in ("unit", "integration", "approval")]
    docs_paths = [ROOT / "README.md", ROOT / "docs", ROOT / "knowledge_base", ROOT / ".llm"]
    content = [
        "# Code map",
        "",
        "Regenerate with:",
        "",
        "```bash",
        "just update-context",
        "```",
        "",
        "This file gives humans and LLM assistants a cheap structural map before they scan the repository.",
        "",
        "## Package modules",
        "",
        *module_rows(),
        "",
        "## Config files",
        "",
        *(existing_paths(config_paths) or ["- None found"]),
        "",
        "## Test areas",
        "",
        *existing_paths(test_paths),
        "",
        "## Documentation and context",
        "",
        *existing_paths(docs_paths),
        "",
        "## Key commands",
        "",
        "- `just test` — run the full test suite",
        "- `just check` — run lint and type checks",
        "- `just run config/config_{{cookiecutter.project_slug}}.yml` — run the workflow",
        "- `just update-context` — refresh this code map and current state",
        "",
    ]
    (KNOWLEDGE_BASE / "code_map.md").write_text("\n".join(content))


def write_current_state() -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    content = [
        "# Current state",
        "",
        "Regenerate with:",
        "",
        "```bash",
        "just update-context",
        "```",
        "",
        "## Project stage",
        "",
        "- Initial scaffold generated from `cookiecutter-eo-llm`.",
        "- `ExampleWorkflow` demonstrates the source / compute / destination pattern.",
        "- The package is ready for the first real EO/SAR workflow implementation.",
        "",
        "## What to read first",
        "",
        "1. `knowledge_base/current_state.md`",
        "2. `knowledge_base/code_map.md`",
        "3. `knowledge_base/architecture.md`",
        "4. `knowledge_base/workflows.md`",
        "5. `.llm/boundaries.md`",
        "",
        "## Open implementation work",
        "",
        "- Rename `ExampleWorkflow` to the real workflow.",
        "- Update `config/config_{{cookiecutter.project_slug}}.yml`.",
        "- Add domain-specific tests before implementing behavior.",
        "- Update `knowledge_base/`, `docs/`, `AGENTS.md`, and `CLAUDE.md` when architecture changes.",
        "",
        "## Last context refresh",
        "",
        f"- {now}",
        "",
    ]
    (KNOWLEDGE_BASE / "current_state.md").write_text("\n".join(content))


def main() -> None:
    write_code_map()
    write_current_state()
    print("Updated knowledge_base/code_map.md and knowledge_base/current_state.md")


if __name__ == "__main__":
    main()
