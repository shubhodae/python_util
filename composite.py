from abc import ABC, abstractmethod
from typing import List


class Department(ABC):
    @abstractmethod
    def get_department(self) -> None:
        """Prints the department name"""


class HRDepartment(Department):
    def __init__(self) -> None:
        self.name = "HR Department"

    def get_department(self) -> None:
        print(self.name)


class AccountsDepartment(Department):
    def __init__(self) -> None:
        self.name = "Accounts Department"

    def get_department(self) -> None:
        print(self.name)


class HeadDepartment(Department):
    def __init__(self, department_list: List[Department]) -> None:
        self.name = "Head Department"
        self.department_list = department_list

    def get_department(self) -> None:
        print(self.name)
        for department in self.department_list:
            department.get_department()


if __name__ == "__main__":
    hr_dept = HRDepartment()
    acc_dept = AccountsDepartment()

    head_dept = HeadDepartment([hr_dept, acc_dept])
    head_dept.get_department()
