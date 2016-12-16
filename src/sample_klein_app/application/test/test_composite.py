"""
Tests for L{sample_klein_app.application.composite}.
"""

from twisted.web import http
from twisted.trial import unittest

from .async import defer_async
from .mock_render import assertResponse

from sample_klein_app.application.composite import Application


__all__ = (
    "CompositeApplicationTests",
)


class CompositeApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.composite}.
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

    async def assertChildApplication(self, sub_app, *args, **kwargs) -> None:
        """
        Assert that a child application is bound to a given name as a child
        resource of L{Application}.

        @see L{assertResponse}

        @param sub_app: The name of the child resource the child application is
            expected to be bound to.

        @param args: Positional arguments to pass to L{assertResponse}.
            The C{application} and C{request_path} arguments are added as the
            first argument.

        @param args: Keyword arguments to pass to L{assertResponse}.
        """
        path_short = b"/" + sub_app
        path_full = path_short + b"/"

        await self.assertResponse(
            path_short,
            response_code=http.MOVED_PERMANENTLY,
            response_location_path=path_full,
        )

        await self.assertResponse(path_full, *args, **kwargs)

    @defer_async
    async def test_root(self) -> None:
        """
        L{Application.root} responds with a canned string.
        """
        await self.assertResponse(
            b"/",
            response_data=(
                b"This is a web application composed from multiple "
                b"applications."
            )
        )

    @defer_async
    async def test_dns(self) -> None:
        """
        L{Application} responds with the DNS application at C{"/dns"}.
        """
        await self.assertChildApplication(b"dns", response_data=b"DNS API.")

    @defer_async
    async def test_hello(self) -> None:
        """
        L{Application} responds with the Hello application at C{"/hello"}.
        """
        await self.assertChildApplication(b"hello", response_data=b"Hello!")

    @defer_async
    async def test_math(self) -> None:
        """
        L{Application} responds with the Math application at C{"/math"}.
        """
        await self.assertChildApplication(
            b"math", response_data=b"Math happens here."
        )
