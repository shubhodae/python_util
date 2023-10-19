from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def draw_circle(self, radius: int) -> None:
        pass

    @abstractmethod
    def draw_square(self, side: int) -> None:
        pass


class VectorRenderer(Renderer):
    def draw_circle(self, radius: int) -> None:
        print(f"Drawing circle of radis: {radius}")

    def draw_square(self, side: int) -> None:
        print(f"Drawing square of side: {side}")


class PixelRenderer(Renderer):
    def draw_circle(self, radius: int) -> None:
        print(f"Drawing pixcels for circle of radis: {radius}")

    def draw_square(self, side: int) -> None:
        print(f"Drawing pixcels for square of side: {side}")


class Shape(ABC):
    def __init__(self, renderer: Renderer) -> None:
        self.renderer = renderer

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def resize(self, factor: int) -> None:
        pass


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: int) -> None:
        self.radius = radius
        super().__init__(renderer)

    def draw(self) -> None:
        self.renderer.draw_circle(radius=self.radius)

    def resize(self, factor: int) -> None:
        self.radius *= factor


class Square(Shape):
    def __init__(self, renderer: Renderer, side: int) -> None:
        self.side = side
        super().__init__(renderer)

    def draw(self) -> None:
        self.renderer.draw_square(side=self.side)

    def resize(self, factor: int) -> None:
        self.side *= factor


if __name__ == "__main__":
    vector = VectorRenderer()
    pixcel = PixelRenderer()

    circle = Circle(pixcel, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
