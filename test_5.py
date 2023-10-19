
class Test:

    def __init__(self) -> None:
        self._test = 10

    def __get_print(self):
        print(self._test)



i = Test()
# i._test = i._test + 10
# print(i._test)
i._Test__get_print()