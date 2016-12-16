"""
Tests for L{sample_klein_app.application.math}.
"""

from twisted.web import http
from twisted.trial import unittest

from .mock_render import assertResponse

from sample_klein_app.application.math import Application


__all__ = (
    "MathApplicationTests",
)


class MathApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.math}.
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

    def test_root(self):
        """
        L{Application.root} returns a canned string.
        """
        return self.assertResponse(b"/", response_data=b"Math happens here.")

    def test_add(self):
        """
        L{Application.add} sums C{a} and C{b}.
        """
        return self.assertResponse(b"/add/1/3", response_data=b"4")

    def test_subtract(self):
        """
        L{Application.subtract} subtracts C{b} from C{a}.
        """
        return self.assertResponse(b"/subtract/4/1", response_data=b"3")

    def test_multiply(self):
        """
        L{Application.multiply} multiplies C{a} and C{b}.
        """
        return self.assertResponse(b"/multiply/2/3", response_data=b"6")

    def test_divide(self):
        """
        L{Application.divide} divides C{a} by C{b}.
        """
        return self.assertResponse(b"/divide/12/3", response_data=b"4.0")

    def test_invalid_input(self):
        """
        Invalid inputs result in an error.
        """
        return self.assertResponse(
            b"/divide/fish/carrots",
            response_data=b"Invalid inputs provided.",
            response_code=http.BAD_REQUEST,
        )
