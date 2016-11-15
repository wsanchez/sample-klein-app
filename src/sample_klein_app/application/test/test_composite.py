"""
Tests for L{sample_klein_app.application.composite}.
"""

from twisted.trial import unittest

from .mock_render import assertResponse

from sample_klein_app.application.composite import Application


__all__ = ["CompositeApplicationTests"]


class CompositeApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.composite}.
    """

    def assertResponse(self, *args, **kwargs):
        application = Application()
        return assertResponse(self, application, *args, **kwargs)

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
        return self.assertResponse(b"/dns/", response_data=b"DNS API.")

    def test_hello(self):
        return self.assertResponse(b"/hello/", response_data=b"Hello!")

    def test_math(self):
        return self.assertResponse(
            b"/math/", response_data=b"Math happens here.",
        )
