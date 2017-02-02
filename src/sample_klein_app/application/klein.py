"""
Klein additions.
"""

from typing import Union

from twisted.web.iweb import IRenderable
from twisted.web.resource import IResource

from klein import Klein


__all__ = (
    "Klein",
    "KleinRenderable",
)


# Expected return types for route methods
KleinRenderable = Union[str, IResource, IRenderable]
