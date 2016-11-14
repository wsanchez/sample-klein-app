"""
Composite application
"""

from klein import Klein

from .dns import Application as DNSApplication
from .hello import Application as HelloApplication
from .math import Application as MathApplication


__all__ = ["Application"]


class Application(object):
    app = Klein()

    @app.route("/")
    def root(self, request):
        return "This is a web application composed from multiple applications."

    @app.route("/dns/", branch=True)
    def dns(self, request):
        return DNSApplication().app.resource()

    @app.route("/hello/", branch=True)
    def hello(self, request):
        return HelloApplication().app.resource()

    @app.route("/math/", branch=True)
    def math(self, request):
        return MathApplication().app.resource()


if __name__ == "__main__":
    application = Application()
    application.app.run("localhost", 8080)
