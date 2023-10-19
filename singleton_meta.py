class SingletonMeta(type):
    __initialized_class_obj: dict[str, object] = {}

    def __new__(self, class_name, bases, attrs):
        if class_name not in self.__initialized_class_obj:
            self.__initialized_class_obj[class_name] = type(class_name, bases, attrs)
        return self.__initialized_class_obj[class_name]


class Test(metaclass=SingletonMeta):
    def __init__(self) -> None:
        print("Tesing init")

    def __str__(self) -> str:
        return "test str"


if __name__ == "__main__":
    o1 = Test()
    print(o1)

    o2 = Test()
    print(o2)

    print(o1 == o2)
