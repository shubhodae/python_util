from dataclasses import dataclass
from abc import ABC, abstractmethod

import math


@dataclass
class Point:
    x: int
    y: int


class PointFactory(ABC):
    @abstractmethod
    def __init__(self, x: int, y: int) -> None:
        """Implements in clild class: set 'self.x' and 'self.y' values"""

    def new(self) -> Point:
        return Point(x=self.x, y=self.y)


class CartesianPointFactory(PointFactory):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class PolarPointFactory(PointFactory):
    def __init__(self, rho: int, theta: int) -> None:
        self.x = rho * math.cos(theta)
        self.y = rho * math.sin(theta)


if __name__ == "__main__":
    p = Point(1, 2)
    p2 = CartesianPointFactory(1, 2).new()
    p3 = PolarPointFactory(1, 2).new()

    print(p)
    print(p2)
    print(p3)
