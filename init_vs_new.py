from typing import Any
from typing_extensions import Self


class Test:
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("__call__ is called !!!")

    def __new__(cls) -> Self:
        print("__new__ is called !!!")
        instance = super().__new__(cls)
        return instance

    def __init__(self) -> None:
        print("__init__ is called !!!")


if __name__ == "__main__":
    t = Test()
    t()

    print(type(Test))
    # print(type(Test()))
