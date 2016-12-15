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
        application = Application()
        return assertResponse(self, application, *args, **kwargs)

    @inlineCallbacks
    def assertSubApplication(self, sub_app, *args, **kwargs):
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
        L{Application.root} returns a canned string.
        """
        return self.assertResponse(
            b"/",
            response_data=(
                b"This is a web application composed from multiple "
                b"applications."
            )
        )

    def test_dns(self):
        return self.assertSubApplication(b"dns", response_data=b"DNS API.")

    def test_hello(self):
        return self.assertSubApplication(b"hello", response_data=b"Hello!")

    def test_math(self):
        return self.assertSubApplication(
            b"math", response_data=b"Math happens here."
        )
