import pytest

from {{cookiecutter.project_slug}}.config.models import (
    ComputeParamsModel,
    DestinationModel,
    SourceModel,
    WorkflowConfigModel,
)
from {{cookiecutter.project_slug}}.workflows.example import ExampleWorkflow


def make_config(
    input_path: str = "data/input.tif",
    output_path: str = "data/output.tif",
    crs: str = "EPSG:4326",
) -> WorkflowConfigModel:
    return WorkflowConfigModel(
        name="test",
        source=SourceModel(input_path=input_path, crs=crs),
        compute_params=ComputeParamsModel(),
        destination=DestinationModel(output_path=output_path),
    )


@pytest.mark.parametrize(
    "input_path,output_path,crs",
    [
        ("data/input.tif", "data/output.tif", "EPSG:4326"),
        ("stack/slc.zarr", "result/coh.tif", "EPSG:32632"),
    ],
)
def test_example_workflow_run_succeeds(
    input_path: str, output_path: str, crs: str
) -> None:
    workflow = ExampleWorkflow(make_config(input_path, output_path, crs))
    workflow.run()


def test_example_workflow_validate_raises_on_missing_input_extension() -> None:
    workflow = ExampleWorkflow(make_config(input_path="data/no-extension"))
    with pytest.raises(ValueError, match="input_path"):
        workflow.validate()


def test_example_workflow_validate_raises_on_missing_output_extension() -> None:
    workflow = ExampleWorkflow(make_config(output_path="data/no-extension"))
    with pytest.raises(ValueError, match="output_path"):
        workflow.validate()
