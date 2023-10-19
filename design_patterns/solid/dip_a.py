import enum
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Generator, List


class Relation(enum.Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3


@dataclass
class Person:
    name: str


@dataclass
class PersonRelation:
    person: Person
    relation: Relation
    related_with: Person


class RelationshipBorwser(ABC):
    @abstractmethod
    def get_clild_of(self, person: Person) -> Generator[Person, None, None]:
        pass


class Relationship(RelationshipBorwser):
    def __init__(self) -> None:
        self.relations: List[PersonRelation] = list()

    def create_parent_child_realation(self, parent: Person, child: Person) -> None:
        self.relations.append(
            PersonRelation(person=parent, relation=Relation.PARENT, related_with=child)
        )
        self.relations.append(
            PersonRelation(person=child, relation=Relation.CHILD, related_with=parent)
        )

    def get_clild_of(self, person: Person) -> Generator[Person, None, None]:
        for r in self.relations:
            if r.person == person and r.relation == Relation.PARENT:
                yield r.related_with


class Research:
    def __init__(self, relationship: RelationshipBorwser) -> None:
        self.relationship = relationship

    def print_child_of(self, p: Person) -> None:
        children = self.relationship.get_clild_of(p)
        for child in children:
            print(f"{p.name} has a child called {child.name}")


p = Person(name="John")
c1 = Person(name="Kelvin")
c2 = Person(name="Steve")

r = Relationship()
r.create_parent_child_realation(p, c1)
r.create_parent_child_realation(p, c2)

re = Research(r)
re.print_child_of(p)
