"""
test_{{cookiecutter.project_name}}.py

Tests for {{cookiecutter.project_name}}.
"""
from {{cookiecutter.project_name}} import app


def test_main(capfd):
    app.main()
    output = capfd.readouterr()[0]
    assert output.strip() == "Successfully installed your project file: {{cookiecutter.project_name}}"
