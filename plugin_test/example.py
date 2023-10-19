from dataclasses import dataclass


@dataclass
class Ram:
    name: str

    def print_name(self) -> None:
        print("name is ram")


@dataclass
class Sam:
    name: str

    def print_name(self) -> None:
        print("name is sam")
