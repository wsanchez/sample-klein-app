from twisted.internet.defer import Deferred, ensureDeferred
from twisted.trial import unittest


__all__ = (
    "TestCase",
)


class TestCase(unittest.TestCase):
    def successResultOf(self, deferred):
        deferred = ensureDeferred(deferred)
        return unittest.TestCase.successResultOf(self, deferred)

    def failureResultOf(self, deferred, *expectedExceptionTypes):
        deferred = ensureDeferred(deferred)
        return unittest.TestCase.failureResultOf(self, deferred)
