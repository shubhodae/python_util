class Person:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"


class PersonFactory:
    person_id = -1

    def create_person(self, name: str) -> Person:
        PersonFactory.person_id += 1
        return Person(id=PersonFactory.person_id, name=name)


if __name__ == "__main__":
    p1 = PersonFactory().create_person(name="test1")
    p2 = PersonFactory().create_person(name="test2")
    p3 = PersonFactory().create_person(name="text3")

    print(p1)
    print(p2)
    print(p3)
