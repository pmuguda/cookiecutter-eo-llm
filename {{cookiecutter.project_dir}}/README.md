# {{cookiecutter.project_name}}

[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_dir}})](https://pypi.org/project/{{cookiecutter.project_dir}}/)
[![License](https://img.shields.io/badge/license-{{cookiecutter.license}}-blue)](LICENSE)
{% if cookiecutter.ci_platform == "github" -%}
[![CI](https://github.com/{{cookiecutter.repository_owner}}/{{cookiecutter.project_dir}}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{cookiecutter.repository_owner}}/{{cookiecutter.project_dir}}/actions)
{% else -%}
[![Pipeline](https://gitlab.com/{{cookiecutter.repository_owner}}/{{cookiecutter.project_dir}}/badges/main/pipeline.svg)](https://gitlab.com/{{cookiecutter.repository_owner}}/{{cookiecutter.project_dir}}/-/pipelines)
{% endif -%}
[![Python](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_dir}})](https://pypi.org/project/{{cookiecutter.project_dir}}/)

{{cookiecutter.project_short_description}}

## Installation

```bash
uv add {{cookiecutter.project_dir}}
```

## Quick start

```bash
{{cookiecutter.project_dir}} config/config_{{cookiecutter.project_slug}}.yml
```

Or from Python:

```python
from pathlib import Path

from {{cookiecutter.project_slug}}.config.models import WorkflowConfigModel
from {{cookiecutter.project_slug}}.main import run

config = WorkflowConfigModel.from_yaml(Path("config/config_{{cookiecutter.project_slug}}.yml"))
run(config)
```

## Configuration

This package is built around one workflow. The CLI loads a plain YAML file into
`WorkflowConfigModel`, then passes that Pydantic object to `run(config)`.

```yaml
name: {{cookiecutter.project_slug}}-run
source:
  input_path: data/input.tif
  crs: EPSG:32632
compute_params: {}
destination:
  output_path: data/output.tif
  overwrite: false
```

No custom YAML tags. No registry. The concrete workflow owns its typed source,
compute, and destination models.

## Implementing your workflow

1. Rename `src/{{cookiecutter.project_slug}}/workflow/example.py`
2. Implement `run(self) -> None` and `validate(self) -> None`
3. Update the single workflow import in `src/{{cookiecutter.project_slug}}/main.py`
4. Update `config/config_{{cookiecutter.project_slug}}.yml`
5. Add tests in `tests/unit/`
6. Update `knowledge_base/workflows.md` and docs when behavior changes

## Development setup

```bash
just setup
just test
just update-context
```

## Commands

| Command | Description |
|---------|-------------|
| `just setup` | Install deps + pre-commit hooks |
| `just lint` | Run ruff check |
| `just format` | Run ruff format |
| `just typecheck` | Run mypy |
| `just check` | lint + typecheck |
| `just test` | Full test suite |
| `just test-unit` | Unit tests only |
| `just test-approval` | Approval/snapshot tests |
| `just test-cov` | Coverage HTML report |
| `just docs` | Serve docs locally |
| `just update-context` | Refresh `knowledge_base/code_map.md` and `current_state.md` |
| `just bump patch` | 0.1.0 → 0.1.1 |
| `just bump minor` | 0.1.0 → 0.2.0 |
| `just bump major` | 0.1.0 → 1.0.0 |
| `just build` | Build distribution |
| `just publish` | Publish to PyPI |

## Commit convention

This project follows [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

| Prefix | SemVer bump |
|--------|-------------|
| `fix:` | PATCH |
| `feat:` | MINOR |
| `feat!:` / `BREAKING CHANGE` | MAJOR |

## Knowledge base

`knowledge_base/` contains living architecture docs. Update the relevant file
with every PR that changes architecture, adds a workflow, or makes a significant
design decision.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

{{cookiecutter.license}} © {{cookiecutter.full_name}}
