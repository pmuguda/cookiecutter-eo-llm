from pathlib import Path

import pytest


@pytest.fixture()
def project_dir(tmp_path: Path) -> Path:
    base = tmp_path / "my-eo-package"
    base.mkdir()
    (base / "CLAUDE.md").write_text("claude content")
    (base / "AGENTS.md").write_text("agents content")
    approval = base / "tests" / "approval"
    approval.mkdir(parents=True)
    (approval / "test_approval.py").write_text("# approval test")
    pyproject = base / "pyproject.toml"
    pyproject.write_text(
        '[project.optional-dependencies]\ndev = [\n    "hypothesis>=6.0",\n    "pytest>=9.0",\n]\n'
        'docs = [\n    "mkdocs>=1.6",\n]\n'
    )
    (base / "docs").mkdir()
    (base / ".github").mkdir()
    (base / ".gitlab-ci.yml").write_text("stages: [lint]")
    return base


def test_remove_agents_md_deletes_file(project_dir: Path) -> None:
    from hooks.post_gen_project import remove_agents_md

    remove_agents_md(project_dir)
    assert not (project_dir / "AGENTS.md").exists()
    assert (project_dir / "CLAUDE.md").exists()


def test_remove_claude_md_deletes_file(project_dir: Path) -> None:
    from hooks.post_gen_project import remove_claude_md

    remove_claude_md(project_dir)
    assert not (project_dir / "CLAUDE.md").exists()
    assert (project_dir / "AGENTS.md").exists()


def test_remove_approval_tests_deletes_dir(project_dir: Path) -> None:
    from hooks.post_gen_project import remove_approval_tests

    remove_approval_tests(project_dir)
    assert not (project_dir / "tests" / "approval").exists()


def test_remove_hypothesis_strips_dep(project_dir: Path) -> None:
    from hooks.post_gen_project import remove_hypothesis

    remove_hypothesis(project_dir / "pyproject.toml")
    content = (project_dir / "pyproject.toml").read_text()
    assert "hypothesis" not in content
    assert "pytest" in content


def test_remove_mkdocs_removes_docs_dir(project_dir: Path) -> None:
    from hooks.post_gen_project import remove_mkdocs

    remove_mkdocs(project_dir, project_dir / "pyproject.toml")
    assert not (project_dir / "docs").exists()
    content = (project_dir / "pyproject.toml").read_text()
    assert "mkdocs" not in content


def test_remove_github_actions_removes_dir(project_dir: Path) -> None:
    from hooks.post_gen_project import remove_github_actions

    remove_github_actions(project_dir)
    assert not (project_dir / ".github").exists()


def test_remove_gitlab_ci_removes_file(project_dir: Path) -> None:
    from hooks.post_gen_project import remove_gitlab_ci

    remove_gitlab_ci(project_dir)
    assert not (project_dir / ".gitlab-ci.yml").exists()
