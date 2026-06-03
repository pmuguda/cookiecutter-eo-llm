from pathlib import Path

import typer

from {{cookiecutter.project_slug}}.config.models import WorkflowConfigModel
from {{cookiecutter.project_slug}}.logger import get_logger
from {{cookiecutter.project_slug}}.workflows.example import ExampleWorkflow as Workflow

app = typer.Typer()
_log = get_logger(__name__)


def run(config_path: Path) -> None:
    config = WorkflowConfigModel.from_yaml(config_path)
    _log.info("starting: %s", config.name)
    workflow = Workflow(config)
    workflow.validate()
    workflow.run()


@app.command()
def cli(
    config: Path = typer.Argument(..., help="Path to workflow YAML config"),
) -> None:
    run(config)


if __name__ == "__main__":
    app()
