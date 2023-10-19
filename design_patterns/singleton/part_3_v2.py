from typing import Any


class Singleton(type):
    __instance: dict[Any:Any] = {}

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if self not in self.__instance:
            self.__instance[self] = super().__call__(*args, **kwds)
        return self.__instance[self]


class Database(metaclass=Singleton):
    pass


if __name__ == "__main__":
    db1 = Database()
    db2 = Database()

    print(id(db1))
    print(id(db2))
