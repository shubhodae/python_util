

class Parent1:
    my_var = "I am in one"
    my_first_var = "I am first"


class Parent2:
    my_var = "I am in two"
    my_second_var = "I am second"


class Child(Parent1, Parent2):

    def print_var(self):
        print(self.my_var)
        print(self.my_first_var)
        print(self.my_second_var)


if __name__ == "__main__":
    print("Hello World")

    obj = Child()
    obj.print_var()
