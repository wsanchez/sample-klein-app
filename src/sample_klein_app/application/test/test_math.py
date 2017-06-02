"""
Tests for :mod:`sample_klein_app.application.math`.
"""

from math import isnan
from typing import Any, List

from hypothesis import assume, given
from hypothesis.strategies import floats, integers

from twisted.web import http

from .mock_render import assertResponse
from .. import math
from ..math import Application
from ...ext.trial import TestCase


__all__ = (
    "MathApplicationTests",
)


List  # pyflakes



class MathApplicationTests(TestCase):
    """
    Tests for :mod:`sample_klein_app.application.math`.
    """

    def test_main(self) -> None:
        """
        :meth:`Application.main` wraps :func:`.._main.main`.
        """
        argsSeen = []  # type: List[Any]

        def main(*args: Any) -> None:
            assert len(argsSeen) == 0
            argsSeen.extend(args)

        self.patch(math, "main", main)

        argv = []  # type: List[Any]
        Application.main(argv)

        self.assertEqual(len(argsSeen), 2)
        self.assertIdentical(argsSeen[0], Application)
        self.assertIdentical(argsSeen[1], argv)


    def assertResponse(self, *args: Any, **kwargs: Any) -> None:
        """
        Generate and process a request using the an instance of
        :class:`.math.Application` and assert that the response is as expected.

        See :meth:`assertResponse`.

        :param args: Positional arguments to pass to :meth:`assertResponse`.
            The ``application`` argument is added as the first argument.

        :param args: Keyword arguments to pass to :meth:`assertResponse`.
        """
        self.successResultOf(
            assertResponse(self, Application(), *args, **kwargs)
        )


    @given(integers())
    def test_numberify_integer(self, integerValue: int) -> None:
        """
        :meth:`.math.Application.numberify` converts a string integer into an
        :class:`int`.
        """
        stringValue = "{}".format(integerValue)
        resultValue = Application.numberify(stringValue)

        self.assertEqual(resultValue, integerValue)
        self.assertEqual(type(resultValue), int)


    @given(floats(allow_nan=True, allow_infinity=True))
    def test_numberify_float(self, floatValue: float) -> None:
        """
        :meth:`.math.Application.numberify` converts a string floating-point
        number into a :class:`float`.
        """
        stringValue = "{}".format(floatValue)
        resultValue = Application.numberify(stringValue)

        if isnan(floatValue):
            self.assertTrue(isnan(resultValue))
        else:
            self.assertEqual(resultValue, floatValue)
        self.assertEqual(type(resultValue), float)


    def test_root(self) -> None:
        """
        :meth:`.math.Application.root` returns a canned string.
        """
        self.assertResponse(b"/", responseData=b"Math happens here.")


    @given(integers(), integers())
    def test_add(self, x: int, y: int) -> None:
        """
        :meth:`.math.Application.add` sums ``a`` and ``b``.
        """
        self.assertResponse(
            "/add/{}/{}".format(x, y).encode("ascii"),
            responseData=str(x + y).encode("ascii"),
        )


    @given(integers(), integers())
    def test_subtract(self, x: int, y: int) -> None:
        """
        :meth:`.math.Application.subtract` subtracts ``b`` from ``a``.
        """
        self.assertResponse(
            "/subtract/{}/{}".format(x, y).encode("ascii"),
            responseData=str(x - y).encode("ascii")
        )


    @given(integers(), integers())
    def test_multiply(self, x: int, y: int) -> None:
        """
        :meth:`.math.Application.multiply` multiplies ``a`` and ``b``.
        """
        self.assertResponse(
            "/multiply/{}/{}".format(x, y).encode("ascii"),
            responseData=str(x * y).encode("ascii")
        )


    @given(integers(), integers())
    def test_divide(self, x: int, y: int) -> None:
        """
        :meth:`.math.Application.divide` divides ``a`` by ``b``.
        """
        assume(y != 0)  # Avoid division by zero
        self.assertResponse(
            "/divide/{}/{}".format(x, y).encode("ascii"),
            responseData=str(x / y).encode("ascii")
        )


    def test_invalid_input(self) -> None:
        """
        Invalid inputs result in an error.
        """
        self.assertResponse(
            b"/divide/fish/carrots",
            responseData=b"Invalid inputs provided.",
            responseCode=http.BAD_REQUEST,
        )
