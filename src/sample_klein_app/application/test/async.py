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
    Wrap an asynchronous callable with a callable that returns a L{Deferred}.

    @param f: An asynchronous callable.
    """
    @wraps(f)
    def wrapper(*args, **kwargs) -> Deferred:
        result = f(*args, **kwargs)
        return ensureDeferred(result)
    return wrapper
