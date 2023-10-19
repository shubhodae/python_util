
class Test:

    def __init__(self, a, b) -> None:
        self._a = a
        self._b = b

    

class Exp:

    def __init__(self, test: Test) -> None:
        self._test = test

    def print_test(self):
        print(self._test)



e = Exp(Test)
e.print_test()

obj = Test(1, 2)

e = Exp(obj)
e.print_test()