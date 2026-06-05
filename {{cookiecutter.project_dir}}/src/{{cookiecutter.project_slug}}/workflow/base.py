from abc import ABC, abstractmethod

from {{cookiecutter.project_slug}}.config.models import WorkflowConfigModel
from {{cookiecutter.project_slug}}.logger import get_logger


class Workflow(ABC):
    def __init__(self, config: WorkflowConfigModel) -> None:
        self.config = config
        self.log = get_logger(self.__class__.__name__)

    @abstractmethod
    def run(self) -> None: ...
