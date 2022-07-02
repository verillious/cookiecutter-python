from pathlib import Path
from shutil import rmtree

slug = "{{ cookiecutter.project_slug }}"
pkg_path = Path.cwd()

create_workflows = "{{cookiecutter.github_workflows}}" != "n"
create_api = "{{cookiecutter.api}}" != "n"
create_cli = "{{cookiecutter.cli}}" != "n"

if not create_workflows:
    workflow_path = pkg_path / ".github"
    rmtree(workflow_path)

if not create_api:
    api_path = pkg_path / "{{ cookiecutter.pkg_name }}" / "api.py"
    api_path.unlink()

if not create_cli:
    cli_path = pkg_path / "{{ cookiecutter.pkg_name }}" / "cli.py"
    cli_path.unlink()
