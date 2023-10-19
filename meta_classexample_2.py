class Meta(type):
    def __new__(self, class_name, bases, attrs):
        # print(attrs)

        a = {}
        for item, value in attrs.items():
            if item.startswith("__"):
                a[item] = value
            else:
                a[item.upper()] = value
        # print(a)

        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print("hi")


d = Dog()
print(d.X)
d.HELLO()
