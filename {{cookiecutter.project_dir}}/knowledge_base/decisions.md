# Design decisions

## Abstract base class over Protocol

`Workflow` uses `ABC` and `abstractmethod` rather than a `Protocol`.
Subclasses share `__init__` logic and benefit from explicit inheritance.
Protocol would require duck-typing checks instead of `isinstance` guarantees.

## Pydantic v2 over dataclasses for config

Pydantic v2 provides field validation, coercion, and clear error messages
out of the box. Dataclasses require manual validators. YAML loading errors
surface as `ValidationError` with field-level detail.

## Plain YAML over custom tags

`!workflow` custom tags were removed. `yaml.safe_load()` + `WorkflowConfigModel.model_validate()`
is simpler, dependency-free, and easier to test. Dispatch happens via `WORKFLOW_REGISTRY`
in `main.py` — no PyYAML magic needed.

## Empty base models over a flat parameters dict

`SourceModel`, `ComputeParamsModel`, `DestinationModel` are empty bases with `extra="allow"`.
This enforces the source / compute / destination separation at the schema level while
leaving field definitions to each concrete workflow. The base models are re-validated
into concrete subclasses inside `Workflow.__init__`, giving full mypy coverage per workflow.

## typer over argparse/click

typer generates a CLI from type annotations with zero boilerplate.
It integrates with the existing type-annotation discipline across the codebase.

## kebab / snake naming split

PyPI and filesystem use kebab-case (`my-eo-package`) to follow packaging conventions.
Python imports use snake_case (`my_eo_package`) because Python identifiers forbid hyphens.
One cookiecutter variable per convention keeps the split explicit and unambiguous.
