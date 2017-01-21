"""
Math application
"""

from typing import Union

from twisted.web import http
from twisted.web.iweb import IRequest

from ._main import main
from .klein import Klein, KleinRenderable


__all__ = (
    "Application",
)


class Application(object):
    """
    Math application.

    Application performs some mathematical functions.
    """

    router = Klein()

    main = classmethod(main)   # type: ignore

    @router.route("/")
    def root(self, request: IRequest) -> KleinRenderable:
        """
        Application root resource.

        Responds with a message noting the nature of the application.

        @param request: The request to respond to.
        """
        return "Math happens here."

    @router.route("/add/<a>/<b>")
    def add(self, request: IRequest, a: str, b: str) -> KleinRenderable:
        """
        Addition resource.

        Adds the two given numbers and responds with the result.

        @param request: The request to respond to.

        @param a: A number to add to C{b}.

        @param b: A number to add to C{a}.
        """
        x = self.numberify(a) + self.numberify(b)  # type: ignore #see #21
        return "{}".format(x)

    @router.route("/subtract/<a>/<b>")
    def subtract(self, request: IRequest, a: str, b: str) -> KleinRenderable:
        """
        Subtraction resource.

        Subtracts one of two given numbers from the other and responds with the
        result.

        @param request: The request to respond to.

        @param a: A number to subtract C{b} from.

        @param b: A number to subtract from C{a}.
        """
        x = self.numberify(a) - self.numberify(b)  # type: ignore #see #21
        return "{}".format(x)

    @router.route("/multiply/<a>/<b>")
    def multiply(self, request: IRequest, a: str, b: str) -> KleinRenderable:
        """
        Multiplication resource.

        Multiplies the two given numbers and responds with the result.

        @param request: The request to respond to.

        @param a: A number to multiply with C{b}.

        @param b: A number to multiply with C{a}.
        """
        x = self.numberify(a) * self.numberify(b)  # type: ignore #see #21
        return "{}".format(x)

    @router.route("/divide/<a>/<b>")
    def divide(self, request: IRequest, a: str, b: str) -> KleinRenderable:
        """
        Division resource.

        Divides one of two given numbers from the other and responds with the
        result.

        @param request: The request to respond to.

        @param a: A number to divide by C{b}.

        @param b: A number to divide C{a} by.
        """
        x = self.numberify(a) / self.numberify(b)  # type: ignore #see #21
        return "{}".format(x)

    @router.handle_errors(ValueError)
    def valueError(self, request: IRequest, failure) -> KleinRenderable:
        """
        Error handler for L{ValueError}.

        @param request: The request to respond to.

        @param failure: The failure that occurred.
        """
        request.setResponseCode(http.BAD_REQUEST)
        return "Invalid inputs provided."

    @staticmethod
    def numberify(string: str) -> Union[int, float]:
        """
        Convert a string into a number.

        @param string: A string to convert into a number.
        """
        try:
            return int(string)
        except ValueError:
            return float(string)


if __name__ == "__main__":  # pragma: no cover
    Application.main()  # type: ignore
