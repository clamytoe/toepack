# Clamytoe's Project Template (*toepack_clone*)
> *Bare minimum project templating system.*

![Python version][python-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

This app was generated with [Cookiecutter](https://github.com/audreyr/cookiecutter) along with [@clamytoe's](https://github.com/clamytoe) [toepack](https://github.com/clamytoe/toepack) project template.

### Initial setup
```bash
cd Projects
git clone https://github.com/clamytoe/toepack.git
cd toepack
```

#### Anaconda setup
```bash
conda env create
```

#### Regular Python setup
```bash
pip install -r requirements.txt
```

#### Final setup
```bash
activate toepack # or source activate toepack
pip install -e .
```

## Usage
```bash
toepack
```

## Contributing
Contributions are very welcome. Tests can be run with with `pytest -v`, please ensure that all tests are passing before submitting a pull request. I have also included the following packages that should be used:
* black
* flake8
* isort
* pylint

I am not adhering to them strictly, but try to clean up what's reasonable.

## License
Distributed under the terms of the [MIT](https://opensource.org/licenses/MIT) license, "toepack" is free and open source software.

## Issues
If you encounter any problems, please [file an issue](https://github.com/clamytoe/toepack/issues) along with a detailed description.


[python-version]:https://img.shields.io/badge/python-3.6.6-brightgreen.svg
[issues-image]:https://img.shields.io/github/issues/clamytoe/toepack.svg
[issues-url]:https://github.com/clamytoe/toepack/issues
[fork-image]:https://img.shields.io/github/forks/clamytoe/toepack.svg
[fork-url]:https://github.com/clamytoe/toepack/network
[stars-image]:https://img.shields.io/github/stars/clamytoe/toepack.svg
[stars-url]:https://github.com/clamytoe/toepack/stargazers
[license-image]:https://img.shields.io/github/license/clamytoe/toepack.svg
[license-url]:https://github.com/clamytoe/toepack/blob/master/LICENSE
