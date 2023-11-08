"""
test_{{cookiecutter.__project_slug}}.py

Tests for {{cookiecutter.__project_slug}}.
"""
from os import environ
from dotenv import load_dotenv
from {{cookiecutter.__project_slug}} import __version__


def test_version():
    assert __version__ == '{{cookiecutter.version}}'


def test_env():
    load_dotenv()
    assert environ.get("TEST_VALUE") == "clamytoe"
