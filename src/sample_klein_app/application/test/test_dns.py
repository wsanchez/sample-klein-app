"""
Tests for L{sample_klein_app.application.dns}.
"""

from twisted.internet.defer import succeed, fail
from twisted.internet.error import DNSLookupError
from twisted.web import http
from twisted.names.error import DNSNameError
from twisted.trial import unittest

from ...application import dns
from .async import defer_async
from .mock_render import assertResponse

from sample_klein_app.application.dns import Application


__all__ = (
    "DNSApplicationTests",
)


class DNSApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.dns}.
    """

    async def assertResponse(self, *args, **kwargs):
        """
        Generate and process a request using the an instance of L{Application}
        and assert that the response is as expected.

        @see L{assertResponse}

        @param args: Positional arguments to pass to L{assertResponse}.
            The C{application} argument is added as the first argument.

        @param args: Keyword arguments to pass to L{assertResponse}.
        """
        application = Application()
        await assertResponse(self, application, *args, **kwargs)

    @defer_async
    async def test_root(self) -> None:
        """
        L{Application.root} returns a canned string.
        """
        await self.assertResponse(b"/", response_data=b"DNS API.")

    @defer_async
    async def test_hostname_found(self) -> None:
        """
        L{Application.hostname} looks up the given name and provides an IP
        address.
        """
        def getHostByName(*args, **kwargs):
            return succeed("10.10.30.40")

        self.patch(dns, "getHostByName", getHostByName)

        await self.assertResponse(
            b"/gethostbyname/foo.example.com", response_data=b"10.10.30.40",
        )

    @defer_async
    async def test_hostname_not_found(self) -> None:
        """
        L{Application.hostname} responds with a L{http.NOT_FOUND} error if the
        host is not found in DNS.
        """
        def getHostByName(*args, **kwargs):
            return fail(DNSNameError())

        self.patch(dns, "getHostByName", getHostByName)

        await self.assertResponse(
            b"/gethostbyname/foo.example.com",
            response_data=b"no such host",
            response_code=http.NOT_FOUND,
        )

    @defer_async
    async def test_hostname_lookup_error(self) -> None:
        """
        L{Application.hostname} responds with a L{http.NOT_FOUND} error if
        there is a DNS lookup error.
        """
        def getHostByName(*args, **kwargs):
            return fail(DNSLookupError())

        self.patch(dns, "getHostByName", getHostByName)

        await self.assertResponse(
            b"/gethostbyname/foo.example.com",
            response_data=b"lookup error",
            response_code=http.NOT_FOUND,
        )
