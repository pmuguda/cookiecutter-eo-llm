from unittest.mock import MagicMock, patch

from {{cookiecutter.project_slug}}.config.models import (
    ComputeParamsModel,
    DestinationModel,
    SourceModel,
    WorkflowConfigModel,
)
from {{cookiecutter.project_slug}}.main import run


def test_run_calls_workflow_validate_and_run() -> None:
    config = WorkflowConfigModel(
        name="test",
        source=SourceModel(input_path="a.tif", crs="EPSG:4326"),
        compute_params=ComputeParamsModel(),
        destination=DestinationModel(output_path="b.tif"),
    )
    mock_instance = MagicMock()
    mock_class = MagicMock(return_value=mock_instance)

    with patch("{{cookiecutter.project_slug}}.main.Workflow", mock_class):
        run(config)

    mock_class.assert_called_once_with(config)
    mock_instance.validate.assert_called_once()
    mock_instance.run.assert_called_once()
