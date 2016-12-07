#!/usr/bin/env python

"""
Setuptools configuration
"""

import sys
from pathlib import Path
from setuptools import setup, find_packages

sys.path.insert(0, "src")

from sample_klein_app import __version__ as version_string  # noqa


#
# Options
#

name = "sample-klein-app"

description = "Sample Twisted Klein Application"

readme_path = Path(__file__).parent / "README.rst"
try:
    long_description = readme_path.open().read()
except IOError:
    long_description = None

url = "https://github.com/wsanchez/sample-klein-app"

author = "Wilfredo S\xe1nchez Vega"

author_email = "wsanchez@wsanchez.net"

license = ""

platforms = ["all"]

packages = find_packages(where="src")

classifiers = [
    "Framework :: Twisted",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
]


#
# Entry points
#

entry_points = {
    "console_scripts": [],
}

script_entry_points = {
    # "web": ("sample.tool", "Tool.main"),
}

for tool, (module, function) in script_entry_points.items():
    entry_points["console_scripts"].append(
        "{}_{} = {}:{}".format(name, tool, module, function)
    )


#
# Dependencies
#

setup_requirements = []

install_requirements = [
    "Twisted>=16.6.0",
    "klein",
]

extras_requirements = {}


#
# Set up Extension modules that need to be built
#

extensions = []


#
# Run setup
#

def main():
    """
    Run L{setup}.
    """
    setup(
        name=name,
        version=version_string,
        description=description,
        long_description=long_description,
        url=url,
        classifiers=classifiers,
        author=author,
        author_email=author_email,
        license=license,
        platforms=platforms,
        packages=packages,
        package_dir={"": "src"},
        package_data={},
        entry_points=entry_points,
        scripts=[],
        data_files=[],
        ext_modules=extensions,
        py_modules=[],
        setup_requires=setup_requirements,
        install_requires=install_requirements,
        extras_require=extras_requirements,
    )


#
# Main
#

if __name__ == "__main__":
    main()
