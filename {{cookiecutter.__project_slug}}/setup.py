"""
setup.py

Setup for installing the package.
"""
from setuptools import setup, find_packages
from pathlib import Path

import {{cookiecutter.__project_slug}}

VERSION = {{cookiecutter.__project_slug}}.__version__
AUTHOR = {{cookiecutter.__project_slug}}.__author__
EMAIL = {{cookiecutter.__project_slug}}.__email__

BASE_DIR = Path(__file__).resolve().parent
README = BASE_DIR.joinpath("README.md")

setup(
    name="{{cookiecutter.__project_slug}}",
    version=VERSION,
    description="{{cookiecutter.description}} ({{cookiecutter.__project_slug}})",
    long_description=README.read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.__project_slug}}",
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
        "Development Status :: 1 - Planning",
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
            "{{cookiecutter.__project_slug}}={{cookiecutter.__project_slug}}.app:main"
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.__project_slug}}/issues',
        'Source': 'https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.__project_slug}}/',
    },
)
