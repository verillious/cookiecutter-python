import os
import subprocess
from contextlib import contextmanager

import pytest


@contextmanager
def cwd(path):
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


def test_bake_project(cookies):
    result = cookies.bake()
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "python-boilerplate"
    assert result.project_path.is_dir()

    tests_dir = result.project_path / "tests"
    core_dir = result.project_path / "python_boilerplate"
    docs_dir = result.project_path / "docs"

    for entry in [f.name for f in result.project_path.iterdir()]:
        assert entry in [
            ".bumpversion.cfg",
            ".editorconfig",
            ".gitignore",
            "CHANGELOG.md",
            "docs",
            "python_boilerplate",
            "README.md",
            "setup.cfg",
            "setup.py",
            "tests",
            "tox.ini",
        ]

    tests_level = [f.name for f in tests_dir.iterdir()]
    assert tests_level == ["test_python_boilerplate.py", "__init__.py"]

    core_level = [f.name for f in core_dir.iterdir()]
    assert core_level == ["core.py", "__init__.py"]

    docs_level = [f.name for f in docs_dir.iterdir()]
    assert docs_level == ["conf.py", "index.rst"]


def test_bake_with_api(cookies):
    result = cookies.bake(extra_context={"api": "y"})
    assert result.exit_code == 0
    core_dir = result.project_path / "python_boilerplate"

    for entry in [f.name for f in core_dir.iterdir()]:
        assert entry in ["api.py", "core.py", "__init__.py"]


def test_bake_with_cli(cookies):
    result = cookies.bake(extra_context={"cli": "y"})
    assert result.exit_code == 0
    core_dir = result.project_path / "python_boilerplate"

    for entry in [f.name for f in core_dir.iterdir()]:
        assert entry in ["cli.py", "core.py", "__init__.py"]


def test_bake_with_workflows(cookies):
    result = cookies.bake(extra_context={"github_workflows": "y"})
    assert result.exit_code == 0
    workflow_dir = result.project_path / ".github" / "workflows"

    for entry in [f.name for f in workflow_dir.iterdir()]:
        assert entry in ["publish.yml", "check.yml"]


def test_bake_with_api_and_cli(cookies):
    result = cookies.bake(extra_context={"api": "y", "cli": "y"})
    assert result.exit_code == 0
    core_dir = result.project_path / "python_boilerplate"

    for entry in [f.name for f in core_dir.iterdir()]:
        assert entry in ["api.py", "cli.py", "core.py", "__init__.py"]


@pytest.mark.parametrize(
    "config",
    [{"api": "y", "cli": "y"}, {"api": "n", "cli": "n"}, {"api": "n", "cli": "y"}],
    ids=["all", "none", "cli"],
)
def test_run_tox(cookies, config):
    result = cookies.bake(extra_context=config)
    assert result.exit_code == 0
    with cwd(str(result.project_path)):
        process = subprocess.run(["tox"], capture_output=True, text=True)
        print(process.stdout)
        print(process.stderr)
        assert process.returncode == 0
