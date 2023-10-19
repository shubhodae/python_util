from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render(self, size: int):
        pass


class VertorRenderer(Renderer):
    def render(self, size: int):
        print(f"rendering vector render of size: {size}")


class PixelRender(Renderer):
    def render(self, size: int):
        print(f"rendering pixer render if size: {size}")


class Shape(ABC):
    def __init__(self, renderer: Renderer, size: int) -> None:
        self.renderer = renderer
        self.size = size

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor):
        pass


class Circle(Shape):
    def draw(self):
        self.renderer.render(self.size)

    def resize(self, factor):
        self.size *= factor


if __name__ == "__main__":
    vector = VertorRenderer()
    pixcel = PixelRender()

    c = Circle(pixcel, 5)
    c.draw()
    c.resize(2)
    c.draw()
