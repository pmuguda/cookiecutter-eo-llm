# cookiecutter-eo-llm

[![CI](https://github.com/pmuguda/cookiecutter-eo-llm/actions/workflows/ci.yml/badge.svg)](https://github.com/pmuguda/cookiecutter-eo-llm/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-github%20pages-blue?logo=readthedocs&logoColor=white)](https://pmuguda.github.io/cookiecutter-eo-llm/)
[![Coverage](https://pmuguda.github.io/cookiecutter-eo-llm/badges/coverage.svg)](https://pmuguda.github.io/cookiecutter-eo-llm/)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white)](https://github.com/pmuguda/cookiecutter-eo-llm)
[![License](https://img.shields.io/github/license/pmuguda/cookiecutter-eo-llm)](LICENSE)

Cookiecutter template for **Earth Observation / SAR Python packages** with
token-efficient, LLM-agnostic context files (CLAUDE.md, AGENTS.md) generated
from a single `.llm/` source of truth at scaffold time.

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
just run config/example_workflow.yaml
```

→ [Full documentation](https://pmuguda.github.io/cookiecutter-eo-llm/)

---

## What you get

| Feature | Detail |
|---------|--------|
| `src/` layout | `project_dir` (kebab) for PyPI · `project_slug` (snake) for imports |
| Workflow pattern | Abstract `Workflow(ABC)` · YAML-tag dispatch · Pydantic v2 config |
| LLM context | CLAUDE.md + AGENTS.md from a single `.llm/` source (≤200 lines each) |
| Living docs | `knowledge_base/` — architecture, workflows, decisions, changelog |
| Full test suite | unit · integration · approval stubs · hypothesis |
| CI/CD | GitHub Actions matrix (py3.10/3.11/3.12) + GitLab CI |
| Developer UX | Justfile · ruff · mypy strict · pre-commit · bump-my-version |

---

## Template variables

| Variable | Default | Notes |
|----------|---------|-------|
| `project_name` | `My EO Package` | Title case — drives `project_dir` and `project_slug` |
| `primary_llm` | `both` | `both` · `claude` · `codex` |
| `include_approval_tests` | `y` | Removes `tests/approval/` when `n` |
| `include_hypothesis` | `y` | Strips hypothesis from pyproject.toml when `n` |
| `include_mkdocs` | `y` | Removes `docs/` when `n` |
| `include_github_actions` | `y` | Removes `.github/` when `n` |
| `include_gitlab_ci` | `y` | Removes `.gitlab-ci.yml` when `n` |

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

## License

MIT © Pavan Muguda Sanjeevamurthy
