from pathlib import Path
from unittest.mock import MagicMock, patch

from {{cookiecutter.project_slug}}.main import run


def test_run_calls_workflow_validate_and_run(tmp_path: Path) -> None:
    config_file = tmp_path / "workflow.yaml"
    config_file.write_text(
        "name: test\n"
        "source:\n"
        "  input_path: a.tif\n"
        "  crs: EPSG:4326\n"
        "compute_params: {}\n"
        "destination:\n"
        "  output_path: b.tif\n"
    )
    mock_instance = MagicMock()
    mock_class = MagicMock(return_value=mock_instance)

    with patch("{{cookiecutter.project_slug}}.main.Workflow", mock_class):
        run(config_file)

    mock_class.assert_called_once()
    mock_instance.validate.assert_called_once()
    mock_instance.run.assert_called_once()
