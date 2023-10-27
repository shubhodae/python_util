import unittest
from typing import Any


class SingleValue:
    def __init__(self, value: int) -> None:
        self.value = value


class ManyValues(list):
    @property
    def sum(self) -> int:
        sum = 0
        for item in self:
            if type(item) == SingleValue:
                sum += item.value
            elif type(item) == int:
                sum += item
            elif type(item) == ManyValues:
                sum += item.sum
        return sum


class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)
