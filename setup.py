#!/usr/bin/env python

"""`Setup.py` for LocalHIP."""

import os
import sys
import setuptools
from setuptools.command.install import install

from localhip.info import __version__


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""

    description = "verify that the git tag matches our version"

    def run(self):
        """Verify that the git tag (`CIRCLE_TAG`) matches our version."""
        tag = os.getenv('CIRCLE_TAG')
        version = f'{__version__}'
        if tag != version:
            info = f"Git tag: {tag} does not match the version of this app: {version}"
            sys.exit(info)


# Get directory where this file is located
directory = os.path.abspath(os.path.dirname(__file__))

# Remove any MANIFEST of a previous installation
if os.path.exists("MANIFEST"):
    os.remove("MANIFEST")

# Define the packages to be installed
packages = [
    "localhip",
    "localhip.cli",
    "localhip.interfaces",
    "localhip.workflows"
]

# Define the package data to be installed
package_data = {}


# Read the contents of your README file
with open(os.path.join(directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


def main():
    """Main function of CMP3 ``setup.py``"""
    # Setup configuration
    setuptools.setup(
        name="localhip",
        version=__version__,
        description="LocalHIP: Automated for electrode localization in iEEG in the BIDS ecosystem",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Sebastien Tourbier",
        author_email="sebastien.tourbier@alumni.epfl.ch",
        url="https://github.com/brainhack-ch/localHIP",
        entry_points={
            "console_scripts": [
                'localhip = localhip.cli.localhip:main',
            ]
        },
        license="BSD-3-Clause",
        classifiers=[
            "Development Status :: 1 - Planning",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Developers",
            "License :: OSI Approved",
            "Programming Language :: Python",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Operating System :: MacOS",
            "Programming Language :: Python :: 3.7",
        ],
        maintainer="Sebastien Tourbier",
        maintainer_email="sebastien.tourbier@alumni.epfl.ch",
        packages=packages,
        include_package_data=True,
        package_data=package_data,
        requires=["nipype (>=1.8.4)", "pybids (>=0.15.5)"],
        python_requires=">=3.7",
        cmdclass={
            "verify": VerifyVersionCommand,
        },
    )


if __name__ == "__main__":
    main()
