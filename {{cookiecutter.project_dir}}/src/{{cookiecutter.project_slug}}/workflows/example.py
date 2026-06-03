from {{cookiecutter.project_slug}}.config.models import WorkflowConfig
from {{cookiecutter.project_slug}}.logger import get_logger
from {{cookiecutter.project_slug}}.workflows.base import Workflow

_log = get_logger(__name__)


class ExampleWorkflow(Workflow):
    def __init__(self, config: WorkflowConfig) -> None:
        super().__init__(config)

    def validate(self) -> None:
        required = {"input_path", "output_path", "crs"}
        missing = required - self.config.parameters.keys()
        if missing:
            raise ValueError(f"Missing required parameters: {missing}")

    def run(self) -> None:
        self.validate()
        _log.info("input:  %s", self.config.parameters["input_path"])
        _log.info("output: %s", self.config.parameters["output_path"])
        _log.info("crs:    %s", self.config.parameters["crs"])
