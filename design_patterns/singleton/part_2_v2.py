from typing import Any, Callable


def singleton(class_) -> Callable:
    instances: dict[Any, object] = {}

    def get_instance(*args, **kwargs) -> object:
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self) -> None:
        print("Loading database")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()

    print(d1 == d2)
