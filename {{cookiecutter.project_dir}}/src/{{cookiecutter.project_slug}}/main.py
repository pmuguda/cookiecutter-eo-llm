from pathlib import Path

import typer

from {{cookiecutter.project_slug}}.config.models import WorkflowConfigModel
from {{cookiecutter.project_slug}}.logger import get_logger
from {{cookiecutter.project_slug}}.workflow.example import ExampleWorkflow as Workflow

app = typer.Typer()
_log = get_logger(__name__)


def run(config: WorkflowConfigModel) -> None:
    _log.info("starting: %s", config.name)
    workflow = Workflow(config)
    workflow.validate()
    workflow.run()


@app.command()
def cli(
    config_path: Path = typer.Argument(..., help="Path to workflow YAML config"),
) -> None:
    run(WorkflowConfigModel.from_yaml(config_path))


if __name__ == "__main__":
    app()
