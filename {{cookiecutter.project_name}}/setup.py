from setuptools import setup, find_packages

import {{cookiecutter.project_name}}

VERSION = {{cookiecutter.project_name}}.__version__
AUTHOR = {{cookiecutter.project_name}}.__author__
EMAIL = {{cookiecutter.project_name}}.__email__

setup(
    name="{{cookiecutter.project_name}}",
    version=VERSION,
    packages=find_packages(),
    url="https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}",
    license="MIT",
    author=AUTHOR,
    author_email=EMAIL,
    description="{{cookiecutter.description}} ({{cookiecutter.project_name}})",
    install_requirements=[],
    entry_points="""
        [console_scripts]
        {{cookiecutter.project_name}}={{cookiecutter.project_name}}.{{cookiecutter.project_name}}:main
    """,
)
