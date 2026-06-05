from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import typer

from {{cookiecutter.project_slug}}.config.models import (
    ComputeParamsModel,
    DestinationModel,
    SourceModel,
    WorkflowConfigModel,
)
from {{cookiecutter.project_slug}}.main import load_config, run_{{cookiecutter.project_slug}}


def test_run_project_calls_workflow_run() -> None:
    config = WorkflowConfigModel(
        name="test",
        source=SourceModel(input_path="a.tif", crs="EPSG:4326"),
        compute_params=ComputeParamsModel(),
        destination=DestinationModel(output_path="b.tif"),
    )
    mock_instance = MagicMock()
    mock_class = MagicMock(return_value=mock_instance)

    with patch("{{cookiecutter.project_slug}}.main.Workflow", mock_class):
        run_{{cookiecutter.project_slug}}(config)

    mock_class.assert_called_once_with(config)
    mock_instance.run.assert_called_once()


def test_load_config_raises_for_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "missing.yml"

    with pytest.raises(typer.BadParameter, match="Config file does not exist"):
        load_config(missing)
