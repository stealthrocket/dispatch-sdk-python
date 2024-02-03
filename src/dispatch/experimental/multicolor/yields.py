from dataclasses import dataclass
from types import FunctionType
from typing import Any


def yields(type: Any):
    """Returns a decorator that marks functions as a type of yield.

    Args:
        type: Opaque type for this yield.
    """

    def decorator(fn: FunctionType) -> FunctionType:
        fn._multicolor_yield_type = type  # type: ignore[attr-defined]
        return fn

    return decorator


class YieldType:
    """Base class for yield types."""


@dataclass
class CustomYield(YieldType):
    """A yield from a function marked with @yields.

    Attributes:
        type: The type of yield that was specified in the @yields decorator.
        args: Positional arguments to the function call.
        kwargs: Keyword arguments to the function call.
    """

    type: Any
    args: list[Any]
    kwargs: dict[str, Any] | None = None


@dataclass
class GeneratorYield(YieldType):
    """A yield from a generator.

    Attributes:
        value: The value that was yielded from the generator.
    """

    value: Any = None
