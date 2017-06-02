"""
Tools for simulating resource rendering.
"""

from typing import Any

from twisted.python.url import URL
from twisted.web import http
from twisted.web.iweb import IRequest

from klein.test.test_resource import _render, requestMock as mock_request

from ...ext.trial import TestCase


__all__ = (
    "assertResponse",
    "render",
)


async def assertResponse(
    test: TestCase, application: Any,
    requestPath: str,
    responseCode: int = http.OK,
    responseData: bytes = None,
    responseLocationPath: str = None,
) -> None:
    """
    Generate and process a request using the given application and assert
    that the response is as expected.

    :param application: The application to route the request to.

    :param requestPath: The path portion of the request URI.

    :param responseCode: The expected HTTP status code for the response.

    :param responseData: The expected HTTP entity body data for the response.

    :param responseLocationPath: The expected ``Location`` HTTP header value
        for the response.
    """
    request = mock_request(requestPath)

    await render(application, request)

    test.assertEqual(request.code, responseCode)

    if responseData is not None:
        data = request.getWrittenData()
        test.assertEqual(data, responseData)

    if responseLocationPath is not None:
        values = request.responseHeaders.getRawHeaders("location")
        test.assertTrue(
            len(values) > 0, "No location header in response."
        )
        test.assertTrue(
            len(values) == 1, "Too many location headers in response."
        )
        url = URL.fromText(values[0])
        path = ("/" + "/".join(url.path)).encode("utf-8")
        test.assertEqual(path, responseLocationPath)


async def render(application: Any, request: IRequest) -> None:
    """
    Render a response from the given application for the given request.

    :param application: The application to route the request to.

    :param request: The request to route the request to the application.
    """
    resource = application.router.resource()
    await _render(resource, request, notifyFinish=True)
