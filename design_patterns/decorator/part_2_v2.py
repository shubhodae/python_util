from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __str__(self) -> str:
        return ""


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def rsize(self, factor: int) -> None:
        self.radius *= factor

    def __str__(self) -> str:
        return f"A circle with radius {self.radius}"


class Square(Shape):
    def __init__(self, side: int) -> None:
        self.side = side

    def __str__(self) -> str:
        return f"A square with side {self.side}"


class ColoredShape(Shape):
    def __init__(self, shape: Shape, color: str) -> None:
        if isinstance(shape, ColoredShape):
            raise Exception("Cannot apply same decorator twice")
        self.shape = shape
        self.color = color

    def __str__(self) -> str:
        return f"{self.shape} has the color {self.color}"


class TransperantShape(Shape):
    def __init__(self, shape: Shape, transparency: float) -> None:
        self.shape = shape
        self.transparency = transparency

    def __str__(self) -> str:
        return f"{self.shape} has {self.transparency * 100}% transparency"


if __name__ == "__main__":
    circle = Circle(2)
    print(circle)

    red_circle = ColoredShape(circle, "red")
    print(red_circle)

    red_half_transperant_circle = TransperantShape(red_circle, 0.5)
    print(red_half_transperant_circle)

    # mixed = ColoredShape(ColoredShape(Circle(8), "red"), "green")
    # print(mixed)
