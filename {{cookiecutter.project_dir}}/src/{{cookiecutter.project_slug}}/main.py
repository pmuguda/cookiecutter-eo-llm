from pathlib import Path

import typer

from {{cookiecutter.project_slug}}.config.models import WorkflowConfigModel
from {{cookiecutter.project_slug}}.logger import get_logger
from {{cookiecutter.project_slug}}.workflows.example import ExampleWorkflow

app = typer.Typer()
_log = get_logger(__name__)

WORKFLOW_REGISTRY: dict[str, type] = {
    "ExampleWorkflow": ExampleWorkflow,
}


def run(config_path: Path) -> None:
    config = WorkflowConfigModel.from_yaml(config_path)
    _log.info("workflow: %s (%s)", config.name, config.type)
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
