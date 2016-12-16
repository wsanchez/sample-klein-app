"""
Tests for L{sample_klein_app.application.composite}.
"""

from twisted.internet.defer import inlineCallbacks
from twisted.web import http
from twisted.trial import unittest

from .mock_render import assertResponse

from sample_klein_app.application.composite import Application


__all__ = (
    "CompositeApplicationTests",
)


class CompositeApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.composite}.
    """

    def assertResponse(self, *args, **kwargs):
        """
        Generate and process a request using the an instance of L{Application}
        and assert that the response is as expected.

        @see L{assertResponse}

        @param args: Positional arguments to pass to L{assertResponse}.
            The C{application} argument is added as the first argument.

        @param args: Keyword arguments to pass to L{assertResponse}.
        """
        application = Application()
        return assertResponse(self, application, *args, **kwargs)

    @inlineCallbacks
    def assertChildApplication(self, sub_app, *args, **kwargs):
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

        yield self.assertResponse(
            path_short,
            response_code=http.MOVED_PERMANENTLY,
            response_location_path=path_full,
        )

        yield self.assertResponse(path_full, *args, **kwargs)

    def test_root(self):
        """
        L{Application.root} responds with a canned string.
        """
        return self.assertResponse(
            b"/",
            response_data=(
                b"This is a web application composed from multiple "
                b"applications."
            )
        )

    def test_dns(self):
        """
        L{Application} responds with the DNS application at C{"/dns"}.
        """
        return self.assertSubApplication(b"dns", response_data=b"DNS API.")

    def test_hello(self):
        """
        L{Application} responds with the Hello application at C{"/hello"}.
        """
        return self.assertSubApplication(b"hello", response_data=b"Hello!")

    def test_math(self):
        """
        L{Application} responds with the Math application at C{"/math"}.
        """
        return self.assertSubApplication(
            b"math", response_data=b"Math happens here."
        )
