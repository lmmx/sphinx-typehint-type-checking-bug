# -- Project information -----------------------------------------------------

project = "sphinx-demo"
copyright = "2021, Louis Maddox"
author = "Louis Maddox"

# The full version, including alpha/beta/rc tags
release = ""


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

suppress_warnings = [
    "app.add_node",
    "app.add_directive",
    "app.add_role",
    "app.add_generic_role",
    "app.add_source_parser",
    "download.not_readable",
    "image.not_readable",
    "ref.term",
    "ref.ref",
    "ref.numref",
    "ref.keyword",
    "ref.option",
    "ref.citation",
    "ref.footnote",
    "ref.doc",
    "ref.python",
    "misc.highlighting_failure",
    "toc.circular",
    "toc.secnum",
    "epub.unknown_project_files",
    "epub.duplicated_toc_entry",
    "autosectionlabel.*",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# Note: if both md and ipynb copies of each notebook exist (as they do when
# using jupytext) then listing ipynb before md ensures Myst will convert the
# notebook. Notebooks which are not executed have outputs as ipynb but not md,
# so the ipynb must be converted
source_suffix = [".rst"]

main_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
# autodoc_typehints = "description"

# https://github.com/sphinx-doc/sphinx/issues/5480
set_type_checking_flag = False

autosummary_generate = True
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
napoleon_use_rtype = True
napoleon_use_params = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
