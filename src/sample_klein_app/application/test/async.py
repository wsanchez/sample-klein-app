"""
Async decorator for trial
"""

from functools import wraps

from twisted.internet.defer import ensureDeferred


__all__ = (
    "defer_async",
)


# Ideally, we want trial to handle coroutines natively, so we won't need this
# decorator.
def defer_async(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        return ensureDeferred(result)
    return wrapper
