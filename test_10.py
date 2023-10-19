class Test:
    a = {"k": 10}

    def __init__(self) -> None:
        self.__dict__ = self.a
        self.b = 9

    def __str__(self) -> str:
        return f"a={self.a}, b={self.b}"


if __name__ == "__main__":
    o1 = Test()
    print(o1)

    o2 = Test()
    o2.a = {"k": 11}

    print(o1)
    print(o2)
