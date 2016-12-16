"""
Hello application
"""

from klein import Klein

from ._main import main


__all__ = (
    "Application",
)


class Application(object):
    router = Klein()

    main = classmethod(main)

    @router.route("/")
    def hello(self, request):
        """
        Application root resource.

        Responds with a message noting the nature of the application.

        @param request: The request to respond to.
        """
        return "Hello!"


if __name__ == "__main__":  # pragma: no cover
    Application.main()
