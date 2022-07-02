from setuptools import setup

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(install_requires=[{% if cookiecutter.cli|lower == 'y' -%}"typer",{%- endif %}{% if cookiecutter.api|lower == 'y' -%}"fastapi","pydantic","uvicorn"{%- endif %}])
