from dataclasses import dataclass
from typing_extensions import Self


@dataclass
class Person:
    # address
    street_address: str = None
    post_code: str = None
    city: str = None

    # employment info
    company_name: str = None
    position: str = None
    annual_income: int = None


class PersonBuilder:  # facade
    def __init__(self, person=None) -> None:
        if not person:
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def at(self, company_name: str) -> Self:
        self.person.company_name = company_name
        return self

    def as_a(self, position: str) -> Self:
        self.person.position = position
        return self

    def earning(self, annual_income: int) -> Self:
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def at(self, street_address: str) -> Self:
        self.person.street_address = street_address
        return self

    def with_postcocde(self, post_code: str) -> Self:
        self.person.post_code = post_code
        return self

    def in_city(self, city: str) -> Self:
        self.person.city = city
        return self


if __name__ == "__main__":
    pb = PersonBuilder()
    pb = (
        pb.lives.at("123 London Rd")
        .in_city("London")
        .with_postcocde("SW12BC")
        .works.at("Fabrikam")
        .as_a("Engineer")
        .earning(1230000)
        .build()
    )
    print(pb)

    p2 = PersonBuilder().build()
    print(p2)
