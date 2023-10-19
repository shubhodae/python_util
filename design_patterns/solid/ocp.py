from dataclasses import dataclass
from abc import ABC, abstractmethod
import types
from typing import Any, List, Generator
import enum


class SIZE(enum.Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class COLOUR(enum.Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4


@dataclass
class Product:
    name: str
    size: SIZE
    colour: COLOUR


class Specification(ABC):
    @abstractmethod
    def _is_satisfied(self, item: Product) -> bool:
        pass

    def __and__(self, obj):
        return AndSpecification([self, obj])

    def __or__(self, obj):
        return OrSpecification([self, obj])


class AndSpecification(Specification):
    def __init__(self, specs: List[Specification]) -> None:
        self.specs = specs

    def _is_satisfied(self, item: Product) -> bool:
        return all(map(lambda spec: spec._is_satisfied(item), self.specs))


class OrSpecification(Specification):
    def __init__(self, specs: List[Specification]) -> None:
        self.specs = specs

    def _is_satisfied(self, item: Product) -> bool:
        return any(map(lambda spec: spec._is_satisfied(item), self.specs))


class ColourSpecification(Specification):
    def __init__(self, colour: COLOUR) -> None:
        self.colour = colour

    def _is_satisfied(self, item: Product) -> bool:
        return item.colour == self.colour


class SizeSpecification(Specification):
    def __init__(self, size: SIZE) -> None:
        self.size = size

    def _is_satisfied(self, item: Product) -> bool:
        return item.size == self.size


class Filter(ABC):
    def __init__(self, items: List[Product]) -> None:
        self.items = items

    @abstractmethod
    def filter(self, spec: Specification) -> Generator[Product, None, None]:
        pass


class ProductFilter(Filter):
    def filter(self, spec: Specification) -> Generator[Product, None, None]:
        for item in self.items:
            if spec._is_satisfied(item):
                yield item


if __name__ == "__main__":
    print("Hello World")

    mouse = Product(name="Mouse", size=SIZE.SMALL, colour=COLOUR.RED)
    keyboard = Product(name="Keyboard", size=SIZE.MEDIUM, colour=COLOUR.GREEN)
    monitor = Product(name="Monitor", size=SIZE.LARGE, colour=COLOUR.YELLOW)
    cpu = Product(name="CPU", size=SIZE.LARGE, colour=COLOUR.BLUE)

    items = [mouse, keyboard, monitor, cpu]
    print("--------------------------------")
    [print(item) for item in items]
    print("--------------------------------")

    filter_obj = ProductFilter(items)

    # Filter RED colour objects
    red_spec = ColourSpecification(COLOUR.RED)
    red_items = filter_obj.filter(red_spec)
    print(list(red_items))

    # Filter LARGE size objects
    large_spec = SizeSpecification(SIZE.LARGE)
    large_items = filter_obj.filter(large_spec)
    print(list(large_items))

    # Filter BLUE and LARGE objects
    # blue_and_large_spces = AndSpecification(
    #     [ColourSpecification(COLOUR.BLUE), SizeSpecification(SIZE.LARGE)]
    # )
    blue_and_large_spces = ColourSpecification(COLOUR.BLUE) & SizeSpecification(
        SIZE.LARGE
    )
    blue_and_large_items = filter_obj.filter(blue_and_large_spces)
    print(list(blue_and_large_items))

    # Filter GREEN or SMALL objects
    # green_or_small_spces = OrSpecification(
    #     [ColourSpecification(COLOUR.GREEN), SizeSpecification(SIZE.SMALL)]
    # )
    green_or_small_spces = ColourSpecification(COLOUR.GREEN) | SizeSpecification(
        SIZE.SMALL
    )
    green_or_small_items = filter_obj.filter(green_or_small_spces)
    print(list(green_or_small_items))
