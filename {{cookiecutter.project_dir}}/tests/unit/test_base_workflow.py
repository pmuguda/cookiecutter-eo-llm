import pytest

from {{cookiecutter.project_slug}}.workflows.base import Workflow


def test_workflow_cannot_be_instantiated_directly() -> None:
    with pytest.raises(TypeError):
        Workflow(config=None)  # type: ignore[arg-type]
