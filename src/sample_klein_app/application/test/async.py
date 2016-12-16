"""
Async decorator for trial
"""

from typing import Callable

from functools import wraps

from twisted.internet.defer import Deferred, ensureDeferred


__all__ = (
    "defer_async",
)


# Ideally, we want trial to handle coroutines natively, so we won't need this
# decorator.
def defer_async(f: Callable) -> Callable:
    """
    Wrap a coroutine such that it returns a deferred.

    This is useful when you want to write a coroutine (an C{async def}
    callable) that is going to be called by code that expects a callable that
    returns a deferred.

    @param f: A coroutine.
    """
    @wraps(f)
    def wrapper(*args, **kwargs) -> Deferred:
        result = f(*args, **kwargs)
        return ensureDeferred(result)
    return wrapper
