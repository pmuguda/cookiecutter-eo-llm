import json
import os
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path

from cookiecutter.main import cookiecutter  # type: ignore[import-untyped]

# Map cookiecutter context keys to hook env var names
_CONTEXT_TO_ENV: dict[str, str] = {
    "ci_platform": "COOKIECUTTER_CI_PLATFORM",
    "test_scheme": "COOKIECUTTER_TEST_SCHEME",
    "primary_llm": "COOKIECUTTER_PRIMARY_LLM",
    "include_mkdocs": "COOKIECUTTER_INCLUDE_MKDOCS",
}


@contextmanager
def _env_override(mapping: dict[str, str]) -> Generator[None, None, None]:
    """Temporarily set environment variables, then restore originals."""
    originals = {k: os.environ.get(k) for k in mapping}
    os.environ.update(mapping)
    try:
        yield
    finally:
        for k, v in originals.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def render_template(output_dir: Path, extra_context: dict[str, str] | None = None) -> Path:
    template_root = Path(__file__).parents[2]
    config_path = template_root / "tests" / "resources" / "example_cookiecutter.json"
    context = json.loads(config_path.read_text())
    if extra_context:
        context.update(extra_context)

    # Build env overrides from context keys that the hook reads via env vars
    env_overrides: dict[str, str] = {}
    for ctx_key, env_key in _CONTEXT_TO_ENV.items():
        if ctx_key in context:
            env_overrides[env_key] = str(context[ctx_key])

    with _env_override(env_overrides):
        cookiecutter(
            str(template_root),
            no_input=True,
            extra_context=context,
            output_dir=str(output_dir),
        )
    project_dir: str = context["project_dir"]
    return output_dir / project_dir
