from abc import ABC, abstractmethod
import enum


class HotDrink(ABC):
    @abstractmethod
    def consume(self) -> None:
        pass


class Tea(HotDrink):
    def consume(self) -> None:
        print("This tea is nice but I'd prefer it with milk.")


class Coffee(HotDrink):
    def consume(self) -> None:
        print("This coffee is delicious.")


class HotDrinksFactory(ABC):
    @abstractmethod
    def prepare(self, amount: float) -> HotDrink:
        pass


class TeaFactory(HotDrinksFactory):
    def prepare(self, amount: float) -> HotDrink:
        print(f"Put in a tea bag, boil water, pour {amount} ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinksFactory):
    def prepare(self, amount: float) -> HotDrink:
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
        return Coffee()


class HotDrinkMachine:
    class AvailableDrink(enum.Enum):
        COFFEE = enum.auto()
        TEA = enum.auto()

    factories: list[tuple[str, HotDrinksFactory]] = []
    initialized: bool = False

    def __init__(self) -> None:
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self) -> HotDrink:
        print("Available drink:")
        for f in self.factories:
            print(f[0])

        s = input(f"Please pick drink (0-{len(self.factories)-1}): ")
        idx = int(s)
        s = input("Specify amout: ")
        amount = float(s)
        return self.factories[idx][1].prepare(amount)


def make_drink(type: str) -> HotDrink:
    if type == "tea":
        return TeaFactory().prepare(200)
    elif type == "coffee":
        return CoffeeFactory().prepare(200)
    else:
        return None


if __name__ == "__main__":
    # entry = input("What kind of drink would you like?")
    # drink = make_drink(entry)
    # drink.consume()

    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()
