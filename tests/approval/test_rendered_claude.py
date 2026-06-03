from pathlib import Path


def test_claude_md_contains_stack_section(rendered: Path) -> None:
    content = (rendered / "CLAUDE.md").read_text()
    assert "## Stack" in content


def test_claude_md_contains_commands_section(rendered: Path) -> None:
    content = (rendered / "CLAUDE.md").read_text()
    assert "## Commands" in content


def test_claude_md_contains_boundaries_section(rendered: Path) -> None:
    content = (rendered / "CLAUDE.md").read_text()
    assert "## Boundaries" in content


def test_claude_md_source_of_truth_footer(rendered: Path) -> None:
    content = (rendered / "CLAUDE.md").read_text()
    assert "Source of truth: .llm/" in content
