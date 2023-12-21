import sys
import os
sys.path.insert(0, os.path.abspath("../src/"))
from sesparser import(
    __title__,
    __description__,
    __url__,
    __version__,
    __author__,
    __author_email__,
    __license__,
    __copyright__,
)
project = __title__
copyright = __copyright__
author = __author__
release = __version__
version = __version__
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    "myst_parser",
    "sphinx_rtd_theme",
]
intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
intersphinx_disabled_domains = ["std"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
templates_path = ['_templates']
epub_show_urls = 'footnote'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']