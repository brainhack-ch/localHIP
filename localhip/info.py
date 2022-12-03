# Copyright (C) 2022, University of Lausanne (UNIL-CHUV), Switzerland, and LocalHIP contributors
# All rights reserved.
#
#  This software is distributed under the open-source Apache 2 license.
"""This file contains cmp package information."""

_version_major = 0
_version_minor = 0
_version_micro = 1
_version_extra = ""
__release_date__ = "DD.MM.2022"

__minor_version__ = "%s.%s" % (_version_major, _version_minor)

__version__ = "v%s.%s.%s%s" % (
    _version_major,
    _version_minor,
    _version_micro,
    _version_extra,
)

# __current_year__ = datetime.datetime.now().strftime("%Y")
__current_year__ = "2022"

__author__ = "The LocalHIP developers"

__copyright__ = (
    "Copyright (C) 2022"  # -{}, ".format(__current_year__)
    + "the University Hospital Center and University of Lausanne (UNIL-CHUV), Switzerland, "
    + "and Contributors, All rights reserved."
)

__credits__ = (
    "Contributors: please check the ``.zenodo.json`` file at the top-level folder"
    "of the repository"
)
__license__ = "Apache 2.0"
__maintainer__ = "Sebastien Tourbier"
__email__ = "sebastien.tourbier@alumni.epfl.ch"
__status__ = "Prototype"

__packagename__ = "localhip"

__url__ = "https://github.com/brainhack-ch/{name}/tree/{version}".format(
    name=__packagename__, version=__version__
)

DOWNLOAD_URL = "https://github.com/brainhack-ch/{name}/archive/{ver}.tar.gz".format(
    name=__packagename__, ver=__version__
)

DOCKER_HUB = "TO_BE_COMPLETED_ONCE_IT_IS_DEPLOYED"


