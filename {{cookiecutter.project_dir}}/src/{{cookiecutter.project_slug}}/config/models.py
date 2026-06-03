from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field


class SourceModel(BaseModel):
    """Input specification. Subclass and add workflow-specific fields."""

    model_config = ConfigDict(extra="allow")


class ComputeParamsModel(BaseModel):
    """Processing parameters. Subclass and add workflow-specific fields."""

    model_config = ConfigDict(extra="allow")


class DestinationModel(BaseModel):
    """Output specification. Subclass and add workflow-specific fields."""

    model_config = ConfigDict(extra="allow")


class WorkflowConfigModel(BaseModel):
    """Top-level workflow config. Validated from plain YAML — no custom tags."""

    name: str
    source: SourceModel
    compute_params: ComputeParamsModel = Field(default_factory=ComputeParamsModel)
    destination: DestinationModel

    @classmethod
    def from_yaml(cls, path: Path) -> WorkflowConfigModel:
        return cls.model_validate(yaml.safe_load(path.read_text()))
