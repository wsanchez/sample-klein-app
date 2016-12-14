"""
Math application
"""

from twisted.web import http

from klein import Klein

from ._main import main


__all__ = ["Application"]


class Application(object):
    router = Klein()

    main = classmethod(main)

    @router.route("/")
    def root(self, request):
        return "Math happens here."

    @router.route("/add/<a>/<b>")
    def add(self, request, a, b):
        return "{}".format(self.numberify(a) + self.numberify(b))

    @router.route("/subtract/<a>/<b>")
    def subtract(self, request, a, b):
        return "{}".format(self.numberify(a) - self.numberify(b))

    @router.route("/multiply/<a>/<b>")
    def multiply(self, request, a, b):
        return "{}".format(self.numberify(a) * self.numberify(b))

    @router.route("/divide/<a>/<b>")
    def divide(self, request, a, b):
        return "{}".format(self.numberify(a) / self.numberify(b))

    @router.handle_errors(ValueError)
    def valueError(self, request, failure):
        request.setResponseCode(http.BAD_REQUEST)
        return "Invalid inputs provided."

    @staticmethod
    def numberify(string):
        if "." in string:
            return float(string)
        else:
            return int(string)


if __name__ == "__main__":  # pragma: no cover
    Application.main()
