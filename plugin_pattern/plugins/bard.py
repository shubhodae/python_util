"""Game Extention that adds a bard character."""

from dataclasses import dataclass
from game import factory


@dataclass
class Bard:
    name: str

    def make_a_noise(self) -> None:
        print("Toss a coin to a witcher!")


def initialize() -> None:
    factory.register("bard", Bard)
