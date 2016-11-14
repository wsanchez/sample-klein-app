"""
Tests for L{sample_klein_app.application.math}.
"""

from twisted.trial import unittest

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

    def test_root(self):
        """
        L{Application.root} returns a canned string.
        """
        application = Application()
        result = application.root(None)
        self.assertEqual(result, "Math happens here.")

    def test_add(self):
        """
        L{Application.add} sums C{a} and C{b}.
        """
        application = Application()
        result = application.add(None, "1", "3")
        self.assertEqual(result, "4")

    def test_subtract(self):
        """
        L{Application.subtract} subtracts C{b} from C{a}.
        """
        application = Application()
        result = application.subtract(None, "4", "1")
        self.assertEqual(result, "3")

    def test_multiply(self):
        """
        L{Application.multiply} multiplies C{a} and C{b}.
        """
        application = Application()
        result = application.multiply(None, "2", "3")
        self.assertEqual(result, "6")

    def test_divide(self):
        """
        L{Application.divide} divides C{a} by C{b}.
        """
        application = Application()
        result = application.divide(None, "12", "3")
        self.assertEqual(result, "4.0")
