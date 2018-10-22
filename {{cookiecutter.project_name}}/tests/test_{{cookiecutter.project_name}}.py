"""
test_{{cookiecutter.project_name}}.py

Tests for {{cookiecutter.project_name}}.
"""
import logging

from {{cookiecutter.project_name}} import __version__

logging.disable(logging.CRITICAL)


def test_version():
    assert __version__ == '{{cookiecutter.version}}'
