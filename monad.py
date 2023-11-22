from typing import Any, Callable
from typing_extensions import Self


class Functor:
    def __init__(self, value: Any) -> None:
        self.value = value

    def map(self, func: Callable[[Any], Any]) -> Self:
        return Functor(func(self.value))
