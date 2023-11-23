from dataclasses import dataclass
from pydantic import BaseModel


@dataclass
class Person:
    name: str
    age: int


class PersonModel(BaseModel):
    name: str
    age: int


if __name__ == "__main__":
    p = Person("Ram", 24)
    print(p)

    p = Person("Ram", "24")
    print(p)
    print(type(p.age))

    p = PersonModel(name="Ram", age=24)
    print(p)

    p = PersonModel(name="Ram", age="24")
    print(p)

    print(type(p.age))

    print(p.model_dump())
