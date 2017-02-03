"""
Hello application
"""

from twisted.web.iweb import IRequest

from ._main import main
from .klein import Klein, KleinRenderable


__all__ = (
    "Application",
)


class Application(object):
    """
    Hello application.

    Application says hello.
    """

    router = Klein()

    main = classmethod(main)  # type: ignore

    @router.route("/")
    def hello(self, request: IRequest) -> KleinRenderable:
        """
        Application root resource.

        Responds with a message noting the nature of the application.

        :param request: The request to respond to.
        """
        return "Hello!"


if __name__ == "__main__":  # pragma: no cover
    Application.main()  # type: ignore
