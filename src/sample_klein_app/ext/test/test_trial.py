"""
Tests for :mod:`sample-klein-app.ext.trial`
"""

from ..klein import requestMock
from ..trial import TestCase


__all__ = ()



class ResultOfTests(TestCase):
    """
    Tests for ``*ResultOf`` methods of :class:`TestCase`.
    """

    def test_successResultOf(self):
        """
        :meth:`TestCase.successResultOf` works with coroutines.
        """
        raise NotImplementedError()

    test_successResultOf.todo = "unimplemented"


    def test_failureResultOf(self):
        """
        :meth:`TestCase.failureResultOf` works with coroutines.
        """
        raise NotImplementedError()

    test_failureResultOf.todo = "unimplemented"



class AssertionTests(TestCase):
    """
    Tests for ``assert*`` methods of :class:`TestCase`.
    """

    def test_assertResponseCode_match(self):
        """
        :meth:`TestCase.assertResponseCode` does not raise when given a request
        with the expected response code.
        """
        request = requestMock(b"/")
        request.code = 201

        self.assertResponseCode(request, 201)


    def test_assertResponseCode_mismatch(self):
        """
        :meth:`TestCase.assertResponseCode` raises :obj:`self.failureException`
        when given a request without the expected response code.
        """
        request = requestMock(b"/")
        request.code = 500

        self.assertRaises(
            self.failureException, self.assertResponseCode, request, 201
        )


    def test_assertResponseContentType_match(self):
        """
        :meth:`TestCase.assertResponseContentType` does not raise when given a
        request with the expected response ``Content-Type`` header.
        """
        request = requestMock(b"/")
        request.setHeader("content-type", "text/l33t")

        self.assertResponseContentType(request, "text/l33t")


    def test_assertResponseContentType_mismatch(self):
        """
        :meth:`TestCase.assertResponseContentType` raises
        :obj:`self.failureException` when given a request without the expected
        response ``Content-Type`` header.
        """
        request = requestMock(b"/")
        request.setHeader("content-type", "text/plain")

        self.assertRaises(
            self.failureException,
            self.assertResponseContentType, request, "text/l33t"
        )
