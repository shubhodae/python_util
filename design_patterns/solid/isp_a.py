from abc import ABC, abstractmethod


class MachinePrinter(ABC):
    @abstractmethod
    def printer(self) -> str:
        pass


class MachineFax(ABC):
    @abstractmethod
    def fax(self) -> str:
        pass


class MachineScan(ABC):
    @abstractmethod
    def scan(self) -> str:
        pass


class MyPrinter(MachinePrinter):
    def printer(self) -> str:
        return "Printing document"


class Multifunction(MachineScan, MachinePrinter):
    @abstractmethod
    def scan(self) -> str:
        pass

    @abstractmethod
    def printer(self) -> str:
        pass


class MyScanner(MachineScan):
    def scan(self) -> str:
        return "Scaning document"


class Photocopier(Multifunction):
    def printer(self) -> str:
        return "Printing document"

    def scan(self) -> str:
        return "Scanning document"


class MultifunctionMachine(Multifunction):
    def __init__(self, printer_obj: MachinePrinter, scanner_obj: MachineScan) -> None:
        self.printer_obj = printer_obj
        self.scanner_obj = scanner_obj

    def printer(self) -> str:
        return self.printer_obj.printer()

    def scan(self) -> str:
        return self.scanner_obj.scan()


p = MyPrinter()
s = MyScanner()
obj = MultifunctionMachine(p, s)
