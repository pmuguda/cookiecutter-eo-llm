# Contributing

## Development setup

```bash
git clone https://github.com/pmuguda/cookiecutter-eo-llm
cd cookiecutter-eo-llm
uv sync --dev
uv run pytest
```

---

## TDD workflow

1. Write a failing test that describes the intended behaviour
2. Write the minimum production code to make it pass
3. Refactor for simplicity and clarity

Never implement without a red test first.

---

## Rendering the template locally

```bash
uvx cookiecutter . --no-input -o /tmp/eo-test
```

This is equivalent to what `tests/helpers/render.py` does in CI.

---

## Running tests

```bash
uv run pytest                          # full suite
uv run pytest tests/test_hooks.py      # hook unit tests only
uv run pytest tests/test_structure.py  # structure checks only
```

---

## Code style

- ruff, line-length 100
- mypy strict on `hooks/` and `tests/`
- No comments — use descriptive names instead
- One function per concern

```bash
uv run ruff check hooks/ tests/
uv run mypy hooks/ tests/
```

---

## Adding a new hook function

1. Write a test in `tests/test_hooks.py` that creates a fake project dir and
   asserts the expected state after the function runs (red)
2. Add the function to `hooks/post_gen_project.py` with a single responsibility (green)
3. Wire it into `main()` — only routing logic lives there
4. Update `docs/hooks.md`

---

## Commit convention

This project follows [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/).

| Type | SemVer | When |
|------|--------|------|
| `fix:` | PATCH | bug in a hook, test, or template file |
| `feat:` | MINOR | new feature flag, new hook, new template file |
| `docs:` | — | documentation only |
| `refactor:` | — | code restructure, no behaviour change |
| `test:` | — | adding or correcting tests |
| `ci:` | — | CI/CD workflow changes |

Breaking changes: append `!` or add a `BREAKING CHANGE:` footer.

**Never add LLM co-author footers to commits.**

---

## PR checklist

- [ ] `uv run pytest` passes
- [ ] `uv run ruff check hooks/ tests/` passes
- [ ] `uv run mypy hooks/ tests/` passes
- [ ] `docs/` updated if behaviour changed
- [ ] Commit messages follow Conventional Commits
- [ ] No LLM co-author footers in any commit
