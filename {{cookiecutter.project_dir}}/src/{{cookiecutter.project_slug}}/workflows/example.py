from {{cookiecutter.project_slug}}.config.models import WorkflowConfig
from {{cookiecutter.project_slug}}.workflows.base import Workflow


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
        print(f"input:  {self.config.parameters['input_path']}")
        print(f"output: {self.config.parameters['output_path']}")
        print(f"crs:    {self.config.parameters['crs']}")
