# Implementing Your Workflow

This package scaffolds around **one workflow**. `ExampleWorkflow` is the
placeholder — replace it with your real implementation.

---

## The config YAML structure

Every workflow reads from the same three-section config:

```yaml
name: coherence-run-2024          # label for this run — used in logs
source:
  input_stack: data/slc.zarr
  crs: EPSG:32632
compute_params:                   # omit entirely if not needed
  window_size: 5
destination:
  output_path: data/coherence.tif
  overwrite: false
```

No `type:` field. The workflow class is fixed per package — `main.py` imports
it directly.

---

## Step 1 — Write a failing test first

```python
# tests/unit/test_coherence_workflow.py
import pytest
from pathlib import Path
from my_eo_package.config.models import (
    SourceModel, ComputeParamsModel, DestinationModel, WorkflowConfigModel,
)
from my_eo_package.workflows.coherence import CoherenceWorkflow


def make_config() -> WorkflowConfigModel:
    return WorkflowConfigModel(
        name="test",
        source=SourceModel(input_stack="data/slc.zarr", crs="EPSG:32632"),
        compute_params=ComputeParamsModel(window_size=5),
        destination=DestinationModel(output_path="data/coherence.tif"),
    )


def test_coherence_run_succeeds() -> None:
    CoherenceWorkflow(make_config()).run()


def test_coherence_validate_raises_on_missing_crs() -> None:
    config = WorkflowConfigModel(
        name="t",
        source=SourceModel(input_stack="a.zarr"),
        destination=DestinationModel(output_path="b.tif"),
    )
    with pytest.raises(ValueError, match="crs"):
        CoherenceWorkflow(config).validate()
```

Run — should fail (red):

```bash
just test-unit
```

---

## Step 2 — Implement the workflow

Rename `workflows/example.py` → `workflows/coherence.py` and replace:

```python
# src/my_eo_package/workflows/coherence.py
from pathlib import Path
from my_eo_package.config.models import (
    SourceModel, ComputeParamsModel, DestinationModel, WorkflowConfigModel,
)
from my_eo_package.logger import get_logger
from my_eo_package.workflows.base import Workflow

_log = get_logger(__name__)


class CoherenceSource(SourceModel):
    input_stack: Path
    crs: str


class CoherenceComputeParams(ComputeParamsModel):
    window_size: int = 5


class CoherenceDestination(DestinationModel):
    output_path: Path
    overwrite: bool = False


class CoherenceWorkflow(Workflow):
    def __init__(self, config: WorkflowConfigModel) -> None:
        super().__init__(config)
        self.source = CoherenceSource.model_validate(config.source.model_dump())
        self.compute = CoherenceComputeParams.model_validate(
            config.compute_params.model_dump()
        )
        self.destination = CoherenceDestination.model_validate(
            config.destination.model_dump()
        )

    def validate(self) -> None:
        if not self.source.crs:
            raise ValueError("source.crs is required")

    def run(self) -> None:
        self.validate()
        _log.info("stack:       %s", self.source.input_stack)
        _log.info("crs:         %s", self.source.crs)
        _log.info("window_size: %s", self.compute.window_size)
        _log.info("output:      %s", self.destination.output_path)
```

Run — should pass (green):

```bash
just test-unit
```

---

## Step 3 — Update main.py

One line changes — the import:

```python
# main.py  (before)
from my_eo_package.workflows.example import ExampleWorkflow as Workflow

# main.py  (after)
from my_eo_package.workflows.coherence import CoherenceWorkflow as Workflow
```

Everything else in `main.py` stays the same.

---

## Step 4 — Update the config file and knowledge base

Update `config/example_workflow.yaml`:

```yaml
name: coherence-run
source:
  input_stack: data/slc.zarr
  crs: EPSG:32632
compute_params:
  window_size: 5
destination:
  output_path: data/coherence.tif
  overwrite: false
```

Update `knowledge_base/workflows.md`:

```markdown
## CoherenceWorkflow

- **Source**: `input_stack` (zarr), `crs`
- **Compute**: `window_size` (int, default 5)
- **Destination**: `output_path`, `overwrite`
```

Run the workflow:

```bash
just run config/example_workflow.yaml
```

---

## Summary

| Step | Action |
|------|--------|
| 1 | Write failing test |
| 2 | Rename `example.py`, implement concrete source / compute / destination models + workflow |
| 3 | Update the one import in `main.py` |
| 4 | Update config YAML and `knowledge_base/workflows.md` |
