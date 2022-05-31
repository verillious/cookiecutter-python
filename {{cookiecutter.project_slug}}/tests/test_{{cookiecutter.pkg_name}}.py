"""Tests for `{{ cookiecutter.pkg_name }}` package."""

import importlib
{% if cookiecutter.api|lower == 'fastapi' %}
from fastapi.testclient import TestClient

from {{ cookiecutter.pkg_name }}.api import app

client = TestClient(app)


def test_api_get_root():
    """test that the api launches"""

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "{{ cookiecutter.project_slug }} {{ cookiecutter.version }}"
{% elif cookiecutter.command_line_interface|lower == 'typer' %}

from typer.testing import CliRunner

from {{ cookiecutter.pkg_name }}.cli import app


def test_command_line_interface():
    """Test the CLI."""

    runner = CliRunner()
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "{{ cookiecutter.project_slug }}" in result.output
    help_result = runner.invoke(app, ["--help"])
    assert help_result.exit_code == 0
    assert "--help                          Show this message and exit.\n" in help_result.output


{% endif %}

def test_import():
    """Test that importing the package works"""

    spec = importlib.util.find_spec("{{ cookiecutter.pkg_name }}")
    assert spec
