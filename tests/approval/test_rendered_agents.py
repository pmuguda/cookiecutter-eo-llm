from pathlib import Path


def test_agents_md_contains_role_section(rendered: Path) -> None:
    content = (rendered / "AGENTS.md").read_text()
    assert "## Role" in content


def test_agents_md_contains_git_workflow_section(rendered: Path) -> None:
    content = (rendered / "AGENTS.md").read_text()
    assert "## Git workflow" in content


def test_agents_md_source_of_truth_footer(rendered: Path) -> None:
    content = (rendered / "AGENTS.md").read_text()
    assert "Source of truth: .llm/" in content


def test_agents_md_no_llm_coauthor(rendered: Path) -> None:
    content = (rendered / "AGENTS.md").read_text().lower()
    assert "co-authored-by" not in content
