import random, string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass(kw_only=True, frozen=True)
class Person:
    name: str
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "_search_string", f"{self.name} {self.address}")


def main() -> None:
    person = Person(name="John", address="123 main st")
    print(person)


if __name__ == "__main__":
    main()
