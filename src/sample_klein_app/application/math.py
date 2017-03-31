# -*- test-case-name: sample_klein_app.application.test.test_math -*-
"""
Math application
"""

from typing import Optional, Sequence, Union

from twisted.python.failure import Failure
from twisted.web import http
from twisted.web.iweb import IRequest

from ._main import main
from ..ext.klein import Klein, KleinRenderable


__all__ = (
    "Application",
)


class Application(object):
    """
    Math application.

    Application performs some mathematical functions.
    """

    router = Klein()

    @classmethod
    def main(cls, argv: Optional[Sequence[str]] = None) -> None:
        """
        Main entry point.
        """
        main(cls, argv)

    @router.route("/")
    def root(self, request: IRequest) -> KleinRenderable:
        """
        Application root resource.

        Responds with a message noting the nature of the application.

        :param request: The request to respond to.
        """
        return "Math happens here."

    @router.route("/add/<a>/<b>")
    def add(self, request: IRequest, a: str, b: str) -> KleinRenderable:
        """
        Addition resource.

        Adds the two given numbers and responds with the result.

        :param request: The request to respond to.

        :param a: A number to add to ``b``.

        :param b: A number to add to ``a``.
        """
        x = self.numberify(a) + self.numberify(b)  # type: ignore #see #21
        return "{}".format(x)

    @router.route("/subtract/<a>/<b>")
    def subtract(self, request: IRequest, a: str, b: str) -> KleinRenderable:
        """
        Subtraction resource.

        Subtracts one of two given numbers from the other and responds with the
        result.

        :param request: The request to respond to.

        :param a: A number to subtract ``b`` from.

        :param b: A number to subtract from ``a``.
        """
        x = self.numberify(a) - self.numberify(b)  # type: ignore #see #21
        return "{}".format(x)

    @router.route("/multiply/<a>/<b>")
    def multiply(self, request: IRequest, a: str, b: str) -> KleinRenderable:
        """
        Multiplication resource.

        Multiplies the two given numbers and responds with the result.

        :param request: The request to respond to.

        :param a: A number to multiply with ``b``.

        :param b: A number to multiply with ``a``.
        """
        x = self.numberify(a) * self.numberify(b)  # type: ignore #see #21
        return "{}".format(x)

    @router.route("/divide/<a>/<b>")
    def divide(self, request: IRequest, a: str, b: str) -> KleinRenderable:
        """
        Division resource.

        Divides one of two given numbers from the other and responds with the
        result.

        :param request: The request to respond to.

        :param a: A number to divide by ``b``.

        :param b: A number to divide ``a`` by.
        """
        x = self.numberify(a) / self.numberify(b)  # type: ignore #see #21
        return "{}".format(x)

    @router.handle_errors(ValueError)
    def valueError(
        self, request: IRequest, failure: Failure
    ) -> KleinRenderable:
        """
        Error handler for :exc:`ValueError`.

        :param request: The request to respond to.

        :param failure: The failure that occurred.
        """
        request.setResponseCode(http.BAD_REQUEST)
        return "Invalid inputs provided."

    @staticmethod
    def numberify(string: str) -> Union[int, float]:
        """
        Convert a string into a number.

        :param string: A string to convert into a number.
        """
        try:
            return int(string)
        except ValueError:
            return float(string)


if __name__ == "__main__":  # pragma: no cover
    Application.main()
