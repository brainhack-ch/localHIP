# Copyright (C) 2022, University of Lausanne (UNIL-CHUV), Switzerland, and LocalHIP contributors
# All rights reserved.
#
#  This software is distributed under the open-source Apache 2 license.
"""This module provides a function to create the BIDS App parser of LocalHIP."""

import argparse
from localhip.info import __version__


def create_parser():
    """Create the parser of localhip python script.
    Returns
    -------
    p : argparse.ArgumentParser
        Parser
    """
    p = argparse.ArgumentParser(description="LocalHIP pipeline main script.")

    p.add_argument(
        "--bids_dir",
        required=True,
        help="The directory with the input dataset " "formatted according to the BIDS standard.",
    )

    p.add_argument(
        "--output_dir",
        required=True,
        help="The directory where the output files "
        "should be stored. If you are running group level analysis "
        "this folder should be prepopulated with the results of the "
        "participant level analysis.",
    )
    p.add_argument(
        "analysis_level",
        help="Level of the analysis that will be performed.",
        choices=["participant"],  # "group"],
    )

    p.add_argument(
        "--participant_label",
        required=True,
        help="The label of the participant"
        "that should be analyzed. The label corresponds to"
        "<participant_label> from the BIDS spec "
        '(so it DOES include "sub-"',
    )

    p.add_argument(
        "--session_label",
        help="The label of the participant session "
        "that should be analyzed. The label corresponds to "
        "<session_label> from the BIDS spec "
        '(so it DOES include "ses-"',
    )

    p.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"LocalHIP pipeline version {__version__}",
    )

    return p
