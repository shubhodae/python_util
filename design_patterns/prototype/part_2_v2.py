from dataclasses import dataclass
from abc import ABC, abstractmethod
import copy


@dataclass
class Address:
    suite: int
    city: str
    street_address: str


@dataclass
class Employee:
    name: str
    address: Address


class EmployeeFactory(ABC):
    @property
    @abstractmethod
    def registry_str(self) -> str:
        pass

    def new(self, name: str, suite: int) -> Employee:
        result = copy.deepcopy(office_employee_registy[self.registry_str])
        result.name = name
        result.address.suite = suite
        return result


office_employee_registy: dict[str, Employee] = {}

office_employee_registy["main_office"] = Employee(
    name="", address=Address(suite=0, city="London", street_address="123 London St.")
)

office_employee_registy["aux_office"] = Employee(
    name="", address=Address(suite=0, city="London", street_address="124B London St")
)


class MainOfficeEmployee(EmployeeFactory):
    registry_str = "main_office"


class AuxOfficeEmployee(EmployeeFactory):
    registry_str = "aux_office"


if __name__ == "__main__":
    john = MainOfficeEmployee().new(name="John", suite=101)
    jane = AuxOfficeEmployee().new(name="Jane", suite=502)

    print(john)
    print(jane)
