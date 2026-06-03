import os
import shutil
import subprocess
from pathlib import Path


def remove_agents_md(project_dir: Path) -> None:
    target = project_dir / "AGENTS.md"
    if target.exists():
        target.unlink()


def remove_claude_md(project_dir: Path) -> None:
    target = project_dir / "CLAUDE.md"
    if target.exists():
        target.unlink()


def remove_approval_tests(project_dir: Path) -> None:
    target = project_dir / "tests" / "approval"
    if target.exists():
        shutil.rmtree(target)


def remove_hypothesis(pyproject_path: Path) -> None:
    lines = pyproject_path.read_text().splitlines()
    filtered = [line for line in lines if "hypothesis" not in line]
    pyproject_path.write_text("\n".join(filtered) + "\n")


def remove_mkdocs(project_dir: Path, pyproject_path: Path) -> None:
    docs = project_dir / "docs"
    if docs.exists():
        shutil.rmtree(docs)
    lines = pyproject_path.read_text().splitlines()
    filtered = [line for line in lines if "mkdocs" not in line]
    pyproject_path.write_text("\n".join(filtered) + "\n")


def configure_test_scheme(project_dir: Path, pyproject_path: Path, scheme: str) -> None:
    """Configure the test suite based on the selected scheme.

    unit               — unit tests only, no hypothesis, no approval tests
    unit_and_approval  — unit + approval tests, no hypothesis
    full               — keeps everything
    """
    if scheme == "unit":
        remove_approval_tests(project_dir)
        remove_hypothesis(pyproject_path)
    elif scheme == "unit_and_approval":
        remove_hypothesis(pyproject_path)
    # "full" keeps everything


def remove_github_actions(project_dir: Path) -> None:
    target = project_dir / ".github"
    if target.exists():
        shutil.rmtree(target)


def remove_gitlab_ci(project_dir: Path) -> None:
    target = project_dir / ".gitlab-ci.yml"
    if target.exists():
        target.unlink()


def init_git(project_dir: Path) -> None:
    subprocess.run(["git", "init"], cwd=project_dir, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.email", "scaffold@cookiecutter-eo-llm"],
        cwd=project_dir, check=True, capture_output=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "cookiecutter-eo-llm"],
        cwd=project_dir, check=True, capture_output=True,
    )
    subprocess.run(["git", "add", "."], cwd=project_dir, check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "chore: initial scaffold from cookiecutter-eo-llm"],
        cwd=project_dir,
        check=True,
        capture_output=True,
    )


def print_next_steps(project_dir: str, project_slug: str) -> None:
    print(f"""
✅  {project_dir} scaffolded.

    cd {project_dir}
    just setup        # install deps + pre-commit hooks
    just test         # run full test suite
    just run config/config_{project_slug}.yml

Update knowledge_base/ as the codebase evolves.
""")


def main() -> None:
    project_dir = Path.cwd()
    pyproject_path = project_dir / "pyproject.toml"

    primary_llm = os.environ.get("COOKIECUTTER_PRIMARY_LLM", "both")
    if primary_llm == "claude":
        remove_agents_md(project_dir)
    elif primary_llm == "codex":
        remove_claude_md(project_dir)

    if os.environ.get("COOKIECUTTER_INCLUDE_MKDOCS", "y") == "n":
        remove_mkdocs(project_dir, pyproject_path)

    ci_platform = os.environ.get("COOKIECUTTER_CI_PLATFORM", "github")
    if ci_platform == "github":
        remove_gitlab_ci(project_dir)
    elif ci_platform == "gitlab":
        remove_github_actions(project_dir)
    # "both" keeps both

    test_scheme = os.environ.get("COOKIECUTTER_TEST_SCHEME", "full")
    configure_test_scheme(project_dir, pyproject_path, test_scheme)

    init_git(project_dir)
    print_next_steps(project_dir.name, project_dir.name.replace("-", "_"))


if __name__ == "__main__":
    main()
