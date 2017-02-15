"""
Shared main function.
"""

from typing import Sequence


def main(applicationClass, argv: Sequence[str] = None) -> None:
    """
    Executable entry point

    :param applicationClass: A Klein application to run.

    :param argv: Command line arguments.  If :obj:`None`, use :data:`sys.argv`.
    """
    application = applicationClass()
    application.router.run(host="localhost", port=8080)
