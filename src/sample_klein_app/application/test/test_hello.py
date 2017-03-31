"""
Tests for :mod:`sample_klein_app.application.hello`.
"""

from typing import Any, List

from .mock_render import assertResponse
from .. import hello
from ..hello import Application
from ...ext.trial import TestCase


__all__ = (
    "HelloApplicationTests",
)


List  # pyflakes


class HelloApplicationTests(TestCase):
    """
    Tests for :mod:`sample_klein_app.application.hello`.
    """

    def test_main(self) -> None:
        """
        :meth:`Application.main` wraps :func:`.._main.main`.
        """
        argsSeen = []  # type: List[Any]

        def main(*args: Any) -> None:
            assert len(argsSeen) == 0
            argsSeen.extend(args)

        self.patch(hello, "main", main)

        argv = []  # type: List[Any]
        Application.main(argv)

        self.assertEqual(len(argsSeen), 2)
        self.assertIdentical(argsSeen[0], Application)
        self.assertIdentical(argsSeen[1], argv)


    def assertResponse(self, *args: Any, **kwargs: Any) -> None:
        """
        Generate and process a request using the an instance of
        :class:`.hello.Application` and assert that the response is as
        expected.

        See :meth:`assertResponse`.

        :param args: Positional arguments to pass to :meth:`assertResponse`.
            The ``application`` argument is added as the first argument.

        :param args: Keyword arguments to pass to :meth:`assertResponse`.
        """
        self.successResultOf(
            assertResponse(self, Application(), *args, **kwargs)
        )


    def test_hello(self) -> None:
        """
        :meth:`.hello.Application.hello` returns a canned string.
        """
        self.assertResponse(b"/", response_data=b"Hello!")
