from pathlib import Path

import typer

from {{cookiecutter.project_slug}}.config.models import WorkflowConfig, register_yaml_tags
from {{cookiecutter.project_slug}}.workflows.example import ExampleWorkflow

app = typer.Typer()

WORKFLOW_REGISTRY: dict[str, type] = {
    "ExampleWorkflow": ExampleWorkflow,
}


def run(config_path: Path) -> None:
    register_yaml_tags()
    config = WorkflowConfig.from_yaml(config_path)
    workflow_class = WORKFLOW_REGISTRY[config.type]
    workflow = workflow_class(config)
    workflow.validate()
    workflow.run()


@app.command()
def cli(
    config: Path = typer.Argument(..., help="Path to workflow YAML config"),
) -> None:
    run(config)


if __name__ == "__main__":
    app()
