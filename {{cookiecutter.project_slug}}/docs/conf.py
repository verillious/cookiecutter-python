project = "{{ cookiecutter.project_name }}"
copyright = "{{ cookiecutter.year }}, {{ cookiecutter.full_name }}"
author = "{{ cookiecutter.full_name }}"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_book_theme"
html_theme_options = {
    "single_page": True,
    "use_fullscreen_button": False,
}
extensions = ["m2r2"]
source_suffix = [".rst", ".md"]
