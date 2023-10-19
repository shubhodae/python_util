from abc import ABC, abstractmethod


class IPerson(ABC):
    @abstractmethod
    def print_person(self) -> None:
        """Implement in clild class"""


class Person(IPerson):
    def print_person(self) -> None:
        print("I am a person")


class ProxyPerson(IPerson):
    def __init__(self) -> None:
        self.person = Person()

    def print_person(self) -> None:
        print("I am a proxy person")
        self.person.print_person()


if __name__ == "__main__":
    print("Hello ---------")
    p1 = Person()
    p1.print_person()

    p2 = ProxyPerson()
    p2.print_person()
