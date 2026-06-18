# Template Variables

All variables are defined in `cookiecutter.json`. Each maps to a Jinja2 expression available across every template file.

---

## Identity

| Variable | Default | Example | Used in |
|----------|---------|---------|---------|
| `full_name` | `Chuck Norris` | `Ada Lovelace` | `pyproject.toml`, `CLAUDE.md`, `AGENTS.md` |
| `email` | `chuck@example.com` | `ada@example.com` | `pyproject.toml`, `.llm/context.md` |
| `repository_owner` | `chucknorris` | `alovelace` | `pyproject.toml`, README badges, CI URLs |

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

## CI platform

| Variable | Default | Options | Effect |
|----------|---------|---------|--------|
| `ci_platform` | `github` | `github` · `gitlab` | Keeps only the selected CI/CD platform |

The selected value also controls repository URLs and README pipeline badges.

---

## Test scheme

| Variable | Default | Effect |
|----------|---------|--------|
| `test_scheme` | `full` | unit tests + approval tests + hypothesis |
| | `unit_and_approval` | unit tests + approval tests, no hypothesis |
| | `unit` | unit tests only, no approval tests or hypothesis |

---

## Feature flags

Each flag is `y` or `n`. The post-gen hook removes the corresponding files when `n`.

| Variable | Default | Effect when `n` |
|----------|---------|-----------------|
| `include_mkdocs` | `y` | Removes `docs/` and strips all `mkdocs*` lines from `pyproject.toml` |
| `open_source` | `y` | Reserved — no files are removed today; a future release will gate PyPI publish config behind this flag |

!!! note "`open_source`"
    Setting `open_source = n` currently has no effect on the generated files.
    The variable is present so the template can distinguish internal packages
    from public ones in future releases (e.g. skipping PyPI trusted-publisher
    setup, omitting the Ko-fi badge).
