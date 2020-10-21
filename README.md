# Clamytoe's Package Template (*toepack*)

> *Simple Python project templating system based on Cookiecutter.*

![Python version][python-version]
![Latest version][latest-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

The pack will create the basic framework for a command line utility that can easily be modified for other purposes. The following will be setup and configured for you:

* Project structure
* Generic Python .gitignore file
* setup.py project file
* MIT License
* README.md with badges, like this README
* Sample headers.py file for web scraping
* Testing with Pytest, with initial test
* Virtual environment support
  * requirements.txt  ([venv](https://docs.python.org/3/library/venv.html))
  * requirements-dev.txt
  * environment.yml   ([conda](https://conda.io/docs/))

## Initial setup

The first thing that you must do is have Cookiecutter installed.

```zsh
pip install --user cookiecutter
```

## Usage

```zsh
cookiecutter https://github.com/clamytoe/toepack
```

Answer the prompts or accept the defaults.

### Alternate usage

You could also clone this repo and install it from that copy:

```zsh
git clone https://github.com/clamytoe/toepack.git
cookiecutter toepack
```

## What it does

If you accept the defaults to the initial questions, this is what the directory structure of your new project will look like:

```zsh
.
├── LICENSE
├── README.md
├── environment.yml
├── requirements-dev.txt
├── requirements.txt
├── setup.py
├── tests
│   ├── __init__.py
│   └── test_toepack_clone.py
└── toepack_clone
    ├── __init__.py
    ├── app.py
    └── headers.py

2 directories, 11 files
```

The **toepack_clone** is the default name of the project and it will change to whatever you enter during that prompt.

> NOTE: I write a lot of web scraping scripts, so the *headers.py* file contains user-agent entries for different browsers and platforms that I use as my headers, delete if you won't be using it.

## Create your virtual environment

Now that your project's structure has been created, you can now create a virtual environment to work from.
The README.md file that's created, will tell you how to create your it with normal python or with Anaconda.

## License

Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "toepack" is free and open source software.

## Issues

If you encounter any problems, please [file an issue](https://github.com/clamytoe/toepack/issues) along with a detailed description.

## Changelog

* **v0.4.0** Removed logging fromt the project, I never really use it on my small scripts and always end up removed it.
* **v0.3.1** Added flake8 to the requirements-dev.txt and environment.yml files.
* **v0.3.0** Removed poetry support since I don't really use it and updated the cookiecutter.json file
* **v0.2.8** Replaced instances of os.path with pathlib.Path and created a logs directory.
* **v0.2.7** Added pyproject.toml for poetry support.
* **v0.2.6** Removed unused linters, added mypy and version badge.
* **v0.2.5** Removed hard set version numbers for the environment/requirement packages.
* **v0.2.4** Added pytest-coverage to the developer dependencies and replaced flake8 with pycodestyle.
* **v0.2.3** Fixed a bug with the logging setup. It would only read in config if project started from project directory.
* **v0.2.2** Disabled logging during tests and prevented log level INFO from displaying in the console.
* **v0.2.1** Added more detail to the README.md file.
* **v0.2.0** Renamed the main script to *app.py*. I did not like the repeat name chaining..
* **v0.1.3** Fixed bug in project_title variable name in the main script template.
* **v0.1.2** Borrowed some setup.py code from [https://github.com/pypa/sampleproject](https://github.com/pypa/sampleproject)
* **v0.1.1** Added changelog to README.md file.
* **v0.1.0** Initial commit.

[python-version]:https://img.shields.io/badge/python-3.6+-brightgreen.svg
[latest-version]:https://img.shields.io/badge/version-0.4.0-blue.svg
[issues-image]:https://img.shields.io/github/issues/clamytoe/toepack.svg
[issues-url]:https://github.com/clamytoe/toepack/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/toepack.svg
[fork-url]:https://github.com/clamytoe/toepack/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/toepack.svg
[stars-url]:https://github.com/clamytoe/toepack/stargazers
[license-image]:https://img.shields.io/github/license/clamytoe/toepack.svg
[license-url]:https://github.com/clamytoe/toepack/blob/master/LICENSE
