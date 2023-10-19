class GraphicObject:
    def __init__(self, color: str = None) -> None:
        self.color = color
        self.children: list[GraphicObject] = []
        self._name: str = "Group"

    @property
    def name(self) -> str:
        return self._name

    def _print(self, items: list["GraphicObject"], depth: int) -> None:
        items.append("*" * depth)
        if self.color:
            items.append(self.color)
        items.append(f"{self.name}\n")
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self) -> str:
        items: list["GraphicObject"] = []
        self._print(items, 0)
        return "".join(items)


class Square(GraphicObject):
    @property
    def name(self) -> str:
        return "Square"


class Circle(GraphicObject):
    @property
    def name(self) -> str:
        return "Circle"


if __name__ == "__main__":
    my_drawing = GraphicObject()
    my_drawing._name = "My Drawing"
    my_drawing.children.append(Square("red"))
    my_drawing.children.append(Square("yellow"))

    group = GraphicObject()
    group.children.append(Circle("Blue"))
    group.children.append(Square("Blue"))
    my_drawing.children.append(group)

    print(my_drawing)
