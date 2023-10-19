from typing import List

class Shape:
    def __init__(self, length, breath):
        self._length = length
        self._breath = breath

    def get_length(self):
        return self._length
    def set_length(self, length):
        self._length = length

    def get_breath(self):
        return self._breath
    def set_breath(self, breath):
        self._breath = breath

    length = property(get_length, set_length)
    breath = property(get_breath, set_breath)


class Rectrangle(Shape):
    pass

class Square(Shape):

    def __init__(self, length):
        self._breath = length
        self._length = length

    def set_breath(self, breath):
        self._breath = breath
        self._length - breath

    def set_length(self, length):
        self._breath = length
        self._length = length


# Duck Type of Shape
class Box:

    def __init__(self, length, breath, height):
        self.length = length
        self.breath = breath
        self.height = height


class AreaCalculator:

    def calculate_area(self, shape_list: List[Shape]):
        for shape in shape_list:
            print(f"Area: {shape.length * shape.breath}")



r = Rectrangle(10, 5)
s = Square(10)
b = Box(10, 2, 5)


shape_list=[r, s, b]

ac = AreaCalculator()
ac.calculate_area(shape_list)