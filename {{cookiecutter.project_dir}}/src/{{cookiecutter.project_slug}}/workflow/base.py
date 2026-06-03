from abc import ABC, abstractmethod

from {{cookiecutter.project_slug}}.config.models import WorkflowConfigModel


class Workflow(ABC):
    def __init__(self, config: WorkflowConfigModel) -> None:
        self.config = config

    @abstractmethod
    def run(self) -> None: ...

    @abstractmethod
    def validate(self) -> None: ...
