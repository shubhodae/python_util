class Undecorated:
    def get(self) -> None:
        return "I am undecorated object"


class Decorated:
    def __init__(self, undocorated_object: Undecorated) -> None:
        self.undocorated_object = undocorated_object

    def get(self):
        return self.undocorated_object.get().replace("undecorated", "decorated")


if __name__ == "__main__":
    uo = Undecorated()
    print(uo.get())

    do = Decorated(uo)
    print(do.get())
