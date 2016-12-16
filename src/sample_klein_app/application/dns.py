"""
DNS application
"""

from functools import wraps

from twisted.internet.defer import ensureDeferred
from twisted.internet.error import DNSLookupError
from twisted.web import http
from twisted.names.client import getHostByName
from twisted.names.error import DNSNameError

from klein import Klein

from ._main import main


__all__ = (
    "Application",
)


# Ideally, we want Klein to handle coroutines natively, so we won't need this
# decorator.
def twisted_async(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        return ensureDeferred(result)
    return wrapper


class Application(object):
    """
    DNS application.

    Application that performs DNS queries.
    """

    router = Klein()

    main = classmethod(main)

    @router.route("/")
    def root(self, request):
        """
        Application root resource.

        Responds with a message noting the nature of the application.

        @param request: The request to respond to.
        """
        return "DNS API."

    @router.route("/gethostbyname/<name>")
    @twisted_async
    async def hostname(self, request, name):
        """
        Hostname lookup resource.

        Performs a lookup on the given name and responds with the resulting
        address.

        @param request: The request to respond to.

        @param name: A host name.
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
