"""
Tools for simulating resource rendering.
"""

from twisted.internet.defer import inlineCallbacks
from twisted.web import http

from klein.test.test_resource import requestMock as mock_request, _render


__all__ = [
    "assertResponse",
]


@inlineCallbacks
def assertResponse(
    test, application, request_path, response_data=None, response_code=http.OK,
):
    request = mock_request(request_path)

    yield render(application, request)

    test.assertEqual(request.code, response_code)

    if response_data is not None:
        test.assertEqual(request.getWrittenData(), response_data)


def render(app, request, notifyFinish=True):
    resource = app.router.resource()
    return _render(resource, request, notifyFinish)
