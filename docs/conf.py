extensions = ["sphinx.ext.autodoc"]

# Project info

project = "sample-klein-app"
copyright = "2016-2017"
author = u"Wilfredo S\xe1nchez Vega"

# File names

templates_path = []
html_static_path = []
source_suffix = [".rst", ".md"]
master_doc = "index"
exclude_patterns = []

# Styling

html_theme = "sphinx_rtd_theme"

# Pedantry

nitpick_ignore = [
    # Bugs in Python documentation
    ("py:class", "float"     ),
    ("py:class", "int"       ),
    ("py:class", "object"    ),
    ("py:class", "Union"     ),
    ("py:data" , "sys.argv"  ),
    ("py:exc"  , "ValueError"),
    ("py:obj"  , "None"      ),
]
