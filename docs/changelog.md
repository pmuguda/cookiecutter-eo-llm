# Changelog

All notable changes to this template are documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
Versioning: [Semantic Versioning](https://semver.org/)

---

## [Unreleased]

## [0.1.0] — 2026-06-04

### Added

- `cookiecutter.json` with template variables including `primary_llm`, `include_mkdocs`, `ci_platform`, and `test_scheme`
- `{{cookiecutter.project_dir}}/` template with full `src/` layout:
  - Abstract `Workflow` base class with `run()` and `validate()` contract
  - `ExampleWorkflow` concrete implementation
  - `WorkflowConfigModel` Pydantic v2 model with `from_yaml()` and plain YAML loading
  - `typer` CLI wired to load a config path and pass `WorkflowConfigModel` into `run(config)`
- `.llm/` context files: `context.md`, `stack.md`, `commands.md`, `boundaries.md`, `skills.md`
- `CLAUDE.md` and `AGENTS.md` both rendered from `.llm/` — under 200 lines each
- `knowledge_base/`: `architecture.md`, `workflows.md`, `decisions.md`, `changelog_context.md`
- `hooks/post_gen_project.py`: 7 single-responsibility functions + `main()` composer
- `hooks/pre_prompt.py`: Python version validation
- Selectable GitHub Actions or GitLab CI with build, test, docs, and publish jobs
- Justfile with `setup`, `lint`, `format`, `typecheck`, `check`, `test`, `bump`, `build`, `publish`, `run`
- `pyproject.toml` with hatchling, bump-my-version, ruff, mypy strict
- Test suite with structure checks, hook unit tests, CLAUDE.md/AGENTS.md approval tests
- Full MkDocs documentation site published on GitHub Pages
