# Design decisions

## Abstract base class over Protocol

`Workflow` uses `ABC` and `abstractmethod` rather than a `Protocol`.
Subclasses share `__init__` logic and benefit from explicit inheritance.
Protocol would require duck-typing checks instead of `isinstance` guarantees.

## Pydantic v2 over dataclasses for config

Pydantic v2 provides field validation, coercion, and clear error messages
out of the box. Dataclasses require manual validators. YAML loading errors
surface as `ValidationError` with field-level detail.

## YAML tags over a registry dict

`!workflow` constructors live in PyYAML itself — no separate mapping to maintain.
Adding a workflow = adding one `yaml.add_constructor` call. No dict to update.

## typer over argparse/click

typer generates a CLI from type annotations with zero boilerplate.
It integrates with the existing type-annotation discipline across the codebase.

## kebab / snake naming split

PyPI and filesystem use kebab-case (`my-eo-package`) to follow packaging conventions.
Python imports use snake_case (`my_eo_package`) because Python identifiers forbid hyphens.
One cookiecutter variable per convention keeps the split explicit and unambiguous.
