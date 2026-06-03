# Architecture

## Package layout

```
src/{{cookiecutter.project_slug}}/
├── __init__.py
├── py.typed
├── logger.py    — get_logger(name) for consistent logging across modules
├── main.py      — run(config_path) entry point + typer CLI
├── workflows/
│   ├── base.py      — abstract Workflow base class
│   └── example.py   — concrete implementation showing the full pattern
└── config/
    └── models.py    — SourceModel, ComputeParamsModel, DestinationModel,
                       WorkflowConfigModel (Pydantic v2, plain YAML)
```

## Config model design

Three empty base models define the contract. Each concrete workflow subclasses
all three and adds its own typed fields.

```
SourceModel        — empty base: input paths, loaders, input settings
ComputeParamsModel — empty base: algorithm parameters, transform options
DestinationModel   — empty base: output paths, exporters, output settings
```

`WorkflowConfigModel` composes all three:

```python
class WorkflowConfigModel(BaseModel):
    name: str
    type: str
    source: SourceModel
    compute_params: ComputeParamsModel   # optional — defaults to empty
    destination: DestinationModel

    @classmethod
    def from_yaml(cls, path: Path) -> WorkflowConfigModel:
        return cls.model_validate(yaml.safe_load(path.read_text()))
```

No custom YAML tags. Plain `yaml.safe_load()` feeds Pydantic validation.

## Workflow config YAML structure

```yaml
name: my-run                  # human-readable label (used in logs)
type: MyWorkflow              # maps to WORKFLOW_REGISTRY key in main.py
source:
  input_path: data/input.tif
  crs: EPSG:32632
compute_params:               # omit entirely if the workflow needs none
  resampling: bilinear
destination:
  output_path: data/output.tif
  overwrite: false
```

## Workflow abstract class

`Workflow` in `workflows/base.py` defines the contract:
- `__init__(self, config: WorkflowConfigModel)` — receives validated config
- `run(self) -> None` — execute the workflow
- `validate(self) -> None` — validate inputs before running

Every concrete workflow must implement both methods.

## Concrete workflow pattern

Each workflow defines its own typed config models, then re-validates the
incoming base models into them in `__init__`:

```python
class MySource(SourceModel):
    input_path: Path
    crs: str = "EPSG:4326"

class MyComputeParams(ComputeParamsModel):
    resampling: str = "bilinear"

class MyDestination(DestinationModel):
    output_path: Path
    overwrite: bool = False

class MyWorkflow(Workflow):
    def __init__(self, config: WorkflowConfigModel) -> None:
        super().__init__(config)
        self.source = MySource.model_validate(config.source.model_dump())
        self.compute = MyComputeParams.model_validate(config.compute_params.model_dump())
        self.destination = MyDestination.model_validate(config.destination.model_dump())
```

## How to add a new workflow

1. Create `src/{{cookiecutter.project_slug}}/workflows/<name>.py`
2. Define `MySource`, `MyComputeParams`, `MyDestination` subclassing the base models
3. Subclass `Workflow`, implement `run()` and `validate()`
4. Register in `WORKFLOW_REGISTRY` in `main.py`
5. Add tests in `tests/unit/test_<name>_workflow.py`
6. Update `knowledge_base/workflows.md`
