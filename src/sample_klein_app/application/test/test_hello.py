"""
Tests for L{sample_klein_app.application.hello}.
"""

from twisted.internet.defer import inlineCallbacks
from twisted.trial import unittest

from .mock_render import mock_request, render

from sample_klein_app.application.hello import Application


__all__ = []


class HelloApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.hello}.
    """

    @inlineCallbacks
    def test_root(self):
        """
        L{Application.root} returns a canned string.
        """
        app = Application()
        request = mock_request(b"/")
        yield render(app, request)

        self.assertEqual(request.getWrittenData(), b"Hello!")
