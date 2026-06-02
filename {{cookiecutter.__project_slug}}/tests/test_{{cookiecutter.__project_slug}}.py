from os import environ
from dotenv import load_dotenv
from {{ cookiecutter.__project_slug }} import __author__, __email__, __version__


def test_project_settings():
    assert __author__ == "{{ cookiecutter.author_name }}"
    assert __email__ == "{{ cookiecutter.author_email }}"
    assert __version__ == "{{ cookiecutter.version }}"


def test_env():
    load_dotenv()
    assert environ.get("TEST_VALUE") == "clamytoe"
