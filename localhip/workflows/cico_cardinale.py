# Copyright (C) 2022, University of Lausanne (UNIL-CHUV), Switzerland, and LocalHIP contributors
# All rights reserved.
#
#  This software is distributed under the open-source license Modified BSD.
"""This module defines the core of localhip to run individual workflows."""

import os
from nipype.pipeline.engine.workflows import Workflow
from nipype import __version__ as nipype_version


def create_cico_wf(bids_dir, output_dir, participant_label, session_label=None):
    """Function to create the Cico Cardinale workflow.

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
    wf : Workflow
        Nipype workflow
    """

    base_dir = os.path.join(bids_dir, 'derivatives', f'nipype-{nipype_version}', f'sub-{participant_label}')
    if session_label is not None:
        base_dir = os.path.join(base_dir, f'ses-{session_label}')

    print(f' * Setup workflow (basedir: {base_dir})')
    wf = Workflow(name="cico_cardinale_wf", base_dir=base_dir)

    return wf
