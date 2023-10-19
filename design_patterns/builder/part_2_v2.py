from typing import List


class HtmlElement:
    indent_size: int = 2

    def __init__(self, name: str = "", text: str = "") -> None:
        self.name: str = name
        self.text: str = text
        self.elements: List[HtmlElement] = list()

    def __str(self, indent_count: int = 0) -> str:
        lines: List[str] = list()
        indent: str = " " * (indent_count * self.indent_size)
        lines.append(f"{indent}<{self.name}>")

        if self.text:
            next_indent = " " * ((indent_count * self.indent_size) + self.indent_size)
            lines.append(f"{next_indent}{self.text}")

        for element in self.elements:
            lines.append(element.__str(indent_count + 1))

        lines.append(f"{indent}</{self.name}>")

        return "\n".join(lines)

    def __str__(self) -> str:
        return str(self.__str(0))


class HtmlBuilder:
    def __init__(self, root_name: str) -> None:
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, child_name: str, child_text: str) -> None:
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def __str__(self) -> str:
        return f"{self.__root}"


builder = HtmlBuilder("ul")
builder.add_child("li", "hello")
builder.add_child("li", "world")
print(builder)
