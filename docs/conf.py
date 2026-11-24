from importlib.metadata import version as _version

project = "my-arithmetic-llamoity"
author = "llamoity"
language = "fr"
release = _version("my-arithmetic-llamoity")   # version calculée par hatch-vcs
version = ".".join(release.split(".")[:2])

extensions = [
    "sphinx.ext.autodoc",      # extrait les docstrings
    "sphinx.ext.napoleon",     # comprend le format numpy/google
    "sphinx.ext.viewcode",     # lien vers le code source
]
napoleon_numpy_docstring = True
napoleon_google_docstring = False

html_theme = "alabaster"
