# Adding a Workflow

Every new processing step in a generated project is a `Workflow` subclass.
The pattern is always the same four steps.

---

## Step 1 — Write a failing test

Before writing any implementation, write the test:

```python
# tests/unit/test_sbas_workflow.py
import pytest
from my_eo_package.config.models import WorkflowConfig
from my_eo_package.workflows.sbas import SBASWorkflow


def make_config() -> WorkflowConfig:
    return WorkflowConfig(
        name="test-sbas",
        type="SBASWorkflow",
        parameters={
            "input_stack": "data/slc_stack.zarr",
            "output_path": "data/velocity.tif",
            "crs": "EPSG:32632",
            "max_temporal_baseline_days": 30,
        },
    )


def test_sbas_run_succeeds() -> None:
    workflow = SBASWorkflow(make_config())
    workflow.run()


def test_sbas_validate_raises_on_missing_crs() -> None:
    config = WorkflowConfig(
        name="test", type="SBASWorkflow",
        parameters={"input_stack": "a.zarr", "output_path": "b.tif"},
    )
    with pytest.raises(ValueError, match="crs"):
        SBASWorkflow(config).validate()
```

Run pytest — it should fail (red):

```bash
just test-unit
```

---

## Step 2 — Implement the subclass

Create `src/my_eo_package/workflows/sbas.py`:

```python
from my_eo_package.config.models import WorkflowConfig
from my_eo_package.workflows.base import Workflow


class SBASWorkflow(Workflow):
    def __init__(self, config: WorkflowConfig) -> None:
        super().__init__(config)

    def validate(self) -> None:
        required = {"input_stack", "output_path", "crs"}
        missing = required - self.config.parameters.keys()
        if missing:
            raise ValueError(f"Missing required parameters: {missing}")

    def run(self) -> None:
        self.validate()
        # implement processing here
        print(f"SBAS: {self.config.parameters['input_stack']} → {self.config.parameters['output_path']}")
```

Run pytest — it should pass (green):

```bash
just test-unit
```

---

## Step 3 — Register the YAML tag

In `src/my_eo_package/config/models.py`, add one constructor inside `register_yaml_tags()`:

```python
def register_yaml_tags() -> None:
    def workflow_constructor(loader, node):
        return loader.construct_mapping(node, deep=True)

    yaml.add_constructor("!workflow", workflow_constructor, Loader=yaml.SafeLoader)
    yaml.add_constructor("!sbas", workflow_constructor, Loader=yaml.SafeLoader)  # ← add this
```

And register the class in `main.py`:

```python
from my_eo_package.workflows.sbas import SBASWorkflow

WORKFLOW_REGISTRY: dict[str, type] = {
    "ExampleWorkflow": ExampleWorkflow,
    "SBASWorkflow": SBASWorkflow,      # ← add this
}
```

---

## Step 4 — Add a config file and update knowledge_base

Create `config/sbas_workflow.yaml`:

```yaml
workflow: !sbas
  name: sbas-velocity
  type: SBASWorkflow
  parameters:
    input_stack: data/slc_stack.zarr
    output_path: data/velocity.tif
    crs: EPSG:32632
    max_temporal_baseline_days: 30
```

Update `knowledge_base/workflows.md` — add an entry for `SBASWorkflow`:

```markdown
## SBASWorkflow

- **Purpose**: SBAS InSAR velocity estimation from an SLC stack.
- **Config type**: `SBASWorkflow`
- **Required parameters**: `input_stack`, `output_path`, `crs`, `max_temporal_baseline_days`
- **Outputs**: velocity GeoTIFF in target CRS
- **Added**: 2024-07-01
```

Run the workflow:

```bash
just run config/sbas_workflow.yaml
```

---

## Summary

| Step | Action | Rule |
|------|--------|------|
| 1 | Write failing test | TDD: red first |
| 2 | Subclass `Workflow`, implement `run()` + `validate()` | SOLID: one responsibility |
| 3 | Register YAML tag + add to `WORKFLOW_REGISTRY` | Open-closed: extend, don't modify |
| 4 | Update `knowledge_base/workflows.md` | Living docs contract |
