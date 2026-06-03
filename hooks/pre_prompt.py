import sys

VALID_PYTHON_REQUIRES = [">=3.10", ">=3.11", ">=3.12"]


def validate_python_requires(python_requires: str) -> None:
    if python_requires not in VALID_PYTHON_REQUIRES:
        print(f"ERROR: python_requires must be one of {VALID_PYTHON_REQUIRES}")
        sys.exit(1)


if __name__ == "__main__":
    import os

    from cookiecutter.main import cookiecutter  # type: ignore[import-untyped]  # noqa: F401

    validate_python_requires(os.environ.get("COOKIECUTTER_PYTHON_REQUIRES", ">=3.10"))
