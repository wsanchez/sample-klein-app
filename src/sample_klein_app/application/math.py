"""
Math application
"""

from klein import Klein


__all__ = ["Application"]


class Application(object):
    app = Klein()

    @staticmethod
    def numberify(string):
        if "." in string:
            return float(string)
        else:
            return int(string)

    @app.route("/")
    def root(self, request):
        return "Math happens here."

    @app.route("/add/<a>/<b>")
    def add(self, request, a, b):
        return "{}".format(self.numberify(a) + self.numberify(b))

    @app.route("/subtract/<a>/<b>")
    def subtract(self, request, a, b):
        return "{}".format(self.numberify(a) - self.numberify(b))

    @app.route("/multiply/<a>/<b>")
    def multiply(self, request, a, b):
        return "{}".format(self.numberify(a) * self.numberify(b))

    @app.route("/divide/<a>/<b>")
    def divide(self, request, a, b):
        return "{}".format(self.numberify(a) / self.numberify(b))

    @app.handle_errors(ValueError)
    def valueError(self, request, failure):
        return "Invalid inputs provided."


if __name__ == "__main__":
    application = Application()
    application.app.run("localhost", 8080)
