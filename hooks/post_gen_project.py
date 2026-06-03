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
    just run config/example_workflow.yaml

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

    if os.environ.get("COOKIECUTTER_INCLUDE_APPROVAL_TESTS", "y") == "n":
        remove_approval_tests(project_dir)

    if os.environ.get("COOKIECUTTER_INCLUDE_HYPOTHESIS", "y") == "n":
        remove_hypothesis(pyproject_path)

    if os.environ.get("COOKIECUTTER_INCLUDE_MKDOCS", "y") == "n":
        remove_mkdocs(project_dir, pyproject_path)

    if os.environ.get("COOKIECUTTER_INCLUDE_GITHUB_ACTIONS", "y") == "n":
        remove_github_actions(project_dir)

    if os.environ.get("COOKIECUTTER_INCLUDE_GITLAB_CI", "y") == "n":
        remove_gitlab_ci(project_dir)

    init_git(project_dir)
    print_next_steps(project_dir.name, project_dir.name.replace("-", "_"))


if __name__ == "__main__":
    main()
