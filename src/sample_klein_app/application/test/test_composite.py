"""
Tests for :mod:`sample_klein_app.application.composite`.
"""

from typing import Any, List

from twisted.web import http

from .mock_render import assertResponse
from .. import composite
from ..composite import Application
from ...ext.trial import TestCase


__all__ = (
    "CompositeApplicationTests",
)


List  # pyflakes



class CompositeApplicationTests(TestCase):
    """
    Tests for :mod:`sample_klein_app.application.composite`.
    """

    def test_main(self) -> None:
        """
        :meth:`Application.main` wraps :func:`.._main.main`.
        """
        argsSeen = []  # type: List[Any]

        def main(*args: Any) -> None:
            assert len(argsSeen) == 0
            argsSeen.extend(args)

        self.patch(composite, "main", main)

        argv = []  # type: List[Any]
        Application.main(argv)

        self.assertEqual(len(argsSeen), 2)
        self.assertIdentical(argsSeen[0], Application)
        self.assertIdentical(argsSeen[1], argv)


    def assertResponse(self, *args: Any, **kwargs: Any) -> None:
        """
        Generate and process a request using the an instance of
        :class:`.composite.Application` and assert that the response is as
        expected.

        See :meth:`assertResponse`.

        :param args: Positional arguments to pass to :meth:`assertResponse`.
            The ``application`` argument is added as the first argument.

        :param args: Keyword arguments to pass to :meth:`assertResponse`.
        """
        self.successResultOf(
            assertResponse(self, Application(), *args, **kwargs)
        )


    def assertChildApplication(
        self, childName: bytes, *args: Any, **kwargs: Any
    ) -> None:
        """
        Assert that a child application is bound to a given name as a child
        resource of :class:`.composite.Application`.

        See :meth:`assertResponse`.

        :param childName: The name of the child resource the child application
            is expected to be bound to.

        :param args: Positional arguments to pass to :meth:`assertResponse`.
            The ``application`` and ``request_path`` arguments are added as the
            first argument.

        :param args: Keyword arguments to pass to :meth:`assertResponse`.
        """
        path_short = b"/" + childName
        path_full = path_short + b"/"

        # Without the trailing "/", we expect a redirect
        self.assertResponse(
            path_short,
            response_code=http.MOVED_PERMANENTLY,
            response_location_path=path_full,
        )

        # With the trailing "/", we expect a regular response
        self.assertResponse(path_full, *args, **kwargs)


    def test_root(self) -> None:
        """
        :meth:`.composite.Application.root` responds with a canned string.
        """
        self.assertResponse(
            b"/",
            response_data=(
                b"This is a web application composed from multiple "
                b"applications."
            )
        )


    def test_dns(self) -> None:
        """
        :class:`.composite.Application` responds with the DNS application at
        ``/dns``.
        """
        self.assertChildApplication(b"dns", response_data=b"DNS API.")


    def test_hello(self) -> None:
        """
        :class:`.composite.Application` responds with the Hello application at
        ``/hello``.
        """
        self.assertChildApplication(b"hello", response_data=b"Hello!")


    def test_math(self) -> None:
        """
        :class:`.composite.Application` responds with the Math application at
        ``/math``.
        """
        self.assertChildApplication(
            b"math", response_data=b"Math happens here."
        )
