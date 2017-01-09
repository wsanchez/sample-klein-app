"""
Tests for L{sample_klein_app.application.math}.
"""

from math import isnan

from twisted.web import http
from twisted.trial import unittest

from hypothesis import given
from hypothesis.strategies import integers, floats

from .async import defer_async
from .mock_render import assertResponse

from sample_klein_app.application.math import Application


__all__ = (
    "MathApplicationTests",
)


class MathApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.math}.
    """

    async def assertResponse(self, *args, **kwargs) -> None:
        """
        Generate and process a request using the an instance of L{Application}
        and assert that the response is as expected.

        @see L{assertResponse}

        @param args: Positional arguments to pass to L{assertResponse}.
            The C{application} argument is added as the first argument.

        @param args: Keyword arguments to pass to L{assertResponse}.
        """
        application = Application()
        await assertResponse(self, application, *args, **kwargs)

    @given(integers())
    def test_numberify_integer(self, integer_value: int) -> None:
        """
        L{Application.numberify} converts a string integer into an L{int}.
        """
        string_value = "{}".format(integer_value)
        result_value = Application.numberify(string_value)

        self.assertEqual(result_value, integer_value)
        self.assertEqual(type(result_value), int)

    @given(floats())
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

    @defer_async
    async def test_root(self) -> None:
        """
        L{Application.root} returns a canned string.
        """
        await self.assertResponse(b"/", response_data=b"Math happens here.")

    @defer_async
    async def test_add(self) -> None:
        """
        L{Application.add} sums C{a} and C{b}.
        """
        await self.assertResponse(b"/add/1/3", response_data=b"4")

    @defer_async
    async def test_subtract(self) -> None:
        """
        L{Application.subtract} subtracts C{b} from C{a}.
        """
        await self.assertResponse(b"/subtract/4/1", response_data=b"3")

    @defer_async
    async def test_multiply(self) -> None:
        """
        L{Application.multiply} multiplies C{a} and C{b}.
        """
        await self.assertResponse(b"/multiply/2/3", response_data=b"6")

    @defer_async
    async def test_divide(self) -> None:
        """
        L{Application.divide} divides C{a} by C{b}.
        """
        await self.assertResponse(b"/divide/12/3", response_data=b"4.0")

    @defer_async
    async def test_invalid_input(self) -> None:
        """
        Invalid inputs result in an error.
        """
        await self.assertResponse(
            b"/divide/fish/carrots",
            response_data=b"Invalid inputs provided.",
            response_code=http.BAD_REQUEST,
        )
