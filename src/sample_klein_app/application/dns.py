# -*- test-case-name: sample_klein_app.application.test.test_dns -*-
"""
DNS application
"""

from typing import Optional, Sequence

from twisted.internet.error import DNSLookupError
from twisted.names.client import getHostByName
from twisted.names.error import DNSNameError
from twisted.web import http
from twisted.web.iweb import IRequest

from ._main import main
from ..ext.klein import Klein, KleinRenderable


__all__ = (
    "Application",
)



class Application(object):
    """
    DNS application.

    Application that performs DNS queries.
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
        return "DNS API."


    @router.route("/gethostbyname/<name>")
    async def hostname(self, request: IRequest, name: str) -> KleinRenderable:
        """
        Hostname lookup resource.

        Performs a lookup on the given name and responds with the resulting
        address.

        :param request: The request to respond to.

        :param name: A host name.
        """
        try:
            address = await getHostByName(name)
        except DNSNameError:
            request.setResponseCode(http.NOT_FOUND)
            return "no such host"
        except DNSLookupError:
            request.setResponseCode(http.NOT_FOUND)
            return "lookup error"

        return address



if __name__ == "__main__":  # pragma: no cover
    Application.main()
