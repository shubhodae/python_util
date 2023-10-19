from abc import abstractmethod


class Test:
    var: int

    def __init__(self) -> None:
        pass

    @abstractmethod
    def print_test(self):
        print("Hello")


t = Test()
t.print_test()
