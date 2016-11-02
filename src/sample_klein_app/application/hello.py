"""
Hello application
"""

from klein import Klein


class Application(object):
    app = Klein()

    @app.route("/")
    def hello(self, request):
        return "Hello!"


if __name__ == "__main__":
    application = Application()
    application.app.run("localhost", 8080)
