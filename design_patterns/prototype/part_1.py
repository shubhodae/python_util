from dataclasses import dataclass

import copy


@dataclass
class Address:
    street_name: str
    city: str
    country: str


@dataclass
class Person:
    name: str
    address: Address


if __name__ == "__main__":
    john = Person(
        name="John",
        address=Address(street_name="123 London St", city="London", country="UK"),
    )
    print(john)
    jane = copy.deepcopy(john)
    jane.name = "Jane"
    jane.address.street_name = "124 London St"
    print("-----")
    print(john)
    print(jane)
