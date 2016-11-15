"""
Tests for L{sample_klein_app.application.math}.
"""

from twisted.internet.defer import succeed, inlineCallbacks
from twisted.web.server import NOT_DONE_YET
from twisted.trial import unittest

from klein.test.test_resource import requestMock

from sample_klein_app.application.math import Application


__all__ = []


class MathApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.math}.
    """

    def test_numberify_integer(self):
        """
        L{Application.numberify} converts a string integer into an L{int}.
        """
        for integer_value in (-1, 0, 1):
            string_value = "{}".format(integer_value)
            result_value = Application.numberify(string_value)

            self.assertEqual(result_value, integer_value)
            self.assertEqual(type(result_value), int)

    def test_numberify_float(self):
        """
        L{Application.numberify} converts a string floating-point number into a
        L{float}.
        """
        for float_value in (-1.0, 0.0, 1.0):
            string_value = "{}".format(float_value)
            result_value = Application.numberify(string_value)

            self.assertEqual(result_value, float_value)
            self.assertEqual(type(result_value), float)

    @inlineCallbacks
    def test_root(self):
        """
        L{Application.root} returns a canned string.
        """
        app = Application()
        request = requestMock(b"/")
        yield render(app.router, request)

        self.assertEqual(request.getWrittenData(), b"Math happens here.")

    @inlineCallbacks
    def test_add(self):
        """
        L{Application.add} sums C{a} and C{b}.
        """
        app = Application()
        request = requestMock(b"/add/1/3")
        yield render(app.router, request)

        self.assertEqual(request.getWrittenData(), b"4")

    @inlineCallbacks
    def test_subtract(self):
        """
        L{Application.subtract} subtracts C{b} from C{a}.
        """
        app = Application()
        request = requestMock(b"/subtract/4/1")
        yield render(app.router, request)

        self.assertEqual(request.getWrittenData(), b"3")

    @inlineCallbacks
    def test_multiply(self):
        """
        L{Application.multiply} multiplies C{a} and C{b}.
        """
        app = Application()
        request = requestMock(b"/multiply/2/3")
        yield render(app.router, request)

        self.assertEqual(request.getWrittenData(), b"6")

    @inlineCallbacks
    def test_divide(self):
        """
        L{Application.divide} divides C{a} by C{b}.
        """
        app = Application()
        request = requestMock(b"/divide/12/3")
        yield render(app.router, request)

        self.assertEqual(request.getWrittenData(), b"4.0")

    @inlineCallbacks
    def test_invalid_input(self):
        """
        Invalid inputs result in an error.
        """
        app = Application()
        request = requestMock(b"/divide/fish/carrots")
        yield render(app.router, request)

        self.assertEqual(request.getWrittenData(), b"Invalid inputs provided.")


def render(router, request, notifyFinish=True):
    result = router.resource().render(request)

    if isinstance(result, bytes):
        request.write(result)
        request.finish()
        return succeed(None)
    elif result is NOT_DONE_YET:
        if request.finished or not notifyFinish:
            return succeed(None)
        else:
            return request.notifyFinish()
    else:
        raise ValueError("Unexpected return value: %r" % (result,))
