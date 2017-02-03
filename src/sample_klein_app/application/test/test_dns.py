"""
Tests for :mod:`sample_klein_app.application.dns`.
"""

from twisted.internet.defer import Deferred, fail, succeed
from twisted.internet.error import DNSLookupError
from twisted.names.error import DNSNameError
from twisted.web import http

from . import unittest
from .mock_render import assertResponse
from .. import dns
from ..dns import Application


__all__ = (
    "DNSApplicationTests",
)


class DNSApplicationTests(unittest.TestCase):
    """
    Tests for :mod:`sample_klein_app.application.dns`.
    """

    def assertResponse(self, *args, **kwargs) -> None:
        """
        Generate and process a request using the an instance of
        :class:`.dns.Application` and assert that the response is as expected.

        See :meth:`assertResponse`.

        :param args: Positional arguments to pass to :meth:`assertResponse`.
            The ``application`` argument is added as the first argument.

        :param args: Keyword arguments to pass to :meth:`assertResponse`.
        """
        self.successResultOf(
            assertResponse(self, Application(), *args, **kwargs)
        )

    def test_root(self) -> None:
        """
        :meth:`.dns.Application.root` returns a canned string.
        """
        self.assertResponse(b"/", response_data=b"DNS API.")

    def test_hostname_found(self) -> None:
        """
        :meth:`.dns.Application.hostname` looks up the given name and provides
        an IP address.
        """
        def getHostByName(*args, **kwargs) -> Deferred:
            return succeed("10.10.30.40")

        self.patch(dns, "getHostByName", getHostByName)

        self.assertResponse(
            b"/gethostbyname/foo.example.com", response_data=b"10.10.30.40",
        )

    def test_hostname_not_found(self) -> None:
        """
        :meth:`.dns.Application.hostname` responds with a
        :const:`twisted.web.http.NOT_FOUND` error if the host is not found in
        DNS.
        """
        def getHostByName(*args, **kwargs) -> Deferred:
            return fail(DNSNameError())

        self.patch(dns, "getHostByName", getHostByName)

        self.assertResponse(
            b"/gethostbyname/foo.example.com",
            response_data=b"no such host",
            response_code=http.NOT_FOUND,
        )

    def test_hostname_lookup_error(self) -> None:
        """
        :meth:`.dns.Application.hostname` responds with a
        :const:`twisted.web.http.NOT_FOUND` error if there is a DNS lookup
        error.
        """
        def getHostByName(*args, **kwargs) -> Deferred:
            return fail(DNSLookupError())

        self.patch(dns, "getHostByName", getHostByName)

        self.assertResponse(
            b"/gethostbyname/foo.example.com",
            response_data=b"lookup error",
            response_code=http.NOT_FOUND,
        )
