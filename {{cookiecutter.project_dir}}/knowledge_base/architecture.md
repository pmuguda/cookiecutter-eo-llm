# Architecture

## Package layout

```
src/{{cookiecutter.project_slug}}/
├── __init__.py
├── py.typed
├── main.py          — run() entry point + typer CLI
├── workflows/
│   ├── base.py      — abstract Workflow base class
│   └── example.py  — one concrete implementation
└── config/
    └── models.py    — WorkflowConfig (Pydantic v2) + YAML tag registration
```

## Workflow abstract class

`Workflow` in `workflows/base.py` defines the contract:
- `__init__(self, config: WorkflowConfig)` — receives validated config
- `run(self) -> None` — execute the workflow
- `validate(self) -> None` — validate inputs before running

Every concrete workflow must implement both methods.

## YAML tag instantiation

`register_yaml_tags()` in `config/models.py` registers PyYAML constructors.
The `!workflow` tag auto-instantiates the correct subclass based on `type:`.
Adding a new workflow: register one new YAML tag. Nothing else changes.

## WorkflowConfig

Pydantic v2 `BaseModel` with three fields:
- `name: str` — human-readable workflow name
- `type: str` — maps to the concrete Workflow subclass name
- `parameters: dict[str, object]` — workflow-specific inputs

`WorkflowConfig.from_yaml(path)` loads and validates the YAML file.

## How to add a new workflow

1. Create `src/{{cookiecutter.project_slug}}/workflows/<name>.py`
2. Subclass `Workflow`, implement `run()` and `validate()`
3. Register a YAML tag in `config/models.py`
4. Add tests in `tests/unit/test_<name>_workflow.py`
5. Update `knowledge_base/workflows.md`
