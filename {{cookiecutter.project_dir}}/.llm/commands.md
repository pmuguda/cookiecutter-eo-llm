## Commands (via Justfile)
just setup                     # install deps + pre-commit hooks
just lint                      # ruff check
just format                    # ruff format
just typecheck                 # mypy
just check                     # lint + typecheck
just test                      # full test suite
just test-unit                 # unit tests only
just test-integration          # integration tests only
just test-approval             # approval / snapshot tests
just test-cov                  # coverage HTML report
just docs                      # mkdocs serve
just docs-build                # build static docs
just update-context            # refresh code_map for next LLM session
just sync-llm                  # rebuild CLAUDE.md + AGENTS.md from .llm/
just sync-llm-check            # fail if CLAUDE.md / AGENTS.md drift from .llm/
just bump patch                # 0.1.0 → 0.1.1  (fix: commits)
just bump minor                # 0.1.0 → 0.2.0  (feat: commits)
just bump major                # 0.1.0 → 1.0.0  (BREAKING CHANGE)
just build                     # build distribution
just publish                   # publish to PyPI
just run config/config_{{cookiecutter.project_slug}}.yml   # run the workflow
