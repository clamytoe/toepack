"""
setup.py

Setup for installing the package.
"""
from setuptools import setup, find_packages
from os import path
from io import open

import {{cookiecutter.project_name}}

VERSION = {{cookiecutter.project_name}}.__version__
AUTHOR = {{cookiecutter.project_name}}.__author__
EMAIL = {{cookiecutter.project_name}}.__email__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="{{cookiecutter.project_name}}",
    version=VERSION,
    description="{{cookiecutter.description}} ({{cookiecutter.project_name}})",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}",
    author=AUTHOR,
    author_email=EMAIL,
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        # How mature is this project? Common values are
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        #   6 - Mature
        #   7 - Inactive
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: {{cookiecutter.python_version}}",
    ],
    keywords="python utility",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),
    install_requires=["pytest"],
    license="MIT",
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_name}}={{cookiecutter.project_name}}.app:main"
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}/issues',
        'Source': 'https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}/',
    },
)
