from pathlib import Path

from {{cookiecutter.project_slug}}.config.models import (
    ComputeParamsModel,
    DestinationModel,
    SourceModel,
    WorkflowConfigModel,
)


def build_example_config(
    input_path: str = "data/input.tif",
    output_path: str = "data/output.tif",
    crs: str = "EPSG:4326",
) -> WorkflowConfigModel:
    return WorkflowConfigModel(
        name="test-example",
        type="ExampleWorkflow",
        source=SourceModel(input_path=input_path, crs=crs),
        compute_params=ComputeParamsModel(),
        destination=DestinationModel(output_path=output_path),
    )


def build_config_from_yaml(path: Path) -> WorkflowConfigModel:
    return WorkflowConfigModel.from_yaml(path)
