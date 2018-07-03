# -*- coding: utf-8 -*-
import {{cookiecutter.project_name}}


def test_main(capfd):
    {{cookiecutter.project_name}}.main()
    output = capfd.readouterr()[0]
    assert output.strip() == "Successfully installed your project file: {{cookiecutter.project_name}}"
