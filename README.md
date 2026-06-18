<p align="center">
  <img src="https://pmuguda.github.io/cookiecutter-eo-llm/assets/icon.svg?v=3" width="120" alt="cookiecutter-eo-llm logo"/>
</p>

<h1 align="center">cookiecutter-eo-llm</h1>

[![CI](https://github.com/pmuguda/cookiecutter-eo-llm/actions/workflows/ci.yml/badge.svg)](https://github.com/pmuguda/cookiecutter-eo-llm/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-github%20pages-blue?logo=readthedocs&logoColor=white)](https://pmuguda.github.io/cookiecutter-eo-llm/)
[![Coverage](https://pmuguda.github.io/cookiecutter-eo-llm/badges/coverage.svg)](https://pmuguda.github.io/cookiecutter-eo-llm/)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white)](https://github.com/pmuguda/cookiecutter-eo-llm)
[![License](https://img.shields.io/github/license/pmuguda/cookiecutter-eo-llm)](LICENSE)
[![Buy me a coffee](https://img.shields.io/badge/buy%20me%20a%20coffee-ko--fi-FF5E5B?logo=ko-fi&logoColor=white)](https://ko-fi.com/pavan_muguda)

A production-minded EO/SAR Python package template with TDD workflows and
LLM-ready context for Claude Code and Codex.

It gives you a typed, tested workflow scaffold from day one: plain YAML config,
a single concrete workflow, strict Python tooling, living architecture docs, and
LLM context files generated from one `.llm/` source of truth.

---

## Use

```bash
uvx cookiecutter gh:pmuguda/cookiecutter-eo-llm
```

Then:

```bash
cd my-eo-package
just setup
just test
just run config/config_my_eo_package.yml
```

→ [Full documentation](https://pmuguda.github.io/cookiecutter-eo-llm/)

---

## What you get

| Feature | Detail |
|---------|--------|
| `src/` layout | `project_dir` (kebab) for PyPI · `project_slug` (snake) for imports |
| Workflow pattern | Abstract `Workflow(ABC)` · one workflow per package · Pydantic v2 config |
| LLM context | CLAUDE.md + AGENTS.md + `.llm/skills.md` from a single `.llm/` source |
| Living docs | `knowledge_base/` — architecture, workflows, decisions, changelog, code map, current state |
| Full test suite | unit · integration · approval stubs · hypothesis |
| CI/CD | Choose GitHub Actions or GitLab CI at scaffold time |
| Developer UX | Justfile · ruff · mypy strict · pre-commit · bump-my-version |

`just update-context` refreshes `knowledge_base/code_map.md` and
`knowledge_base/current_state.md` so new Claude Code/Codex sessions can orient
quickly without a third-party indexing dependency.

---

## Template variables

| Variable | Default | Notes |
|----------|---------|-------|
| `project_name` | `My EO Package` | Title case — drives `project_dir` and `project_slug` |
| `repository_owner` | `chucknorris` | GitHub username, GitLab username, or GitLab group |
| `primary_llm` | `both` | `both` · `claude` · `codex` — controls which LLM context files are kept |
| `ci_platform` | `github` | `github` · `gitlab` — removes the unused platform's files |
| `test_scheme` | `full` | `unit` · `unit_and_approval` · `full` |
| `include_mkdocs` | `y` | Removes `docs/` when `n` |
| `open_source` | `y` | Reserved — will gate PyPI publish config in a future release |

→ [Full variable reference](https://pmuguda.github.io/cookiecutter-eo-llm/variables/)

---

## Template development

```bash
git clone https://github.com/pmuguda/cookiecutter-eo-llm
cd cookiecutter-eo-llm
uv sync --dev
uv run pytest          # 69 tests
```

Render locally:

```bash
uvx cookiecutter . --no-input -o /tmp/eo-test
```

---

## Why it matters

EO/SAR projects often start as notebooks and grow into fragile scripts that
LLM assistants can't reliably navigate because there's no documented structure,
no tests, and no consistent entry point.

This template sets up a package boundary before that drift happens:

- One workflow class, one config file, typed source / compute / destination sections
- Tests and type coverage from the first commit
- `.llm/` context files that keep Claude Code and Codex grounded in your project's rules
- `knowledge_base/` that preserves architectural decisions across sessions
- `just update-context` that refreshes a compact code map without third-party tools

The template intentionally keeps heavy EO libraries optional. Add numpy, xarray,
rasterio, pyproj, shapely, or GDAL only when your workflow needs them.

---

## Credits

Built on excellent open-source tooling: Cookiecutter, uv, hatchling, ruff, mypy,
pytest, Pydantic, Typer, PyYAML, MkDocs, GitHub Actions, and GitLab CI.

---

## License

MIT © Pavan Muguda Sanjeevamurthy
