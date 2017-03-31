"""
Tests for :mod:`sample_klein_app.application.hello`.
"""

from .mock_render import assertResponse
from ..hello import Application
from ...ext.trial import TestCase


__all__ = (
    "HelloApplicationTests",
)


class HelloApplicationTests(TestCase):
    """
    Tests for :mod:`sample_klein_app.application.hello`.
    """

    def assertResponse(self, *args, **kwargs) -> None:
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
