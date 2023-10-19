class CEO:
    __shared_stat = {"name": "Steve", "age": 55}

    def __init__(self) -> None:
        self.__dict__ = self.__shared_stat
        # self.__dict__ = {"name": "Steve", "age": 55}

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"


if __name__ == "__main__":
    ceo1 = CEO()
    print(ceo1)
    ceo2 = CEO()
    ceo2.name = "Xyz"
    print(ceo1)
    print(ceo2)

    print("-----------")
    print(id(ceo1))
    print(id(ceo2))
