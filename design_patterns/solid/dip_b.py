"""
DIP: Dependency Inversion Principle
"""


import enum
from dataclasses import dataclass
from abc import ABC, abstractmethod

from typing import List, Generator


class Relation(enum.Enum):
    PARENT = 1
    CHILD = 2
    SIBLING = 3


@dataclass
class Person:
    name: str


@dataclass
class PersonRelationship:
    person: Person
    relation: Relation
    related_with: Person


class RelationshipBrowser(ABC):
    @abstractmethod
    def get_child_of(self, name) -> Generator[str, None, None]:
        pass


class Relationships(RelationshipBrowser):
    def __init__(self) -> None:
        self.relationships: List[PersonRelationship] = list()

    def create_father_child_relationship(self, father: Person, child: Person) -> None:
        self.relationships.append(
            PersonRelationship(
                person=father, relation=Relation.PARENT, related_with=child
            )
        )
        self.relationships.append(
            PersonRelationship(
                person=child, relation=Relation.CHILD, related_with=father
            )
        )

    def get_child_of(self, name) -> Generator[str, None, None]:
        for r in self.relationships:
            if r.person.name == name and r.relation == Relation.PARENT:
                yield r.related_with.name


class Research:
    def __init__(self, relationships: RelationshipBrowser) -> None:
        # relations: List[PersonRelationship] = relationships.relationships
        # for r in relations:
        #     if (r.person.name == "John") and (r.relation == Relation.PARENT):
        #         print(f"John has a child called {r.related_with.name}")
        data = relationships.get_child_of("John")
        for c in data:
            print(f"John has a child called {c}")


p = Person(name="John")
c1 = Person(name="Chris")
c2 = Person(name="Kelvin")

relationship = Relationships()
relationship.create_father_child_relationship(father=p, child=c1)
relationship.create_father_child_relationship(father=p, child=c2)

Research(relationship)
