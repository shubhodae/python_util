from dataclasses import dataclass
from typing_extensions import Self


@dataclass
class Person:
    name: str | None = None
    position: str | None = None
    date_of_birth: str | None = None


class PersonBuilder:
    def __init__(self) -> None:
        self.person = Person()

    def build(self) -> Person:
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name: str) -> Self:
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position: str) -> Self:
        self.person.position = position
        return self


class PersonDateofBirthBuilder(PersonJobBuilder):
    def born(self, date_of_birth: str) -> Self:
        self.person.date_of_birth = date_of_birth
        return self


if __name__ == "__main__":
    pb = PersonDateofBirthBuilder()
    me = pb.called("shubhadip").works_as_a("Engineer").born("1/1/1988").build()
    print(me)
