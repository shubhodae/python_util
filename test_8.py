from typing import List, Protocol

d = {"a": 2, "b": 4, "c": 9, "d": 22}

var = 99


g = 999


class Item(Protocol):
    quantity: int
    price: float


class Product:
    def __init__(self, name: str, quantity: int, price: float) -> None:
        self.name = name
        self.quantity = quantity
        self.price = price


class Stock:
    def __init__(self, company_name: str, quantity: int, price: float) -> None:
        self.company_name = company_name
        self.quantity = quantity
        self.price = price


def calculate_total(items: List[Item]):
    return sum([item.quantity * item.price for item in items])


product_list = [
    Product("test 1", 2, 10),
    Product("test2", 5, 50),
]

stock_list = [
    Stock("company A", 100, 40),
    Stock("Company B", 150, 700)
]  # fmt: skip

total = calculate_total(product_list)
print(total)

total = calculate_total(stock_list)
print(total)
