from typing import Any


class Singleton(type):
    _instance = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwds)
        return cls._instance[cls]


class Database(metaclass=Singleton):
    def __init__(self) -> None:
        print("Loading database")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()

    print(d1 == d2)
