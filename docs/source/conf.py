# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project specific imports ------------------------------------------------

import datetime
import sys

# -- Project information -----------------------------------------------------

project = "Outreachy Internships with JupyterHub"
copyright = f"{datetime.date.today().year}, Project Jupyter Contributors"
author = "Project Jupyter Contributors"


# -- General configuration ---------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Set the default role so we can use `foo` instead of ``foo``
default_role = "literal"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_copybutton",
    "sphinx_design",
    "myst_parser",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The root toctree document.
root_doc = master_doc = "index"

# The suffix(es) of source filenames.
source_suffix = [".md", ".rst"]

# -- Options for HTML output -------------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "github_url": "https://github.com/jupyterhub/outreachy/",
    "use_edit_page_button": True,
}
html_context = {
    "github_user": "jupyterhub",
    "github_repo": "outreachy",
    "github_version": "main",
    "doc_path": "docs/source",
}

html_favicon = "_static/images/logo/favicon.ico"
html_logo = "_static/images/logo/logo.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# -- Options for linkcheck builder -------------------------------------------
# ref: https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

# A list of regular expressions that match anchors Sphinx should skip when checking
# the validity of anchors in links. Outreachy.org is a notoriously buggy website,
# especially regarding anchors that do not redirect properly.

linkcheck_ignore = ["https://www.outreachy.org/docs/community/#", "(.*)?README.md#"]

# -- Custom scripts ----------------------------------------------------------
import os  # noqa: E402
import subprocess  # noqa: E402

# This script makes calls to the GitHub API, so only run it inside ReadTheDocs
READTHEDOCS = os.environ.get("READTHEDOCS", False)
if READTHEDOCS:
    # Generate tables of issues
    subprocess.run([sys.executable, "_data/get_issues/get-repo-issues.py"], check=True)

# Generate tables of Outreachy interns per cohort
subprocess.run(
    ["python", "_data/outreachy_participants/outreachy_participants.py"], check=True
)
