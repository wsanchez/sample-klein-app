"""
Tests for L{sample_klein_app.application.math}.
"""

from math import isnan

from hypothesis import assume, given
from hypothesis.strategies import floats, integers

from twisted.web import http

from . import unittest
from .mock_render import assertResponse
from ..math import Application


__all__ = (
    "MathApplicationTests",
)


class MathApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.math}.
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

    @given(integers())
    def test_numberify_integer(self, integer_value: int) -> None:
        """
        L{Application.numberify} converts a string integer into an L{int}.
        """
        string_value = "{}".format(integer_value)
        result_value = Application.numberify(string_value)

        self.assertEqual(result_value, integer_value)
        self.assertEqual(type(result_value), int)

    @given(floats(allow_nan=True, allow_infinity=True))
    def test_numberify_float(self, float_value: float) -> None:
        """
        L{Application.numberify} converts a string floating-point number into a
        L{float}.
        """
        string_value = "{}".format(float_value)
        result_value = Application.numberify(string_value)

        if isnan(float_value):
            self.assertTrue(isnan(result_value))
        else:
            self.assertEqual(result_value, float_value)
        self.assertEqual(type(result_value), float)

    def test_root(self) -> None:
        """
        L{Application.root} returns a canned string.
        """
        self.assertResponse(b"/", response_data=b"Math happens here.")

    @given(integers(), integers())
    def test_add(self, x: int, y: int) -> None:
        """
        L{Application.add} sums C{a} and C{b}.
        """
        self.assertResponse(
            "/add/{}/{}".format(x, y).encode("ascii"),
            response_data=str(x + y).encode("ascii"),
        )

    @given(integers(), integers())
    def test_subtract(self, x: int, y: int) -> None:
        """
        L{Application.subtract} subtracts C{b} from C{a}.
        """
        self.assertResponse(
            "/subtract/{}/{}".format(x, y).encode("ascii"),
            response_data=str(x - y).encode("ascii")
        )

    @given(integers(), integers())
    def test_multiply(self, x: int, y: int) -> None:
        """
        L{Application.multiply} multiplies C{a} and C{b}.
        """
        self.assertResponse(
            "/multiply/{}/{}".format(x, y).encode("ascii"),
            response_data=str(x * y).encode("ascii")
        )

    @given(integers(), integers())
    def test_divide(self, x: int, y: int) -> None:
        """
        L{Application.divide} divides C{a} by C{b}.
        """
        assume(y != 0)  # Avoid division by zero
        self.assertResponse(
            "/divide/{}/{}".format(x, y).encode("ascii"),
            response_data=str(x / y).encode("ascii")
        )

    def test_invalid_input(self) -> None:
        """
        Invalid inputs result in an error.
        """
        self.assertResponse(
            b"/divide/fish/carrots",
            response_data=b"Invalid inputs provided.",
            response_code=http.BAD_REQUEST,
        )
