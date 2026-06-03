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
    "config/config_my_eo_package.yml",
    "src/my_eo_package/__init__.py",
    "src/my_eo_package/py.typed",
    "src/my_eo_package/main.py",
    "src/my_eo_package/logger.py",
    "src/my_eo_package/workflow/__init__.py",
    "src/my_eo_package/workflow/base.py",
    "src/my_eo_package/workflow/example.py",
    "src/my_eo_package/config/__init__.py",
    "src/my_eo_package/config/models.py",
    "tests/conftest.py",
    "tests/helpers/config_builder.py",
    "tests/resources/example_workflow.yaml",
    "tests/resources/invalid_workflow.yaml",
    "tests/unit/test_logger.py",
    "tests/unit/test_main.py",
    "tests/unit/test_base_workflow.py",
    "tests/unit/test_example_workflow.py",
    "tests/unit/test_config_models.py",
    "tests/integration/.gitkeep",
    "tests/approval/test_approval.py",
    "tests/approval/approved_files/.gitkeep",
    "notebooks/00_my_eo_package_exploration.ipynb",
    "scripts/example_script.py",
    "docs/mkdocs.yml",
    "docs/index.md",
    "docs/api/index.md",
    ".github/workflows/ci.yml",
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


def test_publish_yml_does_not_exist(rendered: Path) -> None:
    assert not (rendered / ".github" / "workflows" / "publish.yml").exists()


def test_github_ci_has_all_jobs(rendered: Path) -> None:
    content = (rendered / ".github" / "workflows" / "ci.yml").read_text()
    for job in ("build:", "test-dev:", "test-release:", "deploy-docs:", "deploy-pypi:"):
        assert job in content, f"Missing job: {job}"


def test_github_ci_test_dev_not_on_tags(rendered: Path) -> None:
    content = (rendered / ".github" / "workflows" / "ci.yml").read_text()
    assert "!startsWith(github.ref, 'refs/tags/v')" in content


def test_github_ci_deploy_pypi_uses_dist_artifact(rendered: Path) -> None:
    content = (rendered / ".github" / "workflows" / "ci.yml").read_text()
    assert "name: dist" in content
    assert "uv publish dist/*" in content


def test_gitlab_ci_has_three_stages(rendered: Path) -> None:
    content = (rendered / ".gitlab-ci.yml").read_text()
    for stage in ("build", "test", "deploy"):
        assert stage in content, f"Missing stage: {stage}"


def test_gitlab_ci_has_test_dev_and_test_release(rendered: Path) -> None:
    content = (rendered / ".gitlab-ci.yml").read_text()
    assert "test-dev:" in content
    assert "test-release:" in content


def test_gitlab_ci_deploy_uses_build_artifact(rendered: Path) -> None:
    content = (rendered / ".gitlab-ci.yml").read_text()
    assert "artifacts: true" in content
    assert "dist/*" in content


def test_ci_platform_github_keeps_github_removes_gitlab(tmp_path: Path) -> None:
    from tests.helpers.render import render_template

    rendered = render_template(tmp_path, extra_context={"ci_platform": "github"})
    assert (rendered / ".github" / "workflows" / "ci.yml").exists()
    assert not (rendered / ".gitlab-ci.yml").exists()


def test_ci_platform_gitlab_keeps_gitlab_removes_github(tmp_path: Path) -> None:
    from tests.helpers.render import render_template

    rendered = render_template(tmp_path, extra_context={"ci_platform": "gitlab"})
    assert not (rendered / ".github").exists()
    assert (rendered / ".gitlab-ci.yml").exists()


def test_ci_platform_both_keeps_both(tmp_path: Path) -> None:
    from tests.helpers.render import render_template

    rendered = render_template(tmp_path, extra_context={"ci_platform": "both"})
    assert (rendered / ".github" / "workflows" / "ci.yml").exists()
    assert (rendered / ".gitlab-ci.yml").exists()
