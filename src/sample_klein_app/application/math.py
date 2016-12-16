"""
Math application
"""

from twisted.web import http

from klein import Klein

from ._main import main


__all__ = (
    "Application",
)


class Application(object):
    """
    Math application.

    Application performs some mathematical functions.
    """

    router = Klein()

    main = classmethod(main)

    @router.route("/")
    def root(self, request):
        """
        Application root resource.

        Responds with a message noting the nature of the application.

        @param request: The request to respond to.
        """
        return "Math happens here."

    @router.route("/add/<a>/<b>")
    def add(self, request, a, b):
        """
        Addition resource.

        Adds the two given numbers and responds with the result.

        @param request: The request to respond to.

        @param a: A number to add to C{b}.

        @param b: A number to add to C{a}.
        """
        return "{}".format(self.numberify(a) + self.numberify(b))

    @router.route("/subtract/<a>/<b>")
    def subtract(self, request, a, b):
        """
        Subtraction resource.

        Subtracts one of two given numbers from the other and responds with the
        result.

        @param request: The request to respond to.

        @param a: A number to subtract C{b} from.

        @param b: A number to subtract from C{a}.
        """
        return "{}".format(self.numberify(a) - self.numberify(b))

    @router.route("/multiply/<a>/<b>")
    def multiply(self, request, a, b):
        """
        Multiplication resource.

        Multiplies the two given numbers and responds with the result.

        @param request: The request to respond to.

        @param a: A number to multiply with C{b}.

        @param b: A number to multiply with C{a}.
        """
        return "{}".format(self.numberify(a) * self.numberify(b))

    @router.route("/divide/<a>/<b>")
    def divide(self, request, a, b):
        """
        Division resource.

        Divides one of two given numbers from the other and responds with the
        result.

        @param request: The request to respond to.

        @param a: A number to divide by C{b}.

        @param b: A number to divide C{a} by.
        """
        return "{}".format(self.numberify(a) / self.numberify(b))

    @router.handle_errors(ValueError)
    def valueError(self, request, failure):
        """
        Error handler for L{ValueError}.

        @param request: The request to respond to.

        @param failure: The failure that occurred.
        """
        request.setResponseCode(http.BAD_REQUEST)
        return "Invalid inputs provided."

    @staticmethod
    def numberify(string):
        """
        Convert a string into a number.

        @param string: A string to convert into a number.
        """
        if "." in string:
            return float(string)
        else:
            return int(string)


if __name__ == "__main__":  # pragma: no cover
    Application.main()
