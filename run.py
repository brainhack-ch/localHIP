# Copyright (C) 2022, University of Lausanne (UNIL-CHUV), Switzerland, and LocalHIP contributors
# All rights reserved.
#
#  This software is distributed under the open-source license Modified BSD.
"""This module defines the `localhip` entrypoint script that is called by the BIDS App."""

# General imports
import sys
import warnings

# LocalHIP imports
from localhip.info import __version__, __copyright__
from localhip.parser import create_parser
from localhip.project import run_individual


# Filter warning
warnings.filterwarnings(
    "ignore",
    message="""UserWarning: No valid root directory found for domain 'derivatives'.
            Falling back on the Layout's root directory. If this isn't the intended behavior,
            make sure the config file for this domain includes a 'root' key.""",
)


def info():
    """Print version of copyright."""
    print(f"\nLocalHIP pipeline {__version__}")
    print(f"{__copyright__}\n")


def main():
    """Main function that runs the localhip python script.
    Returns
    -------
    exit_code : {0, 1}
        An exit code given to `sys.exit()` that can be:
            * '0' in case of successful completion
            * '1' in case of an error
    """
    # Parse script arguments
    parser = create_parser()
    args = parser.parse_args()

    # Version and copyright message
    info()

    return run_individual(
        bids_dir=args.bids_dir,
        output_dir=args.output_dir,
        participant_label=args.participant_label,
        session_label=args.session_label,
    )


if __name__ == "__main__":
    sys.exit(main())
