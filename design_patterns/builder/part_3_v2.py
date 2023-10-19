from dataclasses import dataclass
from typing_extensions import Self


@dataclass
class Person:
    # address info
    street_address: str | None = None
    city: str | None = None
    postal_code: str | None = None

    # employment info
    company_name: str | None = None
    position: str | None = None
    annual_income: int | None = None


class PersonBuilder:
    def __init__(self, person: Person = None) -> None:
        if not person:
            self.person = Person()
        else:
            self.person = person

    @property
    def lives(self):
        return AddressBuilder(self.person)

    @property
    def works(self):
        return JobBuilder(self.person)

    def build(self) -> Person:
        return self.person


class AddressBuilder(PersonBuilder):
    def __init__(self, pserson: Person) -> None:
        super().__init__(pserson)

    def at(self, street_address: str) -> Self:
        self.person.street_address = street_address
        return self

    def in_city(self, city: str) -> Self:
        self.person.city = city
        return self

    def with_postcode(self, post_code: str) -> Self:
        self.person.postal_code = post_code
        return self


class JobBuilder(PersonBuilder):
    def __init__(self, pserson: Person) -> None:
        super().__init__(pserson)

    def at(self, company_name: str) -> Self:
        self.person.company_name = company_name
        return self

    def as_a(self, positon: str) -> Self:
        self.person.position = positon
        return self

    def earning(self, annual_income: int) -> Self:
        self.person.annual_income = annual_income
        return self


pb = PersonBuilder()
pb = (
    pb.lives.at("AE 582")
    .in_city("kolkata")
    .with_postcode("700064")
    .works.at("Indiqube")
    .as_a("Engineer")
    .earning(300000)
    .build()
)
print(pb)
