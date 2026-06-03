# Changelog

All notable changes to this template are documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
Versioning: [Semantic Versioning](https://semver.org/)

---

## [Unreleased]

## [0.1.0] — 2026-06-04

### Added

- `cookiecutter.json` with 12 template variables including `primary_llm`, `include_approval_tests`, `include_hypothesis`, `include_mkdocs`, `include_github_actions`, `include_gitlab_ci`
- `{{cookiecutter.project_dir}}/` template with full `src/` layout:
  - Abstract `Workflow` base class with `run()` and `validate()` contract
  - `ExampleWorkflow` concrete implementation
  - `WorkflowConfig` Pydantic v2 model with `from_yaml()` and YAML tag registration
  - `typer` CLI wired to `run(config_path)`
- `.llm/` context files: `context.md`, `stack.md`, `commands.md`, `boundaries.md`
- `CLAUDE.md` and `AGENTS.md` both rendered from `.llm/` — under 200 lines each
- `knowledge_base/`: `architecture.md`, `workflows.md`, `decisions.md`, `changelog_context.md`
- `hooks/post_gen_project.py`: 7 single-responsibility functions + `main()` composer
- `hooks/pre_prompt.py`: Python version validation
- GitHub Actions CI matrix (py3.10 / 3.11 / 3.12) + PyPI OIDC publish workflow
- GitLab CI with lint / test / publish stages
- Justfile with `setup`, `lint`, `format`, `typecheck`, `check`, `test`, `bump`, `build`, `publish`, `run`
- `pyproject.toml` with hatchling, bump-my-version, ruff, mypy strict
- Test suite: 69 tests — structure checks, hook unit tests, CLAUDE.md/AGENTS.md approval tests
- Full MkDocs documentation site published on GitHub Pages
