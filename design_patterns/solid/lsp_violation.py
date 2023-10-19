class Rectrangle:
    def __init__(self, width, height) -> None:
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value) -> None:
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value) -> None:
        self._height = value

    @property
    def area(self) -> int:
        return self._width * self._height

    def __str__(self) -> str:
        return f"width: {self._width} | height: {self._height}"


class Square(Rectrangle):
    def __init__(self, size) -> None:
        super().__init__(size, size)

    @Rectrangle.width.setter
    def height(self, value) -> None:
        self._width = self._height = value

    @Rectrangle.height.setter
    def width(self, value) -> None:
        self._width = self._height = value


def use_it(rc: Rectrangle) -> None:
    w = rc.width
    rc.height = 10
    expected = w * 10
    print(f"Expected: {expected}, got: {rc.area}")


rc = Rectrangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
