import pytest

from {{cookiecutter.project_slug}}.config.models import WorkflowConfig
from {{cookiecutter.project_slug}}.workflows.example import ExampleWorkflow


def make_config(parameters: dict) -> WorkflowConfig:  # type: ignore[type-arg]
    return WorkflowConfig(name="test", type="ExampleWorkflow", parameters=parameters)


@pytest.mark.parametrize(
    "parameters",
    [
        {"input_path": "a.tif", "output_path": "b.tif", "crs": "EPSG:4326"},
        {"input_path": "x.tif", "output_path": "y.tif", "crs": "EPSG:32632"},
    ],
)
def test_example_workflow_run_succeeds(parameters: dict) -> None:  # type: ignore[type-arg]
    workflow = ExampleWorkflow(make_config(parameters))
    workflow.run()


def test_example_workflow_validate_raises_on_missing_crs() -> None:
    config = make_config({"input_path": "a.tif", "output_path": "b.tif"})
    workflow = ExampleWorkflow(config)
    with pytest.raises(ValueError, match="crs"):
        workflow.validate()


def test_example_workflow_validate_raises_on_missing_input() -> None:
    config = make_config({"output_path": "b.tif", "crs": "EPSG:4326"})
    workflow = ExampleWorkflow(config)
    with pytest.raises(ValueError, match="input_path"):
        workflow.validate()
