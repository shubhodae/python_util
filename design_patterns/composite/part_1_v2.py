class GraphicObject:
    def __init__(self, color: str = None) -> None:
        self.color = color
        self.children: list["GraphicObject"] = []
        self._name = "Group"

    @property
    def name(self) -> str:
        return self._name

    def _print(self, items: list["GraphicObject"], dept: int) -> None:
        items.append("*" * dept)
        if self.color:
            items.append(self.color)
        items.append(f"{self.name}\n")
        for child in self.children:
            child._print(items, dept + 1)

    def __str__(self) -> str:
        items: list["GraphicObject"] = []
        self._print(items, 0)
        return "".join(items)


class Square(GraphicObject):
    @property
    def name(self) -> str:
        return "Square"


class Cirlce(GraphicObject):
    @property
    def name(self) -> str:
        return "Circle"


if __name__ == "__main__":
    drawing = GraphicObject()
    drawing._name = "My Drawing"
    drawing.children.append(Square("red"))
    drawing.children.append(Square("yellow"))

    group = GraphicObject()
    group.children.append(Cirlce("Blue"))
    group.children.append(Square("Blue"))
    drawing.children.append(group)

    print(drawing)
