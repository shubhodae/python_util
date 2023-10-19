class Sum:
    def __call__(self, x: int, y: int) -> int:
        return x + y


if __name__ == "__main__":
    s = Sum()
    t = s(3, 4)
    print(t)
