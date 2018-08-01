"""
test_{{cookiecutter.project_name}}.py

Tests for {{cookiecutter.project_name}}.
"""
import logging

from {{cookiecutter.project_name}} import app

logging.disable(logging.CRITICAL)


def test_main(capfd):
    app.main()
    output = capfd.readouterr()[0]
    assert output.strip() == "Successfully installed your project file: {{cookiecutter.project_name}}"
