# CI/CD

Generated projects come with GitHub Actions and GitLab CI pre-wired.

---

## GitHub Actions

### ci.yml — Test matrix

Runs on every push and pull request across Python 3.10, 3.11, and 3.12:

```yaml
on: [push, pull_request]

jobs:
  test:
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv sync --dev
      - run: uv run ruff check src/ tests/
      - run: uv run mypy src/
      - run: uv run pytest
```

### publish.yml — PyPI via OIDC

Triggers on `v*` tags. Uses [OIDC trusted publisher](https://docs.pypi.org/trusted-publishers/) — no hardcoded tokens:

```bash
# Publish a new version
just bump minor         # bumps pyproject.toml, commits, tags
git push --follow-tags  # triggers publish.yml
```

Set up trusted publishing once on PyPI:
`PyPI → Your project → Publishing → Add a new publisher → GitHub Actions`

---

## GitLab CI

Three stages: `lint → test → publish`.

- Lint: ruff + mypy
- Test: parallel matrix across Python 3.10 / 3.11 / 3.12
- Publish: triggered on tags, runs `uv build && uv publish`
- Coverage report uploaded as Cobertura artifact

---

## Version bumping

SemVer is managed by `bump-my-version` via `just bump`:

| Command | Effect | Conventional Commits trigger |
|---------|--------|------------------------------|
| `just bump patch` | `0.1.0 → 0.1.1` | `fix:` |
| `just bump minor` | `0.1.0 → 0.2.0` | `feat:` |
| `just bump major` | `0.1.0 → 1.0.0` | `BREAKING CHANGE` |

Commit message template: `chore: bump version {current} → {new}` — no LLM co-author footers.

---

## Pre-commit hooks

`just setup` installs pre-commit hooks automatically:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    hooks:
      - id: ruff        # lint + auto-fix
      - id: ruff-format # format
  - repo: https://github.com/pre-commit/mirrors-mypy
    hooks:
      - id: mypy        # type check
```

Every commit is checked before it lands.
