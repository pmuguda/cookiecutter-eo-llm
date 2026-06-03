# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## Development rules

- TDD: failing test → minimum code → refactor. Small steps always.
- SOLID: one responsibility per function and class.
- No comments — rename and simplify instead.
- Type-annotate every argument and return value. mypy strict must pass.
- One package = one workflow. Rename ExampleWorkflow; update the import in main.py.
- Update knowledge_base/ whenever architecture changes.
- Conventional Commits on every commit — see .llm/boundaries.md.
- Never add LLM co-author footers to commits.

## Stack

- Build: hatchling + uv
- Lint: ruff (line-length 100, select E/F/I/UP/B/SIM)
- Types: mypy strict — every argument and return value annotated
- Test: pytest>=9.0.1 + pytest-cov + pytest-approvaltests-geo + pytest-xdist + hypothesis
- Docs: mkdocs-material + mkdocstrings[python]
- Versioning: bump-my-version via `just bump <part>`
- CI: GitHub Actions + GitLab CI

### EO / SAR stack

- numpy, xarray, dask — array processing
- rasterio, rioxarray — raster I/O
- pyproj, shapely, geopandas — CRS and vector ops
- pydantic>=2.7 — config validation
- typer — CLI
- pyyaml — plain YAML loading, no custom tags

### Architecture

- One workflow per package — imported directly in main.py
- Workflow base class (abstract) in workflows/base.py
- Concrete workflow: subclass Workflow, subclass SourceModel /
  ComputeParamsModel / DestinationModel, implement run() and validate()
- Plain YAML config — name / source / compute_params / destination
- main.py: WorkflowConfigModel.from_yaml() → Workflow → validate → run
- knowledge_base/ updated whenever architecture changes

### Conventions

- Folder names: kebab-case (my-eo-package)
- Import names: snake_case (my_eo_package)
- src/{{cookiecutter.project_slug}} layout — always import from src/
- Type annotations on every public function argument and return value
- NumPy docstring style
- CRS always explicit — never assume EPSG:4326
- Dask arrays for data > 1GB
- No comments — rename and simplify instead

## Commands

```
just setup                     # install deps + pre-commit hooks
just lint                      # ruff check
just format                    # ruff format
just typecheck                 # mypy
just check                     # lint + typecheck
just test                      # full test suite
just test-unit                 # unit tests only
just test-approval             # approval / snapshot tests
just test-cov                  # coverage HTML report
just docs                      # mkdocs serve
just docs-build                # build static docs
just bump patch                # 0.1.0 → 0.1.1  (fix: commits)
just bump minor                # 0.1.0 → 0.2.0  (feat: commits)
just bump major                # 0.1.0 → 1.0.0  (BREAKING CHANGE)
just build                     # build distribution
just publish                   # publish to PyPI
just run config/example.yaml   # run the workflow
```

## Boundaries

### Always

- Run just test before committing
- Explicit CRS on every spatial operation
- Type-annotate every public function argument and return value
- Keep CLAUDE.md and AGENTS.md under 200 lines
- TDD: failing test first, then implement, then refactor
- SOLID: one responsibility per function and class
- Update knowledge_base/ when architecture changes
- Conventional Commits on every commit message
- No LLM co-author footers in any commit

### Ask first

- Adding a new dependency
- Changing public API or function signatures
- Modifying CI/CD workflows
- Switching CRS in existing logic
- Adding GDAL as a direct dependency

### Never

- Commit secrets or credentials
- Push directly to main
- Skip type hints on public functions or return values
- Reproject without specifying target CRS explicitly
- Write comments — simplify the code instead
- Break the abstract Workflow interface contract
- Add "Co-authored-by: Claude" or any LLM attribution to commits

---
Source of truth: .llm/  |  Keep this file under 200 lines
