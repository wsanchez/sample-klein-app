"""
Composite application
"""

from klein import Klein

from .dns import Application as DNSApplication
from .hello import Application as HelloApplication
from .math import Application as MathApplication


__all__ = ["Application"]


class Application(object):
    router = Klein()

    @router.route("/")
    def root(self, request):
        return "This is a web application composed from multiple applications."

    @router.route("/dns/", branch=True)
    def dns(self, request):
        return DNSApplication().router.resource()

    @router.route("/hello/", branch=True)
    def hello(self, request):
        return HelloApplication().router.resource()

    @router.route("/math/", branch=True)
    def math(self, request):
        return MathApplication().router.resource()


if __name__ == "__main__":  # pragma: no cover
    application = Application()
    application.router.run("localhost", 8080)
