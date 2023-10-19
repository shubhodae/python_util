from abc import ABC, abstractmethod


class HtmlElement:
    indent_size: int = 2

    def __init__(self, name: str = "", text: str = "") -> None:
        self.name: str = name
        self.text: str = text
        self.elements: list[HtmlElement] = []

    def __str(self, indent_count=0) -> str:
        lines: list[str] = []

        indent = " " * (indent_count * self.indent_size)
        lines.append(f"{indent}<{self.name}>")

        if self.text:
            next_indent = " " * ((indent_count + 1) * self.indent_size)
            lines.append(f"{next_indent}{self.text}")

        for element in self.elements:
            lines.append(element.__str(indent_count + 1))

        lines.append(f"{indent}</{self.name}>")

        return "\n".join(lines)

    def __str__(self) -> str:
        return f"{self.__str(0)}"

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class BuilderInterface(ABC):
    @abstractmethod
    def add_child(self, child_name: str, text: str) -> None:
        """Implement is child class"""

    @abstractmethod
    def add_child_fluent(self, child_name: str, text: str):
        """Implement in child class"""


class HtmlBuilder:
    def __init__(self, root_element: HtmlElement) -> None:
        self.root_element = root_element
        self.__root = HtmlElement(root_element)

    def add_child(self, child_name: str, child_text: str) -> None:
        self.__root.elements.append(HtmlElement(child_name, child_text))

    def add_child_fluent(self, child_name: str, child_text: str) -> BuilderInterface:
        self.__root.elements.append(HtmlElement(child_name, child_text))
        return self

    def __str__(self) -> str:
        return f"{self.__root}"


# builder = HtmlBuilder("ul")
builder = HtmlElement.create("ul")
# builder.add_child("li", "hello")
# builder.add_child("li", "world")
builder.add_child_fluent("li", "hello").add_child_fluent("li", "world")
print(builder)
