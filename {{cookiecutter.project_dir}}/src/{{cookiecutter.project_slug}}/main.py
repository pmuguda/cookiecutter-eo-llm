from pathlib import Path

import typer

from {{cookiecutter.project_slug}}.config.models import WorkflowConfigModel
from {{cookiecutter.project_slug}}.workflow.example import ExampleWorkflow as Workflow

app = typer.Typer(help="{{cookiecutter.project_short_description}}")


def load_config(config_file: Path) -> WorkflowConfigModel:
    if not config_file.exists():
        raise typer.BadParameter(f"Config file does not exist: {config_file}")
    return WorkflowConfigModel.from_yaml(config_file)


def run_{{cookiecutter.project_slug}}(config: WorkflowConfigModel) -> None:
    workflow = Workflow(config)
    workflow.run()


@app.command(help="Run the {{cookiecutter.project_name}} workflow.")
def cli(
    config_file: Path = typer.Option(
        ...,
        "--config-file",
        "-cf",
        help="Path to workflow YAML config.",
    ),
) -> None:
    run_{{cookiecutter.project_slug}}(load_config(config_file))


if __name__ == "__main__":
    app()
