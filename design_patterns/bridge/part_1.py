# circle square
# vector raster


from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

    @abstractmethod
    def render_square(self, side):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radis {radius}")

    def render_square(self, side):
        print(f"Drawing a square of side {side}")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle of radis {radius}")

    def render_square(self, side):
        print(f"Drawing pixels for a square of side {side}")


class Shape(ABC):
    def __init__(self, renderer: Renderer) -> None:
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer: Renderer, radius: int) -> None:
        self.radius = radius
        super().__init__(renderer)

    def draw(self):
        self.renderer.render_circle(radius=self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
