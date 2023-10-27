from typing_extensions import Self


class GraphicObject:
    def __init__(self, color: str = None) -> None:
        self.color = color
        self.children: list[Self] = []
        self._name: str = "Group"

    @property
    def name(self) -> str:
        return self._name

    def _print(self, items: list[Self], depth: int) -> None:
        items.append("*" * depth)
        if self.color:
            items.append(self.color)
        items.append(f"{self.name}\n")
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self) -> str:
        items: list[Self] = []
        self._print(items, 0)
        return "".join(items)


class Circle(GraphicObject):
    @property
    def name(self) -> str:
        return "Circle"


class Square(GraphicObject):
    @property
    def name(self) -> str:
        return "Square"


if __name__ == "__main__":
    drawing = GraphicObject()
    drawing._name = "My Drawing"
    drawing.children.append(Square("red"))
    drawing.children.append(Square("Yellow"))

    group = GraphicObject()
    group.children.append(Circle("Blue"))
    group.children.append(Square("Blue"))
    drawing.children.append(group)

    print(drawing)
