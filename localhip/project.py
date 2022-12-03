# Copyright (C) 2022, University of Lausanne (UNIL-CHUV), Switzerland, and LocalHIP contributors
# All rights reserved.
#
#  This software is distributed under the open-source license Modified BSD.
"""This module defines the core of localhip to run individual workflows."""

from localhip.workflows import create_cico_wf


def run_individual(bids_dir, output_dir, participant_label, session_label=None):
    """Run a localization workflow at the participant level.

    Parameters
    ----------
    bids_dir: str
        Base directory of the BIDS dataset

    output_dir: str
        Output directory for workflow derivatives

    participant_label: str
        Label of the participant (e.g "01" for "sub-01")

    session_label: str
        Label of the session (e.g "preop" for "ses-preop")

    Returns
    -------
    exit_code: int
        Exit code (0: success / 1: failure)
    """
    # Initialize exit_code
    exit_code = 0

    # Create Cico Cardinale workflow
    wf = create_cico_wf(bids_dir, output_dir, participant_label, session_label)

    # Write the graph of the workflow as a SVG image
    wf.write_graph(graph2use="colored", format="svg", simple_form=True)

    # Create dictionary of arguments passed to plugin_args
    plugin_args = {
        'maxtasksperchild': 1,
        'raise_insufficient': False,
    }

    # Run the workflow
    res = wf.run(plugin="MultiProc", plugin_args=plugin_args)
    print(res)

    return exit_code
