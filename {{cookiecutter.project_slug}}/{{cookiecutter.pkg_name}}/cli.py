"""Console script for {{cookiecutter.pkg_name}}."""
{%- if cookiecutter.command_line_interface|lower == 'typer' %}

import typer

{%- if cookiecutter.api|lower == 'fastapi' %}

from {{ cookiecutter.pkg_name }} import api
{% endif %}
app = typer.Typer()


@app.command()
def main() -> None:
    """Main entrypoint."""

{%- if cookiecutter.api|lower == 'fastapi' %}
    api.run()
{%- elif cookiecutter.command_line_interface|lower == 'typer' %}
    typer.echo("{{ cookiecutter.project_slug }}")
    typer.echo("=" * len("{{ cookiecutter.project_slug }}"))
    typer.echo("{{ cookiecutter.description }}")
{% endif -%}
{%- endif %}
