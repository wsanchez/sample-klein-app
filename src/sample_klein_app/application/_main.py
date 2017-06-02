# -*- test-case-name: sample_klein_app.application.test.test_main -*-
"""
Shared main function.
"""

from typing import Optional, Sequence


def main(applicationClass: type, argv: Optional[Sequence[str]] = None) -> None:
    """
    Executable entry point

    :param applicationClass: A Klein application to run.

    :param argv: Command line arguments.  If :obj:`None`, use :data:`sys.argv`.
    """
    application = applicationClass()
    application.router.run(host="localhost", port=8080)
