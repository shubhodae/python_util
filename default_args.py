from typing import Optional


def foo(items: Optional[list[int]] = None):
    if None == items:
        items = []
    items.append(30)
    return items


def main() -> None:
    # items: list[int] = [90]

    print(foo())
    print(foo())


if __name__ == "__main__":
    main()
