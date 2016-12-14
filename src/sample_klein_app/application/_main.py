"""
Shared main function.
"""

import sys


def main(applicationClass, argv=sys.argv):
    application = applicationClass()
    application.router.run("localhost", 8080)
