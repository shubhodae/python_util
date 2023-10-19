from typing import List


class HtmlElement:
    indent_size: int = 2

    def __init__(self, name: str = "", text: str = "") -> None:
        self.name: str = name
        self.text: str = text
        self.elements: List[HtmlElement] = list()

    def __str(self, indent: int) -> str:
        lines: List[str] = list()
        i: str = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1: str = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self) -> str:
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name) -> None:
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_clild(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def add_clild_fluent(self, child_name, child_text):
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

    def __str__(self) -> str:
        return str(self.__root)


# builder = HtmlBuilder("ul")
builder = HtmlElement.create("ul")
# builder.add_clild("li", "hello")
# builder.add_clild("li", "world")
builder.add_clild_fluent("li", "hello").add_clild_fluent("li", "world")
print("Ordinary Builder:")
print(builder)
