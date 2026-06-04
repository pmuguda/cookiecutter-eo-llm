# CI/CD

Generated projects keep one CI/CD platform: GitHub Actions or GitLab CI,
selected by `ci_platform` during scaffolding.

---

## GitHub Actions

### ci.yml — build, test, docs, and PyPI

The Python matrix is derived from `python_requires`: `>=3.10` tests 3.10-3.12,
`>=3.11` tests 3.11-3.12, and `>=3.12` tests only 3.12.

```yaml
on:
  push:
    branches: [main]
    tags: ["v*"]
  pull_request:
    branches: [main]

jobs:
  build:        # lint + typecheck; builds dist on tags
  test-dev:     # non-tag pushes and PRs
  test-release: # tags only
  deploy-docs:  # main and tags
  deploy-pypi:  # tags only, uses trusted publishing
```

PyPI publish uses [OIDC trusted publisher](https://docs.pypi.org/trusted-publishers/)
on `v*` tags. There are no hardcoded tokens:

```bash
# Publish a new version
just bump minor         # bumps pyproject.toml, commits, tags
git push --follow-tags  # triggers ci.yml release jobs
```

Set up trusted publishing once on PyPI:
`PyPI → Your project → Publishing → Add a new publisher → GitHub Actions`

---

## GitLab CI

Three stages: `build → test → deploy`.

- Lint: ruff + mypy
- Test: development jobs for branches, release jobs for tags
- Publish: tag-triggered GitLab package publish plus optional manual PyPI.org publish
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
