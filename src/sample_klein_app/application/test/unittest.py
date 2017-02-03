"""
Extensions to :mod:`twisted.trial.unittest`
"""

from twisted.internet.defer import Deferred, ensureDeferred
from twisted.trial import unittest


__all__ = (
    "TestCase",
)


class TestCase(unittest.SynchronousTestCase):
    """
    A unit test. The atom of the unit testing universe.

    This class extends :class:`unittest.SynchronousTestCase`.

    It does not extend :class:`unittest.TestCase`, because tests that are
    themselves asynchronous cause some known problems, and one should be able
    to unit test code synchronously.
    """

    def successResultOf(self, deferred: Deferred):
        """
        Override :meth:`unittest.SynchronousTestCase.successResultOf` to enable
        handling of coroutines as well as :class:`Deferred` s.
        """
        deferred = ensureDeferred(deferred)
        return unittest.TestCase.successResultOf(self, deferred)

    # def failureResultOf(self, deferred: Deferred, *expectedExceptionTypes):
    #     """
    #     Override :meth:`unittest.SynchronousTestCase.failureResultOf` to
    #     enable handling of coroutines as well as class:`Deferred` s.
    #     """
    #     deferred = ensureDeferred(deferred)
    #     return unittest.TestCase.failureResultOf(self, deferred)
