# Config Model Design

Why the config is structured the way it is — and why it's better than
the obvious alternative.

---

## The obvious alternative: a flat dict

The simplest possible config model is a single class with a `parameters` dict:

```python
class WorkflowConfig(BaseModel):
    name: str
    parameters: dict[str, Any]   # ← everything in one bag
```

YAML:
```yaml
name: my-run
parameters:
  input_stack: data/slc.zarr
  crs: EPSG:32632
  window_size: 5
  output_path: data/coherence.tif
  overwrite: false
```

This works initially, but there is no schema. `parameters` is just a bag.
Pydantic cannot validate the types. mypy cannot help you. Every workflow
accesses fields like:

```python
self.config.parameters["input_stack"]   # str — not Path
self.config.parameters["window_size"]   # Any — could be str "5" or int 5
self.config.parameters.get("overwrite", False)  # is it bool or str "false"?
```

Runtime surprises. No autocomplete. No type errors until the workflow runs.

---

## Why three base models

EO workflows all follow the same shape regardless of algorithm:

```
read something  →  transform it  →  write somewhere
    source            compute          destination
```

Splitting the config along these lines gives structure without forcing
field definitions on anyone:

```python
class SourceModel(BaseModel):        # everything about inputs
    model_config = ConfigDict(extra="allow")

class ComputeParamsModel(BaseModel): # everything about the algorithm
    model_config = ConfigDict(extra="allow")

class DestinationModel(BaseModel):   # everything about outputs
    model_config = ConfigDict(extra="allow")
```

YAML now has a clear shape every workflow follows:

```yaml
source:
  input_stack: data/slc.zarr
  crs: EPSG:32632
compute_params:
  window_size: 5
destination:
  output_path: data/coherence.tif
  overwrite: false
```

A reader who has never seen this workflow before immediately knows where
to look for the input path (source), the algorithm knob (compute_params),
and the output path (destination). The flat dict gives no such signal.

---

## Why `extra="allow"` on the base models

The base models define **no fields**. They are empty contracts.
`extra="allow"` means Pydantic stores whatever the YAML provides,
without validating types.

This keeps the base models stable. A new workflow can add fields
to its concrete subclasses without touching `models.py`.

At this stage, the data lives in `model_extra` — a plain dict — and
is still untyped. That is intentional. The next step is where typing happens.

---

## Why re-validate in `__init__`

Each concrete workflow subclasses the three base models and defines
its own typed fields:

```python
class CoherenceSource(SourceModel):
    input_stack: Path          # ← str coerced to Path by Pydantic
    crs: str                   # ← required, validated

class CoherenceComputeParams(ComputeParamsModel):
    window_size: int = 5       # ← default, type-checked

class CoherenceDestination(DestinationModel):
    output_path: Path          # ← str coerced to Path
    overwrite: bool = False    # ← default, type-checked
```

In `__init__`, the base model is re-validated into the concrete one:

```python
class CoherenceWorkflow(Workflow):
    def __init__(self, config: WorkflowConfigModel) -> None:
        super().__init__(config)
        self.source = CoherenceSource.model_validate(config.source.model_dump())
        self.compute = CoherenceComputeParams.model_validate(config.compute_params.model_dump())
        self.destination = CoherenceDestination.model_validate(config.destination.model_dump())
```

From this point on, every field access is fully typed:

```python
self.source.input_stack          # Path — autocomplete works, mypy happy
self.compute.window_size         # int  — not Any
self.destination.output_path     # Path — not str
self.destination.overwrite       # bool — not "false"
```

Pydantic validates types and coerces values at `__init__` time, not
at run time. A missing required field or a wrong type raises a `ValidationError`
immediately when the workflow is constructed — before `run()` is ever called.

---

## Why plain YAML instead of custom tags

An earlier design used a `!workflow` custom PyYAML tag and a `type:` field
for dispatching to the right workflow class:

```yaml
workflow: !workflow
  name: example
  type: CoherenceWorkflow   # ← dispatch key
  parameters: ...
```

This required registering a PyYAML constructor, calling `register_yaml_tags()`
before every `from_yaml()`, maintaining a `WORKFLOW_REGISTRY` dict in `main.py`,
and knowing the `!workflow` tag existed at all.

None of it was needed. Each package implements **one workflow**. `main.py`
imports it directly — there is nothing to dispatch to:

```python
# main.py
from my_eo_package.workflow.coherence import CoherenceWorkflow as Workflow

def run_my_eo_package(config: WorkflowConfigModel) -> None:
    workflow = Workflow(config)   # direct, no lookup
    workflow.run()
```

`from_yaml` is three lines:

```python
@classmethod
def from_yaml(cls, path: Path) -> WorkflowConfigModel:
    return cls.model_validate(yaml.safe_load(path.read_text()))
```

No tags. No constructors. No registration. No `type:` field in the YAML.
The config file reads like any other config file.

---

## Before and after

| | Flat dict | Three base models |
|---|---|---|
| Field names | unconstrained | grouped by source / compute / destination |
| Types | `Any` at the config level | typed in concrete subclass |
| mypy | silent | full coverage inside `__init__` |
| Validation timing | at first field access | at `__init__` call |
| Adding a field | edit dict anywhere | add to subclass — base untouched |
| YAML readability | flat list of keys | grouped sections |
| YAML loading | `!workflow` tag + `register_yaml_tags()` | `yaml.safe_load()` |
| Dispatch | `WORKFLOW_REGISTRY[config.type]` | direct import in `main.py` |

The base models do less. Each workflow owns its own schema. The structure
makes the intent readable before a single line of algorithm code is written.
