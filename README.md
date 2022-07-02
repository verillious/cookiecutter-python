# 🍪 cookiecutter-python

![Black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Pulse](https://img.shields.io/github/commit-activity/m/verillious/cookiecutter-python)
![Checks](https://github.com/verillious/cookiecutter-python/actions/workflows/check.yml/badge.svg)

A Cookiecutter template for python packages

## Features

This tool will create a Python project with the following features:

* [Tox](https://tox.readthedocs.io): Run formatting, linting, code-checking and other CI features with tox.
* [EditorConfig](https://editorconfig.org/): Maintain consistent coding styles for multiple developers working on the same project
* Testing with [Pytest](https://pytest.org)
* Code coverage report by [Codecov](https://codecov.io)
* Format with [Black](https://github.com/psf/black) and [Isort](https://github.com/PyCQA/isort)
* Lint code with [Pylint](https://pylint.pycqa.org/en/latest/) and [Flake8](https://flake8.pycqa.org)
* Check static type with [Mypy](http://mypy-lang.org/)
* Check for code vulnerabilities with [Bandit](https://bandit.readthedocs.io/en/latest/)
* Build docs with [Sphinx](https://www.sphinx-doc.org/en/master/index.html)
* Command line interface using [typer](https://typer.tiangolo.com/) (optional)
* API using [fastapi](https://fastapi.tiangolo.com/) (optional)
* GitHub workflows for uploading to PyPI and running code checks
* [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping and tagging with a single command

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Generate a Python package project:

```
cookiecutter gh:verillious/cookiecutter-python
```
