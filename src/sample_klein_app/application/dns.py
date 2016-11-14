"""
DNS application
"""

from twisted.internet.defer import inlineCallbacks
from twisted.internet.error import DNSLookupError
from twisted.web import http
from twisted.names.client import getHostByName
from twisted.names.error import DNSNameError
from klein import Klein


__all__ = ["Application"]


class Application(object):
    router = Klein()

    @router.route("/")
    def root(self, request):
        return "DNS API."

    @router.route("/gethostbyname/<name>")
    @inlineCallbacks
    def hostname(self, request, name):
        try:
            address = yield getHostByName(name)
        except DNSNameError:
            request.setResponseCode(http.NOT_FOUND)
            return "no such host"
        except DNSLookupError:
            request.setResponseCode(http.NOT_FOUND)
            return "lookup error"

        return address


if __name__ == "__main__":
    application = Application()
    application.router.run("localhost", 8080)
