# Installation

## Install uv

This template and all generated projects use `uv` exclusively.

=== "macOS / Linux"
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows"
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

=== "Homebrew"
    ```bash
    brew install uv
    ```

Verify:

```bash
uv --version
# uv 0.4.x (...)
```

---

## Install cookiecutter via uvx

`uvx` runs tools in an isolated environment — no global install needed:

```bash
uvx cookiecutter gh:pmuguda/cookiecutter-eo-llm
```

`uvx` is bundled with uv. No separate install required.

---

## Local development of this template

Clone and set up:

```bash
git clone https://github.com/pmuguda/cookiecutter-eo-llm
cd cookiecutter-eo-llm
uv sync --dev
uv run pytest
```

Render the template locally:

```bash
uvx cookiecutter . --no-input -o /tmp/eo-test
```

---

## Requirements

| Tool | Min version | Purpose |
|------|-------------|---------|
| Python | 3.10 | Runtime for hooks and tests |
| uv | 0.4+ | Package management |
| git | any | `init_git` hook |
| just | any | Justfile commands (optional for template dev) |
