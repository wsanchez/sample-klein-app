"""
Tests for L{sample_klein_app.application.hello}.
"""

from twisted.trial import unittest

from .async import defer_async
from .mock_render import assertResponse

from sample_klein_app.application.hello import Application


__all__ = (
    "HelloApplicationTests",
)


class HelloApplicationTests(unittest.TestCase):
    """
    Tests for L{sample_klein_app.application.hello}.
    """

    async def assertResponse(self, *args, **kwargs):
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

    @defer_async
    async def test_root(self) -> None:
        """
        L{Application.root} returns a canned string.
        """
        await self.assertResponse(b"/", response_data=b"Hello!")
