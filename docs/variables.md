# Template Variables

All variables are defined in `cookiecutter.json`. Each maps to a Jinja2 expression available across every template file.

---

## Identity

| Variable | Default | Example | Used in |
|----------|---------|---------|---------|
| `full_name` | `Pavan Muguda Sanjeevamurthy` | `Ada Lovelace` | `pyproject.toml`, `CLAUDE.md`, `AGENTS.md` |
| `email` | `your@email.com` | `ada@example.com` | `pyproject.toml`, `.llm/context.md` |
| `github_username` | `PavanMuguda` | `alovelace` | `pyproject.toml`, README badges, CI URLs |

---

## Naming

| Variable | Derived from | Convention | Example |
|----------|-------------|------------|---------|
| `project_name` | user input | Title case | `SAR Coherence Processor` |
| `project_dir` | `project_name` auto-derived | **kebab-case** | `sar-coherence-processor` |
| `project_slug` | `project_name` auto-derived | **snake_case** | `sar_coherence_processor` |

!!! important "Two variables, two purposes"
    `project_dir` is used for: the root folder, GitHub repo name, PyPI package name, CLI command.  
    `project_slug` is used for: the importable Python package, `src/` subfolder, all import statements.

    These are derived automatically — you only type `project_name` once.

---

## Package metadata

| Variable | Default | Options |
|----------|---------|---------|
| `project_short_description` | `An Earth Observation Python package.` | free text |
| `version` | `0.1.0` | any SemVer string |
| `python_requires` | `>=3.10` | `>=3.10` · `>=3.11` · `>=3.12` |
| `license` | `MIT` | `MIT` · `Apache-2.0` · `GPL-3.0` · `BSD-3-Clause` · `Proprietary` |

---

## LLM target

| Variable | Default | Effect |
|----------|---------|--------|
| `primary_llm` | `both` | `both` → CLAUDE.md + AGENTS.md generated |
| | | `claude` → AGENTS.md removed by post-gen hook |
| | | `codex` → CLAUDE.md removed by post-gen hook |

!!! note
    `.llm/` context files are **always** generated regardless of `primary_llm`.
    The hook only removes the rendered output file, not the source.

---

## Feature flags

Each flag is `y` or `n`. The post-gen hook removes the corresponding files when `n`.

| Variable | Default | Removes when `n` |
|----------|---------|-----------------|
| `include_approval_tests` | `y` | `tests/approval/` |
| `include_hypothesis` | `y` | `hypothesis` from `pyproject.toml` dev deps |
| `include_mkdocs` | `y` | `docs/` + mkdocs deps from `pyproject.toml` |
| `include_github_actions` | `y` | `.github/` |
| `include_gitlab_ci` | `y` | `.gitlab-ci.yml` |
| `open_source` | `y` | (reserved for future use) |
