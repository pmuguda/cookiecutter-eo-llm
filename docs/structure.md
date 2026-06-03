# Generated Project Structure

Running `uvx cookiecutter gh:pmuguda/cookiecutter-eo-llm` with `project_name = "My EO Package"` produces:

```
my-eo-package/                          ← project_dir (kebab-case)
├── pyproject.toml                      ← hatchling build, all deps, ruff/mypy config
├── Justfile                            ← all dev commands
├── README.md                           ← badges + quick-start
├── CHANGELOG.md                        ← Keep a Changelog format
├── CONTRIBUTING.md                     ← PR checklist, commit convention
│
├── CLAUDE.md                           ← rendered from .llm/  (≤200 lines)
├── AGENTS.md                           ← rendered from .llm/  (≤200 lines)
│
├── .llm/                               ← single source of truth for LLM context
│   ├── context.md                      ← project identity and metadata
│   ├── stack.md                        ← toolchain + EO stack + conventions
│   ├── commands.md                     ← all Justfile commands documented
│   └── boundaries.md                  ← always / ask-first / never rules
│
├── knowledge_base/                     ← living docs — update as you code
│   ├── architecture.md                 ← package layout, Workflow pattern
│   ├── workflows.md                    ← one entry per concrete workflow
│   ├── decisions.md                    ← ADRs: why this lib, why this pattern
│   └── changelog_context.md           ← plain-English summary since last release
│
├── config/
│   └── example_workflow.yaml           ← YAML tag demo
│
├── src/
│   └── my_eo_package/                  ← project_slug (snake_case)
│       ├── __init__.py                 ← exposes __version__
│       ├── py.typed                    ← PEP 561 marker
│       ├── main.py                     ← run() + typer CLI
│       ├── workflows/
│       │   ├── base.py                 ← abstract Workflow(ABC)
│       │   └── example.py             ← ExampleWorkflow
│       └── config/
│           └── models.py              ← WorkflowConfig + register_yaml_tags()
│
├── tests/
│   ├── conftest.py                     ← shared xarray fixture
│   ├── helpers/
│   │   └── config_builder.py          ← WorkflowConfig factory functions
│   ├── resources/
│   │   ├── example_workflow.yaml
│   │   └── invalid_workflow.yaml
│   ├── unit/
│   │   ├── test_main.py
│   │   ├── test_base_workflow.py
│   │   ├── test_example_workflow.py
│   │   └── test_config_models.py
│   ├── integration/
│   │   └── .gitkeep
│   └── approval/
│       ├── test_approval.py
│       └── approved_files/
│
├── notebooks/
│   └── 00_exploration.ipynb
├── scripts/
│   └── example_script.py
├── docs/
│   ├── mkdocs.yml
│   ├── index.md
│   └── api/index.md
│
├── .github/
│   └── workflows/
│       ├── ci.yml                      ← test matrix: py3.10 / 3.11 / 3.12
│       └── publish.yml                ← OIDC trusted publisher to PyPI
├── .gitlab-ci.yml
├── .pre-commit-config.yaml             ← ruff + mypy hooks
├── .gitignore
└── .editorconfig
```

---

## Key design decisions

### kebab vs snake naming

The two cookiecutter variables enforce a deliberate split:

- **`project_dir`** (`my-eo-package`) → filesystem, PyPI, CLI command  
- **`project_slug`** (`my_eo_package`) → Python imports, `src/` subfolder

### Workflow pattern

Every workflow is a class that subclasses `Workflow` and implements two methods:

```python
class Workflow(ABC):
    def run(self) -> None: ...
    def validate(self) -> None: ...
```

Adding a new workflow requires exactly: one new file, one new YAML constructor. Nothing else changes.

### .llm/ as single source of truth

CLAUDE.md and AGENTS.md are both written from the same `.llm/` files at scaffold time.
When the project evolves, update `.llm/` — then regenerate or manually sync both context files.

### knowledge_base/ as living docs

These four files are the contract between the developer and any LLM assistant:

| File | Updated when |
|------|-------------|
| `architecture.md` | layout changes, new patterns |
| `workflows.md` | any workflow is added or changed |
| `decisions.md` | a non-obvious design choice is made |
| `changelog_context.md` | before a release — reset after tagging |
