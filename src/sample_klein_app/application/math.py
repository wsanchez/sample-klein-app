"""
Math application
"""

from klein import Klein


__all__ = ["Application"]


class Application(object):
    router = Klein()

    @staticmethod
    def numberify(string):
        if "." in string:
            return float(string)
        else:
            return int(string)

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
        return "Invalid inputs provided."


if __name__ == "__main__":  # pragma: no cover
    application = Application()
    application.router.run("localhost", 8080)
