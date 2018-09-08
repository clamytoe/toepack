# Clamytoe's Package Template (*toepack*)
> *Bare minimum Python project templating system based on Cookiecutter.*

![Python version][python-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

This template's README was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) using this project.

The pack will create the basic framework for a commandline utility that can easily be modfied for other purposes. The following will be setup and configured for you:

* Project structure
* Generic Python .gitignore file
* Logging, with config and init files
* setup.py project file
* BetterCodeHub integration
* MIT License
* README.md with badges, like this one
* Sample headers.py file web scraping
* Testing with Pytest, with initial test
* TravisCI integration
* Virtual environment support, supports Anaconda envs


## Initial setup
The first thing that you must do is have Cookiecutter installed.

```bash
pip install --user cookiecutter
```

## Usage
```bash
cookiecutter https://github.com/clamytoe/toepack
```
Answer the prompts or accept the defaults.

### Alternate usage
You could also clone this repo and install it from that copy:
```bash
git clone https://github.com/clamytoe/toepack.git
cookiecutter toepack
```

## What does it create?
If you accept the defaults to the initial questions, this is what the directory structure of your new project will look like:
```bash
toepack_clone
├── .bettercodehub.yml
├── environment.yml
├── .gitignore
├── LICENSE
├── logging.json
├── README.md
├── requirements.txt
├── setup.py
├── tests
│   ├── __init__.py
│   └── test_toepack_clone.py
├── toepack_clone
│   ├── headers.py
│   ├── __init__.py
│   ├── log_init.py
│   └── app.py
└── .travis.yml

2 directories, 15 files
```
The **toepack_clone** is the default name of the project and it will change to whatever you enter during that prompt. 

> NOTE: I write a lot of scraping scripts, so the *headers.py* file contains user-agent entries for different browsers and platforms that I use as my headers, delete if you won't be using it.
 
## License
Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "toepack" is free and open source software.

## Issues
If you encounter any problems, please [file an issue](https://github.com/clamytoe/toepack/issues) along with a detailed description.

## Changelog
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

[python-version]:https://img.shields.io/badge/python-3.6.6-brightgreen.svg
[issues-image]:https://img.shields.io/github/issues/clamytoe/toepack.svg
[issues-url]:https://github.com/clamytoe/toepack/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/toepack.svg
[fork-url]:https://github.com/clamytoe/toepack/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/toepack.svg
[stars-url]:https://github.com/clamytoe/toepack/stargazers
[license-image]:https://img.shields.io/github/license/clamytoe/toepack.svg
[license-url]:https://github.com/clamytoe/toepack/blob/master/LICENSE
