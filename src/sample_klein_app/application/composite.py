# -*- test-case-name: sample_klein_app.application.test.test_composite -*-
"""
Composite application
"""

from typing import Optional, Sequence

from twisted.web.iweb import IRequest

from ._main import main
from .dns import Application as DNSApplication
from .hello import Application as HelloApplication
from .math import Application as MathApplication
from ..ext.klein import Klein, KleinRenderable


__all__ = (
    "Application",
)



class Application(object):
    """
    Composite application.

    Application that exposes endpoints that are handled by other applications,
    thereby composing multiple applications into a single application.
    """

    router = Klein()


    @classmethod
    def main(cls, argv: Optional[Sequence[str]] = None) -> None:
        """
        Main entry point.
        """
        main(cls, argv)


    @router.route("/")
    def root(self, request: IRequest) -> KleinRenderable:
        """
        Application root resource.

        Responds with a message noting the nature of the application.

        :param request: The request to respond to.
        """
        return "This is a web application composed from multiple applications."


    @router.route("/dns/", branch=True)
    def dns(self, request: IRequest) -> KleinRenderable:
        """
        DNS application resource.

        Routes requests to :class:`.dns.Application`.

        :param request: The request to respond to.
        """
        return DNSApplication().router.resource()


    @router.route("/hello/", branch=True)
    def hello(self, request: IRequest) -> KleinRenderable:
        """
        Hello application resource.

        Routes requests to :class:`.hello.Application`.

        :param request: The request to respond to.
        """
        return HelloApplication().router.resource()


    @router.route("/math/", branch=True)
    def math(self, request: IRequest) -> KleinRenderable:
        """
        Math application resource.

        Routes requests to :class:`.math.Application`.

        :param request: The request to respond to.
        """
        return MathApplication().router.resource()



if __name__ == "__main__":  # pragma: no cover
    Application.main()
