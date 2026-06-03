from pathlib import Path

import pytest
from pydantic import ValidationError

from {{cookiecutter.project_slug}}.config.models import WorkflowConfig, register_yaml_tags


@pytest.fixture(autouse=True)
def register() -> None:
    register_yaml_tags()


def test_from_yaml_loads_valid_config(tmp_path: Path) -> None:
    yaml_file = tmp_path / "wf.yaml"
    yaml_file.write_text(
        "workflow: !workflow\n"
        "  name: test\n"
        "  type: ExampleWorkflow\n"
        "  parameters:\n"
        "    input_path: a.tif\n"
        "    output_path: b.tif\n"
        "    crs: EPSG:4326\n"
    )
    config = WorkflowConfig.from_yaml(yaml_file)
    assert config.name == "test"
    assert config.type == "ExampleWorkflow"
    assert config.parameters["crs"] == "EPSG:4326"


def test_from_yaml_raises_on_missing_name(tmp_path: Path) -> None:
    yaml_file = tmp_path / "wf.yaml"
    yaml_file.write_text(
        "workflow: !workflow\n"
        "  type: ExampleWorkflow\n"
        "  parameters:\n"
        "    input_path: a.tif\n"
    )
    with pytest.raises(ValidationError):
        WorkflowConfig.from_yaml(yaml_file)


def test_workflow_config_direct_construction() -> None:
    config = WorkflowConfig(name="x", type="T", parameters={"k": "v"})
    assert config.name == "x"
