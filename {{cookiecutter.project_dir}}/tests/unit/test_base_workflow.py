import pytest

from {{cookiecutter.project_slug}}.config.models import (
    DestinationModel,
    SourceModel,
    WorkflowConfigModel,
)
from {{cookiecutter.project_slug}}.workflow.base import Workflow


class MinimalWorkflow(Workflow):
    def run(self) -> None:
        self.log.info("running")


def test_workflow_cannot_be_instantiated_directly() -> None:
    with pytest.raises(TypeError):
        Workflow(config=None)  # type: ignore[arg-type]


def test_workflow_base_initializes_logger() -> None:
    config = WorkflowConfigModel(
        name="test",
        source=SourceModel(),
        destination=DestinationModel(),
    )
    workflow = MinimalWorkflow(config)

    assert workflow.log.name == "MinimalWorkflow"
