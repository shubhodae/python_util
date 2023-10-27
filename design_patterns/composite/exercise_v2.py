import unittest
from collections.abc import Iterable, Iterator


class ValueContainer(Iterable):
    @property
    def sum(self) -> int:
        result = 0
        for c in self:
            for i in c:
                result += i
        return result


class SingleValue(ValueContainer):
    def __init__(self, value: int) -> None:
        self.value = value

    def __iter__(self) -> Iterator:
        yield self.value


class ManyValues(list, ValueContainer):
    pass


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
