from pathlib import Path

from {{cookiecutter.project_slug}}.config.models import WorkflowConfig


def build_example_config(
    input_path: str = "data/input.tif",
    output_path: str = "data/output.tif",
    crs: str = "EPSG:4326",
) -> WorkflowConfig:
    return WorkflowConfig(
        name="test-example",
        type="ExampleWorkflow",
        parameters={
            "input_path": input_path,
            "output_path": output_path,
            "crs": crs,
        },
    )


def build_config_from_yaml(path: Path) -> WorkflowConfig:
    return WorkflowConfig.from_yaml(path)
