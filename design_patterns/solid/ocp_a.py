from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Generator
import enum


class Colour(enum.Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


class Size(enum.Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


@dataclass
class Product:
    name: str
    size: Size
    colour: Colour


class Specification(ABC):
    @abstractmethod
    def _is_satisfied(self, item: Product) -> bool:
        pass

    def __and__(self, obj):
        return AndSpecification(self, obj)

    def __or__(self, obj):
        return OrSpecification(self, obj)


class AndSpecification(Specification):
    def __init__(self, *args) -> None:
        self.args = args

    def _is_satisfied(self, item: Product) -> bool:
        return all(map(lambda spec: spec._is_satisfied(item), self.args))


class OrSpecification(Specification):
    def __init__(self, *args) -> None:
        self.args = args

    def _is_satisfied(self, item: Product) -> bool:
        return any(map(lambda spec: spec._is_satisfied(item), self.args))


class ColourSpecification(Specification):
    def __init__(self, colour: Colour) -> None:
        self.colour = colour

    def _is_satisfied(self, item: Product) -> bool:
        return item.colour == self.colour


class Filter(ABC):
    def __init__(self, items: List[Product]) -> None:
        self.items = items

    @abstractmethod
    def filter(self, spec: Specification) -> Generator[Product, None, None]:
        pass


class SizeSpecification(Specification):
    def __init__(self, size: Size) -> None:
        self.size = size

    def _is_satisfied(self, item: Product) -> bool:
        return item.size == self.size


class ProductFilter(Filter):
    def filter(self, spec: Specification) -> Generator[Product, None, None]:
        for item in self.items:
            if spec._is_satisfied(item):
                yield item


if __name__ == "__main__":
    print("Hello World")

    earphone = Product(name="earphone", size=Size.SMALL, colour=Colour.RED)
    laptop = Product(name="laptop", size=Size.MEDIUM, colour=Colour.YELLOW)
    desk = Product(name="desk", size=Size.LARGE, colour=Colour.GREEN)
    flower = Product(name="flower", size=Size.MEDIUM, colour=Colour.RED)

    items = [earphone, laptop, desk, flower]
    # print(items)

    filter_obj = ProductFilter(items)

    red_spec = ColourSpecification(Colour.RED)
    red_items = filter_obj.filter(red_spec)
    print(list(red_items))

    medium_spce = SizeSpecification(Size.MEDIUM)
    medium_items = filter_obj.filter(medium_spce)
    print(list(medium_items))

    large_and_green_spec = SizeSpecification(Size.LARGE) & ColourSpecification(
        Colour.GREEN
    )
    large_and_green_items = filter_obj.filter(large_and_green_spec)
    print(list(large_and_green_items))

    red_or_green_spec = ColourSpecification(Colour.GREEN) | ColourSpecification(
        Colour.YELLOW
    )
    # red_or_green_spec = OrSpecification(
    #     ColourSpecification(Colour.GREEN), ColourSpecification(Colour.YELLOW)
    # )
    red_or_green_items = filter_obj.filter(red_or_green_spec)
    print("-------------------OR------------------")
    print(list(red_or_green_items))
