from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel


class WorkflowConfig(BaseModel):
    name: str
    type: str
    parameters: dict[str, Any]

    @classmethod
    def from_yaml(cls, path: Path) -> WorkflowConfig:
        raw = yaml.safe_load(path.read_text())
        workflow_data = raw.get("workflow", raw)
        return cls.model_validate(workflow_data)


def register_yaml_tags() -> None:
    def workflow_constructor(
        loader: yaml.SafeLoader, node: yaml.MappingNode
    ) -> dict[str, Any]:
        return loader.construct_mapping(node, deep=True)

    yaml.add_constructor("!workflow", workflow_constructor, Loader=yaml.SafeLoader)
