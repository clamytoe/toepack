"""
test_{{cookiecutter.project_name}}.py

Tests for {{cookiecutter.project_name}}.
"""
from os import environ
from dotenv import load_dotenv
from {{cookiecutter.project_name}} import __version__


def test_version():
    assert __version__ == '{{cookiecutter.version}}'


def test_env():
    load_dotenv()
    assert environ.get("TEST_VALUE") == "clamytoe"
