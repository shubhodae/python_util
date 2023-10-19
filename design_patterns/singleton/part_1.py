from typing_extensions import Self
import random


class Database:
    _instance = None

    # def __init__(self) -> None:
    #     print("inside init")
    #     print(f"id = {random.randint(1, 101)}")

    def __new__(cls, *args, **kwargs) -> Self:
        # print("inside new")
        # print(f"id = {random.randint(1, 101)}")
        if not cls._instance:
            # cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()

    print(d1 == d2)
