# Current state

Regenerate with:

```bash
just update-context
```

## Project stage

- Initial scaffold generated from `cookiecutter-eo-llm`.
- `ExampleWorkflow` demonstrates the source / compute / destination pattern.
- The package is ready for the first real EO/SAR workflow implementation.

## What to read first

1. `knowledge_base/current_state.md`
2. `knowledge_base/code_map.md`
3. `knowledge_base/architecture.md`
4. `knowledge_base/workflows.md`
5. `.llm/boundaries.md`

## Open implementation work

- Rename `ExampleWorkflow` to the real workflow.
- Update `config/config_{{cookiecutter.project_slug}}.yml`.
- Add domain-specific tests before implementing behavior.
- Update `knowledge_base/`, `docs/`, `AGENTS.md`, and `CLAUDE.md` when architecture changes.

## Last context refresh

- Generated during scaffold.
