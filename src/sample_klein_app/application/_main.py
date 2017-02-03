"""
Shared main function.
"""

import sys
from typing import Sequence


def main(applicationClass, argv: Sequence[str] = None) -> None:
    """
    Executable entry point

    :param applicationClass: A Klein application to run.

    :param argv: Command line arguments.  If :obj:`None`, use :data:`sys.argv`.
    """
    if argv is None:
        argv = sys.argv

    application = applicationClass()
    application.router.run("localhost", 8080)
