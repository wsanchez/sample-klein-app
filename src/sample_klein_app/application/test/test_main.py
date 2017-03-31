"""
Tests for L{rms.application._main}.
"""

from attr import Factory, attrib, attrs

from .._main import main
from ...ext.trial import TestCase


__all__ = (
    "ApplicationMainTests",
)


class ApplicationMainTests(TestCase):
    """
    Tests for L{rms.application._main}.
    """

    def test_main(self) -> None:
        """
        L{main} runs the router.
        """
        MockApplication.main(["app", "arg1", "arg2"])

        runsSeen = MockApplication.router.runsSeen

        self.assertEqual(len(runsSeen), 1)
        self.assertEqual(runsSeen[0], dict(host="localhost", port=8080))


class MockApplication(object):
    """
    Mock application.
    """

    @attrs
    class MockRouter(object):
        """
        Mock router.
        """

        runsSeen = attrib(default=Factory(list))

        def run(self, **kwargs):
            self.runsSeen.append(kwargs)

    router = MockRouter()

    main = classmethod(main)  # type: ignore
