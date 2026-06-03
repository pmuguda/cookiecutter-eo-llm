from pathlib import Path

import pytest

from tests.helpers.render import render_template


@pytest.fixture(scope="session")
def rendered(tmp_path_factory: pytest.TempPathFactory) -> Path:
    output_dir = tmp_path_factory.mktemp("rendered")
    return render_template(output_dir)
