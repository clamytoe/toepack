# {{cookiecutter.project_title}} (*{{cookiecutter.project_name}}*)
> *{{cookiecutter.description}}*

![Python version][python-version]
![Latest version][latest-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

NOTE: This app was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with [@clamytoe's](https://github.com/clamytoe) [toepack](https://github.com/clamytoe/toepack) project template.

### Initial setup
```zsh
cd Projects
git clone https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}.git
cd {{cookiecutter.project_name}}
```

#### Anaconda setup
If you are an Anaconda user, this command will get you up to speed with the base installation.
```zsh
conda env create
conda activate {{cookiecutter.project_name}}
```

#### Regular Python setup
If you are just using normal Python, this will get you ready, but I highly recommend that you do this in a virtual environment. There are many ways to do this, the simplest using *venv*.
```zsh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Final setup
```zsh
pip install -e .
```

## Usage
```zsh
{{cookiecutter.project_name}}
```

## Contributing
Contributions are very welcome. Tests can be run with with `pytest -v`, please ensure that all tests are passing and that you've checked your code with the following packages before submitting a pull request:
* black
* isort
* mypy
* pytest-cov

I am not adhering to them strictly, but try to clean up what's reasonable.

## License
Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "{{cookiecutter.project_name}}" is free and open source software.

## Issues
If you encounter any problems, please [file an issue](https://github.com/clamytoe/toepack/issues) along with a detailed description.

## Changelog
* **v{{cookiecutter.version}}** Initial commit.

[python-version]:https://img.shields.io/badge/python-{{cookiecutter.python_version}}-brightgreen.svg
[latest-version]:https://img.shields.io/badge/version-{{cookiecutter.version}}-blue.svg
[issues-image]:https://img.shields.io/github/issues/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}.svg
[issues-url]:https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}/issues
[fork-image]:https://img.shields.io/github/forks/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}.svg
[fork-url]:https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}/network
[stars-image]:https://img.shields.io/github/stars/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}.svg
[stars-url]:https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}/stargazers
[license-image]:https://img.shields.io/github/license/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}.svg
[license-url]:https://github.com/{{cookiecutter.github_account}}/{{cookiecutter.project_name}}/blob/master/LICENSE
