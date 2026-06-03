from pathlib import Path

from {{cookiecutter.project_slug}}.main import run


def main() -> None:
    run(Path("config/example_workflow.yaml"))


if __name__ == "__main__":
    main()
