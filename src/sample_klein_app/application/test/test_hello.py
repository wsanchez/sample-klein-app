"""
Tests for L{sample_klein_app.application.hello}.
"""

from . import unittest
from .mock_render import assertResponse

from sample_klein_app.application.hello import Application


__all__ = (
    "HelloApplicationTests",
)


class HelloApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.hello}.
    """

    def assertResponse(self, *args, **kwargs) -> None:
        """
        Generate and process a request using the an instance of L{Application}
        and assert that the response is as expected.

        @see L{assertResponse}

        @param args: Positional arguments to pass to L{assertResponse}.
            The C{application} argument is added as the first argument.

        @param args: Keyword arguments to pass to L{assertResponse}.
        """
        self.successResultOf(
            assertResponse(self, Application(), *args, **kwargs)
        )

    def test_root(self) -> None:
        """
        L{Application.root} returns a canned string.
        """
        self.assertResponse(b"/", response_data=b"Hello!")
