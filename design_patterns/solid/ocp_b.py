from dataclasses import dataclass
import enum
from typing import List, Generator


class Size(enum.Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Colour(enum.Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3


@dataclass
class Product:
    name: str
    size: Size
    colour: Colour


class Filter:
    def __init__(self, items: List[Product]) -> None:
        self.items = items

    def colour_filter(self, colour: Colour) -> Generator[Product, None, None]:
        for item in self.items:
            if item.colour == colour:
                yield item

    def size_filter(self, size: Size) -> Generator[Product, None, None]:
        for item in self.items:
            if item.size == size:
                yield item

    def colour_and_size_filter(
        self, colour: Colour, size: Size
    ) -> Generator[Product, None, None]:
        for item in self.items:
            if (item.colour == colour) and (item.size == size):
                yield (item)


if __name__ == "__main__":
    print("Hello World")

    earphone = Product(name="earphone", size=Size.SMALL, colour=Colour.RED)
    laptop = Product(name="laptop", size=Size.MEDIUM, colour=Colour.YELLOW)
    desk = Product(name="desk", size=Size.LARGE, colour=Colour.GREEN)

    items = [earphone, laptop, desk]

    filter_obj = Filter(items)

    red_items = filter_obj.colour_filter(Colour.RED)
    print(list(red_items))

    medium_items = filter_obj.size_filter(Size.MEDIUM)
    print(list(medium_items))

    large_and_green_items = filter_obj.colour_and_size_filter(Colour.GREEN, Size.LARGE)
    print(list(large_and_green_items))
