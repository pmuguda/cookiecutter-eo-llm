from pathlib import Path

import pytest
from pydantic import ValidationError

from {{cookiecutter.project_slug}}.config.models import (
    ComputeParamsModel,
    DestinationModel,
    SourceModel,
    WorkflowConfigModel,
)


def test_source_model_accepts_arbitrary_fields() -> None:
    src = SourceModel(input_path="data/input.tif", crs="EPSG:4326")
    assert src.model_extra["input_path"] == "data/input.tif"
    assert src.model_extra["crs"] == "EPSG:4326"


def test_compute_params_model_is_empty_by_default() -> None:
    params = ComputeParamsModel()
    assert params.model_extra == {}


def test_compute_params_model_accepts_arbitrary_fields() -> None:
    params = ComputeParamsModel(resampling="nearest", window_size=5)
    assert params.model_extra["resampling"] == "nearest"


def test_destination_model_accepts_arbitrary_fields() -> None:
    dst = DestinationModel(output_path="data/out.tif", overwrite=False)
    assert dst.model_extra["output_path"] == "data/out.tif"


def test_workflow_config_model_requires_name(tmp_path: Path) -> None:
    f = tmp_path / "wf.yaml"
    f.write_text(
        "type: ExampleWorkflow\n"
        "source:\n  input_path: data/input.tif\n"
        "compute_params: {}\n"
        "destination:\n  output_path: data/output.tif\n"
    )
    with pytest.raises(ValidationError):
        WorkflowConfigModel.from_yaml(f)


def test_workflow_config_model_requires_type(tmp_path: Path) -> None:
    f = tmp_path / "wf.yaml"
    f.write_text(
        "name: test\n"
        "source:\n  input_path: data/input.tif\n"
        "compute_params: {}\n"
        "destination:\n  output_path: data/output.tif\n"
    )
    with pytest.raises(ValidationError):
        WorkflowConfigModel.from_yaml(f)


def test_workflow_config_model_from_yaml_loads_all_sections(tmp_path: Path) -> None:
    f = tmp_path / "wf.yaml"
    f.write_text(
        "name: test-run\n"
        "type: ExampleWorkflow\n"
        "source:\n"
        "  input_path: data/input.tif\n"
        "  crs: EPSG:32632\n"
        "compute_params:\n"
        "  resampling: nearest\n"
        "destination:\n"
        "  output_path: data/output.tif\n"
        "  overwrite: true\n"
    )
    config = WorkflowConfigModel.from_yaml(f)
    assert config.name == "test-run"
    assert config.type == "ExampleWorkflow"
    assert config.source.model_extra["crs"] == "EPSG:32632"
    assert config.compute_params.model_extra["resampling"] == "nearest"
    assert config.destination.model_extra["overwrite"] is True


def test_workflow_config_model_compute_params_defaults_to_empty(tmp_path: Path) -> None:
    f = tmp_path / "wf.yaml"
    f.write_text(
        "name: test\n"
        "type: ExampleWorkflow\n"
        "source:\n  input_path: data/input.tif\n"
        "destination:\n  output_path: data/output.tif\n"
    )
    config = WorkflowConfigModel.from_yaml(f)
    assert config.compute_params.model_extra == {}
