# Hooks

Cookiecutter hooks run Python scripts before and after rendering.

---

## pre_prompt.py

Validates `python_requires` before the template renders. Exits with an error
if an unsupported Python version string is supplied.

**Accepted values**: `>=3.10` · `>=3.11` · `>=3.12`

---

## post_gen_project.py

Runs in the freshly rendered project directory. Each concern is its own
single-responsibility function — no logic lives in `main()`.

### Functions

#### `remove_agents_md(project_dir)`
Deletes `AGENTS.md` when `primary_llm == "claude"`.
The developer only needs Claude Code context; the OpenAI AGENTS spec is removed.

#### `remove_claude_md(project_dir)`
Deletes `CLAUDE.md` when `primary_llm == "codex"`.
The developer only needs the AGENTS.md spec; the CLAUDE.md file is removed.

#### `remove_approval_tests(project_dir)`
Removes `tests/approval/` when `include_approval_tests == "n"`.

#### `remove_hypothesis(pyproject_path)`
Strips the `hypothesis` line from `pyproject.toml` dev deps when
`include_hypothesis == "n"`. All other deps are preserved.

#### `remove_mkdocs(project_dir, pyproject_path)`
Removes `docs/` and all `mkdocs*` lines from `pyproject.toml` when
`include_mkdocs == "n"`.

#### `remove_github_actions(project_dir)`
Removes `.github/` when `include_github_actions == "n"`.

#### `remove_gitlab_ci(project_dir)`
Removes `.gitlab-ci.yml` when `include_gitlab_ci == "n"`.

#### `init_git(project_dir)`
Runs `git init && git add . && git commit` with message:

```
chore: initial scaffold from cookiecutter-eo-llm
```

No LLM co-author footers are added.

#### `print_next_steps(project_dir, project_slug)`
Prints a concise onboarding message after all other steps complete.

### Composition

`main()` reads the cookiecutter context from environment variables and
calls the above functions in order. No conditional logic lives in `main()`.

---

## Testing hooks

Hook functions are tested in isolation in `tests/test_hooks.py`.
Each test creates a minimal fake project directory and asserts the
expected file system state after the function runs.

```bash
uv run pytest tests/test_hooks.py -v
```
