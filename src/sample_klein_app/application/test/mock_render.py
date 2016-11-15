"""
Tools for simulating resource rendering.
"""

from klein.test.test_resource import requestMock as mock_request, _render


__all__ = [
    "mock_request",
    "render",
]


def render(app, request, notifyFinish=True):
    resource = app.router.resource()
    return _render(resource, request, notifyFinish)
