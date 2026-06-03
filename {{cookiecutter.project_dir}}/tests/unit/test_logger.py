import logging

import pytest

from {{cookiecutter.project_slug}}.logger import get_logger


def test_get_logger_returns_logger() -> None:
    assert isinstance(get_logger("test"), logging.Logger)


def test_get_logger_name_is_set() -> None:
    assert get_logger("my.module").name == "my.module"


def test_get_logger_level_is_info() -> None:
    assert get_logger("lvl").level == logging.INFO


def test_get_logger_has_stream_handler() -> None:
    logger = get_logger("handler.test")
    assert any(isinstance(h, logging.StreamHandler) for h in logger.handlers)


def test_get_logger_is_idempotent() -> None:
    first = get_logger("same.name")
    second = get_logger("same.name")
    assert first is second
    assert len(first.handlers) == 1


def test_get_logger_format_includes_level_and_name(caplog: pytest.LogCaptureFixture) -> None:
    logger = get_logger("{{cookiecutter.project_slug}}.test")
    with caplog.at_level(logging.INFO, logger="{{cookiecutter.project_slug}}.test"):
        logger.info("hello from test")
    assert "hello from test" in caplog.text
