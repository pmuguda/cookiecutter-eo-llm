from pathlib import Path

from {{cookiecutter.project_slug}}.config.models import (
    ComputeParamsModel,
    DestinationModel,
    SourceModel,
    WorkflowConfigModel,
)
from {{cookiecutter.project_slug}}.logger import get_logger
from {{cookiecutter.project_slug}}.workflows.base import Workflow

_log = get_logger(__name__)


class ExampleSource(SourceModel):
    """Concrete source model for ExampleWorkflow."""

    input_path: Path
    crs: str = "EPSG:4326"


class ExampleComputeParams(ComputeParamsModel):
    """Concrete compute params for ExampleWorkflow — extend as needed."""


class ExampleDestination(DestinationModel):
    """Concrete destination model for ExampleWorkflow."""

    output_path: Path
    overwrite: bool = False


class ExampleWorkflow(Workflow):
    def __init__(self, config: WorkflowConfigModel) -> None:
        super().__init__(config)
        self.source = ExampleSource.model_validate(config.source.model_dump())
        self.compute = ExampleComputeParams.model_validate(
            config.compute_params.model_dump()
        )
        self.destination = ExampleDestination.model_validate(
            config.destination.model_dump()
        )

    def validate(self) -> None:
        if not self.source.input_path.suffix:
            raise ValueError("source.input_path must have a file extension")
        if not self.destination.output_path.suffix:
            raise ValueError("destination.output_path must have a file extension")

    def run(self) -> None:
        self.validate()
        _log.info("source:    %s", self.source.input_path)
        _log.info("crs:       %s", self.source.crs)
        _log.info("output:    %s", self.destination.output_path)
        _log.info("overwrite: %s", self.destination.overwrite)
