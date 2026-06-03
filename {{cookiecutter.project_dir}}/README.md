# {{cookiecutter.project_name}}

[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_dir}})](https://pypi.org/project/{{cookiecutter.project_dir}}/)
[![License](https://img.shields.io/badge/license-{{cookiecutter.license}}-blue)](LICENSE)
[![CI](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_dir}}/actions/workflows/ci.yml/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_dir}}/actions)
[![Python](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_dir}})](https://pypi.org/project/{{cookiecutter.project_dir}}/)

{{cookiecutter.project_short_description}}

## Installation

```bash
uv add {{cookiecutter.project_dir}}
```

## Quick start

```bash
{{cookiecutter.project_dir}} config/example_workflow.yaml
```

Or from Python:

```python
from {{cookiecutter.project_slug}}.main import run
from pathlib import Path

run(Path("config/example_workflow.yaml"))
```

## Configuration

Workflows are defined in YAML using tagged constructors:

```yaml
workflow: !workflow
  name: example
  type: ExampleWorkflow
  parameters:
    input_path: data/input.tif
    output_path: data/output.tif
    crs: EPSG:4326
```

Each `type` maps to a `Workflow` subclass. The YAML tag `!workflow` auto-instantiates
the correct class via `register_yaml_tags()` in `config/models.py`.

## Adding a new workflow

1. Subclass `Workflow` in `src/{{cookiecutter.project_slug}}/workflows/`
2. Implement `run(self) -> None` and `validate(self) -> None`
3. Register a YAML tag in `src/{{cookiecutter.project_slug}}/config/models.py`
4. Add tests in `tests/unit/` and update `knowledge_base/workflows.md`

## Development setup

```bash
just setup
just test
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
