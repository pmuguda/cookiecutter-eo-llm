# Quickstart

## Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) — the only package manager used in any generated project

Install uv if you don't have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Generate a project

```bash
uvx cookiecutter gh:pmuguda/cookiecutter-eo-llm
```

You will be prompted for:

```
full_name [Pavan Muguda Sanjeevamurthy]: Ada Lovelace
email [your@email.com]: ada@example.com
github_username [PavanMuguda]: alovelace
project_name [My EO Package]: SAR Coherence Processor
project_short_description [...]: Sentinel-1 InSAR coherence estimation pipeline.
version [0.1.0]:
python_requires [>=3.10]:
license [MIT]:
primary_llm [both]:
include_approval_tests [y]:
include_hypothesis [y]:
include_mkdocs [y]:
include_github_actions [y]:
include_gitlab_ci [y]:
open_source [y]:
```

!!! tip "Automated / CI usage"
    Skip all prompts with `--no-input`:
    ```bash
    uvx cookiecutter gh:pmuguda/cookiecutter-eo-llm --no-input
    ```

---

## Run the generated project

```bash
cd sar-coherence-processor
just setup          # uv sync --dev + pre-commit install
just test           # full test suite
just run config/example_workflow.yaml
```

Expected output:

```
input:  data/input.tif
output: data/output.tif
crs:    EPSG:4326
```

---

## Verify everything is wired

```bash
just check          # ruff + mypy strict — zero errors expected
just test           # all tests green
```

---

## Next steps

1. Read [`knowledge_base/architecture.md`](structure.md) — understand the Workflow pattern
2. Add your first real workflow → [Adding a workflow guide](guides/add-workflow.md)
3. Update `.llm/` files as your architecture evolves
4. Push to GitHub and watch CI run automatically
