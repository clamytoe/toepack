"""
test_{{cookiecutter.project_name}}.py

Tests for {{cookiecutter.project_name}}.
"""
import {{cookiecutter.project_name}}


def test_main(capfd):
    app.main()
    output = capfd.readouterr()[0]
    assert output.strip() == "Successfully installed your project file: {{cookiecutter.project_name}}"
