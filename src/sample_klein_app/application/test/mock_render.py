"""
Tools for simulating resource rendering.
"""

from twisted.python.url import URL
from twisted.internet.defer import inlineCallbacks
from twisted.web import http

from klein.test.test_resource import requestMock as mock_request, _render


__all__ = [
    "assertResponse",
]


@inlineCallbacks
def assertResponse(
    test, application,
    request_path,
    response_data=None,
    response_code=http.OK,
    response_location_path=None,
):
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


def render(app, request, notifyFinish=True):
    resource = app.router.resource()
    return _render(resource, request, notifyFinish)
