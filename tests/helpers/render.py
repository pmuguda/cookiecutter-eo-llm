import json
from pathlib import Path

from cookiecutter.main import cookiecutter  # type: ignore[import-untyped]


def render_template(output_dir: Path, extra_context: dict[str, str] | None = None) -> Path:
    template_root = Path(__file__).parents[2]
    config_path = template_root / "tests" / "resources" / "example_cookiecutter.json"
    context = json.loads(config_path.read_text())
    if extra_context:
        context.update(extra_context)
    cookiecutter(
        str(template_root),
        no_input=True,
        extra_context=context,
        output_dir=str(output_dir),
    )
    project_dir: str = context["project_dir"]
    return output_dir / project_dir
