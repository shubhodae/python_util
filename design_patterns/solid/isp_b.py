# ISP: Iterface Segrigation Principle

from abc import ABC, abstractmethod


class Machine(ABC):
    @abstractmethod
    def printer(self) -> str:
        pass

    @abstractmethod
    def fax(self) -> str:
        pass

    @abstractmethod
    def scan(self) -> str:
        pass
