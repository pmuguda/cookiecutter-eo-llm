from abc import ABC, abstractmethod

from {{cookiecutter.project_slug}}.config.models import WorkflowConfig


class Workflow(ABC):
    def __init__(self, config: WorkflowConfig) -> None:
        self.config = config

    @abstractmethod
    def run(self) -> None: ...

    @abstractmethod
    def validate(self) -> None: ...
