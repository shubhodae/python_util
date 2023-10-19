from dataclasses import dataclass
import copy


@dataclass
class Address:
    suite: str
    city: str
    street_address: str


@dataclass
class Employee:
    name: str
    address: Address


class EmployeeFactory:
    main_office_employee = Employee(
        name="", address=Address(suite=0, city="London", street_address="123 London St")
    )
    aux_office_employee = Employee(
        name="",
        address=Address(suite=0, city="London", street_address="124B London St"),
    )

    def __new_employee(proto: Employee, name: str, suite: int) -> Employee:
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name: str, suite: int) -> Employee:
        return EmployeeFactory.__new_employee(
            proto=EmployeeFactory.main_office_employee, name=name, suite=suite
        )

    @staticmethod
    def new_aux_office_employee(name: str, suite: int) -> Employee:
        return EmployeeFactory.__new_employee(
            proto=EmployeeFactory.aux_office_employee, name=name, suite=suite
        )


john = EmployeeFactory.new_main_office_employee("John", 201)
jane = EmployeeFactory.new_aux_office_employee("Jane", 302)

print(john)
print(jane)
