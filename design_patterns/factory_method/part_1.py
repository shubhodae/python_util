# import enum
import math

from typing_extensions import Self


# class CoortinateSystem(enum.Enum):
#     CARTESIAN = 1
#     POALR = 2


class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

    # def __init__(
    #     self, a: int, b: int, system: CoortinateSystem = CoortinateSystem.CARTESIAN
    # ) -> None:
    #     if system == CoortinateSystem.CARTESIAN:
    #         self.x = a
    #         self.y = b
    #     elif system == CoortinateSystem.POALR:
    #         self.x = a * math.cos(b)
    #         self.y = a * math.sin(b)

    class PointFactory:
        def new_cartesian_point(self, x: int, y: int) -> Self:
            return Point(x, y)

        def new_polar_point(self, rho: int, theta: int) -> Self:
            return Point(rho * math.cos(theta), rho * math.sin(theta))

    factory = PointFactory()


if __name__ == "__main__":
    p = Point(3, 4)
    p2 = Point.factory.new_polar_point(1, 2)
    print(p, p2)
