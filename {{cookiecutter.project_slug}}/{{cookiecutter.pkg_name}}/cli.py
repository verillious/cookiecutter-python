"""Console script for {{cookiecutter.pkg_name}}."""
{%- if cookiecutter.cli|lower == 'y' %}

import typer

{%- if cookiecutter.api|lower == 'y' %}

from {{ cookiecutter.pkg_name }} import api
{% endif %}
app = typer.Typer()


@app.command()
def main() -> None:
    """Main entrypoint."""

{%- if cookiecutter.api|lower == 'y' %}
    api.run()
{%- elif cookiecutter.cli|lower == 'y' %}
    typer.echo("{{ cookiecutter.project_slug }}")
    typer.echo("=" * len("{{ cookiecutter.project_slug }}"))
    typer.echo("{{ cookiecutter.description }}")
{% endif -%}
{%- endif %}
