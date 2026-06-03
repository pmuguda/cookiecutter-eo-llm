# Adding a Workflow

Every processing step is a `Workflow` subclass. The pattern is always the same
five steps.

---

## Config model design

The template provides three empty base models in `config/models.py`:

```python
class SourceModel(BaseModel):        # input paths, loaders, input settings
    model_config = ConfigDict(extra="allow")

class ComputeParamsModel(BaseModel): # algorithm params, transform options
    model_config = ConfigDict(extra="allow")

class DestinationModel(BaseModel):   # output paths, exporters, output settings
    model_config = ConfigDict(extra="allow")
```

Each concrete workflow subclasses all three and adds its own typed fields.

---

## Step 1 — Write a failing test

```python
# tests/unit/test_sbas_workflow.py
import pytest
from pathlib import Path
from my_eo_package.config.models import (
    SourceModel, ComputeParamsModel, DestinationModel, WorkflowConfigModel,
)
from my_eo_package.workflows.sbas import SBASWorkflow


def make_config() -> WorkflowConfigModel:
    return WorkflowConfigModel(
        name="test-sbas",
        type="SBASWorkflow",
        source=SourceModel(input_stack="data/slc.zarr", crs="EPSG:32632"),
        compute_params=ComputeParamsModel(max_baseline_days=30),
        destination=DestinationModel(output_path="data/velocity.tif"),
    )


def test_sbas_run_succeeds() -> None:
    SBASWorkflow(make_config()).run()


def test_sbas_validate_raises_on_missing_crs() -> None:
    config = WorkflowConfigModel(
        name="t", type="SBASWorkflow",
        source=SourceModel(input_stack="a.zarr"),
        destination=DestinationModel(output_path="b.tif"),
    )
    with pytest.raises(ValueError, match="crs"):
        SBASWorkflow(config).validate()
```

Run pytest — it should fail (red):

```bash
just test-unit
```

---

## Step 2 — Implement the workflow

Create `src/my_eo_package/workflows/sbas.py`:

```python
from pathlib import Path
from my_eo_package.config.models import (
    SourceModel, ComputeParamsModel, DestinationModel, WorkflowConfigModel,
)
from my_eo_package.logger import get_logger
from my_eo_package.workflows.base import Workflow

_log = get_logger(__name__)


class SBASSource(SourceModel):
    input_stack: Path
    crs: str


class SBASComputeParams(ComputeParamsModel):
    max_baseline_days: int = 30


class SBASDestination(DestinationModel):
    output_path: Path
    overwrite: bool = False


class SBASWorkflow(Workflow):
    def __init__(self, config: WorkflowConfigModel) -> None:
        super().__init__(config)
        self.source = SBASSource.model_validate(config.source.model_dump())
        self.compute = SBASComputeParams.model_validate(config.compute_params.model_dump())
        self.destination = SBASDestination.model_validate(config.destination.model_dump())

    def validate(self) -> None:
        if not self.source.crs:
            raise ValueError("source.crs is required")

    def run(self) -> None:
        self.validate()
        _log.info("stack:    %s", self.source.input_stack)
        _log.info("crs:      %s", self.source.crs)
        _log.info("output:   %s", self.destination.output_path)
```

Run pytest — it should pass (green):

```bash
just test-unit
```

---

## Step 3 — Register in main.py

```python
from my_eo_package.workflows.sbas import SBASWorkflow

WORKFLOW_REGISTRY: dict[str, type] = {
    "ExampleWorkflow": ExampleWorkflow,
    "SBASWorkflow": SBASWorkflow,      # ← add this
}
```

---

## Step 4 — Add a config file

Create `config/sbas_workflow.yaml`:

```yaml
name: sbas-velocity
type: SBASWorkflow
source:
  input_stack: data/slc_stack.zarr
  crs: EPSG:32632
compute_params:
  max_baseline_days: 30
destination:
  output_path: data/velocity.tif
  overwrite: false
```

---

## Step 5 — Update knowledge_base

Add an entry to `knowledge_base/workflows.md`:

```markdown
## SBASWorkflow

- **Purpose**: SBAS InSAR velocity from an SLC stack.
- **Source**: `input_stack` (zarr), `crs`
- **Compute**: `max_baseline_days` (int, default 30)
- **Destination**: `output_path`, `overwrite`
```

Run the workflow:

```bash
just run config/sbas_workflow.yaml
```

---

## Summary

| Step | Action |
|------|--------|
| 1 | Failing test — TDD red |
| 2 | Subclass `SourceModel`, `ComputeParamsModel`, `DestinationModel` + `Workflow` |
| 3 | Register in `WORKFLOW_REGISTRY` |
| 4 | Add YAML config |
| 5 | Update `knowledge_base/workflows.md` |
