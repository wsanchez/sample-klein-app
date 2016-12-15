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
        return "Hello!"


if __name__ == "__main__":  # pragma: no cover
    Application.main()
