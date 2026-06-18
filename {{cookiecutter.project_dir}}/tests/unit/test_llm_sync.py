import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def test_claude_and_agents_match_llm_source() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/sync_llm.py", "--check"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
