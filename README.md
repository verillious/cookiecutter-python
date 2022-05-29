# 🍪 cookiecutter-python
A Cookiecutter template for python packages

## Features

This tool will create Python project with the following features:

* [Tox](https://tox.readthedocs.io): Run formatting, linting, code-checking and other CI features with tox.
* [EditorConfig](https://editorconfig.org/): Maintain consistent coding styles for multiple developers working on the same project
* Testing with [Pytest](https://pytest.org)
* Code coverage report by [Codecov](https://codecov.io)
* Format with [Black](https://github.com/psf/black) and [Isort](https://github.com/PyCQA/isort)
* Lint code with [Pylint](https://pylint.pycqa.org/en/latest/) and [Flake8](https://flake8.pycqa.org)
* Check static type with [Mypy](http://mypy-lang.org/)
* Check for code vulnerabilities with [Bandit](https://bandit.readthedocs.io/en/latest/)
* Build docs with [Sphinx](https://www.sphinx-doc.org/en/master/index.html)
* Command line interface using [Click](https://click.palletsprojects.com/en/8.0.x/) (optional)
* [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping and tagging with a single command

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Generate a Python package project:

```
cookiecutter verillious/cookiecutter-python
```
