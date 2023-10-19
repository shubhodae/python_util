from dataclasses import dataclass
from abc import ABC, abstractmethod
import math


@dataclass
class Point:
    x: int
    y: int


class PointFactory(ABC):
    @abstractmethod
    def new(self) -> Point:
        """Implements in child class"""


class CartesianPointFactory(PointFactory):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def new(self) -> Point:
        return Point(self.x, self.y)


class PolarPointFactory(PointFactory):
    def __init__(self, rho: int, theta: int) -> None:
        self.x = rho * math.cos(theta)
        self.y = rho * math.sin(theta)

    def new(self) -> Point:
        return Point(self.x, self.y)


if __name__ == "__main__":
    p = Point(1, 2)
    p1 = CartesianPointFactory(1, 2).new()
    p2 = PolarPointFactory(1, 2).new()

    print(p)
    print(p1)
    print(p2)
