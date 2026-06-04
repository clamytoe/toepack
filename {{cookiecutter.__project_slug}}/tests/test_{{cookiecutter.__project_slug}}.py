from os import environ
from dotenv import load_dotenv
from {{ cookiecutter.__project_slug }} import __author__, __email__, __version__


def test_project_settings():
    assert __author__ == "{{ cookiecutter.author_name }}"
    assert __email__ == "{{ cookiecutter.author_email }}"
    assert __version__ == "{{ cookiecutter.version }}"


def test_env_loading(tmp_path, monkeypatch):
    # Create a temporary .env file
    env_file = tmp_path / ".env"
    env_file.write_text("TEST_KEY=12345\n")

    # Change working directory so dotenv loads from tmp_path
    monkeypatch.chdir(tmp_path)

    load_dotenv(env_file)  # Load the .env file

    # Ensure the variable is loaded
    assert environ.get("TEST_KEY") == "12345"
