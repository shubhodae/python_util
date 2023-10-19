from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def draw_point(p):
    print(".", end="")


@dataclass
class Line:
    start: Point
    end: Point


class Rectrangle(list):
    """Represented as a list of lines."""

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.append(Line(start=Point(x=x, y=y), end=Point(x=x + width, y=y)))
        self.append(
            Line(start=Point(x=x + width, y=y), end=Point(x=x + width, y=y + height))
        )
        self.append(Line(start=Point(x=x, y=y), end=Point(x=x, y=y + height)))
        self.append(
            Line(start=Point(x=x, y=y + height), end=Point(x=x + width, y=y + height))
        )


class LineToPointAdapter(list):
    count: int = 0

    def __init__(self, line: Line) -> None:
        super().__init__()
        self.count += 1
        print(
            f"{self.count}: Generating points for line "
            f"[{line.start.x},{line.start.y}]→"
            f"[{line.end.x},{line.end.y}]"
        )

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        if left - right == 0:
            for y in range(top, bottom):
                self.append(Point(x=left, y=y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x=x, y=top))


def draw(recs: list[Rectrangle]) -> None:
    print("\n\n----------- Drawing some stuff ------------------\n")
    for rc in recs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)


if __name__ == "__main__":
    rs = [Rectrangle(1, 1, 10, 10), Rectrangle(3, 3, 6, 6)]

    draw(rs)
    draw(rs)
