# Contributing to {{cookiecutter.project_name}}

## Development setup

```bash
just setup
```

## TDD workflow

Write a failing test first. Then write the minimum code to make it pass.
Then refactor. Always small steps — never implement without a red test.

## Implementing the workflow

This package is built around **one workflow**. `ExampleWorkflow` is the scaffold
placeholder — replace it with your real implementation:

1. Rename `workflow/example.py` and its classes to match your domain
2. Define `MySource(SourceModel)`, `MyComputeParams(ComputeParamsModel)`,
   `MyDestination(DestinationModel)` with typed fields
3. Implement `run()`; add workflow-specific validation inside `run()` when needed
4. Update the single import in `main.py`
5. Add unit tests in `tests/unit/`
6. Update `knowledge_base/workflows.md`

## Updating knowledge_base/

Every PR that changes architecture or adds a workflow must update
the relevant `knowledge_base/` file. PRs without this update will not be merged.
When code behavior changes, update the matching docs in the same PR so the
README, `docs/`, `.llm/`, and `knowledge_base/` stay aligned.

## Code style

- ruff, line-length 100
- mypy strict — every argument and return value typed
- NumPy docstrings
- No comments — use descriptive names instead
- kebab-case for folder names and PyPI package name
- snake_case for Python imports and module names

## Commit convention

This project follows [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

Types: `feat` `fix` `docs` `style` `refactor` `perf` `test` `build` `ci` `chore` `revert`

Breaking changes: append `!` or add a `BREAKING CHANGE:` footer.

SemVer mapping: `fix` → PATCH · `feat` → MINOR · `BREAKING CHANGE` → MAJOR

Never add LLM co-author footers to commits.

Version bumps: `just bump <patch|minor|major>`

## PR checklist

- [ ] `just test` passes
- [ ] `just typecheck` passes
- [ ] `just lint` passes
- [ ] `knowledge_base/` updated if architecture changed
- [ ] `docs/` updated if public API or architecture changed
- [ ] Commit messages follow Conventional Commits
- [ ] No LLM co-author footers in any commit
