import os
import sys
sys.path.insert(0, os.path.abspath("../src/"))
from sesparser import(
    __version__
)
release_notes = f"A stable public version {__version__} has been released for the python package **sesparser** which is available online at python packages [pypi library](https://pypi.org/project/sesparser/)\nThe latest version of the module can be installed through this below pip command:\n```pip install sesparser```\nIf you need to install it offline, then first download the [sesparser-{__version__}-py3-none-any.whl](https://github.com/suryavaddiraju/sesparser/releases/download/v{__version__}/sesparser-{__version__}-py3-none-any.whl) file attached in the assets part of this release note. then use this below pip command\n```pip install path/to/the/downloaded/whl/file```\nAdditional release note for this version is made available at the [HISTORY.MD](/HISTORY.MD) file located in this [github repository](https://github.com/suryavaddiraju/sesparser) root folder."
print(f'"version={__version__}" >> "$GITHUB_OUTPUT"')
print(f'"release_notes={release_notes}" >> "$GITHUB_OUTPUT"')