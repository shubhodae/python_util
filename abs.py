from abc import ABC, abstractmethod


class AnotherClass:
    var_y: int = 999

    def get_y(self):
        print(self.var_y)


    def add_x(self):
        print(self.var_y + 1)


class TestAbstruct(ABC):

    var_x: int = 99

    def get_x(self):
        print(self.var_x)

    @abstractmethod
    def add_x(self, i):
        pass

    @abstractmethod
    def substract_x(self, i):
        pass



class ClildAbstruct(TestAbstruct):

    def add_x(self, i):
        return self.var_x + i
    

class GrandclildAbstruct(ClildAbstruct):

    def substract_x(self, i):
        return self.var_x - i



# obj = GrandclildAbstruct()
# obj.get_x()
# print(obj.add_x(6))
# print(obj.substract_x(7))



class TestInheritance(AnotherClass, TestAbstruct):

    def substract_x(self, i):
        print(self.var_x - i)


obj = TestInheritance()
obj.get_y()
obj.add_x()
obj.substract_x(1)