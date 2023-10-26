from typing import Any


class Stack:
    def __init__(self) -> None:
        self.elements: dict[int, Any] = {}
        self.currnet_position: int = 0

    def push(self, item: Any) -> "Stack":
        self.currnet_position += 1
        self.elements[self.currnet_position] = item
        return self

    def pop(self) -> Any:
        item = self.elements[self.currnet_position]
        del self.elements[self.currnet_position]
        self.currnet_position -= 1
        return item

    def __str__(self) -> str:
        items: list[Any] = []
        for position in range(1, self.currnet_position + 1):
            items.append(f"{self.elements[position]}")
        return " ".join(items)


def main() -> None:
    s = Stack()
    i = s.push(5).push(6).push(10).push(9).pop()
    print(i)
    print(s)


if __name__ == "__main__":
    main()
