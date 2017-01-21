"""
Tests for L{sample_klein_app.application.composite}.
"""

from twisted.web import http

from . import unittest
from .mock_render import assertResponse

from sample_klein_app.application.composite import Application


__all__ = (
    "CompositeApplicationTests",
)


class CompositeApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.composite}.
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

    def assertChildApplication(self, sub_app, *args, **kwargs) -> None:
        """
        Assert that a child application is bound to a given name as a child
        resource of L{Application}.

        @see L{assertResponse}

        @param sub_app: The name of the child resource the child application is
            expected to be bound to.

        @param args: Positional arguments to pass to L{assertResponse}.
            The C{application} and C{request_path} arguments are added as the
            first argument.

        @param args: Keyword arguments to pass to L{assertResponse}.
        """
        path_short = b"/" + sub_app
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
        L{Application.root} responds with a canned string.
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
        L{Application} responds with the DNS application at C{"/dns"}.
        """
        self.assertChildApplication(b"dns", response_data=b"DNS API.")

    def test_hello(self) -> None:
        """
        L{Application} responds with the Hello application at C{"/hello"}.
        """
        self.assertChildApplication(b"hello", response_data=b"Hello!")

    def test_math(self) -> None:
        """
        L{Application} responds with the Math application at C{"/math"}.
        """
        self.assertChildApplication(
            b"math", response_data=b"Math happens here."
        )
