"""
Shared main function.
"""

import sys


def main(applicationClass, argv=sys.argv):
    """
    Executable entry point

    @param applicationClass: A Klein application to run.

    @param argv: Command line arguments.
    """
    application = applicationClass()
    application.router.run("localhost", 8080)
