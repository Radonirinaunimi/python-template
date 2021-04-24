"""
This file contains the current state of packaging in Python using
Distribution Utilities (Distutils) and its extension from the end
user'point-of-view.

Documentation:
https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/introduction.html
"""

import pathlib
from setuptools import setup
from setuptools import find_packages

PACKAGE = "<package_name>"
THIS_DIR = pathlib.Path(__file__).parent
LONG_DESCRIPTION = (THIS_DIR / "README.md").read_text()
REQUIREMENTS = (THIS_DIR / "requirements.txt").read_text()


setup(
    name=PACKAGE,
    version='0.1.0-dev',
    description="<brief description here>",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="<list of authors>",
    author_email="<correspondence email>",
    license="MIT",
    url="<project url>",
    zip_safe=False,
    project_urls={
        "Source": "<github_address>",
        "Documentation": "<documentation_page>"
    },
    entry_points={
        "console_scripts": [
            "<package_name> = <package_name>.run:main"
        ]
    },
    package_dir={"": "src"},
    packages=find_packages("src"),
    install_requires=REQUIREMENTS,
    classifiers=[
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: <topic>/<subtopic>"
    ],
    setup_requires=["wheel"],
    python_requires='>=3.7'
)
