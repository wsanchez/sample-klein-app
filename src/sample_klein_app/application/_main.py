"""
Shared main function.
"""

import sys
from typing import Sequence


def main(applicationClass, argv: Sequence[str] = sys.argv) -> None:
    """
    Executable entry point

    @param applicationClass: A Klein application to run.

    @param argv: Command line arguments.
    """
    application = applicationClass()
    application.router.run("localhost", 8080)
