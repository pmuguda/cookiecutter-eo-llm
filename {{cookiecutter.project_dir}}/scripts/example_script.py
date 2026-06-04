from pathlib import Path

from {{cookiecutter.project_slug}}.config.models import WorkflowConfigModel
from {{cookiecutter.project_slug}}.main import run


def main() -> None:
    config = WorkflowConfigModel.from_yaml(
        Path("config/config_{{cookiecutter.project_slug}}.yml")
    )
    run(config)


if __name__ == "__main__":
    main()
