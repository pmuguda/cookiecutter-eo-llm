# Changelog

All notable changes to this template are documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
Versioning: [Semantic Versioning](https://semver.org/)

---

## [Unreleased]

### Added

- `scripts/sync_llm.py` — generates `CLAUDE.md` and `AGENTS.md` from `.llm/`,
  making `.llm/` a real (not aspirational) single source of truth
- `just sync-llm` / `just sync-llm-check` commands
- No-drift enforcement: `sync_llm.py --check` runs in the generated project's
  test suite and in the template's own suite, so CLAUDE.md/AGENTS.md can no
  longer silently diverge from `.llm/`
- `generate_llm_context()` post-gen hook step that builds both context files

### Changed

- `CLAUDE.md` and `AGENTS.md` are now generated artifacts; the hand-written
  templates were removed
- `.llm/commands.md` corrected (config filename) and completed (`update-context`,
  `sync-llm`, `test-integration`)
- `update_code_map.py` no longer overwrites human-curated `current_state.md`
  (seeds it once if missing); `code_map.md` is still regenerated each run
- `just update-context` now runs via `uv run python` for interpreter consistency

## [0.1.0] — 2026-06-04

### Added

- `cookiecutter.json` with template variables including `primary_llm`, `include_mkdocs`, `ci_platform`, and `test_scheme`
- `{{cookiecutter.project_dir}}/` template with full `src/` layout:
  - Abstract `Workflow` base class with `run()` contract and base workflow logger
  - `ExampleWorkflow` concrete implementation
  - `WorkflowConfigModel` Pydantic v2 model with `from_yaml()` and plain YAML loading
  - `typer` CLI wired to check a config path and pass `WorkflowConfigModel` into `run_<project_slug>(config)`
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
