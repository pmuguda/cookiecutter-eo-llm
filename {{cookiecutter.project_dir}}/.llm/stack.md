## Toolchain
- Build: hatchling + uv
- Lint: ruff (line-length 100, select E/F/I/UP/B/SIM)
- Types: mypy strict — every argument and return value annotated
- Test: pytest>=9.0.1 + pytest-cov>=7.0.0 + pytest-approvaltests-geo>=1.9.0
         + pytest-xdist + hypothesis
- Docs: mkdocs-material + mkdocstrings[python]
- Versioning: bump-my-version via `just bump <part>`
- CI: GitHub Actions + GitLab CI

## EO / SAR stack
- numpy, xarray, dask            — array processing
- rasterio, rioxarray            — raster I/O
- pyproj, shapely, geopandas     — CRS and vector ops
- pydantic>=2.7                  — config validation
- typer                          — CLI
- pyyaml                          — plain YAML loading, no custom tags
- scipy                          — signal processing

## Architecture
- Workflow base class (abstract) in workflows/base.py
- One workflow per package — imported directly in main.py, no registry
- Concrete workflow: subclass SourceModel / ComputeParamsModel / DestinationModel
- YAML configs in config/ — one file per workflow run
- Plain YAML: name / source / compute_params / destination — no custom tags
- main.py: run(config_path) function + typer CLI
- knowledge_base/ updated whenever architecture changes

## Conventions
- Folder names: kebab-case (my-eo-package)
- Import names: snake_case (my_eo_package)
- src/{{cookiecutter.project_slug}} layout — always import from src/
- Type annotations on every public function argument and return value
- NumPy docstring style
- CRS always explicit — never assume EPSG:4326
- Dask arrays for data > 1GB
- No comments — rename and simplify instead
