from collections.abc import (
    Callable
)

def set_module(module) -> Callable: # shamelessly ripped from pandas
    """Private decorator for overriding __module__ on a function or class.

    Example usage::

        @set_module("pandas")
        def example():
            pass

        assert example.__module__ == "pandas"
    """

    def decorator(func: Callable) -> Callable:
        if module is not None:
            func.__module__ = module
        return func

    return decorator

