"""
Klein additions.
"""

from typing import Union

from twisted.web.iweb import IRenderable
from twisted.web.resource import IResource

from klein import Klein as SuperKlein


__all__ = (
    "Klein",
    "KleinRenderable",
)


# Expected return types for route methods
KleinRenderable = Union[str, IResource, IRenderable]


#
# Subclass Klein so that we can override its documentation to work with Sphinx;
# Klein uses epydoc syntax, which is not compatible, and because the router
# is an attribute of each application, its doc string shows up in our
# documentation.
#
class Klein(SuperKlein):
    """
    Request router.
    """
