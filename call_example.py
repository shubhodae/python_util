from typing import Any
from typing_extensions import Self


class Test:
    def __new__(cls) -> Self:
        print("new calling")
        return super().__new__(cls)

    def __init__(self) -> None:
        print("init calling")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("call calling")


if __name__ == "__main__":
    a = Test()
    print(a)
