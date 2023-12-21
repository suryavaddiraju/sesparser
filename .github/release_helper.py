import os
import sys
import uuid
current_dir = os.getcwd()

# Construct the relative path
relative_path = os.path.join(current_dir, './src/sesparser/')

# Get the absolute path
absolute_path = os.path.abspath(relative_path)
sys.path.insert(0, absolute_path)
print("Current directory:", current_dir)
print("Absolute path to 'src':", absolute_path)
print("sys.path:", sys.path)
from __version__ import(
    __version__
)
release_notes = f"""A stable public version {__version__} has been released for the python package **sesparser** which is available online at python packages [pypi library](https://pypi.org/project/sesparser/)
The latest version of the module can be installed through this below pip command:
```pip install sesparser```
If you need to install it offline, then first download the [sesparser-{__version__}-py3-none-any.whl](https://github.com/suryavaddiraju/sesparser/releases/download/v{__version__}/sesparser-{__version__}-py3-none-any.whl) file attached in the assets part of this release note. then use this below pip command
```pip install path/to/the/downloaded/whl/file```
Additional release note for this version is made available at the [HISTORY.MD](/HISTORY.MD) file located in this [github repository](https://github.com/suryavaddiraju/sesparser) root folder."""


def set_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{name}={value}', file=fh)


def set_multiline_output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        delimiter = uuid.uuid1()
        print(f'{name}<<{delimiter}', file=fh)
        print(value, file=fh)
        print(delimiter, file=fh)

set_output("version",__version__)
set_multiline_output("release_notes",release_notes)