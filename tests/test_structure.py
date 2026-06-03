from pathlib import Path

import pytest

EXPECTED_PATHS = [
    "pyproject.toml",
    "Justfile",
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CLAUDE.md",
    "AGENTS.md",
    ".pre-commit-config.yaml",
    ".gitignore",
    ".editorconfig",
    ".llm/context.md",
    ".llm/stack.md",
    ".llm/commands.md",
    ".llm/boundaries.md",
    "knowledge_base/architecture.md",
    "knowledge_base/workflows.md",
    "knowledge_base/decisions.md",
    "knowledge_base/changelog_context.md",
    "config/example_workflow.yaml",
    "src/my_eo_package/__init__.py",
    "src/my_eo_package/py.typed",
    "src/my_eo_package/main.py",
    "src/my_eo_package/workflows/__init__.py",
    "src/my_eo_package/workflows/base.py",
    "src/my_eo_package/workflows/example.py",
    "src/my_eo_package/config/__init__.py",
    "src/my_eo_package/config/models.py",
    "tests/conftest.py",
    "tests/helpers/config_builder.py",
    "tests/resources/example_workflow.yaml",
    "tests/resources/invalid_workflow.yaml",
    "tests/unit/test_main.py",
    "tests/unit/test_base_workflow.py",
    "tests/unit/test_example_workflow.py",
    "tests/unit/test_config_models.py",
    "tests/integration/.gitkeep",
    "tests/approval/test_approval.py",
    "tests/approval/approved_files/.gitkeep",
    "notebooks/00_exploration.ipynb",
    "scripts/example_script.py",
    "docs/mkdocs.yml",
    "docs/index.md",
    "docs/api/index.md",
    ".github/workflows/ci.yml",
    ".github/workflows/publish.yml",
    ".gitlab-ci.yml",
]


@pytest.mark.parametrize("rel_path", EXPECTED_PATHS)
def test_expected_path_exists(rendered: Path, rel_path: str) -> None:
    assert (rendered / rel_path).exists(), f"Missing: {rel_path}"


def test_project_dir_is_kebab(rendered: Path) -> None:
    assert rendered.name == "my-eo-package"


def test_project_slug_is_snake(rendered: Path) -> None:
    assert (rendered / "src" / "my_eo_package").is_dir()


def test_claude_md_under_200_lines(rendered: Path) -> None:
    lines = (rendered / "CLAUDE.md").read_text().splitlines()
    assert len(lines) <= 200, f"CLAUDE.md has {len(lines)} lines (limit 200)"


def test_agents_md_under_200_lines(rendered: Path) -> None:
    lines = (rendered / "AGENTS.md").read_text().splitlines()
    assert len(lines) <= 200, f"AGENTS.md has {len(lines)} lines (limit 200)"


def test_llm_directory_has_four_files(rendered: Path) -> None:
    llm_dir = rendered / ".llm"
    files = {f.name for f in llm_dir.iterdir() if f.is_file()}
    assert files == {"context.md", "stack.md", "commands.md", "boundaries.md"}


def test_no_llm_coauthor_in_pyproject(rendered: Path) -> None:
    content = (rendered / "pyproject.toml").read_text().lower()
    assert "co-authored-by" not in content
    assert "generated-by" not in content


def test_project_dir_in_pyproject_name(rendered: Path) -> None:
    content = (rendered / "pyproject.toml").read_text()
    assert 'name = "my-eo-package"' in content


def test_project_slug_in_pyproject_scripts(rendered: Path) -> None:
    content = (rendered / "pyproject.toml").read_text()
    assert "my_eo_package.main:app" in content
