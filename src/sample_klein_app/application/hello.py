"""
Hello application
"""

from klein import Klein


__all__ = ["Application"]


class Application(object):
    router = Klein()

    @router.route("/")
    def hello(self, request):
        return "Hello!"


if __name__ == "__main__":  # pragma: no cover
    application = Application()
    application.router.run("localhost", 8080)
