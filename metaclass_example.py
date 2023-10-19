# class Test:
#     pass


# def func():
#     pass


# print(type(Test))


class Foo:
    def show(self):
        print("hi")


def add_attribute(self):
    self.z = 9


Test = type("Test", (Foo,), {"x": 5, "add_attribute": add_attribute})
t = Test()
# t.wy = "hello"
# # print(t.wy)
# t.show()

t.add_attribute()
print(t.z)
