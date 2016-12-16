"""
Tools for simulating resource rendering.
"""

from twisted.python.url import URL
from twisted.internet.defer import inlineCallbacks
from twisted.web import http

from klein.test.test_resource import requestMock as mock_request, _render


__all__ = (
    "assertResponse",
    "render",
)


@inlineCallbacks
def assertResponse(
    test, application,
    request_path,
    response_code=http.OK,
    response_data=None,
    response_location_path=None,
):
    """
    Generate and process a request using the given application and assert
    that the response is as expected.

    @param application: The application to route the request to.

    @param request_path: The path portion of the request URI.

    @param response_code: The expected HTTP status code for the response.

    @param response_data: The expected HTTP entity body data for the response.

    @param response_location_path: The expected C{"Location"} HTTP header value
        for the response.
    """
    request = mock_request(request_path)

    yield render(application, request)

    test.assertEqual(request.code, response_code)

    if response_data is not None:
        data = request.getWrittenData()
        test.assertEqual(data, response_data)

    if response_location_path is not None:
        values = request.responseHeaders.getRawHeaders("location")
        test.assertTrue(
            len(values) > 0, "No location header in response."
        )
        test.assertTrue(
            len(values) == 1, "Too many location headers in response."
        )
        url = URL.fromText(values[0])
        path = ("/" + "/".join(url.path)).encode("utf-8")
        test.assertEqual(path, response_location_path)


def render(application, request):
    """
    Render a response from the given application for the given request.

    @param application: The application to route the request to.

    @param request: The request to route the request to the application.
    """
    resource = application.router.resource()
    return _render(resource, request, notifyFinish=True)
