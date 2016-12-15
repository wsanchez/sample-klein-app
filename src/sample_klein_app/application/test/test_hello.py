"""
Tests for L{sample_klein_app.application.hello}.
"""

from twisted.trial import unittest

from .mock_render import assertResponse

from sample_klein_app.application.hello import Application


__all__ = (
    "HelloApplicationTests",
)


class HelloApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.hello}.
    """

    def assertResponse(self, *args, **kwargs):
        application = Application()
        return assertResponse(self, application, *args, **kwargs)

    def test_root(self):
        """
        L{Application.root} returns a canned string.
        """
        return self.assertResponse(b"/", response_data=b"Hello!")
