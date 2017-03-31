# -*- test-case-name: sample_klein_app.application.test.test_hello -*-
"""
Hello application
"""

from typing import Optional, Sequence

from twisted.web.iweb import IRequest

from ._main import main
from ..ext.klein import Klein, KleinRenderable


__all__ = (
    "Application",
)



class Application(object):
    """
    Hello application.

    Application says hello.
    """

    router = Klein()


    @classmethod
    def main(cls, argv: Optional[Sequence[str]] = None) -> None:
        """
        Main entry point.
        """
        main(cls, argv)


    @router.route("/")
    def hello(self, request: IRequest) -> KleinRenderable:
        """
        Application root resource.

        Responds with a message noting the nature of the application.

        :param request: The request to respond to.
        """
        return "Hello!"



if __name__ == "__main__":  # pragma: no cover
    Application.main()
