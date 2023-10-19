from dataclasses import dataclass, field
import math

from typing_extensions import Self


@dataclass
class Point:
    x: int
    y: int

    class PointFactory:
        def new_cartesian_point(self, x: int, y: int) -> Self:
            return Point(x=x, y=y)

        def new_polar_point(self, rho: int, theta: int) -> Self:
            return Point(x=rho * math.cos(theta), y=rho * math.sin(theta))

    factory: PointFactory = field(init=False, default=PointFactory(), repr=False)


if __name__ == "__main__":
    p = Point(3, 4)
    p1 = Point.factory.new_cartesian_point(3, 4)
    p2 = Point.factory.new_polar_point(3, 4)

    print(p)
    print(p1)
    print(p2)
