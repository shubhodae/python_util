
def test_switch(value):
    match value:
        case 1:
            print("one")
        case 2:
            print("two")
        case _:
            print("else")


def main():
    print("Hello World")
    test_switch(4)


if __name__ == "__main__":
    main()
